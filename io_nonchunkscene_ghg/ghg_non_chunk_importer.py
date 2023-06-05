from struct import pack, unpack
import os
import bpy
import mathutils
import math

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
            #Finding Nemo
            if vertices == 124:
                #key
                #if this requires the same it requires or and and condition
                if faces.remove([46,47,48]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([73,74,75]):
                    pass
                elif faces.remove([42,43,44]):
                    pass
                elif faces.remove([43,44,45]):
                    pass
                elif faces.remove([47,48,49]):
                    pass
                elif faces.remove([107,108,109]):
                    pass
                elif faces.remove([106,107,108]):
                    pass
                elif faces.remove([114,115,116]):
                    pass
                elif faces.remove([110,111,112]):
                    pass
                elif faces.remove([111,112,113]):
                    pass
                elif faces.remove([115,116,117]):
                    pass
                elif faces.remove([25,26,27]):
                    pass
                elif faces.remove([24,25,26]):
                    pass
                elif faces.remove([99,100,101]):
                    pass
                elif faces.remove([98,99,100]):
                    pass
                elif faces.remove([67,68,69]):
                    pass
                elif faces.remove([66,67,68]):
                    pass
                elif faces.remove([92,93,94]):
                    pass
                elif faces.remove([93,94,95]):
                    pass
                elif faces.remove([19,20,21]):
                    pass
                elif faces.remove([18,19,20]):
                    pass
                elif faces.append([120,121,122]):
                    pass
                elif faces.append([121,122,123]):
                    pass
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
                
        
                
        
        
        
