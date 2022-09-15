"""
File: boggle.py
Name:
----------------------------------------
This programs need to input thw word and find the neghibor can compose the  word in length 4 and in dictionary
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

word = []
big_lst = []

def main():
	"""
	TODO:
	"""
	read_dictionary()
	choose_the_word()
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	find_word()
	####################
	end = time.time()



	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word
	with open(FILE,'r')as f:
		for line in f:
			line_ = line.split(	)
			word.extend(line_)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# We need to reduce search times
	for i in word:
		if i.startswith(sub_s):
			return True
	return False



def find_word():
	# We need to use helper function to find the word)
	ans_ = []
	for pos in range(4*4):
		find_word_helper('',pos,[],ans_)
	print("There are "+str(len(ans_)) +"words in total")

def find_word_helper(s,pos,use_pos,ans_):

	global big_lst,word
	# to change the position into rows and columns
	row = pos//4
	col = pos % 4
	#  we need to add the string
	s += big_lst[row][col]
	use_pos.append(pos)
	# choose
	if len(s) >= 2 and not has_prefix(s):
		use_pos.pop()
		return
	# explore and unchoose
	elif len(s) >= 4 and (s in word) and (s not in ans_):
		print("Found:" + s)
		ans_.append(s)
	# We need to  make sure the condition that is in neghibor and rows and cols be positive
	for i in range(row-1,row+2):
		for j in range(col-1,col+2):
			n_pos = i * 4 + j
			if 4 > i >= 0 and 4 > j >= 0 and n_pos not in use_pos:
				find_word_helper(s,n_pos,use_pos,ans_)
	use_pos.pop()


def choose_the_word():
	# We need to let user to input the word

	a = str(input("1 row of letters:"))
	if len(a) == 7:
		str1 = a.lower()
		str2 = str1.split(' ')
		big_lst.append(str2)
	else:
		pass
	b = str(input("2 row of letters:"))
	if len(b) == 7:
		str3 = b.lower()
		str4 = str3.split(' ')
		big_lst.append(str4)
	else:
		pass
	c = str(input("3 row of letters:"))
	if len(c) == 7:
		str5 = c.lower()
		str6 = str5.split(' ')
		big_lst.append(str6)
	else:
		pass
	d = str(input("4 row of letters:"))
	if len(d) == 7:
		str7 = d.lower()
		str8 = str7.split(' ')
		big_lst.append(str8)
	else:
		pass

	return big_lst


if __name__ == '__main__':
	main()
