from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio
from .pearl import *

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
    vertices2pt2=[]
    vertices2_=[]
    faces2=[]
    
    vertices2pt2=[]
    faces2pt2=[]

    fa1=-3
    fb1=-2
    fc1=-1
    
    fa1_=-4
    fb1_=-3
    fc1_=-2
    
    fa1pt2=-4
    fb1pt2=-3
    fc1pt2=-2
    fd1pt2=-1

    FileSize = unpack("<I", f.read(4))[0]
    null1 = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    TextureEntrySize1 = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    MaterialEntrySize1 = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    
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
                    for i in range(VertexCount-2):
                        fa1+=1*3
                        fb1+=1*3
                        fc1+=1*3
                        faces2.append([fa1,fb1,fc1])
                elif VertexCount:
                    for i in range(VertexCount):
                        vx_ = unpack("<h", f.read(2))[0] / 4096
                        vy_ = unpack("<h", f.read(2))[0] / 4096
                        vz_ = unpack("<h", f.read(2))[0] / 4096
                        fn_ = unpack("<h", f.read(2))[0] / 4096
                        ux_ = unpack("<h", f.read(2))[0] / 4096
                        uy_ = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2pt2.append([vx_,vz_,vy_])
                    for i in range(VertexCount):
                        f.seek(-16,1)
                    for i in range(VertexCount):
                        vx1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fa1_
                        vy1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fb1_
                        vz1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fc1_
                        fn1 = unpack("<h", f.read(2))[0] / 4096
                        ux1 = unpack("<h", f.read(2))[0] / 4096
                        uy1 = unpack("<h", f.read(2))[0] / 4096
                        vx2 = vx1
                        vy2 = vy1
                        vz2 = vz1
                        f.seek(4,1)
                        fa1_+=1*4
                        fb1_+=1*4
                        fc1_+=1*4
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
    mesh2.from_pydata(vertices2, [], faces2)
    object2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(object2)
    
    mesh2_ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2_.from_pydata(vertices2pt2, [], [])
    object2_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2_)
    collection.objects.link(object2_)
    
    if vertices2_[0:3] == [{-3.069, -3.962, -2.021}, {0.036, 1.975, 0.944}, {4.036, 5.975, 4.944}]:
        pearl_(filepath)
