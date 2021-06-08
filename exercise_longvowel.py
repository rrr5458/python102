word = "Bang"
new_word = ""

for letter in word:
    if letter == "A" or letter == "a":
        letter = "aaaa"
        new_word += letter
    elif letter =="E" or letter == "e":
        letter = "eeee"
        new_word += letter
    elif letter =="I" or letter == "i":
        letter = "iiii"
        new_word += letter
    elif letter =="O" or letter == "o":
        letter = "oooo"
        new_word += letter
    elif letter =="U" or letter == "u":
        letter = "uuuu"
        new_word += letter
    else: 
        new_word += letter
print(new_word)
   
    