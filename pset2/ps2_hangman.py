# 6.00 Problem Set 3
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Time: 1:30
# Hangman
#

GUESSES_MAX = 8

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.

	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code
# -----------------------------------

def concealed_current_word(answer, found):
	"""
	answer (string): the correct answer for the game
	found (dict string -> Boolean): a dictionary representing whether or not
		a specific letter in our word had been guessed yet

	Returns a string of the answer with unguessed characters "hidden"
	"""

	cache = ''
	for letter in answer:
		if found[letter]:
			cache += letter
		else:
			cache += '_'
		cache += ' '
	return cache

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
answer = choose_word(wordlist)
guesses_left = GUESSES_MAX

found = {}
for letter in answer:
	found[letter] = False

available_letters = 'abcdefghijklmnopqrstuvwxyz'

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is', len(answer), 'letters long.'
print '------------'

while guesses_left > 0:
	print 'You have', guesses_left, 'guesses left'
	print 'Available letters:', available_letters

	current_guess = raw_input('Please guess a letter: ')
	current_guess = current_guess.lower()
	available_letters = available_letters.replace(current_guess, '')

	if current_guess in found:
		found[current_guess] = True
		print 'Good guess:', concealed_current_word(answer, found)
	else:
		guesses_left -= 1
		print 'Oops!  That letter is not in my word:', \
			concealed_current_word(answer, found)

	print '-----------'

	# See if the player has won the game and react accordingly
	game_won = True
	for letter in found:
		if not found[letter]:
			game_won = False

	if game_won:
		print 'Congrulations, you won!'
		break

	# See if the player has lost the game and react accordingly
	# BTW, I just lost The Game typing that last comment :_(
	if guesses_left < 1:
		print 'I\'m sorry, you are out of usable guesses'
		print 'Correct answer:', answer
