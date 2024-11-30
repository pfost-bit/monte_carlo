"""
monte_carlo

This package provides tools for running Monte Carlo simulations, including components for handling dice, games, and analysis.

Modules:
    - die: Contains the Die class for simulating dice rolls.
    - game: Contains the Game class for managing dice games.
    - analyzer: Contains the Analyzer class for analyzing game results.
"""

from .die import Die
from .game import Game
from .analyzer import Analyzer

__all__ = ['Die', 'Game', 'Analyzer']

def monte_carlo_help():
    """
    Display help information for all classes in the monte_carlo package.
    """
    help(Die)
    help(Game)
    help(Analyzer)

# Customize the help function for the package
def __dir__():
    return __all__

def __getattr__(name):
    if name == 'help':
        return monte_carlo_help
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

