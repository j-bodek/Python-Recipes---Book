
# for complex patterns
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
replacedText = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(replacedText)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

from calendar import month_abbr
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))
'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'





