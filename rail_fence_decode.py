encrypted_message = input("What is the encrypted message?\n")
encrypted_message = encrypted_message.replace(" ", "")

if len(encrypted_message) % 2 == 0:
    midway_index = int((len(encrypted_message) / 2))
else:
    midway_index = int((len(encrypted_message) / 2)) + 1

string1 = encrypted_message[0:midway_index]
string2 = encrypted_message[midway_index:]

message = ""
current_string = string1

while len(current_string) != 0:
    message += current_string[0]
    if current_string == string1:
        string1 = string1[1:]
        current_string = string2
    else:
        string2 = string2[1:]
        current_string = string1

print("\nHere is the decoded message!\n")
print(message)