from typing import TypedDict, Literal

"""
Instead of a type alias dict[], we can inherit the `TypedDict` class
and give specific types to each of our record fields:
"""
class Person(TypedDict):
    name: str
    gender: Literal["male"] | Literal["female"] | Literal["other"]
    prize: str
    year: int
    birth: int
    death: int | None
    country: str

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
Compared to nobel.py, the definitions of these two
functions becomes simplified, since the type checker
can make stronger assertions about our values.
"""

def sort_winners_by_name(winners: list[Person]) -> None:
    winners.sort(key=lambda p: p["name"])

def winners_born_after(winners: list[Person], yob: int) -> list[Person]:
    return [w for w in winners if w["birth"] >= yob]
