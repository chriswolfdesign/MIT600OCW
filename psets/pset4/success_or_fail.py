#
# success_or_fail.py
#
# A module that will allow a user to create test methods much more easily
# with color-coding and functions that tell them whether or not they passed
# a test inside of their conditional statements.
#
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Version: July 8, 2017
#

from colors import *

"""
success(function_call, expected_result, received_result)

This function takes in the function_call you are attempting to debug.  The
program will then announce that the function_call was performed correctly.
If user provides expected_result and received_result, the program will also
print those for the user to see and add to their data.

function_call: string - A string representation of the function you just
						called.  User is responsible for this representation.

expected_result: string - A string representation of the output you expected
                          your program to provide.
                 
				 Default = ''

received_result: string - A string representation of the output your program
						  actually provided.

				 Default = ''

return: None
"""
def success(function_call, expected_result='', received_result=''):
	
	print
	print blue('-------------------------------------------------------------')
	print blue('SUCCESS: ' + str(function_call))

	if not (expected_result == '' and received_result == ''):
		print
		print blue('    Expected result: ' + str(expected_result))
		print blue('    Received result: ' + str(received_result))

	print blue('-------------------------------------------------------------')
	print

"""
fail(function_call, expected_result, received_result)

This function takes in the function_call you are attempting to debug.  The
program will then announce that the function_call was performed incorrectly.
If user provides expected_result and received_result, the program will also
print those for the user to see and add to their data.

function_call: string - A string representation of the function you just
						called.  User is responsible for this representation.

expected_result: string - A string representation of the output you expected
                          your program to provide.
                 
				 Default = ''

received_result: string - A string representation of the output your program
						  actually provided.

				 Default = ''

return: None
"""
def fail(function_call, expected_result='', received_result=''):
	
	print
	print red('-------------------------------------------------------------')
	print red('FAIL: ' + str(function_call))

	if not (expected_result == '' and received_result == ''):
		print
		print red('    Expected result: ' + str(expected_result))
		print red('    Received result: ' + str(received_result))

	print red('-------------------------------------------------------------')
	print


