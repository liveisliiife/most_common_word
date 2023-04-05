import os
my_dict = dict()
name = input("Enter filename:")
if not os.path.isfile(name):
    print("File not found")
    exit()

file = open(name)
for line in file:
    words = line.split()
    for word in words:
        my_dict[word] = my_dict.get(word,0) +1


max_count = -1
max_word = None
for word,count in my_dict.items():
    if max_count == -1 or count > max_count:
        max_word =word
        max_count = count

print(max_word,max_count)

file.close()