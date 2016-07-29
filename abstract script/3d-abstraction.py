import bpy
import random
import mathutils

"""
A library would have been very helpful for some of
the arrays in this script.
"""

"4 is smooth enough, 5 will be perfectly smooth (at 0.25 radius)"
SUBDIV_LEVELS = 4 
PLANE_RADIUS = 0.25
NUM_OBJECTS = 3
INIT_LOCATION = [0, 0, 0]

RANDOM_LENGTHX_K = 0
RANDOM_LENGTHX_L = 1

RANDOM_LENGTHYZ_K = -1
RANDOM_LENGTHYZ_L = 1

RANDOM_WIDTH_K = 1
RANDOM_WIDTH_L = 2

def randomLengthX():
    return random.uniform(RANDOM_LENGTHX_K, RANDOM_LENGTHX_L)
    
def randomLengthYZ():
    return random.uniform(RANDOM_LENGTHYZ_K, RANDOM_LENGTHYZ_L)

def randomWidth():
    return random.uniform(RANDOM_WIDTH_K, RANDOM_WIDTH_L)
    
def getPositions():
    positionsList = []
    
    for item in bpy.data.objects:  
        if item.type == 'MESH':  
            for vertex in item.data.vertices:  
                positionsList.append(vertex.co)
                
    return positionsList
    
def createFirstShape(INIT_LOCATION):
    coordinates = [randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomWidth(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomWidth()]
    
    "Create Plane"
    bpy.ops.mesh.primitive_plane_add(radius=PLANE_RADIUS, view_align=False, enter_editmode=False, location=(INIT_LOCATION[0], INIT_LOCATION[1], INIT_LOCATION[2]), rotation=(0, 1.57, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    
    "Enter editmode"
    bpy.ops.object.editmode_toggle()
    
    "Extrude Plane"
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(coordinates[0], coordinates[1], coordinates[2]), "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(coordinates[3], coordinates[4], coordinates[5]), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    
    "Scale up"
    scaleSize = coordinates[6]
    bpy.ops.transform.resize(value=(scaleSize, scaleSize, scaleSize), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    "Extrude Again"
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(coordinates[7], coordinates[8], coordinates[9]), "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(coordinates[10], coordinates[11], coordinates[12]), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    
    "Scale Again"
    scaleSize = coordinates[13]
    bpy.ops.transform.resize(value=(scaleSize, scaleSize, scaleSize), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    "Exit editmode"
    bpy.ops.object.editmode_toggle()
    
    "Add subsurf modifier"
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = SUBDIV_LEVELS
    bpy.context.object.modifiers["Subsurf"].render_levels = SUBDIV_LEVELS
    
    return coordinates

def calcThisBeginning(lastPositions, twoAgoPositions):
    "Process vectors"
    if twoAgoPositions == None:
        "This is needed as a constraint for the spacer & direction"
    else:
        endPointCoords "Get coords of end point"
        spacerPositions = calcSpacer(lastPositions)
        for i in range (0, 4)
            spacerPositions[i] = spacerPositions[i] + 1
            print(spacerPositions[i])
        
        
    return
    
def calcSpacer(lastPositions):
    spacerDirections = calcDirection()
    spacerPositions = []
    for i in range(8, 12):
        position0 = lastPositions[i][0] + spacerDirections[0]
        position1 = lastPositions[i][1] + spacerDirections[1]
        position2 = lastPositions[i][2] + spacerDirections[2]
    
        spacerPositions.append(mathutils.Vector((position0, position1, position2)))
    return spacerPositions
    
def calcDirection():
    xDirection = random.uniform(-1, 1)
    yDirection = random.uniform(-1, 1)
    directions = mathutils.Vector((xDirection, yDirection, 0))
    return directions  

def calcThisMiddle(lastPositions, twoAgoPositions):
    if twoAgoPositions = None:
    
    else:
    return

def calcTwoAgoEnd(lastPositions, twoAgoPositions):
    if twoAgoPositions = None:
    
    else:
    return TwoAgoEnd
    
def createNextShape(coordinates, twoAgoEnd):
    begCoordinates = calcThisBeginning(lastPositions, twoAgoEnd)
    
    "Create Plane"
    bpy.ops.mesh.primitive_plane_add(radius=PLANE_RADIUS, view_align=False, enter_editmode=False, location=(begCoordinates[0], begCoordinates[1], begCoordinates[2]), rotation=(0, 1.57, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    
    "Enter editmode"
    bpy.ops.object.editmode_toggle()
    
    midCoordinates = calcThisMiddle(coordinates)
    
    "Extrude Plane"
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(coordinates[0], coordinates[1], coordinates[2]), "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(coordinates[3], coordinates[4], coordinates[5]), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    
    "Scale up"
    scaleSize = coordinates[6]
    bpy.ops.transform.resize(value=(scaleSize, scaleSize, scaleSize), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    "Extrude Again"
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(coordinates[7], coordinates[8], coordinates[9]), "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.transform.translate(value=(coordinates[10], coordinates[11], coordinates[12]), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    
    "Scale Again"
    scaleSize = coordinates[13]
    bpy.ops.transform.resize(value=(scaleSize, scaleSize, scaleSize), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    "Exit editmode"
    bpy.ops.object.editmode_toggle()
    
    "Add subsurf modifier"
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = SUBDIV_LEVELS
    bpy.context.object.modifiers["Subsurf"].render_levels = SUBDIV_LEVELS
    
    coordinates2 = [randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomWidth(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomLengthX(), randomLengthYZ(), randomLengthYZ(), randomWidth(), begCoordinates[0], begCoordinates[1], begCoordinates[2]]
    return coordinates2

def calcTwoAgoPositions(coordinates):
    return twoAgoPositions
    
def calcLastPositions(coordinates):
    return lastPositions
    
    
    
def createMaterials():
    """
    Creates materials but doesn't apply them
    to anything. Remove the comments to apply first
    material to active object.
    """
    for i in range(6):
        """ob = bpy.context.object
        me = ob.data"""
        mat = bpy.data.materials.new("Mat_%i" % i)
        def red():
            "r, g, b"
            mat.diffuse_color = 1, 0, 0
        def orange():
            mat.diffuse_color = 1, 0.1, 0
        def yellow():
            mat.diffuse_color = 1, 0.5, 0
        def green():
            mat.diffuse_color = 0, 1, 0
        def blue():
            mat.diffuse_color = 0, 0, 1
        def violet():
            mat.diffuse_color = 0.5, 0, 1
        colors = {0 : red,
                  1 : orange,
                  2 : yellow,
                  3 : green,
                  4 : blue,
                  5 : violet
        }
        colors[i]()
        "me.materials.append(mat)"

"---------------------------------------------------------------------"
"Start the process" 
createMaterials()

"Create first shape and add material"
coordinates = createFirstShape(INIT_LOCATION)
bpy.context.object.active_material = bpy.data.materials["Mat_0"]

twoAgoPositions = None
lastPositions = None

for i in range((NUM_OBJECTS - 1)):
    if i < 1:
        coordinates = createNextShape(coordinates, twoAgoEnd)
        lastPositions = getPositions()
    else:
        "Add the actual two-ago end here"
        coordinates = createNextShape(coordinates, twoAgoEnd)
        twoAgoPositions = lastPositions
        lastPositions = getPositions()
    "TODO: Logic to cycle materials after 5 (back to 1)"
    bpy.context.object.active_material = bpy.data.materials["Mat_%i" % (i + 1)]



        

    
    

