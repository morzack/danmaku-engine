# engine.py

import math

# all the primitives for the game engine

# vector2 is a 2d vector. ez
class Vector2:
    def __init__(self, x=0, y=0, vector=None):
        self.x = x
        self.y = y
        if vector != None:
            self.x = vector.x
            self.y = vector.y
    
    def add(self, x=None, y=None, vector=None):
        if vector != None:
            self.x += vector.x
            self.y += vector.y
            return
        if x != None:
            self.x += x
        if y != None:
            self.y += y
    
    def mult(self, scalar=None, vector=None):
        if scalar != None:
            self.x *= scalar
            self.y *= scalar
            return
        if vector != None:
            self.x *= vector.x
            self.y *= vector.y
            return

    def sub(self, vector):
        # subtract another vector from this one
        vector.mult(scalar=-1)
        self.add(vector=vector)

    def div(self, scalar=None, vector=None):
        if scalar != None:
            self.x /= scalar
            self.y /= scalar
            return
        if vector != None:
            self.x /= vector.x
            self.y /= vector.y
            return

    def magnitude(self):
        # get the magnitude of this vector
        return math.sqrt(self.x**2+self.y**2)

    def normal(self):
        # get the normalized vector of this one
        return Vector2(vector=self).div(scalar=self.magnitude())

# usable for storing the position of pretty much anything
class Position:
    def __init__(self, vector=None):
        if vector != None:
            self.v = vector
        else:
            self.v = Vector2()

    # can be passed x/y coords or another position object
    def set_position(self, x=None, y=None, position=None):
        if position != None:
            self.v.x = position.v.x
            self.v.y = position.v.y
            return
        if x != None:
            self.v.x = x
        if y != None:
            self.v.y = y

    def set_x(self, new_x):
        self.v.x = new_x
    
    def set_y(self, new_y):
        self.v.y = new_y

    # get distance between two positions
    def get_distance(self, other_position):
        return math.sqrt((other_position.v.x-self.v.x)**2+(other_position.v.y-self.v.y)**2)

    def move_position(self, delta_x=0, delta_y=0):
        # move this position using deltas
        self.v.add(delta_x, delta_y)

# colliders are objects that are attached to handle collisions
class CircleCollider:
    def __init__(self, size=1):
        self.position = Position()
        self.radius = size

    def set_size(self, new_size):
        self.radius = new_size

    def check_collision_circle(self, other_collider, proximity=0):
        # proximity will cause the collision checking to stop if the other object is farther than proximity

        # get distance between centers, subtract radiuses and see if less than zero
        # if less than zero then there must be an intersect
        # it makes sense i swear
        distance = self.position.get_distance(other_collider.position)
        if proximity > 0 and distance < proximity:
            return (distance - self.radius - other_collider.radius) < 0
        else:
            return False
        # god i wish this were compiled code

# a physical object has a collider and things like that, basically things that matter
class InteractiveObject:
    def __init__(self, tags=[]):
        # tags is expected to be a list of strings for comparisons to be made

        # let's just assume it uses a circlecollider for now
        # this can be used to store the position and stuff to make it nice and easy on programming
        self.collider = CircleCollider()
        self.tags = tags # now this is where the fun begins

    def check_collisions(self, otherObjects, proximity=0, collided=True):
        # check for collisions and return all objects that collided (or not based on collided parameter)
        r = []
        for o in otherObjects:
            c = self.collider.check_collision_circle(o.collider, proximity)
            if c and collided:
                r.append(o)
            if not c and not collided:
                r.append(o)
        return r

    def check_tag(self, otherObjects, tag, present=True):
        # please gather collisions before calling this for speedyboi
        # but basically just see if there is a tag in the objects passed
        # returns a list of objects with the tag being searched for
        # present can be used to change if its looking for things _with_ the tag or without it
        r = []
        for o in otherObjects:
            p = tag in o.tags
            if p and present:
                r.append(o)
            if not p and not present:
                r.append(o)
        return r

    def check_tags(self, otherObjects, tags, present=True):
        # basically just check_tag but looks for multiple tags
        # using set so that it returns unique objects
        r = set()
        for tag in tags:
            o = self.check_tag(otherObjects, tag, present)
            r = r.update(o)
        return list(r)