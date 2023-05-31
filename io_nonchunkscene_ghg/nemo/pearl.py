from struct import pack, unpack
import os
import bpy
import mathutils
import bmesh

"""def CleanGHGNemoBonesWIP(f, bones=[]):

    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')
    
    FileSize = unpack("<I", f.read(4))[0]
    unk01 = unpack("<I", f.read(4))[0]
    textureCount = unpack("<I", f.read(4))[0]
    textureStartSize = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    MaterialStartSize = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    BoneParentSize = unpack("<I", f.read(4))[0]
    BoneMatrixSize = unpack("<I", f.read(4))[0]
    f.seek(BoneMatrixSize-36, 1)
    for i in range(BoneCount):
        f.seek(48,1)
        mposx = unpack("<f", f.read(4))[0]
        mposy = unpack("<f", f.read(4))[0]
        mposz = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        bones.append([mposx, mposy, mposz])
            

        bone = skel.edit_bones.new("GHG Bones")
            
        bone.head = ([
            +mposx,
            +mposy,
            +mposz,
            ])
            
        bone.tail = ([
            bone.head[0] + 0.03,
            bone.head[1],
            bone.head[2],
            ])
    bpy.ops.object.mode_set(mode = 'OBJECT')"""

def WholeMeshGHGPearlOne(f, vertices=[], uvs=[],normals=[], fa=-1,fb=0,fc=1):
    chunkSize = 0
    QT = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(QT)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            decmimal = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx,vy,vz])
                normals.append([0,0,nz])
            if len(vertices) == 2165:
                #Pearl
                faces = [[1123,1124,1125]]
            
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
    """vindex = 0
    for vertex in mesh.vertices:
        vertex.normal = normals[vindex]
        vindex += 1"""
                
        
                
        
        
        
