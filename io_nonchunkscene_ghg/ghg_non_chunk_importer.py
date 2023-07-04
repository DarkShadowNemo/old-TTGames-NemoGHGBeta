from struct import pack, unpack
import os
import bpy
import mathutils
import math

def GHG_whole_entire_model_0x030200010380066D(f, vertices=[], faces=[], fa=-3,fb=-2,fc=-1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            if vertexCount == 6:
                for i in range(vertexCount//2):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount//2-2):
                    fa+=1*3
                    fb+=1*3
                    fc+=1*3
                    faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_model_0x030200010380086D(f, vertices=[], faces=[], fa=-3,fb=-2,fc=-1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            if vertexCount == 8:
                for i in range(vertexCount//2):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount//8):
                    fa+=1*4
                    fb+=1*4
                    fc+=1*4
                    faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_model_0x0302000103800A6D(f, vertices=[], faces=[], fa=-3,fb=-2,fc=-1):
    pass
    
    

                



def NonParseGHG(filepath):
    with open(filepath, "rb") as f:
        pass
            
                
        
                
        
        
        
