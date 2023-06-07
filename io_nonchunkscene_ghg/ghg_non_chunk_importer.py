from struct import pack, unpack
import os
import bpy
import mathutils
import math

def read_att(f, vertices=[], faces=[], fa=-1, fb=0, fc=1, normals=[], bones=[]):
    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')
    f.seek(24,1)
    BoneCount = unpack("<I", f.read(4))[0]
    f.seek(4,1)
    BoneEndSizeData = unpack("<I", f.read(4))[0]
    f.seek(BoneEndSizeData-36,1)
    for i in range(BoneCount):
        f.seek(112,1)
        bonex = unpack("<f", f.read(4))[0]
        boney = unpack("<f", f.read(4))[0]
        bonez = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        
        bones.append([bonex,boney,bonez])
        bone = skel.edit_bones.new("ghg bone")
        #todo clean bones and align roll
        bone.head = (
            +bonex,
            +boney,
	    +bonez,
            )
        bone.tail = (
            bone.head[0],
            bone.head[1],
            bone.head[2] + 0.03,
        )
    bpy.ops.object.mode_set(mode = 'OBJECT')
    f.seek(0)
    
        
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            clump = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
                normals.append([0,0,1])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]//2
            clump = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                normals.append([0,0,1])
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
                
        elif Chunk == b"\x04\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            clump = unpack("B", f.read(1))[0]
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
                normals.append([0,0,1])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
    

                



def NonParseGHG(filepath, LEGO_STAR_WARS=1, HAVEN_CALL_OF_THE_KING=1, CRASH_BANDICOOT_THE_WRATH_OF_CORTEX=1, FINDING_NEMO=1, CUSTOM_=1):
    with open(filepath, "rb") as f:
        if LEGO_STAR_WARS == 1:
            read_att(f, vertices=[], faces=[], fa=-1, fb=0, fc=1, normals=[], bones=[])
        if HAVEN_CALL_OF_THE_KING == 1:
            pass
        if CRASH_BANDICOOT_THE_WRATH_OF_CORTEX == 1:
            pass
        if FINDING_NEMO == 1:
            pass
        if CUSTOM_ == 1:
            pass
                
        
                
        
        
        
