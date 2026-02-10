"""Tests for PromptBuilder class."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from prompt.builder import PromptBuilder


def test_prompt_builder_init():
    """Test PromptBuilder initialization."""
    builder = PromptBuilder()
    assert len(builder) == 0
    assert builder.messages == []
    assert builder.context == {}


def test_add_system_message():
    """Test adding system messages."""
    builder = PromptBuilder()
    builder.add_system("You are a helpful assistant.")
    
    assert len(builder) == 1
    assert builder.messages[0]["role"] == "system"
    assert builder.messages[0]["content"] == "You are a helpful assistant."


def test_add_user_message():
    """Test adding user messages."""
    builder = PromptBuilder()
    builder.add_user("What is Python?")
    
    assert len(builder) == 1
    assert builder.messages[0]["role"] == "user"
    assert builder.messages[0]["content"] == "What is Python?"


def test_add_assistant_message():
    """Test adding assistant messages."""
    builder = PromptBuilder()
    builder.add_assistant("Python is a programming language.")
    
    assert len(builder) == 1
    assert builder.messages[0]["role"] == "assistant"
    assert builder.messages[0]["content"] == "Python is a programming language."


def test_method_chaining():
    """Test method chaining for fluent API."""
    builder = PromptBuilder()
    result = builder.add_system("System").add_user("User").add_assistant("Assistant")
    
    assert result is builder
    assert len(builder) == 3
    assert builder.messages[0]["role"] == "system"
    assert builder.messages[1]["role"] == "user"
    assert builder.messages[2]["role"] == "assistant"


def test_add_custom_message():
    """Test adding custom role messages."""
    builder = PromptBuilder()
    builder.add_message("custom_role", "Custom content")
    
    assert len(builder) == 1
    assert builder.messages[0]["role"] == "custom_role"
    assert builder.messages[0]["content"] == "Custom content"


def test_set_context():
    """Test setting context variables."""
    builder = PromptBuilder()
    builder.set_context("key1", "value1")
    builder.set_context("key2", 42)
    
    assert builder.context["key1"] == "value1"
    assert builder.context["key2"] == 42


def test_clear():
    """Test clearing messages and context."""
    builder = PromptBuilder()
    builder.add_system("System").add_user("User")
    builder.set_context("key", "value")
    
    assert len(builder) == 2
    assert len(builder.context) == 1
    
    builder.clear()
    
    assert len(builder) == 0
    assert len(builder.context) == 0


def test_build_messages_format():
    """Test building prompt in messages format."""
    builder = PromptBuilder()
    builder.add_system("System message")
    builder.add_user("User message")
    
    result = builder.build("messages")
    
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"role": "system", "content": "System message"}
    assert result[1] == {"role": "user", "content": "User message"}


def test_build_string_format():
    """Test building prompt in string format."""
    builder = PromptBuilder()
    builder.add_system("System message")
    builder.add_user("User message")
    
    result = builder.build("string")
    
    assert isinstance(result, str)
    assert "SYSTEM: System message" in result
    assert "USER: User message" in result


def test_build_chat_format():
    """Test building prompt in chat format."""
    builder = PromptBuilder()
    builder.add_system("System message")
    builder.add_user("User message")
    
    result = builder.build("chat")
    
    assert isinstance(result, dict)
    assert "messages" in result
    assert len(result["messages"]) == 2


def test_build_invalid_format():
    """Test building prompt with invalid format raises error."""
    builder = PromptBuilder()
    builder.add_user("Test")
    
    try:
        builder.build("invalid_format")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Unknown format" in str(e)


def test_str_representation():
    """Test string representation of builder."""
    builder = PromptBuilder()
    builder.add_system("System")
    builder.add_user("User")
    
    result = str(builder)
    
    assert "SYSTEM: System" in result
    assert "USER: User" in result


def test_len():
    """Test len() function on builder."""
    builder = PromptBuilder()
    assert len(builder) == 0
    
    builder.add_system("Test")
    assert len(builder) == 1
    
    builder.add_user("Test")
    assert len(builder) == 2
