# Dr. Paul Tarau’s Assignment
"""
Write a Python 3 program that:
- reads  a text document stored in a file
- counts how many times each token (word, punctuation or number) occurs in the file
- prints out the 5 most frequently occurring tokens, together with their occurrence count, one per line

Skills needed:

- reading a file into a string
- splitting a string into a list of tokens
- use of dictionaries
- iteration over lists and a dictionaries
- use of a sorting algorithm, built in the Python system

"us_constitution.txt" in this directory, for testing your code.
"""

with open ("constitution.txt", "r") as a:
    contents = a.read()
    print (contents)
    SplitIt =contents.split()

counts = {}
for name in SplitIt:
    SplitContents = name.split(contents)

    if name not in counts:
        counts[name] = 1
    else :

        counts[name] = counts[name] + 1
#print (counts)
print (sorted(counts.items(),key=lambda x :x[1])[-5:])