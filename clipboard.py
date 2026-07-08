#!/usr/bin/env python3
"""
py-clipboard-manager — 剪贴板历史管理器
支持：macOS/Windows/Linux，自动保存剪贴板历史
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime

# 跨平台剪贴板
try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False
    print("⚠️ 安装 pyperclip 以支持更多平台: pip3 install pyperclip")


HISTORY_FILE = os.path.expanduser("~/.py-clipboard-history.json")
MAX_ITEMS = 100


def load_history():
    """加载历史记录"""
    if os.path.isfile(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_history(history):
    """保存历史记录"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def get_clipboard():
    """获取当前剪贴板内容"""
    if HAS_PYPERCLIP:
        try:
            return pyperclip.paste()
        except:
            return None
    return None


def set_clipboard(text):
    """设置剪贴板内容"""
    if HAS_PYPERCLIP:
        try:
            pyperclip.copy(text)
            return True
        except:
            return False
    return False


def add_item(text: str):
    """添加新记录"""
    if not text or not text.strip():
        return

    history = load_history()

    # 去重（相同内容移到最前）
    for item in history:
        if item["content"] == text:
            history.remove(item)
            break

    # 添加新记录
    item = {
        "content": text[:5000],  # 限制长度
        "time": datetime.now().isoformat(),
        "preview": text[:100] + ("..." if len(text) > 100 else "")
    }
    history.insert(0, item)

    # 限制数量
    if len(history) > MAX_ITEMS:
        history = history[:MAX_ITEMS]

    save_history(history)


def list_history(limit: int = 10):
    """列出历史记录"""
    history = load_history()
    if not history:
        return "❌ 暂无剪贴板历史"

    lines = [f"剪贴板历史 (共 {len(history)} 条):", "=" * 50]
    for i, item in enumerate(history[:limit]):
        ts = item["time"][:19].replace("T", " ")
        lines.append(f"\n[{i+1}] {ts}")
        lines.append(f"    {item['preview']}")

    return "\n".join(lines)


def clear_history():
    """清空历史"""
    save_history([])
    return "✅ 已清空剪贴板历史"


def copy_item(index: int):
    """复制历史记录到剪贴板"""
    history = load_history()
    if 0 <= index < len(history):
        text = history[index]["content"]
        if set_clipboard(text):
            return f"✅ 已复制第 {index+1} 条到剪贴板"
        return "❌ 复制失败"
    return "❌ 索引不存在"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="剪贴板历史管理器")
    parser.add_argument("-l", "--list", action="store_true", help="列出历史")
    parser.add_argument("-c", "--copy", type=int, metavar="N", help="复制第 N 条到剪贴板")
    parser.add_argument("-C", "--clear", action="store_true", help="清空历史")
    parser.add_argument("-n", "--num", type=int, default=10, help="列出数量")
    args = parser.parse_args()

    if args.list:
        print(list_history(args.num))
    elif args.copy:
        print(copy_item(args.copy - 1))
    elif args.clear:
        print(clear_history())
    else:
        # 监听模式（需安装 pyperclip）
        if not HAS_PYPERCLIP:
            print("❌ 监听模式需要 pyperclip: pip3 install pyperclip")
            sys.exit(1)

        print("📋 剪贴板监听模式已启动 (Ctrl+C 退出)")
        print("每次剪贴板内容变化会自动保存...")

        last_content = get_clipboard()
        while True:
            time.sleep(1)
            current = get_clipboard()
            if current and current != last_content:
                add_item(current)
                print(f"✅ 已保存: {current[:50]}...")
                last_content = current