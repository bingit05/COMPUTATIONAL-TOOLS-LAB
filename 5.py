

text = input("Enter a string: ")


words = text.split()

word_frequency = [(word, words.count(word)) for word in set(words)]

print("\nWord Frequency:")
for word, count in word_frequency:
    print(word, ":", count)


characters = [char for char in text if char != " "]

char_frequency = [(char, characters.count(char)) for char in set(characters)]

print("\nCharacter Frequency:")
for char, count in char_frequency:
    print(char, ":", count)