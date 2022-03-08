import subprocess
import os
import random
from push_swap import Push_swap

def compile():
	if subprocess.run(["make", "fclean", "-C", ".."], capture_output=True).returncode:
		print("KO: \"make fclean\"")
		exit(1)

	if subprocess.run(["make", "-C", ".."], capture_output=True).returncode:
		print("KO: \"make\"")
		exit(1)

	if not os.path.exists("../push_swap"):
		print("KO: \"executable \"push_swap\" not found\"")
		exit(1)
	print("OK")

def	test_error():
	path = "test_files/test_error/"
	for filename in os.listdir(path):
		file = open(path + filename, "r")
		args = file.read().split()
		out = subprocess.run([".././push_swap"] + args, capture_output=True)
		if out.stdout.decode("ascii") or out.stderr.decode("ascii") != "Error\n":
			print("KO: \"./push_swap", " ".join(args) + "\"")
		else:
			print("OK")
		file.close()

def test_identity():
	path = "test_files/test_identity/"
	for filename in os.listdir(path):
		file = open(path + filename, "r")
		args = file.read().split()
		out = subprocess.run([".././push_swap"] + args, capture_output=True)
		if out.stdout.decode("ascii") or out.stderr.decode("ascii"):
			print("KO: \"./push_swap", " ".join(args) + "\"")
		else:
			print("OK")
		file.close()

def test_sort(N, T):
	count = []
	sorting = True
	for _ in range(T):
		arr = [str(x) for x in range(N)]
		random.shuffle(arr)
		out = subprocess.run([".././push_swap"] + arr, capture_output=True)
		ops = out.stdout.decode("ascii").split("\n")
		ops.pop(-1)
		count.append(len(ops))
		ps = Push_swap([int(x) for x in arr])
		for op in ops:
			if op == "sa":
				ps.sa()
			elif op == "sb":
				ps.sb()
			elif op == "ss":
				ps.ss()
			elif op == "pa":
				ps.pa()
			elif op == "pb":
				ps.pb()
			elif op == "ra":
				ps.ra()
			elif op == "rb":
				ps.rb()
			elif op == "rr":
				ps.rr()
			elif op == "rra":
				ps.rra()
			elif op == "rrb":
				ps.rrb()
			elif op == "rrr":
				ps.rrr()
		if ps.a != sorted([int(x) for x in arr]) or len(ps.b):
			sorting = False
	if sorting:
		print("sorting OK")
		print("Test cases = ", T)
		print("Worst = ", max(count))
		print("Average = ", int(sum(count)/len(count)))
	else:
		print("sorting KO")
	

def main():
	print("\n---COMPILATION---")
	compile()
	print("\n---TEST ERROR---")
	test_error()
	print("\n---TEST IDENTITY---")
	test_identity()
	print("\n---TEST 2---")
	test_sort(2, 100)
	print("\n---TEST 3---")
	test_sort(3, 100)
	print("\n---TEST 5---")
	test_sort(5, 100)
	print("\n---TEST 100---")
	test_sort(100, 100)
	print("\n---TEST 500---")
	test_sort(500, 20)
	subprocess.run(["make", "fclean", "-C", ".."], capture_output=True)

if __name__ == "__main__":
	main()