import random
import array

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

def getChars(prompt, choices):
  global MAX_LEN
  n = int(input(prompt))
  if(MAX_LEN < 0):
    print("Can't have this many characters as MAX Length is only", MAX_LEN)
    return
  MAX_LEN = MAX_LEN - n
  arr = [random.choice(choices) for _ in range(n)]
  return arr

MAX_LEN = int(input("Enter the length of the password."))

digits = getChars("How many digits do you want in the password: ", DIGITS)
upper = getChars("How many upper case chars do you want in the password: ", UPCASE_CHARACTERS)
lower = getChars("How many lower case chars do you want in the password: ", LOCASE_CHARACTERS)
symbols = getChars("How many symbols do you want in the password: ", SYMBOLS)
remains = [random.choice(COMBINED_LIST) for _ in range(MAX_LEN)]

total = digits + upper + lower + symbols + remains
random.shuffle(total)

password = ""
for x in total:
password = password + x
		
print(password)
