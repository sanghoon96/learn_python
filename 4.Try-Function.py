def printinfo( fname, fage = 35 ):
    return fname, fage

name, age = printinfo( fage=50, fname="miki" )
print(name + ', ' + str(age))