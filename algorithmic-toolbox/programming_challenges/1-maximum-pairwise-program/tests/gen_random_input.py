import random
import sys

n = int(sys.argv[1])
rand_range = int(sys.argv[2])
myseed = int(sys.argv[3])
random.seed(myseed)

print(n)
print(" ".join([str(random.randint(1, rand_range)) for _ in range(n)]))
