def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    order = {ch: i for i, ch in enumerate(alphabet)}
    if names:
        return sorted(names, key=lambda word: order.get(word[0], -1))[0]

assert first(["fish","dog","cat"]) == "cat"
assert first([]) == None
assert first(["örn","älg","åsna"]) == "åsna"

# now all bugs are fixed... right? 🥺
