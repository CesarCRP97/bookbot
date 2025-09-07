from stats import num_words_text, num_chars_in_text

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = num_words_text(text)
    char_dict = num_chars_in_text(text)
    print(f"{num_words} words found in the document")
    print(char_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

main()