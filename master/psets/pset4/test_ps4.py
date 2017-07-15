# 
# test_ps4.py
#
# A temporary file to test the activities in ps4.py
#
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Version: July 8, 2017
#

from success_or_fail import *
from ps4 import *

def test_find_inverse():
	
	# find_inverse(-1)
	function_call = 'find_inverse(-1)'
	expected_output = 26
	received_output = find_inverse(-1)

	if expected_output == received_output:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# find_inverse(-10)
	function_call = 'find_inverse(-10)'
	expected_output = 16
	received_output = find_inverse(-11)

	if expected_output == received_output:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	#find_inverse(-26)
	function_call = 'find_inverse(-27)'
	expected_output = 0
	received_output = find_inverse(-27)

	if expected_output == received_output:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)

def test_build_coder():
	
	# build_coder(2)
	function_call = 'build_coder(2)'
	expected_output = {' ' : 'b', \
	                   'a' : 'c', \
					   'b' : 'd', \
					   'c' : 'e', \
					   'd' : 'f', \
					   'e' : 'g', \
					   'f' : 'h', \
					   'g' : 'i', \
					   'h' : 'j', \
					   'i' : 'k', \
					   'j' : 'l', \
					   'k' : 'm', \
					   'l' : 'n', \
					   'm' : 'o', \
					   'n' : 'p', \
					   'o' : 'q', \
					   'p' : 'r', \
					   'q' : 's', \
					   'r' : 't', \
					   's' : 'u', \
					   't' : 'v', \
					   'u' : 'w', \
					   'v' : 'x', \
					   'w' : 'y', \
					   'x' : 'z', \
					   'y' : ' ', \
					   'z' : 'a'}

	received_output = build_coder(2)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_coder(-10)
	function_call = 'build_coder(-10)'
	expected_output = {' ' : 'q', \
	                   'a' : 'r', \
					   'b' : 's', \
					   'c' : 't', \
					   'd' : 'u', \
					   'e' : 'v', \
					   'f' : 'w', \
					   'g' : 'x', \
					   'h' : 'y', \
					   'i' : 'z', \
					   'j' : ' ', \
					   'k' : 'a', \
					   'l' : 'b', \
					   'm' : 'c', \
					   'n' : 'd', \
					   'o' : 'e', \
					   'p' : 'f', \
					   'q' : 'g', \
					   'r' : 'h', \
					   's' : 'i', \
					   't' : 'j', \
					   'u' : 'k', \
					   'v' : 'l', \
					   'w' : 'm', \
					   'x' : 'n', \
					   'y' : 'o', \
					   'z' : 'p'}

	received_output = build_coder(-10)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_coder(27)
	function_call = 'build_coder(27)'
	expected_output = {' ' : ' ', \
	                   'a' : 'a', \
					   'b' : 'b', \
					   'c' : 'c', \
					   'd' : 'd', \
					   'e' : 'e', \
					   'f' : 'f', \
					   'g' : 'g', \
					   'h' : 'h', \
					   'i' : 'i', \
					   'j' : 'j', \
					   'k' : 'k', \
					   'l' : 'l', \
					   'm' : 'm', \
					   'n' : 'n', \
					   'o' : 'o', \
					   'p' : 'p', \
					   'q' : 'q', \
					   'r' : 'r', \
					   's' : 's', \
					   't' : 't', \
					   'u' : 'u', \
					   'v' : 'v', \
					   'w' : 'w', \
					   'x' : 'x', \
					   'y' : 'y', \
					   'z' : 'z'}

	received_output = build_coder(27)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
