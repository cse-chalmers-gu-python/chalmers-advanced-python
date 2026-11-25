def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""
    return sorted(names)[0]

assert first(["fish","dog","cat"]) == "cat"
assert first([]) == None # fails! 😔

