from struct import pack, unpack
import os
import bpy
import mathutils
import math

def align_roll( vec, vecz, tarz ):

    sine_roll = vec.normalized().dot(vecz.normalized().cross(tarz.normalized()))

    if 1 < abs(sine_roll):
        sine_roll /= abs(sine_roll)
            
    if 0 < vecz.dot( tarz ):
        return math.asin( sine_roll )
        
    elif 0 < sine_roll:
        return -math.asin( sine_roll ) + math.pi
        
    else:
        return -math.asin( sine_roll ) - math.pi

def GHG_read(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1, bones=[]):
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
        matrix_ = mathutils.Matrix().transposed()
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
            for i in range(vertexCount-2):
                fa +=1
                fb +=1
                fc +=1
                faces.append([fa,fb,fc])
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount//2):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount//2-2):
                fa +=1
                fb +=1
                fc +=1
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
                vxn = unpack("<f", f.read(4))[0]
                vyn = unpack("<f", f.read(4))[0]
                vzn = unpack("<f", f.read(4))[0]
                nzx = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
            for i in range(vertexCount//2-2):
                fa +=1
                fb +=1
                fc +=1
                faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
                



def NonParseGHG(filepath, GHG_Meshes=False, GHG_MESH_SEP=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes:
            GHG_read(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1, bones=[])
        if GHG_MESH_SEP == 2:
            GHG_seperate_readInt_two(f, vertices=[], faces=[], normals=[])
                
        
                
        
        
        
