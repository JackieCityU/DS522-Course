text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

words_to_remove = ['is', 'better', 'than']

# Convert to lowercase first to ensure all matches are caught
clean_text = text.lower()

# Loop through our removal list and replace words with empty strings
for word in words_to_remove:
    
    clean_text = clean_text.replace(f" {word} ", " ")

print("Final Text:")
print(clean_text)