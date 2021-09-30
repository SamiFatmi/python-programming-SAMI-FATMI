import math
import matplotlib.pyplot as plt


class Shape:
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
        if not isinstance(value,(int,float)):
            raise TypeError("x coordinate must be an int or a float")
        self._x = value 

    @y.setter
    def y(self,value)->None:
        if not isinstance(value,(int,float)):
            raise TypeError("y coordinate must be an int or a float")
        self._y = value 

    
    def __repr__ (self)->str:
        return f"This is a shape with center coordinates ({self._x} , {self._y})"


    def move(self,xdistance,ydistance):
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance

    def move_to(self,x,y):
        if not all([isinstance(i,(int,float)) for i in [x,y]]) :
            raise TypeError("X and Y distances should be a number")
        self._x=x
        self._y=y
        


class Circle(Shape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y)
        self.radius=radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Radius must be an int or a float")

        if value==0:
            raise ValueError("Radius can't be 0 ")

        if value<0:
            raise ValueError("Radius can't be negative ")
            
        self._radius = value 

    
    def __repr__(self):
        return f"This is a circle with center coordinates ({self.x} , {self.y}) and radius {self.radius}"

    def area(self):
        return math.pi*(self._radius**2)

    def perimeter(self):
        return 2*math.pi*self._radius

    def __eq__(self,other):
        return True if self._radius == other._radius else False

    def contain(self,x,y):
        if not all([isinstance(i,(int,float)) for i in [x,y]]):
            raise TypeError("Point coordinates should be numbers")
        if pow(pow(x-self._x,2)+pow(y-self._y,2),0.5)<=self._radius :
            return True 
        else :
            return False
    
    def scale(self,value):
        if not isinstance(value,(int,float)) :
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
 
        self._radius *= value 

    def change_radius(self,value):
        if not isinstance(value,(int,float)) :
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
 
        self._radius = value

    def plot(self):
        X = [ self._x+ self._radius*math.cos(math.radians(i)) for i in range(1,361)]
        Y = [ self._y+ self._radius*math.sin(math.radians(i)) for i in range(1,361)]
        plt.plot(X,Y)

    




