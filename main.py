from spellchecker import SpellChecker

def create_word_set(filepath):
    # create a spell checker object
    spell = SpellChecker()

    # download the text file and create a set of words
    with open(filepath, "r") as file:
        text = file.read().split()
        words = set(text)
    
    
    
    # remove conjunction words
    conjunctions = {"and", "or", "but", "for", "so"}
    words.difference_update(conjunctions)
    
    return words, spell
    
    return words, spell

def spell_check_user_word(words, spell):
    # prompt the user to input a word to spell check
    word = input("Enter a word to spell check: ")

    # create a list of suggested corrections for the word
    corrections = spell.candidates(word)

    # if the word is misspelled, print the suggested corrections
    if word not in words:
        print(f"Misspelled word: {word}")
        if len(corrections) > 0:
            print(f"Suggested corrections: {corrections}")
        else:
            print("No suggested corrections found.")
    else:
        print("Word is spelled correctly!")

# specify the path of the text file to download
filepath = r"C:\Users\user\Desktop\SpellCheckerOffline\env\files\Convolutional_MKL_Based_Multimodal.txt"

# create a set of words and a spell checker object from the downloaded text file
words, spell = create_word_set(filepath)

# prompt the user to input a word to spell check
spell_check_user_word(words, spell)
