## Installation
A virtual environment is recommended
```bash 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing
Pytest is used for the testing framework.

Run the tests with:
`python -m pytest tests/test_main.py`

## Benchmarking
Performance benchmarking is included using pytest-benchmark. To reproduce the benchmark tests on another machine run:

```bash
cd results
pytest --benchmark-only \
      --benchmark-histogram \
      --benchmark-json=./insertion_sort_benchmarks.json \
      ../tests/test_main.py
```
Results are stored in `results/insertion_sort_benchmarks.json`