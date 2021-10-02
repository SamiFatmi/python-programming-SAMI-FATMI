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
        if str(value)=='True' or str(value)=='False' :
            raise TypeError("x coordinate can't be a boolean")

        if not isinstance(value,(int,float)):
            raise TypeError("x coordinate must be an int or a float")
        self._x = value 

    @y.setter
    def y(self,value)->None:
        if str(value)=='True' or str(value)=='False' :
            raise TypeError("y coordinate can't be a boolean")


        if not isinstance(value,(int,float)):
            raise TypeError("y coordinate must be an int or a float")
        self._y = value 

    
    def __repr__ (self)->str:
        return f"This is a shape with center coordinates ({self._x} , {self._y})"


    def move(self,xdistance,ydistance):
        if str(xdistance) in['True','False'] or str(ydistance) in['True','False']:
            raise TypeError("X and Y distances can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        

    def move_to(self,x,y):
        if str(x) in['True','False'] or str(y) in ['True','False']:
            raise TypeError("X and Y coordinates can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [x,y]]) :
            raise TypeError("X and Y coordinates should be a number")

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
        if str(value) in ['True','False']:
            raise TypeError("Radius can't be a boolean")

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
        if type(other) != type(self):
            raise TypeError("Can't compare a circle with a non-circle")
        return True if self._radius == other._radius else False

    def contain(self,x,y):
        if str(x) in ['True','False'] or str(y) in ['True','False']:
            raise TypeError("X and Y can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [x,y]]):
            raise TypeError("Point coordinates should be numbers")

        if pow(pow(x-self._x,2)+pow(y-self._y,2),0.5)<=self._radius :
            return True 
        else :
            return False
    
    def scale(self,value):
        if str(value) in ['True','False']:
            raise TypeError("Scaling value can't be a boolean")

        if not isinstance(value,(int,float)):
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
 
        self._radius *= value 
        return Circle(self._x,self._y,self._radius)

    def move(self,xdistance,ydistance):
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or str(xdistance) in ['True','False'] or str(ydistance) in ['True','False']:                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Circle(self._x,self._y,self._radius)

    def move_to(self,x,y):
        if not all([isinstance(i,(int,float)) for i in [x,y]]) or str(x) in ['True','False'] or str(y) in ['True','False']:                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=x
        self._y=y
        return Circle(self._x,self._y,self._radius)

    def change_radius(self,value):
        if not isinstance(value,(int,float)) or str(value) in ['True','False']:
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
        self._radius = value
        return Circle(self._x,self._y,value)

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
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Height must be an int or a")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self._side1 = value 

    @side2.setter
    def side2(self,value)->None:
        if not isinstance(value,(int,float)) or isinstance(value,bool):
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
    
    def corners (self):
        distance = pow(pow(self._side1/2,2)+pow(self._side2/2,2),0.5)
        inner_angle=math.acos(self._side1/(2*distance))

        c1=[self._x + math.cos(inner_angle+self._angle)*distance, self._y +math.sin(inner_angle+self._angle)*distance]
        c2=[self._x + math.cos(math.pi - inner_angle +self._angle)*distance,self._y + math.sin(math.pi - inner_angle +self._angle)*distance]
        c3=[self._x + math.cos(math.pi + inner_angle+self._angle)*distance,self._y + math.sin(math.pi + inner_angle+self._angle)*distance]
        c4=[self._x + math.cos(math.tau - inner_angle+self._angle)*distance,self._y +math.sin(math.tau - inner_angle+self._angle)*distance]

        return [c1,c2,c3,c4,c1]
    
    def move(self,xdistance,ydistance):
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or not all([not isinstance(i,bool) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Rectangle(self._x,self._y,self._side1,self._side2)

    def move_to(self,new_x,new_y):
        if not all([isinstance(i,(int,float)) for i in [new_x,new_y]]) or not all([not isinstance(i,bool) for i in [new_x,new_y]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=new_x
        self._y=new_y
        return Rectangle(new_x,new_y,self._side1,self._side2)

    @staticmethod
    def euc_distance(point1,point2):
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

    def area(self):
        return self._side1*self._side2

    def perimeter(self):
        return 2*self._side1 + 2*self._side2

    def __eq__(self,other):
        if type(other)!=type(self):
            raise TypeError("Can't compare a rectangle with a non rectangle")
        if (self._side1 == other._side1 and self._side2 == other._side2 ) or (self._side2 == other._side1 and self._side1 == other._side2 ) :
            return True 
        else :
            return False

    def contains(self,x,y):
        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):
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
        if not isinstance(rotation_angle,(int,float)) or isinstance(rotation_angle,bool):
            raise TypeError("Rotation angle should be an int or a float")
        self._angle+=rotation_angle
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def make_horizontal(self):
        if self._side1>=self._side2:
            self._angle = 0
        else:
            self._angle = 90
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)
    
    def make_vertical(self):
        if self._side1>=self._side2:
            self._angle = 90
        else:
            self._angle = 0
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def scale(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Scaling Value should be a number")
        
        if value == 0 :
            raise ValueError("Scaling value can't be 0")

        if value<0 :
            raise ValueError("Scaling Value can't be negative")
        self._side1*=value
        self._side2*=value
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def change_size(self,new_side1,new_side2):
        if not all([isinstance(i,(int,float)) for i in [new_side1,new_side2]]) or not all([not isinstance(i,bool) for i in[new_side1,new_side2]]):
            raise TypeError("The new length and width must be numbers")

        if new_side1==0 or new_side2==0:
            raise ValueError("Length and width can't be 0")

        if new_side1<0 or new_side2<0:
            raise ValueError("Length and width can't be negative")

        self._side1=new_side1
        self._side2=new_side2

        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)


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
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._x = value

    @y.setter
    def y(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._y = value

    @z.setter
    def z(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Value should be a number")
        
        self._z = value

    def move(self,x,y,z):
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]) or not all([not isinstance(x,bool) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x+=x
        self._y+=y
        self._z+=z

    def move_to(self,x,y,z):
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]) or not all([not isinstance(x,bool) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x=x
        self._y=y
        self._z=z



class Cube(Shape_3D):
    def __init__(self,x,y,z,side1):
        super().__init__(x,y,z)
        self.side1=side1

    @property
    def side1(self):
        return self._side1 

    @side1.setter
    def side1(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 1 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 1 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 1 can't be negative")

        self._side1=value

    @staticmethod
    def euc_distance(point1,point2):
        return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)**0.5

    def corners(self):

        c1=[self.x+self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c2=[self.x+self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c3=[self.x+self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c4=[self.x+self.side1/2,self.y+self.side1/2,self.z-self.side1]
        c5=[self.x-self.side1/2,self.y+self.side1/2,self.z+self.side1]
        c6=[self.x-self.side1/2,self.y-self.side1/2,self.z+self.side1]
        c7=[self.x-self.side1/2,self.y-self.side1/2,self.z-self.side1]
        c8=[self.x-self.side1/2,self.y+self.side1/2,self.z-self.side1]

        return [c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5]


    def area(self):
        return self.side1**3 

    def circumference_surface(self):
        return (self.side1**2)*6


    def contains(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if (self.x-self.side1/2<=X<=self.x+self.side1/2 and self.y-self.side1/2<=Y<=self.y+self.side1/2 and self.z-self.side1/2<=Z<=self.z+self.side1/2) else False

    def move(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x+=X
        self.y+=Y
        self.z+=Z
        return Cube(self.x,self.y,self.z,self.side1)
        

    def move_to(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x=X
        self.y=Y
        self.z=Z
        return Cube(self.x,self.y,self.z,self.side1) 

    def scale(self,scaling_value):
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.side1*=scaling_value
        return Cube(self.x,self.y,self.z,self.side1)

    def change_size(self,side_value):
        if not isinstance(side_value,(int,float)) or isinstance(side_value,bool):
            raise TypeError("Side dimension must be a valid number")

        if side_value == 0:
            raise ValueError("Side dimension can't be 0")

        if side_value < 0 :
            raise ValueError("Side dimension can't be negative")

        self.side1=side_value
        return Cube(self.x,self.y,self.z,self.side1)
        

    def plot(self):
        pass 



class Rec_Cuboid(Cube):
    def __init__(self,x,y,z,side1,side2,side3):
        super().__init__(x,y,z,side1)
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
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 2 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 2 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 2 can't be negative")

        self._side2=value

    @side3.setter
    def side3(self,value) :
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Dimension of side 3 should be a valid number")
        
        if value==0:
            raise ValueError("Dimension of side 3 can't be 0")
        
        if value<0:
            raise ValueError("Dimension of side 3 can't be negative")

        self._side3=value

    def area(self):
        return self.side1*self.side2*self.side3 

    def circumference_surface(self):
        return self.side1*self.side2*2 + self.side1*self.side3*2 + self.side2*self.side3*2

    def contains(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if  self.x-self.side1 <=X<= self.x+self.side1 and self.y-self.side2 <=Y<= self.y+self.side2 and self.z-self.side3 <=Z<= self.z+self.side3 else False

    def rotate(self,axis,angle):
        pass

    def scale(self,scaling_value):
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

    def change_size(self,new_side1,new_side2,new_side3):
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
    
    def corners(self):
        c1=[self.x+self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c2=[self.x+self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c3=[self.x+self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c4=[self.x+self.side1/2,self.y+self.side2/2,self.z-self.side3]
        c5=[self.x-self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c6=[self.x-self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c7=[self.x-self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c8=[self.x-self.side1/2,self.y+self.side2/2,self.z-self.side3]

        return [c1,c2,c3,c4,c1,c5,c6,c2,c6,c7,c3,c7,c8,c4,c8,c5]

    def plot(self):
        pass 
        


class Sphere(Shape_3D):
    def __init__(self,x,y,z,radius):
        super().__init__(x,y,z)
        self.radius=radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError("Radius value must be a valid number")
        if value==0:
            raise ValueError("Radius can't be 0")
        if value<0:
            raise ValueError("Radius can't be negative")
        
        self._radius=value

    def volume(self):
        return 4 * math.pi*(self.radius**3)/3

    def circumference_surface(self):
        return 4*math.pi*(self.radius**2)

    def contains(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        return True if  ((self.x-X)**2 + (self.y-Y)**2 + (self.z-Z)**2)**0.5 <= self.radius else False


    def move(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x +=X
        self.y +=Y
        self.z +=Z
        return Sphere(self.x,self.y,self.z,self.radius)

    def move_to(self,X,Y,Z):
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        self.x =X
        self.y =Y
        self.z =Z
        return Sphere(self.x,self.y,self.z,self.radius) 


    def scale(self,scaling_value):
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.radius *= scaling_value
        return Sphere(self.x,self.y,self.z,self.radius)

    def change_radius(self,new_radius_value):
        if not isinstance(new_radius_value,(int,float)) or isinstance(new_radius_value,bool):
            raise TypeError("New radius value must be a valid number")

        if new_radius_value == 0:
            raise ValueError("New radius value can't be 0")

        if new_radius_value < 0 :
            raise ValueError("New radius value can't be negative")

        self.radius = new_radius_value
        return Sphere(self.x,self.y,self.z,self.radius)

    def plot(self):
        pass 

