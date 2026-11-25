def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""
    if names:
        return sorted(names)[0]

assert first(["fish","dog","cat"]) == "cat"
assert first([]) == None
assert first(["örn","älg","åsna"]) == "åsna" # fails! 🙄
