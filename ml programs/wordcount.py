from collections import Counter
import string
file_name = "C:\Users\kodid\OneDrive\Documents\ bharath.txt"
word_counts = Counter()
with open(file_name, 'r') as file:
 for line in file:
  line = line.translate(str.maketrans('', '', string.punctuation)).lower()
 words = line.split()
 word_counts.update(words)
for word, count in word_counts.items():
 print(f"'{word}' appears {count} times in {file_name}.")
