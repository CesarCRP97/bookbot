def num_words_text(text):
    words = text.split()
    return len(words)


def num_chars_in_text(text):
    char_dictionary = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in char_dictionary:
            char_dictionary[c] += 1
        else:
            char_dictionary[c] = 1
    return char_dictionary
        
