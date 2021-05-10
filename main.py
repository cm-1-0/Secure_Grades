from cryptography.fernet import Fernet

print("Hello Colin")
ques_1 = input("What is the password: ")
if ques_1 == "Soccer10":
    print("Welcome!")
    eng_file = open("English Grade", "w")
    ques_2 = input("How many grades would you like to enter: ")
    for num in ques_2:
        grade = input("Enter the grades: ")
        eng_file.write(grade)
        eng_file.close()

# eng_file = open("English Grade", "r")
# line = eng_file.read()
# line.split(", ")
# total = sum([int(num) for num in line.split(", ")])
# avg = total / int(ques_2)
# print(avg)

key = Fernet.generate_key()
with open("key", "wb") as key_file:
    key_file.write(key)


def load_key():
    return open("key", "rb").read()


fernet = Fernet(key)
with open("English Grade", "rb") as file:
    original = file.read()
encrypted = fernet.encrypt(original)
with open("English Grade", "wb") as encrypted_file:
    encrypted_file.write(encrypted)
