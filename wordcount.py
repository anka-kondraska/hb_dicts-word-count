# put your code here.
text = open("test.txt")

word_count =  {}

for line in text:
    words = line.rstrip().split(" ")
    for word in words:
        word = word.lower().strip(',.!?')
        word_count[word] = word_count.get(word, 0) + 1

print word_count