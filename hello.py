import sys 


def hello():
	if sys.argv[1] == "Jupyter":
		hellojupyter()
	else:
		helloworld()	

def hellojupyter():
	print("Hello, Jupyter!")

def helloworld():
	print("Hello, World!")

if __name__ == '__main__':
	hello()
