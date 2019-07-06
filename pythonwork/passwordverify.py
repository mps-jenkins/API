import re

#password= input("Enter your password")
password = "Yyio123ihj$"
flag = 0
while True:
    if (len(password) < 8):
        flag = -1
        break
    elif not re.search("[a-z]",password):
        flag = -1
        break
    elif not re.search("[A-Z]",password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[$#@]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")

        break

if flag == -1:
    print("no valid password")
