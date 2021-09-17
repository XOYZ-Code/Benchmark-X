from hashlib import new
from modules.Benchmark import Benchmark
import os

os.system('clear')
newBench = Benchmark(5)

newBench.benchmark_arrays()
newBench.calculate_results()
