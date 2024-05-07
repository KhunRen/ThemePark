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
        top_cone = basic.Cone(name="top_cone", coords=(0, 0, 36.8413 ))
        top_cone.scale((30, 30, 5.28961))
        modifier.wireframe(top_cone.object, 0.024, 1, False)
        
        seat = basic.Torus(name="seat", coords=(0, 0, 19.7393))
        seat.scale((23.6526, 23.6526, 2.09852))
        
        back_rest = basic.Cylinder(name="back_rest", coords=(0, 0, 22.1694 ))
        back_rest.scale((29.0064, 29.0064, 2.09852))
        modifier.wireframe(back_rest.object, 0.02)
        modifier.subdivision_surface(back_rest.object, 1)
        
        fence = basic.Cylinder(name="fence", coords=(0, 0, 27.85))
        fence.scale((29.0064,29.0064,3.58164))
        modifier.wireframe(fence.object, 0.02)
        
        
        utility.parent_objects(seat.object,back_rest.object)
        utility.parent_objects(seat.object,fence.object)
        utility.parent_objects(seat.object,top_cone.object)
        
        
        self.mainObject = seat.object
        self.allObjects = {
            "top_cone": top_cone.object,
            "seat": seat.object,
            "back_rest": back_rest.object,
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
                self.allObjects["seat"].rotation_euler[1] = math.radians(-7.08689 * (i / (total_frames / 2)))
            else:
                # Bagian 2 (frame 251 - 500)
                self.allObjects["seat"].rotation_euler[1] = math.radians(-7.08689 * (1 - (i - total_frames / 2) / (total_frames / 2)))
            
            # Rotasi terhadap sumbu Z
            self.allObjects["seat"].rotation_euler[2] = math.radians(20 * i)
            
            # Menyisipkan keyframe untuk rotasi objek "seat"
            self.allObjects["seat"].keyframe_insert(data_path="rotation_euler", frame=i)
        
        
        