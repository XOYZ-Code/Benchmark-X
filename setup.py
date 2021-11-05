from hashlib import new
from modules.Benchmark import Benchmark
import os
import sys

os.system('cls')

bench_strength = 5

for i in range(len(sys.argv)):
    if sys.argv[i] == '-strength':
        bench_strength = int(sys.argv[i + 1])

newBench = Benchmark(bench_strength=bench_strength)

for i in range(5):
    newBench.benchmark_arrays()
newBench.calculate_results()
