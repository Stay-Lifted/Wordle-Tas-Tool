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


import wordtasmodule
from colored import fg, attr

colored_green = fg('green')
colored_yellow = fg('yellow')
colored_reset = attr('reset')

def round_header(round_number: int = 1, words_left: int = -100):
    print('Round ' + str(round_number) + '. There are currently ' + str(words_left) + ' possible answers.')

def get_guess() -> str:
    print('Input your first guess.')
    guess = input('\nGuess: ')
    return guess

def get_green() -> str:
    print('\nWhich letters were ' + colored_green + 'green' + colored_reset + '?')
    print('If there were no green letters, press enter.')
    print('If the green letter occurs multiple times in a word but is only green once,')
    print('type the positions of the letters (example: 1 5)')
    green_letters = input('\n' + colored_green + 'Green Letters: ' + colored_reset)
    return green_letters

def get_yellow() -> str:
    print('\nWhich letters were ' + colored_yellow + 'yellow' + colored_reset + '?')
    print('If no letters were yellow, press enter.')
    yellow_letters = input('\n' + colored_yellow + 'Yellow letters: ' + colored_reset)
    return yellow_letters

def win_condition():
    is_looping = True
    while is_looping == True:
        print('\nDid that work?')
        answer = input('Y/N: ')
        if answer == 'Y' or answer == 'y':
            print('Nice!')
            exit()
        elif answer == 'N' or answer == 'n':
            break
        else:
            print('That last input didn\'t work :(')
            continue

def suggest(candidates: dict):
    guesses = wordtasmodule.generate_guess(candidates)

    if len(candidates) == 0:
        print('No good guesses were found :(')
        exit()
    elif len(candidates) == 1:
        print('The only valid guess left is ', guesses)
    else:
        print("Ok, it looks like the best guesses are going to be", guesses)