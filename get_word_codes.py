def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value is a list of the character codes of the letters
        of the word that is its key"""
    return {key : [ord(w) for w in key] for key in words}

words = ['yes', 'no']
codes = get_word_codes(words)
print (codes)

