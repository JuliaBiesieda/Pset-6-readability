from cs50 import get_string

text = get_string("Text: ").lower()
print(f"The length is {len(text)}")

letters = 0
words = 0
sentences = 0


for i in text:
    # this loop looks through the string and calculates whitespaces

    # this loop excludes symbols and only calculates letters
    if i.isalpha():
        letters += 1

    # this loop calculates symbols aka number of sentences
    if i == "!" or i == "?" or i == ".":
        sentences += 1

words += len(text.split())

# print(words)
# print(letters)
# print(sentences)

average_letters = 100 * (letters / words)
average_words = 100 * (sentences / words)
index = round(0.0588 * average_letters - 0.296 * average_words - 15.8)

# print(average_letters)
# print(average_words)
# print(f"index is {index}")

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")