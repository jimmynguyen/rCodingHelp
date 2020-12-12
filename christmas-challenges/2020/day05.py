# You can't have Christmas without a tree! (Day 5)
# Challenge :
# Write a program that prints an ascii Christmas tree to the console - up to you what it looks like! The user must be prompted to enter the height of the tree.
import random
import sys
import time

# get height
question = "How big of a tree are we looking for?\n>> "
while True:
    try:
        h = int(input(question))
        if h <= 0:
            raise ValueError
        break
    except ValueError:
        question = "Invalid height. Please enter a valid numerical value greater than 0\n>> "

# build tree layers
ornaments = ["i","+","O"]
tree = ["+","A"]
for i in range(h):
    if i == 0:
        layer = "/ \\"
    elif i % 3 == 0:
        layer = "/" + ("=" * len(tree[-1][1:-1])) + "\\"
    else:
        length = len(tree[-1])
        idx_ornament = i%3
        layer = ornaments[idx_ornament]
        idx_ornament = (idx_ornament + 1) % 3
        for j in range(0,length//2):
            if j % 2 == 0:
                layer = " " + layer + " "
            else:
                layer = ornaments[idx_ornament] + layer + ornaments[idx_ornament]
                idx_ornament = (idx_ornament + 1) % 3
        layer = "/" + layer + "\\"
    tree.append(layer)
tree[-1] = "/" + "=" * len(tree[-1][1:-1]) + "\\"

# create tree with padding
max_length = len(tree[-1])
if h <= 2:
    tree.append("|")
else:
    tree.append("|_|")
for i,layer in enumerate(tree):
    padding = " " * (((max_length - len(layer)) // 2) + max_length)
    tree[i] = padding + layer + padding
tree = "\n".join(tree)

# draw tree and animate
num_flakes = max(5,len(tree)//18)
num_loops = 10
for i in range(num_loops):
    tree = tree.replace("*"," ")
    for _ in range(num_flakes):
        while True:
            idx = random.randint(0,len(tree)-1)
            if tree[idx] == " ":
                tree = tree[:idx] + "*" + tree[idx+1:]
                break
    print(tree)
    if i < num_loops - 1:
        sys.stdout.write("\033[{}F".format(tree.count("\n")+1))
    time.sleep(1)