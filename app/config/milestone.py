from typing import List, TypedDict

class Milestone(TypedDict):
    accumulated_exp: int
    diamonds: int
    xp_potion: int

MILESTONE: List[Milestone] = [
    {"accumulated_exp": 0, "diamonds": 0, "xp_potion": 0},
    {"accumulated_exp": 500, "diamonds": 1, "xp_potion": 1},
    {"accumulated_exp": 1000, "diamonds": 2, "xp_potion": 2},
    {"accumulated_exp": 3000, "diamonds": 3, "xp_potion": 3},
    {"accumulated_exp": 12000, "diamonds": 5, "xp_potion": 5},
    {"accumulated_exp": 60000, "diamonds": 8, "xp_potion": 8},
    {"accumulated_exp": 360000, "diamonds": 12, "xp_potion": 12},
    {"accumulated_exp": 2520000, "diamonds": 20, "xp_potion": 20}
]