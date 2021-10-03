from logging import error
from unittest.main import main
from shapes import Shape
from shapes import Circle
from shapes import Rectangle
from shapes import Shape_3D
from shapes import Sphere
from shapes import Rec_Cuboid
from shapes import Cube
import numpy as np

import math 
import matplotlib.pyplot as plt
import time
import os


circle_list=[]
square_list=[]
rectangle_list=[]

sphere_list=[]
rec_cuboid_list=[]
cube_list=[]

choice1,choice2,choice3,choice4=0,0,0,0

program_menu= "Please enter you choice:\n\n2 = 2D Geometry Shapes\n\n3 = 3D Geometry Shapes\n\nQ = Quit\n\n\nAnswer.."

main_menu="\n1. Create a new shape\n2. Select a shape\n3. Quit\n\n\n"

menu_1="\nWhat type of shape ?\nA.Circle\nB.Rectangle\nC.Square\nM. Go back to main menu\n\n\n"
menu_circle="Please enter the x and y coordinates and the radius of your circle\n\n\n"
menu_rectangle="Please enter the x and y coordinates and height and width of you rectangle\n\n\n"
menu_square="Please enter the x and y coordinates and length of the side of your square \n\n\n"

menu_2="What type of shape ?\nA.Circle\nB.Rectangle\nC.Square\nM. Go back to main menu\n\n\n"
menu_select_circle="What do you want to do with this circle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n\n8. Remove\n\n\n"
menu_select_rectangle="What do you want to do with this rectangle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Remove\n\n\n"
menu_select_square="What do you want to do with this square ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Rotate\n8. Make it horizontale\n9. Check if it contains a point\n10. Remove\n\n\n"

main_menu_3D="\n1. Create a new 3D shape\n2. Select a 3D shape\n3. Quit\n\n\n"

menu_1_3D="\nWhat type of shape ?\nA.Sphere\nB.Rectangular Cuboid\nC.Cube\nM. Go back to main menu\n\n\n"
menu_sphere_3D="Please enter the X,Y and Z coordinates and the RADIUS of your sphere\n\n\n"
menu_rec_cuboid_3D="Please enter the X,Y and Z coordinates and the HEIGHT, WIDTH and DEPTH of you rectagular cuboid\n\n\n"
menu_cube_3D="Please enter the X,Y and Z coordinates and side length of yout cube \n\n\n"

menu_2_3D="What type of shape ?\nA.Sphere\nB.Rectangular Cuboid\nC.Cube\nM. Go back to main menu\n\n\n"
menu_select_sphere_3D="What do you want to do with this sphere ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n\n8. Remove\n\n\n"
menu_select_rec_cuboid_3D="What do you want to do with this rectangular cuboid ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Remove\n\n\n"
menu_select_cube_3D="What do you want to do with this square ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Remove\n\n\n"



