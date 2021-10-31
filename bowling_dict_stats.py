import statistics

pinole_league_dict = {
    '102821': [200, 228, 184],
    '102121': [146, 189, 234],
    '101421': [189, 135, 221],
    '100721': [199, 192, 258],
    '093021': [225, 268, 198],
    '092321': [235, 205, 216],
    '091621': [151, 194, 214],
    '090921': [227, 159, 198],
}

#convert dictionary values into a list
pinole_values = list(pinole_league_dict.values())
pinole_dict_list = []
for i in range(0,len(pinole_values)):
    for x in range(0,3):
        pinole_dict_list.append(pinole_values[i][x])

print("\n****Pinole Valley Thursday League****")
print(f"Total games:  ", len(pinole_dict_list))
print(f"Total pins:  ", sum(pinole_dict_list))
print(f"Average:  {int(statistics.mean(pinole_dict_list))}")
print(f"Standard Deivation:  {int(statistics.stdev(pinole_dict_list))}")
print(f"High game:   ", max(pinole_dict_list))
print(f"Low game:   ", min(pinole_dict_list))


earl_league_dict= {
    '092621': [234, 279, 256],
    '102621': [220, 187, 225]
    }

#convert dictionary values into a list
earl_values = list(earl_league_dict.values())
earl_dict_list = []
for i in range(0,len(earl_values)):
    for x in range(0,3):
        earl_dict_list.append(earl_values[i][x])


print("\n****Earl Anthony Tuesday League****")
print(f"Total games:  ", len(earl_dict_list))
print(f"Total pins:  ", sum(earl_dict_list))
print(f"Average:  {int(statistics.mean(earl_dict_list))}")
print(f"Standard Deivation:  {int(statistics.stdev(earl_dict_list))}")
print(f"High game:   ", max(earl_dict_list))
print(f"Low game:   ", min(earl_dict_list))

#study for later use
#a = ({k: sum(v) for k, v in pinole_league_dict.items()})
#b = sum(map(len, pinole_league_dict.values()))
#ad = ({k: sum(v) for k, v in earl_league_dict.items()})
#bd = sum(map(len, earl_league_dict.values()))