def test_build_encoder():
	
	# build_encoder(2)
	function_call = 'build_encoder(2)'
	expected_output = {' ' : 'b', \
	                   'a' : 'c', \
					   'b' : 'd', \
					   'c' : 'e', \
					   'd' : 'f', \
					   'e' : 'g', \
					   'f' : 'h', \
					   'g' : 'i', \
					   'h' : 'j', \
					   'i' : 'k', \
					   'j' : 'l', \
					   'k' : 'm', \
					   'l' : 'n', \
					   'm' : 'o', \
					   'n' : 'p', \
					   'o' : 'q', \
					   'p' : 'r', \
					   'q' : 's', \
					   'r' : 't', \
					   's' : 'u', \
					   't' : 'v', \
					   'u' : 'w', \
					   'v' : 'x', \
					   'w' : 'y', \
					   'x' : 'z', \
					   'y' : ' ', \
					   'z' : 'a'}

	received_output = build_encoder(2)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_encoder(-10)
	function_call = 'build_encoder(-10)'
	expected_output = {' ' : 'q', \
	                   'a' : 'r', \
					   'b' : 's', \
					   'c' : 't', \
					   'd' : 'u', \
					   'e' : 'v', \
					   'f' : 'w', \
					   'g' : 'x', \
					   'h' : 'y', \
					   'i' : 'z', \
					   'j' : ' ', \
					   'k' : 'a', \
					   'l' : 'b', \
					   'm' : 'c', \
					   'n' : 'd', \
					   'o' : 'e', \
					   'p' : 'f', \
					   'q' : 'g', \
					   'r' : 'h', \
					   's' : 'i', \
					   't' : 'j', \
					   'u' : 'k', \
					   'v' : 'l', \
					   'w' : 'm', \
					   'x' : 'n', \
					   'y' : 'o', \
					   'z' : 'p'}

	received_output = build_encoder(-10)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_encoder(27)
	function_call = 'build_encoder(27)'
	expected_output = {' ' : ' ', \
	                   'a' : 'a', \
					   'b' : 'b', \
					   'c' : 'c', \
					   'd' : 'd', \
					   'e' : 'e', \
					   'f' : 'f', \
					   'g' : 'g', \
					   'h' : 'h', \
					   'i' : 'i', \
					   'j' : 'j', \
					   'k' : 'k', \
					   'l' : 'l', \
					   'm' : 'm', \
					   'n' : 'n', \
					   'o' : 'o', \
					   'p' : 'p', \
					   'q' : 'q', \
					   'r' : 'r', \
					   's' : 's', \
					   't' : 't', \
					   'u' : 'u', \
					   'v' : 'v', \
					   'w' : 'w', \
					   'x' : 'x', \
					   'y' : 'y', \
					   'z' : 'z'}

	received_output = build_encoder(27)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
def test_build_decoder():
	
	# build_decoder(2)
	function_call = 'build_decoder(2)'
	expected_output = {' ' : 'y', \
	                   'a' : 'z', \
					   'b' : ' ', \
					   'c' : 'a', \
					   'd' : 'b', \
					   'e' : 'c', \
					   'f' : 'd', \
					   'g' : 'e', \
					   'h' : 'f', \
					   'i' : 'g', \
					   'j' : 'h', \
					   'k' : 'i', \
					   'l' : 'j', \
					   'm' : 'k', \
					   'n' : 'l', \
					   'o' : 'm', \
					   'p' : 'n', \
					   'q' : 'o', \
					   'r' : 'p', \
					   's' : 'q', \
					   't' : 'r', \
					   'u' : 's', \
					   'v' : 't', \
					   'w' : 'u', \
					   'x' : 'v', \
					   'y' : 'w', \
					   'z' : 'x'}

	received_output = build_decoder(2)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_decoder(-10)
	function_call = 'build_decoder(-10)'
	expected_output = {' ' : 'j', \
	                   'a' : 'k', \
					   'b' : 'l', \
					   'c' : 'm', \
					   'd' : 'n', \
					   'e' : 'o', \
					   'f' : 'p', \
					   'g' : 'q', \
					   'h' : 'r', \
					   'i' : 's', \
					   'j' : 't', \
					   'k' : 'u', \
					   'l' : 'v', \
					   'm' : 'w', \
					   'n' : 'x', \
					   'o' : 'y', \
					   'p' : 'z', \
					   'q' : ' ', \
					   'r' : 'a', \
					   's' : 'b', \
					   't' : 'c', \
					   'u' : 'd', \
					   'v' : 'e', \
					   'w' : 'f', \
					   'x' : 'g', \
					   'y' : 'h', \
					   'z' : 'i'}

	received_output = build_decoder(-10)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
	# build_decoder(27)
	function_call = 'build_decoder(27)'
	expected_output = {' ' : ' ', \
	                   'a' : 'a', \
					   'b' : 'b', \
					   'c' : 'c', \
					   'd' : 'd', \
					   'e' : 'e', \
					   'f' : 'f', \
					   'g' : 'g', \
					   'h' : 'h', \
					   'i' : 'i', \
					   'j' : 'j', \
					   'k' : 'k', \
					   'l' : 'l', \
					   'm' : 'm', \
					   'n' : 'n', \
					   'o' : 'o', \
					   'p' : 'p', \
					   'q' : 'q', \
					   'r' : 'r', \
					   's' : 's', \
					   't' : 't', \
					   'u' : 'u', \
					   'v' : 'v', \
					   'w' : 'w', \
					   'x' : 'x', \
					   'y' : 'y', \
					   'z' : 'z'}

	received_output = build_decoder(27)

	is_same = True

	for letter in expected_output:
		if not expected_output[letter] == received_output[letter]:
			is_same = False
	
	if is_same:
		success(function_call)
	else:
		fail(function_call, expected_output, received_output)
	
