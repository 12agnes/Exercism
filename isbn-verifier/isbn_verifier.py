import re 

def verify(isbn):

	if isbn == '':
		return False

	if re.findall(r'\d{10}[X]', isbn):
		if len(isbn) == 10:
			return True
		else:
			return False

	if re.findall(r'\d{10}', isbn):
		return True

	if re.findall(r'\d{9}[X]', isbn):
		return True

	if re.findall(r'\d{9}[0-8]', isbn):
		return False


		
	format_validate = re.findall(r'\d{1}\-\d{1,3}\-\d{1,5}\-[0-8]', isbn)

	if format_validate:
		return True
	if re.findall(r'\d{1}\-\d{3}\-\d{5}-\d{2}', isbn):
		return False
	if re.findall(r'\d{1}\-\d{3}\-\d{3}[1]\d{1}-[X]', isbn):
		return False
	if re.findall(r'\d{1}\-\d{1,3}\-\d{1,5}\-[X]', isbn):
		return True
	if re.findall(r'\d{1}\-\d{1,3}\-\d{1}[A-Z]\d{1,3}\-[0-8]', isbn):
		return False
	if re.findall(r'\d{1}\-\d{1,3}\-\d{1,3}', isbn):
		return False
	else:
		return False