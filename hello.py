import sys

def hello():
	if sys.argv[1] == "Mars":
		hellomars()
	elif sys.argv[1] == "Jupyter":
		hellojupyter()
	else:
		helloworld()

def hellomars():
	print("Hello, Mars!")	


def hellojupyter():
	print("Hello, Jupyter!")

def helloworld():
	print("Hello, World!")


if __name__ == '__main__':
	hello()
