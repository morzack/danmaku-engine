# bullet.py

from engine import Position, InteractiveObject, Vector2

import math
import json

# a class that can shoot bullets, because that's important
# think of this more as a barrel rather than an enemy
# like enemies/players should have _these_
# these are also colliderless
class ShootingObject:
    def __init__(self, tags=[], default_speed=0, relative_position=Position()):
        # note that the tags are what are passed on to the spawned bullets
        self.tags = tags
        # relative position is relative to parent, true is relative to screen
        self.relative_position = relative_position
        self.true_position = Position()
        
        self.default_speed = default_speed
    
    def set_tags(self, tags):
        self.tags = tags

    def update_position_parent(self, parent_position):
        # note that this should be called pretty frequently
        # parent_position is used to update the true position
        # please remember to update the relative position when moving this around
        self.true_position.set_position(position=Position(Vector2(vector=parent_position).add(vector=self.relative_position.v)))
    
    def spawn_bullet(self, speed=None, normal_velocity=None, angle=None):
        # spawn a bullet with a given velocity or angle
        if speed == None and self.default_speed > 0:
            speed = self.default_speed

        if normal_velocity != None:
            return Bullet(self.true_position, normal_velocity, speed, self.tags)
        if angle != None:
            # trig *shudders*
            r = math.radians(angle)
            d_y = speed*math.sin(r)
            d_x = speed*math.cos(r)
            return Bullet(self.true_position, Vector2(d_x, d_y), speed, self.tags)

# basically just a bullet
# note that _these_ bullets have a set velocity and always move with it
# you want curvy bullets? i guess do it yourself.
class Bullet(InteractiveObject):
    def __init__(self, position, normal_velocity, speed, tags=[]):
        super().__init__(tags=tags)
        self.collider.position.set_position(position=position)
        self.velocity = Vector2(vector=normal_velocity)
        self.velocity.mult(scalar=speed)

    def update_position(self, delta_time=1):
        # update position with an optional time delta (ooh fancy)
        # yay real(ish) physics
        self.collider.position.move_position(delta_x=self.velocity.x*delta_time, delta_y=self.velocity.y*delta_time)

    # not adding a special collision checking function because there's already a helper
    # really this is just a glorified object tbh

# a weaponized object basically is just a normal object with guns attached
# you know what i mean. it has things that shoot bullets
# oh yeah these can be loaded from configs!
# you'll want to handle shooting these in another place
class WeaponizedObject(InteractiveObject):
    def __init__(self, tags=[], barrels=[], position=None):
        super().__init__(tags=tags)
        
        self.barrels = barrels
        self.tags = tags

        if position != None:
            self.collider.position = position
        
        self.update_barrels()

    def update_barrels(self):
        # just spam this function lol
        # go through and update barrels, like move them back to the right relative position and things
        for barrel in self.barrels:
            barrel.update_position_parent(self.collider.position.v)

    def load_barrels(self, barrel_configuration_filename):
        # load in barrels from a configuration file
        with open(barrel_configuration_filename, 'r') as f:
            barrel_data = json.load(f)

            self.tags = barrel_data["tags"]
            
            self.barrels = []
            for barrel in barrel_data["barrels"]:
                b = ShootingObject(self.tags, barrel["speed"])
                b.relative_position = Position(Vector2(
                    barrel["x"],
                    barrel["y"]
                ))
                self.barrels.append(b)
            
            self.update_barrels()