from typing import Type
import unittest
import math
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
        self.assertEqual(s.y,self.y)
        with self.assertRaises(TypeError):
            self.x = "2"
            s = self.create_shape()
        
        self.x=1
        with self.assertRaises(TypeError):
            self.y = "4"
            s = self.create_shape()
        
        self.y=True
        with self.assertRaises(TypeError):
            s=self.create_shape()

    def test_move(self):
        s = self.create_shape()
        s.move(-1,-2)
        self.assertEqual(s.x,0)
        self.assertEqual(s.y,0)
        with self.assertRaises(TypeError):
            s= self.create_shape()
            s.move("r",0)
        with self.assertRaises(TypeError):
            s= self.create_shape()
            s.move(-1,"0")
        
        with self.assertRaises(TypeError):
            s.move(True,0)
    
    def test_move_to(self):
        s=self.create_shape()
        s.move_to(0,0)
        self.assertEqual(s.x,0)
        self.assertEqual(s.y,0)

        with self.assertRaises(TypeError):
            s.move_to("e",0)

        with self.assertRaises(TypeError):
            s.move_to(-1111111,"0")

        with self.assertRaises(TypeError):
            s.move_to(True,0)


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.radius=0,0,5

    def create_circle(self):
        return Circle(self.x,self.y,self.radius)

    def test_create_circle(self):
        c = self.create_circle()
        self.assertEqual(c.x,self.x)
        self.assertEqual(c.y,self.y)
        self.assertEqual(c.radius,self.radius)

        with self.assertRaises(TypeError):
            self.x=""
            c = self.create_circle()
        
        self.x=0
        with self.assertRaises(TypeError):
            self.y=""
            c = self.create_circle()

        self.y=0
        with self.assertRaises(TypeError):
            self.radius=""
            c = self.create_circle()

        self.radius=0
        with self.assertRaises(ValueError):
            c = self.create_circle()

        self.radius=-5
        with self.assertRaises(ValueError):
            c = self.create_circle()

        self.radius = True
        with self.assertRaises(TypeError):
            c = self.create_circle()
    
    def test_area(self):
        c = self.create_circle()
        self.assertEqual(c.area(),5*5*math.pi)

        c.radius = 10 
        self.assertEqual(c.area(),10*10*math.pi)

    def test_perimeter(self):
        c = self.create_circle()
        self.assertEqual(c.perimeter(),5*math.tau)

        c.radius=10
        self.assertEqual(c.perimeter(),10*math.tau)
    
    def test_eq(self):
        c0 =self.create_circle()
        c1 = Circle(1,3,5)
        c2 = Circle(0,0,1)
        v  = 4
         
        self.assertTrue(c0==c1)
        self.assertFalse(c0==c2)

        with self.assertRaises(TypeError):
            n = (c0 == v)

    def test_contain(self):
        c=self.create_circle()
        
        x=1
        y=1
        self.assertTrue(c.contain(x,y))

        x=6
        y=0
        self.assertFalse(c.contain(x,y))

        x=5
        self.assertTrue(c.contain(x,y))

        x=5.00001
        self.assertFalse(c.contain(x,y))

        with self.assertRaises(TypeError):
            m = (c.contain(0,True))

    def test_scale(self):
        c=self.create_circle()

        with self.assertRaises(ValueError):
            c.scale(0)
        
        with self.assertRaises(ValueError):
            c.scale(-1)

        with self.assertRaises(TypeError):
            c.scale("")

        with self.assertRaises(TypeError):
            c.scale(True)

        with self.assertRaises(TypeError):
            c.scale(False)
        
        c2 = c.scale(1)
        self.assertEqual(c.radius,c2.radius)

        c.scale(2)
        self.assertEqual(c.radius,10)

    def test_move(self):
        c = self.create_circle()

        with self.assertRaises(TypeError):
            c.move("",5)

        with self.assertRaises(TypeError):
            c.move(5,"")

        with self.assertRaises(TypeError):
            c.move(True,5)

        with self.assertRaises(TypeError):
            c.move(5,False)

        c.move(0,0)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

        c.move(5,5)
        self.assertEqual(c.x,5)
        self.assertEqual(c.y,5)

        c.move(-5,-5)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)
    
    def test_move_to(self):
        c = self.create_circle()

        with self.assertRaises(TypeError):
            c.move_to("",5)

        with self.assertRaises(TypeError):
            c.move_to(5,"")

        with self.assertRaises(TypeError):
            c.move_to(True,5)

        with self.assertRaises(TypeError):
            c.move_to(5,False)

        c.move_to(10,10)
        self.assertEqual(c.x,10)
        self.assertEqual(c.y,10)

        c.move_to(5,5)
        self.assertEqual(c.x,5)
        self.assertEqual(c.y,5)

        c.move_to(-5,-5)
        self.assertEqual(c.x,-5)
        self.assertEqual(c.y,-5)

    def test_change_radius(self):
        c=self.create_circle()

        with self.assertRaises(TypeError):
            c.change_radius("")
        
        with self.assertRaises(TypeError):
            c.change_radius(True)

        with self.assertRaises(ValueError):
            c.change_radius(0)

        with self.assertRaises(ValueError):
            c.change_radius(-1)
        
        c.change_radius(100)
        self.assertEqual(c.radius,100)

        c.change_radius(5)
        self.assertEqual(c.radius,5)

    #TODO: test plot



        






        

        








if __name__ == "__main__":
    unittest.main() # the code that is ran is unittest.main() which runs all our tests

