def greetings(name: str | None):
    if name:
        return f"Hello, {name}."
    else:
        return "Hello, my friend."
