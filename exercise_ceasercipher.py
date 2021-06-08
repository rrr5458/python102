alphabet = list("abcdefghijklmnopqrstuvwxyz  ")

message = "meet me at the creek"
coded_message = ""

for letter in message:
    i = alphabet.index(letter)
    letter = alphabet[i + 1]
    coded_message += letter

print(coded_message)