import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length: Desired length of the password.
      include_uppercase: Boolean indicating if uppercase letters should be included.
      include_lowercase: Boolean indicating if lowercase letters should be included.
      include_numbers: Boolean indicating if numbers should be included.
      include_symbols: Boolean indicating if symbols should be included.

  Returns:
      A random password string.
  """
  # Define character sets based on user choices
  char_set = ""
  if include_uppercase:
    char_set += string.ascii_uppercase
  if include_lowercase:
    char_set += string.ascii_lowercase
  if include_numbers:
    char_set += string.digits
  if include_symbols:
    char_set += string.punctuation

  # Generate random password
  password = ''.join(random.sample(char_set, length))
  return password

def get_user_input():
  """
  Prompts the user for password length and character options.

  Returns:
      A tuple containing (length, include_uppercase, include_lowercase, include_numbers, include_symbols)
  """
  while True:
    try:
      length = int(input("Enter desired password length: "))
      if length <= 0:
        raise ValueError("Password length must be positive")
      break
    except ValueError:
      print("Invalid input. Please enter a positive integer.")

  include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
  include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
  include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
  include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

  return length, include_uppercase, include_lowercase, include_numbers, include_symbols

if __name__ == "__main__":
  length, include_uppercase, include_lowercase, include_numbers, include_symbols = get_user_input()
  password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
  print(f"Your generated password is: {password}")

