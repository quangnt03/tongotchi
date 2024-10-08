from typing import TypedDict, List


class Level(TypedDict):
    level: int
    exp: int
    diamonds: int
    tickets: int
    evolution: int
    egg: int


LEVEL_REWARD: List[Level] = [
    {"level": 0, "exp": 0, "diamonds": 0, "tickets": 0, "evolution": 0, "egg": 0},
    {"level": 1, "exp": 25, "diamonds": 0, "tickets": 50, "evolution": 0, "egg": 0},
    {"level": 2, "exp": 56, "diamonds": 0, "tickets": 50, "evolution": 0, "egg": 0},
    {"level": 3, "exp": 92, "diamonds": 0, "tickets": 50, "evolution": 0, "egg": 0},
    {"level": 4, "exp": 133, "diamonds": 0, "tickets": 50, "evolution": 0, "egg": 0},
    {"level": 5, "exp": 181, "diamonds": 0, "tickets": 50, "evolution": 0, "egg": 0},
    {"level": 6, "exp": 236, "diamonds": 0, "tickets": 100, "evolution": 0, "egg": 0},
    {"level": 7, "exp": 299, "diamonds": 0, "tickets": 100, "evolution": 0, "egg": 0},
    {"level": 8, "exp": 370, "diamonds": 0, "tickets": 100, "evolution": 0, "egg": 0},
    {"level": 9, "exp": 449, "diamonds": 0, "tickets": 100, "evolution": 0, "egg": 0},
    {"level": 10, "exp": 538, "diamonds": 0, "tickets": 100, "evolution": 0, "egg": 0},
    {"level": 11, "exp": 636, "diamonds": 0, "tickets": 300, "evolution": 0, "egg": 0},
    {"level": 12, "exp": 745, "diamonds": 0, "tickets": 300, "evolution": 0, "egg": 0},
    {"level": 13, "exp": 864, "diamonds": 0, "tickets": 300, "evolution": 0, "egg": 0},
    {"level": 14, "exp": 994, "diamonds": 0, "tickets": 300, "evolution": 0, "egg": 0},
    {"level": 15, "exp": 1136, "diamonds": 1, "tickets": 0, "evolution": 1, "egg": 0},
    {"level": 16, "exp": 1289, "diamonds": 0, "tickets": 300, "evolution": 1, "egg": 0},
    {"level": 17, "exp": 1455, "diamonds": 0, "tickets": 435, "evolution": 1, "egg": 0},
    {"level": 18, "exp": 1633, "diamonds": 0, "tickets": 435, "evolution": 1, "egg": 0},
    {"level": 19, "exp": 1824, "diamonds": 0, "tickets": 435, "evolution": 1, "egg": 0},
    {"level": 20, "exp": 2028, "diamonds": 1, "tickets": 0, "evolution": 1, "egg": 0},
    {"level": 21, "exp": 2246, "diamonds": 0, "tickets": 435, "evolution": 1, "egg": 0},
    {"level": 22, "exp": 2478, "diamonds": 0, "tickets": 570, "evolution": 1, "egg": 0},
    {"level": 23, "exp": 2724, "diamonds": 0, "tickets": 570, "evolution": 1, "egg": 0},
    {"level": 24, "exp": 2985, "diamonds": 0, "tickets": 570, "evolution": 1, "egg": 0},
    {"level": 25, "exp": 3260, "diamonds": 2, "tickets": 0, "evolution": 2, "egg": 1},
    {"level": 26, "exp": 3551, "diamonds": 0, "tickets": 570, "evolution": 2, "egg": 0},
    {"level": 27, "exp": 3857, "diamonds": 0, "tickets": 570, "evolution": 2, "egg": 0},
    {"level": 28, "exp": 4179, "diamonds": 0, "tickets": 705, "evolution": 2, "egg": 0},
    {"level": 29, "exp": 4517, "diamonds": 0, "tickets": 705, "evolution": 2, "egg": 0},
    {"level": 30, "exp": 4871, "diamonds": 2, "tickets": 0, "evolution": 2, "egg": 0},
    {"level": 31, "exp": 5242, "diamonds": 0, "tickets": 705, "evolution": 2, "egg": 0},
    {"level": 32, "exp": 5630, "diamonds": 0, "tickets": 705, "evolution": 2, "egg": 0},
    {"level": 33, "exp": 6035, "diamonds": 0, "tickets": 705, "evolution": 2, "egg": 0},
    {"level": 34, "exp": 6457, "diamonds": 0, "tickets": 840, "evolution": 2, "egg": 0},
    {"level": 35, "exp": 6897, "diamonds": 3, "tickets": 0, "evolution": 2, "egg": 0},
    {"level": 36, "exp": 7354, "diamonds": 0, "tickets": 840, "evolution": 2, "egg": 0},
    {"level": 37, "exp": 7830, "diamonds": 0, "tickets": 840, "evolution": 3, "egg": 1},
    {"level": 38, "exp": 8324, "diamonds": 0, "tickets": 840, "evolution": 3, "egg": 0},
    {"level": 39, "exp": 8837, "diamonds": 0, "tickets": 840, "evolution": 3, "egg": 0},
    {"level": 40, "exp": 9368, "diamonds": 3, "tickets": 0, "evolution": 3, "egg": 0},
    {"level": 41, "exp": 9919, "diamonds": 0, "tickets": 975, "evolution": 3, "egg": 0},
    {
        "level": 42,
        "exp": 10489,
        "diamonds": 0,
        "tickets": 975,
        "evolution": 3,
        "egg": 0,
    },
    {
        "level": 43,
        "exp": 11078,
        "diamonds": 0,
        "tickets": 975,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 44,
        "exp": 11687,
        "diamonds": 0,
        "tickets": 975,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 45, "exp": 12316, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 46,
        "exp": 12965,
        "diamonds": 0,
        "tickets": 975,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 47,
        "exp": 13635,
        "diamonds": 0,
        "tickets": 1110,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 48,
        "exp": 14326,
        "diamonds": 0,
        "tickets": 1110,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 49,
        "exp": 15037,
        "diamonds": 0,
        "tickets": 1110,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 50, "exp": 15770, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 51,
        "exp": 16524,
        "diamonds": 0,
        "tickets": 1110,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 52,
        "exp": 17299,
        "diamonds": 0,
        "tickets": 1110,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 53,
        "exp": 18096,
        "diamonds": 0,
        "tickets": 1245,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 54,
        "exp": 18915,
        "diamonds": 0,
        "tickets": 1245,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 55, "exp": 19756, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 56,
        "exp": 20620,
        "diamonds": 0,
        "tickets": 1245,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 57,
        "exp": 21506,
        "diamonds": 0,
        "tickets": 1245,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 58,
        "exp": 22415,
        "diamonds": 0,
        "tickets": 1245,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 59,
        "exp": 23347,
        "diamonds": 0,
        "tickets": 1380,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 60, "exp": 24302, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 61,
        "exp": 25280,
        "diamonds": 0,
        "tickets": 1380,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 62,
        "exp": 26282,
        "diamonds": 0,
        "tickets": 1380,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 63,
        "exp": 27308,
        "diamonds": 0,
        "tickets": 1380,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 64,
        "exp": 28357,
        "diamonds": 0,
        "tickets": 1380,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 65, "exp": 29431, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 66,
        "exp": 30529,
        "diamonds": 0,
        "tickets": 1515,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 67,
        "exp": 31651,
        "diamonds": 0,
        "tickets": 1515,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 68,
        "exp": 32798,
        "diamonds": 0,
        "tickets": 1515,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 69,
        "exp": 33970,
        "diamonds": 0,
        "tickets": 1515,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 70, "exp": 35167, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 71,
        "exp": 36389,
        "diamonds": 0,
        "tickets": 1515,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 72,
        "exp": 37636,
        "diamonds": 0,
        "tickets": 1920,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 73,
        "exp": 38909,
        "diamonds": 0,
        "tickets": 1920,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 74,
        "exp": 40208,
        "diamonds": 0,
        "tickets": 1920,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 75, "exp": 41533, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 76,
        "exp": 42884,
        "diamonds": 0,
        "tickets": 1920,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 77,
        "exp": 44261,
        "diamonds": 0,
        "tickets": 1920,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 78,
        "exp": 45664,
        "diamonds": 0,
        "tickets": 2325,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 79,
        "exp": 47094,
        "diamonds": 0,
        "tickets": 2325,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 80, "exp": 48551, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 81,
        "exp": 50034,
        "diamonds": 0,
        "tickets": 2325,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 82,
        "exp": 51545,
        "diamonds": 0,
        "tickets": 2325,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 83,
        "exp": 53083,
        "diamonds": 0,
        "tickets": 2325,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 84,
        "exp": 54648,
        "diamonds": 0,
        "tickets": 2730,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 85, "exp": 56241, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 86,
        "exp": 57862,
        "diamonds": 0,
        "tickets": 2730,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 87,
        "exp": 59510,
        "diamonds": 0,
        "tickets": 2730,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 88,
        "exp": 61187,
        "diamonds": 0,
        "tickets": 2730,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 89,
        "exp": 62892,
        "diamonds": 0,
        "tickets": 2730,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 90, "exp": 64625, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 91,
        "exp": 66387,
        "diamonds": 0,
        "tickets": 3135,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 92,
        "exp": 68177,
        "diamonds": 0,
        "tickets": 3135,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 93,
        "exp": 69996,
        "diamonds": 0,
        "tickets": 3135,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 94,
        "exp": 71844,
        "diamonds": 0,
        "tickets": 3135,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 95, "exp": 73721, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
    {
        "level": 96,
        "exp": 75628,
        "diamonds": 0,
        "tickets": 3135,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 97,
        "exp": 77564,
        "diamonds": 0,
        "tickets": 3540,
        "evolution": 4,
        "egg": 0,
    },
    {
        "level": 98,
        "exp": 80500,
        "diamonds": 0,
        "tickets": 3540,
        "evolution": 4,
        "egg": 0,
    },
    {"level": 99, "exp": 83481, "diamonds": 4, "tickets": 0, "evolution": 4, "egg": 0},
]
