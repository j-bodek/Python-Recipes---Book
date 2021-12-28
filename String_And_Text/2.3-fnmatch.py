from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('foo.txt', '?uo.txt'))

print(fnmatch('dat45.csv', 'dat[0-4]*')) #check 4 not 45
print(fnmatch('dat45.csv', 'dat[0-3]*'))


names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
