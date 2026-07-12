import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*-+_="
digits = "0123456789"

while True:       # Repeat the code forever

    len_pass = int(input("Enter the length of the password: "))
    
    if len_pass >= 8:
        break      # Loops breaker
    elif len_pass < 8:
        print("Password length is invalid. Please enter a length of at least 8  characters.")

    else:
        print("Something went wrong. Error 303")


allowed_chars = lowercase  # This creates your character pool which has default lowercase

password = []     # Creates an empty list

while True:
    use_upper = input("Do you want to use uppercase letters? (y/n): ").strip().lower()
    
    if use_upper =="y":
        allowed_chars += uppercase   # The uppercase is added to allowed chars
        password.append(random.choice(uppercase)) # Picks random UL, adds to []
        break
    elif use_upper =="n":
        break
        
    else:
        print("Invalid choice! Please try again.") # The loop repeats as no y/n


while True:
    use_digits = input("Do you want to use digits? (y/n): ").strip().lower()
    
    if use_digits =="y":
        allowed_chars += digits
        password.append(random.choice(digits))
        break
    elif use_digits =="n":
        break
        
    else:
        print("Invalid choice! Please try again.")


while True:
    use_special = input("Do you want to use special characters? (y/n): ").strip().lower()

    if use_special =="y":
        allowed_chars += special
        password.append(random.choice(special))
        break
    elif use_special =="n":
        break

    else:
        print("Invalid choice! Please try again.")

remain = len_pass - len(password)  # Subtracts the choice len from entered len

password.extend(random.choices(allowed_chars, k=remain))  # Choices the remaining chars

random.shuffle(password)  # Shuffles the characters of password
process_pass = ''.join(password)   # Merges each chars of the password

with open ("password.txt", "a+") as f:   # Opens/Makes a new file
    f.write(f"{process_pass}\n")     # Writes and saves the password in file

print(f"Password generated is {process_pass} and saved to password.txt")




'''
allowed_chars = LOWERCASE

password = []


# Helper function for yes/no input
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ("y", "n"):
            return answer

        print("Please enter only 'y' or 'n'.")


# -------------------------------
# Uppercase
# -------------------------------
if ask_yes_no("Include uppercase letters? (y/n): ") == "y":
    allowed_chars += UPPERCASE
    password.append(random.choice(UPPERCASE))


# -------------------------------
# Digits
# -------------------------------
if ask_yes_no("Include digits? (y/n): ") == "y":
    allowed_chars += DIGITS
    password.append(random.choice(DIGITS))


# -------------------------------
# Special Characters
# -------------------------------
if ask_yes_no("Include special characters? (y/n): ") == "y":
    allowed_chars += SPECIAL
    password.append(random.choice(SPECIAL))
'''