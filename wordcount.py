"""Count words in file."""

import sys

def word_count(file):

    log_file = open(file)

    word_count = {}

    for line in log_file:
        line = line.rstrip() #remove whitespace trailing each line, 
                            #otherwise you get "/n" at the end of each line
        line = line.rstrip(".")
        line = line.split(" ") #split each line into lists at the spaces

        for word in line:
            if word.lower() not in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1

    for word, count in word_count.items():
        print(word, count)

word_count("test.txt")


