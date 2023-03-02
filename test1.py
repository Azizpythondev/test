
import random

tuple_1 = random.randint(1,5)
tuple_2 = random.randint(3,8)
numbers = (tuple_1, tuple_2)
def funk():
    if tuple_1 == tuple_2:
        print('bar dublikat sanlar')
    else:
        print('joq dublikat sanlar')
    return numbers
print(funk())

import random
list = []
tuple_1 = random.randint(1,5)
tuple_2 = random.randint(1,5)
if tuple_1 == tuple_2:
    print('bar dublikat sanlar')
else:
    print('joq dublikat sanlar')
list.append(tuple_1)
list.append(tuple_2)
user = list(map(lambda x: x, list))
print(user)
