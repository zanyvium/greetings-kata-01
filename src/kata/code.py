def greetings(name: str | None):
    if name:
        if name.isupper():
            return f"HELLO {name}!"
        else:
            return f"Hello, {name}."
    else:
        return "Hello, my friend."
