from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio

def truncate_cstr(s: bytes) -> bytes:
    index = s.find(0)
    if index == -1: return s
    return s[:index]
def fetch_cstr(f: 'filelike') -> bytearray:
    build = bytearray()
    while 1:
        strbyte = f.read(1)
        if strbyte == b'\0' or not strbyte: break
        build += strbyte
    return build

def GHG_mesh(f, filepath):

    idx1=0
    idx1_=0

    vertices2=[]
    vertices2_=[]
    faces2=[]
    
    vertices2pt2=[]
    faces2pt2=[]

    fa1=-3
    fb1=-2
    fc1=-1
    
    fa1pt2=-4
    fb1pt2=-3
    fc1pt2=-2
    fd1pt2=-1
    
    f.seek(0)
    Chunks = f.read()
    f.seek(0)

    while f.tell() < len(Chunks):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            VertexCount = unpack("B", f.read(1))[0]//2
            flag01 = unpack("B", f.read(1))[0]
            if flag01 == 0x6D:
                if VertexCount == 0:
                    pass
                elif VertexCount == 1:
                    pass
                elif VertexCount == 2:
                    pass
                elif VertexCount == 3:
                    for i in range(VertexCount):
                        vx = unpack("<h", f.read(2))[0] / 4096
                        vy = unpack("<h", f.read(2))[0] / 4096
                        vz = unpack("<h", f.read(2))[0] / 4096
                        fn = unpack("<h", f.read(2))[0] / 4096
                        ux = unpack("<h", f.read(2))[0] / 4096
                        uy = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2.append([vx,vz,vy])
                    f.seek(78,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag1 = unpack("B", f.read(1))[0]
                    if flag1 == 0x6E:
                        fa1= unpack("B", f.read(1))[0] & 0x0F
                        fb1= unpack("B", f.read(1))[0] & 0x0F
                        fc1= unpack("B", f.read(1))[0] & 0x0F
                        fa1//=3
                        fb1//=3
                        fc1//=3
                        fa1+=1*len(vertices2)-3
                        fb1+=1*len(vertices2)-3
                        fc1+=1*len(vertices2)-3
                        faces2.append([fa1,fb1,fc1])
                        
                    for i in range(VertexCount):
                        f.seek(-16,1)
                    f.seek(-78,1)
                    f.seek(-2,1)
                    f.seek(-3,1)
                    for i in range(VertexCount):
                        vx1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fa1
                        vy1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fb1
                        vz1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fc1
                        fn1 = unpack("<h", f.read(2))[0] / 4096
                        ux1 = unpack("<h", f.read(2))[0] / 4096
                        uy1 = unpack("<h", f.read(2))[0] / 4096
                        vx2 = vx1
                        vy2 = vy1
                        vz2 = vz1
                        f.seek(4,1)
                        fa1+=1*3
                        fb1+=1*3
                        fc1+=1*3
                        idx1+=1
                        
                        if idx1 == 1:
                            vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))
                            
                        elif idx1 == 2:
                            vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))
                        elif idx1 == 3:
                            vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))
                            
                            
                        
                        
                        

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2.from_pydata(vertices2_, [], [])
    object2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(object2)
    
    obj_a3 = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    
    if vertices2_[0:3] == [{-0.031, 1.965, 3.031}, {2.971, 4.963, 6.033}, {9.035, 5.974, 7.955}]:
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
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.editmode_toggle()
