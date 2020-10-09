def pairs(iterator):
	iterator = iterator.__iter__()
	first,second = iterator.__next__(),iterator.__next__()
	while True:
			yield first,second
			try:
				first = iterator.__next__()
			except StopIteration:
				break
			try:
				second = iterator.__next__()
			except StopIteration:
				yield first,None
				break
#print(*map(lambda p:chr(int(''.join(p),16)),pairs(input())),sep="")
print(*map(lambda p:int(''.join(p),16),pairs(input())))
