# Flocking Behaviour Library / Module / Whatever
This is a tiny python library that provides the interface to mimic flocking behaviour 

## Installation

You can just clone it and hook it up to whatever code or multiple agents simulations you have

```bash
git clone https://github.com/LichcrazeLC/flocking-behaviour-lib.git
```
## Usage

The flock() function takes a group of agents, an agent position and an agent velocity and computes a new velocity vector which is a sum of the separation, alignment and cohesion functions for the requesting agent. Each flocking behaviour function is weighted and the result cand be easily tweaked by changing the weights.

```python
avoidance_vector_weight = 2
alignment_vector_weight = 5
cohesion_vector_weight = 1

def flock(rock_group, pos, vel):
...
return normalizeVector([cohesion_vector[0] * cohesion_vector_weight + alignment_vector[0] * alignment_vector_weight + separation_vector[0] * avoidance_vector_weight + vel[0], cohesion_vector[1] * cohesion_vector_weight + alignment_vector[1] * alignment_vector_weight + separation_vector[1] * avoidance_vector_weight + vel[1]])
```

There's also an attack() method that has nothing to do with flocking behaviour, but returns a velocity vector which aggressively targets one particular point.

```python
def attack(my_ship, pos, vel):
    if dist(pos, my_ship.get_pos()) < 200:      
        vec = normalizeVector([my_ship.get_pos()[0] - pos[0], my_ship.get_pos()[1] - pos[1]])
        return [vec[0] * 2, vec[1] * 2]
    else:
        return False
```

## Contributing
We've already been through this.
