import string
import random
import hashlib

while True:

    userinput = input("what is the length of the password you would like? -> ")
    if not userinput.isdigit():
        print("your didnt put a number -> ")
#    elif int(userinput) <= 7:
 #       print("password must be atleast 8 characters long")
    else:
        userinput = int(userinput)
        password_chars = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

        password = "".join(random.choices(password_chars, k=userinput))
        print(f"Generated Password: {password}")
        sat = input("are you satisfied with the password? yes/no ")
        if sat == "yes" or sat == "y":
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("your password is > ", hashed_password)
            break


