from stats import num_words_text, num_chars_in_text, sorted_dict_chars

__frank_relative_filepath__ = "books/frankenstein.txt"

def main():
    book_report(__frank_relative_filepath__)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def pretty_format_chars(sorted_chars):
    for elem in sorted_chars:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["num"]}")
    
def book_report(filepath):
    text = get_book_text(filepath)
    num_words = num_words_text(text)
    num_chars = num_chars_in_text(text)
    sorted_chars = sorted_dict_chars(num_chars)
    #Print formatting
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    pretty_format_chars(sorted_chars)
    print("============= END ===============")

main()