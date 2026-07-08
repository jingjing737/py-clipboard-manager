# py-clipboard-manager 📋

剪贴板历史管理器，macOS/Windows/Linux 通用。

### 安装依赖

> ⚠️ **注意**：不要用 `pip3 install`，必须用 `python3 -m pip install` 确保装到正确的 Python 环境。

```bash
# 安装 pyperclip（跨平台剪贴板）
python3 -m pip install pyperclip
```

# 列出最近 10 条历史
python3 clipboard.py -l

# 复制第 3 条到剪贴板
python3 clipboard.py -c 3

# 清空历史
python3 clipboard.py -C
```

## 监听模式（自动保存）

```bash
# 启动监听，每次复制自动保存历史
python3 clipboard.py

# 列出历史
python3 clipboard.py -l -n 20
```

## 参数

| 参数 | 说明 |
|------|------|
| `-l, --list` | 列出历史 |
| `-c, --copy N` | 复制第 N 条到剪贴板 |
| `-C, --clear` | 清空历史 |
| `-n, --num N` | 列出数量 |

## 特性

- ✅ 自动保存剪贴板历史
- ✅ 去重（相同内容不重复）
- ✅ 支持 macOS/Windows/Linux
- ✅ 历史保存在 `~/.py-clipboard-history.json`

## License

MIT