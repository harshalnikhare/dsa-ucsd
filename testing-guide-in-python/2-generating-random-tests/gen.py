# gen.py
import random
import sys

n = int(sys.argv[1])
myseed = int(sys.argv[2])
random.seed(myseed)
print(n)
# 1000 could also be moved to parameters instead of making it
# a hard constant in the code
print("_".join([str(random.randint(1, 1000)) for i in range(n)]))
