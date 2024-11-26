data = [
    ["G", "A", "I", "H", "C", "C", "N", "W", "O", "D", "T", "E", "L", "O", "R"],
    ["N", "D", "N", "E", "I", "N", "G", "R", "T", "E", "N", "S", "I", "O", "N"],
    ["I", "T", "T", "A", "O", "Y", "O", "R", "L", "D", "S", "E", "S", "E", "C"],
    ["T", "A", "I", "R", "R", "M", "R", "L", "E", "I", "C", "H", "F", "O", "G"],
    ["E", "L", "M", "T", "A", "I", "E", "E", "K", "R", "T", "I", "N", "L", "N"],
    ["E", "G", "A", "N", "H", "W", "N", "Y", "V", "N", "E", "Q", "A", "I", "S"],
    ["L", "A", "T", "E", "E", "G", "E", "N", "C", "O", "U", "N", "T", "E", "R"],
    ["F", "I", "E", "R", "G", "O", "I", "O", "D", "E", "C", "R", "E", "M", "E"],
    ["C", "D", "A", "U", "E", "D", "Y", "L", "S", "E", "F", "S", "O", "R", "J"],
    ["S", "F", "I", "T", "L", "I", "S", "T", "E", "N", "T", "R", "I", "E", "E"],
    ["B", "L", "I", "N", "K", "S", "J", "V", "B", "L", "U", "S", "H", "D", "C"],
    ["S", "A", "N", "E", "E", "T", "O", "U", "C", "H", "D", "D", "I", "T", "T"],
    ["P", "G", "I", "V", "V", "L", "K", "L", "A", "T", "E", "N", "S", "M", "I"],
    ["O", "O", "S", "D", "K", "H", "E", "A", "L", "T", "H", "Y", "A", "T", "O"],
    ["S", "M", "E", "A", "N", "E", "S", "N", "S", "M", "I", "L", "E", "C", "N"],
    ["A", "H", "N", "M", "I", "G", "N", "I", "M", "R", "A", "H", "C", "D", "W"],
    ["O", "M", "Y", "E", "R", "N", "A", "F", "F", "E", "C", "T", "I", "O", "N"],
    ["A", "K", "I", "A", "D", "M", "I", "R", "A", "T", "I", "O", "N", "C", "K"]
]

print("Type 'STOP123' if you want to end this program")


while True:
    word = input("Enter word to get loaction: ")
    word = word.upper()
    if word == "STOP123":
        break
    found = False
    for i in range(0,len(data)):
        row = data[i]
        for k in range(len(row)):
            ele = row[k]
            if ele == word[0]:
                if len(word)+i<=len(data):
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i+x][k] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+x+1,k+1])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)<=i+1:
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i-x][k] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1-x,k+1])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)+k<=len(row):
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i][k+x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1,k+x+1])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)<=k+1:
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i][k-x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1,k+1-x])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)+k<=len(row) and len(word)<=i+1:
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i-x][k+x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1-x,k+1+x])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)+k<=len(row) and len(word)+i<=len(data):
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i+x][k+x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1+x,k+1+x])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)<=k+1 and len(word)+i<=len(data):
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i+x][k-x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1+x,k+1-x])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
                if len(word)<=k+1 and len(word)<=i+1:
                    x =0
                    positions = []
                    flag = True
                    for u in word:
                        if data[i-x][k-x] != u:
                            flag = False
                            break
                        else:
                            positions.append([i+1-x,k+1-x])
                        x+=1
                    if flag:
                        for z in range(0,len(word)):
                            print(f"char: {word[z]}, row = {positions[z][0]}, column = {positions[z][1]}")
                            found = True
    if found == False:
        print("Word NOT found")
