from struct import pack, unpack
import os
import bpy
import mathutils
import math

def GHG_whole_entire_model2(f, vertices2=[], faces2=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices2.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces2.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices2, [], faces2)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_model1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            if len(faces) == 156:
                if faces.remove([104,105,106]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                elif faces.remove([51,52,53]):
                    pass
                elif faces.remove([50,51,52]):
                    pass
                elif faces.remove([20,21,22]):
                    pass
                elif faces.remove([19,20,21]):
                    pass
                elif faces.remove([135,136,137]):
                    pass
                elif faces.remove([134,135,136]):
                    pass
                elif faces.remove([73,74,75]):
                    pass
                elif faces.remove([114,115,116]):
                    pass
                elif faces.remove([145,146,147]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([113,114,115]):
                    pass
                elif faces.remove([144,145,146]):
                    pass
                elif faces.remove([30,31,32]):
                    pass
                elif faces.remove([29,30,31]):
                    pass
                elif faces.remove([83,84,85]):
                    pass
                elif faces.remove([61,62,63]):
                    pass
                elif faces.remove([60,61,62]):
                    pass
                elif faces.remove([82,83,84]):
                    pass
                
            

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def GHG_whole_model3(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x04\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

    



def NonParseGHG(filepath, GHG_Meshes=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes == 1:
            if os.path.basename(filepath) == "ray.ghg":
                GHG_whole_entire_model1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
        if GHG_Meshes == 2:
            if os.path.basename(filepath) == "ray.ghg":
                GHG_whole_entire_model2(f, vertices2=[], faces2=[], fa=-1, fb=0, fc=1)

        if GHG_Meshes == 3:
            if os.path.basename(filepath) == "ray.ghg":
                GHG_whole_entire_model3(f, vertices2=[], faces2=[], fa=-1, fb=0, fc=1)
            
                
        
                
        
        
        
