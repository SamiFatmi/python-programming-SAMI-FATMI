from logging import error
from unittest.main import main
from shapes import Circle
from shapes import Rectangle
from shapes import Sphere
from shapes import Rec_Cuboid
from shapes import Cube
import numpy as np

import matplotlib.pyplot as plt
import time # https://realpython.com/python-sleep/
import os

#creating lists for the geometric shapes that our used will create
circle_list=[] 
square_list=[] 
rectangle_list=[] 

sphere_list=[] 
rec_cuboid_list=[] 
cube_list=[] 


while True : #program will run until we chose to quit by entering Q in the main menu 
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal screen, this will be done before each print statement, syntax found on : https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    main_choice=input("Please enter you choice:\n\n2 = 2D Geometry Shapes\n\n3 = 3D Geometry Shapes\n\nQ = Quit\n\n\n").strip() #Taking the user's choice 

    if main_choice not in ["2","3","Q","q"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please enter a valid choice")

    elif main_choice.capitalize()=="Q":
        break

    elif main_choice=="2" : #2D Geometry
        while True:
            try:
                show_plot=True  #boolean to keep track of the cases where we should plot or not plot

                os.system('cls' if os.name == 'nt' else 'clear')
                choice1=input("\n1. Create a new shape\n\n2. Select a shape\n\nQ. Quit\n\n\n").strip()
                if choice1 not in ["1","2","Q","q"]:
                    print("Please enter a valid choice")
                    time.sleep(1.5)
                    show_plot=False 

                elif choice1=="1": # Case : user wants to create a new 2D shape
                    os.system('cls' if os.name == 'nt' else 'clear')
                    choice2=((input("\nWhat type of shape ?\n\nA.Circle\n\nB.Rectangle\n\nC.Square\n\nM. Go back to main menu\n\n\n")).strip()).capitalize()
                    
                    if choice2 not in ["A","B","C","M"]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Invalid choice")
                        time.sleep(1.5)
                        show_plot=False 
                    
                    elif choice2 =="A":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x=float(input("Please enter the X coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y=float(input("Please enter the Y coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        radius=float(input("Please enter the RADIUS of your circle\n\n\n").strip())
                        
                        name = "cir"+str(len(circle_list))
                        circle_list.append([name,Circle(x,y,radius)])

                    elif choice2 =="B":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x=float(input("Please enter the X coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y=float(input("Please enter the Y coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side1=float(input("Please enter the WIDTH of you rectangle\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side2=float(input("Please enter the HEIGHT of you rectangle\n\n\n").strip())
                        
                        name = "rec" +str(len(rectangle_list))
                        rectangle_list.append([name,Rectangle(x,y,side1,side2)])

                    elif choice2 =="C":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x=float(input("Please enter the X coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y=float(input("Please enter the Y coordinate\n\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side=float(input("Please enter the WIDTH of your square \n\n\n").strip())
                        
                        name = "squ"+str(len(square_list))
                        square_list.append([name,Rectangle(x,y,side,side)])


                    elif choice2 =="M":
                        show_plot=False 
                        continue

                elif choice1=="2": 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    choice2=((input("What type of shape ?\nA.Circle\nB.Rectangle\nC.Square\n\nM. Go back to main menu\n\n\n")).strip()).capitalize()
                    if choice2 not in ["A","B","C","M"]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Please enter a valid choice")
                        time.sleep(1.5)
                        show_plot=False 
                    elif choice2 =="A":
                        if len(circle_list)==0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("There are no circles to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a circle by entering its number\n")
                            for index_circle in range(len(circle_list)):
                                print(f"{index_circle}. {circle_list[index_circle][0]}")

                            choice3=int(input("").strip())

                            if choice3>=len(circle_list) or choice3<0:
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 

                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                selected_shape=circle_list[choice3][1]
                                choice4=input("What do you want to do with this circle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n8. Compare it to another\n\n9. Info\n\nR. Remove\n\n\n").strip()
                                
                                if choice4 not in ["1","2","3","4","5","6","7","8","9","R","r"]:
                                    print("Please enter a valid choice")
                                    time.sleep(1.5)
                                    show_plot=False 
                                
                                elif choice4=="1": #Area
                                    print(f"\n{selected_shape.area()}\n")
                                
                                elif choice4=="2": #Circumference
                                    print(f"\n{selected_shape.perimeter}\n")
                                
                                elif choice4=="3": #Move it
                                    x=float(input("Please enter the translation distance in X axis :\n\n").strip())
                                    y=float(input("Please enter the translation distance in Y axis :\n\n").strip())

                                    selected_shape.move(x,y)
                                    
                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())

                                    selected_shape.move_to(x,y)

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float((input("Please enter the scaling value ").strip()))
                                    
                                    selected_shape.scale(scaling_value)

                                elif choice4=="6": #Change radius
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_radius=float(input("Please enter the new radius value ").strip())
                                    selected_shape.change_radius(new_radius)

                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :").strip())
                                   
                                    if selected_shape.contain(x,y) :
                                        print(f"The point ({x},{y}) is withing this circle")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y}) is not withing this circle")
                                        time.sleep(4)

                                elif choice4=="8": #Compare it to another circle
                                    show_plot=False
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("There are no circles to be selected")

                                    if len(circle_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no circles to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a circle by entering its number\n")
                                        for index_circle in range(len(circle_list)):
                                            if index_circle!=choice3:
                                                print(f"{index_circle}. {circle_list[index_circle][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if circle_list[choice3][1]==circle_list[choice5][1]:
                                            print("These 2 circles are equal")
                                        else : 
                                            print("These 2 circles are not equal equal")
                                    
                                    time.sleep(4)

                                elif choice4=="9" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)


                                elif choice4=="R" or choice4=="r": #Remove it
                                    circle_list.remove(circle_list[choice3])
                                
                    elif choice2 =="B":
                        if len(rectangle_list)==0:
                            print("There are no rectangles to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a rectangle by entering its number")
                            for index_rec in range(len(rectangle_list)):
                                print(f"{index_rec}. {rectangle_list[index_rec][0]}")
                            
                            choice3=int(input("").strip())

                            if choice3>=len(rectangle_list) or choice3<0:
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 
                            else:
                                selected_shape=rectangle_list[choice3][1]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                choice4=input("What do you want to do with this rectangle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Compare to another rectangle\n9. Rotate\n10. Make horizontal\n11. Make vertical\n12. Info\nR. Remove\n\n\n")
                                
                                if choice4 not in ["1","2","3","4","5","6","7","8","9","10","11","12","r","R"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Please enter a valid choice")
                                    time.sleep(1.5)
                                    show_plot=False

                                elif choice4=="1": #Area
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.area()}\n")
                                    time.sleep(4)
                                    show_plot=False
                                elif choice4=="2": #Circumference
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False
                                    print(f"\n{selected_shape.perimeter}\n")
                                    time.sleep(4)
                                
                                elif choice4=="3": #Move it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the distances in the X direction").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the distances in the Y direction").strip())
                                    rectangle_list[choice3][1]=selected_shape.move(x,y)

                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    rectangle_list[choice3][1]=selected_shape.move_to(x,y)
                                   

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                    scaling_value=int(input("Please enter the scaling value :\n\n").strip())
                                    rectangle_list[choice3][1]=selected_shape.scale(scaling_value)
                                    
                                elif choice4=="6": #Change dimensions
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_x=float(input("Please enter the new WIDTH :\n\n").strip())
                                    new_y=float(input("Please enter the new HEIGHT :\n\n").strip())
                                    rectangle_list[choice3][1]=selected_shape.change_size(new_x,new_y)
                                    
                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    if selected_shape.contains(x,y) :
                                        print(f"The point ({x},{y}) is withing this rectangle")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y}) is not withing this rectangle")
                                        time.sleep(4)
                                            
                                elif choice4=="8": #Compare it to another rectangle

                                    show_plot=False
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("There are no rectangles to be selected")

                                    if len(rectangle_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no rectangles to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a rectangle by entering its number\n")
                                        for index_rectangle in range(len(rectangle_list)):
                                            if index_rectangle!=choice3:
                                                print(f"{index_rectangle}. {rectangle_list[index_rectangle][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if rectangle_list[choice3][1]==rectangle_list[choice5][1]:
                                            print("These 2 rectangles are equal")
                                        else : 
                                            print("These 2 rectangles are not equal")
                                    
                                    time.sleep(4)

                                elif choice4=="9": #rotate
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    angle=float(input("Please enter the rotation angle :\n\n").strip())
                                    selected_shape.rotate(angle) 
                                
                                elif choice4=="10": #Make horizontal
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    rectangle_list[choice3][1]=selected_shape.make_horizontal()

                                elif choice4=="11": #Make vertical
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    rectangle_list[choice3][1]=selected_shape.make_vertical()
                                
                                elif choice4=="12" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)

                                elif choice4.capitalize()=="R": #Remove it
                                    rectangle_list.remove(rectangle_list[choice3])

                    elif choice2 =="C": # Select a square

                        if len(square_list)==0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("There are no squares to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a square by entering its number")
                            for index_squ in range(len(square_list)):
                                print(f"{index_squ}. {square_list[index_squ][0]}")

                            choice3=int(input("").strip())

                            if choice3>=len(square_list) or choice3<0:
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 
                            else:
                                selected_shape=square_list[choice3][1]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                choice4=input("What do you want to do with this square ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Compare it to another square\n9. Rotate\n10. Make it horizontal\n11. Info\nR. Remove\n\n\n").strip()

                                if choice4 not in ["1","2","3","4","5","6","7","8","9","10","11","R","r"]:
                                    print("Please enter a valid choice")
                                    time.sleep(1.5)
                                    show_plot=False 
                                
                                elif choice4=="1": #Area
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.area()}\n")
                                
                                elif choice4=="2": #Circumference
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.perimeter}\n")
                                
                                elif choice4=="3": #Move it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the distance in the X direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the distance in the Y direction :\n\n").strip())
                                    selected_shape.move(x,y)
                
                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    selected_shape.move_to(x,y)

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float(input("Please enter the scaling value :\n\n").strip())
                                    selected_shape.scale(scaling_value)
                                    
                                elif choice4=="6": #Change dimensions
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_x=float(input("Please enter the new width :\n\n").strip())
                                    selected_shape.change_size(new_x,new_x)
                                
                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    if selected_shape.contains(x,y) :
                                        print(f"The point ({x},{y}) is withing this square")
                                        time.sleep(4)
                                    else :
                                        print(f"The point ({x},{y}) is not withing this square")
                                        time.sleep(4)

                                elif choice4=="8": #Compare it to another square
                                    show_plot=False

                                    if len(square_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no squares to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a circle by entering its number\n")
                                        for index_square in range(len(square_list)):
                                            if index_square!=choice3:
                                                print(f"{index_square}. {square_list[index_square][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if square_list[choice3][1]==square_list[choice5][1]:
                                            print("These 2 squares are equal")
                                        else : 
                                            print("These 2 squares are not equal")
                                    
                                    time.sleep(4)
                                    
                                elif choice4=="9": #rotate
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    angle=float(input("Please enter the rotation angle :\n\n").strip())
                                    selected_shape.rotate(angle)

                                elif choice4=="10": #Make Horizontal
                                    selected_shape.make_horizontal()

                                elif choice4=="11" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)
                            
                                elif choice4.capitalize()=="R": #Remove it
                                    square_list.remove(square_list[choice3])

                    elif choice2 =="M": # Back to the Main Menu
                        show_plot=False 
                        continue

                elif choice1.capitalize()=="Q": # Quit
                    break
            
            except (TypeError,ValueError) as err:
                print(err)
                time.sleep(1.5)   
                show_plot = False

            if show_plot:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please close the plot figure to continue")
                
                for circle in circle_list:
                    circle[1].plot()

                for rectangle in rectangle_list:
                    rectangle[1].plot()

                for square in square_list:
                    square[1].plot()

                plt.gca().set_aspect('equal', adjustable='box')
                plt.grid()
                plt.show()


    else: # 3D Shapes
        while True:
            try:
                show_plot=True 

                os.system('cls' if os.name == 'nt' else 'clear')
                choice1=input("\n1. Create a new 3D shape\n\n2. Select a 3D shape\n\nQ. Quit\n\n\n").strip() # 3D main menu
                if choice1 not in ["1","2","Q","q"]:
                    print("Please enter a valid choice")
                    time.sleep(1.5)
                    show_plot=False 

                elif choice1=="1": #create a 3d shape
                    os.system('cls' if os.name == 'nt' else 'clear') #clear the
                    choice2=(input("\nWhat type of shape ?\n\nA.Sphere\n\nB.Rectangular Cuboid\n\nC.Cube\n\nM. Go back to main menu\n\n\n").strip()).capitalize()
                    
                    if choice2 not in ["A","B","C","M"]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Invalid choice")
                        time.sleep(1.5)
                        show_plot=False 
                    
                    elif choice2 =="A":#create a sphere
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x = float(input("Please enter the X coordinate of the center of your sphere :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y = float(input("Please enter the Y coordinate of the center of your sphere :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        z = float(input("Please enter the Z coordinate of the center of your sphere :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        radius = float(input("Please enter the RADIUS of your sphere :\n\n").strip())

                        name = "sphere"+str(len(sphere_list))

                        sphere_list.append([name,Sphere(x,y,z,radius)])
                        
                    elif choice2 =="B":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x = float(input("Please enter the X coordinate of the center of your rectangular cuboid :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y = float(input("Please enter the Y coordinate of the center of your rectangular cuboid :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        z = float(input("Please enter the Z coordinate of the center of your rectangular cuboid :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side1 = float(input("Please enter the WIDTH of your rectangular cuboid :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side2 = float(input("Please enter the HEIGHT of your rectangular cuboid :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side3 = float(input("Please enter the DEPTH of your rectangular cuboid :\n\n").strip())

                        name = "r_cub" +str(len(rec_cuboid_list))
                        rec_cuboid_list.append([name,Rec_Cuboid(x,y,z,side1,side2,side3)])
                      
                    elif choice2 =="C": #create a Cube
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x = float(input("Please enter the X coordinate of the center of your cube :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y = float(input("Please enter the Y coordinate of the center of your cube :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        z = float(input("Please enter the Z coordinate of the center of your cube :\n\n").strip())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        side = float(input("Please enter the WIDTH of your cube :\n\n").strip())
                        
                        name = "cub"+str(len(cube_list))
                        cube_list.append([name,Cube(x,y,z,side)])

                    elif choice2 =="M":
                        show_plot=False 
                        continue
                
                elif choice1=="2": 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    choice2=(input("What type of shape ?\nA.Sphere\nB.Rectangular Cuboid\nC.Cube\nM. Go back to main menu\n\n\n").strip()).capitalize()
                    
                    if choice2 not in ["A","B","C","M"]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Please enter a valid choice")
                        time.sleep(1.5)
                        show_plot=False 
                    
                    elif choice2 =="A":
                        if len(sphere_list)==0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("There are no spheres to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a sphere by entering its number :\n")
                            for index_sphere in range(len(sphere_list)):
                                print(f"{index_sphere}. {sphere_list[index_sphere][0]}")
                            choice3=int(input("").strip())

                            if choice3>=len(sphere_list) or choice3<0:
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 
                            
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                selected_shape=sphere_list[choice3][1]
                                choice4=input("What do you want to do with this sphere ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n8. Compare with another sphere\n9.Info\nR. Remove\n\n\n").strip()
                                
                                if choice4 not in ["1","2","3","4","5","6","7","8","9","r","R"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Please enter a valid choice")
                                    time.sleep(1.5)
                                    show_plot=False 
                                
                                elif choice4=="1": #Area
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.volume()}\n")
                                    time.sleep(3)
                                
                                elif choice4=="2": #Circumference
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.circumference_surface()}\n")
                                    time.sleep(3)
                                
                                elif choice4=="3": #Move it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the distances of which you want to move your sphere in the X direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the distances of which you want to move your sphere in the Y direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the distances of which you want to move your sphere in the Z direction :\n\n").strip())

                                    selected_shape.move(x,y,z)
                                    

                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())
                                    
                                    selected_shape.move_to(x,y,z)                          

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float(input("Please enter the scaling value ").strip())

                                    selected_shape.scale(scaling_value)
                                    

                                elif choice4=="6": #Change radius
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_radius=float(input("Please enter the new radius value ").strip())

                                    selected_shape.change_radius(new_radius)
                                    

                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())

                                    if selected_shape.contains(x,y,z) :
                                        print(f"The point ({x},{y},{z}) is withing this sphere")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this sphere")
                                        time.sleep(4)  

                                elif choice4=="8": #Compare it to another sphere
                                    show_plot=False

                                    if len(sphere_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no spheres to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a circle by entering its number\n")
                                        for index_sphere in range(len(sphere_list)):
                                            if index_sphere!=choice3:
                                                print(f"{index_sphere}. {sphere_list[index_sphere][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if sphere_list[choice3][1]==sphere_list[choice5][1]:
                                            print("These 2 spheres are equal")
                                        else : 
                                            print("These 2 spheres are not equal")
                                    
                                    time.sleep(4) 
                                
                                elif choice4=="9" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)
                                
                                elif choice4.capitalize()=="R": #Remove it
                                    sphere_list.remove(sphere_list[choice3])
                                    

                    elif choice2 =="B": # Rectangular cuboid
                        if len(rec_cuboid_list)==0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("There are no rectangular cuboids to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a rectangular cuboid by entering its number")
                            for index_rec in range(len(rec_cuboid_list)):
                                print(f"{index_rec}. {rec_cuboid_list[index_rec][0]}")
                            
                            choice3=int(input("").strip())

                            if choice3>=len(rec_cuboid_list) or choice3<0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 
                            else:
                                selected_shape=rec_cuboid_list[choice3][1]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                choice4=input("What do you want to do with this rectangular cuboid ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Compare it to another rectangular cuboid\n9. Info\nR. Remove\n\n\n").strip()
                                
                                if choice4 not in ["1","2","3","4","5","6","7","8","9","r","R"]: # Invalid choice
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Please enter a valid choice")
                                    show_plot=False 
                                
                                elif choice4=="1": #Volume
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.volume()}\n")
                                
                                elif choice4=="2": #Circumference
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.circumference_surface()}\n")
                                
                                elif choice4=="3": #Move it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the distances of which you want to move your rectangular cuboid in the X direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the distances of which you want to move your rectangular cuboid in the Y direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the distances of which you want to move your rectangular cuboid in the Z direction :\n\n").strip())

                                    rec_cuboid_list[choice3][1]=selected_shape.move(x,y,z)

                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'ccoordinate of the pointlear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())

                                    rec_cuboid_list[choice3][1]=selected_shape.move_to(x,y,z)

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float(input("Please enter the scaling value :\n\n").strip())

                                    rec_cuboid_list[choice3][1]=selected_shape.scale(scaling_value)                            

                                elif choice4=="6": #Change dimensions
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_x=float(input("Please enter the new WIDTH :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_y=float(input("Please enter the new HEIGHT :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_z=float(input("Please enter the new DEPTH :\n\n").strip())

                                    rec_cuboid_list[choice3][1]=selected_shape.change_size(new_x,new_y,new_z)

                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'ccoordinate of the pointlear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())

                                    if selected_shape.contains(x,y,z) :
                                        print(f"The point ({x},{y},{z}) is withing this rectangular cuboid")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this rectangular cuboid")
                                        time.sleep(4)
                                            
                                elif choice4=="8": #Compare it to another rectangular cuboid
                                    show_plot=False

                                    if len(rec_cuboid_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no rectangular cuboids to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a rectangular cuboid by entering its number\n")
                                        for index_rec_cuboid in range(len(rec_cuboid_list)):
                                            if index_rec_cuboid!=choice3:
                                                print(f"{index_rec_cuboid}. {rec_cuboid_list[index_rec_cuboid][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if rec_cuboid_list[choice3][1]==rec_cuboid_list[choice5][1]:
                                            print("These 2 rectangular cuboids are equal")
                                        else : 
                                            print("These 2 rectangular cuboids are not equal")
                                    
                                    time.sleep(4) 
                                
                                elif choice4=="9" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)

                                elif choice4.capitalize()=="R": #Remove it
                                    rec_cuboid_list.remove(rec_cuboid_list[choice3])

                    elif choice2 =="C": # Select a cube

                        if len(cube_list)==0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("There are no cubes to be selected")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Please select a cube by entering its number :\n")
                            for index_squ in range(len(cube_list)):
                                print(f"{index_squ}. {cube_list[index_squ][0]}")

                            choice3=int(input("").strip())

                            if choice3>=len(cube_list) or choice3<0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Invalid index")
                                time.sleep(1.5)
                                show_plot=False 
                            else:
                                selected_shape=cube_list[choice3][1]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                choice4=input("What do you want to do with this square ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Compare it to another cube\n9. Info\nR. Remove\n\n\n").strip()
                                
                                if choice4 not in ["1","2","3","4","5","6","7","8","9","r","R"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Please enter a valid choice")
                                    time.sleep(1.5)
                                    show_plot=False 
                                
                                elif choice4=="1": #volume
                                    show_plot=False
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.volume()}\n")
                                    time.sleep(4)
                                
                                elif choice4=="2": #Circumference
                                    show_plot=False
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"\n{selected_shape.circumference_surface()}\n")
                                    time.sleep(4)
                                
                                elif choice4=="3": #Move it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the distances of which you want to move your cube in the X direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    y=float(input("Please enter the distances of which you want to move your cube in the Y direction :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the distances of which you want to move your cube in the Z direction :\n\n").strip())
                                    
                                    selected_shape.move(x,y,z)
                                    
                                elif choice4=="4": #Move to a certain point
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'ccoordinate of the pointlear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())

                                    selected_shape.move_to(x,y,z)

                                elif choice4=="5": #Scale it
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    scaling_value=float(input("Please enter the scaling value :\n\n").strip())
                                    
                                    selected_shape.scale(scaling_value)
                                    
                                elif choice4=="6": #Change dimensions
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    new_x=float(input("Please enter the new WIDTH :\n\n").strip())
                                    
                                    selected_shape.change_size(new_x)

                                elif choice4=="7": ##Check if it contains a point
                                    show_plot=False 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x=float(input("Please enter the X coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'ccoordinate of the pointlear')
                                    y=float(input("Please enter the Y coordinate of the point :\n\n").strip())
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    z=float(input("Please enter the Z coordinate of the point :\n\n").strip())

                                    if selected_shape.contains(x,y,z) :
                                        print(f"The point ({x},{y},{z}) is withing this cube")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this cube")
                                        time.sleep(4)
                                
                                elif choice4=="8": #Compare it to another cube
                                    show_plot=False

                                    if len(cube_list) < 2:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("There are no cubes to be selected")
                                        time.sleep(1.5)
                                        show_plot=False 
                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Please select a cube by entering its number\n")
                                        for index_cube in range(len(cube_list)):
                                            if index_cube!=choice3:
                                                print(f"{index_cube}. {cube_list[index_cube][0]}")

                                        choice5=int(input("").strip())
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if cube_list[choice3][1]==cube_list[choice5][1]:
                                            print("These 2 cubes are equal")
                                        else : 
                                            print("These 2 cubes are not equal")
                                    
                                    time.sleep(4) 
                                
                                elif choice4=="9" : #Info
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    show_plot=False                                    
                                    print(selected_shape)
                                    time.sleep(4)

                                elif choice4.capitalize()=="R": #Remove it
                                    cube_list.remove(cube_list[choice3])

                    elif choice2.capitalize() =="M": # Back to the Main Menu
                        show_plot=False 
                        continue

                elif choice1.capitalize()=="Q": # Quit
                    break

            except (TypeError,ValueError) as err:
                print(err)
                time.sleep(1.5)   
                show_plot = False

            if show_plot:

                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please close the plot figure to continue")

                fig = plt.figure()
                ax = plt.axes(projection='3d')
                u = np.linspace(0, np.pi, 20)
                v = np.linspace(0, 2 * np.pi, 20)

                for sphere in sphere_list:  # https://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut5.html
                    actual_sphere = sphere[1]
                    x = actual_sphere.x + np.outer(np.sin(u), np.sin(v))*actual_sphere.radius
                    y = actual_sphere.y + np.outer(np.sin(u), np.cos(v))*actual_sphere.radius
                    z = actual_sphere.z + np.outer(np.cos(u), np.ones_like(v)) *actual_sphere.radius

                    ax.plot_wireframe(x, y, z)

                    

                for rec_cuboid in rec_cuboid_list:
                    actual_rec = rec_cuboid[1]
                    corners = actual_rec.corners()
                    X = [ item[0] for item in corners]
                    Y = [ item[1] for item in corners]    
                    Z = [ item[2] for item in corners]

                    ax.plot3D(X, Y, Z)    

                for cube in cube_list:
                    actual_cube = cube[1]
                    corners = actual_cube.corners()
                    X = [ item[0] for item in corners]
                    Y = [ item[1] for item in corners]    
                    Z = [ item[2] for item in corners]

                    ax.plot3D(X, Y, Z)

                
                plt.show()
                