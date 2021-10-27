import statistics

pinole_league = [
    146, 189, 234,
    189, 135, 221,
    199, 192, 258,
    225, 268, 198,
    235, 205, 216,
    151, 194, 214,
    227, 159, 198,
]
print("\n****Pinole Valley Thursday League****")
print(f"Total games:  ", len(pinole_league))
print(f"Total pins:  ", sum(pinole_league))
print(f"Average:  {int(statistics.mean(pinole_league))}")
print(f"Standard Deivation:  {int(statistics.stdev(pinole_league))}")
print(f"High game:   ", max(pinole_league))
print(f"Low game:   ", min(pinole_league))


earl_league = [
    234, 279, 256,
    220, 187, 225,
    ]
print("\n****Earl Anthony Tuesday League****")
print(f"Total games:  ", len(earl_league))
print(f"Total pins:  ", sum(earl_league))
print(f"Average:  {int(statistics.mean(earl_league))}")
print(f"Standard Deivation:  {int(statistics.stdev(earl_league))}")
print(f"High game:   ", max(earl_league))
print(f"Low game:   ", min(earl_league))