while True :
    os.system('cls' if os.name == 'nt' else 'clear')
    main_choice=input(program_menu).strip()

    if main_choice not in ["2","3","Q","q"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please enter a valid choice")

    elif main_choice=="q" or main_choice=="Q":
        break

    elif main_choice=="2" : #2D Geometry
        while True:

            show_plot=True 

            os.system('cls' if os.name == 'nt' else 'clear')
            choice1=input(main_menu)
            if choice1 not in ["1","2","3"]:
                print("Please enter a valid choice")
                time.sleep(1.5)
                show_plot=False 

            elif choice1=="1":
                os.system('cls' if os.name == 'nt' else 'clear')
                choice2=(input(menu_1)).capitalize()
                if choice2!="A" and choice2!="B" and choice2!="C" and choice2!="M":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Invalid choice")
                    time.sleep(1.5)
                    show_plot=False 
                elif choice2 =="A":
                    try:             
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,radius=input(menu_circle).split()
                        x = float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y = float(y) if str(float(y))==y or str(int(y))==y else y
                        radius = float(radius) if str(float(radius))==radius or str(int(radius))==radius else radius

                        name = "cir"+str(len(circle_list))
                        try: 
                            circle_list.append([name,Circle(x,y,radius)])
                        except (ValueError,TypeError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except ValueError as err :
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 

                elif choice2 =="B":
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,side1,side2=input(menu_rectangle).split()
                        x= float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y= float(y) if (str(float(y))==y or str(int(y))==y) else y
                        side1 = float(side1) if (str(float(side1))==side1 or str(int(side1))==side1) else side1
                        side2 = float(side2) if (str(float(side2))==x or str(int(side2))==side2) else side2
                        name = "rec" +str(len(rectangle_list))
                        try:
                            rectangle_list.append([name,Rectangle(x,y,side1,side2)])
                        except (ValueError,TypeError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except (ValueError,TypeError) as err:
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 

                elif choice2 =="C":
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,side=input(menu_square).split()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x= float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y= float(y) if (str(float(y))==y or str(int(y))==y) else y
                        side = float(side) if (str(float(side))==side or str(int(side))==side) else side
                        name = "squ"+str(len(square_list))
                        try:
                            square_list.append([name,Rectangle(x,y,side,side)])
                        except (TypeError,ValueError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except (ValueError,TypeError) as err:
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 


                elif choice2 =="M":
                    show_plot=False 
                    continue
            

            elif choice1=="2":
                os.system('cls' if os.name == 'nt' else 'clear')
                choice2=(input(menu_2)).capitalize()
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
                        print("Please select a circle by entering its number\n\n")
                        for index_circle in range(len(circle_list)):
                            print(f"{index_circle}. {circle_list[index_circle][0]}")
                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(circle_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            selected_shape=circle_list[choice3][1]
                            choice4=input(menu_select_circle)
                            if choice4 not in ["1","2","3","4","5","6","7"]:
                                print("Please enter a valid choice")
                                time.sleep(1.5)
                                show_plot=False 
                            elif choice4=="1": #Area
                                print(f"\n{selected_shape.area()}\n")
                            elif choice4=="2": #Circumference
                                print(f"\n{selected_shape.perimeter}\n")
                            elif choice4=="3": #Move it
                                x,y=input("Please enter the distances of which you want to move your circle in the X and Y directions\n\n").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    selected_shape.move(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=input("Please enter the coordinates of the point you want to move your cirle to\n\n").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    selected_shape.move_to(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change radius
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_radius=input("Please enter the new radius value ")
                                new_radius=float(new_radius) if str(float(new_radius))==new_radius or str(int(new_radius))==new_radius else new_radius
                                try:
                                    selected_shape.change_radius(new_radius)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="7": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=input("Please enter the coordinates of the point ").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    if selected_shape.contain(x,y) :
                                        print(f"The point ({x},{y}) is withing this circle")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y}) is not withing this circle")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                            elif choice4=="8": #Remove it
                                circle_list.remove(circle_list[choice3])
                            

                elif choice2 =="B":
                    if len(rectangle_list)==0:
                        print("There are no rectangles to be selected")
                        time.sleep(1.5)
                        show_plot=False 
                    else:
                        print("Please select a rectangle by entering its number")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for index_rec in range(len(rectangle_list)):
                            print(f"{index_rec}. {rectangle_list[index_rec][0]}")

                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(rectangle_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            selected_shape=rectangle_list[choice3][1]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            try:
                                choice4=input(menu_select_rectangle)
                            except ValueError as err:
                                print(err)
                                time.sleep(1.5)
                                show_plot=False
                            if choice4 not in ["1","2","3","4","5","6","7","8","9","10"]:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Please enter a valid choice")
                                show_plot=False 
                            elif choice4=="1": #Area
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n{selected_shape.area()}\n")
                            elif choice4=="2": #Circumference
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n{selected_shape.perimeter}\n")
                            elif choice4=="3": #Move it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=(input("Please enter the distances of which you want to move your rectangle in the X and Y directions").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    rectangle_list[choice3][1]=selected_shape.move(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=(input("Please enter the coordinates of the point you want to move your rectangle to").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    rectangle_list[choice3][1]=selected_shape.move_to(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    rectangle_list[choice3][1]=selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change dimensions
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_x,new_y=(input("Please enter the new dimensions ").strip()).split()
                                new_x=float(new_x) if str(float(new_x))==new_x or str(int(new_x))==new_x else new_x
                                new_y=float(new_y) if str(float(new_y))==new_y or str(int(new_y))==new_y else new_y
                                try:
                                    rectangle_list[choice3][1]=selected_shape.change_size(new_x,new_y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="7": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=input("Please enter the coordinates of the point ").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    if selected_shape.contains(x,y) :
                                        print(f"The point ({x},{y}) is withing this rectangle")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y}) is not withing this rectangle")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)

                            elif choice4=="7": #Remove it
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

                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(square_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            selected_shape=square_list[choice3][1]
                            choice4=input(menu_select_square)
                            if choice4 not in ["1","2","3","4","5","6","7","8","9"]:
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
                                x,y=(input("Please enter the distances of which you want to move your rectangle in the X and Y directions").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    selected_shape.move(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=(input("Please enter the coordinates of the point you want to move your rectangle to").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    selected_shape.move_to(x,y)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change dimensions
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_x=input("Please enter the new width ")
                                new_x=float(new_x) if str(float(new_x))==new_x or str(int(new_x))==new_x else new_x
                                try:
                                    selected_shape.change_size(new_x,new_x)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="7": #rotate
                                os.system('cls' if os.name == 'nt' else 'clear')
                                angle=input("Please enter the rotation angle")
                                angle=float(angle) if str(float(angle))==angle or str(int(angle))==angle else angle

                                try:
                                    selected_shape.rotate(angle) 
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="8": #Make Horizontal
                                selected_shape.make_horizontal()

                            elif choice4=="9": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y=input("Please enter the coordinates of the point ").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                try:
                                    if selected_shape.contains(x,y) :
                                        print(f"The point ({x},{y}) is withing this square")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y}) is not withing this square")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)

                            elif choice4=="10": #Remove it
                                square_list.remove(square_list[choice3])

                elif choice2 =="M": # Back to the Main Menu
                    show_plot=False 
                    continue

            elif choice1=="3": # Quit
                break

            

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

#menu_1_3D="\nWhat type of shape ?\nA.Sphere\nB.Rectangular Cuboid\nC.Cube\nM. Go back to main menu\n\n\n"
#menu_sphere_3D="Please enter the X,Y and Z coordinates and the RADIUS of your sphere\n\n\n"
#menu_rec_cuboid_3D="Please enter the X,Y and Z coordinates and the HEIGHT, WIDTH and DEPTH of you rectagular cuboid\n\n\n"
#menu_cube_3D="Please enter the X,Y and Z coordinates and side length of yout cube \n\n\n"

#menu_2_3D="What type of shape ?\nA.Sphere\nB.Rectangular Cuboid\nC.Cube\nM. Go back to main menu\n\n\n"
#menu_select_sphere_3D="What do you want to do with this sphere ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n\n8. Remove\n\n\n"
#menu_select_rec_cuboid_3D="What do you want to do with this rectangular cuboid ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Remove\n\n\n"
#menu_select_cube_3D="What do you want to do with this square ?\n1. Volume\n2. Circumference surface\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Check if it contains a point\n8. Remove\n\n\n"

    else:
        while True:
            show_plot=True 

            os.system('cls' if os.name == 'nt' else 'clear')
            choice1=input(main_menu_3D).strip()
            if choice1 not in ["1","2","3"]:
                print("Please enter a valid choice")
                time.sleep(1.5)
                show_plot=False 

            elif choice1=="1": #create a 3d shape
                os.system('cls' if os.name == 'nt' else 'clear') #clear the
                choice2=(input(menu_1_3D)).capitalize()
                if choice2 not in ["A","B","C","M"]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Invalid choice")
                    time.sleep(1.5)
                    show_plot=False 
                elif choice2 =="A":#create a sphere
                    try:             
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,z,radius=input(menu_sphere_3D).split()
                        x = float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y = float(y) if str(float(y))==y or str(int(y))==y else y
                        z = float(z) if str(float(z))==y or str(int(z))==z else z
                        radius = float(radius) if str(float(radius))==radius or str(int(radius))==radius else radius

                        name = "sphere"+str(len(sphere_list))
                        try: 
                            sphere_list.append([name,Sphere(x,y,z,radius)])
                        except (ValueError,TypeError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except ValueError as err :
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 

                elif choice2 =="B":
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,z,side1,side2,side3=(input(menu_rec_cuboid_3D).strip()).split()
                        x= float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y= float(y) if (str(float(y))==y or str(int(y))==y) else y
                        z= float(z) if (str(float(z))==z or str(int(z))==z) else z
                        side1 = float(side1) if (str(float(side1))==side1 or str(int(side1))==side1) else side1
                        side2 = float(side2) if (str(float(side2))==side2 or str(int(side2))==side2) else side2
                        side3 = float(side3) if (str(float(side3))==side3 or str(int(side3))==side3) else side3
                        name = "r_cub" +str(len(rec_cuboid_list))
                        try:
                            rec_cuboid_list.append([name,Rec_Cuboid(x,y,z,side1,side2,side3)])
                        except (ValueError,TypeError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except (ValueError,TypeError) as err:
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 

                elif choice2 =="C": #create a Cube
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x,y,z,side=(input(menu_cube_3D).strip()).split()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        x= float(x) if (str(float(x))==x or str(int(x))==x) else x
                        y= float(y) if (str(float(y))==y or str(int(y))==y) else y
                        z= float(z) if (str(float(z))==z or str(int(z))==z) else z
                        side = float(side) if (str(float(side))==side or str(int(side))==side) else side
                        name = "cub"+str(len(cube_list))
                        try:
                            cube_list.append([name,Cube(x,y,z,side)])
                        except (TypeError,ValueError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 
                    except (ValueError,TypeError) as err:
                        print(err)
                        time.sleep(1.5)
                        show_plot=False 


                elif choice2 =="M":
                    show_plot=False 
                    continue
            

            elif choice1=="2": 
                os.system('cls' if os.name == 'nt' else 'clear')
                choice2=(input(menu_2_3D).strip()).capitalize()
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
                        print("Please select a sphere by entering its number\n\n")
                        for index_sphere in range(len(sphere_list)):
                            print(f"{index_sphere}. {sphere_list[index_sphere][0]}")
                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(sphere_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            selected_shape=sphere_list[choice3][1]
                            choice4=input(menu_select_sphere_3D).strip()
                            if choice4 not in ["1","2","3","4","5","6","7"]:
                                print("Please enter a valid choice")
                                time.sleep(1.5)
                                show_plot=False 
                            elif choice4=="1": #Area
                                print(f"\n{selected_shape.volume()}\n")
                                time.sleep(3)
                            elif choice4=="2": #Circumference
                                print(f"\n{selected_shape.circumference_surface()}\n")
                                time.sleep(3)
                            elif choice4=="3": #Move it
                                x,y,z=(input("Please enter the distances of which you want to move your sphere in the X and Y directions\n\n").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    selected_shape.move(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=input("Please enter the coordinates of the point you want to move your sphere to\n\n").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    selected_shape.move_to(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change radius
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_radius=input("Please enter the new radius value ").strip()
                                new_radius=float(new_radius) if str(float(new_radius))==new_radius or str(int(new_radius))==new_radius else new_radius
                                try:
                                    selected_shape.change_radius(new_radius)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="7": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=input("Please enter the coordinates of the point ").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    if selected_shape.contains(x,y,z) :
                                        print(f"The point ({x},{y},{z}) is withing this sphere")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this sphere")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                            elif choice4=="8": #Remove it
                                sphere_list.remove(sphere_list[choice3])
                            

                elif choice2 =="B":
                    if len(rec_cuboid_list)==0:
                        print("There are no rectangular cuboids to be selected")
                        time.sleep(1.5)
                        show_plot=False 
                    else:
                        print("Please select a rectangular cuboid by entering its number")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for index_rec in range(len(rec_cuboid_list)):
                            print(f"{index_rec}. {rec_cuboid_list[index_rec][0]}")

                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(rec_cuboid_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            selected_shape=rec_cuboid_list[choice3][1]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            try:
                                choice4=input(menu_select_rec_cuboid_3D)
                            except ValueError as err:
                                print(err)
                                time.sleep(1.5)
                                show_plot=False
                            if choice4 not in ["1","2","3","4","5","6","7","8","9","10"]:
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
                                x,y,z=(input("Please enter the distances of which you want to move your rectangle in the X,Y and Z directions").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    rec_cuboid_list[choice3][1]=selected_shape.move(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=(input("Please enter the coordinates of the point you want to move your rectangle to").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    rec_cuboid_list[choice3][1]=selected_shape.move_to(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    rec_cuboid_list[choice3][1]=selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change dimensions
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_x,new_y,new_z=(input("Please enter the new dimensions ").strip()).split()
                                new_x=float(new_x) if str(float(new_x))==new_x or str(int(new_x))==new_x else new_x
                                new_y=float(new_y) if str(float(new_y))==new_y or str(int(new_y))==new_y else new_y
                                new_z=float(new_z) if str(float(new_z))==new_z or str(int(new_z))==new_z else new_z
                                try:
                                    rec_cuboid_list[choice3][1]=selected_shape.change_size(new_x,new_y,new_z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="7": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=input("Please enter the coordinates of the point ").split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    if selected_shape.contains(x,y,z) :
                                        print(f"The point ({x},{y},{z}) is withing this rectangular cuboid")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this rectangular cuboid")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)

                            elif choice4=="7": #Remove it
                                rec_cuboid_list.remove(rec_cuboid_list[choice3])

                elif choice2 =="C": # Select a cube

                    if len(cube_list)==0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("There are no cubes to be selected")
                        time.sleep(1.5)
                        show_plot=False 
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Please select a cube by entering its number")
                        for index_squ in range(len(cube_list)):
                            print(f"{index_squ}. {cube_list[index_squ][0]}")

                        choice3=input("")
                        choice3= int(choice3) if str(int(choice3))==choice3 else choice3

                        if choice3>=len(cube_list) or choice3<0:
                            print("Invalid index")
                            time.sleep(1.5)
                            show_plot=False 
                        else:
                            selected_shape=cube_list[choice3][1]
                            choice4=input(menu_select_cube_3D)
                            if choice4 not in ["1","2","3","4","5","6","7","8","9"]:
                                print("Please enter a valid choice")
                                time.sleep(1.5)
                                show_plot=False 
                            elif choice4=="1": #volume
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n{selected_shape.volume()}\n")
                            elif choice4=="2": #Circumference
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n{selected_shape.circumference_surface()}\n")
                            elif choice4=="3": #Move it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=(input("Please enter the distances of which you want to move your rectangle in the X and Y directions").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    selected_shape.move(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="4": #Move to a certain point
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=(input("Please enter the coordinates of the point you want to move your rectangle to").strip()).split()
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    selected_shape.move_to(x,y,z)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="5": #Scale it
                                os.system('cls' if os.name == 'nt' else 'clear')
                                scaling_value=input("Please enter the scaling value ")
                                scaling_value=float(scaling_value) if str(float(scaling_value))==scaling_value or str(int(scaling_value))==scaling_value else scaling_value
                                try:
                                    selected_shape.scale(scaling_value)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 

                            elif choice4=="6": #Change dimensions
                                os.system('cls' if os.name == 'nt' else 'clear')
                                new_x=input("Please enter the new width ")
                                new_x=float(new_x) if str(float(new_x))==new_x or str(int(new_x))==new_x else new_x
                                try:
                                    selected_shape.change_size(new_x)
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)
                                    show_plot=False 


                            elif choice4=="7": ##Check if it contains a point
                                show_plot=False 
                                os.system('cls' if os.name == 'nt' else 'clear')
                                x,y,z=input("Please enter the coordinates of the point ").split()
                                
                                x=float(x) if str(float(x))==x or str(int(x))==x else x
                                y=float(y) if str(float(y))==y or str(int(y))==y else y
                                z=float(z) if str(float(z))==z or str(int(z))==z else z
                                try:
                                    if selected_shape.contains(x,y) :
                                        print(f"The point ({x},{y},{z}) is withing this cube")
                                        time.sleep(4)
                                    
                                    else :
                                        print(f"The point ({x},{y},{z}) is not withing this cube")
                                        time.sleep(4)
                                        
                                except (ValueError,TypeError) as err:
                                    print(err)
                                    time.sleep(1.5)

                            elif choice4=="8": #Remove it
                                cube_list.remove(cube_list[choice3])

                elif choice2 =="M": # Back to the Main Menu
                    show_plot=False 
                    continue

            elif choice1=="3": # Quit
                break

            

            if show_plot:

                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please close the plot figure to continue")

                fig = plt.figure()
                ax = plt.axes(projection='3d')
                u = np.linspace(0, np.pi, 20)
                v = np.linspace(0, 2 * np.pi, 20)

                for sphere in sphere_list:
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
                




