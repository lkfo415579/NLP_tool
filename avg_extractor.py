def read_corpus(dir):
	print '########Reading Corpus_' + ' From file "' + dir + '"###########'
	file = open(dir, 'r')

	def number_file(dir):
		with open(dir) as f:
			return sum(1 for _ in f)

	#len_p = number_file(file)
	
	output_zh = open(dir+'.zh', "wa")
	output_en = open(dir+'.en', "wa")
	
	corpus = []
	with open(dir , 'r') as file:
		run = 0
		for line in file:
			run += 1
			if not (run % 2):
				zh_line = line
				output_zh.write(zh_line)
			else:
				en_line = line
				output_en.write(en_line)
	output_zh.close()
	output_en.close()
		
	print '########End###########'
	return 1

def extract():
	import sys
	if len(sys.argv) != 2:
		print 'Usage: python', sys.argv[0], 'input-file'
		exit()
	input_file = sys.argv[1]
	
	read_corpus(input_file)

if __name__ == "__main__":
	extract()