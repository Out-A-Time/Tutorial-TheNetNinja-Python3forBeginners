with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there ninjas, Python is awesome')

# Append more text to the file
with open('files/write.txt', 'a') as write_file:
    write_file.write('\nI love so much, I dream in Python')

quotes = [
    '\nI can resist everything except temptation',
    '\nAlways forgive your enemies - nothing annoys hem so much',
    '\nWe are all in the gutter, but some of usu are looking at the stars'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
