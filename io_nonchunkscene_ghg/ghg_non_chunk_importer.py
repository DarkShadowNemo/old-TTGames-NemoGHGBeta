from struct import pack, unpack
import os
import bpy
import mathutils
import bmesh

faces=[]

def CleanGHGNemoBonesWIP(f, bones=[]):

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
    bpy.ops.object.mode_set(mode = 'OBJECT')

def WholeMeshGHGOne(f, vertices=[], faces=[], uvs=[],fa=-1,fb=0,fc=1,fa_=-3,fb_=-2,fc_=-1):
    chunkSize = 0
    QT = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(QT)):
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
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            decmimal = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                #ea = unpack("B", f.read(1))[0]
                #eb = unpack("B", f.read(1))[0] // 2 - 1
                f.seek(10,1)
                vertices.append([vx,vy,vz])
            for i in range(vertexCount//3):
                fa_ += len(vertices[int(vx)])
                fb_ += len(vertices[int(vy)])
                fc_ += len(vertices[int(vz)])
                faces.append([fa_,fb_,fc_])
                    
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
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
            if len(vertices) == 595:
                #Anemone
                #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
                if faces.remove([173,174,175]):
                    pass
                elif faces.remove([174,175,176]):
                    pass
                elif faces.remove([244,245,246]):
                    pass
                elif faces.remove([243,244,245]):
                    pass
                elif faces.remove([208,209,210]):
                    pass
                elif faces.remove([209,210,211]):
                    pass
                elif faces.remove([278,279,280]):
                    pass
                elif faces.remove([279,280,281]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                #elif faces.remove([103,104,105]):
                    #pass
                elif faces.remove([104,105,106]):
                    pass
                elif faces.remove([138,139,140]):
                    pass
                elif faces.remove([139,140,141]):
                    pass
                elif faces.remove([383,384,385]):
                    pass
                elif faces.remove([384,385,386]):
                    pass
                elif faces.remove([313,314,315]):
                    pass
                elif faces.remove([314,315,316]):
                    pass
                elif faces.remove([349,350,351]):
                    pass
                elif faces.remove([348,349,350]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.remove([33,34,35]):
                    pass
                elif faces.remove([68,69,70]):
                    pass
                elif faces.remove([69,70,71]):
                    pass
                elif faces.append([571,575,576]):
                    pass
                
            
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def NonParseGHG(filepath, GHG_Meshes=False,GHG_Skeleton_Data=False):
    with open(filepath, "rb") as f:
        if GHG_Meshes:
            WholeMeshGHGOne(f, vertices=[], faces=[], uvs=[],fa=-1,fb=0,fc=1,fa_=-3,fb_=-2,fc_=-1)
        if GHG_Skeleton_Data:
            CleanGHGNemoBonesWIP(f, bones=[])
                
        
                
        
        
        
