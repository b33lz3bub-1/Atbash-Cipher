import sys

dictionary_caps = {"Z" : "A", "Y" : "B" , "X" : "C", "W" : "D", "V" : "E", "U" : "F",
                "T" : "G", "S" : "H", "R" : "I", "Q" : "J", "P" : "K", "O" : "L",
                "N" : "M", "M" : "N", "L" : "O", "K" : "P", "J" : "Q", "I" : "R",
                "H" : "S", "G" : "T", "F" : "U", "E" : "V", "D" : "W", "C" : "X",
                "B" : "Y", "A" : "Z"}
dictionary_small = {"z" : "a", "y" : "b" , "x" : "c", "w" : "d", "v" : "e", "u" : "f",
                "t" : "g", "s" : "h", "r" : "i", "q" : "j", "p" : "k", "o" : "l",
                "n" : "m", "m" : "n", "l" : "o", "k" : "p", "j" : "q", "i" : "r",
                "h" : "s", "g" : "t", "f" : "u", "e" : "v", "d" : "w", "c" : "x",
                "b" : "y", "a" : "z"}

def decode(latter):
    p_text = ""
    
    if latter not in dictionary_caps and latter not in dictionary_small:
        p_text += latter
    elif latter in dictionary_caps:
        p_text += dictionary_caps[latter]
    else:
        p_text += dictionary_small[latter]
    return p_text
    
string = sys.argv[1]        # take first argument as string

string = string.split()     # Split the string into list of words

plain_text = ""            # Resultant Cipher Text
for word in string:         # Take each word from the list of string
    for i in range(len(word)):
        plain_text += decode(word[i])
    plain_text += " "

print plain_text

     
    
