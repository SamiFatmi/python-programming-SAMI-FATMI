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
    def y(self,value:float)->None:
        if str(value)=='True' or str(value)=='False' :
            raise TypeError("y coordinate can't be a boolean")


        if not isinstance(value,(int,float)):
            raise TypeError("y coordinate must be an int or a float")
        self._y = value 

    def move(self,xdistance:float,ydistance:float)->None:
        if str(xdistance) in['True','False'] or str(ydistance) in['True','False']:
            raise TypeError("X and Y distances can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance  

    def move_to(self,x:float,y:float)->None:
        if str(x) in['True','False'] or str(y) in ['True','False']:
            raise TypeError("X and Y coordinates can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [x,y]]) :
            raise TypeError("X and Y coordinates should be a number")

        self._x=x
        self._y=y
        
    def __repr__ (self)->str:
        return (f"Type: 2D Shape\nCenter : ({self.x},{self.y})")
        


class Circle(Shape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y)
        self.radius=radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value:float)->None:
        if str(value) in ['True','False']:
            raise TypeError("Radius can't be a boolean")

        if not isinstance(value,(int,float)) :
            raise TypeError("Radius must be an int or a float")

        if value==0:
            raise ValueError("Radius can't be 0 ")

        if value<0:
            raise ValueError("Radius can't be negative ")
            
        self._radius = value 

    def area(self)->float:
        return math.pi*(self._radius**2)

    def perimeter(self)->float:
        return 2*math.pi*self._radius

    def move(self,xdistance:float,ydistance:float)->'Circle':
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or str(xdistance) in ['True','False'] or str(ydistance) in ['True','False']:                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Circle(self._x,self._y,self._radius)

    def move_to(self,x:float,y:float)->'Circle':
        if not all([isinstance(i,(int,float)) for i in [x,y]]) or str(x) in ['True','False'] or str(y) in ['True','False']:                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=x
        self._y=y
        return Circle(self._x,self._y,self._radius)
    
    def scale(self,value:float)->'Circle':
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

    def change_radius(self,value:float)->'Circle':
        if not isinstance(value,(int,float)) or str(value) in ['True','False']:
            raise TypeError("Value must be an int or a float")

        if value==0:
            raise ValueError("Value can't be 0 ")

        if value<0:
            raise ValueError("Value can't be negative ")
        self._radius = value
        return Circle(self._x,self._y,value)

    def contain(self,x:float,y:float)->bool:
        if str(x) in ['True','False'] or str(y) in ['True','False']:
            raise TypeError("X and Y can't be booleans")

        if not all([isinstance(i,(int,float)) for i in [x,y]]):
            raise TypeError("Point coordinates should be numbers")

        if pow(pow(x-self._x,2)+pow(y-self._y,2),0.5)<=self._radius :
            return True 
        else :
            return False

    def __eq__(self,other:'Circle')->bool:
        if type(other) != type(self):
            raise TypeError("Can't compare a circle with a non-circle")
        return True if self._radius == other._radius else False

    def plot(self)->None:
        X = [ self._x+ self._radius*math.cos(math.radians(i)) for i in range(1,361)]
        Y = [ self._y+ self._radius*math.sin(math.radians(i)) for i in range(1,361)]
        plt.plot(X,Y)

    def __repr__(self)->str:
        return (f"Type: Circle\nCenter : ({self.x},{self.y})\nRadius : {self.radius}")
    
    
    




class Rectangle(Shape):
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
        if not all([isinstance(i,(int,float)) for i in [xdistance,ydistance]]) or not all([not isinstance(i,bool) for i in [xdistance,ydistance]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance
        return Rectangle(self._x,self._y,self._side1,self._side2)

    def move_to(self,new_x:float,new_y:float)->'Rectangle':
        if not all([isinstance(i,(int,float)) for i in [new_x,new_y]]) or not all([not isinstance(i,bool) for i in [new_x,new_y]]):                               #https://stackoverflow.com/questions/23986266/is-there-a-better-way-of-checking-multiple-variables-are-a-single-type-in-python
            raise TypeError("X and Y distances should be a number")
        self._x=new_x
        self._y=new_y
        return Rectangle(new_x,new_y,self._side1,self._side2)

    def area(self)->float:
        return self._side1*self._side2

    def perimeter(self)->float:
        return 2*self._side1 + 2*self._side2

    def scale(self,value:float)->'Rectangle':
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
        if not isinstance(rotation_angle,(int,float)) or isinstance(rotation_angle,bool):
            raise TypeError("Rotation angle should be an int or a float")
        self._angle+=rotation_angle
        return Rectangle(self._x,self._y,self._side1,self._side2,self._angle)

    def make_horizontal(self)->'Rectangle':
        if self._side1>=self._side2:
            self._angle = 0
            return Rectangle(self._x,self._y,self._side1,self._side2,0)
        else:
            self._angle = 90
            return Rectangle(self._x,self._y,self._side1,self._side2,90)
    
    def make_vertical(self)->'Rectangle':
        if self._side1>=self._side2:
            self._angle = 90
            return Rectangle(self._x,self._y,self._side1,self._side2,90)
        else:
            self._angle = 0
            return Rectangle(self._x,self._y,self._side1,self._side2,0)

    def contains(self,x:float,y:float)->bool:
        if not all([isinstance(i,(int,float)) for i in [x,y]]) or not all([not isinstance(i,bool) for i in [x,y]]):
            raise TypeError("Point coordinates must be numbers")

        if self._angle == 0 :
            if self._x-self._side1/2 <= x <= self._x+self._side1/2 and self._y-self._side2/2 <= y <= self._y+self._side2/2:
                return True
            else:
                return False 
        else : 
            for point in self.corners():
                if self.euc_distance(point,[x,y]) > self.euc_distance((self.corners())[0],(self.corners())[2]):
                    return False
            return True 
    
    def __eq__(self,other:'Rectangle')->bool:
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
        if not all([isinstance(i,(int,float)) for i in [x,y,z]]) or not all([not isinstance(x,bool) for i in [x,y,z]]):
            raise TypeError("Values should be numbers")

        self._x+=x
        self._y+=y
        self._z+=z

    def move_to(self,x:float,y:float,z:float):
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
        return self.side1**3 

    def circumference_surface(self)->float:
        return (self.side1**2)*6


    def move(self,X:float,Y:float,Z:float)->'Cube':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x+=X
        self.y+=Y
        self.z+=Z
        return Cube(self.x,self.y,self.z,self.side1)
        

    def move_to(self,X:float,Y:float,Z:float)->'Cube':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x=X
        self.y=Y
        self.z=Z
        return Cube(self.x,self.y,self.z,self.side1) 

    def scale(self,scaling_value:float)->'Cube':
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.side1*=scaling_value
        return Cube(self.x,self.y,self.z,self.side1)

    def change_size(self,side_value:float)->'Cube':
        if not isinstance(side_value,(int,float)) or isinstance(side_value,bool):
            raise TypeError("Side dimension must be a valid number")

        if side_value == 0:
            raise ValueError("Side dimension can't be 0")

        if side_value < 0 :
            raise ValueError("Side dimension can't be negative")

        self.side1=side_value
        return Cube(self.x,self.y,self.z,self.side1)
    
    def contains(self,X:float,Y:float,Z:float)->bool:
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
        return self.side1*self.side2*self.side3 

    def circumference_surface(self)->float:
        return self.side1*self.side2*2 + self.side1*self.side3*2 + self.side2*self.side3*2

    def move(self,X:float,Y:float,Z:float)->'Rec_Cuboid':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x+=X
        self.y+=Y
        self.z+=Z
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3)
        

    def move_to(self,X:float,Y:float,Z:float)->'Rec_Cuboid':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeEßrror ("Distances must be valid numbers")

        self.x=X
        self.y=Y
        self.z=Z
        return Rec_Cuboid(self.x,self.y,self.z,self.side1,self.side2,self.side3) 


    def scale(self,scaling_value:float)->'Rec_Cuboid':
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
        c1=[self.x+self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c2=[self.x+self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c3=[self.x+self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c4=[self.x+self.side1/2,self.y+self.side2/2,self.z-self.side3]
        c5=[self.x-self.side1/2,self.y+self.side2/2,self.z+self.side3]
        c6=[self.x-self.side1/2,self.y-self.side2/2,self.z+self.side3]
        c7=[self.x-self.side1/2,self.y-self.side2/2,self.z-self.side3]
        c8=[self.x-self.side1/2,self.y+self.side2/2,self.z-self.side3]

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
        return 4 * math.pi*(self.radius**3)/3

    def circumference_surface(self)->float:
        return 4*math.pi*(self.radius**2)



    def move(self,X:float,Y:float,Z:float)->'Sphere':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Distances must be valid numbers")

        self.x +=X
        self.y +=Y
        self.z +=Z
        return Sphere(self.x,self.y,self.z,self.radius)

    def move_to(self,X:float,Y:float,Z:float)->'Sphere':
        if not all([isinstance(i,(int,float)) for i in [X,Y,Z]]) or not all([not isinstance(i,bool) for i in [X,Y,Z]]):
            raise TypeError ("Point coordinates must be valid numbers")

        self.x =X
        self.y =Y
        self.z =Z
        return Sphere(self.x,self.y,self.z,self.radius) 


    def scale(self,scaling_value:float)->'Sphere':
        if not isinstance(scaling_value,(int,float)) or isinstance(scaling_value,bool):
            raise TypeError("Scaling value must be a valid number")

        if scaling_value == 0:
            raise ValueError("Scaling value can't be 0")

        if scaling_value < 0 :
            raise ValueError("Scaling value can't be negative")

        self.radius *= scaling_value
        return Sphere(self.x,self.y,self.z,self.radius)

    def change_radius(self,new_radius_value:float)->'Sphere':
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




