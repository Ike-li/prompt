"""
Prompt - A Python library for building and managing prompts for Large Language Models
"""

from .builder import PromptBuilder
from .template import PromptTemplate

__version__ = "0.1.0"
__all__ = ["PromptBuilder", "PromptTemplate"]
