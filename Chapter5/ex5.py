from collections import OrderedDict, defaultdict

"""
# 5.1
import zoo
print(zoo.hour())

# 5.2
import zoo as menagerie
print(menagerie.hour())

# 5.3
from zoo import hour
print(hour())
"""
# 5.4
from zoo import hour as info
print(info())

# 5.5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# 5.6
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# 5.7
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append("something for a")
print(dict_of_lists['a'])
