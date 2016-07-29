'''
Change object materials to toon shaders.
'''

import bpy

for material in bpy.data.materials:
    # Changes current object material to 'toon'.
    material.diffuse_shader = 'TOON'
    material.diffuse_toon_size = 1.3
    material.diffuse_toon_smooth = 0.020354
    print(material.diffuse_toon_size) # - Outputs to the blender console, opens auto in mac...
    
print('Hello World');