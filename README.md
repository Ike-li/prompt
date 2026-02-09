# Prompt - 大模型提示词构建库

一个用于构建和管理大型语言模型（LLM）提示词的Python库。

A Python library for building and managing prompts for Large Language Models.

## 功能特性 (Features)

- 🔨 **PromptBuilder**: 灵活的提示词构建器，支持多种消息角色
- 📝 **PromptTemplate**: 可重用的提示词模板系统，支持变量替换
- 📚 **PromptLibrary**: 常用提示词模板集合
- 🎯 **类型安全**: 完整的类型注解支持
- ✅ **全面测试**: 30+ 单元测试，确保代码质量

## 安装 (Installation)

```bash
pip install -e .
```

## 快速开始 (Quick Start)

### 1. 使用 PromptBuilder 构建提示词

```python
from prompt import PromptBuilder

# 创建构建器
builder = PromptBuilder()

# 添加系统消息
builder.add_system("你是一个有帮助的AI助手。")

# 添加用户消息
builder.add_user("Python是什么？")

# 添加助手回复（用于few-shot示例）
builder.add_assistant("Python是一种高级编程语言。")

# 构建最终提示词
messages = builder.build("messages")
print(messages)
```

输出:
```python
[
    {"role": "system", "content": "你是一个有帮助的AI助手。"},
    {"role": "user", "content": "Python是什么？"},
    {"role": "assistant", "content": "Python是一种高级编程语言。"}
]
```

### 2. 使用链式调用

```python
from prompt import PromptBuilder

# 链式调用，构建完整对话
builder = (PromptBuilder()
    .add_system("你是一个Python专家。")
    .add_user("如何排序列表？")
    .add_assistant("使用 sorted() 函数或 .sort() 方法。")
    .add_user("有什么区别？"))

# 生成字符串格式的提示词
prompt_string = builder.build("string")
print(prompt_string)
```

### 3. 使用 PromptTemplate 创建模板

```python
from prompt import PromptTemplate

# 创建带变量的模板
template = PromptTemplate(
    "请将以下文本从{source_lang}翻译成{target_lang}：\n\n{text}\n\n翻译："
)

# 格式化模板
prompt = template.format(
    source_lang="英语",
    target_lang="中文",
    text="Hello, how are you?"
)

print(prompt)
```

输出:
```
请将以下文本从英语翻译成中文：

Hello, how are you?

翻译：
```

### 4. 使用预定义模板库

```python
from prompt import PromptTemplate
from prompt.template import PromptLibrary

# 问答模板
qa_template = PromptLibrary.question_answer()
prompt = qa_template.format(question="机器学习是什么？")

# 摘要模板
summary_template = PromptLibrary.summarization()
prompt = summary_template.format(text="长文本内容...")

# 代码生成模板
code_template = PromptLibrary.code_generation()
prompt = code_template.format(
    language="Python",
    task="实现快速排序算法"
)

# 分类模板
classify_template = PromptLibrary.classification()
prompt = classify_template.format(
    categories="积极, 消极, 中性",
    text="这个产品很棒！"
)
```

## API 文档 (API Documentation)

### PromptBuilder

**主要方法:**

- `add_system(content: str)` - 添加系统消息
- `add_user(content: str)` - 添加用户消息
- `add_assistant(content: str)` - 添加助手消息
- `add_message(role: str, content: str)` - 添加自定义角色消息
- `set_context(key: str, value: Any)` - 设置上下文变量
- `clear()` - 清除所有消息和上下文
- `build(format: str = "messages")` - 构建最终提示词
  - `format="messages"`: 返回消息列表
  - `format="string"`: 返回字符串格式
  - `format="chat"`: 返回聊天API格式

### PromptTemplate

**主要方法:**

- `format(**kwargs)` - 格式化模板，替换变量
- `get_variables()` - 获取模板中的所有变量
- `validate(**kwargs)` - 验证是否提供了所有必需变量

### PromptLibrary

**预定义模板:**

- `question_answer()` - 问答任务模板
- `summarization()` - 文本摘要模板
- `translation()` - 翻译任务模板
- `code_generation()` - 代码生成模板
- `classification()` - 分类任务模板

## 高级用法 (Advanced Usage)

### 模板变量验证

```python
from prompt import PromptTemplate

template = PromptTemplate("你好 {name}，今天{weather}")

# 获取所有变量
variables = template.get_variables()
print(variables)  # ['name', 'weather']

# 验证变量
is_valid = template.validate(name="张三")
print(is_valid)  # False (缺少 weather)

is_valid = template.validate(name="张三", weather="晴朗")
print(is_valid)  # True
```

### 设置默认值

```python
from prompt import PromptTemplate

# 创建带默认值的模板
template = PromptTemplate(
    "你好 {name}，今天{weather}",
    name="用户",
    weather="晴朗"
)

# 使用默认值
prompt = template.format()
print(prompt)  # "你好 用户，今天晴朗"

# 覆盖默认值
prompt = template.format(name="李四")
print(prompt)  # "你好 李四，今天晴朗"
```

### 不同输出格式

```python
from prompt import PromptBuilder

builder = PromptBuilder()
builder.add_system("系统").add_user("用户")

# 消息列表格式
messages = builder.build("messages")

# 字符串格式
string = builder.build("string")

# 聊天API格式
chat = builder.build("chat")
```

## 开发 (Development)

### 运行测试

```bash
# 安装开发依赖
pip install pytest pytest-cov

# 运行所有测试
pytest tests/ -v

# 运行测试并生成覆盖率报告
pytest tests/ --cov=src/prompt --cov-report=html
```

### 项目结构

```
prompt/
├── src/
│   └── prompt/
│       ├── __init__.py      # 包初始化
│       ├── builder.py       # PromptBuilder 类
│       └── template.py      # PromptTemplate 类
├── tests/
│   ├── __init__.py
│   ├── test_builder.py      # PromptBuilder 测试
│   └── test_template.py     # PromptTemplate 测试
├── README.md
├── pyproject.toml
└── requirements.txt
```

## 许可证 (License)

MIT License

## 贡献 (Contributing)

欢迎提交 Issue 和 Pull Request！

Welcome to submit Issues and Pull Requests!
