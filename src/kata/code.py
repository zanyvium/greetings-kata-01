def _make_stand_in_greeting() -> str:
    return_string = "Hello, my friend."
    return return_string


def _make_greetings_for_single_name(name: str | None) -> str:
    if name:
        if name.isupper():
            return_string = f"HELLO {name}!"
        else:
            return_string = f"Hello, {name}."
    else:
        return_string = _make_stand_in_greeting()
    return return_string


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
