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
        
class OmbakBanyu_Atas(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        self.animate()
        
    def create(self):
        base = basic.Cylinder(name="base", coords=(0, 0, -0.5))
        base.scale((31.1973, 31.1973, 0.79709))
        modifier.subdivision_surface(base.object, 3)
        
        top_part = basic.Cone(name="top_part", coords=(0, 0, 36.8413 ))
        top_part.scale((30, 30, 5.28961))
        modifier.wireframe(top_part.object, 0.024, 1, False)
        
        top_part_holder = basic.Torus(name="top_part_holder", coords=(0, 0, 19.7393))
        top_part_holder.scale((23.6526, 23.6526, 2.09852))
        
        top_wire = basic.Cylinder(name="top_wire", coords=(0, 0, 22.1694 ))
        top_wire.scale((29.0064, 29.0064, 2.09852))
        modifier.wireframe(top_wire.object, 0.02)
        modifier.subdivision_surface(top_wire.object, 1)
        
        fence = basic.Cylinder(name="fence", coords=(0, 0, 27.85))
        fence.scale((29.0064,29.0064,3.58164))
        modifier.wireframe(fence.object, 0.02)
        
        
        utility.parent_objects(top_part_holder.object,top_wire.object)
        utility.parent_objects(top_part_holder.object,fence.object)
        utility.parent_objects(top_part_holder.object,top_part.object)
        
        
        self.mainObject = base.object
        self.allObjects = {
            "top_part": top_part.object,
            "top_part_holder": top_part_holder.object,
            "top_wire": top_wire.object,
            "fence": fence.object
        }
            
    def animate(self):
        # Mendapatkan jumlah frame pada animasi
        total_frames = 500
        
        # Pembagian frame menjadi 2 bagian
        for i in range(1, total_frames + 1):
            # Rotasi terhadap sumbu Y
            if i <= total_frames / 2:
                # Bagian 1 (frame 1 - 250)
                self.allObjects["top_part_holder"].rotation_euler[1] = math.radians(-7.08689 * (i / (total_frames / 2)))
            else:
                # Bagian 2 (frame 251 - 500)
                self.allObjects["top_part_holder"].rotation_euler[1] = math.radians(-7.08689 * (1 - (i - total_frames / 2) / (total_frames / 2)))
            
            # Rotasi terhadap sumbu Z
            self.allObjects["top_part_holder"].rotation_euler[2] = math.radians(20 * i)
            
            # Menyisipkan keyframe untuk rotasi objek "top_part_holder"
            self.allObjects["top_part_holder"].keyframe_insert(data_path="rotation_euler", frame=i)
        
        
        