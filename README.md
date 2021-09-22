# Benchmark-X v0.0.3

Benchmark-X is a combination of different scripts to test your computer capability for programming, data analasys or anything else that comes to my mind.
While I work on this project the benchmark will get more advanced, will have different options and will work on Windows, Linux and MacOS.

## Parameters & Arguments

### bench_strength

The bench_strength parameter describes the strength of the benchmark. The value can be between 1 and 10. If the value is 0 the bench will skip every part of the benchmark and only tests for functionality. Higher bench_strength comes with different scoring systems. Each system will have its own leaderboard if you decide to either make your results public or when you compare different computers.

## Benchmarks

### Benchmark [ARRAY]

The Array Benchmark does 2 major things. First of all it creates a massive mulitdimensional array and secondly it creates a big amount of random numbers. The dimension count, the array length and the random number range scales with bench_strength.

---

## Changelog

### v0.0.3
- Added the option for multiple runs
    - The benchmarks now are able to run for n-times and calculate an average of the results.
