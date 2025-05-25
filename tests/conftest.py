import platform


def pytest_benchmark_generate_json(config, benchmarks, include_data):
    return {
        "machine_info": {
            "algorithm": "insertion_sort",
            "python_version": platform.python_version(),
        },
        "benchmarks": [
            {
                "name": b.name,
                "stats": {
                    "min": b.stats.min,
                    "max": b.stats.max,
                    "mean": b.stats.mean,
                    "stddev": b.stats.stddev,
                    "rounds": b.stats.rounds,
                    "unit": "ns"
                }
            }
            for b in benchmarks
        ]
    }