def wc(command, flags, params, output):
	wordCount = 0
	with open(params[0]) as treasure:
		for line in treasure:
			wordCount += len(line.split())
	print(wordCount)
	return