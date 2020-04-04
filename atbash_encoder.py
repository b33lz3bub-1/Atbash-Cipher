import sys

dictionary_caps = {"A" : "Z", "B" : "Y" , "C" : "X", "D" : "W", "E" : "V", "F" : "U",
                "G" : "T", "H" : "S", "I" : "R", "J" : "Q", "K" : "P", "L" : "O",
                "M" : "N", "N" : "M", "O" : "L", "P" : "K", "Q" : "J", "R" : "I",
                "S" : "H", "T" : "G", "U" : "F", "V" : "E", "W" : "D", "X" : "C",
                "Y" : "B", "Z" : "A"}
dictionary_small = {"a" : "z", "b" : "y" , "c" : "x", "d" : "w", "e" : "v", "f" : "u",
                "g" : "t", "h" : "s", "i" : "r", "j" : "q", "k" : "p", "l" : "o",
                "m" : "n", "n" : "m", "o" : "l", "p" : "k", "q" : "j", "r" : "i",
                "s" : "h", "t" : "g", "u" : "f", "v" : "e", "w" : "d", "x" : "c",
                "y" : "b", "z" : "a"}

def encode(latter):
    c_text = ""
    
    if latter not in dictionary_caps and latter not in dictionary_small:
        c_text += latter
    elif latter in dictionary_caps:
        c_text += dictionary_caps[latter]
    else:
        c_text += dictionary_small[latter]
    return c_text
    
string = sys.argv[1]        # take first argument as string

string = string.split()     # Split the string into list of words

cipher_text = ""            # Resultant Cipher Text
for word in string:         # Take each word from the list of string
    for i in range(len(word)):
        cipher_text += encode(word[i])
    cipher_text += " "

print cipher_text

     
    
