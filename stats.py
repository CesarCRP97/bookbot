def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def num_words_text(text):
    words = text.split()
    return len(words)



