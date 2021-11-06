import os
import time
import random
from tqdm import tqdm
import colorama

class Benchmark:

    benchmark_results = {
        'benchmark_array': []
    }

    def __init__(self, 
                bench_strength=1,
                wait_10_sec=False) -> None:
        colorama.init()

        self.log('Please remember to close any application you may have opened in the background to guarantee the best results.', 'WARNING')

        if wait_10_sec:
            self.log('Benchmark will start in 10 seconds.', 'INFORMATION')

            for _ in tqdm(range(10), desc='Waiting 10 seconds before startup'):
                time.sleep(1)

        self.log('Init Benchmark Object')
        self.log('bench_strength = ' + str(bench_strength), 'INFORMATION')

        if bench_strength > 5:
            self.log('Benchmark strengths over 5 can take up to half an hour or more depending on your system', 'WARNING')

        self.bench_settings = {
            'bench_strength': int(bench_strength),
            'benchmarks': {
                'benchmark_arrays': {
                    'array_size': 5000 * bench_strength,
                    'array_depth': 50 * bench_strength,
                    'array_min': 0,
                    'array_max': 1000 * (100 * bench_strength)
                }
            }
        }

    def log(self, 
            logtext, 
            category = '', 
            log_to_file = True,
            log_file = 'Benchmark.log',
            args = []):
        if args == []:
            if category == '':
                self.logger(
                    colorama.Fore.MAGENTA +
                    '[' + time.ctime() + '] ' +
                    colorama.Fore.CYAN +
                    logtext +
                    colorama.Style.RESET_ALL,
                    log_to_file,
                    log_file
                )
            elif category == 'WARNING':
                self.logger(
                    colorama.Fore.RED +
                    '[         WARNING        ] ' +
                    logtext +
                    colorama.Style.RESET_ALL,
                    log_to_file,
                    log_file
                )
            elif category == 'INFORMATION':
                self.logger(
                    colorama.Fore.YELLOW +
                    '[       INFORMATION      ] ' +
                    logtext +
                    colorama.Style.RESET_ALL,
                    log_to_file,
                    log_file
                )
            elif category == 'RESULT':
                self.logger(
                    colorama.Fore.CYAN +
                    '[         RESULT         ] ' +
                    logtext +
                    colorama.Style.RESET_ALL,
                    log_to_file,
                    log_file
                )
            else:
                pass
        else:
            # Handle special commands like getting the ram address for an object
            pass
    
    def logger(self, logtext, log_to_file, log_file):
        print(logtext)

        if log_to_file and log_file != None:
            if os.path.exists(log_file):
                open(log_file, 'a').write(logtext + '\n')
            else:
                open(log_file, 'w').write(logtext + '\n')

    def calculate_results(self):
        self.benchmark_results['benchmark_array'].append({})

        self.benchmark_results['benchmark_array'][-1]['time_total'] = 0
        self.benchmark_results['benchmark_array'][-1]['points'] = 0

        for bench in range(len(self.benchmark_results['benchmark_array']) - 1):
            cache_time_total = round(self.benchmark_results['benchmark_array'][bench]['time_end'] - self.benchmark_results['benchmark_array'][bench]['time_start'], 2)
            self.benchmark_results['benchmark_array'][-1]['time_total'] += cache_time_total
            cache_points = round(self.bench_settings['bench_strength'] / cache_time_total, 2)
            self.benchmark_results['benchmark_array'][-1]['points'] += cache_points

            self.benchmark_results['benchmark_array'][bench]['time_total'] = cache_time_total
            self.benchmark_results['benchmark_array'][bench]['points'] = cache_points

            self.log('Benchmark [ARRAY] run [' + str(bench) + '] got: ' + str(self.benchmark_results['benchmark_array'][bench]['points']) + ' x-points')

        self.benchmark_results['benchmark_array'][-1]['time_total'] = round(self.benchmark_results['benchmark_array'][-1]['time_total'] / (len(self.benchmark_results['benchmark_array']) - 1), 3)
        self.benchmark_results['benchmark_array'][-1]['points'] = round(self.benchmark_results['benchmark_array'][-1]['points'] / (len(self.benchmark_results['benchmark_array']) - 1), 3)

        self.log('Benchmark [ARRAY] took: ' + str(self.benchmark_results['benchmark_array'][-1]['time_total']) + 's on average', 'RESULT')
        self.log('Benchmark [ARRAY] got:  ' + str(self.benchmark_results['benchmark_array'][-1]['points']) + ' x-points', 'RESULT')

    def benchmark_arrays(self):
        self.benchmark_results['benchmark_array'].append({})
        self.benchmark_results['benchmark_array'][-1]['time_start'] = time.time()
        self.benchmark_results['benchmark_array'][-1]['array'] = []
        benchmark_tqdm = tqdm(
            desc='Benchmarking Arrays',
            total=self.bench_settings['benchmarks']['benchmark_arrays']['array_depth'] * self.bench_settings['benchmarks']['benchmark_arrays']['array_size']
        )

        for depth in range(self.bench_settings['benchmarks']['benchmark_arrays']['array_depth']):

            self.benchmark_results['benchmark_array'][-1]['array'].append([])

            for size in range(self.bench_settings['benchmarks']['benchmark_arrays']['array_size']):
                
                self.benchmark_results['benchmark_array'][-1]['array'][-1].append(random.randint(
                    self.bench_settings['benchmarks']['benchmark_arrays']['array_min'],
                    self.bench_settings['benchmarks']['benchmark_arrays']['array_max'],
                ))

                benchmark_tqdm.update(1)
        
        benchmark_tqdm.close()

        self.benchmark_results['benchmark_array'][-1]['time_end'] = time.time()
