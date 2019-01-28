from basics import scrabble

for word in scrabble.wordlist:
    if "oo" in word and "aa" in word:
        print(word)

print("==============================")

for word in scrabble.wordlist:
    if "q" in word and "u" not in word:
        print(word)

print("==============================")

letters = "qwertyuiopasdfghjklzxcvbnm"


def has_double(letter):
    for word in scrabble.wordlist:
        if letter+letter in word:
            return True
    return False


for letter in letters:
    if not has_double(letter):
        print(letter + " never appears doubled")

print("==============================")

vowels = "aeiou"


def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
