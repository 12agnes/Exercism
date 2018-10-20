def is_pangram(sentence):
	small = set()
	# iterate over characters inside sentence
	for character in sentence:
		# if character found inside the set
		try:
			if character.isalpha():
				small.add(character.lower())
		except:
			raise Exception("the sentence is not qualified to be pangram")
	return len(small) == 26