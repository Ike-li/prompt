#!/usr/bin/env python
"""
示例代码：演示 Prompt 库的使用方法
Examples demonstrating the usage of the Prompt library
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from prompt import PromptBuilder, PromptTemplate
from prompt.template import PromptLibrary


def example_1_basic_builder():
    """示例1：基础 PromptBuilder 用法"""
    print("=" * 60)
    print("示例1: 基础 PromptBuilder 用法")
    print("Example 1: Basic PromptBuilder Usage")
    print("=" * 60)
    
    builder = PromptBuilder()
    builder.add_system("你是一个有帮助的AI助手。")
    builder.add_user("Python是什么？")
    
    messages = builder.build("messages")
    print("\n消息格式 (Messages format):")
    for msg in messages:
        print(f"  {msg}")
    
    print("\n字符串格式 (String format):")
    print(builder.build("string"))
    print()


def example_2_method_chaining():
    """示例2：方法链式调用"""
    print("=" * 60)
    print("示例2: 方法链式调用")
    print("Example 2: Method Chaining")
    print("=" * 60)
    
    builder = (PromptBuilder()
        .add_system("你是一个Python专家。")
        .add_user("如何排序列表？")
        .add_assistant("使用 sorted() 函数或 .sort() 方法。")
        .add_user("有什么区别？"))
    
    print("\n构建的对话:")
    print(builder.build("string"))
    print()


def example_3_template_basic():
    """示例3：基础模板用法"""
    print("=" * 60)
    print("示例3: 基础模板用法")
    print("Example 3: Basic Template Usage")
    print("=" * 60)
    
    template = PromptTemplate(
        "请将以下文本从{source_lang}翻译成{target_lang}：\n\n{text}\n\n翻译："
    )
    
    prompt = template.format(
        source_lang="英语",
        target_lang="中文",
        text="Hello, how are you?"
    )
    
    print("\n生成的提示词:")
    print(prompt)
    print()


def example_4_template_library():
    """示例4：使用预定义模板库"""
    print("=" * 60)
    print("示例4: 使用预定义模板库")
    print("Example 4: Using Template Library")
    print("=" * 60)
    
    # 问答模板
    print("\n1. 问答模板 (Question-Answer Template):")
    qa_template = PromptLibrary.question_answer()
    print(qa_template.format(question="机器学习是什么？"))
    
    # 摘要模板
    print("\n2. 摘要模板 (Summarization Template):")
    summary_template = PromptLibrary.summarization()
    print(summary_template.format(text="这是一段需要总结的长文本..."))
    
    # 代码生成模板
    print("\n3. 代码生成模板 (Code Generation Template):")
    code_template = PromptLibrary.code_generation()
    print(code_template.format(
        language="Python",
        task="实现快速排序算法"
    ))
    
    # 分类模板
    print("\n4. 分类模板 (Classification Template):")
    classify_template = PromptLibrary.classification()
    print(classify_template.format(
        categories="积极, 消极, 中性",
        text="这个产品很棒！"
    ))
    print()


def example_5_template_validation():
    """示例5：模板变量验证"""
    print("=" * 60)
    print("示例5: 模板变量验证")
    print("Example 5: Template Variable Validation")
    print("=" * 60)
    
    template = PromptTemplate("你好 {name}，今天{weather}")
    
    # 获取变量
    variables = template.get_variables()
    print(f"\n模板变量: {variables}")
    
    # 验证
    print(f"验证(只有name): {template.validate(name='张三')}")
    print(f"验证(name和weather): {template.validate(name='张三', weather='晴朗')}")
    
    # 使用默认值
    template_with_defaults = PromptTemplate(
        "你好 {name}，今天{weather}",
        name="用户",
        weather="晴朗"
    )
    print(f"\n使用默认值: {template_with_defaults.format()}")
    print(f"覆盖默认值: {template_with_defaults.format(name='李四')}")
    print()


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("Prompt 库使用示例")
    print("Prompt Library Usage Examples")
    print("=" * 60 + "\n")
    
    example_1_basic_builder()
    example_2_method_chaining()
    example_3_template_basic()
    example_4_template_library()
    example_5_template_validation()
    
    print("=" * 60)
    print("所有示例运行完成！")
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
