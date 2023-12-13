import random 

def upperCase(passwordCharacters):
    upper1 = chr(random.randint(65, 90))
    upper2 = chr(random.randint(65, 90))
    passwordCharacters.extend([upper1, upper2])

    return passwordCharacters

def lowerCase(passwordCharacters):
    lower1 = chr(random.randint(97,122))
    lower2 = chr(random.randint(97,122))
    passwordCharacters.extend([lower1, lower2])

    return passwordCharacters

def numbers(passwordCharacters):
    number1 = chr(random.randint(48, 57))
    number2 = chr(random.randint(48, 57))
    passwordCharacters.extend([number1, number2])

    return passwordCharacters

def symbols(passwordCharacters):
    symbol1 = chr(random.randint(33,39))
    symbol2 = chr(random.randint(33,39))
    passwordCharacters.extend([symbol1, symbol2])

    return passwordCharacters

def main():
    passwordCharacters = []
    upperCase(passwordCharacters)
    lowerCase(passwordCharacters)
    numbers(passwordCharacters)
    symbols(passwordCharacters)

    random.shuffle(passwordCharacters)
    password = ("".join(map(str,passwordCharacters)))
    

    file = open("passwordList.txt", 'a+')

    content = file.read()

    if password in content:
        file.write("DUPLICATE \n")
        main()  
    else:
        file.writelines([password,"\n"])
        print(password)
        exit()

main()