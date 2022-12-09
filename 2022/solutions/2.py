import pandas as pd

data = pd.read_csv('input/2.txt', header = None, sep = " ", names = ["them","me"])

combos = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

pnts = {'X':1,'Y':2,'Z':3}

data['points'] = data.apply(lambda row: combos[row.them + row.me] + pnts[row.me], axis = 1)

print(sum(data.points))

combos = {
    'AX': 3,
    'AY': 1,
    'AZ': 2,
    'BX': 1,
    'BY': 2,
    'CX': 2,
    'BZ': 3,
    'CY': 3,
    'CZ': 1
}
pnts = {'X':0,'Y':3,'Z':6}

data['points'] = data.apply(lambda row: combos[row.them + row.me] + pnts[row.me], axis = 1)

print(sum(data.points))