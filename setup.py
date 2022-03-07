from hashlib import new
from modules.Benchmark import Benchmark
import os
import time
import sys

os.system('cls')

bench_strength = 5

for i in range(len(sys.argv)):
    if sys.argv[i] == '-strength':
        bench_strength = int(sys.argv[i + 1])

newBench = Benchmark(bench_strength=bench_strength)

newBench.log('Total runs: ' + str(newBench.total_runs), 'INFORMATION')

for i in range(newBench.total_runs):
    run_id = '[' + str(i) + ']'
    newBench.benchmark_arrays(run_id)
    newBench.benchmark_fileWrite(run_id)
newBench.calculate_results()

newBench.dump_results(time.ctime().replace(':', '') + '_results.json')
