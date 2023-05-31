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

def WholeMeshGHGClamOne(f, vertices=[], faces=[], uvs=[],normals=[], fa=-1,fb=0,fc=1):
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
                f.seek(10,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
            if len(vertices) == 197:
                #Clam
                #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
                if faces.remove([142,143,144]):
                    pass
                elif faces.remove([141,142,143]):
                    pass
                elif faces.remove([176,177,178]):
                    pass
                elif faces.remove([130,131,132]):
                    pass
                elif faces.remove([131,132,133]):
                    pass
                elif faces.remove([180,181,182]):
                    pass
                elif faces.remove([131,132,133]):
                    pass
                elif faces.remove([179,180,181]):
                    pass
                elif faces.remove([131,132,133]):
                    pass
                elif faces.remove([172,173,174]):
                    pass
                elif faces.remove([171,172,173]):
                    pass
                elif faces.remove([170,171,172]):
                    pass
                elif faces.remove([140,141,142]):
                    pass
                elif faces.remove([150,151,152]):
                    pass
                elif faces.remove([151,152,153]):
                    pass
                elif faces.remove([169,170,171]):
                    pass
                elif faces.remove([168,169,170]):
                    pass
                elif faces.remove([115,116,117]):
                    pass
                elif faces.remove([175,176,177]):
                    pass
                elif faces.remove([143,144,145]):
                    pass
                elif faces.remove([62,63,64]):
                    pass
                elif faces.remove([59,60,61]):
                    pass
                elif faces.remove([63,64,65]):
                    pass
                elif faces.remove([164,165,166]):
                    pass
                elif faces.remove([163,164,165]):
                    pass
                elif faces.remove([174,175,176]):
                    pass
                elif faces.remove([94,95,96]):
                    pass
                elif faces.remove([95,96,97]):
                    pass
                elif faces.remove([87,88,89]):
                    pass
                
            
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
    vindex = 0
    for vertex in mesh.vertices:
        vertex.normal = normals[vindex]
        vindex += 1
                
        
                
        
        
        
