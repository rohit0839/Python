## Encryption using Dictionary

my_dict={"A":"E", "B":"F", "C":"G", "D":"H", "E":"I",
           "F":"J", "G":"K", "H":"L", "I":"M", "J":"N",
           "K":"O", "L":"P", "M":"Q", "N":"R", "O":"S",
           "P":"T", "Q":"U", "R":"V", "S":"W", "T":"X",
           "U":"Y", "V":"Z", "W":"A", "X":"B", "Y":"C",
           "Z":"D", "1":"4", "2":"5", "3":"6",
           "4":"7", "5":"8","6":"9","7":"0","8":"1",
           "9":"2","0":"3", " ":" "}

message = input("Enter Message: ").upper()
encrypted = ""

for letters in message:
    if letters in my_dict:
        encrypted += my_dict[letters]
    else:
        encrypted += letters

print(encrypted.lower())

