placeholder = "[name]"
with open("Output/sent/lastletter.txt", "w") as outputfile:
    pass

with open("Input/Names/invited_names.txt", "r") as namefile:
    namelist = namefile.readlines()

with open("Input/Letters/starting_letter.txt", "r") as startfile:
    contents = startfile.read()


for names in namelist:
    strippedname = names.strip()
    new_letter = contents.replace(placeholder, strippedname)
    with open(f"Output/sent/letter_for_{strippedname}.txt", "w") as completter:
        completter.write(new_letter)
