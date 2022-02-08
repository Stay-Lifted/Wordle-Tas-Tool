# Wordle Tas Tool
## Terminal application for solving Wordle puzzles

Wordle Tas Tool (WTT) is a Python script that iterates over SCOWL95 to solve Wordle puzzles.
Once the user inputs their guess and Wordle's reaction, WTT will remove invalid words and
suggest the user's next move using English word usage data.

This code was designed to be versatile and work in more contexts than standard Wordle
gameplay provides. Please feel free to modify the code or use it in your own projects!

## Running

`python3 wordletas.py`

## Python Dependancies

This project requires the packages wordfreq and colored. You can use the following commands
to install them:
```
pip install wordfreq
pip install colored
```

## Licensing

This code is open source under the MIT license. See license.txt for more information.

See SCOWL95 for licensing information. Special thanks to Kevin Atkinson, J Ross Beresford, 
Alan Beale, and everyone else involved for creating such an amazing resource.
