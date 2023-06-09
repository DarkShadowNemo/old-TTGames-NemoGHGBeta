from struct import pack, unpack
import os
import bpy
import mathutils
import math

def GHG_Weights():
    pass

def GHG_Bones(f, bones=[]):
    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')
    f.seek(0)
    FileSize = unpack("<I", f.read(4))[0]
    unk = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    TextureEntrySize1 = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    MaterialEntrySize1 = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    BoneEntrySize1 = unpack("<I", f.read(4))[0]
    BoneEntrySize2 = unpack("<I", f.read(4))[0]
    f.seek(BoneEntrySize2-36,1)
    for i in range(BoneCount):
        f.seek(112,1)
        BonePosX = unpack("<f", f.read(4))[0]
        BonePosY = unpack("<f", f.read(4))[0]
        BonePosZ = unpack("<f", f.read(4))[0]
        unk = unpack("<f", f.read(4))[0]

        bone = skel.edit_bones.new("0")
        bone.head = (
            +BonePosX,
            +BonePosY,
            +BonePosZ,
            )
        bone.tail = (
            bone.head[0] + 0.03,
            bone.head[1],
	    bone.head[2],
            )
    bpy.ops.object.mode_set(mode = 'OBJECT')

def GHG_whole_entire_model(f, vertices=[], faces=[], fa=-1,fb=0,fc=1):
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
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif Chunk == b"\x04\02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

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
    

                



def NonParseGHG(filepath, whole_entire_GHGMesh=False, GHG_Bone_data=False, offset_1=False, seek_=0, offset_2=False, seek__=0, offset_3=False, seek___=0):
    with open(filepath, "rb") as f:
        if offset_1:
            read_GHG_mesh_1(f, seek1=seek_, vertices=[], faces=[])
        if offset_2:
            read_GHG_mesh_2(f, seek2=seek__, vertices=[], faces=[])
        if offset_3:
            read_GHG_mesh_3(f, seek3=seek___, vertices=[], faces=[])
        if whole_entire_GHGMesh:
            GHG_whole_entire_model(f, vertices=[], faces=[], fa=-1,fb=0,fc=1)
        if GHG_Bone_data:
            GHG_Bones(f, bones=[])
                
        
                
        
        
        
