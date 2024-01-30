from struct import unpack, pack
import os
import bmesh
import math
import bpy
import mathutils
from io import BytesIO as bio
from bpy_extras import mesh_utils

vertices1=[]
vertices2=[]
vertices3=[]

def truncate_cstr(s: bytes) -> bytes:
    index = s.find(0)
    if index == -1: return s
    return s[:index]
def fetch_cstr(f: 'filelike') -> bytearray:
    build = bytearray()
    while 1:
        strbyte = f.read(1)
        if strbyte == b'\0' or not strbyte: break
        build += strbyte
    return build

def GHG_mesh(f, filepath):
    boneIndex = -1

    bones_=[]

    bone_parentlist=[]
        
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
    Texture_EntrySize = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    Material_EntrySize = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    SclBoneEntrySize = unpack("<I", f.read(4))[0]
    PosBoneEntrySize = unpack("<I", f.read(4))[0]
    RotBoneEntrySize = unpack("<I", f.read(4))[0]
    Unk_ = unpack("<I", f.read(4))[0]
    Unk__ = unpack("<I", f.read(4))[0]
    EndMaterialEntrySize = unpack("<I", f.read(4))[0]
    NamedtableEntrySize,=unpack("<I", f.read(4))
    f.seek(EndMaterialEntrySize-56,1)
    ntbl_buffer = bio(f.read(NamedtableEntrySize))
    name_i = 0
    while 1:
        name = fetch_cstr(ntbl_buffer).decode('ascii')
        if not name: break
        name_i +=1
    f.seek(0)
    f.seek(32,1)
    f.seek(SclBoneEntrySize-32,1)

    for i in range(BoneCount):
        f.seek(64,1)
        bdiv4_v00 = unpack("<f", f.read(4))[0]
        bdiv4_v04 = unpack("<f", f.read(4))[0]
        bdiv4_v08 = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        bone_parent,=unpack("b", f.read(1))
        bone_parentlist.append(bone_parent)
        #ntbl_buffer.seek(name_offset - 1) or ntbl_buffer.seek(name_offset)
        #bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
        name_offset,=unpack("<L", f.read(4)) # WHAT doesnt work
        f.seek(11,1)
        ntbl_buffer.seek(name_offset)
            
    f.seek(0)
    f.seek(36,1)
    f.seek(RotBoneEntrySize-36,1)
    for i in range(BoneCount):
        ScaleX = unpack("<f", f.read(4))[0]
        rotationz = unpack("<f", f.read(4))[0]
        rotationy = unpack("<f", f.read(4))[0]
        null1 = unpack("<f", f.read(4))[0]
        nrotationz = unpack("<f", f.read(4))[0]
        ScaleY = unpack("<f", f.read(4))[0]
        rotationx = unpack("<f", f.read(4))[0]
        nrotationy = unpack("<f", f.read(4))[0]
        null2 = unpack("<f", f.read(4))[0]
        nrotationx = unpack("<f", f.read(4))[0]
        ScaleZ = unpack("<f", f.read(4))[0]
        null3 = unpack("<f", f.read(4))[0]
        posx = unpack("<f", f.read(4))[0]
        posy = unpack("<f", f.read(4))[0]
        posz = unpack("<f", f.read(4))[0]
        ScaleW = unpack("<f", f.read(4))[0]

        matrix = mathutils.Matrix([[ScaleX,rotationz,rotationy,null1],[nrotationz,ScaleY,rotationx,nrotationy],[null2,nrotationx,ScaleZ,null3],[posx,posy,posz,ScaleW]]).inverted().to_3x3().transposed()

        bone_name = fetch_cstr(ntbl_buffer).decode('ascii')

        bone = skel.edit_bones.new(bone_name)
        
        bone.tail = mathutils.Vector([0,0,0.03])
        
        bone.head = ([
            posx,
            posy,
            posz,
        ])
        
        bone.length = -0.03
        
        bone.transform(matrix)
    for bone_id, bone_parent in enumerate(bone_parentlist):
        if bone_parent < 0: continue # root bone is set to -1
        skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
    bpy.ops.object.mode_set(mode = 'OBJECT')

    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm_1ccc = bmesh.new()
    bm_1cc = bmesh.new()

    
    bm_1bb = bmesh.new()
    bm_1e = bmesh.new()
    bm_1d = bmesh.new()
    bm_1c = bmesh.new()
    bm_1b = bmesh.new()
    bm_1a = bmesh.new()
    bm_1 = bmesh.new()
    bm = bmesh.new()
    bm2 = bmesh.new()
    bm3 = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x03\x01\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            if vertexCount == 3:
                for i in range(vertexCount//3):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    fa1 = bm.verts.new([-vx1,-vy1,-vz1])
                    fb1 = bm.verts.new([-vx2,-vy2,-vz2])
                    fc1 = bm.verts.new([-vx3,-vy3,-vz3])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                face_on = bm.faces.new([fa1,fb1,fc1])
            elif vertexCount == 4:
                for i in range(vertexCount//4):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    fa1 = bm_1.verts.new([-vx1,-vy1,-vz1])
                    fb1 = bm_1.verts.new([-vx2,-vy2,-vz2])
                    fc1 = bm_1.verts.new([-vx3,-vy3,-vz3])
                    fd1 = bm_1.verts.new([-vx4,-vy4,-vz4])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    face_on = bm_1.faces.new([fa1,fb1,fc1])
                                    face_on = bm_1.faces.new([fb1,fc1,fd1])
            elif vertexCount == 5:
                for i in range(vertexCount//5):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    type5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5 = unpack("<f", f.read(4))[0]
                    fa1 = bm_1a.verts.new([-vx1,-vy1,-vz1])
                    fb1 = bm_1a.verts.new([-vx2,-vy2,-vz2])
                    fc1 = bm_1a.verts.new([-vx3,-vy3,-vz3])
                    fd1 = bm_1a.verts.new([-vx4,-vy4,-vz4])
                    fe1 = bm_1a.verts.new([-vx5,-vy5,-vz5])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        
                                        face_on = bm_1a.faces.new([fa1,fb1,fc1])
                                        face_on = bm_1a.faces.new([fb1,fc1,fd1])
                                        face_on = bm_1a.faces.new([fc1,fd1,fe1])
            elif vertexCount == 6:
                for i in range(vertexCount//6):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    type5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5 = unpack("<f", f.read(4))[0]
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    type6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6 = unpack("<f", f.read(4))[0]
                    f.seek(-96,1)
                    vx1a = unpack("<f", f.read(4))[0]
                    vy1a = unpack("<f", f.read(4))[0]
                    vz1a = unpack("<f", f.read(4))[0]
                    type1a = unpack("B", f.read(1))[0]
                    value1a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1a = unpack("<f", f.read(4))[0]
                    vx2a = unpack("<f", f.read(4))[0]
                    vy2a = unpack("<f", f.read(4))[0]
                    vz2a = unpack("<f", f.read(4))[0]
                    type2a = unpack("B", f.read(1))[0]
                    value2a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2a = unpack("<f", f.read(4))[0]
                    vx3a = unpack("<f", f.read(4))[0]
                    vy3a = unpack("<f", f.read(4))[0]
                    vz3a = unpack("<f", f.read(4))[0]
                    type3a = unpack("B", f.read(1))[0]
                    value3a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3a = unpack("<f", f.read(4))[0]
                    vx4a = unpack("<f", f.read(4))[0]
                    vy4a = unpack("<f", f.read(4))[0]
                    vz4a = unpack("<f", f.read(4))[0]
                    type4a = unpack("B", f.read(1))[0]
                    value4a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4a = unpack("<f", f.read(4))[0]
                    vx5a = unpack("<f", f.read(4))[0]
                    vy5a = unpack("<f", f.read(4))[0]
                    vz5a = unpack("<f", f.read(4))[0]
                    type5a = unpack("B", f.read(1))[0]
                    value5a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5a = unpack("<f", f.read(4))[0]
                    vx6a = unpack("<f", f.read(4))[0]
                    vy6a = unpack("<f", f.read(4))[0]
                    vz6a = unpack("<f", f.read(4))[0]
                    type6a = unpack("B", f.read(1))[0]
                    value6a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6a = unpack("<f", f.read(4))[0]
                    fa1 = bm_1b.verts.new([-vx1,-vy1,-vz1])
                    fb1 = bm_1b.verts.new([-vx2,-vy2,-vz2])
                    fc1 = bm_1b.verts.new([-vx3,-vy3,-vz3])
                    fd1 = bm_1b.verts.new([-vx4,-vy4,-vz4])
                    fe1 = bm_1b.verts.new([-vx5,-vy5,-vz5])
                    ff1 = bm_1b.verts.new([-vx6,-vy6,-vz6])
                    faa1 = bm_1bb.verts.new([-vx1a,-vy1a,-vz1a])
                    fbb1 = bm_1bb.verts.new([-vx2a,-vy2a,-vz2a])
                    fcc1 = bm_1bb.verts.new([-vx3a,-vy3a,-vz3a])
                    fdd1 = bm_1bb.verts.new([-vx4a,-vy4a,-vz4a])
                    fee1 = bm_1bb.verts.new([-vx5a,-vy5a,-vz5a])
                    fff1 = bm_1bb.verts.new([-vx6a,-vy6a,-vz6a])
                    if type1a == 1:
                        if type2a == 1:
                            if type3a == 0:
                                if type4a == 0:
                                    if type5a == 0:
                                        if type6a == 0:
                                            face_on = bm_1bb.faces.new([faa1,fbb1,fcc1])
                                            face_on = bm_1bb.faces.new([fbb1,fcc1,fdd1])
                                            face_on = bm_1bb.faces.new([fcc1,fdd1,fee1])
                                            face_on = bm_1bb.faces.new([fdd1,fee1,fff1])
                                            
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 1:
                                    if type5 == 1:
                                        if type6 == 0:
                                            face_on = bm_1b.faces.new([fa1,fb1,fc1])
                                            face_on = bm_1b.faces.new([fd1,fe1,ff1])
                        

            elif vertexCount == 7:
                for i in range(vertexCount//7):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    type5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5 = unpack("<f", f.read(4))[0]
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    type6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6 = unpack("<f", f.read(4))[0]
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    type7 = unpack("B", f.read(1))[0]
                    value7 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7 = unpack("<f", f.read(4))[0]
                    f.seek(-112,1)

                    vx1a1 = unpack("<f", f.read(4))[0]
                    vy1a1 = unpack("<f", f.read(4))[0]
                    vz1a1 = unpack("<f", f.read(4))[0]
                    type1a1 = unpack("B", f.read(1))[0]
                    value1a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1a1 = unpack("<f", f.read(4))[0]
                    vx2a1 = unpack("<f", f.read(4))[0]
                    vy2a1 = unpack("<f", f.read(4))[0]
                    vz2a1 = unpack("<f", f.read(4))[0]
                    type2a1 = unpack("B", f.read(1))[0]
                    value2a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2a1 = unpack("<f", f.read(4))[0]
                    vx3a1 = unpack("<f", f.read(4))[0]
                    vy3a1 = unpack("<f", f.read(4))[0]
                    vz3a1 = unpack("<f", f.read(4))[0]
                    type3a1 = unpack("B", f.read(1))[0]
                    value3a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3a1 = unpack("<f", f.read(4))[0]
                    vx4a1 = unpack("<f", f.read(4))[0]
                    vy4a1 = unpack("<f", f.read(4))[0]
                    vz4a1 = unpack("<f", f.read(4))[0]
                    type4a1 = unpack("B", f.read(1))[0]
                    value4a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4a1 = unpack("<f", f.read(4))[0]
                    vx5a1 = unpack("<f", f.read(4))[0]
                    vy5a1 = unpack("<f", f.read(4))[0]
                    vz5a1 = unpack("<f", f.read(4))[0]
                    type5a1 = unpack("B", f.read(1))[0]
                    value5a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5a1 = unpack("<f", f.read(4))[0]
                    vx6a1 = unpack("<f", f.read(4))[0]
                    vy6a1 = unpack("<f", f.read(4))[0]
                    vz6a1 = unpack("<f", f.read(4))[0]
                    type6a1 = unpack("B", f.read(1))[0]
                    value6a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6a1 = unpack("<f", f.read(4))[0]
                    vx7a1 = unpack("<f", f.read(4))[0]
                    vy7a1 = unpack("<f", f.read(4))[0]
                    vz7a1 = unpack("<f", f.read(4))[0]
                    type7a1 = unpack("B", f.read(1))[0]
                    value7a1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7a1 = unpack("<f", f.read(4))[0]
                    f.seek(-112,1)

                    vx1b = unpack("<f", f.read(4))[0]
                    vy1b = unpack("<f", f.read(4))[0]
                    vz1b = unpack("<f", f.read(4))[0]
                    type1b = unpack("B", f.read(1))[0]
                    value1b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1b = unpack("<f", f.read(4))[0]
                    vx2b = unpack("<f", f.read(4))[0]
                    vy2b = unpack("<f", f.read(4))[0]
                    vz2b = unpack("<f", f.read(4))[0]
                    type2b = unpack("B", f.read(1))[0]
                    value2b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2b = unpack("<f", f.read(4))[0]
                    vx3a = unpack("<f", f.read(4))[0]
                    vy3a = unpack("<f", f.read(4))[0]
                    vz3a = unpack("<f", f.read(4))[0]
                    type3b = unpack("B", f.read(1))[0]
                    value3b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3a = unpack("<f", f.read(4))[0]
                    vx4b = unpack("<f", f.read(4))[0]
                    vy4b = unpack("<f", f.read(4))[0]
                    vz4b = unpack("<f", f.read(4))[0]
                    type4b = unpack("B", f.read(1))[0]
                    value4b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4b = unpack("<f", f.read(4))[0]
                    vx5b = unpack("<f", f.read(4))[0]
                    vy5b = unpack("<f", f.read(4))[0]
                    vz5b = unpack("<f", f.read(4))[0]
                    type5b = unpack("B", f.read(1))[0]
                    value5b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5b = unpack("<f", f.read(4))[0]
                    vx6b = unpack("<f", f.read(4))[0]
                    vy6b = unpack("<f", f.read(4))[0]
                    vz6b = unpack("<f", f.read(4))[0]
                    type6b = unpack("B", f.read(1))[0]
                    value6b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6b = unpack("<f", f.read(4))[0]
                    vx7b = unpack("<f", f.read(4))[0]
                    vy7b = unpack("<f", f.read(4))[0]
                    vz7b = unpack("<f", f.read(4))[0]
                    type7b = unpack("B", f.read(1))[0]
                    value7b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7b = unpack("<f", f.read(4))[0]
                    
                    fa1 = bm_1c.verts.new([-vx1,-vy1,-vz1])
                    fb1 = bm_1c.verts.new([-vx2,-vy2,-vz2])
                    fc1 = bm_1c.verts.new([-vx3,-vy3,-vz3])
                    fd1 = bm_1c.verts.new([-vx4,-vy4,-vz4])
                    fe1 = bm_1c.verts.new([-vx5,-vy5,-vz5])
                    ff1 = bm_1c.verts.new([-vx6,-vy6,-vz6])
                    fg1 = bm_1c.verts.new([-vx7,-vy7,-vz7])

                    faa1 = bm_1cc.verts.new([-vx1a1,-vy1a1,-vz1a1])
                    fba1 = bm_1cc.verts.new([-vx2a1,-vy2a1,-vz2a1])
                    fca1 = bm_1cc.verts.new([-vx3a1,-vy3a1,-vz3a1])
                    fda1 = bm_1cc.verts.new([-vx4a1,-vy4a1,-vz4a1])
                    fea1 = bm_1cc.verts.new([-vx5a1,-vy5a1,-vz5a1])
                    ffa1 = bm_1cc.verts.new([-vx6a1,-vy6a1,-vz6a1])
                    fga1 = bm_1cc.verts.new([-vx7a1,-vy7a1,-vz7a1])

                    faaa1 = bm_1ccc.verts.new([-vx1b,-vy1b,-vz1b])
                    fbaa1 = bm_1ccc.verts.new([-vx2b,-vy2b,-vz2b])
                    fcaa1 = bm_1ccc.verts.new([-vx3a,-vy3a,-vz3a])
                    fdaa1 = bm_1ccc.verts.new([-vx4b,-vy4b,-vz4b])
                    feaa1 = bm_1ccc.verts.new([-vx5b,-vy5b,-vz5b])
                    ffaa1 = bm_1ccc.verts.new([-vx6b,-vy6b,-vz6b])
                    fgaa1 = bm_1ccc.verts.new([-vx7b,-vy7b,-vz7b])

                    if type1b == 1:
                        if type2b == 1:
                            if type3b == 0:
                                if type4b == 1:
                                    if type5b == 1:
                                        if type6b == 0:
                                            if type7b == 0:
                                                face_on = bm_1ccc.faces.new([faaa1,fbaa1,fcaa1])
                                                face_on = bm_1ccc.faces.new([fdaa1,feaa1,ffaa1])

                                                face_on = bm_1ccc.faces.new([feaa1,ffaa1,fgaa1])
                    if type1a1 == 1:
                        if type2a1 == 1:
                            if type3a1 == 0:
                                if type4a1 == 0:
                                    if type5a1 == 1:
                                        if type6a1 == 1:
                                            if type7a1 == 0:
                                                face_on = bm_1cc.faces.new([faa1,fba1,fca1])
                                                face_on = bm_1cc.faces.new([fba1,fca1,fda1])

                                                face_on = bm_1cc.faces.new([fea1,ffa1,fga1])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                face_on = bm_1c.faces.new([fa1,fb1,fc1])
                                                face_on = bm_1c.faces.new([fb1,fc1,fd1])
                                                face_on = bm_1c.faces.new([fc1,fd1,fe1])
                                                face_on = bm_1c.faces.new([fd1,fe1,ff1])
                                                face_on = bm_1c.faces.new([fe1,ff1,fg1])

            elif vertexCount == 8:
                for i in range(vertexCount//8):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    type5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5 = unpack("<f", f.read(4))[0]
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    type6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6 = unpack("<f", f.read(4))[0]
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    type7 = unpack("B", f.read(1))[0]
                    value7 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7 = unpack("<f", f.read(4))[0]
                    vx8 = unpack("<f", f.read(4))[0]
                    vy8 = unpack("<f", f.read(4))[0]
                    vz8 = unpack("<f", f.read(4))[0]
                    type8 = unpack("B", f.read(1))[0]
                    value8 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8 = unpack("<f", f.read(4))[0]
                    fa1 = bm_1d.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1d.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1d.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1d.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1d.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1d.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1d.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1d.verts.new([-vx8,-vy8,-vz8]) # 7
                    if type5 == 0:
                        
                        bm_1d.faces.new([fa1,fb1,fc1])
                        bm_1d.faces.new([fb1,fc1,fd1])
                        bm_1d.faces.new([fc1,fd1,fe1])
                        bm_1d.faces.new([fd1,fe1,ff1])
                        bm_1d.faces.new([fe1,ff1,fg1])
                        bm_1d.faces.new([ff1,fg1,fh1])
                    elif type5 == 1:
                        bm_1d.faces.new([fa1,fb1,fc1])
                        bm_1d.faces.new([fb1,fc1,fd1])
                        bm_1d.faces.new([fe1,ff1,fg1])
                        bm_1d.faces.new([ff1,fg1,fh1])

            elif vertexCount == 9:
                for i in range(vertexCount//9):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    type1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1 = unpack("<f", f.read(4))[0]
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    type2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2 = unpack("<f", f.read(4))[0]
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    type3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3 = unpack("<f", f.read(4))[0]
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4 = unpack("<f", f.read(4))[0]
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    type5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5 = unpack("<f", f.read(4))[0]
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    type6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6 = unpack("<f", f.read(4))[0]
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    type7 = unpack("B", f.read(1))[0]
                    value7 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7 = unpack("<f", f.read(4))[0]
                    vx8 = unpack("<f", f.read(4))[0]
                    vy8 = unpack("<f", f.read(4))[0]
                    vz8 = unpack("<f", f.read(4))[0]
                    type8 = unpack("B", f.read(1))[0]
                    value8 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8 = unpack("<f", f.read(4))[0]
                    vx9 = unpack("<f", f.read(4))[0]
                    vy9 = unpack("<f", f.read(4))[0]
                    vz9 = unpack("<f", f.read(4))[0]
                    type9 = unpack("B", f.read(1))[0]
                    value9 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9 = unpack("<f", f.read(4))[0]
                    fa1 = bm_1e.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1e.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1e.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1e.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1e.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1e.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1e.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1e.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1e.verts.new([-vx9,-vy9,-vz9]) # 8
                    if type5 == 0:
                        bm_1e.faces.new([fa1,fb1,fc1])
                        bm_1e.faces.new([fb1,fc1,fd1])
                        bm_1e.faces.new([fc1,fd1,fe1])
                        bm_1e.faces.new([fd1,fe1,ff1])
                        bm_1e.faces.new([fe1,ff1,fg1])
                        bm_1e.faces.new([ff1,fg1,fh1])
                        bm_1e.faces.new([fg1,fh1,fi1])
                    elif type5 == 1:
                        bm_1e.faces.new([fa1,fb1,fc1])
                        bm_1e.faces.new([fb1,fc1,fd1])
                        bm_1e.faces.new([fe1,ff1,fg1])
                        bm_1e.faces.new([ff1,fg1,fh1])
                        bm_1e.faces.new([fg1,fh1,fi1])
                
                                        
                                    
                
        elif Chunks == b"\x03\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                    
                vx2 = unpack("<h", f.read(2))[0] / 4096
                vy2 = unpack("<h", f.read(2))[0] / 4096
                vz2 = unpack("<h", f.read(2))[0] / 4096
                vw2 = unpack("<h", f.read(2))[0] / 4096
                f.seek(8,1)
                f_1 = bm2.verts.new([-vx2,-vy2,-vz2])
        elif Chunks == b"\x04\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                    
                vx3 = unpack("<f", f.read(4))[0]
                vy3 = unpack("<f", f.read(4))[0]
                vz3 = unpack("<f", f.read(4))[0]
                vw3 = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                f__ = bm3.verts.new([-vx3,-vy3,-vz3])
                                
                        
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects1 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects1)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    objects1.parent = arma
    armamodifier1 = objects1.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1.object = arma

    vgroups1 = [objects1.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #######################################
    #######################################
    #######################################

    mesh__1 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1.from_mesh(mesh__1)
    objects1_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__1)
    collection.objects.link(objects1_)
    bmesh.ops.remove_doubles(bm_1, verts = bm_1.verts, dist = 0.0001)
    bm_1.to_mesh(mesh__1)

    objects1_.parent = arma
    armamodifier1_ = objects1_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1_.object = arma

    vgroups1_ = [objects1_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1a.from_mesh(mesh__2)
    objects1a_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__2)
    collection.objects.link(objects1a_)
    bmesh.ops.remove_doubles(bm_1a, verts = bm_1a.verts, dist = 0.0001)
    bm_1a.to_mesh(mesh__2)

    objects1a_.parent = arma
    armamodifier1a_ = objects1a_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1a_.object = arma

    vgroups1a_ = [objects1a_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #############################################
    #############################################
    #############################################

    mesh__3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1b.from_mesh(mesh__3)
    objects1b_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__3)
    collection.objects.link(objects1b_)
    bmesh.ops.remove_doubles(bm_1b, verts = bm_1b.verts, dist = 0.0001)
    bm_1b.to_mesh(mesh__3)

    objects1b_.parent = arma
    armamodifier1b_ = objects1b_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1b_.object = arma

    vgroups1b_ = [objects1b_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###########################

    mesh__3a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1bb.from_mesh(mesh__3a)
    objects1bb_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__3a)
    collection.objects.link(objects1bb_)
    bmesh.ops.remove_doubles(bm_1bb, verts = bm_1bb.verts, dist = 0.0001)
    bm_1bb.to_mesh(mesh__3a)

    objects1bb_.parent = arma
    armamodifier1bb_ = objects1bb_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1bb_.object = arma

    vgroups1bb_ = [objects1bb_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    
    ###########################

    

    mesh__4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1c.from_mesh(mesh__4)
    objects1c_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__4)
    collection.objects.link(objects1c_)
    bmesh.ops.remove_doubles(bm_1c, verts = bm_1c.verts, dist = 0.0001)
    bm_1c.to_mesh(mesh__4)

    objects1c_.parent = arma
    armamodifier1c_ = objects1c_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1c_.object = arma

    vgroups1c_ = [objects1c_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__4a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1cc.from_mesh(mesh__4a)
    objects1cc_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__4a)
    collection.objects.link(objects1cc_)
    bmesh.ops.remove_doubles(bm_1cc, verts = bm_1cc.verts, dist = 0.0001)
    bm_1cc.to_mesh(mesh__4a)

    objects1cc_.parent = arma
    armamodifier1cc_ = objects1cc_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1cc_.object = arma

    vgroups1cc_ = [objects1cc_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__4aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ccc.from_mesh(mesh__4aa)
    objects1ccc_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__4aa)
    collection.objects.link(objects1ccc_)
    bmesh.ops.remove_doubles(bm_1ccc, verts = bm_1ccc.verts, dist = 0.0001)
    bm_1ccc.to_mesh(mesh__4aa)

    objects1ccc_.parent = arma
    armamodifier1ccc_ = objects1ccc_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ccc_.object = arma

    vgroups1ccc_ = [objects1ccc_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ################################################
    ################################################
    ################################################

    mesh__5 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1d.from_mesh(mesh__5)
    objects1d_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__5)
    collection.objects.link(objects1d_)
    bmesh.ops.remove_doubles(bm_1d, verts = bm_1d.verts, dist = 0.0001)
    bm_1d.to_mesh(mesh__5)

    objects1d_.parent = arma
    armamodifier1d_ = objects1d_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1d_.object = arma

    vgroups1d_ = [objects1d_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    mesh__6 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1e.from_mesh(mesh__6)
    objects1e_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__6)
    collection.objects.link(objects1e_)
    bmesh.ops.remove_doubles(bm_1e, verts = bm_1e.verts, dist = 0.0001)
    bm_1e.to_mesh(mesh__6)

    objects1e_.parent = arma
    armamodifier1e_ = objects1e_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1e_.object = arma

    vgroups1e_ = [objects1e_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###########################################################################################
    ###########################################################################################

    

    ###########################################################################################
    ###########################################################################################
    

    ###########################################################################################
    ###########################################################################################


    ###############################################################
    ###############################################################
    ###############################################################
    

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm2.from_mesh(mesh2)
    objects2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(objects2)
    bmesh.ops.remove_doubles(bm2, verts = bm2.verts, dist = 0.0001)
    bm2.to_mesh(mesh2)

    objects2.parent = arma
    armamodifier2 = objects2.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier2.object = arma

    vgroups2 = [objects2.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm3.from_mesh(mesh3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)
    bmesh.ops.remove_doubles(bm3, verts = bm3.verts, dist = 0.0001)
    bm3.to_mesh(mesh3)

    objects3.parent = arma
    armamodifier3 = objects3.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3.object = arma

    vgroups3 = [objects3.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    
                        

def GHG_mesh_1(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm = bmesh.new()
    memory_face_offset=67043583
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x03\x01\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                    
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                vw1 = unpack("<f", f.read(4))[0]
                fa1 = bm.verts.new([-vx1,-vy1,-vz1])
                                
                        
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    """for fac in bm.faces:
        fac.normal_flip()

    for fac in mesh.polygons:
        fac.use_smooth = True"""
                

def GHG_mesh_2(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x03\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0]//2
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<h", f.read(2))[0] / 4096
                vy1 = unpack("<h", f.read(2))[0] / 4096
                vz1 = unpack("<h", f.read(2))[0] / 4096
                vw1 = unpack("<h", f.read(2))[0] / 4096
                f.seek(8,1)
                bm.verts.new([-vx1,-vy1,-vz1])
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    """for fac in mesh.polygons:
        fac.use_smooth = True"""

def GHG_mesh_3(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    uvs=[]
    bm = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x04\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                vw1 = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                bm.verts.new([-vx1,-vy1,-vz1])
                    
            
                
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    """for fac in bm.faces:
        fac.normal_flip()

    for fac in mesh.polygons:
        fac.use_smooth = True"""

def GHG_weights_3(f, filepath):

    ob = bpy.context.object

    for pbone in ob.pose.bones:
        pbone.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier.object = arma
    vgroups = [ob.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    """f.seek(0)
    weightChunk = f.read()
    f.seek(0)
    for i in range(len(weightChunk)):
        weightsChunks = f.read(4)
        if weightsChunks == b"\x01\x00\x01\x05":
            pass"""
    #0x01000105
            

def ghg_open(filepath, offset_on_off=False, offsets="", weights_on=False, weight_offset=""):
    with open(filepath, "rb") as f:
        if offset_on_off:
            if offsets == "all":
                GHG_mesh(f, filepath)

        if weights_on:
            if weight_offset == "0x01000105":
                GHG_weights_3(f, filepath)
            
            
                
            
    
