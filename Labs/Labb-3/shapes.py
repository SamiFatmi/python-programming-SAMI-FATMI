import math
import matplotlib.pyplot as plt


class Shape:
    """ This class will be parent to the classes 'Rectangle' and 'Circle', it will contain the 
    coordinates of the 2D shapes
     """
    def __init__ (self,x:float,y:float)->None:
        self.x= x 
        self.y= y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self,value)->None:

        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("x coordinate must be an int or a float")
        self._x = value 

    @y.setter
    def y(self,value:float)->None:

        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("y coordinate must be an int or a float")
        self._y = value 

    def move(self,xdistance:float,ydistance:float)->None:
        """ Moving the Shape
        Input from the user : X and Y translation distances
        function will move the shape by adding the distances to the X and Y coordinates
        """

        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or not all([ not isinstance(i,bool) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance  

    def move_to(self,x:float,y:float)->None:
        """ Moving the shape to an exact point
        Input from the user :  X and Y coordinates of the point
        function will move the shape by changing the center of the shape's coordinates
        to the coordinates given by the user 
        """

        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):
            raise TypeError("X and Y coordinates should be a number")

        self._x=x
        self._y=y
        
    def __repr__ (self)->str:
        return (f"Type: 2D Shape\nCenter : ({self.x},{self.y})")
        


class Circle(Shape):
    """ This is a child class of Shape, it takes the X and Y coordinates from Shape
    This class will contain all the methods for plotting, area and circumference counting,
    moving, scaling or changing size and comparing to other circles.
    """
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y)
        self.radius=radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value:float)->None:

        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Radius must be an int or a float")

        if value==0:
            raise ValueError("Radius can't be 0 ")

        if value<0:
            raise ValueError("Radius can't be negative ")
            
        self._radius = value 

    def area(self)->float:
        """
        Calculating and returning the area of the circle
        """
        return math.pi*(self._radius**2)

    def perimeter(self)->float:
        """
        Calculating and returning the circumference of the circle
        """
        return 2*math.pi*self._radius

    def move(self,xdistance:float,ydistance:float)->'Circle':
        """ Moving the circle
        Input from the user : X and Y translation distances
        function will move the circle by adding the distances to the X and Y coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or not all([not isinstance(i,bool) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Circle(self._x,self._y,self._radius)

    def move_to(self,x:float,y:float)->'Circle':
        """ Moving the circle to an exact point
        Input from the user :  X and Y coordinates of the point
        function will move the circle by changing the center of the circle's coordinates
        to the coordinates given by the user 
        """
        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=x
        self._y=y
        return Circle(self._x,self._y,self._radius)
    
    def scale(self,value:float)->'Circle':
        """ Scaling the circle
        input from the user : scaling value
        The method scales the circle by multiplying the radius by the scaling value
        """

        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
 
        self._radius *= value 
        return Circle(self._x,self._y,self._radius)

    def change_radius(self,value:float)->'Circle':
        """ Changing the circle's radius 
        input from the user : new radius
        The method changes the circle's  radius to the new value
        """
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
        self._radius = value
        return Circle(self._x,self._y,value)

    def contain(self,x:float,y:float)->bool:
        """Check if a point is within a circle by comparing the distance from the point to the center
        of the circle and the radius 
        point coordinates should be given by the user"""

        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):
            raise TypeError("Point coordinates should be numbers")

        if pow(pow(x-self._x,2)+pow(y-self._y,2),0.5)<=self._radius :
            return True 
        else :
            return False

    def __eq__(self,other:'Circle')->bool:
        """ Compairing 2 circles and checking if their radius is the same
        if they have the same radius then they are equal"""
        if type(other) != type(self):
            raise TypeError("Can't compare a circle with a non-circle")
        return True if self._radius == other._radius else False

    def plot(self)->None:
        """ Plotting 360 degrees of a circle """
        X = [ self._x+ self._radius*math.cos(math.radians(i)) for i in range(1,361)]
        Y = [ self._y+ self._radius*math.sin(math.radians(i)) for i in range(1,361)]
        plt.plot(X,Y)

    def __repr__(self)->str:
        return (f"Type: Circle\nCenter : ({self.x},{self.y})\nRadius : {self.radius}")
    
    
    




class Rectangle(Shape):
    """ This is a child class of Shape, it takes the X and Y coordinates from Shape
    This class will contain all the methods for plotting, area and circumference counting,
    moving, scaling or changing size and comparing to other rectangles.
    """
    def __init__(self,x:float,y:float,side1:float,side2:float,angle:float=0)->None:
        super().__init__(x,y)
        self.side1=side1
        self.side2=side2
        self.angle=angle 
    
    @property
    def side1(self):
        return self._side1
    
    @property
    def side2(self):
        return self._side2
    
    @property
    def angle(self):
        return self._angle

    @side1.setter
    def side1(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Height must be an int or a")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self._side1 = value 

    @side2.setter
    def side2(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Height must be an int or a float")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self._side2 = value 

    @angle.setter
    def angle(self,value:float)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Angle must be an int or a float ")
        self._angle = value 

    def move(self,xdistance:float,ydistance:float)->'Rectangle':
        """ Moving the rectangle
        Input from the user : X and Y translation distances
        function will move the rectangle by adding the distances to the X and Y coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or not all([not isinstance(i,bool) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Rectangle(self._x,self._y,self._side1,self._side2)

    def move_to(self,new_x:float,new_y:float)->'Rectangle':
        """ Moving the rectangle to an exact point
        Input from the user :  X and Y coordinates of the point
        function will move the rectangle by changing the center of the rectangle's coordinates
        to the coordinates given by the user 
        """
        if not all([isinstance(i,(int,float)) for i in [new_x,new_y]]) or not all([not isinstance(i,bool) for i in [new_x,new_y]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=new_x
        self._y=new_y
        return Rectangle(new_x,new_y,self._side1,self._side2)


    def area(self)->float:
        """
        Calculating and returning the area of the rectangle
        """
        return self._side1*self._side2


    def perimeter(self)->float:
        """
        Calculating and returning the circumference of the rectangle
        """
        return 2*self._side1 + 2*self._side2


    def scale(self,value:float)->'Rectangle':
        """ Scaling the rectangle
        input from the user : scaling value
        The method scales the rectangle by multiplying the width and height by the scaling value
        """
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Scaling Value should be a number")
        
        if value == 0 :
            raise ValueError("Scaling value can't be 0")

        if value<0 :
            raise ValueError("Scaling Value can't be negative")
        self._side1*=value
        self._side2*=value
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def change_size(self,new_side1:float,new_side2:float)->'Rectangle':
        """ Changing the rectangle's size 
        input from the user : new radius
        The method changes the rectangle's width and height to the new values
        """
        if not all([isinstance(i,(int,float)) for i in [new_side1,new_side2]]) or not all([not isinstance(i,bool) for i in[new_side1,new_side2]]):
            raise TypeError("The new length and width must be numbers")

        if new_side1==0 or new_side2==0:
            raise ValueError("Length and width can't be 0")

        if new_side1<0 or new_side2<0:
            raise ValueError("Length and width can't be negative")

        self._side1=new_side1
        self._side2=new_side2

        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)
    
    def rotate(self,rotation_angle:float)->'Rectangle':
        """ Rotating the rectangle
        input from the user : rotation angle 
        Method rotates the rectangle by adding the rotation angle value to the actual angle value"""
        if not isinstance(rotation_angle,(int,float)) or isinstance(rotation_angle,bool):
            raise TypeError("Rotation angle should be an int or a float")
        self._angle+=rotation_angle
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def make_horizontal(self)->'Rectangle':
        """ Making the rectangle horizontal by checking which side is longer and setting the angle 
        to 0 or 90 depending on the cases"""
        if self._side1>=self._side2:
            self._angle = 0
            return Rectangle(self._x,self._y,self._side1,self._side2,0)
        else:
            self._angle = 90
            return Rectangle(self._x,self._y,self._side1,self._side2,90)
    
    def make_vertical(self)->'Rectangle':
        """ Making the rectangle vertical by checking which side is longer and setting the angle 
        to 0 or 90 depending on the cases"""
        if self._side1>=self._side2:
            self._angle = 90
            return Rectangle(self._x,self._y,self._side1,self._side2,90)
        else:
            self._angle = 0
            return Rectangle(self._x,self._y,self._side1,self._side2,0)

    def contains(self,x:float,y:float)->bool:
        """ Checking if a point is within our rectangle 
        Input by the user is the point coordinates
        since the user can rotate the rectangle we can't only check if the 
        point X coordinate is betwen center X +/- width and the same for Y 
        coordinates.

        We will check the area of all the triangles that could be made including our
        point in this way: 
        Let's say our rectangle is made of 4 points A,B,C,D
        Our point is called P 
        then for the point P to be within ABCD, all these triangles:
        PAB ,PBC, PCD and PDA should have areas that add up to the area of the rectangle,
        if the areas of those triangles' sum is bigger than the area of the rectangle 
        then our point P is outside the rectangle ABCD.
        """

        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):
            raise TypeError("Point coordinates must be numbers")

        if self._angle == 0 :
            if self._x-self._side1/2 <= x <= self._x+self._side1/2 and self._y-self._side2/2 <= y <= self._y+self._side2/2:
                return True
            else:
                return False 
        else : 
            rec_corners=self.corners()
            point1=rec_corners[0]
            point2=rec_corners[1]
            point3=rec_corners[2]
            point4=rec_corners[3]

            triangle1_area= max(abs(point1[0]-point2[0]),abs(point1[0]-x),abs(x-point2[0]))*max(abs(point1[1]-point2[1]),abs(point1[1]-y),abs(y-point2[1])) - abs((point1[0]-point2[0])*(point1[1]-point2[1]))/2 - abs((point1[0]-x)*(point1[1]-y))/2 - abs((x-point2[0])*(y-point2[1]))/2
            triangle2_area= max(abs(point3[0]-point2[0]),abs(point3[0]-x),abs(x-point2[0]))*max(abs(point3[1]-point2[1]),abs(point3[1]-y),abs(y-point2[1])) - abs((point3[0]-point2[0])*(point3[1]-point2[1]))/2 - abs((point3[0]-x)*(point3[1]-y))/2 - abs((x-point2[0])*(y-point2[1]))/2
            triangle3_area= max(abs(point3[0]-point4[0]),abs(point3[0]-x),abs(x-point4[0]))*max(abs(point3[1]-point4[1]),abs(point3[1]-y),abs(y-point4[1])) - abs((point3[0]-point4[0])*(point3[1]-point4[1]))/2 - abs((point3[0]-x)*(point3[1]-y))/2 - abs((x-point4[0])*(y-point4[1]))/2
            triangle4_area= max(abs(point1[0]-point4[0]),abs(point1[0]-x),abs(x-point4[0]))*max(abs(point1[1]-point4[1]),abs(point1[1]-y),abs(y-point4[1])) - abs((point1[0]-point4[0])*(point1[1]-point4[1]))/2 - abs((point1[0]-x)*(point1[1]-y))/2 - abs((x-point4[0])*(y-point4[1]))/2

            if (triangle1_area+triangle2_area+triangle3_area+triangle4_area) - self.area() > 0.01:
                return False
            return True 
    
    def __eq__(self,other:'Rectangle')->bool:
        """ Comparing 2 rectangles by checking if they have the same width and height
        since rectangles can be rotated, 2 rectangles having 
        """
        if type(other)!=type(self):
            raise TypeError("Can't compare a rectangle with a non rectangle")
        if (self._side1 == other._side1 and self._side2 == other._side2 ) or (self._side2 == other._side1 and self._side1 == other._side2 ) :
            return True 
        else :
            return False

    @staticmethod
    def euc_distance(point1:list,point2:list)->float:
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
    
    def corners (self)->list:
        distance = pow(pow(self._side1/2,2)+pow(self._side2/2,2),0.5)
        inner_angle=math.acos(self._side1/(2*distance))

        c1=[self._x + math.cos(inner_angle+math.radians(self.angle))*distance, self._y +math.sin(inner_angle+math.radians(self.angle))*distance]
        c2=[self._x + math.cos(math.pi - inner_angle +math.radians(self.angle))*distance,self._y + math.sin(math.pi - inner_angle +math.radians(self.angle))*distance]
        c3=[self._x + math.cos(math.pi + inner_angle+math.radians(self.angle))*distance,self._y + math.sin(math.pi + inner_angle+math.radians(self.angle))*distance]
        c4=[self._x + math.cos(math.tau - inner_angle+math.radians(self.angle))*distance,self._y +math.sin(math.tau - inner_angle+math.radians(self.angle))*distance]

        return [c1,c2,c3,c4,c1]
    
    def plot(self):
        X_coordinates = [(self.corners())[i][0] for i in range(5)]
        Y_coordinates = [(self.corners())[i][1] for i in range(5)]
        plt.plot(X_coordinates,Y_coordinates)


    def __repr__(self)->str:
        if self._side1!=self._side2:
            return (f"Type: Rectangle\nCenter : ({self.x},{self.y})\nWidth : {self.side1}\nHeight: {self.side2}")
        else:
            return (f"Type: Square\nCenter : ({self.x},{self.y})\nWidth : {self.side1}")

# 3D shapes
class Shape_3D: 
    def __init__(self,x:float,y:float,z:float)->None:
        self.x=x
        self.y=y
        self.z=z

    @property
    def x(self)->float:
        return self._x
    
    @property
    def y(self)->float:
        return self._y
    
    @property
    def z(self)->float:
        return self._z

    @x.setter
    def x(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._x = value

    @y.setter
    def y(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._y = value

    @z.setter
    def z(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._z = value

    def move(self,x:float,y:float,z:float)->None:
        """ Moving the 3D Shape
        Input from the user : X,Y and Z translation distances
        function will move the 3D shape by adding the distances to the X,Y and Z coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]) or not all([not isinstance(x,bool) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x+=x
        self._y+=y
        self._z+=z

    def move_to(self,x:float,y:float,z:float):
        """ Moving the shape to an exact point
        Input from the user :  X,Y and Z coordinates of the point
        function will move the shape by changing the center of the shape's coordinates
        to the coordinates given by the user 
        """
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]) or not all([not isinstance(x,bool) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x=x
        self._y=y
        self._z=z

    def __repr__(self)->str:
        return (f"Type: 3D Shape\nCenter : ({self.x},{self.y},{self.z})")


class Cube(Shape_3D):
    def __init__(self,x:float,y:float,z:float,side1:float)->None:
        super().__init__(x,y,z)
        self.side1=side1

    @property
    def side1(self)->float:
        return self._side1 

    @side1.setter
    def side1(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 1 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 1 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 1 can't be negative")

        self._side1=value



    def volume(self)->float:
        """ Calculating and returning the volume of the cube """
        return self.side1**3 

    def circumference_surface(self)->float:
        """ Calculating and returning the circumference surface of the cube """
        return (self.side1**2)*6


    def move(self,X:float,Y:float,Z:float)->'Cube':
        """ Moving the cube
        Input from the user :  X,Y and Z translation distances
        function will move the cube by adding the distances to the X,Y and Z coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x+=X
        self.y+=Y
        self.z+=Z
        return Cube(self.x,self.y,self.z,self.side1)
        

    def move_to(self,X:float,Y:float,Z:float)->'Cube':
        """ Moving the cube to an exact point
        Input from the user :  X,Y and Z coordinates of the point
        function will move the cube by changing the center of the cube's coordinates
        to the coordinates given by the user 
        """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x=X
        self.y=Y
        self.z=Z
        return Cube(self.x,self.y,self.z,self.side1) 

    def scale(self,scaling_value:float)->'Cube':
        """ Scaling the cube
        input from the user : scaling value
        The method scales the cube by multiplying the width,height and depth by the scaling value
        """
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.side1*=scaling_value
        return Cube(self.x,self.y,self.z,self.side1)

    def change_size(self,side_value:float)->'Cube':
        """ Changing the cube's size 
        input from the user : new width 
        The method changes the cubes's width to the new value
        """
        if not isinstance(side_value,(int,float)) or isinstance(side_value,bool):
            raise TypeError("Side dimension must be a valid number")

        if side_value == 0:
            raise ValueError("Side dimension can't be 0")

        if side_value < 0 :
            raise ValueError("Side dimension can't be negative")

        self.side1=side_value
        return Cube(self.x,self.y,self.z,self.side1)
    
    def contains(self,X:float,Y:float,Z:float)->bool:
        """ Checking if the """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if (self.x-self.side1/2<=X<=self.x+self.side1/2 and self.y-self.side1/2<=Y<=self.y+self.side1/2 and self.z-self.side1/2<=Z<=self.z+self.side1/2) else False

    def __eq__(self, o: object) -> bool:
        if type(self)!=type(o):
            raise TypeError("Can't compare a cube with a non-cube.")
        else:
            return True if (self.side1 == o.side1) else False

    @staticmethod
    def euc_distance(point1:list,point2:list)->float:
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)**0.5

    def corners(self)->list:

        c1=[self.x+self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c2=[self.x+self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c3=[self.x+self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c4=[self.x+self.side1/2,self.y+self.side1/2,self.z-self.side1]
        c5=[self.x-self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c6=[self.x-self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c7=[self.x-self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c8=[self.x-self.side1/2,self.y+self.side1/2,self.z-self.side1]

        return [c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5]
    
    def __repr__(self)->str:
        return (f"Type: Cube\nCenter : ({self.x},{self.y},{self.z})\nWidth : {self.side1}")

        
        



class Rec_Cuboid(Cube):
    def __init__(self,x:float,y:float,z:float,side1:float,side2:float,side3:float)->None:
        super().__init__(x,y,z,side1)
        self.side2=side2
        self.side3=side3

    @property
    def side2(self)->float:
        return self._side2 

    @property
    def side3(self)->float:
        return self._side3 

    @side2.setter
    def side2(self,value:float)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 2 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 2 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 2 can't be negative")

        self._side2=value

    @side3.setter
    def side3(self,value:float)->None :
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 3 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 3 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 3 can't be negative")

        self._side3=value

    def volume(self)->float:
        """
        Calculating and returning the volume of the rectangular cuboid
        """
        return self.side1*self.side2*self.side3 

    def circumference_surface(self)->float:
        """
        Calculating and returning the circumference surface of the rectangular cuboid
        """
        return self.side1*self.side2*2 + self.side1*self.side3*2 + self.side2*self.side3*2

    def move(self,X:float,Y:float,Z:float)->'Rec_Cuboid':
        """ Moving the rectangular cuboid
        Input from the user :  X,Y and Z translation distances
        function will move the rectangular cuboid by adding the distances to the  X,Y and Z coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x+=X
        self.y+=Y
        self.z+=Z
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3)
        

    def move_to(self,X:float,Y:float,Z:float)->'Rec_Cuboid':
        """ Moving the rectangular cuboid to an exact point
        Input from the user :  X,Y and Z coordinates of the point
        function will move the rectangular cuboid by changing the center of the rectangular cuboid's coordinates
        to the coordinates given by the user 
        """
        
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeEßrror ("Distances must be valid numbers")

        self.x=X
        self.y=Y
        self.z=Z
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3) 


    def scale(self,scaling_value:float)->'Rec_Cuboid':
        """ Scaling the rectangular cuboid
        input from the user : scaling value
        The method scales the rectangular cuboid by multiplying the width, height and depth by the scaling value
        """
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.side1*=scaling_value
        self.side2*=scaling_value
        self.side3*=scaling_value
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3)

    def change_size(self,new_side1:float,new_side2:float,new_side3:float)->'Rec_Cuboid':
        """ Changing the rectangular cuboid's size 
        input from the user : new width, height and depth
        The method changes the rectangular cuboid's width, height and depth to the new values
        """
        if not all([isinstance(i,(int,float)) for i in [new_side1,new_side2,new_side3]]) or not all([ not isinstance(i,bool) for i in [new_side1,new_side2,new_side3]]):
            raise TypeError("New sides values must be valid numbers")

        if new_side1== 0 or new_side2 == 0 or new_side3 == 0:
            raise ValueError("New sides values can't be 0")

        if new_side1< 0 or new_side2 < 0 or new_side3 < 0 :
            raise ValueError("New sides values can't be negative")

        self.side1=new_side1
        self.side2=new_side2
        self.side3=new_side3
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3)
    
    def contains(self,X:float,Y:float,Z:float)->bool:
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if  self.x-self.side1 <=X<= self.x+self.side1 and self.y-self.side2 <=Y<= self.y+self.side2 and self.z-self.side3 <=Z<= self.z+self.side3 else False
    
    def __eq__(self, o: object) -> bool:
        if type(self)!=type(o):
            raise TypeError("Can't compare a rectangular cuboid shape with a non-rectangular cuboid shape.")
        else:
            return True if (self.side1 == o.side1 or self.side1 == o.side2 or self.side1 == o.side3) and (self.side2 == o.side1 or self.side2 == o.side2 or self.side2 == o.side3) and (self.side3 == o.side1 or self.side3 == o.side2 or self.side3 == o.side3) else False
    
    def corners(self)->list:    
        c1=[self.x+self.side1/2,self.y+self.side2/2,self.z+self.side3/2]
        c2=[self.x+self.side1/2,self.y-self.side2/2,self.z+self.side3/2]
        c3=[self.x+self.side1/2,self.y-self.side2/2,self.z-self.side3/2]
        c4=[self.x+self.side1/2,self.y+self.side2/2,self.z-self.side3/2]
        c5=[self.x-self.side1/2,self.y+self.side2/2,self.z+self.side3/2]
        c6=[self.x-self.side1/2,self.y-self.side2/2,self.z+self.side3/2]
        c7=[self.x-self.side1/2,self.y-self.side2/2,self.z-self.side3/2]
        c8=[self.x-self.side1/2,self.y+self.side2/2,self.z-self.side3/2]

        return [c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5]
    
    def __repr__(self)->str:
        return (f"Type: Rectangular cuboid\nCenter : ({self.x},{self.y},{self.z})\nWidth : {self.side1}\nHeight : {self.side2}\nDepth : {self.side3}")


        


class Sphere(Shape_3D):
    def __init__(self,x:float,y:float,z:float,radius:float)->None:
        super().__init__(x,y,z)
        self.radius=radius

    @property
    def radius(self)->float:
        return self._radius

    @radius.setter
    def radius(self,value)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Radius value must be a valid number")
        if value==0:
            raise ValueError("Radius can't be 0")
        if value<0:
            raise ValueError("Radius can't be negative")
        
        self._radius=value

    def volume(self)->float:
        """ Calculating and returning the volume of the sphere  """
        return 4 * math.pi*(self.radius**3)/3

    def circumference_surface(self)->float:
        """ Calculating and returning the circumference surface of the sphere """
        return 4*math.pi*(self.radius**2)



    def move(self,X:float,Y:float,Z:float)->'Sphere':
        """ Moving the sphere
        Input from the user :  X,Y and Z translation distances
        function will move the sphere by adding the distances to the  X,Y and Z coordinates
        """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x +=X
        self.y +=Y
        self.z +=Z
        return Sphere(self.x,self.y,self.z,self.radius)

    def move_to(self,X:float,Y:float,Z:float)->'Sphere':
        """ Moving the sphere to an exact point
        Input from the user :  X,Y and Z coordinates of the point
        function will move the sphere by changing the center of the sphere's coordinates
        to the coordinates given by the user 
        """
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        self.x =X
        self.y =Y
        self.z =Z
        return Sphere(self.x,self.y,self.z,self.radius) 


    def scale(self,scaling_value:float)->'Sphere':
        """ Scaling the sphere
        input from the user : scaling value
        The method scales the sphere by multiplying the radius by the scaling value
        """
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.radius *= scaling_value
        return Sphere(self.x,self.y,self.z,self.radius)

    def change_radius(self,new_radius_value:float)->'Sphere':
        """ Changing the spheres's radius 
        input from the user : new radius
        The method changes the spheres's  radius to the new value
        """
        if not isinstance(new_radius_value,(int,float)) or isinstance(new_radius_value,bool):
            raise TypeError("New radius value must be a valid number")

        if new_radius_value == 0:
            raise ValueError("New radius value can't be 0")

        if new_radius_value < 0 :
            raise ValueError("New radius value can't be negative")

        self.radius = new_radius_value
        return Sphere(self.x,self.y,self.z,self.radius)

    def contains(self,X:float,Y:float,Z:float)->bool:
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if  ((self.x-X)**2 + (self.y-Y)**2 + (self.z-Z)**2)**0.5 <= self.radius else False
    
    def __eq__(self, o: object) -> bool:
        if type(self)!=type(o):
            raise TypeError("Can't compare a Sphere with a non-sphere.")
        else:
            return True if self.radius == o.radius else False

    def __repr__(self)->str:
        return (f"Type: Sphere\nCenter : ({self.x},{self.y},{self.z})\nRadius : {self.radius}")




