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

"""
A function which takes as arguments:
1. a list of `Person` values
2. a name of type `str`
and returns either:
- a `Person` value
- the value `None`
"""
def find_winner(winners: list[Person], name: str) -> Person | None:
    for w in winners:
        if w["name"] == name: return w
