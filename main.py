from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    only_alpha_char = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    for char in file_contents.lower():
        if char.isalpha():
            only_alpha_char += char 

    print(f"--- Begin report of", path_to_file, "---")
    print(word_count, "words found in the document\n")
    character_counted = character_count(only_alpha_char)
    sorted_character_counted = sort_by_value_desc_order(character_counted)
    print(list_chars(sorted_character_counted))


main()
