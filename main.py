with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_ = names.readlines()

list_names = []
for name in list_:
    new_name = name.strip()
    list_names.append(new_name)

with open("./Input/Letters/starting_letter.txt", mode="r") as let:
    letters = let.readlines()

n = 0
for name in list_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invite:
        if n == 0:
            letters[0] = letters[0].replace("[name]", f"{name}")
        else:
            letters[0] = letters[0].replace(f"{old_name}", f"{name}")
        invite.writelines(letters)
        old_name = name
        n += 1
