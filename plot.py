import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from copy import deepcopy
values = {
    'ECAL local reconstruction': 38.9,
    'HCAL local reconstruction': 73.9,
    'Jets/MET': 	14,
    'E/Gamma': 20.4,
    'Muons': 34.2,
    'Pixel tracking': 65.7,
    'Full tracking': 114.2,
    'Vertex reconstruction':	2.3,
    'Particle Flow and Taus': 36.8,
    'HLT': 14.7,
    'Overhead': 56.4,
}

explode = [0 for _ in range(len(values))]
explode[0] = 0.1
explode[1] = 0.1

total = sum(values.values())
out = plt.pie(list(values.values()),
              autopct='%1.1f%%', shadow=False, explode=explode, labels=list(values.keys()))

plt.axis('equal')
# plt.tight_layout()
plt.rcParams.update({'font.size': 22})
plt.show()

tmp = list(values.values()).copy()

frame = pd.DataFrame()
frame['Group'] = list(values.keys())
frame['Real-Time (ms)'] = [str(deepcopy(x))+' ms' for x in values.values()]
frame['Percentage'] = [
    str(round(x * 100 / sum(values.values()), 2)) + '%' for x in values.values()]
print(tmp)
frame.loc[len(values)] = ('Total', str(sum(tmp)) + ' ms', '100%')
print(frame.to_latex())
