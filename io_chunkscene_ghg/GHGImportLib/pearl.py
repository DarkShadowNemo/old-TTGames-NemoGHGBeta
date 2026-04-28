import bpy
import os

def pearl_(filepath):
    obj_a3 = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj_a3
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[0].select = True
    obj_a3.data.vertices[0].co.x = 1370/4096
    obj_a3.data.vertices[0].co.z = -1526/4096
    obj_a3.data.vertices[0].co.y = -1193/4096
    obj_a3.data.vertices[1].select = True
    obj_a3.data.vertices[1].co.x = 1432/4096
    obj_a3.data.vertices[1].co.z = -1846/4096
    obj_a3.data.vertices[1].co.y = -1078/4096
    obj_a3.data.vertices[2].select = True
    obj_a3.data.vertices[2].co.x = 1282/4096
    obj_a3.data.vertices[2].co.z = -1449/4096
    obj_a3.data.vertices[2].co.y = -1282/4096
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
