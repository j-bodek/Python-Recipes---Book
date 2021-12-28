

# str.find(), str.endswith(), str.startswith() - for easy iterals

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')
# Match at start or end
print(text.startswith('yeah'))

print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
#for more complex sentences use module re
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes-text1')
else:
    print('no-text1')
    
if re.match(r'\d+/\d+/\d+', text2):
    print('yes-text2')
else:
    print('no-text2')


datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text)) #find all strings that match datapat pattern


# FOR MORE INFORMATIONS ABOUT REGULAR EXPRESSIONS CHECK THIS LINK ==> https://docs.python.org/3/library/re.html





