import time

start_time = time.time()

# text files are unordered, new name on each line
# Hint: You might try importing a data structure you built during the week
# duplicates: 64
# non duplicates: 19876

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# O(n)
all_names = {}
dups = {}

# put all names from first file in dict
for name in names_1:
    all_names[name] = True

# check all names against first list dict, if same, put in dups dict
for name in names_2:
    try:
        if all_names[name]:
            dups[name] = True
    except:
        pass

duplicates = dups.keys()

# PROVIDED CODE
'''
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")