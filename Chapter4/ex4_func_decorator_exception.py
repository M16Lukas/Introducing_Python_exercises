# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']


# 4.9
def get_odds():
    for num in range(10):
        if not num % 2 == 0:
            yield num


get_odd = list(get_odds())
for odd in get_odd:
    if get_odd[2] == odd:
        print(odd)


# 4.10
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func


# 4.11
class OopsException(Exception):
    pass


try:
    raise OopsException
except OopsException:
    print('Caught an opps')

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A run turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
