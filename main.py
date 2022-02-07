import string

LOGO = '''
 .  .  _   _   __  _    _  _   _   _    _  _  .  ..    . _  _ ___ _  _  
 |\/| / \ |_) (_  |_   /  / \ | \ |_   /  / \ |\ | \  / |_ |_) | |_ |_) 
 |  | \_/ | \ __) |_   \_ \_/ |_/ |_   \_ \_/ | \|  \/  |_ | \ | |_ | \ 
                                                                                                                                         
'''


# For space in sentence I set "/"
LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "
]
MORSE_LETTERS = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", '.-..', "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---",
    "...--", "....-", ".....", "-....", "--...", "---..", "----.", "/"
]
MORSE_DICTIONARY = {k: v for k, v in zip(LETTERS, MORSE_LETTERS)}


def string_to_morse(sentence):
    morse_code = [
        MORSE_DICTIONARY[letter] for letter in sentence.lower()
    ]
    return " ".join(morse_code)


def morse_to_string(morse_code):
    split_sentence = morse_code.split(" ")
    print(split_sentence)
    # We can get the key value in python list using list.index() function
    # When I didn't have ready lists of morse letters and letters
    # I would make it like this:
    # letters = list(MORSE_DICTIONARY.keys())
    # morse_letters = list(MORSE_DICTIONARY.values())
    sentence = [
        LETTERS[MORSE_LETTERS.index(code)] for code in split_sentence
    ]
    return "".join(sentence)


print(LOGO)
user_input = input("Type here what you need to translate to morse code: ")
print(string_to_morse(user_input))
print(morse_to_string(string_to_morse(user_input)))


# def sentence_to_morse(user_input):
#     sentence_list = user_input.split(" ")
#     morse_world_list = [
#         string_to_morse(word) for word in sentence_list
#     ]
#     return " / ".join(morse_world_list)

# A	.-
# B	-...
# C	-.-.
# D	-..
# E	.
# F	..-.
# G	--.
# H	....
# I	..
# J	.---
# K	-.-
# L	.-..
# M	--
# N	-.
# O	---
# P	.--.
# Q	--.-
# R	.-.
# S	...
# T	-
# U	..-
# V	...-
# W	.--
# X	-..-
# Y	-.--
# Z	--..
# 0	-----
# 1	.----
# 2	..---
# 3	...--
# 4	....-
# 5	.....
# 6	-....
# 7	--...
# 8	---..
# 9	----.
