import os; os.system("cls")
class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                                              # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        print('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):                                          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))                                           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other                                             # rely on existing __eq__ definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'                           # adapt list representation

  def __neg__(self):
    """Return copy of vector with all coordinates negated."""
    result = Vector(len(self))                                           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __lt__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords < other._coords

  def __le__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords <= other._coords

def total(vec):
  total = 0
  for sum in vec:
    total += sum
  return total

if __name__ == '__main__':
  x = Vector(5)
  for i in range(5):
    x[i] = (i+2)*10 
  print(f"x : {x}")

  y = Vector(5)
  for i in range(5):
    y[i] = (5-i)*10 
  print(f"y : {y}")

  print(f"Total x : {total(x)}")
  print(f"Total y : {total(y)}")

  z = x
  for i in range(5):
    z[i] = z[i]*2
  print(f"z : {z}")

  print(f"Total z : {total(z)}")