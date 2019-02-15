# 3.1
year_lists = [1980, 1981, 1982, 1983, 1984, 1985]

# 3.2
print(year_lists[3])

# 3.3
print(year_lists[-1])

# 3.4
things = ["mozzarella", "cinderella", "salmonella"]

# 3.5
print(things[1].capitalize())
print(things)

# 3.6
print(things[0].upper())

# 3.7
del things[2]
print(things)

# 3.8
surprise = ["Groucho", "Chico", "Harpo"]

# 3.9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise)
