import math

avoidance_vector_weight = 2
alignment_vector_weight = 5
cohesion_vector_weight = 1

def attack(my_ship, pos, vel):
    if dist(pos, my_ship.get_pos()) < 200:      
        vec = normalizeVector([my_ship.get_pos()[0] - pos[0], my_ship.get_pos()[1] - pos[1]])
        return [vec[0] * 2, vec[1] * 2]
    else:
        return False
        
def flock(rock_group, pos, vel):
    resulting_vector_x, resulting_vector_y = 0, 0            
    alignment_resulting_vector_x, alignment_resulting_vector_y = 0, 0
    cohesion_resulting_vector_x, cohesion_resulting_vector_y = 0, 0
    counter = 1

    adjustmentNeeded = False
        
    for rock in rock_group:
        if rock.get_pos() != pos and dist(pos, rock.get_pos()) < 150: 
                    
            #SEPARATION
            vec = (rock.get_pos()[0] - pos[0], rock.get_pos()[1] - pos[1])
            resulting_vector_x += vec[0]
            resulting_vector_y += vec[1]

            #ALIGNMENT
            alignment_resulting_vector_x += rock.vel[0]
            alignment_resulting_vector_y += rock.vel[1]
                    
            #COHESION
            cohesion_resulting_vector_x += rock.get_pos()[0]
            cohesion_resulting_vector_y += rock.get_pos()[1]
                    
            ++counter
                    
            adjustmentNeeded = True
                
    if adjustmentNeeded == True:
            #SEPARATION
            resulting_vector = (resulting_vector_x / counter, resulting_vector_y / counter)
            opposite_vector = [ -resulting_vector[0], -resulting_vector[1]]
            separation_vector = normalizeVector(opposite_vector)
                    
            #ALIGNMENT        
            alignment_vector = normalizeVector([alignment_resulting_vector_x / counter, alignment_resulting_vector_y / counter])
                    
            #COHESION
            cohesion_vector = normalizeVector([(cohesion_resulting_vector_x / counter) - pos[0], (cohesion_resulting_vector_y / counter) - pos[1]])
                    
            #COMPUTE NEW VELOCITY VECTOR
            return normalizeVector([cohesion_vector[0] * cohesion_vector_weight + alignment_vector[0] * alignment_vector_weight + separation_vector[0] * avoidance_vector_weight + vel[0], cohesion_vector[1] * cohesion_vector_weight + alignment_vector[1] * alignment_vector_weight + separation_vector[1] * avoidance_vector_weight + vel[1]])
    else:
        return False

def normalizeVector(vec):
    magnitude = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    if magnitude != 0:       
        return [vec[0] / magnitude, vec[1] / magnitude]
    else:
        return vec
    
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)