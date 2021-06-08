sentence = "I am a programmer"
new_sentence = ""

for letter in sentence: 
    if letter == "A" or letter == "a":
        letter = "4"
        new_sentence += letter
    elif letter == "E" or letter == "e":
        letter = "3"
        new_sentence += letter
    elif letter == "G" or letter == "g":
        letter = "6"
        new_sentence += letter
    elif letter == "I" or letter == "i":
        letter = "1"
        new_sentence += letter
    elif letter == "O" or letter == "o":
        letter = "0"
        new_sentence += letter
    elif letter == "S" or letter == "s":
        letter = "5"
        new_sentence += letter
    elif letter == "T" or letter == "t":
        letter = "7"
        new_sentence += letter
    else: 
        new_sentence += letter

print(new_sentence)
    
    
