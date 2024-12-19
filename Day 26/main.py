import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
dictionary = {}

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# print(dictionary)


word = input("Enter your word").upper()

output = [dictionary[item] for item in word]
print(output)
