"""
A type alias allows us to conveniently refer to a complex type annotation
A `Person` is a dictionary with:
  - keys of type `str`
  - values which are either:
    - of type `str`
    - of type `int`
    - the value `None`
"""
Person = dict[str, str | int | None]

"""
A list of `Person` values
"""
nobel_winners: list[Person] = [
    {
        "name": "Marie Curie",
        "gender": "female",
        "prize": "Nobel Prize in Chemistry",
        "year": 1911,
        "birth": 1867,
        "death": 1934,
        "country": "Poland"
    },
    {
        "name": "Kazuo Ishiguro",
        "gender": "male",
        "prize": "Nobel Prize in Literature",
        "year": 2017,
        "birth": 1954,
        "death": None,
        "country": "Japan"
    },
]

def count_winners(winners: list[Person]) -> int:
    """
    Count the number of winners. Takes as arguments:
    1. a list of `Person` values
    and returns:
    - an `int`
    """
    return len(winners)

def sort_winners_by_name(winners: list[Person]) -> None:
    """
    Sort winners alphabetically by name, in-place. Takes as arguments:
    1. a list of `Person` values
    """
    winners.sort(key=lambda p: str(p["name"]))

def winners_born_after(winners: list[Person], yob: int) -> list[Person]:
    """
    Find all winners born after a given date. Takes as arguments:
    1. a list of `Person` values
    2. a year of birth as `int`
    and returns:
    - a list of `Person` values
    """
    return [w for w in winners if type(w["birth"]) == int and w["birth"] >= yob]

def find_winner(winners: list[Person], name: str) -> Person | None:
    """
    Find a winner with the provided name. Takes as arguments:
    1. a list of `Person` values
    2. a name of type `str`
    and returns either:
    - a `Person` value
    - the value `None`
    """
    for w in winners:
        if w["name"] == name: return w
