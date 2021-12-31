
# Delete spaces
sequence = '     Hello, World  \n'
# Wanted => 'Hello, World'
print(sequence.strip())
# 'Hello, World'  => deleted right and left spaces
print(sequence.rstrip())
# '     Hello, World' => delete right spaces
print(sequence.lstrip())
# 'Hello, World   ' => delete left spaces


sequence = '----Hello------'
# wanted => 'Hello'
print(sequence.strip('-'))
# 'Hello'


