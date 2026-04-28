import bpy
import os

def pearl_(filepath):
    obj_a3 = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj_a3
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[0].select = True
    obj_a3.data.vertices[3].select = True
    obj_a3.data.vertices[4].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[0].select = True
    obj_a3.data.vertices[4].select = True
    obj_a3.data.vertices[2].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[6].select = True
    obj_a3.data.vertices[8].select = True
    obj_a3.data.vertices[10].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[6].select = True
    obj_a3.data.vertices[9].select = True
    obj_a3.data.vertices[10].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[12].select = True
    obj_a3.data.vertices[14].select = True
    obj_a3.data.vertices[16].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[12].select = True
    obj_a3.data.vertices[16].select = True
    obj_a3.data.vertices[15].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1222].select = True
    obj_a3.data.vertices[1277].select = True
    obj_a3.data.vertices[1221].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1076].select = True
    obj_a3.data.vertices[1074].select = True
    obj_a3.data.vertices[1079].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1076].select = True
    obj_a3.data.vertices[1079].select = True
    obj_a3.data.vertices[1078].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1076].select = True
    obj_a3.data.vertices[1078].select = True
    obj_a3.data.vertices[1747].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1078].select = True
    obj_a3.data.vertices[1752].select = True
    obj_a3.data.vertices[1747].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1074].select = True
    obj_a3.data.vertices[1079].select = True
    obj_a3.data.vertices[1069].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1078].select = True
    obj_a3.data.vertices[636].select = True
    obj_a3.data.vertices[1079].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1277].select = True
    obj_a3.data.vertices[1221].select = True
    obj_a3.data.vertices[1279].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1219].select = True
    obj_a3.data.vertices[1221].select = True
    obj_a3.data.vertices[1279].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1055].select = True
    obj_a3.data.vertices[1044].select = True
    obj_a3.data.vertices[1053].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1042].select = True
    obj_a3.data.vertices[1044].select = True
    obj_a3.data.vertices[1053].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1069].select = True
    obj_a3.data.vertices[1079].select = True
    obj_a3.data.vertices[1118].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode='OBJECT')
    obj_a3.data.vertices[1078].select = True
    obj_a3.data.vertices[636].select = True
    obj_a3.data.vertices[634].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
