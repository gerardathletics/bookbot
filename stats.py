def get_num_words(text):
    num_words = len(text.split())

    return f"{num_words} words found in the document"


def count_each_letter(text):
    letters = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters


def get_sorted_letters(letters):
    sorted_letters = sorted(letters.items())
    return sorted_letters


def sort_characters_by_count(letters_dict):
    list_of_dicts = []
    for char, count in letters_dict.items():
        list_of_dicts.append({"char": char, "num": count})
    list_of_dicts.sort(key=lambda item: item["num"], reverse=True)
    return list_of_dicts
