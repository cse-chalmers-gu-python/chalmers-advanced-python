# A pure function which can be tested with input/output pairs.
def take(n: int, s: str) -> str:
    return s[:n]

#             Inputs         Output
#           -----------     --------
assert take( 3, "hello") == "hel"
assert take( 0, "hello") == ""
assert take(20, "hello") == "hello"


# A function with side effects needs to be tested differently.
def save(path: str, text: str) -> None:
    if text:
        with open(path, "w") as f:
            f.write(text)
    else:
        print("Missing text")

# what needs to be checked in each of these cases?
save("test1.txt", "hello")  # file written correctly
save("test2.txt", "")       # message printed to console
save(":/", "hello")         # exception raised (invalid path)
