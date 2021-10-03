import unittest
import math
from shapes import Shape
from shapes import Circle
from shapes import Rectangle
from shapes import Shape_3D
from shapes import Cube
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



class TestShape_3D(unittest.TestCase):
    def setUp(self) -> None:
        self.x=0
        self.y=0
        self.z=0

    def create_shape_3D(self):
        return Shape_3D(self.x,self.y,self.z)

    def test_create_shape_3D(self):
        s = self.create_shape_3D()
        self.assertEqual(s.x,self.x)
        self.assertEqual(s.y,self.y)
        self.assertEqual(s.z,self.z)

        with self.assertRaises(TypeError):
            self.x=True 
            s = self.create_shape_3D()

        with self.assertRaises(TypeError):
            self.x="True" 
            s = self.create_shape_3D()
        
        with self.assertRaises(TypeError):
            self.x="" 
            s = self.create_shape_3D()

        self.x=0
        with self.assertRaises(TypeError):
            self.y=True 
            s = self.create_shape_3D()

        with self.assertRaises(TypeError):
            self.y="True" 
            s = self.create_shape_3D()
        
        with self.assertRaises(TypeError):
            self.y="" 
            s = self.create_shape_3D()
        
        self.y=0
        with self.assertRaises(TypeError):
            self.z=True 
            s = self.create_shape_3D()

        with self.assertRaises(TypeError):
            self.z="True" 
            s = self.create_shape_3D()
        
        with self.assertRaises(TypeError):
            self.z="" 
            s = self.create_shape_3D()

    def test_move(self):
        s = self.create_shape_3D()

        with self.assertRaises(TypeError):
            s.move(0,0,"")

        with self.assertRaises(TypeError):
            s.move(0,"",3)

        with self.assertRaises(TypeError):
            s.move("",0,3)

        s = self.create_shape_3D()

        s.move(1,1,1)
        self.assertEqual(s.x,1)
        self.assertEqual(s.y,1)
        self.assertEqual(s.z,1)

        s.move(0,1,0)
        self.assertEqual(s.x,1)
        self.assertEqual(s.y,2)
        self.assertEqual(s.z,1)

        s.move(-5,-5,-5)
        self.assertEqual(s.x,-4)
        self.assertEqual(s.y,-3)
        self.assertEqual(s.z,-4)

    def test_move_to(self):
        s = self.create_shape_3D()

        with self.assertRaises(TypeError):
            s.move_to(0,0,"")

        with self.assertRaises(TypeError):
            s.move_to(0,"",3)

        with self.assertRaises(TypeError):
            s.move_to("",0,3)

        s = self.create_shape_3D()

        s.move_to(1,1,1)
        self.assertEqual(s.x,1)
        self.assertEqual(s.y,1)
        self.assertEqual(s.z,1)

        s.move_to(0,1,0)
        self.assertEqual(s.x,0)
        self.assertEqual(s.y,1)
        self.assertEqual(s.z,0)

        s.move_to(-5,-5,-5)
        self.assertEqual(s.x,-5)
        self.assertEqual(s.y,-5)
        self.assertEqual(s.z,-5)

