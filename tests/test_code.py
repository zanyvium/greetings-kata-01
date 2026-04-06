from src.kata.code import greetings


def test_single_greeting():
    name = "Bob"
    assert greetings(name) == f"Hello, {name}."
