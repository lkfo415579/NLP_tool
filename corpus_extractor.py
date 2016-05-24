def read_corpus(dir,num_lines):
	print '########Reading Corpus_' + ' From file "' + dir + '"###########'
	file_en = open(dir + ".en", 'r')
	file_zh = open(dir + ".zh", 'r')
	file_en = tuple(file_en)
	file_zh = tuple(file_zh)
	
	def number_file(dir):
		with open(dir) as f:
			return sum(1 for _ in f)

	#len_p = number_file(file)
	
	output_zh = open(dir+'_'+str(num_lines)+'.zh', "wa")
	output_en = open(dir+'_'+str(num_lines)+'.en', "wa")
	
	
	numbers = range(len(file_en))
	
	import random
	random.shuffle(numbers)
	numbers = numbers[:1000]
	print "First 20 number of lines"
	print numbers[:20]


	#write en file
	for num in numbers:
		output_en.write(file_en[num])
	for num in numbers:
		output_zh.write(file_zh[num])
		
		
	output_zh.close()
	output_en.close()
		
	print '########End###########'
	return 1

def extract():
	import sys
	if len(sys.argv) != 3:
		print 'Usage: python', sys.argv[0], '[input-file] [num_lines]'
		exit()
	input_file = sys.argv[1]
	num_lines = sys.argv[2]
	num_lines = int(num_lines)
	
	read_corpus(input_file,num_lines)

if __name__ == "__main__":
	extract()