import math
import sys

Input_Pattern = sys.argv[1]
Output_Pattern = sys.argv[2]
Output_File = sys.argv[3]

#Input_Pattern = 'Input-Sample'
#Output_Pattern = 'Output-Sample'
#Output_File = 'Output-File'

try:
	fpin_open = open(Input_Pattern)
	fpout_open = open(Output_Pattern)
	fout_open = open(Output_File, 'w')
	print('File Opened.')
except:
	print('Error! File not exist.')
	exit()

for line in fpin_open:
	print('input: ' + line.rstrip());
	nm = line.split()
	n = int(nm[0])
	m= int(nm[1])
	print('n = ' + str(n))
	print('m = ' + str(m))
	pi = 3*math.pow(2, m)/2
	n_f = int(n % pi)
	#
	Fnm2 = [0]
	Fnm1 = [1]
	cin = 0
	#from F2
	Fn = [0]
	for i in range(n_f-1):
		#print('i:' + str(i), end="\r")
		Fn = []
		len_Fnm2 = len(Fnm2)
		len_Fnm1 = len(Fnm1)
		for j in range(len_Fnm1+1):
			Fnm2_element = 0
			Fnm1_element = 0
			if j < len_Fnm2:
				Fnm2_element = Fnm2[j]
			if j < len_Fnm1:
				Fnm1_element = Fnm1[j]
			if len(Fn) <= 20:
				Fn.append((Fnm2_element + Fnm1_element + cin)%2)
			cin = (Fnm2_element + Fnm1_element + cin)//2
		Fnm2 = Fnm1[:]
		Fnm1 = Fn[:]
	#
	#m = 0 Mn = 0
	if m == 0:
		Mn = 0
	else:
		Mn = 0
		pow = 1
		for i in range(m):
			if i >= m:
				break
			if i >= len(Fn):
				break
			Mn = Mn + pow*Fn[i]
			pow = pow * 2

	answer = fpout_open.readline()
	print('Your Result: ' + str(Mn))
	print('Answer: ' + answer.rstrip())
	if Mn != int(answer):
		print('Error!\n')
	else:
		print('Correct!\n')
	fout_open.write(str(Mn) + '\n')

exit()