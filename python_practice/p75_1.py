from sys import argv
if len(argv) == 1:
    print("Hello, Guest")
else:
    print("Hello, {0}".format(argv[1]))