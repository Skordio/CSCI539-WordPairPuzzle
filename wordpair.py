# run this in ubuntu

import random

def find_two_words():
    with open('/usr/share/dict/words') as wordlist:
        words = wordlist.read().split()
        while True:
            word = random.choice(words)
            while len(word) < 4:
                word = random.choice(words)
            last_3_letters = word[-3:]

            for w in words:
                if w.startswith(last_3_letters) and len(w) > 3 and w != word:
                    return word, w

def other_possible_matches(word1, word2):
    with open('/usr/share/dict/words') as wordlist:
        words = wordlist.read().split()
        start_letters_word1 = word1[:3]
        end_letters_word2 = word2[3:]
        
        for w in words:
            if w[:3] == start_letters_word1 and len(w) == len(word1) and w != word1:
                for w2 in words:
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