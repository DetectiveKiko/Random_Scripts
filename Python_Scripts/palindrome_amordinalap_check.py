import nltk
from nltk.corpus import wordnet
from english_words import get_english_words_set

# Download WordNet once (it will skip if already downloaded)
nltk.download('wordnet', quiet=True)

# Load English word set
english_words_set = get_english_words_set(['web2', 'gcide'])

# Normalize: make all words lowercase and keep only alphabetic ones
word_set = {w.lower() for w in english_words_set if w.isalpha()}


# Check if word is valid in any dictionary
def valid_word_anysource(w):
    w = w.lower()
    return (w in word_set) or bool(wordnet.synsets(w))


# Check if word is a palindrome
def is_palindrome(word):
    w = word.lower()
    return w == w[::-1]


# Check if word is an amordnalap (both word and reverse are valid words)
def is_amordnalap(word):
    w = word.lower()
    rev = w[::-1]
    return valid_word_anysource(w) and valid_word_anysource(rev)


# Print result for palindrome
def print_palindrome(word):
    if is_palindrome(word):
        print(f"'{word}' is a palindrome!")
    else:
        print(f"'{word}' is NOT a palindrome.")


# Print result for amordnalap
def print_amordnalap(word):
    if is_amordnalap(word):
        print(f"'{word}' is an amordnalap! ({word} ↔ {word[::-1]})")
    else:
        print(f"'{word}' is NOT an amordnalap.")


# Interactive user input
def intercative_user_input():
    print("🌀 Palindrome & Amordnalap Checker 🌀")
    print("Type a word to check (or type 'exit' to quit):\n")

    while True:
        word = input("Enter a word: ").strip()
        if word.lower() == "exit":
            print("Goodbye! 👋")
            break

        if not word.isalpha():
            print("Please enter alphabetic words only.\n")
            continue

        print_palindrome(word)
        print_amordnalap(word)
        print()  # newline for spacing


# Run main function
if __name__ == "__main__":
    intercative_user_input()
