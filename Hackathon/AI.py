import api
from operator import itemgetter

import random as rnd




# function checks if package would fit in a position 

def fits(o_length,o_width,o_height,x,y,z,truck_length,truck_width,truck_height,space):

    if x<0 :
        return False

    elif x+o_length >=  truck_length or y+o_width >= truck_width or z+o_height >= truck_height :
        return False
    else :
        xrange = [x for x in range(x,x+o_length,4)]
        xrange.append(x+o_length)
        yrange = [y for y in range(y,y+o_width,4)]
        yrange.append(y+o_width)
        zrange = [z for z in range(z,z+o_height,4)]
        zrange.append(z+o_height)

        for px in xrange:
            for py in yrange:
                for pz in zrange:
                    if space[px][py][pz]!=-1 :
                        return False 
    return True 


# function checks packages under 

def packages_under(length,width,x,y,z,space):
    heavy=[]
    medium=[]
    light=[]
    
    for px in [x,x+length-1]:
        for py in [y,y+width-1]:
            for pz in range(0,z,5):
                if space[px][py][pz]!=-1:
                    cube = space[px][py][pz]
                    if cube[1]==2 and cube[0] not in heavy:
                        heavy.append(cube[0])
                    elif cube[1]==1 and cube[0] not in medium:
                        medium.append(cube[0])
                    elif cube[1]==0 and cube[0] not in light:
                        light.append(cube[0])
    
    return [heavy,medium,light]

# function checks packages behind 

