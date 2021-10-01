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


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.side1,self.side2 = 5,5,4,2

    def create_rectangle(self):
        return Rectangle(self.x,self.y,self.side1,self.side2)

    def test_create_rectangle(self):
        r = self.create_rectangle()

        self.side1=""
        with self.assertRaises(TypeError):
            r = self.create_rectangle()
        
        
        self.side1 = True
        with self.assertRaises(TypeError):
            r = self.create_rectangle()
        
        self.side1 = False
        with self.assertRaises(TypeError):
            r = self.create_rectangle()
            
        self.side1 = 4

        self.side2=""
        with self.assertRaises(TypeError):
            r = self.create_rectangle()
        
        
        self.side2 = True
        with self.assertRaises(TypeError):
            r = self.create_rectangle()
        
        self.side2 = False
        with self.assertRaises(TypeError):
            r = self.create_rectangle()

        self.side2=2
        r = self.create_rectangle()

        self.assertEqual(r.x,5)
        self.assertEqual(r.y,5)
        self.assertEqual(r.side1,4)
        self.assertEqual(r.side2,2)
        self.assertEqual(r.angle,0)
    
    def test_corners(self):
        self.x,self.y,self.side1,self.side2= 0,0,2,2
        r = self.create_rectangle()

        testcorners=[[1,1],[-1,1],[-1,-1],[1,-1],[1,1]]
        corners = r.corners()
        for i,j in zip(corners,testcorners):
            for x,y in zip(i,j):
                self.assertAlmostEqual(x,y)

        r = Rectangle(0,0,2,2,90)
        
        testcorners=[[-1,1],[-1,-1],[1,-1],[1,1],[-1,1]]
        corners = r.corners()
        for i,j in zip(corners,testcorners):
            for x,y in zip(i,j):
                self.assertAlmostEqual(x,y)

    def test_move(self):
        r = self.create_rectangle()

        with self.assertRaises(TypeError):
            r.move("",1)

        with self.assertRaises(TypeError):
            r.move(1,"")

        with self.assertRaises(TypeError):
            r.move(True,1)

        with self.assertRaises(TypeError):
            r.move(1,False)

        r.move(5,5)
        self.assertEqual(r.x,10)
        self.assertEqual(r.y,10)

        r.move(0,0)
        self.assertEqual(r.x,10)
        self.assertEqual(r.y,10)

        r.move(-10,5)
        self.assertEqual(r.x,0)
        self.assertEqual(r.y,15)





    def test_move_to(self):
        r = self.create_rectangle()

        with self.assertRaises(TypeError):
            r.move_to("",1)

        with self.assertRaises(TypeError):
            r.move_to(1,"")

        with self.assertRaises(TypeError):
            r.move_to(True,1)

        with self.assertRaises(TypeError):
            r.move_to(1,False)

        r.move_to(5,5)
        self.assertEqual(r.x,5)
        self.assertEqual(r.y,5)

        r.move_to(0,0)
        self.assertEqual(r.x,0)
        self.assertEqual(r.y,0)

        r.move_to(-10,5)
        self.assertEqual(r.x,-10)
        self.assertEqual(r.y,5)

    def test_area(self):
        r = self.create_rectangle()

        self.assertEqual(r.area(),8)

        r.side1 = 5
        r.side2 = 10
        self.assertEqual(r.area(),50)

    def test_perimeter(self):
        r = self.create_rectangle()

        self.assertEqual(r.perimeter(),12)

        r.side1 = 5
        r.side2 = 10
        self.assertEqual(r.perimeter(),30)

    def test_eq(self):
        r1 = self.create_rectangle()

        with self.assertRaises(TypeError):
            x = (r1==5)
        
        r2 = Rectangle(3,0,4,2)
        r3 = Rectangle(0,0,2,4)
        r4 = Rectangle(3,10,4,4)
        self.assertTrue(r1==r2)
        self.assertTrue(r1==r3)
        self.assertFalse(r1==r4)

    def test_contains(self):
        r = self.create_rectangle()

        with self.assertRaises(TypeError):
            v = r.contains("",0)

        with self.assertRaises(TypeError):
            v = r.contains(0,"")
        
        with self.assertRaises(TypeError):
            v = r.contains(True,0)

        with self.assertRaises(TypeError):
            v = r.contains(0,True)

        self.assertTrue(r.contains(5,5))
        self.assertTrue(r.contains(5,6))
        self.assertFalse(r.contains(5,7))
        self.assertFalse(r.contains(10,10))


    def test_rotate(self):
        r = self.create_rectangle()

        with self.assertRaises(TypeError):
            r.rotate("")

        with self.assertRaises(TypeError):
            r.rotate(True)

        r.rotate(20)
        self.assertEqual(r.angle,20)

        r.rotate(20)
        self.assertEqual(r.angle,40)

        r.rotate(-40)
        self.assertEqual(r.angle,0)


    def test_make_horizontal(self):
        r = self.create_rectangle()

        r.make_horizontal()
        self.assertEqual(r.angle,0)

        r.rotate(20)
        r.make_horizontal()
        self.assertEqual(r.angle,0)

        r = Rectangle(5,5,2,20)
        r.make_horizontal()
        self.assertEqual(r.angle,90)


    def test_make_vertical(self):
        r = self.create_rectangle()

        r.make_vertical()
        self.assertEqual(r.angle,90)

        r.rotate(20)
        r.make_vertical()
        self.assertEqual(r.angle,90)

        r = Rectangle(5,5,2,20)
        r.make_vertical()
        self.assertEqual(r.angle,0)

    def test_scale(self):
        r = self.create_rectangle()
        
        with self.assertRaises(TypeError):
            r.scale("")

        with self.assertRaises(TypeError):
            r.scale(True)

        with self.assertRaises(ValueError):
            r.scale(-1)

        with self.assertRaises(ValueError):
            r.scale(0)

        r.scale(2)
        self.assertEqual(r.side1,8)
        self.assertEqual(r.side2,4)

        r.scale(1)
        self.assertEqual(r.side1,8)
        self.assertEqual(r.side2,4)

        r.scale(0.5)
        self.assertEqual(r.side1,4)
        self.assertEqual(r.side2,2)

        self.assertEqual(type(r),type(r.scale(1)))


    def test_change_size(self):
        r = self.create_rectangle()

        with self.assertRaises(TypeError):
            r.change_size("",5)

        with self.assertRaises(TypeError):
            r.change_size(5,"")

        with self.assertRaises(TypeError):
            r.change_size(True,5)

        with self.assertRaises(TypeError):
            r.change_size(5,False)

        with self.assertRaises(ValueError):
            r.change_size(0,5)

        with self.assertRaises(ValueError):
            r.change_size(5,0)

        r.change_size(10,10)
        self.assertEqual(r.side1,10)
        self.assertEqual(r.side2,10)
        self.assertEqual(r.x,5)
        self.assertEqual(r.y,5)

        r.change_size(1,500)
        self.assertEqual(r.side1,1)
        self.assertEqual(r.side2,500)
        self.assertEqual(r.x,5)
        self.assertEqual(r.y,5)









if __name__ == "__main__":
    unittest.main() # the code that is ran is unittest.main() which runs all our tests

