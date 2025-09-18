import sys
from stats import get_num_words, get_chars_dict, convert_sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_chars_dict(text)
    sorted_list = convert_sort(num_chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at " + book_path + "...")
    print(f"----------- Word Count ----------\nFound " + str(num_words) + " total words")
    print(f"--------- Character Count -------")
    for i in sorted_list:
        print (i["char"] + ": " + str(i["num"]))
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()