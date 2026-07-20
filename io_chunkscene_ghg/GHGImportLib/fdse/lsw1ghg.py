from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio

def LegoStarWarsghgTo3dsBeta_(f):
    
    vertices=[]
    f.seek(0)
    chunks = f.read()
    f.seek(0)
    while f.tell() < len(chunks):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0]//2
            flag1 = unpack("B", f.read(1))[0]
            if flag1 == 109:
                vertexcount1 = vertexcount
                if vertexcount > 3:
                    vertexcount1-=1
                for jjj in range(vertexcount1):
                    vx = unpack("<h", f.read(2))[0]/4096
                    vy = unpack("<h", f.read(2))[0]/4096
                    vz = unpack("<h", f.read(2))[0]/4096
                    fnz = unpack("<h", f.read(2))[0]/4096
                    uvx = unpack("<h", f.read(2))[0]/4096
                    uvy = unpack("<h", f.read(2))[0]/4096
                    f.seek(4,1)
                    vertices.append([vx,vz,vy])
        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], [])
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
