from challenges.sum_of_cubes import sum_of_cubes

def test_with_array1():
  result = sum_of_cubes([1, 5, 9])
  assert result == 855

def test_with_array2():
  result = sum_of_cubes([3, 4, 5])
  assert result == 216

def test_with_array3():
  result = sum_of_cubes([2])
  assert result == 8

def test_with_empty_array():
  result = sum_of_cubes([])
  assert result == 0