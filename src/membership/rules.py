"""
"""

from wheezy.validation.rules import length
from wheezy.validation.rules import required


password_rules = [required, length(min=8), length(max=12)]
