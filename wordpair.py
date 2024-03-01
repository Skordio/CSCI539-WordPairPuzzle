import random
import nltk

def is_nltk_data_downloaded(corpus_name):
    try:
        nltk.data.find(f'corpora/{corpus_name}')
        return True
    except LookupError:
        return False

if not is_nltk_data_downloaded('words'):
    print(f"nltk words corpus is not downloaded. Downloading now...")
    nltk.download('words')

from nltk.corpus import words

def find_two_words():
    word_list = words.words('en')
    while True:
        word = random.choice(word_list)
        while len(word) < 4:
            word = random.choice(word_list)
        last_3_letters = word[-3:]

        for w in word_list:
            if w.startswith(last_3_letters) and len(w) > 3 and w != word and len(w) == len(word):
                return word, w

def other_possible_matches(word1, word2):
    word_list = words.words('en')
    start_letters_word1 = word1[:len(word1)-3]
    end_letters_word2 = word2[3:]
    
    for w in word_list:
        if len(w) == len(word1) and w[:len(w)-3] == start_letters_word1 and w != word1:
            for w2 in word_list:
                if w2[3:] == end_letters_word2 and len(w2) == len(word2) and w2 != word2:
                    return True

def main():
    word1, word2 = find_two_words()
    while other_possible_matches(word1, word2):
        word1, word2 = find_two_words()
    print(word1, word2)
        
    pass

if __name__ == "__main__":
    main()