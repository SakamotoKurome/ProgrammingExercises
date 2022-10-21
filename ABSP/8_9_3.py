import os
import re
search_for = re.compile(r'\d+')
dir = os.getcwd()
for file in os.listdir(dir):
    if file.endswith('.txt'):
        with open(os.path.join(dir, file), 'r') as f:
            lines = f.readlines()
        for line in lines:
            if search_for.search(line) != None:
                print(line.strip())