def test_apply_coder():
	
	# apply_coder('Hello!', build_encoder(3))
	function_call = 'apply_coder(\'Hello\', build_encoder(3))'
	expected_result = 'Khoor!'
	received_result = apply_coder('Hello!', build_encoder(3))

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	
	# apply_coder('Ifmmp,anzaobnfajtaDisjt!', build_decoder(1))
	function_call = 'apply_coder(\'Ifmmp,anzaobnfajtaDisjt!\', ' + \
		'build_decoder(1))'
	expected_result = 'Hello, my name is Chris!'
	received_result = apply_coder('Ifmmp,anzaobnfajtaDisjt!', \
		build_decoder(1))
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# apply_coder('It's a pleasure to meet you, Chris!', build_decoder(-27))
	function_call = 'apply_coder(\'It\'s a pleasure to meet you, Chris!\'' + \
		', build_decoder(-27))'
	expected_result = 'It\'s a pleasure to meet you, Chris!'
	received_result = apply_coder('It\'s a pleasure to meet you, Chris!', \
		build_decoder(-27))
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

def test_apply_shift():
	
	# apply_coder('Hello!', 3)
	function_call = 'apply_coder(\'Hello\', 3)'
	expected_result = 'Khoor!'
	received_result = apply_shift('Hello!', 3)

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	
	# apply_coder('Ifmmp,anzaobnfajtaDisjt!', 26)
	function_call = 'apply_coder(\'Ifmmp,anzaobnfajtaDisjt!\', 26)'
	expected_result = 'Hello, my name is Chris!'
	received_result = apply_shift('Ifmmp,anzaobnfajtaDisjt!', 26)
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# apply_coder('It's a pleasure to meet you, Chris!', -27)
	function_call = 'apply_coder(\'It\'s a pleasure to meet you, Chris!\', 27)'
	expected_result = 'It\'s a pleasure to meet you, Chris!'
	received_result = apply_shift('It\'s a pleasure to meet you, Chris!', 27)
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)


def test_find_best_shift():
	
	# find_best_shift(wordlist, apply_coder('Hello, world!', 5))	
	function_call = 'find_best_shift(wordlist, apply_shift(' + \
		'\'Hello, world!\', 5))'
	expected_result = 5
	received_result = find_best_shift(wordlist, \
		apply_shift('Hello, world!', 5))

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# find_best_shift(wordlist, apply_coder('I like Computer Science!', 12))
	function_call = 'find_best_shift(wordlist, apply_shift(' + \
		'\'I like Computer Science!\', 12))'
	expected_result = 12
	received_result = find_best_shift(wordlist, \
		apply_shift('I like Computer Science!', 12))
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# find_best_shift(wordlist, apply_coder('Prgramming is hard!', 0))
	function_call = 'find_best_shift(wordlist, apply_shift(' + \
		'\'Programming is hard!\', 0))'
	expected_result = 0
	received_result = find_best_shift(wordlist, \
		apply_shift('Programming is hard!', 0))
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)


