"""Shieldhood - AI Security Layer for Bankr.bot"""

from .guard import Shieldhood

__version__ = "2.0.0"
__author__ = "Laramée Line"
__all__ = ["Shieldhood"]

# Make it easy to import
__version__ = Shieldhood.__module__  # just for reference
