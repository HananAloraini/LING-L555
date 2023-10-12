import sys


line = sys.stdin.readline()
counter = 1
while line:

	print('# sent_id = %d' % (counter))
	line = sys.stdin.readline()
	counter = counter + 1
	print('# text = %s' % (line))
	
	token = line.split(' ')
	counter1 = 1
	for c in token:
		print('# text = %d %s' % (counter1, c))
		counter1 = counter1 + 1