def test_apply_shifts():

	# test_apply_shifts('Do Androids Dream of Electric Sheep?, 
	# 	[(0, 6), (3, 18), (12, 16)])
	function_call = 'apply_shifts(\'Do Androids Dream of Electric' + \
		'Sheep?\', [(0, 6), (3, 18), (12, 16)])'
	expected_result = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
	received_result = apply_shifts('Do Androids Dream of Electric Sheep?', \
		[(0, 6), (3, 18), (12, 16)])
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# test_apply_shifts('Hello, world!', [(0, 5), (2, 19), (7, 21)])
	function_call = 'apply_shifts(\'Hello, world!\',' + \
		'[(0, 5), (2, 19), (7, 21)])'
	expected_result = 'Mjiil,xnficv!'
	received_result = apply_shifts('Hello, world!', [(0, 5), (2, 19), (7, 21)])

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	# test_apply_shifts('Programming is fun!', [(0, 3), (7, 2), (11, 4)])
	function_call = 'apply_shifts(\'Programming is fun!\', ' + \
		'[(0, 3), (7, 2), (11, 4)])'
	expected_result = 'Surjudprnsliraiocw!'
	received_result = apply_shifts('Programming is fun!', \
		[(0, 3), (7, 2), (11, 4)])
	
	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

def test_find_best_shifts():
	expected_result = 'Do Androids Dream of Electric Sheep?'
	encrypted_text = apply_shifts('Do Androids Dream of Electric Sheep?', \
		[(0, 6), (3, 18), (12, 16)])
	correct_shifts = find_best_shifts(wordlist, encrypted_text)
	received_result = apply_shifts(encrypted_text, correct_shifts)
	function_call = 'Do Androids Dream of Electric Sheep?'

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	expected_result = 'I like Computer Science!'
	encrypted_text = apply_shifts('I like Computer Science!', \
		[(0, 5), (2, 16), (7, 12)])
	correct_shifts = find_best_shifts(wordlist, encrypted_text)
	received_result = apply_shifts(encrypted_text, correct_shifts)
	function_call = 'I like Computer Science!'

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

	expected_result = 'This homework has made me angry!'
	encrypted_text = apply_shifts('This homework has made me angry!', [(0, 3), (5, 4), (14, 24), (18, 2)])
	correct_shifts = find_best_shifts(wordlist, encrypted_text)
	received_result = apply_shifts(encrypted_text, correct_shifts)
	function_call = 'This homework has made me angry!'

	if expected_result == received_result:
		success(function_call)
	else:
		fail(function_call, expected_result, received_result)

if __name__ == '__main__':

	print
	
	print purple('-----------------------------------------------------------')
	print purple('test_find_inverse()')
	print purple('-----------------------------------------------------------')
	test_find_inverse()
	
	print purple('-----------------------------------------------------------')
	print purple('test_build_coder()')
	print purple('-----------------------------------------------------------')
	test_build_coder()

	print purple('-----------------------------------------------------------')
	print purple('test_build_encoder()')
	print purple('-----------------------------------------------------------')
	test_build_encoder()

	print purple('-----------------------------------------------------------')
	print purple('test_build_decoder()')
	print purple('-----------------------------------------------------------')
	test_build_decoder()

	print purple('-----------------------------------------------------------')
	print purple('test_apply_coder()')
	print purple('-----------------------------------------------------------')
	test_apply_coder()

	print purple('-----------------------------------------------------------')
	print purple('test_apply_shift()')
	print purple('-----------------------------------------------------------')
	test_apply_shift()

	print purple('-----------------------------------------------------------')
	print purple('test_find_best_shift()')
	print purple('-----------------------------------------------------------')
	test_find_best_shift()

	print purple('-----------------------------------------------------------')
	print purple('test_apply_shifts()')
	print purple('-----------------------------------------------------------')
	test_apply_shifts()

	print purple('-----------------------------------------------------------')
	print purple('test_find_best_shifts()')
	print purple('-----------------------------------------------------------')
	test_find_best_shifts()
