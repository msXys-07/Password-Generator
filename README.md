# 🔐 Password Generator

A simple command-line password generator written in Python.

This program generates secure random passwords based on user preferences such as password length, uppercase letters, digits, and special characters. Every generated password is also saved to a `password.txt` file.

## Features

- Custom password length (minimum 8 characters)
- Optional uppercase letters
- Optional digits
- Optional special characters
- Randomized password generation
- Saves generated passwords to `password.txt`

## Requirements

- Python 3.x

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/msXys-07/Password-Generator.git
```

2. Navigate to the project folder:

```bash
cd Password-Generator
```

3. Run the program:

```bash
python password_gen.py
```

## Example

```
Enter the length of the password: 12
Do you want to use uppercase letters? (y/n): y
Do you want to use digits? (y/n): y
Do you want to use special characters? (y/n): y

Password generated is T9@pF4h!zQ2a and saved to password.txt
```

## Project Structure

```
Password-Generator/
│── password_generator.py
│── password.txt
└── README.md
```

## Future Improvements

- Password strength indicator
- Copy password to clipboard
- Generate multiple passwords at once
- Graphical User Interface (GUI)
- Custom character exclusions

## Author

Mayank Singh Chauhan [Yash]