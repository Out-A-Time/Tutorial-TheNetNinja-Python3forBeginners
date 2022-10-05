# MAPS
from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# FOR LOOP
for word in words:
    anagrams.append(jumble(word))
print(anagrams)
#['teootreb', 'rctroas', 'osaepott']

# COMPRHENSION METHOD
anagrams = [jumble(word) for word in words]
print(anagrams)
#['otertebo', 'trrsaco', 'eaotostp']

# MAP
anagrams = list(map(jumble, words))
print(anagrams)
#['rtotebeo', 'trocsra', 'aespotot']
