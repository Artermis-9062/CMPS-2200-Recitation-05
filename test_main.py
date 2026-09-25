from main import *

# 2 pts
def test_count_values():
    assert count_values([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]
    assert count_values([2, 2, 1, 1, 1, 0], 2) == [1, 3, 2]

# 1 pts
def test_count_values_hard():
    assert count_values([2,2,1,1,6,6,1,3], 6) == [0,3,2,1,0,0,2] 

# 1 pts
def test_get_positions():
    assert get_positions([2, 3, 2, 1]) == [0, 2, 5, 7]

# 2 pts
def test_construct_output():
    assert construct_output([2,2,1,0,1,0,1,3], [0, 2, 5, 7]) == [0,0,1,1,1,2,2,3]
    assert construct_output([2,2,1,0,1,0,1,3,3], [0, 2, 5, 7]) == [0,0,1,1,1,2,2,3,3]

# 1 pts
def test_count_values_mr():
    assert count_values_mr([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]

