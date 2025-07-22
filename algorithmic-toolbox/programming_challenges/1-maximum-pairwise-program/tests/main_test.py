import sys
import os
import random

tests = int(sys.argv[1])
n = int(sys.argv[2])
input_length = int(sys.argv[3])

for i in range(tests):
    print("Test #" + str(i))
    os.system(
        "python3 gen_random_input.py "
        + str(n)
        + " "
        + str(input_length)
        + " "
        + str(i)
        + " "
        + " > input.txt"
    )
    os.system("python3 model.py < input.txt > model.txt")
    os.system("python3 main.py < input.txt > main.txt")

    with open("model.txt") as f:
        model = f.read()
        print("Model: ", model)
    with open("main.txt") as f:
        main = f.read()
        print("Main: ", main)
    if model != main:
        break
