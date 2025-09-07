from stats import get_book_text, num_words_text

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = num_words_text(text)
    print(f"{num_words} words found in the document")


main()