import sys

Input_Pattern = sys.argv[1]
Output_Pattern = sys.argv[2]
Output_File = sys.argv[3]

try:
	fpin_open = open(Input_Pattern)
	fpout_open = open(Output_Pattern)
	fout_open = open(Output_File, 'w')
	print('File Opened.')
except:
	print('Error! File not exist.')
	exit()
#
Output_Data = ''
for line in fpin_open:
	print('input: ' + line.rstrip());
	Output_Line = ''
	degree = 8
	empty = 1
	for coef in line.split():
		#first element
		if int(coef) == 1 and empty == 1:
			if degree == 1:
				Output_Line = 'x'
			elif degree == 0:
				Output_Line = '1'
			else:
				Output_Line = 'x^' + str(degree)
		elif int(coef) == -1 and empty == 1:
			if degree == 1:
				Output_Line = '-x'
			elif degree == 0:
				Output_Line = '-1'
			else:
				Output_Line = '-x^' + str(degree)
		elif int(coef) != 0 and empty == 1:
			if degree == 1:
				Output_Line = coef + 'x'
			elif degree == 0:
				Output_Line = coef
			else:
				Output_Line = coef + 'x^' + str(degree)
		#other
		if empty == 0:
			if int(coef) == 1:
				if degree == 1:
					Output_Line = Output_Line + ' + x'
				elif degree == 0:
					Output_Line = Output_Line + ' + 1'
				else:
					Output_Line = Output_Line + ' + x^' + str(degree)
			elif int(coef) == -1:
				if degree == 1:
					Output_Line = Output_Line + ' - ' + 'x'
				elif degree == 0:
					Output_Line = Output_Line + ' - ' + str(abs(int(coef)))
				else:
					Output_Line = Output_Line + ' - ' + 'x^' + str(degree)
			elif int(coef) > 0:
				if degree == 1:
					Output_Line = Output_Line + ' + ' + coef + 'x'
				elif degree == 0:
					Output_Line = Output_Line + ' + ' + coef
				else:
					Output_Line = Output_Line + ' + ' + coef + 'x^' + str(degree)
			elif int(coef) < 0:
				if degree == 1:
					Output_Line = Output_Line + ' - ' + str(abs(int(coef))) + 'x'
				elif degree == 0:
					Output_Line = Output_Line + ' - ' + str(abs(int(coef)))
				else:
					Output_Line = Output_Line + ' - ' + str(abs(int(coef))) + 'x^' + str(degree)
		#
		if int(coef) != 0:
			empty = 0
		#
		degree -= 1
	if Output_Line == '':
		Output_Line = '0'
	answer = fpout_open.readline()
	print('Your Result: ' + Output_Line)
	print('Answer: ' + answer.rstrip())
	if answer.rstrip() != Output_Line:
		print('Error!')
	else:
		print('Correct!\n')

	Output_Data = Output_Data + Output_Line + '\n'
fout_open.write(Output_Data.rstrip())