#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Day 24 Project (Part 2) Mail Merge/Input/Names/invited_names.txt") as f:
    list_names = f.readlines()

with open("../Day 24 Project (Part 2) Mail Merge/Input/Letters/starting_letter.txt") as g:
    txt = g.read()
    for i in list_names:
        new_txt = txt.replace("[name]", i.strip())
        with open(f"./Output/ReadyToSend/letter_for_{i.strip()}.txt", mode="w") as v:
            v.write(new_txt)