import pytest
from calc.evaluation import evaluate
from parser.parser import sympify


def test_evaluate():
    """Test primitive expression"""
    expr = evaluate("350*150")
    answer = sympify("52500")
    assert expr == answer
