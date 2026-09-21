word = input("Enter a word: ")

for letter in word:
    print(letter)

number = 1

for letter in word:
    print(f"{number}. {letter}")
    number = number + 1

print(f"The word has {len(word)} letters.")
