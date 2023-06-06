from struct import pack, unpack
import os
import bpy
import mathutils
import math


#WHAT THE UVS ARE GOING STRANGE PATTERNS WITH BYTES???
#need help on this
def GHG_seek_uvs_tri(f, seek_=0, uvs=[]):
    obdata = bpy.context.object.data
    f.seek(seek_,1)
    uvcount = unpack("B", f.read(1))[0]
    f.seek(1,1)
    for i in range(int(uvcount*2)):
        uvx = unpack("B", f.read(1))[0] / 255.0
        uvy = unpack("B", f.read(1))[0] / 255.0
        uvs.append([uvx,uvy])
    uv_tex = obdata.uv_layers.new()
    uv_layer = obdata.uv_layers[0].data
    vert_loops = {}
    for l in obdata.loops:
        vert_loops.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs):
        for li in vert_loops[i]:
            uv_layer[li].uv = coord

def GHG_seek_indivitual_triangles(f, seek_= 0, normals=[], vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(seek_,1)
    vertexCount = unpack("B", f.read(1))[0]
    f.seek(1,1)
    for i in range(vertexCount//2):
        vx = unpack("<h", f.read(2))[0] / 4096.0
        vy = unpack("<h", f.read(2))[0] / 4096.0
        vz = unpack("<h", f.read(2))[0] / 4096.0
        nz = unpack("<h", f.read(2))[0] / 4096.0
        f.seek(8,1)
        vertices.append([vx,vy,vz])
        normals.append([0,0,1])
    for i in range(vertexCount//2-2):
        #faces = ([i+i%2],[i-i%2+1],[i+2])
        fa += 1
        fb += 1
        fc += 1
        faces.append([fa,fb,fc])
            
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials.new(name="dragonjan_materials")
            
    for fac in mesh.polygons:
        fac.use_smooth = True

    vindex = 0
    for vertex in mesh.vertices:
        vertex.normal = normals[vindex]
        vindex += 1

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
                



def NonParseGHG(filepath, GHG_Meshes=False, GHG_MESH_SEP=1, seek__=0, seek_uv=0, GHG_MESH_SEP_UV=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes:
            GHG_read(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1, bones=[])
        if GHG_MESH_SEP == 2:
            GHG_seek_indivitual_triangles(f, seek_= seek__, normals=[], vertices=[], faces=[], fa=-1, fb=0, fc=1)
        if GHG_MESH_SEP_UV == 2:
            GHG_seek_uvs_tri(f, seek_=seek_uv, uvs=[])
                
        
                
        
        
        
