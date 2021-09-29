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
        if not isinstance((xdistance,ydistance),(int,float)):
            raise TypeError("X and Y distances should be a number")
        self._x+=xdistance
        self._y+=ydistance

    def move_to(self,x,y):
        if not isinstance((x,y),(int,float)):
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
        if not isinstance((x,y),(int,float)):
            raise TypeError("Point coordinates should be numbers")
        if pow(pow(x-self._x,2)+pow(y-self._y,2),0.5)<=self._radius :
            return True 
        else :
            return False

    




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
        if self.side1==self.side2:
            return f"This is a rectangle with center coordinates ({self._x} , {self._y}), height {self._side1}, width {self._side2} and tilted with an angle of {self._angle}"
        else:
            return f"This is a square with center coordinates ({self._x} , {self._y}), height and width {self._side2} and tilted with an angle of {self._angle}"

    def corners (self):
        distance = pow(pow(self._side1/2,2)+pow(self._side2/2,2),0.5)
        inner_angle=math.acos(self._side1/(2*distance))

        '''inner_angle1 = math.acos(self._side1/(2*distance))
        inner_angle2 = math.pi - inner_angle1
        inner_angle3 = math.pi + inner_angle1
        inner_angle4 = math.tau - inner_angle1 

        
        c1v1=math.cos(inner_angle+self._angle)*distance
        c1v2=math.sin(inner_angle+self._angle)*distance

        c2v1=math.cos(math.pi - inner_angle +self._angle)*distance
        c2v2=math.sin(math.pi - inner_angle +self._angle)*distance

        c3v1=math.cos(math.pi + inner_angle+self._angle)*distance
        c3v2=math.sin(math.pi + inner_angle+self._angle)*distance

        c4v1=math.cos(math.tau - inner_angle+self._angle)*distance
        c4v2=math.sin(math.tau - inner_angle+self._angle)*distance'''

        c1=[self._x + math.cos(inner_angle+self._angle)*distance, self._y +math.sin(inner_angle+self._angle)*distance]
        c2=[self._x + math.cos(math.pi - inner_angle +self._angle)*distance,self._y + math.sin(math.pi - inner_angle +self._angle)*distance]
        c3=[self._x + math.cos(math.pi + inner_angle+self._angle)*distance,self._y + math.sin(math.pi + inner_angle+self._angle)*distance]
        c4=[self._x + math.cos(math.tau - inner_angle+self._angle)*distance,self._y +math.sin(math.tau - inner_angle+self._angle)*distance]

        return [c1,c2,c3,c4,c1]

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
        if not isinstance((x,y),(int,float)):
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

    def rotate(self,rotation_angle):
        if not isinstance(rotation_angle,(int,float)):
            raise TypeError("Rotation angle should be an int or a float")

        self._angle += math.radians(rotation_angle)




#TODO: create a cube class
#TODO: create a rectangular cuboid class
#TODO: create a sphere class
#TODO: create a cylinder class