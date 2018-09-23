import sys

def print_result(number, length):
	while len(number) < length:
		number = [None] + number
	for digit in number:
		if digit is None:
			print(" "),
		else:
			print digit,
	print ("\n"),

if len(sys.argv) != 3:
	print("Wrong number of arguments! Usage: add_under_the_line number1 number2")
else:
	arg1 = list(sys.argv[1])
	arg2 = list(sys.argv[2])
	if len(arg1) < len(arg2):
		while len(arg1) < max([len(arg1), len(arg2)]):
			arg1 = [None] + arg1
	elif len(arg2) < len(arg1):
		while len(arg2) < max([len(arg1), len(arg2)]):
			arg2 = [None] + arg2
	result = []
	memory = [None]
	for i in range(len(arg1)):
		memory += [None]
	for i in range(len(arg1)-1, -1, -1):
		n = int(0 if arg1[i] is None else arg1[i]) + \
			int(0 if arg2[i] is None else arg2[i]) + \
			int(0 if memory[i+1] is None else memory[i+1])
		result = [n % 10] + result
		if n >= 10:
			memory[i] = n / 10
	if memory[0] is not None:
		result = [memory[0]] + result
	else:
		memory = memory[1:]
	print_result(memory, len(result)+2)
	print_result(arg1, len(result)+2)
	print "+",
	print_result(arg2, len(result)+1)
	print "_" * (len(result)*2+3)
	print_result(result, len(result)+2)