import unittest
from shapes import Shape
from shapes import Circle
from shapes import Rectangle
from shapes import Shape_3D
from shapes import Rec_Cuboid
from shapes import Sphere


class TestShape(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2 

    def create_shape(self):
        return Shape(self.x, self.y)
    
    def test_create_shape(self) -> None:
        s = self.create_shape()
        self.assertEqual(s.x, self.x)



if __name__ == "__main__":
    unittest.main() # the code that is ran is unittest.main() which runs all our tests

