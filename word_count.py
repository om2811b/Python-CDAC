import csv
with open("notes.txt", "r") as file:
    text = file.read().lower()

punctuation = ".,!?;:\"'#()"

for ch in punctuation:
    text = text.replace(ch, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

with open("word_count.txt", "w") as file:
    for word, count in sorted_words:
        file.write(word + " : " + str(count) + "\n")
