"""
Vector and Matrix calculator
Alexandre Cornu
Contains the classes for Vector and Matrix
History:
Nov 8, 2024: Added the __init__(), components() setter and getter, magnitude, __add__(), __sub__(), __mul__(), dot_product(), and is_same_dimension() methods
Nov 11, 2024: Added the Op() class. Removed the dot_product() method from the Vector class and added it to the Op class. Added cross_product() method to Op. Added __str__() magic method to Vector
Nov 14, 2024: Added the angle_betwen_vectors() method
Nov 15, 2024: Added the __init__() method, validate_matrix() method, multiply() method
Nov 16, 2024: Modified the __init() method to assign the Matrix class a list of Vector objects and added the from_2d_list() method. Added the __str__() magic method for Matrix class
"""
import math

class Vector():
  """
  Creates a vector object in any dimension
  Attributes:
    _components (list[float]): A list containing n amount of components of an n-dimentional vector
  """
  def __init__(self, components):
    """
    Assigns values to the vector object
    Args:
      components (list[float]): A list that contains the components of the vector
    """
    self.components = components

  @property
  def components(self):
    return self._components
  
  @components.setter
  def components(self, new_comps):
    """
    Validates the components list before it is set
    Args:
      new_comp (list): A list of variable length that contains the components of the vector
    """
    for comp in new_comps:
      if isinstance(comp, int) == False and isinstance(comp, float) == False:
        raise TypeError("Components list must contain either floats or ints")
    self._components = new_comps

  def magnitude(self):
    """
    Calculates the magnitude of the vector
    Returns:
      math.sqrt(squared_sum) (float): The magnitude of the vector
    """
    squared_sum = 0
    for comp in self.components:
      squared_sum += comp**2
    return math.sqrt(squared_sum)
  
  def __add__(self, other_vector):
    """
    Operation for vector addition
    Args:
      other_vector (Vector): The addend of the operation
    Returns:
      resultant (Vector): The resultant vector of the addition
    """
    resultant_components = []
    # Validates that other_vector is a Vector object
    if self.__class__.is_same_dimension(self, other_vector):
      for index, comp in enumerate(other_vector.components):
        resultant_components.append(self.components[index]+comp)
    else:
      raise Exception("__add__ method cannot add vectors with different dimensions")
    resultant = Vector(resultant_components)
    return resultant

  def __mul__(self, scalar):
    """
    Magic method for scalar multiplication
    Args:
      scalar (int or float): A scalar value that is multiplied with the vector
    Returns:
      resultant (Vector): The resultant vector of the multiplication
    """
    resultant_components = []
    if isinstance(scalar, int) or isinstance(scalar, float):
      for comp in self.components:
        resultant_components.append(comp*scalar)
    else:
      raise TypeError("Scalar multiplication for a Vector object only works when given an integer or float")
    resultant = Vector(resultant_components)
    return resultant

  def __sub__(self, other_vector):
    """
    Operation for vector subtraction
    Args:
      other_vector (Vector): The subtrahend of the subtraction
    Returns:
      resultant (Vector): The resultant vector of the subtraction
    """
    if self.__class__.is_same_dimension(self, other_vector):
      subtrahend = other_vector*-1
      resultant = self + subtrahend # It is doing addition because Vector - Vector is the same Vector + (-Vector))
    else:
      raise Exception("__sub__() method cannot subtract vectors with different dimensions")
    return resultant

  def __str__(self):
    return f"{self.components}"

  @staticmethod
  def is_same_dimension(v1, v2):
    """
    Checks if two vectors have the same dimension
    Also validates if the two passed values are Vector objects
    Args:
      v1 (Vector): A vector being compared
      v2 (Vector): A vector being compared
    Returns:
      same_dimension (bool): True if the length of the component lists are equivalent. False if the lengths do not match
    """
    if isinstance(v1, Vector) == False or isinstance(v2, Vector) == False:
      raise Exception("Cannot compare the dimensions of an object that is not a vector")
    else:
      same_dimension = len(v1.components) == len(v2.components)
    return same_dimension


