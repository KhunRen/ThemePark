
import bpy
import os
import sys
from importlib import reload


dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 500
bpy.context.scene.frame_set(1)

import builder
reload(builder)
