"""Tests for PromptTemplate class."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from prompt.template import PromptTemplate, PromptLibrary


def test_template_init():
    """Test PromptTemplate initialization."""
    template = PromptTemplate("Hello {name}")
    assert template.template == "Hello {name}"
    assert template.defaults == {}


def test_template_with_defaults():
    """Test PromptTemplate with default values."""
    template = PromptTemplate("Hello {name}", name="World")
    assert template.defaults["name"] == "World"


def test_template_format():
    """Test formatting a template."""
    template = PromptTemplate("Hello {name}, you are {age} years old.")
    result = template.format(name="Alice", age=30)
    assert result == "Hello Alice, you are 30 years old."


def test_template_format_with_defaults():
    """Test formatting with default values."""
    template = PromptTemplate("Hello {name}", name="World")
    result = template.format()
    assert result == "Hello World"


def test_template_format_override_defaults():
    """Test overriding default values."""
    template = PromptTemplate("Hello {name}", name="World")
    result = template.format(name="Alice")
    assert result == "Hello Alice"


def test_template_format_missing_variable():
    """Test formatting with missing required variable."""
    template = PromptTemplate("Hello {name}")
    try:
        template.format()
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Missing required template variable" in str(e)


def test_get_variables():
    """Test getting all variables from template."""
    template = PromptTemplate("Hello {name}, your score is {score}")
    variables = template.get_variables()
    assert "name" in variables
    assert "score" in variables
    assert len(variables) == 2


def test_validate_with_all_variables():
    """Test validate returns True when all variables provided."""
    template = PromptTemplate("Hello {name}")
    assert template.validate(name="Alice")


def test_validate_with_missing_variables():
    """Test validate returns False when variables missing."""
    template = PromptTemplate("Hello {name}, you are {age}")
    assert not template.validate(name="Alice")


def test_validate_with_defaults():
    """Test validate with default values."""
    template = PromptTemplate("Hello {name}", name="World")
    assert template.validate()


def test_template_str():
    """Test string representation of template."""
    template = PromptTemplate("Hello {name}")
    assert str(template) == "Hello {name}"


def test_question_answer_template():
    """Test question-answer template from library."""
    template = PromptLibrary.question_answer()
    result = template.format(question="What is Python?")
    assert "What is Python?" in result
    assert "Question:" in result
    assert "Answer:" in result


def test_summarization_template():
    """Test summarization template from library."""
    template = PromptLibrary.summarization()
    result = template.format(text="Long text here")
    assert "Long text here" in result
    assert "summarize" in result.lower()


def test_translation_template():
    """Test translation template from library."""
    template = PromptLibrary.translation()
    result = template.format(
        source_lang="English",
        target_lang="Chinese",
        text="Hello"
    )
    assert "English" in result
    assert "Chinese" in result
    assert "Hello" in result


def test_code_generation_template():
    """Test code generation template from library."""
    template = PromptLibrary.code_generation()
    result = template.format(
        language="Python",
        task="Sort a list"
    )
    assert "Python" in result
    assert "Sort a list" in result


def test_classification_template():
    """Test classification template from library."""
    template = PromptLibrary.classification()
    result = template.format(
        categories="positive, negative, neutral",
        text="I love this product"
    )
    assert "positive, negative, neutral" in result
    assert "I love this product" in result
