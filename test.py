with open('current_user.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    words = line.split(':')
    print(words[0])
