def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""

    # Version 1: wrong index 1
    # return sorted(names)[1] # 🐞 1

    # Version 2: doesn't handle empty list
    # return sorted(names)[0] # 🐞 2

    # Version 3: doesn't sort å ä ö correctly
    if names:
        return sorted(names)[0]

assert first(["fish","dog","cat"]) == "cat"
assert first([]) == None
assert first(["örn","älg","åsna"]) == "älg"
