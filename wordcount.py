# put your code here.
from sys import argv
from collections import Counter

filename = argv[1]

text = open(filename)

# word_count =  {}

# for line in text:
#     words = line.rstrip().split(" ")
#     for word in words:
#         word = word.lower().strip(',.!?:;"_')
#         word_count[word] = word_count.get(word, 0) + 1


# for word, value in word_count.iteritems():
#     print word, value
#print sorted(word_count.items(), key = lambda x: x[1])

words=[]
for line in text:
    words.extend(line.rstrip().split(" "))
c = Counter(words)
print sorted(c.items(), key = lambda x: x[1])
