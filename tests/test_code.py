from src.kata.code import greetings


def test_single_greeting():
    name = "Bob"
    assert greetings(name) == f"Hello, {name}."


def test_stand_in_for_null():
    name = ""
    assert greetings(name) == "Hello, my friend."


def test_shouting():
    name = "JERRY"
    assert greetings(name) == f"HELLO {name}!"


def test_two_lower_case_names():
    names = ["Jill", "Jane"]
    assert greetings(names) == f"Hello {names[0]} and {names[1]}."
