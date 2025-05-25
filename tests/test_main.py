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

@pytest.fixture
def duplicate_keys_array():
    return [
        (2, 'first'),
        (2, 'second'),
        (1, 'third'),
        (3, 'fourth'),
        (2, 'fifth')
    ]

@pytest.fixture(params=[10, 100, 1000, 10000])
def random_sized_array(request):
    size = request.param
    return [random.randint(1, 1000) for _ in range(size)]

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

def test_stable_sort(duplicate_keys_array):
    array_to_sort = duplicate_keys_array.copy()
    insertion_sort(array_to_sort)
    assert all(array_to_sort[i][0] <= array_to_sort[i+1][0] 
              for i in range(len(array_to_sort)-1)), "Array not properly sorted"
    assert array_to_sort[0] == (1, 'third'), "Smallest key not first"
    assert array_to_sort[-1] == (3, 'fourth'), "Largest key not last"
    twos_sorted = [(i, val) for i, (key, val) in enumerate(array_to_sort) if key == 2]
    positions = [pos for pos, _ in twos_sorted]
    assert positions == list(range(min(positions), max(positions) + 1)), \
           "Elements with equal keys should be consecutive"
    
def test_random_sizes(random_sized_array, benchmark):
    """Test sorting performance on random arrays of different sizes."""
    array_to_sort = random_sized_array.copy()
    benchmark.pedantic(
        insertion_sort,
        args=(array_to_sort,),
        iterations=1,
        rounds=1
    )
    assert array_to_sort == sorted(random_sized_array)