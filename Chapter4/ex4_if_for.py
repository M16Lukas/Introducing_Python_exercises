# 4.1
guess_me = 7
if guess_me < 7:
    print('loo law')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4.2
guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

# 4.3
for i in [3, 2, 1, 0]:
    print(i)