class Rectangle(Shape):
    def __init__(self,x:float,y:float,side1:float,side2:float,angle:float=0)->None:
        super().__init__(x,y)
        self.side1=side1
        self.side2=side2
        self.angle=math.radians(angle) 
    
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
    def side1(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Height must be an int or a")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self._side1 = value 

    @side2.setter
    def side2(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Height must be an int or a float")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self._side2 = value 

    @angle.setter
    def angle(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Angle must be an int or a float ")
        self._angle = value 

    def __repr__(self):
        if self._side1!=self._side2:
            return f"This is a rectangle with center coordinates ({self._x} , {self._y}), height {self._side1}, width {self._side2} and tilted with an angle of {self._angle}"
        else:
            return f"This is a square with center coordinates ({self._x} , {self._y}), height and width {self._side2} and tilted with an angle of {self._angle}"
    
    @staticmethod
    def corners (self):
        distance = pow(pow(self._side1/2,2)+pow(self._side2/2,2),0.5)
        inner_angle=math.acos(self._side1/(2*distance))

        c1=[self._x + math.cos(inner_angle+self._angle)*distance, self._y +math.sin(inner_angle+self._angle)*distance]
        c2=[self._x + math.cos(math.pi - inner_angle +self._angle)*distance,self._y + math.sin(math.pi - inner_angle +self._angle)*distance]
        c3=[self._x + math.cos(math.pi + inner_angle+self._angle)*distance,self._y + math.sin(math.pi + inner_angle+self._angle)*distance]
        c4=[self._x + math.cos(math.tau - inner_angle+self._angle)*distance,self._y +math.sin(math.tau - inner_angle+self._angle)*distance]

        return [c1,c2,c3,c4,c1]

    @staticmethod
    def euc_distance(point1,point2):
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

    def area(self):
        return self._side1*self._side2

    def perimeter(self):
        return 2*self._side1 + 2*self._side2

    def __eq__(self,other):
        if (self._side1 == other._side1 and self._side2 == other._side2 ) or (self._side2 == other._side1 and self._side1 == other._side2 ) :
            return True 
        else :
            return False

    def contains(self,x,y):
        if not all([isinstance(i,(int,float)) for i in [x,y]]):
            raise TypeError("Point coordinates must be numbers")

        if self._angle == 0 :
            if self._x-self._side1/2 <= x <= self._x+self._side1/2 and self._y-self._side2/2 <= y <= self._y+self._side2/2:
                return True
            else:
                return False 
        else : 
            for point in self.corners():
                if euc_distance(point,[x,y]) > euc_distance((self.corners())[0],(self.corners())[2]):
                    return False
            return True 
    
    def plot(self):
        X_coordinates = [(self.corners())[i][0] for i in range(5)]
        Y_coordinates = [(self.corners())[i][1] for i in range(5)]
        plt.plot(X_coordinates,Y_coordinates)

    def rotate(self,rotation_angle):
        if not isinstance(rotation_angle,(int,float)):
            raise TypeError("Rotation angle should be an int or a float")

        self._angle += math.radians(rotation_angle)

    def make_horizontal(self):
        if self._side1>=self._side2:
            self._angle = 0
        else:
            self._angle = math.pi/2
    
    def make_vertical(self):
        if self._side1>=self._side2:
            self._angle = math.pi/2
        else:
            self._angle = 0

    def scale(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Scaling Value should be a number")
        
        self._side1*=value
        self._side2*=value

    def change_size(self,new_side1,new_side2):
        if not all([isinstance(i,(int,float)) for i in [new_side1,new_side2]]):
            raise TypeError("The new length and width must be numbers")

        if new_side1==0 or new_side2==0:
            raise ValueError("Length and width can't be 0")

        if new_side1<0 or new_side2<0:
            raise ValueError("Length and width can't be negative")

        self._side1=new_side1
        self._side2=new_side2


# 3D shapes
class Shape_3D: 
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z

    @x.setter
    def x(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Value should be a number")
        
        self._x = value

    @y.setter
    def y(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Value should be a number")
        
        self._y = value

    @z.setter
    def z(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Value should be a number")
        
        self._z = value

    def move(self,x,y,z):
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x+=x
        self._y+=y
        self._z+=z

    def move_to(self,x,y,z):
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x=x
        self._y=y
        self._z=z



class Cube(Shape_3D):
    def __init__(self,x,y,z,side1,angle1=0,angle2=0,angle3=0):
        super().__init__(x,y,z)
        self.side1=side1
        self.angle1=math.radians(angle1)
        self.angle2=math.radians(angle2)
        self.angle3=math.radians(angle3)

    @property
    def side1(self):
        return self._side1 

    @property
    def angle1(self):
        return self._angle1 
    
    @property
    def angle2(self):
        return self._angle2 

    @property
    def angle3(self):
        return self._angle3

    @side1.setter
    def side1(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Dimension of side 1 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 1 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 1 can't be negative")

        self._side1=value



    @angle1.setter
    def angle1(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle1=math.radians(value)
    
    @angle2.setter
    def angle2(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle2=math.radians(value)
    
    @angle3.setter
    def angle3(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle3=math.radians(value)

        #TODO:implement AREA 
        #TODO:implement circumference surface
        #TODO:implement contains 
        #TODO:implement Rotate



class Rec_Cuboid(Cube):
    def __init__(self,x,y,z,side1,side2,side3,angle1=0,angle2=0,angle3=0):
        super().__init__(x,y,z,side1,angle1,angle2,angle3)
        self.side2=side2
        self.side3=side3

    @property
    def side2(self):
        return self._side2 

    @property
    def side3(self):
        return self._side3 

    @side2.setter
    def side2(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Dimension of side 2 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 2 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 2 can't be negative")

        self._side2=value

    @side3.setter
    def side3(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Dimension of side 3 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 3 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 3 can't be negative")

        self._side3=value



class Sphere(Shape_3D):
    def __init__(self,x,y,z,radius):
        super().__init__(x,y,z)
        self.radius=radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Radius value must be a valid number")
        if radius==0:
            raise ValueError("Radius can't be 0")
        if radius<0:
            raise ValueError("Radius can't be negative")
        
        self._radius=value




class Cylinder(Sphere):
    def __init__(self,x,y,z,radius,length,angle1=0,angle2=0,angle3=0):
        super().__init__(x,y,z,radius)
        self.length=length
        self.angle1=math.radians(angle1)
        self.angle2=math.radians(angle2)
        self.angle3=math.radians(angle3)

    @property
    def length(self):
        return self._length 

    @property
    def angle1(self):
        return self._angle1 
    
    @property
    def angle2(self):
        return self._angle2 

    @property
    def angle3(self):
        return self._angle3

    @length.setter
    def length(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("length should be a valid number")
        
        if value==0:
            raise ValueError("length can't be 0")
        
        if value<0:
            raise ValueError("length can't be negative")

        self._length=value

    @angle1.setter
    def angle1(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle1=math.radians(value)
    
    @angle2.setter
    def angle2(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle2=math.radians(value)
    
    @angle3.setter
    def angle3(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Angle 1 should be a valid number")

        self._angle3=math.radians(value)
    pass

