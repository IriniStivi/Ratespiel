import re

print("Rate, woran ich denke:")
for i in 1, 2, 3, 4, 5, 6, 7:
    
    z = input()
    if re.findall("[Ll]uhmann", z):     # finds "L/luhmann"
        print("Du kannst ja Gedanken lesen!")
        break
    else:
        print("Nö.")
print("Luhmann, du Eule.")
