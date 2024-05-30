from texts import logo
print(logo)
 
from texts import alphabet

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += letter
  print(f"Here's the {direction}d result: {end_text}")

should_cont = True
while should_cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Do you want to go again? type 'y' for yes and 'n' for no: ")
  if result == "y":
    continue
  elif result == "n":
    should_cont = False
    print("operation complate!")
  else:
    print("error.")