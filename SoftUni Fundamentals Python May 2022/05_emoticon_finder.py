data = input()
for char in range(len(data)):
    emoticon = ""
    if data[char] == ':':
        emoticon += ":"+data[char+1]
        print(emoticon)