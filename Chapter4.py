# Taking input and viewing data in file

fileName = input("Enter the name of the file: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# count the sentences.
sentences = text.count('.') + text.count('?') + text.count('!') + \
            text.count(';') + text.count(':')

# count the words.
words = len(text.split())

# count the syllables
syllables = 0
for word in text.split():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch index and grade level
index = 206.835 - 1.015 * (words / float(sentences)) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / float(sentences)) + \
                  11.8 * (syllables / float(words)) - 15.59))

# Output the results
print("The Flesch index is: ", index)
print("The Grade level equivalent is: ", level)
print(sentences," sentences")
print(words," words")
print(syllables," syllables")

