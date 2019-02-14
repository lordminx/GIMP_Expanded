# coding: utf-8
titel = "GIMP"

expanded = titel + "\n\n" + "GNU Image Manipulation Program"

temp = expanded + "\n\n"

result = temp

while count_words(result) < 50000:
    if "GNU" in temp:
        temp = expand_gnu(temp)
        result += temp
    if "UNIX" in temp:
        temp = expand_unix(temp)
        result += temp
        
with open("GIMP_expanded.txt") as f:
    f.write(result)
    
    
