def take(n: int, s: str) -> str:
    return s[:n]

# Some of these expresions are type-correct, and others aren't

take(3, "hello") # correct
take("h", "hello") # incorrect, first argument should be int
take(2, ["hello"]) # incorrect, second argument should be str
take(3, "hello") + "icopter" # correct, but warning about unused value
take(3, "hello").append("icopter") # incorrect, return type str doesn't support .append()

