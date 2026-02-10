"""
PromptTemplate - Template system for reusable prompts
"""

from typing import Dict, Any, Optional, List
import re


class PromptTemplate:
    """
    A template system for creating reusable prompts with variable substitution.
    
    Example:
        >>> template = PromptTemplate(
        ...     "Hello {name}, you have {count} messages.",
        ...     name="User",
        ...     count=5
        ... )
        >>> prompt = template.format()
        >>> print(prompt)
        Hello User, you have 5 messages.
    """
    
    def __init__(self, template: str, **defaults: Any):
        """
        Initialize a prompt template.
        
        Args:
            template: Template string with {variable} placeholders
            **defaults: Default values for template variables
        """
        self.template = template
        self.defaults = defaults
    
    def format(self, **kwargs: Any) -> str:
        """
        Format the template with the provided variables.
        
        Args:
            **kwargs: Variable values to substitute in the template
            
        Returns:
            The formatted prompt string
        """
        # Merge defaults with provided kwargs
        variables = {**self.defaults, **kwargs}
        
        try:
            return self.template.format(**variables)
        except KeyError as e:
            raise ValueError(f"Missing required template variable: {e}")
    
    def get_variables(self) -> List[str]:
        """
        Get all variable names in the template.
        
        Returns:
            List of variable names found in the template
        """
        # Find all {variable_name} patterns
        pattern = r'\{([^}]+)\}'
        matches = re.findall(pattern, self.template)
        return matches
    
    def validate(self, **kwargs: Any) -> bool:
        """
        Check if all required variables are provided.
        
        Args:
            **kwargs: Variable values to check
            
        Returns:
            True if all variables are satisfied, False otherwise
        """
        variables = {**self.defaults, **kwargs}
        required_vars = set(self.get_variables())
        provided_vars = set(variables.keys())
        return required_vars.issubset(provided_vars)
    
    def __str__(self) -> str:
        """Return the raw template string."""
        return self.template


class PromptLibrary:
    """
    A collection of commonly used prompt templates.
    """
    
    @staticmethod
    def question_answer() -> PromptTemplate:
        """
        Template for question-answering tasks.
        
        Returns:
            A PromptTemplate for Q&A
        """
        return PromptTemplate(
            "Please answer the following question:\n\nQuestion: {question}\n\nAnswer:"
        )
    
    @staticmethod
    def summarization() -> PromptTemplate:
        """
        Template for text summarization tasks.
        
        Returns:
            A PromptTemplate for summarization
        """
        return PromptTemplate(
            "Please summarize the following text:\n\n{text}\n\nSummary:"
        )
    
    @staticmethod
    def translation() -> PromptTemplate:
        """
        Template for translation tasks.
        
        Returns:
            A PromptTemplate for translation
        """
        return PromptTemplate(
            "Translate the following text from {source_lang} to {target_lang}:\n\n{text}\n\nTranslation:"
        )
    
    @staticmethod
    def code_generation() -> PromptTemplate:
        """
        Template for code generation tasks.
        
        Returns:
            A PromptTemplate for code generation
        """
        return PromptTemplate(
            "Generate {language} code for the following task:\n\n{task}\n\nCode:"
        )
    
    @staticmethod
    def classification() -> PromptTemplate:
        """
        Template for classification tasks.
        
        Returns:
            A PromptTemplate for classification
        """
        return PromptTemplate(
            "Classify the following text into one of these categories: {categories}\n\nText: {text}\n\nCategory:"
        )
