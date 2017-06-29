from ps3a import *
import time
from perm import *

def remove_duplicates(list):
    """
    Takes in a list and returns a new copy of the list, removing
    any duplicates

    list: The list we hope to remove duplicates from
    returns: a list with all duplicates removed
    """
    new_list = []

    for item in list:
        if not item in new_list:
            new_list.append(item)

    return new_list

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    possible_words = []
    for i in range(calculate_handlen(hand) + 1):
        possible_words = possible_words + get_perms(hand, i)

    possible_words = remove_duplicates(possible_words)

    best_score = 0
    best_word = '.'

    for word in possible_words:
        # If this is the best word we have found so far, update our variables
        if word in word_list and get_word_score(word, HAND_SIZE) > best_score:
            best_score = get_word_score(word, HAND_SIZE)
            best_word = word

    return best_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    score = 0

    # Clone the hand so the original can still be used later
    clone_hand = {}
    for letter in hand:
        clone_hand[letter] = hand[letter]

    while True:
        if calculate_handlen(clone_hand) < 1:
            print 'Total score {}'.format(score)
            print
            break

        print 'Current hand: ',
        display_hand(clone_hand)
        print 'Enter a word, or a "." to indicate that you are finished: ',
        word = comp_choose_word(clone_hand, word_list)
        print word

        if word == '.':
            print 'Total score: {}'.format(score)
            print
            break

        this_score = get_word_score(word, HAND_SIZE)
        score += this_score
        clone_hand = update_hand(clone_hand, word)
        print '"{}" earned {} points. Total score: {}'.format\
            (word, this_score, score)
        print

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = deal_hand(HAND_SIZE)
    choice = ' '
    while not choice == 'e':
        choice = ' '
        player = ' '
        while not (player == 'u' or player == 'c'):
            player = raw_input('Who would you like to play the next hand ' + \
                '(u: user, c: computer)? ')

        if player == 'c':
            comp_play_hand(hand, word_list)
        elif player == 'u':
            play_hand(hand, word_list)

        while not (choice == 'r' or choice == 'n' or choice == 'e'):
            choice = raw_input('Would you like to keep playing ' + \
                '(n: new hand, r: replay your last hand, e: exit game)? ')

        if choice == 'n':
            hand = deal_hand(HAND_SIZE)

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    hand = deal_hand(HAND_SIZE)
    play_game(word_list)