class Matrix():
  """
  Creates a matrix of any dimension
  Example of how it looks:
  [[Vector],[Vector],[Vector]]
  Attributes:
    vector_list (list[Vector]): This 2d list contains the elements present in the matrix
    square (bool): True if the matrix has equal length for its rows and collumns
  """

  def __init__(self, vector_list):
    """
    Assigns values to the Matrix object
    Args:
      vector_list (list[Vector]): A list of vectors with equal dimensions
    """
    self.validate_matrix(vector_list)
    self.vector_list = vector_list
    # This can use the first vector of vector_list because the vectors have already been validated to be of equal dimensions
    self.square = len(vector_list) == len(vector_list[0].components)
    
  
  @staticmethod
  def validate_matrix(vector_list):
    """
    Validates the given list of elements to ensure that they are only made up of ints or floats
    Raises an error if the given 2d list is not valid
    Args:
      vector_list (list[Vector]): A list of vectors with equal dimensions
    """
    if not isinstance(vector_list, list):
      raise TypeError(f"{type(vector_list)} type argument is not valid for instantiating a Matrix object")

    for vector in vector_list:
      if not isinstance(vector, Vector):
        raise TypeError("Matrix class requires a list of Vector object to be instantiated")
    
    # Multiple for loops have to be used since this validation below requires that all of the elements in vector_list have been validated to be Vectors
    comparison_vector = vector_list[0]
    for vector in vector_list:
      if not Vector.is_same_dimension(comparison_vector,vector):
        raise Exception("All vectors in the list must have equal dimensions")
  
  @classmethod
  def from_2d_list(cls,elements):
    """
    Creates a matrix object from a list of vectors
    Args:
      elements (list[list[float]]): A 2d list containing the elements present in the matrix
    Returns:
      cls(vector_list) (Matrix): A matrix object made from a 2d list of vector components
    """

    if not isinstance(elements, list):
      raise TypeError("Matrix class requires a 2d list of ints or floats to be passed as an argument")
    
    collumn_length = len(elements[0])

    for sublist in elements:
      if len(sublist) != collumn_length: # Verifies that the matrix has consistent lengths
        raise Exception("The sublists in the provided argument must have equal lengths")
      for component in sublist:
        if not isinstance(component, int) and not isinstance(component, float):
          raise TypeError("The elements in the 2d list must be either an int or a float")
    
    vector_list = []
    for sublist in elements:
      vector_list.append(Vector(sublist))

    return cls(vector_list)


  def multiply(self, other_matrix):
    """
    This is the function for matrix-vector/matrix-matrix multiplication
    Args:
      other_matrix (Matrix or Vector): The vector/matrix who is being transformed by the calling matrix
    Returns:
      transformed_matrix (Matrix or Vector): The resulting tranformation/vector after being transformed by the calling matrix
    """
    # Add validations later
    if isinstance(other_matrix, Vector):
      other_matrix_vectors = [other_matrix] # Turns it into a 2d list due to how the algorithm works for matrix multiplication
    else:
      other_matrix_vectors = other_matrix.vector_list

    transformed_matrix_list = []

    for vector in other_matrix_vectors:
      transformed_vector = Vector([0,0]) # Creates the zero vector
      for index, comp in enumerate(vector.components):
        # (Note to self) This calculation could be a bit cleaner if you made __iadd__() for the Vector class
        transformed_vector = transformed_vector + self.vector_list[index]*comp
      transformed_matrix_list.append(transformed_vector)
    
    if len(transformed_matrix_list) == 1:
      transformed_matrix = transformed_matrix_list[0]
    else:
      transformed_matrix = Matrix(transformed_matrix_list)

    return transformed_matrix

  def __str__(self):
    """
    Returns a list of the components of the vectors in the Matrix object
    """
    printable_list = []
    for vector in self.vector_list:
      printable_list.append(vector.components)
    return str(printable_list)

class Op():
  """
  This class will be used to perform more complex operations on vectors and matrices
  """

  @classmethod
  def dot_product(cls, v1, v2):
    """
    Operation for the dot product of two vectors
    Args:
      v1 (Vector): An operand in the dot product
      v2 (Vector): The other operand in the dot product
    Returns:
      scalar (int or float): The scalar that is outputed from the dot product
    """
    if Vector.is_same_dimension(v1, v2):
      scalar = 0
      # The arrangement of v1 and v2 in this calculation does not matter because dot product is commutative
      for index, comp in enumerate(v2.components):
        scalar += v1.components[index]*comp
    else:
      raise Exception("Cannot evaluate the dot product of two vectors with different dimesions")
    return scalar

  @classmethod
  def cross_product(cls, v1, v2):
    """
    Operation for the cross product of two vectors
    Args:
      v1 (Vector): The first operand in the cross product
      v2 (Vector): The second operand in the dot product
    Returns:
      v3 (Vector): The cross product of v1 & v2 (a Vector orthogonal to v1 & v2 whose magnitude is equal to the magnitude of v1 & v2's determinant)
    """
    # Note, even though the method is validating that the two vectors are exclusively in 3d, it is possible to have a cross product in 7d if you treat the vectors like octonions (but I have yet to learn enough about this subject to give compute a 7d cross product)

    if len(v1.components) == 3 and len(v2.components) == 3:
      x_comp = (v1.components[1]*v2.components[2]) - (v1.components[2]*v2.components[1])
      y_comp = (v1.components[2]*v2.components[0]) - (v1.components[0]*v2.components[2])
      z_comp = (v1.components[0]*v2.components[1]) - (v1.components[1]*v2.components[0])
      v3 = Vector([x_comp,y_comp,z_comp])
    else:
      raise Exception("Cross product can only be used for vectors exclusively in 3d")

    return v3
  
  @classmethod
  def angle_between_vectors(cls, v1, v2):
    """
    Finds the angle between to given vecters using the dot product
    Args:
      v1 (Vector): The first vector
      v2 (Vector): The second vector
    Returns:
      angle (float): The angle between the two vectors (in degrees)
    """
    if Vector.is_same_dimension(v1, v2):
      if v1.magnitude() == 0 or v2.magnitude() == 0:
        raise ValueError("Cannot find the angle between two vectors if one of them is the zero vector")
      numerator = cls.dot_product(v1,v2)
      denominator = v1.magnitude()*v2.magnitude()
      
      angle = math.acos(numerator/denominator)
      # converts to degrees
      angle = round(angle*(360/math.tau), 2)
    else:
      raise Exception("Cannot evaluate the angle between two vectors with different dimesions")
    return angle
# ---------------------------
# Below is the main.py code
# ---------------------------

v1 = Vector([0,1])

v2 = Vector([-1,0])

M1 = Matrix([v1,v2])

v3 = Vector([4,5])
v4 = Vector([2,3])

M2 = Matrix([v3,v4])

#r = Op.angle_between_vectors(v1,v2)

print(M1.multiply(M2))