def packages_behind(order_class,width,height,x,y,z,space):
    higher_packages_behind = []
    empty_volume_behind = 0

    for px in range(0,x,3):
        for py in [y,(y+width)//2,y+width-1]:
            for pz in [z,z+height-1]:
                if space[px][py][pz]!= -1 and space[px][py][pz][2] < order_class and space[px][py][pz][0] not in higher_packages_behind :
                    higher_packages_behind.append(space[px][py][pz][0])
                elif space[px][py][pz] == -1 :
                    empty_volume_behind += 1

    
    return [higher_packages_behind,empty_volume_behind]

def volume_right(x,y,z,length,height,space):
    empty_space = 0
    if y==0 : 
        return empty_space 
    else : 
        for index_z in [z,z+height//2,z+height-1]:
            for index_x in [x,x+length//2,x+length-1]:
                for index_y in range(y-1,-1,-1):
                    if space[index_x][index_y][index_z]!=-1:
                        return empty_space
            empty_space +=1
    
    return empty_space


# place a package in the space 

def place_package(package_id,package_weight_class,package_order_class,best_length,best_width,best_height,x,y,z,space):
    for px in range(x,x+best_length):
        for py in range(y,y+best_width):
            for pz in range(z,z+best_height):
                space[px][py][pz]=[package_id,package_weight_class,package_order_class]



map_name = "training1"
api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4" 
response = api.new_game(api_key, map_name)
game_info = response


vehicle_length = game_info["vehicle"]["length"]
vehicle_width = game_info["vehicle"]["width"]
vehicle_height = game_info["vehicle"]["height"]
kartonger = game_info["dimensions"]


truck_length = vehicle_length
truck_width = vehicle_width
truck_height = vehicle_height


weight = [-5,-12,-50,-100,-100,-500,-700]

#creating packages' list 
packages=[]

for kartong in kartonger:
    packages.append([kartong['id'],kartong['length'],kartong['width'],kartong['height'],kartong['weightClass'],kartong['orderClass'],kartong['length']*kartong['width']*kartong['height']])

# sorting the packages twice 

packages = sorted(sorted(sorted(packages, key=itemgetter(6), reverse=True), key=itemgetter(4), reverse=True),key=itemgetter(5), reverse=True)

#creating the population 
pop_size = 50
nr_gen = 200 

genomes = [ [0,[- rnd.random() for _ in range(7)]] for __ in range(pop_size)]

gen_nr = 0



genome_nr = 0

for nr_generations in range(nr_gen):

    genome_nr = 0
    for genome in genomes:
        
    # creating the space
        
        space = [[[ - 1 for z in range(truck_height)] for y in range(truck_width)] for x in range(truck_length)]
        max_length = 0

        #weights 
        weight = genome[1]

        print(f"\nGen{gen_nr} ({genome_nr}) : Weights {weight}")
        
        # available positions :

        available_positions = [[0,y,0] for y in range(truck_width)]
        placed_packages = []

        #picking a package
        for package in packages:

            #print(f"Checking package : {package[0]}")

            #taking out the properties of the package 
            package_id = package[0]
            package_temporary_length = package[1]
            package_temporary_width = package[2]
            package_temporary_height = package[3]
            package_weight_class = package[4]
            package_order_class = package[5]

            # finding all possible orientations 

            orientation1 = [package_temporary_length,package_temporary_width,package_temporary_height]
            orientation2 = [package_temporary_length,package_temporary_height,package_temporary_width]
            orientation3 = [package_temporary_width,package_temporary_length,package_temporary_height]
            orientation4 = [package_temporary_width,package_temporary_height,package_temporary_length]
            orientation5 = [package_temporary_height,package_temporary_length,package_temporary_width]
            orientation6 = [package_temporary_height,package_temporary_width,package_temporary_length]

            orientations = [orientation1,orientation2,orientation3,orientation4,orientation5,orientation6]

            # case orientation1
            decisions = []
            #print(available_positions)

            for o in orientations : 
                o_length = o[0]
                o_width = o[1]
                o_height = o[2]

            

                #check where the package would fit 
                ap_for_this_orientation = []
                
                #print(len(available_positions))
                for ap in available_positions : 
                    x=ap[0]
                    y=ap[1]
                    z=ap[2]
                    #fit = True
                    #if x + o_length-1 < truck_length and y + o_width-1 < truck_width and z + o_height-1 < truck_height :
                    #    for x_index in range(x+1,x+o_length,2):
                    #        for y_index in range(y,y+o_width,2):
                    #            for z_index in range(z,z+o_height,2):
                    #                if space[x_index][y_index][z_index]!=-1:
                    #                    fit = False

                    #            if fit==False :
                    #                break
                    #        if fit==False :
                    #                break
                    #    if fit==False :
                    #                break
                    #else: 
                    #    fit = False 

                    #if fit :


                    if fits(o_length,o_width+1,o_height,x,y,z,truck_length,truck_width,truck_height,space):
                        ap_for_this_orientation.append(ap)

                    if [ap[0]-o_length+1,ap[1],ap[2]] not in ap_for_this_orientation and fits(o_length,o_width+1,o_height,x-o_length+1,y,z,truck_length,truck_width,truck_height,space):
                        ap_for_this_orientation.append([ap[0]-o_length+1,ap[1],ap[2]])
                        
                #print(len(ap_for_this_orientation))

                #print(f"Nr available positions : {len(ap_for_this_orientation)}")
                for p in ap_for_this_orientation:
                    x=p[0]
                    y=p[1]
                    z=p[2]    
                    
                    #check heavy packages under 
                    heavy_packages_under_heavy=0
                    medium_packages_under_heavy=0
                    light_packages_under_heavy=0

                    if package_weight_class == 2 and z>0 :
                        packs_under = packages_under(o_length,o_width,x,y,z,space)
                        heavy_packages_under_heavy = len(packs_under[0])
                        medium_packages_under_heavy = len(packs_under[1])
                        light_packages_under_heavy = len(packs_under[2])

                    
                    #check higher priority behind
                    higher_order_behind = 0
                    volume_behind = 0

                    if x != 0 :
                        higher_order_behind = len((packages_behind(package_order_class,o_width,o_height,x,y,z,space))[0])
                        volume_behind = (packages_behind(package_order_class,o_width,o_height,x,y,z,space))[1]
                    #check empty volume to the right 

                    empty_v = volume_right(x,y,z,o_length,o_height,space)

                    #check added length

                    added_length = max(max_length, x+o_length) - max_length 

                    #calculate score of the position 

                    score = heavy_packages_under_heavy * weight[0] + medium_packages_under_heavy*weight[1] + light_packages_under_heavy*weight[2] + higher_order_behind*weight[3] + volume_behind*weight[4] + added_length * weight[5] +empty_v*weight[6]

                #add score and position and orientation to list of decisions 

                    decisions.append([score,o_length,o_width,o_height,x,y,z])

            if decisions==[] :
                print("Couldn't fit all the boxes ..")
                break
            else : 
                decisions.sort(reverse=True)
                #print(f"Nr decisions made : {len(decisions)}")

                best_decision = decisions[0]
                worst_score = decisions[-1][0]
                best_score = best_decision[0]
                best_length = best_decision[1]
                best_width = best_decision[2]
                best_height = best_decision[3]
                best_x = best_decision[4]
                best_y = best_decision[5]
                best_z = best_decision[6]

                max_length = max(max_length,best_x+best_length)
                #print(f"Max_length : {max_length} = {100*max_length/truck_length} % of the truck")


                # place the package in the space 
                #print(f"Placing package {package_id} at ({best_x},{best_y},{best_z}) and dim ({best_length},{best_width},{best_height}), decisions with score {best_score} vs worst {worst_score}")
                place_package(package_id,package_weight_class,package_order_class,best_length,best_width,best_height,best_x,best_y,best_z,space)
                #placed_packages.append([package_id,best_length,best_width,best_height,best_x,best_y,best_z])
                placed_packages.append({"id": package_id, "x1": best_x, "x2": best_x, "x3": best_x, "x4": best_x,
                                                "x5": best_x + best_length, "x6": best_x + best_length, "x7": best_x + best_length, "x8": best_x + best_length,
                                                "y1": best_y, "y2": best_y, "y3": best_y, "y4": best_y,
                                                "y5": best_y + best_width, "y6": best_y + best_width, "y7": best_y + best_width, "y8": best_y + best_width,
                                                "z1": best_z, "z2": best_z, "z3": best_z, "z4": best_z,
                                                "z5": best_z + best_height, "z6": best_z + best_height, "z7": best_z + best_height, "z8": best_z + best_height, "weightClass": package_weight_class, "orderClass": package_order_class})
                # remove the available positions under the package 
                # create the new available positions 

                for y in range(best_y,best_y + best_width):
                    available_positions.append([best_x+best_length,y,best_z]) if best_z == 0 or isinstance(space[best_x+best_length][y][best_z-1],list)  else None
                    available_positions.append([best_x,y,best_z+best_height])
                    for x in range(best_x,best_x+best_length):
                        available_positions.remove([x,y,best_z]) if [x,y,best_z] in available_positions else None

                #adding the new x_lim to the new positions 
                #if max_length+1<truck_length:
                #    for y in range(truck_width):
                #        available_positions.append([max_length+1,y,0]) if [max_length+1,y,0] not in available_positions else None

                #checking if any new positions is inside a placed package
                for p in available_positions:
                    if space[p[0]][p[1]][p[2]]!=-1:
                        available_positions.remove(p)
                
                #print(f"Nr positions available : {len(available_positions)}")

        if decisions!=[]:
            try : 
                submit_game_response = api.submit_game(api_key, map_name, placed_packages)
                fitness = submit_game_response['score']
                link = submit_game_response['link']
                print(f"Fitness : {fitness} - Visualisation : {link}")
                genome[0]=fitness
            except (TypeError,ValueError) as err : 
                print(err)
        
        genome_nr +=1 

    # sorting the genomes 

    genomes.sort(reverse=True)
    print (f"Gen{gen_nr} best scores :")
    for gengen in range(5):
        print(f"    Score : {genomes[gengen][0]} - Weights : {genomes[gengen][1]}")
        


    #picking the parents
    parent1=genomes[0]
    parent2=genomes[1]

    parent3=genomes[2]
    parent4=genomes[3]
    parent5=genomes[4]


    # creating the offspring 
    if parent1[0]==0:
        genomes = [ [0,[- rnd.random() for _ in range(7)]] for __ in range(pop_size)]


    elif parent1[0]!=parent2[0] :
        genomes=[parent1,parent2,parent3,parent4,parent5]

        for indexxx in range(45):
            w1 = (rnd.choice([parent1[1][0],parent2[1][0]])) * (rnd.randint(90,110))/100
            w2 = (rnd.choice([parent1[1][1],parent2[1][1]])) * (rnd.randint(90,110))/100
            w3 = (rnd.choice([parent1[1][2],parent2[1][2]])) * (rnd.randint(90,110))/100
            w4 = (rnd.choice([parent1[1][3],parent2[1][3]])) * (rnd.randint(90,110))/100
            w5 = (rnd.choice([parent1[1][4],parent2[1][4]])) * (rnd.randint(90,110))/100
            w6 = (rnd.choice([parent1[1][5],parent2[1][5]])) * (rnd.randint(90,110))/100
            w7 = (rnd.choice([parent1[1][6],parent2[1][6]])) * (rnd.randint(90,110))/100
            
            genomes.append([0,[w1,w2,w3,w4,w5,w6,w7]])

    elif parent1[0]!=parent3[0]:
        genomes=[parent1,parent2,parent3,parent4,parent5]

        for indexxx in range(15): 
            w1 = (rnd.choice([parent1[1][0],parent2[1][0]])) * (rnd.randint(90,110))/100
            w2 = (rnd.choice([parent1[1][1],parent2[1][1]])) * (rnd.randint(90,110))/100
            w3 = (rnd.choice([parent1[1][2],parent2[1][2]])) * (rnd.randint(90,110))/100
            w4 = (rnd.choice([parent1[1][3],parent2[1][3]])) * (rnd.randint(90,110))/100
            w5 = (rnd.choice([parent1[1][4],parent2[1][4]])) * (rnd.randint(90,110))/100
            w6 = (rnd.choice([parent1[1][5],parent2[1][5]])) * (rnd.randint(90,110))/100
            w7 = (rnd.choice([parent1[1][6],parent2[1][6]])) * (rnd.randint(90,110))/100
            
            genomes.append([0,[w1,w2,w3,w4,w5,w6,w7]])

        for indexxx in range(30):
            w1 = (rnd.choice([parent1[1][0],parent2[1][0],parent3[1][0],parent4[1][0],parent5[1][0]])) * (rnd.randint(95,105))/100
            w2 = (rnd.choice([parent1[1][1],parent2[1][1],parent3[1][1],parent4[1][1],parent5[1][1]])) * (rnd.randint(95,105))/100
            w3 = (rnd.choice([parent1[1][2],parent2[1][2],parent3[1][2],parent4[1][2],parent5[1][2]])) * (rnd.randint(95,105))/100
            w4 = (rnd.choice([parent1[1][3],parent2[1][3],parent3[1][3],parent4[1][3],parent5[1][3]])) * (rnd.randint(95,105))/100
            w5 = (rnd.choice([parent1[1][4],parent2[1][4],parent3[1][4],parent4[1][4],parent5[1][4]])) * (rnd.randint(95,105))/100
            w6 = (rnd.choice([parent1[1][5],parent2[1][5],parent3[1][5],parent4[1][5],parent5[1][5]])) * (rnd.randint(95,105))/100
            w7 = (rnd.choice([parent1[1][6],parent2[1][6],parent3[1][6],parent4[1][6],parent5[1][6]])) * (rnd.randint(95,105))/100
            
            genomes.append([0,[w1,w2,w3,w4,w5,w6,w7]])

    elif parent1[0]==parent3[0]:
         
        genomes = [parent1,parent2,parent3]

        
        for indexxx in range(47):
            genweight = [ - rnd.random() for _ in range(7)]
            genomes.append([0,genweight])


    gen_nr +=1


    

