fname = input("Enter the name of the file:")
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
def l33t(word,infile):
	if char in word:
		if char in infile:
			char.replace('o','0')
			char.replace('o','0')
			char.replace('a','4')
			char.replace('A','4')
			char.replace('e','E')
			char.replace('E','3')
			char.replace('i','1')
			char.replace('er','xor')
		else:
			pass
for line in infile:
alphabets = line.split()
lines = lines + 1
words = words + len(alphabets)
characters = characters + len(line)
print(lines)
print(words)
print(characters)
