n = int(input())
synonym_dict = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(synonym)

for el in synonym_dict:
    print(f'{el} - {", ".join(synonym_dict[el])}')
