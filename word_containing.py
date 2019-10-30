def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    word_list=sentence.split()
    capital_letter = letter.capitalize()
    letter_word=[
		word 
		for word in word_list 
		if letter in word or capital_letter in word 
	]
    return letter_word
    
sentence = "Anyone who has never made a mistake has never tried anything new"
print (words_containing(sentence, 'a'))
