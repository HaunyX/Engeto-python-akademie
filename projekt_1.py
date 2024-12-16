"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author : Dominik Hauner
email  : haunerd@seznam.cz
"""
users_name_registred = {
    "bob" : "123",
    "ann" : "pass123",
    "mike": "password123",
    "liz" : "pass123"                                            
}
user_name = input("username : ")
user_password = input("password : ")
print("-"*40)
if user_name in users_name_registred:
    
    if users_name_registred[user_name] == user_password:
        print(f"Welcome to the app, {user_name}\nWe have 3 texts to be analyzed.")
        print("-"*40)
    
    else:
        print("unregistered user, terminating the program...")
        exit()
else:
    print("unregistered user, terminating the program...")
    exit()
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

numbers_of_texts = []
for numbers in range(len(TEXTS)):
    numbers_of_texts.append(str(numbers + 1))

choice = (input("Enter a number btw. 1 and 3 to select: "))

index = int(choice)
if choice in numbers_of_texts:
    
    words_in_TEXTS = TEXTS[index - 1].split()

    words_without_punctuation = []
    for word in words_in_TEXTS:
        clean_word = word.strip(",.?!:;()\"'")
        words_without_punctuation.append(clean_word)
    
    
    word_count = 0
    for word in words_in_TEXTS:
        word_count += 1
    print("-"*40)
    print(f"There are {word_count} words in the selected text.")

    title_word_count = 0
    for title_word in words_in_TEXTS:
        if title_word == title_word.title() and not title_word.isnumeric():
            title_word_count += 1
    print(f"There are {title_word_count} titlecase words.")

    uppercase_word_count = 0
    for upper_word in words_in_TEXTS:
        if upper_word == upper_word.upper() and not upper_word[0].isnumeric():
            uppercase_word_count += 1
    print(f"There are {uppercase_word_count} uppercase words.")

    lowercase_word_count = 0
    for lower_word in words_in_TEXTS:
        if lower_word == lower_word.lower() and not lower_word.isnumeric():
            lowercase_word_count += 1
    print(f"There are {lowercase_word_count} lowercase words.")

    numeric_string_count = 0
    for numeric_string in words_in_TEXTS:  
        if numeric_string.isdigit():
            numeric_string_count += 1
    print(f"There are {numeric_string_count} numeric strings.")
    
    number_count = 0
    for number in words_in_TEXTS:
        if number.isdigit():
            number_count += int(number)
    print(f"The sum of all the numbers {number_count}")
    print("-"*40)

    print("""LEN |   OCCURENCES     |NR.""")
    print("-"*40)

    index_list =[]

    for len_index in words_without_punctuation:
        len_index = len(len_index)
        index_list.append(len_index)
        index_list.sort()


    length_counts = {}
    for length in index_list:
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    sorted_lengths = sorted(length_counts.items())

    for length, count in sorted_lengths:
        print(f"{length:<4}|{'*' * count:<18}|{count}" )


elif not choice.isdigit():
    print("Zadalo jste jiný symbol než číslo.")

elif choice not in numbers_of_texts:
    print(f"Možnost {choice} není v možnostech.")