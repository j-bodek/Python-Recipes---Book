
# USEFULL LINKS:
# -  https://docs.python.org/3/howto/regex.html
# -  https://docs.python.org/3/library/re.html
# -  https://developers.google.com/edu/python/regular-expressions



# 1. re module
import re

# 2. methods to search for matches

testString = '123abc456789abc123ABC'

pattern = re.compile(r'abc')
# then we can use this string to find matches
matches = pattern.finditer(testString)

# or use it on re module
matches = re.finditer(r'abc', testString)

# iterate object
print('------------------- Matches with finditer method -------------------')
for match in matches:
    print(match)


a = r'\tHello' #\t -> tab  but r means that this is a raw string so it will be print as '\tHello' instead of '  Hello'
print(a)


# OTHER METHODS match(), search(), findall()
print('------------------- Matches with findall method -------------------')
matches = pattern.findall(testString)
print(matches)
print('------------------- Matches with match method -------------------')
match = pattern.match(testString) # match looks only at begining
print(match)
match = re.match(r'123', testString) # match looks only at begining
print(match)


# 3. methods on a match objects
matches = pattern.finditer(testString)

# group, start, end, span - methods
for match in matches:
    print(f'Match span (start and end index) => {match.span()}')
    print(f'Match start (start index) => {match.start()}')
    print(f'Match end (end index) => {match.end()}')
    print(f'Match group => {match.group()}')


# 4. meta characters
# ALL META CHARACTERS: . ^ $ * + ? { } [ ] \ | ( )

#    . Any character (except newline character) "he..o"
print('------------------- . - Meta character -------------------')
matches = re.findall(r'.', testString)
print(matches)
#    ^ Starts with "^hello"
print('------------------- ^ - Meta character -------------------')
matches = re.findall(r'^123', testString)
print(matches)
#    $ Ends with "world$"
print('------------------- $ - Meta character -------------------')
matches = re.findall(r'ABC$', testString)
print(matches)
#    * Zero or more occurrences "aix*"
#    + One or more occurrences "aix+"
#    { } Exactly the specified number of occurrences "al{2}"
#    [] A set of characters "[a-m]"
#    \ Signals a special sequence (can also be used to escape special characters) "\d"
#    | Either or "falls|stays"
#    ( ) Capture and group





# 5. More special sequences
print('------------------- More special sequences -------------------')

#    \d :Matches any decimal digit; this is equivalent to the class [0-9].
#    \D : Matches any non-digit character; this is equivalent to the class [^0-9].
#    \s : Matches any whitespace character;
#    \S : Matches any non-whitespace character;
#    \w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
#    \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
#    \b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
#    \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
#    \A Returns a match if the specified characters are at the beginning of the string "\AThe"
#    \Z Returns a match if the specified characters are at the end of the string "Spain\Z"
testString = 'hello 123_ heyho hey'
pattern = re.compile(r'\bhey') # digits
matches = pattern.findall(testString)
print(matches)




# 6. Sets

print('------------------- Sets -------------------')

testString = 'hello 123_ heyho hey'
pattern = re.compile(r'[lo]')
pattern = re.compile(r'[hello]') # find all characters h, e, l, o
pattern = re.compile(r'[a-f]') # find all a-f
pattern = re.compile(r'[1-5]') # find all 1-5
pattern = re.compile(r'[a-zA-Z]') # find all a-z including upper case letters
matches = pattern.findall(testString)
print(matches)




# 7. Quantifier

print('------------------- Quantifier -------------------')

#    * : 0 or more
#    + : 1 or more
#    ? : 0 or 1, used when a character can be optional
#    {4} : exact number
#    {4,6} : range numbers (min, max)

testString = 'hello _123_ heyho hey'
pattern = re.compile(r'\d*') # find all other elements and matches
pattern = re.compile(r'_\d') # find digit with '_' in front of it
pattern = re.compile(r'\d{3}') # look for exactly 3 digits
matches = pattern.findall(testString)
print(matches)



print('------------------- Example with Dates -------------------')

dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

# we only wants to extract the dates in format of year-month-day
datePattern = re.compile(r'\d{4}-\d{2}-\d{2}') # year-month-day format
datePattern = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}') # year-month-day format or year/month/day
datePattern = re.compile(r'\d{4}-0[5-6]-\d{2}') # year-month-day format and only may or june
matchesDates = datePattern.findall(dates)
print(matchesDates)



# 8. Conditions

print('------------------- Conditions -------------------')

myString = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
# extract all names
print('------------------- Names Matches -------------------')
namePattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+') # . is optional character and | is exception character
nameMatches = namePattern.finditer(myString)
for match in nameMatches:
    print(match)
    
    
    
    
# 9. Grouping
    
# now extract all emails from the string
print('------------------- Email Matches -------------------')
emailPattern = re.compile(r'[a-zA-Z0-9-]+@') # any number of characters or digits but followed by @
# ( ) - defining groups
emailPattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)') # any number of characters or digits but followed by @ and then containing characters and dot
emailMatches = emailPattern.finditer(myString)
for match in emailMatches:
    print(f'Group 0 => {match.group(0)}')
    print(f'Group 1 => {match.group(1)}')
    print(f'Group 2 => {match.group(2)}')
    print(f'Group 3 => {match.group(3)}')





# 10. Modification
print('------------------- Modification -------------------')


# split, sub  -  methods
testString = 'abc123ABCDEF123ABC'
pattern = re.compile(r'123')
splited = pattern.split(testString) # split string using pattern in this example '123'
print(splited) #  ==>  ['abc', 'ABCDEF', 'ABC']

# sub method finds all patterns and replace it with different substrings
testString = 'hello world, you are the best world'
pattern = re.compile(r'world')
subbedString = pattern.sub('planet', testString)
print(subbedString)


urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
# extract urls
urlPattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
urlsMatches = urlPattern.finditer(urls)
for match in urlsMatches:
    print(match.group())
    
# replace urls beginning to return only domain names
subbedUrls = urlPattern.sub(r'\2\3', urls) # replace emails with second and third group from pattern
print(subbedUrls)




# 11. Compilations flags

#    ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
#    DOTALL, S : Make . match any character, including newlines.
#    IGNORECASE, I : Do case-insensitive matches.
#    LOCALE, L : Do a locale-aware match.
#    MULTILINE, M : Multi-line matching, affecting ^ and $.
#    VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.

print('------------------- Compilations flags -------------------')

testString = 'hello World, you are the best World'
pattern = re.compile(r'world', re.IGNORECASE) # make our pattern case insensitive
matches = pattern.findall(testString)
print(matches)



























