# put your code here.
text = open("twain.txt")

word_count =  {}

for line in text:
    words = line.rstrip().split(" ")
    for word in words:
        word = word.lower().strip(',.!?:;"_')
        word_count[word] = word_count.get(word, 0) + 1


for word, value in word_count.iteritems():
    print word, value
#print sorted(word_count.items(), key = lambda x: x[1])