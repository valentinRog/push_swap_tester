import subprocess
import os
from push_swap import Push_swap

def compile():
	if subprocess.run(["make", "fclean", "-C", ".."], capture_output=True).returncode:
		print("fclean KO")
		exit(1)

	if subprocess.run(["make", "-C", ".."], capture_output=True).returncode:
		print("compilation KO")
		exit(1)

	if not os.path.exists("../push_swap"):
		print("executable \"push_swap\" not found")
		exit(1)

def	test_error():
	path = "test_files/test_error/"
	for filename in os.listdir(path):
		file = open(path + filename, "r")
		args = file.read().split()
		out = subprocess.run([".././push_swap"] + args, capture_output=True)
		if out.stdout.decode("ascii") or out.stderr.decode("ascii") != "Error\n":
			print("KO")
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
			print("KO")
		else:
			print("OK")
		file.close()

def main():
	compile()
	test_error()
	test_identity()

if __name__ == "__main__":
	main()