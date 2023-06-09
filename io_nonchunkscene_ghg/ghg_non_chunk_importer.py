from struct import pack, unpack
import os
import bpy
import mathutils
import math

def read_GHG_mesh_1(f, seek1=0, vertices=[], faces=[]):

    f.seek(seek1,1)
        
    for i in range(3):
        vx = unpack("<f", f.read(4))[0]
        vy = unpack("<f", f.read(4))[0]
        vz = unpack("<f", f.read(4))[0]
        nz = unpack("<f", f.read(4))[0]
        vertices.append([vx,vy,vz])
    for i in range(1):
        faces.append([0,1,2])
    

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def read_GHG_mesh_2(f, seek2=0, vertices=[], faces=[]):

    f.seek(seek2,1)
        
    for i in range(3):
        vx = unpack("<h", f.read(2))[0] / 4096.0
        vy = unpack("<h", f.read(2))[0] / 4096.0
        vz = unpack("<h", f.read(2))[0] / 4096.0
        nz = unpack("<h", f.read(2))[0] / 4096.0
        f.seek(8,1)
        vertices.append([vx,vy,vz])
    for i in range(1):
        faces.append([0,1,2])
    

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def read_GHG_mesh_3(f, seek3=0, vertices=[], faces=[]):

    f.seek(seek3,1)
        
    for i in range(3):
        vx = unpack("<f", f.read(4))[0]
        vy = unpack("<f", f.read(4))[0]
        vz = unpack("<f", f.read(4))[0]
        nz = unpack("<f", f.read(4))[0]
        f.seek(16,1)
        vertices.append([vx,vy,vz])
    for i in range(1):
        faces.append([0,1,2])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
    

                



def NonParseGHG(filepath, offset_1=False, seek_=0, offset_2=False, seek__=0, offset_3=False, seek___=0):
    with open(filepath, "rb") as f:
        if offset_1:
            read_GHG_mesh_1(f, seek1=seek_, vertices=[], faces=[])
        if offset_2:
            read_GHG_mesh_2(f, seek2=seek__, vertices=[], faces=[])
        if offset_3:
            read_GHG_mesh_3(f, seek3=seek___, vertices=[], faces=[])
                
        
                
        
        
        
