# doc-annotator

**统一文档智能注释器** — Claude Code 通用技能

自动识别文件类型 → 转为可读文本 → LLM 理解分析 → 产出对应注释

## 支持的文件类型

| 类型 | 格式 | 注释产物 |
|------|------|---------|
| 演示文稿 | `.pptx` `.ppt` | 演讲备注（注入 PPT）+ 排练文档 |
| PDF 论文 | `.pdf` | 阅读笔记（摘要/方法/图表/评价） |
| Word 文档 | `.docx` `.doc` `.epub` | 章节摘要 + 关键术语表 |
| Excel 表格 | `.xlsx` `.xls` `.csv` | 数据解读 + 趋势标注 |
| 音频录音 | `.mp3` `.wav` `.m4a` `.ogg` | 会议纪要 / 转录要点 |
| 网页 | `.html` `.htm` URL | 内容摘要 + 要点提炼 |
| YouTube | URL | 视频摘要 + 时间线 |
| Jupyter | `.ipynb` | 代码逻辑解读 |
| 纯文本 | `.txt` `.md` `.json` | 关键提炼 |

## 快速安装

### 1. 克隆到 Claude Code 技能目录

```bash
git clone https://github.com/fyz2025/doc-annotator.git ~/.claude/skills/doc-annotator/
```

### 2. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

或使用已有的 markitdown 虚拟环境（推荐）：

```bash
# 设置环境变量指向你的 markitdown venv
export DOC_ANNOTATOR_VENV="E:/Projects/技能/markitdown 文本转换/.venv"
```

### 3. 重启 Claude Code 会话

技能会被自动加载，在可用技能列表中显示为 `doc-annotator`。

## 使用方式

在 Claude Code 对话中直接说：

- "帮我给这个 PPT 生成演讲注释" + 拖入文件
- "Summarize this PDF paper" + 拖入文件
- "分析这个 Excel 表格数据"
- "把这段会议录音转成纪要"

LLM 会自动调用 `doc-annotator` 技能完成文件转换、理解和注释生成。

## 项目结构

```
doc-annotator/
├── SKILL.md                    # 技能定义（Claude Code 入口）
├── README.md                   # 本文件
├── requirements.txt            # Python 依赖
├── .gitignore
└── scripts/
    ├── convert.py              # 统一文件转 Markdown
    ├── inject_pptx_notes.py    # PPTX 备注注入
    ├── write_docx_notes.py     # DOCX 注释写入
    ├── write_md_notes.py       # Markdown 注释生成
    └── utils.py                # 共享工具
```

## 依赖

- [markitdown](https://github.com/microsoft/markitdown) — 文件转 Markdown 引擎
- python-pptx — PPTX 读写
- python-docx — DOCX 读写
- pdfplumber / pdfminer.six — PDF 解析
- openpyxl — Excel 解析
- SpeechRecognition + pydub — 音频转录
- youtube-transcript-api — YouTube 字幕

## License

MIT
