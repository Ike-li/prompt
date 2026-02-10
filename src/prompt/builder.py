"""
PromptBuilder - Core class for constructing prompts dynamically
"""

from typing import List, Dict, Any, Optional


class PromptBuilder:
    """
    A flexible builder class for constructing prompts for Large Language Models.
    
    Example:
        >>> builder = PromptBuilder()
        >>> builder.add_system("You are a helpful assistant.")
        >>> builder.add_user("What is the capital of France?")
        >>> prompt = builder.build()
    """
    
    def __init__(self):
        """Initialize an empty prompt builder."""
        self.messages: List[Dict[str, str]] = []
        self.context: Dict[str, Any] = {}
    
    def add_system(self, content: str) -> 'PromptBuilder':
        """
        Add a system message to the prompt.
        
        Args:
            content: The system message content
            
        Returns:
            Self for method chaining
        """
        self.messages.append({"role": "system", "content": content})
        return self
    
    def add_user(self, content: str) -> 'PromptBuilder':
        """
        Add a user message to the prompt.
        
        Args:
            content: The user message content
            
        Returns:
            Self for method chaining
        """
        self.messages.append({"role": "user", "content": content})
        return self
    
    def add_assistant(self, content: str) -> 'PromptBuilder':
        """
        Add an assistant message to the prompt.
        
        Args:
            content: The assistant message content
            
        Returns:
            Self for method chaining
        """
        self.messages.append({"role": "assistant", "content": content})
        return self
    
    def add_message(self, role: str, content: str) -> 'PromptBuilder':
        """
        Add a custom role message to the prompt.
        
        Args:
            role: The role of the message (e.g., "system", "user", "assistant")
            content: The message content
            
        Returns:
            Self for method chaining
        """
        self.messages.append({"role": role, "content": content})
        return self
    
    def set_context(self, key: str, value: Any) -> 'PromptBuilder':
        """
        Set a context variable that can be used in templates.
        
        Args:
            key: The context variable name
            value: The context variable value
            
        Returns:
            Self for method chaining
        """
        self.context[key] = value
        return self
    
    def clear(self) -> 'PromptBuilder':
        """
        Clear all messages and context.
        
        Returns:
            Self for method chaining
        """
        self.messages = []
        self.context = {}
        return self
    
    def build(self, format: str = "messages") -> Any:
        """
        Build the final prompt in the specified format.
        
        Args:
            format: Output format ("messages", "string", or "chat")
            
        Returns:
            The built prompt in the requested format
        """
        if format == "messages":
            return self.messages.copy()
        elif format == "string":
            return self._build_string()
        elif format == "chat":
            return self._build_chat_format()
        else:
            raise ValueError(f"Unknown format: {format}")
    
    def _build_string(self) -> str:
        """Build prompt as a single string."""
        parts = []
        for msg in self.messages:
            role = msg["role"].upper()
            content = msg["content"]
            parts.append(f"{role}: {content}")
        return "\n\n".join(parts)
    
    def _build_chat_format(self) -> Dict[str, List[Dict[str, str]]]:
        """Build prompt in chat API format."""
        return {"messages": self.messages.copy()}
    
    def __len__(self) -> int:
        """Return the number of messages in the prompt."""
        return len(self.messages)
    
    def __str__(self) -> str:
        """Return string representation of the prompt."""
        return self._build_string()
