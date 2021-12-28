

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
# split after ';' plus any number of spaces \s
# split after ',' plus any number of spaces \s
# split after '\s' plus any number of spaces \s
splitedLine = re.split(r'[;,\s]\s*', line)
print(splitedLine)

line = 'asdf fjdk; afed, --fjek,--asdf,  -foo'
splitedLine = re.split(r'[;,\s-]\s*-*', line)
print(splitedLine)



