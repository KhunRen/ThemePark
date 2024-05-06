import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import bpy
from importlib import reload
import random
reload(basics)

        
class Ombak_banyu(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        # self.horses = []
        # self.plot_horse()
        # self.animate()
        
    def create(self):
        base = basic.Cylinder(name="base", coords=(0, 0, -0.5))
        base.scale((31.1973, 31.1973, 0.79709))
        modifier.subdivision_surface(base.object, 3)
        
        # upper_base = basic.Cylinder(name="upper_base", coords=(0, 0, 1))
        # upper_base.scale((20.2937, 20.2937, 1.07793))
        
        # lower_base = basic.Cylinder(name="lower_base", coords=(0, 0, 0.413442))
        # lower_base.scale((22.3037, 22.3037, 0.507933))
        
        
        # center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 14.5379))
        # center_pole.scale((5, 5, 13.79))
        
        # top_part = basic.Cone(name="top_part", coords=(0, 0, 35.9213 ))
        # top_part.scale((26.3782, 26.3782, 8.64961))
        # modifier.wireframe(top_part.object, 0.024, 1, False)
        
        # top_part_holder = basic.Torus(name="top_part_holder", coords=(0, 0, 19.3793))
        # top_part_holder.scale((23.6526, 23.6526, 7.92263))
        
        # top_banner = basic.Torus(name="top_banner", coords=(0, 0, 27.1721 ))
        # top_banner.scale((23.8237,23.8237,23.8237))
        
        # top_wire = basic.Cylinder(name="top_wire", coords=(0, 0, 22.1694 ))
        # top_wire.scale((29.0064, 29.0064, 2.09852))
        # modifier.wireframe(top_wire.object, 0.02)
        # modifier.subdivision_surface(top_wire.object, 1)
        
        # fence = basic.Cylinder(name="fence", coords=(0, 0, 1.15))
        # fence.scale((27.3717,27.3717,1.47164))
        # modifier.wireframe(fence.object, 0.02)
        
        # top_closer = basic.Cylinder(name="top_closer", coords=(0, 0, 23.7899))
        # top_closer.scale((20.2084, 20.2084, 1.22842))
        
        # for i in range(0, 3):
        #     pole_decor = basic.Cylinder(name=f"pole_decor{i}", coords=(0, 0, 20.0281- (7*i)))
        #     pole_decor.scale((6.50674, 6.50674, 2.75145))
        #     modifier.wireframe(pole_decor.object, 0.051,0,False)
        #     utility.parent_objects(center_pole.object, pole_decor.object)
        
        # top_ornament = basic.Cylinder(name="top_ornament", coords=(0, 0, 25.1319))
        # top_ornament.scale((23.8683,23.8683,8.4359))
        # modifier.wireframe(top_ornament.object, 0.02)
        # modifier.subdivision_surface(top_ornament.object, 1)
        # modifier.displace(top_ornament.object, 1, 0.959)
        # modifier.cast(top_ornament.object,-0.86)
        
        # utility.parent_objects(base.object,top_ornament.object)
        # utility.parent_objects(base.object, upper_base.object)
        # utility.parent_objects(base.object, lower_base.object)
        # utility.parent_objects(base.object, center_pole.object)
        # utility.parent_objects(base.object, top_part.object)
        # utility.parent_objects(base.object, top_part_holder.object)
        # utility.parent_objects(base.object, top_banner.object)
        # utility.parent_objects(base.object, top_wire.object)
        # utility.parent_objects(base.object, fence.object)
        # utility.parent_objects(base.object, top_closer.object)
        
        # self.mainObject = base.object
        # self.allObjects = {
        #     "upper_base": upper_base.object,
        #     "lower_base": lower_base.object,
        #     "center_pole": center_pole.object,
        #     "top_part": top_part.object,
        #     "top_part_holder": top_part_holder.object,
        #     "top_banner": top_banner.object,
        #     "top_wire": top_wire.object,
        #     "fence": fence.object
        # }
    # def plot_horse(self):
    #     for i in range(0, 360, 45):
    #         x = 15 * math.cos(math.radians(i))
    #         y = 15 * math.sin(math.radians(i))
    #         height = 16
    #         if i % 90 == 0:
    #             height = 19
            
    #         random_num = random.randint(0, 1)
    #         horse = None
    #         # horse = Horse("horse", (x, y, height))
            
    #         if random_num == 1:
    #             horse = Bench("bench", (x, y, height))
    #         else:
    #             horse = Horse("horse", (x, y, height))
                
    #         horse.rotate((0, 0, i+90))
    #         utility.parent_objects(self.allObjects["center_pole"], horse.mainObject)
    #         self.horses.append(horse)
            
    # def animate(self):
    #     end_frame = bpy.context.scene.frame_end
    #     for i in range(1, end_frame+1):
    #         self.allObjects["center_pole"].rotation_euler[2] = math.radians(i/2)
    #         self.allObjects["center_pole"].keyframe_insert(data_path="rotation_euler", frame=i)
    #         for horse in self.horses:
    #             movement = 0.007
    #             if self.horses.index(horse) % 2 == 0:
    #                 movement = -0.007
    #             if i % 100 <= 50:
    #                 horse.mainObject.location.z += movement
    #             else:
    #                 horse.mainObject.location.z -= movement
                
    #             horse.mainObject.keyframe_insert(data_path="location", frame=i)
        
        
        
        