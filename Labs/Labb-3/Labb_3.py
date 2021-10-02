from shapes import Shape
from shapes import Circle
from shapes import Rectangle
import math 
import matplotlib.pyplot as plt
import time
import os


circle_list=[]
square_list=[]
rectangle_list=[]

choice1,choice2,choice3,choice4=0,0,0,0


main_menu="\n1. Create a new shape\n2. Select a shape\n3. Quit\n\n\n"

menu_1="\nWhat type of shape ?\nA.Circle\nB.Rectangle\nC.Square\nM. Go back to main menu\n\n\n"
menu_circle="Please enter the x and y coordinates and the radius of your circle\n\n\n"
menu_rectangle="Please enter the x and y coordinates and height and width of you rectangle\n\n\n"
menu_square="Please enter the x and y coordinates and length of the side of your square \n\n\n"

menu_2="What type of shape ?\nA.Circle\nB.Rectangle\nC.Square\nM. Go back to main menu\n\n\n"
menu_select_circle="What do you want to do with this circle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change radius \n7. Check if it contains a point\n\n8. Remove\n\n\n"
menu_select_rectangle="What do you want to do with this rectangle ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Rotate\n8. Make it horizontale\n9. Make it vertical\n10. Remove\n\n\n"
menu_select_square="What do you want to do with this square ?\n1. Area\n2. Circumference\n3. Move it\n4. Move it to an exact point\n5. Scale it\n6. Change dimensions to exact values\n7. Rotate\n8. Make it horizontale\n9. Remove\n\n\n"

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
                               
                            else :
                                print(f"The point ({x},{y}) is withing this circle")
                                
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
                    choice4=input(menu_select_rectangle)
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

                    elif choice4=="7": #rotate
                        os.system('cls' if os.name == 'nt' else 'clear')
                        angle=input("Please enter the rotation angle")
                        angle=float(angle) if str(float(angle))==angle or str(int(angle))==angle else angle

                        try:
                            rectangle_list[choice3][1]=selected_shape.rotate(angle)
                        except (ValueError,TypeError) as err:
                            print(err)
                            time.sleep(1.5)
                            show_plot=False 

                    elif choice4=="8": #Make Horizontal
                        rectangle_list[choice3][1]=selected_shape.make_horizontal()

                    elif choice4=="9": #Make Vertical
                        rectangle_list[choice3][1]=selected_shape.make_vertical()

                    elif choice4=="10": #Remove it
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

                    elif choice4=="9": #Remove it
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
        
        time.sleep(1)
        plt.show()





