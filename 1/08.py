import re
def cipher(string):
    result = ""
    for i in range(0,len(string)):
        if re.match("[a-z]",string[i]):
            result += chr(219 - ord(string[i]))
        else :
            result += string[i]
    return result

print(cipher("I Am An Engineer."))