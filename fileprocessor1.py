with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()

print("Printing out User Data:\n")

for line in lines:
    if line.startswith('#'):
        continue
    data = line.strip().split(':')

    if len(data) !=4:
        print(f"Invalid data format: {line}")
        continue

    username, password, userid, groupid = data
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")
