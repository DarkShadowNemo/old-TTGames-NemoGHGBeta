from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio

def LegoStarWarsghgTo3dsBeta_(f, filepath):
    
    vertices=[]
    faces=[]
    vertices2=[]
    faces2=[]
    fa=-3
    fb=-2
    fc=-1
    fa1=-3
    fb1=-2
    fc1=-1
    idx1=0
    
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
                elif vertexcount == 3:
                    vertexcount1-=1
                if vertexcount1 == 2:
                    for j in range(vertexcount):
                        vx1 = unpack("<h", f.read(2))[0]/4096
                        vy1 = unpack("<h", f.read(2))[0]/4096
                        vz1 = unpack("<h", f.read(2))[0]/4096
                        fnz1 = unpack("<h", f.read(2))[0]/4096
                        uvx1 = unpack("<h", f.read(2))[0]/4096
                        uvy1 = unpack("<h", f.read(2))[0]/4096
                        f.seek(4,1)
                        vertices2.append([vx1,vz1,vy1])
                    for i in range(vertexcount-2):
                        fa1+=1*3
                        fb1+=1*3
                        fc1+=1*3
                        faces2.append([fa1,fb1,fc1])
                elif vertexcount1 == 3:
                    for j in range(vertexcount1):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        fnz = unpack("<h", f.read(2))[0]/4096
                        uvx = unpack("<h", f.read(2))[0]/4096
                        uvy = unpack("<h", f.read(2))[0]/4096
                        f.seek(4,1)
                        vertices.append([vx,vz,vy])
                    for i in range(vertexcount1-2):
                        fa+=1*3
                        fb+=1*3
                        fc+=1*3
                        faces.append([fa,fb,fc])
                    
        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2.from_pydata(vertices2, [], faces2)
    objects2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(objects2)

