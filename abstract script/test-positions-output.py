import bpy
import random
import mathutils

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

def calcThisBeginning(lastPositions, twoAgoPositions):
    "Process vectors"
    """
    if twoAgoPositions == None:
        "This is needed as a constraint for the spacer & direction"
    else:
    
        endPointCoords "Get coords of end point"
        """
    spacerPositions = calcSpacer(lastPositions)
    print("break")
    for i in range (0, 4):
        spacerPositions[i] = spacerPositions[i] + mathutils.Vector((1, 1, 1))
        print(spacerPositions[i])
        
        
    return
    
def calcSpacer(lastPositions):
    print("Break")
    spacerDirections = calcDirection()
    print(spacerDirections)
    print("Break")
    spacerPositions = []
    for i in range(8, 12):
        position0 = lastPositions[i][0] + spacerDirections[0]
        position1 = lastPositions[i][1] + spacerDirections[1]
        position2 = lastPositions[i][2] + spacerDirections[2]
    
        spacerPositions.append(mathutils.Vector((position0, position1, position2)))
        print(spacerPositions[i-8])
    return spacerPositions
    
def calcDirection():
    xDirection = random.uniform(-1, 1)
    yDirection = random.uniform(-1, 1)
    directions = mathutils.Vector((xDirection, yDirection, 0))
    return directions  
    
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
    
    
    
coordinates = createFirstShape(INIT_LOCATION)
lastPositions = getPositions()

for item in bpy.data.objects:  
      
    print(item.name)  
    if item.type == 'MESH':  
        for vertex in item.data.vertices:  
            print(vertex.co)
            temp = vertex.co
            "print(temp[0])"
            

calcThisBeginning(lastPositions, None)            