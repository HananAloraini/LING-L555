import sys

line = sys.stdin.readline()
counter = 1

while line:
	line =  line.strip()

	if line == '':
		line = sys.stdin.readline()
		continue

	print('# sent_id = %d' % (counter))
	counter = counter + 1
	print('# text = %s' % line.strip())	

	punct = line
	punct = punct.replace('(', ' ( ')
	punct = punct.replace(')', ' ) ')
	punct = punct.replace(':', ' : ')
	punct = punct.replace('.', ' . ')
	punct = punct.replace(',', ' , ')
	punct = punct.replace('"', ' " ')
	token = punct.split(' ')
	counter1 = 1
	for c in token:
		if c.strip() == '':
			continue
		print('%d	%s	%s	%s	%s	%s	%s	%s	%s	%s' % (counter1,	c,	'_',	'_',	'_',	'_',	'_',	'_',	'_',	'_'))
		counter1 = counter1 + 1
	line = sys.stdin.readline()
	print()
