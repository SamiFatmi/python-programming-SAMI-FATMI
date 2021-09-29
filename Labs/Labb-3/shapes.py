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

    #TODO: implement MOVE
    #TODO: implement MOVE TO POINT



class Circle(Shape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y)
        self.radius=radius
    
    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Radius must be an int or a float")

        if value==0:
            raise ValueError("Radius can't be 0 ")

        if value<0:
            raise ValueError("Radius can't be negative ")
            
        self.radius = value 

    
    def __repr__(self):
        return f"This is a circle with center coordinates ({self.x} , {self.y}) and radius {self.radius}"

    #TODO: implement AREA
    #TODO: implement PERIMETER
    #TODO: implement ==
    #TODO: implement POINT_COMPARISION
    




class Rectangle(Shape):
    def __init__(self,x:float,y:float,side1:float,side2:float,angle:float=0)->None:
        super().__init__(x,y)
        self.side1=side1
        self.side2=side2
        self.angle=angle 
    
    @property
    def side1(self):
        return self.side1
    
    @property
    def side2(self):
        return self.side2
    
    @property
    def angle(self):
        return self.angle

    @side1.setter
    def side1(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Height must be an int or a")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self.side1 = value 

    @side2.setter
    def side2(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Height must be an int or a float")

        if value==0:
            raise ValueError("Height can't be 0 ")

        if value<0:
            raise ValueError("Height can't be negative ")

        self.side2 = value 

    @angle.setter
    def angle(self,value)->None:
        if not isinstance(value,(int,float)) :
            raise TypeError("Angle must be an int or a float ")
        self.angle = value 

    def __repr__(self):
        if self.side1==self.side2:
            return f"This is a rectangle with center coordinates ({self.x} , {self.y}), height {self.side1}, width {self.side2} and tilted with an angle of {self.angle}"
        else:
            return f"This is a square with center coordinates ({self.x} , {self.y}), height and width {self.side2} and tilted with an angle of {self.angle}"

    #TODO: implement AREA
    #TODO: implement PERIMETER
    #TODO: implement ==
    #TODO: implement POINT_COMPARISION
    #TODO: implement ROTATE



#TODO: create a cube class
#TODO: create a rectangular cuboid class
#TODO: create a sphere class
#TODO: create a cylinder class