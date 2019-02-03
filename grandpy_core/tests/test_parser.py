import pytest
import sys

print(sys.path)
from grandpy_core.parser import delete_spaces, list_parsed

def parser(sentence):
    pass

def test_delete_spaces():
    assert delete_spaces("   je suis   ") == "je suis"

def test_list_parsed():
    splitted = ["je","cherche","l'église", "de", "Lille"]
    assert list_parsed(splitted) == "l'église Lille"

def test_parser_empty():
    with pytest.raises(AssertionError):
        list_parsed([])