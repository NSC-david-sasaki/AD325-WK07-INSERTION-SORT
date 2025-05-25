import pytest
import random
from src.main import insertion_sort

@pytest.fixture
def small_array():
    return [64, 34, 25, 12, 22, 11, 90]

@pytest.fixture
def large_array():
    arr = list(range(10000))
    random.shuffle(arr)
    return arr

@pytest.fixture
def nearly_sorted_array():
    arr = list(range(1, 1000))
    arr[3], arr[4] = arr[4], arr[3]  # Small perturbation
    return arr

@pytest.fixture
def reversed_array():
    return list(range(1000, 0, -1))

def test_small_array_sort(small_array, benchmark):
    array_to_sort = small_array.copy()
    benchmark(insertion_sort, array_to_sort)
    assert array_to_sort == sorted(small_array)

def test_large_array_sort(large_array, benchmark):
    array_to_sort = large_array.copy()
    benchmark(insertion_sort, array_to_sort)
    assert array_to_sort == sorted(large_array)

def test_nearly_sorted_array_sort(nearly_sorted_array, benchmark):
    array_to_sort = nearly_sorted_array.copy()
    benchmark(insertion_sort, array_to_sort)
    assert array_to_sort == sorted(nearly_sorted_array)

def test_reversed_array_sort(reversed_array, benchmark):
    array_to_sort = reversed_array.copy()
    benchmark(insertion_sort, array_to_sort)
    assert array_to_sort == sorted(reversed_array)