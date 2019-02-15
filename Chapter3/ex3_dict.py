# 3.10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# 3.11
print(e2f['walrus'])

# 3.12
f2e = dict()
for keys, values in e2f.items():
    f2e[values] = keys

# 3.13
print(f2e['chien'])

# 3.14
print(e2f.keys())

# 3.15
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

# 3.16
print(life.keys())

# 3.17
print(life['animals'].keys())

# 3.18
print(life['animals']['cats'])
