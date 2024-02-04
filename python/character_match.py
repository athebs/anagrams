# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	first_string= string1.lower()
	second_string= string2.lower()
	if len(first_string) != len(second_string):
		return False
	comparision_string= ''
	for char in first_string:
		if char in second_string: 
			comparision_string += char 
	if len(comparision_string)== len(second_string):
		return True
	else:
		return False 



# Part 2
def anagrams_for(word, list_of_words):
	# your code here
	pass
# print(is_character_match('charm', 'march'))
# print(is_character_match('zach2', 'attAck'))
