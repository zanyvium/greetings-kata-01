def _make_stand_in_greeting() -> str:
    return "Hello, my friend."


def _make_greetings_for_single_name(name: str | None) -> str:
    if name:
        if name.isupper():
            return f"HELLO {name}!"
        else:
            return f"Hello, {name}."
    else:
        return _make_stand_in_greeting()


def greetings(names: list[str | None] | str | None) -> str:
    if isinstance(names, list):
        if len(names) == 0:
            return_string = _make_stand_in_greeting()
        if len(names) == 1:
            return_string = _make_greetings_for_single_name(names[0])
        else:
            return_string = "Hello, " + " and ".join(name for name in names) + "."
    else:
        return_string = _make_greetings_for_single_name(names)
    return return_string
