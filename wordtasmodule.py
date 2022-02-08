# MIT License

# Copyright (c) 2022 Joshua McGuire

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import wordfreq

english_language = set(())

with open('Scowl95', 'r') as Scowl:
    for word in Scowl:
        english_language.add(word.strip().lower())


## Takes the number of letters as a parameter
## Returns a dictionary of matching words and their usage frequency

def generate_candidates(number_of_letters: int = 5, 
                        word_set: set = english_language) -> dict:
    
    invalid_words = set(())
    word_dict = dict()

    for word in word_set:
        if len(word) != number_of_letters:
            invalid_words.add(word)
        if '\'' in word or '.' in word:
            invalid_words.add(word)
    
    word_set = word_set - invalid_words
    word_dict = dict.fromkeys(word_set, 0)

    for word in word_dict:
        word_dict[word] = wordfreq.zipf_frequency(word, 'en')
    
    return word_dict


## Takes the user's guess and wordle's outputs as parameters
## Returns a refined list of word candidates

def refine_candidates(guess: str, green_letters: str,
                      yellow_letters: str, candidates: dict) -> dict:
    green_letters = green_letters.replace(' ', '')
    yellow_letters = yellow_letters.replace(' ', '')

    candidates = set(dict.fromkeys(candidates))
    valid_letters = set(yellow_letters)
    valid_indexes = []
    invalid_words = set(())\
    
    
    if green_letters != '':
        if green_letters.isalpha():
            for letter in green_letters:
                valid_indexes.append(guess.find(letter))
                valid_letters.add(letter)
        elif green_letters.isnumeric():
            for number in green_letters:
                valid_indexes.append(int(number) - 1)
                valid_letters.add(guess[int(number) - 1])
                

        for word in candidates:
            for index in valid_indexes:
                if word[index] != guess[index]:
                    invalid_words.add(word)

    invalid_letters = set(set(guess) - valid_letters)
    
    for word in candidates:
        for letter in valid_letters:
            if letter not in word:
                invalid_words.add(word)
        for letter in invalid_letters:
            if letter in word:
                invalid_words.add(word)

    valid_words = candidates - invalid_words

    return generate_candidates(word_set = valid_words)


## Takes the dictionary of valid words as a parameter
## Returns a list the top 5 best guesses based on word usage

def generate_guess(candidates: dict) -> list:
    usage_values = list(candidates.values())
    usage_values.sort(reverse = True)
    top_values = usage_values[0:5]
    guesses = []
    best_guesses = []

    for word in candidates:
        for value in top_values:
            if candidates[word] == value:
                guesses.append(word)
    
    for word in guesses:
        if word not in best_guesses:
            best_guesses.append(word)
    
    return best_guesses