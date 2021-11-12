import matplotlib.pyplot as plt
from plotly import offline
plt.style.use('seaborn-whitegrid')
import numpy as np

pinole_league_dict = {
    '111121': [176, 211, 235],
    '110421': [190, 205, 259],
    '102821': [200, 228, 184],
    '102121': [146, 189, 234],
    '101421': [189, 135, 221],
    '100721': [199, 192, 258],
    '093021': [225, 268, 198],
    '092321': [235, 205, 216],
    '091621': [151, 194, 214],
    '090921': [227, 159, 198],
}
earl_league_dict = {
    '092621': [234, 279, 256],
    '102621': [220, 187, 225],
    '110221': [214, 182, 187],
    '110921': [258, 190, 224],
}

ev, ek = [], []
earl_values = list(earl_league_dict.values())
earl_keys = list(earl_league_dict.keys())
for i in earl_values:
    ev.append(sum(i)//3)
for i in earl_keys:
    ek.append(i)

pv, pk = [], []
pinole_values = list(pinole_league_dict.values())
pinole_keys = list(pinole_league_dict.keys())
for i in pinole_values:
    pv.append(sum(i)//3)
for i in pinole_keys:
    pk.append(i)

fig = plt.figure()
ax = plt.axes()

ax.plot(ek, ev)
ax.plot(pk, pv)
plt.show()
