ipsum_file = open('files/ipsum.txt')

for line in ipsum_file:
    print(line.rstrip())

ipsum_file.seek(0)

lines = ipsum_file.readlines()
print(lines)

# Finds 50th character in the file text, and reads next 100
ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)

# We always have to close the file (performance)
ipsum_file.close()

# Other way to keep file closed after we done are job 'open as dna_file'
# Filtering content


def sequence_filter(line):
    return '>' not in line


with open('files/dna_sequence.txt') as dna_file:
    lines_dna_all = dna_file.readlines()
    print(lines_dna_all)
    lines_dna_mod = list(filter(sequence_filter, lines_dna_all))
    print(lines_dna_mod)
