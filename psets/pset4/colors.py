# colors.py
# 
# This is a helper module I created to aid in the debugging process.
# Using this process I can color-code my output.
# ex. Successes can be printed in blue (I use green as my default text in my
#     terminal.
# 	  Failures can be printed in red.
#
# Name: Chris Wolf
# Contact: chriswolfdesign@gmail.com
# Version: July 8, 2017

"""
red(string)

string: The string you wish to convert to a red font.
return: The string converted to the color red.
"""
def red(string):
	return '\033[91m{}\033[0m'.format(string)

"""
blue(string)

string: The string you wish to convert to a blue font.
return: The string converted to the color blue.
"""
def blue(string):
	return '\033[96m{}\033[0m'.format(string)

"""
green(string)

string: The string you wish to convert to a green font.
return: The string converted to the color green.
"""
def green(string):
	return '\033[92m{}\033[0m'.format(string)

"""
black(string)

string: The string you wish to convert to a black font.
return: The string converted to the color black.
"""
def black(string):
	return '\033[98m{}\033[0m'.format(string)

"""
purple(string)

string : The string you wish to conver to a purple font.
return: The string converted to the color purple.
"""
def purple(string):
	return '\033[95m{}\033[0m'.format(string)
