with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()


def encode(string):
 
    encoding = "" 
 
    i = 0
    while i < len(string):
        count = 1
 
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
 
        encoding += str(count) + string[i]
        i = i + 1
 
    return encoding
 
 

with open('file_decode.txt', 'w') as file:
    encoding = encode(string)
    file.write(encoding)

print(encode(string))