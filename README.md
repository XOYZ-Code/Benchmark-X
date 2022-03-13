# Benchmark-X v0.2.0-alpha

Benchmark-X is a combination of different scripts to test your computer capability for programming, data analasys or anything else that comes to my mind.
While I work on this project the benchmark will get more advanced, will have different options and will work on Windows, Linux and MacOS.

---

## Parameters & Arguments

### strength

The strength parameter describes the strength of the benchmark. The value can be any number but is 5 if nothing is given to the program. If the value is 0 the bench will skip every part of the benchmark and only tests for functionality. Higher strength comes with different scoring systems. Each system will have its own leaderboard if you decide to either make your results public or when you compare different computers.

---

## Benchmarks

### Benchmark [ARRAY]

The Array Benchmark does 2 major things. First of all it creates a massive mulitdimensional array and secondly it creates a big amount of random numbers. The dimension count, the array length and the random number range scales with strength.

### Benchmark [FILWR]

The File write Benchmark tests the system capability of writing data to the storage. [ARRAY] tries to fill up the ram as fast as possible while [FILWR] does it with the Hard Drive. This Benchmark helps to identify bad or slow Hard Drive that cannot handle much data in short time

---

## Changelog

### v0.2.0-alpha

- Added Benchmark File Write [FILWR]
- Result dumping
    - Results will now be printed to a json file in the logs/ folder
- Set the standard strength to 5 if no strength is given over the arguments for simple .exe executions.

### v0.0.3
- Added the option for multiple runs
    - The benchmarks now are able to run for n-times and calculate an average of the results.
