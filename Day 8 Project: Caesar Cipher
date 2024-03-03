import string

alphabet = list(string.ascii_lowercase)

action = input("Encode or Decode your message [E/D]: ")

if action == "E":
  user_message = input("Encode your message: ")
  shift = int(input("Number of shifts: "))
  encoded_message=""
  for parsed_letter in user_message:
    if parsed_letter in alphabet:
      shift_cypher = alphabet.index(parsed_letter) + shift
      encoded_message += alphabet[shift_cypher%len(alphabet)]
  print("Your encoded message is: " + encoded_message)
elif action == "D":
  user_message = input("Decode your message: ")
  shift = int(input("Number of shifts: "))
  encoded_message=""
  for parsed_letter in user_message:
    shift_cypher = alphabet.index(parsed_letter) - shift
    encoded_message += alphabet[shift_cypher%len(alphabet)]
  print("Your decoded message is: " + encoded_message)