class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.side1=0,0,0,4

    def create_cube(self):
        return Cube(self.x,self.y,self.z,self.side1)

    def test_create_cube(self):
        c = self.create_cube()

        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)
        self.assertEqual(c.z,0)
        self.assertEqual(c.side1,4)

        self.side1 = 0 
        with self.assertRaises(ValueError):
            c = self.create_cube()
        
        self.side1 = -1 
        with self.assertRaises(ValueError):
            c = self.create_cube()

        self.side1 = "" 
        with self.assertRaises(TypeError):
            c = self.create_cube()
        
        self.side1 = True 
        with self.assertRaises(TypeError):
            c = self.create_cube()

        self.side1 = 4 
        self.x = ""
        with self.assertRaises(TypeError):
            c = self.create_cube()

        self.x = True
        with self.assertRaises(TypeError):
            c = self.create_cube()

        self.x=0
        self.y = ""
        with self.assertRaises(TypeError):
            c = self.create_cube()

        self.y = True
        with self.assertRaises(TypeError):
            c = self.create_cube()
        
        self.y=0
        self.z = ""
        with self.assertRaises(TypeError):
            c = self.create_cube()

        self.z = True
        with self.assertRaises(TypeError):
            c = self.create_cube()

    def test_corners(self):
        c = self.create_cube()
        c1=[self.x+self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c2=[self.x+self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c3=[self.x+self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c4=[self.x+self.side1/2,self.y+self.side1/2,self.z-self.side1]
        c5=[self.x-self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c6=[self.x-self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c7=[self.x-self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c8=[self.x-self.side1/2,self.y+self.side1/2,self.z-self.side1]

        self.assertEqual(c.corners(),[c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5])

    def test_area(self):
        c = self.create_cube()

        self.assertEqual(c.volume(),self.side1**3)

        c.side1 = 3 
        self.assertEqual(c.volume(),27)

    def test_circumference_surface(self):
        c = self.create_cube()

        self.assertEqual(c.circumference_surface(),(self.side1**2)*6)

        c.side1=10

        self.assertEqual(c.circumference_surface(),600)

    def test_contains(self):
        c = self.create_cube()

        with self.assertRaises(TypeError):
            c.contains(0,0,"")

        with self.assertRaises(TypeError):
            c.contains(0,"",0)

        with self.assertRaises(TypeError):
            c.contains("",0,0)

        with self.assertRaises(TypeError):
            c.contains(0,0,False)

        with self.assertRaises(TypeError):
            c.contains(0,False,0)

        with self.assertRaises(TypeError):
            c.contains(False,0,0)

        self.assertTrue(c.contains(0,0,0))
        self.assertTrue(c.contains(0,0,2))
        self.assertTrue(c.contains(0,2,0))
        self.assertTrue(c.contains(2,0,0))
        self.assertTrue(c.contains(0,0,-2))
        self.assertTrue(c.contains(0,-2,0))
        self.assertTrue(c.contains(-2,0,0))

        self.assertFalse(c.contains(5,5,5))
        self.assertFalse(c.contains(2.01,0,0))

    def test_move(self):
        c = self.create_cube()

        with self.assertRaises(TypeError):
            c.move(0,0,"")

        with self.assertRaises(TypeError):
            c.move(0,"",0)

        with self.assertRaises(TypeError):
            c.move("",0,0)

        with self.assertRaises(TypeError):
            c.move(0,0,True)

        with self.assertRaises(TypeError):
            c.move(0,False,0)

        with self.assertRaises(TypeError):
            c.move(False,0,0)

        c.move(5,5,5)
        self.assertEqual(c.x,5)
        self.assertEqual(c.y,5)
        self.assertEqual(c.z,5)

        c.move(5,5,5)
        self.assertEqual(c.x,10)
        self.assertEqual(c.y,10)
        self.assertEqual(c.z,10)

        c.move(-20,0,100)
        self.assertEqual(c.x,-10)
        self.assertEqual(c.y,10)
        self.assertEqual(c.z,110)
    
    def test_move_to(self):
        c = self.create_cube()

        with self.assertRaises(TypeError):
            c.move_to(0,0,"")

        with self.assertRaises(TypeError):
            c.move_to(0,"",0)

        with self.assertRaises(TypeError):
            c.move_to("",0,0)

        with self.assertRaises(TypeError):
            c.move_to(0,0,True)

        with self.assertRaises(TypeError):
            c.move_to(0,False,0)

        with self.assertRaises(TypeError):
            c.move_to(False,0,0)

        c.move_to(5,5,5)
        self.assertEqual(c.x,5)
        self.assertEqual(c.y,5)
        self.assertEqual(c.z,5)

        c.move_to(15,5,55)
        self.assertEqual(c.x,15)
        self.assertEqual(c.y,5)
        self.assertEqual(c.z,55)

        c.move_to(-20,0,100)
        self.assertEqual(c.x,-20)
        self.assertEqual(c.y,0)
        self.assertEqual(c.z,100)

    def test_scale(self):
        c = self.create_cube()

        with self.assertRaises(TypeError):
            c.scale("")

        with self.assertRaises(TypeError):
            c.scale(True)

        with self.assertRaises(ValueError):
            c.scale(0)

        with self.assertRaises(ValueError):
            c.scale(-10)

        c.scale(10)
        self.assertEqual(c.side1,40)

        c.scale(0.1)
        self.assertEqual(c.side1,4)

        c.scale(25)
        self.assertEqual(c.side1,100)

    def test_change_size(self):
        c = self.create_cube()

        with self.assertRaises(TypeError):
            c.change_size("")

        with self.assertRaises(TypeError):
            c.change_size(True)

        with self.assertRaises(ValueError):
            c.change_size(0)

        with self.assertRaises(ValueError):
            c.change_size(-10)

        c.change_size(10)
        self.assertEqual(c.side1,10)

        c.change_size(0.1)
        self.assertEqual(c.side1,0.1)

        c.change_size(25)
        self.assertEqual(c.side1,25)

    def test_eq(self):
        c1 = Cube(-1,-2,-500,40)
        c2 = Cube(0,0,0,15)
        c3 = Cube(10,-9,109,40)
        s = Sphere(5,5,5,15)

        self.assertFalse(c1==c2)
        self.assertTrue(c1==c3)

        with self.assertRaises(TypeError):
            condition = c1==s
        

    
class TestRec_Cuboid(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 0
        self.y = 0
        self.z = 0
        self.side1 = 2
        self.side2 = 4
        self.side3 = 6

    def create_Rec_Cuboid(self):
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3)

    def test_create_Rec_Cuboid(self):
        r = self.create_Rec_Cuboid()

        self.assertEqual(r.side1,self.side1)
        self.assertEqual(r.side2,self.side2)
        self.assertEqual(r.side3,self.side3)


        with self.assertRaises(TypeError):
            r.side1=""
        
        with self.assertRaises(TypeError):
            r.side2=""
        
        with self.assertRaises(TypeError):
            r.side3=""
        
        with self.assertRaises(TypeError):
            r.side1=True
        
        with self.assertRaises(TypeError):
            r.side2=True
        
        with self.assertRaises(TypeError):
            r.side3=True

    
    def test_area(self):
        r = self.create_Rec_Cuboid()
        self.assertEqual(r.volume(),self.side1*self.side2*self.side3)

        r.side1=1
        r.side2=2
        r.side3=3
        self.assertEqual(r.volume(),6)

    def test_circumference_surface(self):
        r = self.create_Rec_Cuboid()
        self.assertEqual(r.circumference_surface(),self.side1*self.side2*2 + self.side1*self.side3*2 + self.side2*self.side3*2)

        r.side1=1
        r.side2=2
        r.side3=3
        self.assertEqual(r.circumference_surface(),22)

    def test_contains(self):
        r = self.create_Rec_Cuboid()

        with self.assertRaises(TypeError):
            r.contains("",9,9)

        with self.assertRaises(TypeError):
            r.contains(True,9,9)

        with self.assertRaises(TypeError):
            r.contains(9,"",9)

        with self.assertRaises(TypeError):
            r.contains(9,True,9)

        with self.assertRaises(TypeError):
            r.contains(9,9,"")

        with self.assertRaises(TypeError):
            r.contains(9,9,True)

        self.assertTrue(r.contains(0,0,0))
        self.assertTrue(r.contains(0.5,1,1.5))
        self.assertTrue(r.contains(-0.5,-1,-1.5))

        self.assertFalse(r.contains(0,0,-10))
        self.assertFalse(r.contains(0.5,1,-11.5))
        self.assertFalse(r.contains(-0.5,11,-1.5))

    def test_scale(self):
        r = self.create_Rec_Cuboid()

        with self.assertRaises(TypeError):
            r.scale("")

        with self.assertRaises(TypeError):
            r.scale(False)

        with self.assertRaises(ValueError):
            r.scale(0)

        with self.assertRaises(ValueError):
            r.scale(-9)

        r.scale(1)
        self.assertEqual(r.side1,self.side1)
        self.assertEqual(r.side2,self.side2)
        self.assertEqual(r.side3,self.side3)

        r.scale(10)
        self.assertEqual(r.side1,20)
        self.assertEqual(r.side2,40)
        self.assertEqual(r.side3,60)

        r.scale(10)
        self.assertEqual(r.side1,200)
        self.assertEqual(r.side2,400)
        self.assertEqual(r.side3,600)

        r.scale(1/200)
        self.assertEqual(r.side1,1)
        self.assertEqual(r.side2,2)
        self.assertEqual(r.side3,3)

    def test_change_siez(self):
        r = self.create_Rec_Cuboid()

        with self.assertRaises(TypeError):
            r.change_size("",10,10)

        with self.assertRaises(TypeError):
            r.change_size(True,10,10)

        with self.assertRaises(TypeError):
            r.change_size(10,"",10)

        with self.assertRaises(TypeError):
            r.change_size(10,True,10)

        with self.assertRaises(TypeError):
            r.change_size(10,10,"")

        with self.assertRaises(TypeError):
            r.change_size(10,10,True)


        with self.assertRaises(ValueError):
            r.change_size(0,10,10)

        with self.assertRaises(ValueError):
            r.change_size(-1,10,10)

        with self.assertRaises(ValueError):
            r.change_size(10,0,10)

        with self.assertRaises(ValueError):
            r.change_size(10,-1,10)

        with self.assertRaises(ValueError):
            r.change_size(10,10,0)

        with self.assertRaises(ValueError):
            r.change_size(10,10,-1)

        
        r.change_size(5,5,5)
        self.assertEqual(r.side1,5)
        self.assertEqual(r.side2,5)
        self.assertEqual(r.side3,5)
        
        r.change_size(1,15,50)
        self.assertEqual(r.side1,1)
        self.assertEqual(r.side2,15)
        self.assertEqual(r.side3,50)

    def test_corners(self):
        r = self.create_Rec_Cuboid()

        c1=[self.x+self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c2=[self.x+self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c3=[self.x+self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c4=[self.x+self.side1/2,self.y+self.side2/2,self.z-self.side3]
        c5=[self.x-self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c6=[self.x-self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c7=[self.x-self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c8=[self.x-self.side1/2,self.y+self.side2/2,self.z-self.side3]

        list2 = [c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5]
        list1 = r.corners()

        self.assertEqual(list1,list2)
    
    def test_eq(self):
        r1 = Rec_Cuboid(-1,-2,-500,40,50,60)
        r2 = Rec_Cuboid(0,0,0,15,9,9)
        r3 = Rec_Cuboid(10,-9,109,40,60,50)
        s = Sphere(5,5,5,15)

        self.assertFalse(r1==r2)
        self.assertTrue(r1==r3)

        with self.assertRaises(TypeError):
            condition = r1==s


class TestSphere(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.radius =  0,0,0,5

    def create_Sphere(self):
        return Sphere(self.x,self.y,self.z,self.radius)

    def test_create_Sphere(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.radius = ""

        with self.assertRaises(TypeError):
            s.radius = False

        with self.assertRaises(ValueError):
            s.radius = 0

        with self.assertRaises(ValueError):
            s.radius = -1

        self.assertEqual(s.radius,self.radius)

    def test_volume(self):
        s = self.create_Sphere()
        self.assertEqual(s.volume(),4 * math.pi*(self.radius**3)/3)
        
        s.radius = 10
        v = 4 * math.pi*1000/3
        self.assertEqual(s.volume(),v)

    def test_circrumference_surface(self):
        s = self.create_Sphere()
        self.assertEqual(s.circumference_surface(),4*math.pi*(self.radius**2))

        s.radius=10 
        self.assertEqual(s.circumference_surface(),4*math.pi*(10**2))

    def test_contains(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.contains("",0,0)

        with self.assertRaises(TypeError):
            s.contains(True,0,0)

        with self.assertRaises(TypeError):
            s.contains(0,"",0)

        with self.assertRaises(TypeError):
            s.contains(0,True,0)

        with self.assertRaises(TypeError):
            s.contains(0,0,"")

        with self.assertRaises(TypeError):
            s.contains(0,0,True)

        self.assertTrue(s.contains(0,0,0))
        self.assertTrue(s.contains(0,0,5))
        self.assertTrue(s.contains(0,5,0))
        self.assertTrue(s.contains(-5,0,0))

        self.assertFalse(s.contains(-5,10,0))
        self.assertFalse(s.contains(-5,0,15))
        self.assertFalse(s.contains(20,0,0))

    def test_move(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.move("",0,0)

        with self.assertRaises(TypeError):
            s.move(False,0,0)

        with self.assertRaises(TypeError):
            s.move(0,"",0)

        with self.assertRaises(TypeError):
            s.move(0,False,0)

        with self.assertRaises(TypeError):
            s.move(0,0,"")

        with self.assertRaises(TypeError):
            s.move(0,0,False)

        s.move(5,5,5)
        self.assertEqual(s.x,5)
        self.assertEqual(s.y,5)
        self.assertEqual(s.z,5)

        s.move(5,5,5)
        self.assertEqual(s.x,10)
        self.assertEqual(s.y,10)
        self.assertEqual(s.z,10)

        s.move(-10,-10,-10)
        self.assertEqual(s.x,0)
        self.assertEqual(s.y,0)
        self.assertEqual(s.z,0)

    def test_move_to(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.move_to("",0,0)

        with self.assertRaises(TypeError):
            s.move_to(False,0,0)

        with self.assertRaises(TypeError):
            s.move_to(0,"",0)

        with self.assertRaises(TypeError):
            s.move_to(0,False,0)

        with self.assertRaises(TypeError):
            s.move_to(0,0,"")

        with self.assertRaises(TypeError):
            s.move_to(0,0,False)

        s.move_to(5,5,5)
        self.assertEqual(s.x,5)
        self.assertEqual(s.y,5)
        self.assertEqual(s.z,5)

        s.move_to(15,5,25)
        self.assertEqual(s.x,15)
        self.assertEqual(s.y,5)
        self.assertEqual(s.z,25)

        s.move_to(-10,-150,-1)
        self.assertEqual(s.x,-10)
        self.assertEqual(s.y,-150)
        self.assertEqual(s.z,-1)

    def test_scale(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.scale("")

        with self.assertRaises(TypeError):
            s.scale(True)

        with self.assertRaises(ValueError):
            s.scale(0)

        with self.assertRaises(ValueError):
            s.scale(-1)

        s.scale(10)
        self.assertEqual(s.radius,50)

        s.scale(0.1)
        self.assertEqual(s.radius,5)

        s.scale(4)
        self.assertEqual(s.radius,20)

    def test_change_radius(self):
        s = self.create_Sphere()

        with self.assertRaises(TypeError):
            s.change_radius("")

        with self.assertRaises(TypeError):
            s.change_radius(True)

        with self.assertRaises(ValueError):
            s.change_radius(0)

        with self.assertRaises(ValueError):
            s.change_radius(-1)

        s.change_radius(10)
        self.assertEqual(s.radius,10)

        s.change_radius(0.1)
        self.assertEqual(s.radius,0.1)

        s.change_radius(4)
        self.assertEqual(s.radius,4)
    
    def test_eq(self):
        s1 = Sphere(-1,-2,-500,40)
        s2 = Sphere(0,0,0,15)
        s3 = Sphere(10,-9,109,40)
        r = Rec_Cuboid(5,5,5,15,42,24)

        self.assertFalse(s1==s2)
        self.assertTrue(s1==s3)

        with self.assertRaises(TypeError):
            print(s1==r)
        

        












        




if __name__ == "__main__":
    unittest.main() # the code that is ran is unittest.main() which runs all our tests

