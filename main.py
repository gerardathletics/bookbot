import sys
from stats import get_num_words, count_each_letter, get_sorted_letters, sort_characters_by_count


def get_book_text(book_name):
    with open(book_name, "r") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words_str = get_num_words(text)
    num_words = int(num_words_str.split()[0])

    letter_counts = count_each_letter(text)
    sorted_char_list = sort_characters_by_count(letter_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
