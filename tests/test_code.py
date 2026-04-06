from src.kata.code import greetings


def test_single_greeting():
    name = "Bob"
    assert greetings(name) == f"Hello, {name}."


def test_stand_in_for_null():
    name = ""
    assert greetings(name) == "Hello, my friend."
