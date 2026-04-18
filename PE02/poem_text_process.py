from collections import Counter

import string

file = open("/Users/jackie/DS522/DS522-Course/PE02/poem.txt")
print(file.read())

#opening the file
with open("/Users/jackie/DS522/DS522-Course/PE02/poem.txt", "r") as file:
    text = file.read()
print(text.rstrip())

#Remove the punctuation marks
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator).lower()
print(clean_text)

#3.	Using a dictionary, count the number of times each 
# character appears in the text.
char_count = Counter(char for char in clean_text if char not in [" ", "\n"])
print(char_count)

#4.	Using a separate dictionary, 
# count the number of times each word appears in the text.
words = clean_text.split()
word_count = Counter(words) 
print(word_count)

#5.	Finally, remove the word or words 
# with the highest amount of frequency.
max_freq = max(word_count.values())

# Find most frequent words
most_frequent_words = [word for word, count in word_count.items() if count == max_freq]
# Removing the frquent words
filtered_words = [word for word in words if word not in most_frequent_words]
# Reconstruct text
filtered_text = " ".join(filtered_words)
print("\nMost Frequent Words Removed:\n", most_frequent_words)
print("\nFiltered Text:\n", filtered_text)

#Question: What is the importance of text 
# processing or provide an example use of text 
# processing.
### Text processing helps computers in understanding and analyzing human language
### efficiently, e.g spam email detection, it helps identify
### suspicious words that occur frequently plus patterns to tell
### if email is a spam or not.



