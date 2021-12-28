

data = [1,2,3,4,5,6,7,8,9,10,11]
first, *middle, last = data
print(first)
print(middle)
print(last)

# 1
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
# 11



records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
# foo 1 2
# bar hello
# foo 3 4