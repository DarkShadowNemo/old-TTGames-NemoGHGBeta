from struct import pack, unpack
import os
import bpy
import mathutils
import math

def GHG_read(f, vertices=[], edges=[], normals=[], ea=-1, eb=0, bones=[]):
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
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            clump = unpack("B", f.read(1))[0]
            for i in range(vertexCount//2):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount//2-2):
                ea +=1
                eb +=1
                edges.append([ea,eb])
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
                ea +=1
                eb +=1
                edges.append([ea,eb])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, edges, [])
    bpy.context.collection.objects.link(object)
                



def NonParseGHG(filepath, GHG_Meshes=False, GHG_MESH_SEP=1, seek__=0, seek_uv=0, GHG_MESH_SEP_UV=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes:
            GHG_read(f, vertices=[], edges=[], normals=[], ea=-1, eb=-0, bones=[])
        if GHG_MESH_SEP == 2:
            GHG_seek_indivitual_triangles(f, seek_= seek__, normals=[], vertices=[], faces=[], fa=-1, fb=0, fc=1)
        if GHG_MESH_SEP_UV == 2:
            GHG_seek_uvs_tri(f, seek_=seek_uv, uvs=[])
                
        
                
        
        
        
