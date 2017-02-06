def varXor(string1, string2):
	varx = int(string1, 16) ^ int(string2, 16)
	return '%x' % varx

string1 = raw_input("String 1: ")
string2 = raw_input("String 2: ")

print varXor(string1, string2)
