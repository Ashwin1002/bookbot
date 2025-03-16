from stats import get_word_count, get_character_count, get_sorted_character_count

import sys

def main():
    try:
        file_contents = get_book_text(sys.argv[1])
        num_words = get_word_count(file_contents)
        char_dict = get_character_count(file_contents)
        sorted_char_dict = get_sorted_character_count(char_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for k, v in sorted_char_dict.items():
            print(f"{k}: {v}")
        print("============= END ===============")
    except Exception as _:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()
