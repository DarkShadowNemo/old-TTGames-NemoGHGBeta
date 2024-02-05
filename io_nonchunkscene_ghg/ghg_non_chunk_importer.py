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

    bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiiii = bmesh.new()
    bm_1iiiiiiiiii = bmesh.new()
    bm_1iiiiiiiii = bmesh.new()
    bm_1iiiiiiii = bmesh.new()
    bm_1iiiiiii = bmesh.new()
    bm_1iiiiii = bmesh.new()
    bm_1iiiii = bmesh.new()
    bm_1iiii = bmesh.new()
    bm_1iii = bmesh.new()
    bm_1ii = bmesh.new()

    bm_1i = bmesh.new()
    
    bm_1hhhhhhhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhhh = bmesh.new()
    bm_1hhhhhhhhh = bmesh.new()
    bm_1hhhhhhhh = bmesh.new()
    bm_1hhhhhhh = bmesh.new()
    bm_1hhhhhh = bmesh.new()
    bm_1hhhhh = bmesh.new()
    bm_1hhhh = bmesh.new()
    bm_1hhh = bmesh.new()
    bm_1hh = bmesh.new()
    bm_1h = bmesh.new()

    bm_1gggggggggg = bmesh.new()
    bm_1ggggggggg = bmesh.new()
    bm_1gggggggg = bmesh.new()
    bm_1ggggggg = bmesh.new()
    bm_1gggggg = bmesh.new()
    bm_1ggggg = bmesh.new()
    bm_1gggg = bmesh.new()
    bm_1ggg = bmesh.new()
    bm_1gg = bmesh.new()
    bm_1g = bmesh.new()
    bm_1ccc = bmesh.new()
    bm_1cc = bmesh.new()
    bm_1f = bmesh.new()
    bm_1ff = bmesh.new()
    bm_1fff = bmesh.new()
    bm_1dd = bmesh.new()
    bm_1ddd = bmesh.new()
    bm_1bb = bmesh.new()
    bm_1e = bmesh.new()
    bm_1ee = bmesh.new()
    bm_1eee = bmesh.new()
    bm_1eeee = bmesh.new()
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
                    f.seek(-128,1)
                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    vx21 = unpack("<f", f.read(4))[0]
                    vy21 = unpack("<f", f.read(4))[0]
                    vz21 = unpack("<f", f.read(4))[0]
                    type21 = unpack("B", f.read(1))[0]
                    value21 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw21 = unpack("<f", f.read(4))[0]
                    vx31 = unpack("<f", f.read(4))[0]
                    vy31 = unpack("<f", f.read(4))[0]
                    vz31 = unpack("<f", f.read(4))[0]
                    type31 = unpack("B", f.read(1))[0]
                    value31 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw31 = unpack("<f", f.read(4))[0]
                    vx41 = unpack("<f", f.read(4))[0]
                    vy41 = unpack("<f", f.read(4))[0]
                    vz41 = unpack("<f", f.read(4))[0]
                    type41 = unpack("B", f.read(1))[0]
                    value41 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw41 = unpack("<f", f.read(4))[0]
                    vx51 = unpack("<f", f.read(4))[0]
                    vy51 = unpack("<f", f.read(4))[0]
                    vz51 = unpack("<f", f.read(4))[0]
                    type51 = unpack("B", f.read(1))[0]
                    value51 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw51 = unpack("<f", f.read(4))[0]
                    vx61 = unpack("<f", f.read(4))[0]
                    vy61 = unpack("<f", f.read(4))[0]
                    vz61 = unpack("<f", f.read(4))[0]
                    type61 = unpack("B", f.read(1))[0]
                    value61 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw61 = unpack("<f", f.read(4))[0]
                    vx71 = unpack("<f", f.read(4))[0]
                    vy71 = unpack("<f", f.read(4))[0]
                    vz71 = unpack("<f", f.read(4))[0]
                    type71 = unpack("B", f.read(1))[0]
                    value71 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw71 = unpack("<f", f.read(4))[0]
                    vx81 = unpack("<f", f.read(4))[0]
                    vy81 = unpack("<f", f.read(4))[0]
                    vz81 = unpack("<f", f.read(4))[0]
                    type81 = unpack("B", f.read(1))[0]
                    value81 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw81 = unpack("<f", f.read(4))[0]
                    f.seek(-128,1)

                    vx11a = unpack("<f", f.read(4))[0]
                    vy11a = unpack("<f", f.read(4))[0]
                    vz11a = unpack("<f", f.read(4))[0]
                    type11a = unpack("B", f.read(1))[0]
                    value11a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11a = unpack("<f", f.read(4))[0]
                    vx21a = unpack("<f", f.read(4))[0]
                    vy21a = unpack("<f", f.read(4))[0]
                    vz21a = unpack("<f", f.read(4))[0]
                    type21a = unpack("B", f.read(1))[0]
                    value21a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw21a = unpack("<f", f.read(4))[0]
                    vx31a = unpack("<f", f.read(4))[0]
                    vy31a = unpack("<f", f.read(4))[0]
                    vz31a = unpack("<f", f.read(4))[0]
                    type31a = unpack("B", f.read(1))[0]
                    value31a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw31a = unpack("<f", f.read(4))[0]
                    vx41a = unpack("<f", f.read(4))[0]
                    vy41a = unpack("<f", f.read(4))[0]
                    vz41a = unpack("<f", f.read(4))[0]
                    type41a = unpack("B", f.read(1))[0]
                    value41a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw41a = unpack("<f", f.read(4))[0]
                    vx51a = unpack("<f", f.read(4))[0]
                    vy51a = unpack("<f", f.read(4))[0]
                    vz51a = unpack("<f", f.read(4))[0]
                    type51a = unpack("B", f.read(1))[0]
                    value51a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw51a = unpack("<f", f.read(4))[0]
                    vx61a = unpack("<f", f.read(4))[0]
                    vy61a = unpack("<f", f.read(4))[0]
                    vz61a = unpack("<f", f.read(4))[0]
                    type61a = unpack("B", f.read(1))[0]
                    value61a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw61a = unpack("<f", f.read(4))[0]
                    vx71a = unpack("<f", f.read(4))[0]
                    vy71a = unpack("<f", f.read(4))[0]
                    vz71a = unpack("<f", f.read(4))[0]
                    type71a = unpack("B", f.read(1))[0]
                    value71a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw71a = unpack("<f", f.read(4))[0]
                    vx81a = unpack("<f", f.read(4))[0]
                    vy81a = unpack("<f", f.read(4))[0]
                    vz81a = unpack("<f", f.read(4))[0]
                    type81a = unpack("B", f.read(1))[0]
                    value81a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw81a = unpack("<f", f.read(4))[0]

                    faaa1 = bm_1ddd.verts.new([-vx11a,-vy11a,-vz11a]) # 0
                    fbbb1 = bm_1ddd.verts.new([-vx21a,-vy21a,-vz21a]) # 1
                    fccc1 = bm_1ddd.verts.new([-vx31a,-vy31a,-vz31a]) # 2
                    fddd1 = bm_1ddd.verts.new([-vx41a,-vy41a,-vz41a]) # 3
                    feee1 = bm_1ddd.verts.new([-vx51a,-vy51a,-vz51a]) # 4
                    ffff1 = bm_1ddd.verts.new([-vx61a,-vy61a,-vz61a]) # 5
                    fggg1 = bm_1ddd.verts.new([-vx71a,-vy71a,-vz71a]) # 6
                    fhhh1 = bm_1ddd.verts.new([-vx81a,-vy81a,-vz81a]) # 7
                    
                    faa1 = bm_1dd.verts.new([-vx11,-vy11,-vz11]) # 0
                    fbb1 = bm_1dd.verts.new([-vx21,-vy21,-vz21]) # 1
                    fcc1 = bm_1dd.verts.new([-vx31,-vy31,-vz31]) # 2
                    fdd1 = bm_1dd.verts.new([-vx41,-vy41,-vz41]) # 3
                    fee1 = bm_1dd.verts.new([-vx51,-vy51,-vz51]) # 4
                    fff1 = bm_1dd.verts.new([-vx61,-vy61,-vz61]) # 5
                    fgg1 = bm_1dd.verts.new([-vx71,-vy71,-vz71]) # 6
                    fhh1 = bm_1dd.verts.new([-vx81,-vy81,-vz81]) # 7

                    fa1 = bm_1d.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1d.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1d.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1d.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1d.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1d.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1d.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1d.verts.new([-vx8,-vy8,-vz8]) # 7
                    if type11a == 1:
                        if type21a == 1:
                            if type31a == 0:
                                if type41a == 0:
                                    if type51a == 1:
                                        if type61a == 1:
                                            if type71a == 0:
                                                if type81a == 0:
                                                    bm_1ddd.faces.new([faaa1,fbbb1,fccc1])
                                                    bm_1ddd.faces.new([fbbb1,fccc1,fddd1])
                                                    bm_1ddd.faces.new([feee1,ffff1,fggg1])
                                                    bm_1ddd.faces.new([ffff1,fggg1,fhhh1])
                                                    
                    if type11 == 1:
                        if type21 == 1:
                            if type31 == 0:
                                if type41 == 1:
                                    if type51 == 1:
                                        if type61 == 0:
                                            if type71 == 0:
                                                if type81 == 0:
                                                    bm_1dd.faces.new([faa1,fbb1,fcc1])
                                                    bm_1dd.faces.new([fdd1,fee1,fff1])
                                                    bm_1dd.faces.new([fee1,fff1,fgg1])
                                                    bm_1dd.faces.new([fff1,fgg1,fhh1])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    bm_1d.faces.new([fa1,fb1,fc1])
                                                    bm_1d.faces.new([fb1,fc1,fd1])
                                                    bm_1d.faces.new([fc1,fd1,fe1])
                                                    bm_1d.faces.new([fd1,fe1,ff1])
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
                    f.seek(-144,1)

                    

                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    vx21 = unpack("<f", f.read(4))[0]
                    vy21 = unpack("<f", f.read(4))[0]
                    vz21 = unpack("<f", f.read(4))[0]
                    type21 = unpack("B", f.read(1))[0]
                    value21 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw21 = unpack("<f", f.read(4))[0]
                    vx31 = unpack("<f", f.read(4))[0]
                    vy31 = unpack("<f", f.read(4))[0]
                    vz31 = unpack("<f", f.read(4))[0]
                    type31 = unpack("B", f.read(1))[0]
                    value31 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw31 = unpack("<f", f.read(4))[0]
                    vx41 = unpack("<f", f.read(4))[0]
                    vy41 = unpack("<f", f.read(4))[0]
                    vz41 = unpack("<f", f.read(4))[0]
                    type41 = unpack("B", f.read(1))[0]
                    value41 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw41 = unpack("<f", f.read(4))[0]
                    vx51 = unpack("<f", f.read(4))[0]
                    vy51 = unpack("<f", f.read(4))[0]
                    vz51 = unpack("<f", f.read(4))[0]
                    type51 = unpack("B", f.read(1))[0]
                    value51 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw51 = unpack("<f", f.read(4))[0]
                    vx61 = unpack("<f", f.read(4))[0]
                    vy61 = unpack("<f", f.read(4))[0]
                    vz61 = unpack("<f", f.read(4))[0]
                    type61 = unpack("B", f.read(1))[0]
                    value61 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw61 = unpack("<f", f.read(4))[0]
                    vx71 = unpack("<f", f.read(4))[0]
                    vy71 = unpack("<f", f.read(4))[0]
                    vz71 = unpack("<f", f.read(4))[0]
                    type71 = unpack("B", f.read(1))[0]
                    value71 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw71 = unpack("<f", f.read(4))[0]
                    vx81 = unpack("<f", f.read(4))[0]
                    vy81 = unpack("<f", f.read(4))[0]
                    vz81 = unpack("<f", f.read(4))[0]
                    type81 = unpack("B", f.read(1))[0]
                    value81 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw81 = unpack("<f", f.read(4))[0]
                    vx91 = unpack("<f", f.read(4))[0]
                    vy91 = unpack("<f", f.read(4))[0]
                    vz91 = unpack("<f", f.read(4))[0]
                    type91 = unpack("B", f.read(1))[0]
                    value91 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw91 = unpack("<f", f.read(4))[0]
                    f.seek(-144,1)


                    

                    vx111 = unpack("<f", f.read(4))[0]
                    vy111 = unpack("<f", f.read(4))[0]
                    vz111 = unpack("<f", f.read(4))[0]
                    type111 = unpack("B", f.read(1))[0]
                    value111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw111 = unpack("<f", f.read(4))[0]
                    vx211 = unpack("<f", f.read(4))[0]
                    vy211 = unpack("<f", f.read(4))[0]
                    vz211 = unpack("<f", f.read(4))[0]
                    type211 = unpack("B", f.read(1))[0]
                    value211 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw211 = unpack("<f", f.read(4))[0]
                    vx311 = unpack("<f", f.read(4))[0]
                    vy311 = unpack("<f", f.read(4))[0]
                    vz311 = unpack("<f", f.read(4))[0]
                    type311 = unpack("B", f.read(1))[0]
                    value311 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw311 = unpack("<f", f.read(4))[0]
                    vx411 = unpack("<f", f.read(4))[0]
                    vy411 = unpack("<f", f.read(4))[0]
                    vz411 = unpack("<f", f.read(4))[0]
                    type411 = unpack("B", f.read(1))[0]
                    value411 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw411 = unpack("<f", f.read(4))[0]
                    vx511 = unpack("<f", f.read(4))[0]
                    vy511 = unpack("<f", f.read(4))[0]
                    vz511 = unpack("<f", f.read(4))[0]
                    type511 = unpack("B", f.read(1))[0]
                    value511 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw511 = unpack("<f", f.read(4))[0]
                    vx611 = unpack("<f", f.read(4))[0]
                    vy611 = unpack("<f", f.read(4))[0]
                    vz611 = unpack("<f", f.read(4))[0]
                    type611 = unpack("B", f.read(1))[0]
                    value611 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw611 = unpack("<f", f.read(4))[0]
                    vx711 = unpack("<f", f.read(4))[0]
                    vy711 = unpack("<f", f.read(4))[0]
                    vz711 = unpack("<f", f.read(4))[0]
                    type711 = unpack("B", f.read(1))[0]
                    value711 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw711 = unpack("<f", f.read(4))[0]
                    vx811 = unpack("<f", f.read(4))[0]
                    vy811 = unpack("<f", f.read(4))[0]
                    vz811 = unpack("<f", f.read(4))[0]
                    type811 = unpack("B", f.read(1))[0]
                    value811 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw811 = unpack("<f", f.read(4))[0]
                    vx911 = unpack("<f", f.read(4))[0]
                    vy911 = unpack("<f", f.read(4))[0]
                    vz911 = unpack("<f", f.read(4))[0]
                    type911 = unpack("B", f.read(1))[0]
                    value911 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw911 = unpack("<f", f.read(4))[0]
                    f.seek(-144,1)



                    
                    vx1111 = unpack("<f", f.read(4))[0]
                    vy1111 = unpack("<f", f.read(4))[0]
                    vz1111 = unpack("<f", f.read(4))[0]
                    type1111 = unpack("B", f.read(1))[0]
                    value1111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1111 = unpack("<f", f.read(4))[0]
                    vx2111 = unpack("<f", f.read(4))[0]
                    vy2111 = unpack("<f", f.read(4))[0]
                    vz2111 = unpack("<f", f.read(4))[0]
                    type2111 = unpack("B", f.read(1))[0]
                    value2111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2111 = unpack("<f", f.read(4))[0]
                    vx3111 = unpack("<f", f.read(4))[0]
                    vy3111 = unpack("<f", f.read(4))[0]
                    vz3111 = unpack("<f", f.read(4))[0]
                    type3111 = unpack("B", f.read(1))[0]
                    value3111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3111 = unpack("<f", f.read(4))[0]
                    vx4111 = unpack("<f", f.read(4))[0]
                    vy4111 = unpack("<f", f.read(4))[0]
                    vz4111 = unpack("<f", f.read(4))[0]
                    type4111 = unpack("B", f.read(1))[0]
                    value4111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4111 = unpack("<f", f.read(4))[0]
                    vx5111 = unpack("<f", f.read(4))[0]
                    vy5111 = unpack("<f", f.read(4))[0]
                    vz5111 = unpack("<f", f.read(4))[0]
                    type5111 = unpack("B", f.read(1))[0]
                    value5111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5111 = unpack("<f", f.read(4))[0]
                    vx6111 = unpack("<f", f.read(4))[0]
                    vy6111 = unpack("<f", f.read(4))[0]
                    vz6111 = unpack("<f", f.read(4))[0]
                    type6111 = unpack("B", f.read(1))[0]
                    value6111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6111 = unpack("<f", f.read(4))[0]
                    vx7111 = unpack("<f", f.read(4))[0]
                    vy7111 = unpack("<f", f.read(4))[0]
                    vz7111 = unpack("<f", f.read(4))[0]
                    type7111 = unpack("B", f.read(1))[0]
                    value7111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7111 = unpack("<f", f.read(4))[0]
                    vx8111 = unpack("<f", f.read(4))[0]
                    vy8111 = unpack("<f", f.read(4))[0]
                    vz8111 = unpack("<f", f.read(4))[0]
                    type8111 = unpack("B", f.read(1))[0]
                    value8111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8111 = unpack("<f", f.read(4))[0]
                    vx9111 = unpack("<f", f.read(4))[0]
                    vy9111 = unpack("<f", f.read(4))[0]
                    vz9111 = unpack("<f", f.read(4))[0]
                    type9111 = unpack("B", f.read(1))[0]
                    value9111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9111 = unpack("<f", f.read(4))[0]

                    
                    fa1 = bm_1e.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1e.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1e.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1e.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1e.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1e.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1e.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1e.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1e.verts.new([-vx9,-vy9,-vz9]) # 8


                    faa1 = bm_1ee.verts.new([-vx11,-vy11,-vz11]) # 0
                    fbb1 = bm_1ee.verts.new([-vx21,-vy21,-vz21]) # 1
                    fcc1 = bm_1ee.verts.new([-vx31,-vy31,-vz31]) # 2
                    fdd1 = bm_1ee.verts.new([-vx41,-vy41,-vz41]) # 3
                    fee1 = bm_1ee.verts.new([-vx51,-vy51,-vz51]) # 4
                    fff1 = bm_1ee.verts.new([-vx61,-vy61,-vz61]) # 5
                    fgg1 = bm_1ee.verts.new([-vx71,-vy71,-vz71]) # 6
                    fhh1 = bm_1ee.verts.new([-vx81,-vy81,-vz81]) # 7
                    fii1 = bm_1ee.verts.new([-vx91,-vy91,-vz91]) # 8

                    faaa1 = bm_1eee.verts.new([-vx111,-vy111,-vz111]) # 0
                    fbbb1 = bm_1eee.verts.new([-vx211,-vy211,-vz211]) # 1
                    fccc1 = bm_1eee.verts.new([-vx311,-vy311,-vz311]) # 2
                    fddd1 = bm_1eee.verts.new([-vx411,-vy411,-vz411]) # 3
                    feee1 = bm_1eee.verts.new([-vx511,-vy511,-vz511]) # 4
                    ffff1 = bm_1eee.verts.new([-vx611,-vy611,-vz611]) # 5
                    fggg1 = bm_1eee.verts.new([-vx711,-vy711,-vz711]) # 6
                    fhhh1 = bm_1eee.verts.new([-vx811,-vy811,-vz811]) # 7
                    fiii1 = bm_1eee.verts.new([-vx911,-vy911,-vz911]) # 8

                    faaaa1 = bm_1eeee.verts.new([-vx1111,-vy1111,-vz1111]) # 0
                    fbbbb1 = bm_1eeee.verts.new([-vx2111,-vy2111,-vz2111]) # 1
                    fcccc1 = bm_1eeee.verts.new([-vx3111,-vy3111,-vz3111]) # 2
                    fdddd1 = bm_1eeee.verts.new([-vx4111,-vy4111,-vz4111]) # 3
                    feeee1 = bm_1eeee.verts.new([-vx5111,-vy5111,-vz5111]) # 4
                    fffff1 = bm_1eeee.verts.new([-vx6111,-vy6111,-vz6111]) # 5
                    fgggg1 = bm_1eeee.verts.new([-vx7111,-vy7111,-vz7111]) # 6
                    fhhhh1 = bm_1eeee.verts.new([-vx8111,-vy8111,-vz8111]) # 7
                    fiiii1 = bm_1eeee.verts.new([-vx9111,-vy9111,-vz9111]) # 8

                    if type1111 == 1:
                        if type2111 == 1:
                            if type3111 == 0:
                                if type4111 == 0:
                                    if type5111 == 0:
                                        if type6111 == 0:
                                            if type7111 == 1:
                                                if type8111 == 1:
                                                    if type9111 == 0:
                                                        bm_1eeee.faces.new([faaaa1,fbbbb1,fcccc1])
                                                        bm_1eeee.faces.new([fbbbb1,fcccc1,fdddd1])
                                                        bm_1eeee.faces.new([fcccc1,fdddd1,feeee1])
                                                        bm_1eeee.faces.new([fdddd1,feeee1,fffff1])
                                                        bm_1eeee.faces.new([fgggg1,fhhhh1,fiiii1])
                                                        
                                                        

                    if type111 == 1:
                        if type211 == 1:
                            if type311 == 0:
                                if type411 == 0:
                                    if type511 == 1:
                                        if type611 == 1:
                                            if type711 == 0:
                                                if type811 == 0:
                                                    if type911 == 0:
                                                        bm_1eee.faces.new([faaa1,fbbb1,fccc1])
                                                        bm_1eee.faces.new([fbbb1,fccc1,fddd1])
                                                        bm_1eee.faces.new([feee1,ffff1,fggg1])
                                                        bm_1eee.faces.new([ffff1,fggg1,fhhh1])
                                                        bm_1eee.faces.new([fggg1,fhhh1,fiii1])
                                                        

                    if type11 == 1:
                        if type21 == 1:
                            if type31 == 0:
                                if type41 == 1:
                                    if type51 == 1:
                                        if type61 == 0:
                                            if type71 == 1:
                                                if type81 == 1:
                                                    if type91 == 0:
                                                        bm_1ee.faces.new([faa1,fbb1,fcc1])
                                                        bm_1ee.faces.new([fdd1,fee1,fff1])
                                                        bm_1ee.faces.new([fgg1,fhh1,fii1])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    if type9 == 0:
                                                        bm_1e.faces.new([fa1,fb1,fc1])
                                                        bm_1e.faces.new([fb1,fc1,fd1])
                                                        bm_1e.faces.new([fc1,fd1,fe1])
                                                        bm_1e.faces.new([fd1,fe1,ff1])
                                                        bm_1e.faces.new([fe1,ff1,fg1])
                                                        bm_1e.faces.new([ff1,fg1,fh1])
                                                        bm_1e.faces.new([fg1,fh1,fi1])

            elif vertexCount == 10:
                for i in range(vertexCount//10):
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
                    vx10 = unpack("<f", f.read(4))[0]
                    vy10 = unpack("<f", f.read(4))[0]
                    vz10 = unpack("<f", f.read(4))[0]
                    type10 = unpack("B", f.read(1))[0]
                    value10 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10 = unpack("<f", f.read(4))[0]
                    f.seek(-160,1)
                    
                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    vx21 = unpack("<f", f.read(4))[0]
                    vy21 = unpack("<f", f.read(4))[0]
                    vz21 = unpack("<f", f.read(4))[0]
                    type21 = unpack("B", f.read(1))[0]
                    value21 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw21 = unpack("<f", f.read(4))[0]
                    vx31 = unpack("<f", f.read(4))[0]
                    vy31 = unpack("<f", f.read(4))[0]
                    vz31 = unpack("<f", f.read(4))[0]
                    type31 = unpack("B", f.read(1))[0]
                    value31 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw31 = unpack("<f", f.read(4))[0]
                    vx41 = unpack("<f", f.read(4))[0]
                    vy41 = unpack("<f", f.read(4))[0]
                    vz41 = unpack("<f", f.read(4))[0]
                    type41 = unpack("B", f.read(1))[0]
                    value41 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw41 = unpack("<f", f.read(4))[0]
                    vx51 = unpack("<f", f.read(4))[0]
                    vy51 = unpack("<f", f.read(4))[0]
                    vz51 = unpack("<f", f.read(4))[0]
                    type51 = unpack("B", f.read(1))[0]
                    value51 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw51 = unpack("<f", f.read(4))[0]
                    vx61 = unpack("<f", f.read(4))[0]
                    vy61 = unpack("<f", f.read(4))[0]
                    vz61 = unpack("<f", f.read(4))[0]
                    type61 = unpack("B", f.read(1))[0]
                    value61 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw61 = unpack("<f", f.read(4))[0]
                    vx71 = unpack("<f", f.read(4))[0]
                    vy71 = unpack("<f", f.read(4))[0]
                    vz71 = unpack("<f", f.read(4))[0]
                    type71 = unpack("B", f.read(1))[0]
                    value71 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw71 = unpack("<f", f.read(4))[0]
                    vx81 = unpack("<f", f.read(4))[0]
                    vy81 = unpack("<f", f.read(4))[0]
                    vz81 = unpack("<f", f.read(4))[0]
                    type81 = unpack("B", f.read(1))[0]
                    value81 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw81 = unpack("<f", f.read(4))[0]
                    vx91 = unpack("<f", f.read(4))[0]
                    vy91 = unpack("<f", f.read(4))[0]
                    vz91 = unpack("<f", f.read(4))[0]
                    type91 = unpack("B", f.read(1))[0]
                    value91 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw91 = unpack("<f", f.read(4))[0]
                    vx101 = unpack("<f", f.read(4))[0]
                    vy101 = unpack("<f", f.read(4))[0]
                    vz101 = unpack("<f", f.read(4))[0]
                    type101 = unpack("B", f.read(1))[0]
                    value101 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw101 = unpack("<f", f.read(4))[0]

                    f.seek(-160,1)
                    
                    vx111 = unpack("<f", f.read(4))[0]
                    vy111 = unpack("<f", f.read(4))[0]
                    vz111 = unpack("<f", f.read(4))[0]
                    type111 = unpack("B", f.read(1))[0]
                    value111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw111 = unpack("<f", f.read(4))[0]
                    vx211 = unpack("<f", f.read(4))[0]
                    vy211 = unpack("<f", f.read(4))[0]
                    vz211 = unpack("<f", f.read(4))[0]
                    type211 = unpack("B", f.read(1))[0]
                    value211 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw211 = unpack("<f", f.read(4))[0]
                    vx311 = unpack("<f", f.read(4))[0]
                    vy311 = unpack("<f", f.read(4))[0]
                    vz311 = unpack("<f", f.read(4))[0]
                    type311 = unpack("B", f.read(1))[0]
                    value311 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw311 = unpack("<f", f.read(4))[0]
                    vx411 = unpack("<f", f.read(4))[0]
                    vy411 = unpack("<f", f.read(4))[0]
                    vz411 = unpack("<f", f.read(4))[0]
                    type411 = unpack("B", f.read(1))[0]
                    value411 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw411 = unpack("<f", f.read(4))[0]
                    vx511 = unpack("<f", f.read(4))[0]
                    vy511 = unpack("<f", f.read(4))[0]
                    vz511 = unpack("<f", f.read(4))[0]
                    type511 = unpack("B", f.read(1))[0]
                    value511 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw511 = unpack("<f", f.read(4))[0]
                    vx611 = unpack("<f", f.read(4))[0]
                    vy611 = unpack("<f", f.read(4))[0]
                    vz611 = unpack("<f", f.read(4))[0]
                    type611 = unpack("B", f.read(1))[0]
                    value611 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw611 = unpack("<f", f.read(4))[0]
                    vx711 = unpack("<f", f.read(4))[0]
                    vy711 = unpack("<f", f.read(4))[0]
                    vz711 = unpack("<f", f.read(4))[0]
                    type711 = unpack("B", f.read(1))[0]
                    value711 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw711 = unpack("<f", f.read(4))[0]
                    vx811 = unpack("<f", f.read(4))[0]
                    vy811 = unpack("<f", f.read(4))[0]
                    vz811 = unpack("<f", f.read(4))[0]
                    type811 = unpack("B", f.read(1))[0]
                    value811 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw811 = unpack("<f", f.read(4))[0]
                    vx911 = unpack("<f", f.read(4))[0]
                    vy911 = unpack("<f", f.read(4))[0]
                    vz911 = unpack("<f", f.read(4))[0]
                    type911 = unpack("B", f.read(1))[0]
                    value911 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw911 = unpack("<f", f.read(4))[0]
                    vx1011 = unpack("<f", f.read(4))[0]
                    vy1011 = unpack("<f", f.read(4))[0]
                    vz1011 = unpack("<f", f.read(4))[0]
                    type1011 = unpack("B", f.read(1))[0]
                    value1011 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1011 = unpack("<f", f.read(4))[0]
                    
                    fa1 = bm_1f.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1f.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1f.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1f.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1f.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1f.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1f.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1f.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1f.verts.new([-vx9,-vy9,-vz9]) # 8
                    fj1 = bm_1f.verts.new([-vx10,-vy10,-vz10]) # 9

                    fa1a = bm_1ff.verts.new([-vx11,-vy11,-vz11]) # 0
                    fb1a = bm_1ff.verts.new([-vx21,-vy21,-vz21]) # 1
                    fc1a = bm_1ff.verts.new([-vx31,-vy31,-vz31]) # 2
                    fd1a = bm_1ff.verts.new([-vx41,-vy41,-vz41]) # 3
                    fe1a = bm_1ff.verts.new([-vx51,-vy51,-vz51]) # 4
                    ff1a = bm_1ff.verts.new([-vx61,-vy61,-vz61]) # 5
                    fg1a = bm_1ff.verts.new([-vx71,-vy71,-vz71]) # 6
                    fh1a = bm_1ff.verts.new([-vx81,-vy81,-vz81]) # 7
                    fi1a = bm_1ff.verts.new([-vx91,-vy91,-vz91]) # 8
                    fj1a = bm_1ff.verts.new([-vx101,-vy101,-vz101]) # 9

                    fa1b = bm_1fff.verts.new([-vx111,-vy111,-vz111]) # 0
                    fb1b = bm_1fff.verts.new([-vx211,-vy211,-vz211]) # 1
                    fc1b = bm_1fff.verts.new([-vx311,-vy311,-vz311]) # 2
                    fd1b = bm_1fff.verts.new([-vx411,-vy411,-vz411]) # 3
                    fe1b = bm_1fff.verts.new([-vx511,-vy511,-vz511]) # 4
                    ff1b = bm_1fff.verts.new([-vx611,-vy611,-vz611]) # 5
                    fg1b = bm_1fff.verts.new([-vx711,-vy711,-vz711]) # 6
                    fh1b = bm_1fff.verts.new([-vx811,-vy811,-vz811]) # 7
                    fi1b = bm_1fff.verts.new([-vx911,-vy911,-vz911]) # 8
                    fj1b = bm_1fff.verts.new([-vx1011,-vy1011,-vz1011]) # 9
                    if type111 == 1:
                        if type211 == 1:
                            if type311 == 0:
                                if type411 == 0:
                                    if type511 == 1:
                                        if type611 == 1:
                                            if type711 == 0:
                                                if type811 == 1:
                                                    if type911 == 1:
                                                        if type1011 == 0:
                                                            bm_1fff.faces.new([fa1b,fb1b,fc1b]) # 0 1 2
                                                            bm_1fff.faces.new([fb1b,fc1b,fd1b]) # 1 2 3
                                                            bm_1fff.faces.new([fe1b,ff1b,fg1b]) # 4 5 6
                                                            bm_1fff.faces.new([fh1b,fi1b,fj1b]) # 8,9,10
                                                            
                    if type11 == 1:
                        if type21 == 1:
                            if type31 == 0:
                                if type41 == 1:
                                    if type51 == 1:
                                        if type61 == 0:
                                            if type71 == 0:
                                                if type81 == 0:
                                                    if type91 == 0:
                                                        if type101 == 0:
                                                            bm_1ff.faces.new([fa1a,fb1a,fc1a])
                                                            bm_1ff.faces.new([fd1a,fe1a,ff1a])
                                                            bm_1ff.faces.new([fe1a,ff1a,fg1a])
                                                            bm_1ff.faces.new([ff1a,fg1a,fh1a])
                                                            bm_1ff.faces.new([fg1a,fh1a,fi1a])
                                                            bm_1ff.faces.new([fh1a,fi1a,fj1a])
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    if type9 == 0:
                                                        if type10 == 0:
                                                            bm_1f.faces.new([fa1,fb1,fc1])
                                                            bm_1f.faces.new([fb1,fc1,fd1])
                                                            bm_1f.faces.new([fc1,fd1,fe1])
                                                            bm_1f.faces.new([fd1,fe1,ff1])
                                                            bm_1f.faces.new([fe1,ff1,fg1])
                                                            bm_1f.faces.new([ff1,fg1,fh1])
                                                            bm_1f.faces.new([fg1,fh1,fi1])
                                                            bm_1f.faces.new([fh1,fi1,fj1])

            elif vertexCount == 11:
                for i in range(vertexCount//11):
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
                    vx10 = unpack("<f", f.read(4))[0]
                    vy10 = unpack("<f", f.read(4))[0]
                    vz10 = unpack("<f", f.read(4))[0]
                    type10 = unpack("B", f.read(1))[0]
                    value10 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10 = unpack("<f", f.read(4))[0]
                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    f.seek(-176,1)

                    vx12 = unpack("<f", f.read(4))[0]
                    vy12 = unpack("<f", f.read(4))[0]
                    vz12 = unpack("<f", f.read(4))[0]
                    type12 = unpack("B", f.read(1))[0]
                    value12 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12 = unpack("<f", f.read(4))[0]
                    vx22 = unpack("<f", f.read(4))[0]
                    vy22 = unpack("<f", f.read(4))[0]
                    vz22 = unpack("<f", f.read(4))[0]
                    type22 = unpack("B", f.read(1))[0]
                    value22 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw22 = unpack("<f", f.read(4))[0]
                    vx32 = unpack("<f", f.read(4))[0]
                    vy32 = unpack("<f", f.read(4))[0]
                    vz32 = unpack("<f", f.read(4))[0]
                    type32 = unpack("B", f.read(1))[0]
                    value32 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw32 = unpack("<f", f.read(4))[0]
                    vx42 = unpack("<f", f.read(4))[0]
                    vy42 = unpack("<f", f.read(4))[0]
                    vz42 = unpack("<f", f.read(4))[0]
                    type42 = unpack("B", f.read(1))[0]
                    value42 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw42 = unpack("<f", f.read(4))[0]
                    vx52 = unpack("<f", f.read(4))[0]
                    vy52 = unpack("<f", f.read(4))[0]
                    vz52 = unpack("<f", f.read(4))[0]
                    type52 = unpack("B", f.read(1))[0]
                    value52 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw52 = unpack("<f", f.read(4))[0]
                    vx62 = unpack("<f", f.read(4))[0]
                    vy62 = unpack("<f", f.read(4))[0]
                    vz62 = unpack("<f", f.read(4))[0]
                    type62 = unpack("B", f.read(1))[0]
                    value62 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw62 = unpack("<f", f.read(4))[0]
                    vx72 = unpack("<f", f.read(4))[0]
                    vy72 = unpack("<f", f.read(4))[0]
                    vz72 = unpack("<f", f.read(4))[0]
                    type72 = unpack("B", f.read(1))[0]
                    value72 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw72 = unpack("<f", f.read(4))[0]
                    vx82 = unpack("<f", f.read(4))[0]
                    vy82 = unpack("<f", f.read(4))[0]
                    vz82 = unpack("<f", f.read(4))[0]
                    type82 = unpack("B", f.read(1))[0]
                    value82 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw82 = unpack("<f", f.read(4))[0]
                    vx92 = unpack("<f", f.read(4))[0]
                    vy92 = unpack("<f", f.read(4))[0]
                    vz92 = unpack("<f", f.read(4))[0]
                    type92 = unpack("B", f.read(1))[0]
                    value92 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw92 = unpack("<f", f.read(4))[0]
                    vx102 = unpack("<f", f.read(4))[0]
                    vy102 = unpack("<f", f.read(4))[0]
                    vz102 = unpack("<f", f.read(4))[0]
                    type102 = unpack("B", f.read(1))[0]
                    value102 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw102 = unpack("<f", f.read(4))[0]
                    vx112 = unpack("<f", f.read(4))[0]
                    vy112 = unpack("<f", f.read(4))[0]
                    vz112 = unpack("<f", f.read(4))[0]
                    type112 = unpack("B", f.read(1))[0]
                    value112 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw112 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx122 = unpack("<f", f.read(4))[0]
                    vy122 = unpack("<f", f.read(4))[0]
                    vz122 = unpack("<f", f.read(4))[0]
                    type122 = unpack("B", f.read(1))[0]
                    value122 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw122 = unpack("<f", f.read(4))[0]
                    vx222 = unpack("<f", f.read(4))[0]
                    vy222 = unpack("<f", f.read(4))[0]
                    vz222 = unpack("<f", f.read(4))[0]
                    type222 = unpack("B", f.read(1))[0]
                    value222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw222 = unpack("<f", f.read(4))[0]
                    vx322 = unpack("<f", f.read(4))[0]
                    vy322 = unpack("<f", f.read(4))[0]
                    vz322 = unpack("<f", f.read(4))[0]
                    type322 = unpack("B", f.read(1))[0]
                    value322 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw322 = unpack("<f", f.read(4))[0]
                    vx422 = unpack("<f", f.read(4))[0]
                    vy422 = unpack("<f", f.read(4))[0]
                    vz422 = unpack("<f", f.read(4))[0]
                    type422 = unpack("B", f.read(1))[0]
                    value422 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw422 = unpack("<f", f.read(4))[0]
                    vx522 = unpack("<f", f.read(4))[0]
                    vy522 = unpack("<f", f.read(4))[0]
                    vz522 = unpack("<f", f.read(4))[0]
                    type522 = unpack("B", f.read(1))[0]
                    value522 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw522 = unpack("<f", f.read(4))[0]
                    vx622 = unpack("<f", f.read(4))[0]
                    vy622 = unpack("<f", f.read(4))[0]
                    vz622 = unpack("<f", f.read(4))[0]
                    type622 = unpack("B", f.read(1))[0]
                    value622 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw622 = unpack("<f", f.read(4))[0]
                    vx722 = unpack("<f", f.read(4))[0]
                    vy722 = unpack("<f", f.read(4))[0]
                    vz722 = unpack("<f", f.read(4))[0]
                    type722 = unpack("B", f.read(1))[0]
                    value722 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw722 = unpack("<f", f.read(4))[0]
                    vx822 = unpack("<f", f.read(4))[0]
                    vy822 = unpack("<f", f.read(4))[0]
                    vz822 = unpack("<f", f.read(4))[0]
                    type822 = unpack("B", f.read(1))[0]
                    value822 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw822 = unpack("<f", f.read(4))[0]
                    vx922 = unpack("<f", f.read(4))[0]
                    vy922 = unpack("<f", f.read(4))[0]
                    vz922 = unpack("<f", f.read(4))[0]
                    type922 = unpack("B", f.read(1))[0]
                    value922 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw922 = unpack("<f", f.read(4))[0]
                    vx1022 = unpack("<f", f.read(4))[0]
                    vy1022 = unpack("<f", f.read(4))[0]
                    vz1022 = unpack("<f", f.read(4))[0]
                    type1022 = unpack("B", f.read(1))[0]
                    value1022 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1022 = unpack("<f", f.read(4))[0]
                    vx1122 = unpack("<f", f.read(4))[0]
                    vy1122 = unpack("<f", f.read(4))[0]
                    vz1122 = unpack("<f", f.read(4))[0]
                    type1122 = unpack("B", f.read(1))[0]
                    value1122 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1122 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)



                    vx1222 = unpack("<f", f.read(4))[0]
                    vy1222 = unpack("<f", f.read(4))[0]
                    vz1222 = unpack("<f", f.read(4))[0]
                    type1222 = unpack("B", f.read(1))[0]
                    value1222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1222 = unpack("<f", f.read(4))[0]
                    vx2222 = unpack("<f", f.read(4))[0]
                    vy2222 = unpack("<f", f.read(4))[0]
                    vz2222 = unpack("<f", f.read(4))[0]
                    type2222 = unpack("B", f.read(1))[0]
                    value2222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2222 = unpack("<f", f.read(4))[0]
                    vx3222 = unpack("<f", f.read(4))[0]
                    vy3222 = unpack("<f", f.read(4))[0]
                    vz3222 = unpack("<f", f.read(4))[0]
                    type3222 = unpack("B", f.read(1))[0]
                    value3222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3222 = unpack("<f", f.read(4))[0]
                    vx4222 = unpack("<f", f.read(4))[0]
                    vy4222 = unpack("<f", f.read(4))[0]
                    vz4222 = unpack("<f", f.read(4))[0]
                    type4222 = unpack("B", f.read(1))[0]
                    value4222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4222 = unpack("<f", f.read(4))[0]
                    vx5222 = unpack("<f", f.read(4))[0]
                    vy5222 = unpack("<f", f.read(4))[0]
                    vz5222 = unpack("<f", f.read(4))[0]
                    type5222 = unpack("B", f.read(1))[0]
                    value5222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5222 = unpack("<f", f.read(4))[0]
                    vx6222 = unpack("<f", f.read(4))[0]
                    vy6222 = unpack("<f", f.read(4))[0]
                    vz6222 = unpack("<f", f.read(4))[0]
                    type6222 = unpack("B", f.read(1))[0]
                    value6222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6222 = unpack("<f", f.read(4))[0]
                    vx7222 = unpack("<f", f.read(4))[0]
                    vy7222 = unpack("<f", f.read(4))[0]
                    vz7222 = unpack("<f", f.read(4))[0]
                    type7222 = unpack("B", f.read(1))[0]
                    value7222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7222 = unpack("<f", f.read(4))[0]
                    vx8222 = unpack("<f", f.read(4))[0]
                    vy8222 = unpack("<f", f.read(4))[0]
                    vz8222 = unpack("<f", f.read(4))[0]
                    type8222 = unpack("B", f.read(1))[0]
                    value8222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8222 = unpack("<f", f.read(4))[0]
                    vx9222 = unpack("<f", f.read(4))[0]
                    vy9222 = unpack("<f", f.read(4))[0]
                    vz9222 = unpack("<f", f.read(4))[0]
                    type9222 = unpack("B", f.read(1))[0]
                    value9222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9222 = unpack("<f", f.read(4))[0]
                    vx10222 = unpack("<f", f.read(4))[0]
                    vy10222 = unpack("<f", f.read(4))[0]
                    vz10222 = unpack("<f", f.read(4))[0]
                    type10222 = unpack("B", f.read(1))[0]
                    value10222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10222 = unpack("<f", f.read(4))[0]
                    vx11222 = unpack("<f", f.read(4))[0]
                    vy11222 = unpack("<f", f.read(4))[0]
                    vz11222 = unpack("<f", f.read(4))[0]
                    type11222 = unpack("B", f.read(1))[0]
                    value11222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11222 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx12222 = unpack("<f", f.read(4))[0]
                    vy12222 = unpack("<f", f.read(4))[0]
                    vz12222 = unpack("<f", f.read(4))[0]
                    type12222 = unpack("B", f.read(1))[0]
                    value12222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12222 = unpack("<f", f.read(4))[0]
                    vx22222 = unpack("<f", f.read(4))[0]
                    vy22222 = unpack("<f", f.read(4))[0]
                    vz22222 = unpack("<f", f.read(4))[0]
                    type22222 = unpack("B", f.read(1))[0]
                    value22222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw22222 = unpack("<f", f.read(4))[0]
                    vx32222 = unpack("<f", f.read(4))[0]
                    vy32222 = unpack("<f", f.read(4))[0]
                    vz32222 = unpack("<f", f.read(4))[0]
                    type32222 = unpack("B", f.read(1))[0]
                    value32222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw32222 = unpack("<f", f.read(4))[0]
                    vx42222 = unpack("<f", f.read(4))[0]
                    vy42222 = unpack("<f", f.read(4))[0]
                    vz42222 = unpack("<f", f.read(4))[0]
                    type42222 = unpack("B", f.read(1))[0]
                    value42222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw42222 = unpack("<f", f.read(4))[0]
                    vx52222 = unpack("<f", f.read(4))[0]
                    vy52222 = unpack("<f", f.read(4))[0]
                    vz52222 = unpack("<f", f.read(4))[0]
                    type52222 = unpack("B", f.read(1))[0]
                    value52222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw52222 = unpack("<f", f.read(4))[0]
                    vx62222 = unpack("<f", f.read(4))[0]
                    vy62222 = unpack("<f", f.read(4))[0]
                    vz62222 = unpack("<f", f.read(4))[0]
                    type62222 = unpack("B", f.read(1))[0]
                    value62222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw62222 = unpack("<f", f.read(4))[0]
                    vx72222 = unpack("<f", f.read(4))[0]
                    vy72222 = unpack("<f", f.read(4))[0]
                    vz72222 = unpack("<f", f.read(4))[0]
                    type72222 = unpack("B", f.read(1))[0]
                    value72222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw72222 = unpack("<f", f.read(4))[0]
                    vx82222 = unpack("<f", f.read(4))[0]
                    vy82222 = unpack("<f", f.read(4))[0]
                    vz82222 = unpack("<f", f.read(4))[0]
                    type82222 = unpack("B", f.read(1))[0]
                    value82222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw82222 = unpack("<f", f.read(4))[0]
                    vx92222 = unpack("<f", f.read(4))[0]
                    vy92222 = unpack("<f", f.read(4))[0]
                    vz92222 = unpack("<f", f.read(4))[0]
                    type92222 = unpack("B", f.read(1))[0]
                    value92222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw92222 = unpack("<f", f.read(4))[0]
                    vx102222 = unpack("<f", f.read(4))[0]
                    vy102222 = unpack("<f", f.read(4))[0]
                    vz102222 = unpack("<f", f.read(4))[0]
                    type102222 = unpack("B", f.read(1))[0]
                    value102222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw102222 = unpack("<f", f.read(4))[0]
                    vx112222 = unpack("<f", f.read(4))[0]
                    vy112222 = unpack("<f", f.read(4))[0]
                    vz112222 = unpack("<f", f.read(4))[0]
                    type112222 = unpack("B", f.read(1))[0]
                    value112222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw112222 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx122222 = unpack("<f", f.read(4))[0]
                    vy122222 = unpack("<f", f.read(4))[0]
                    vz122222 = unpack("<f", f.read(4))[0]
                    type122222 = unpack("B", f.read(1))[0]
                    value122222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw122222 = unpack("<f", f.read(4))[0]
                    vx222222 = unpack("<f", f.read(4))[0]
                    vy222222 = unpack("<f", f.read(4))[0]
                    vz222222 = unpack("<f", f.read(4))[0]
                    type222222 = unpack("B", f.read(1))[0]
                    value222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw222222 = unpack("<f", f.read(4))[0]
                    vx322222 = unpack("<f", f.read(4))[0]
                    vy322222 = unpack("<f", f.read(4))[0]
                    vz322222 = unpack("<f", f.read(4))[0]
                    type322222 = unpack("B", f.read(1))[0]
                    value322222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw322222 = unpack("<f", f.read(4))[0]
                    vx422222 = unpack("<f", f.read(4))[0]
                    vy422222 = unpack("<f", f.read(4))[0]
                    vz422222 = unpack("<f", f.read(4))[0]
                    type422222 = unpack("B", f.read(1))[0]
                    value422222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw422222 = unpack("<f", f.read(4))[0]
                    vx522222 = unpack("<f", f.read(4))[0]
                    vy522222 = unpack("<f", f.read(4))[0]
                    vz522222 = unpack("<f", f.read(4))[0]
                    type522222 = unpack("B", f.read(1))[0]
                    value522222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw522222 = unpack("<f", f.read(4))[0]
                    vx622222 = unpack("<f", f.read(4))[0]
                    vy622222 = unpack("<f", f.read(4))[0]
                    vz622222 = unpack("<f", f.read(4))[0]
                    type622222 = unpack("B", f.read(1))[0]
                    value622222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw622222 = unpack("<f", f.read(4))[0]
                    vx722222 = unpack("<f", f.read(4))[0]
                    vy722222 = unpack("<f", f.read(4))[0]
                    vz722222 = unpack("<f", f.read(4))[0]
                    type722222 = unpack("B", f.read(1))[0]
                    value722222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw722222 = unpack("<f", f.read(4))[0]
                    vx822222 = unpack("<f", f.read(4))[0]
                    vy822222 = unpack("<f", f.read(4))[0]
                    vz822222 = unpack("<f", f.read(4))[0]
                    type822222 = unpack("B", f.read(1))[0]
                    value822222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw822222 = unpack("<f", f.read(4))[0]
                    vx922222 = unpack("<f", f.read(4))[0]
                    vy922222 = unpack("<f", f.read(4))[0]
                    vz922222 = unpack("<f", f.read(4))[0]
                    type922222 = unpack("B", f.read(1))[0]
                    value922222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw922222 = unpack("<f", f.read(4))[0]
                    vx1022222 = unpack("<f", f.read(4))[0]
                    vy1022222 = unpack("<f", f.read(4))[0]
                    vz1022222 = unpack("<f", f.read(4))[0]
                    type1022222 = unpack("B", f.read(1))[0]
                    value1022222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1022222 = unpack("<f", f.read(4))[0]
                    vx1122222 = unpack("<f", f.read(4))[0]
                    vy1122222 = unpack("<f", f.read(4))[0]
                    vz1122222 = unpack("<f", f.read(4))[0]
                    type1122222 = unpack("B", f.read(1))[0]
                    value1122222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1122222 = unpack("<f", f.read(4))[0]



                    f.seek(-176,1)

                    vx1222222 = unpack("<f", f.read(4))[0]
                    vy1222222 = unpack("<f", f.read(4))[0]
                    vz1222222 = unpack("<f", f.read(4))[0]
                    type1222222 = unpack("B", f.read(1))[0]
                    value1222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1222222 = unpack("<f", f.read(4))[0]
                    vx2222222 = unpack("<f", f.read(4))[0]
                    vy2222222 = unpack("<f", f.read(4))[0]
                    vz2222222 = unpack("<f", f.read(4))[0]
                    type2222222 = unpack("B", f.read(1))[0]
                    value2222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2222222 = unpack("<f", f.read(4))[0]
                    vx3222222 = unpack("<f", f.read(4))[0]
                    vy3222222 = unpack("<f", f.read(4))[0]
                    vz3222222 = unpack("<f", f.read(4))[0]
                    type3222222 = unpack("B", f.read(1))[0]
                    value3222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3222222 = unpack("<f", f.read(4))[0]
                    vx4222222 = unpack("<f", f.read(4))[0]
                    vy4222222 = unpack("<f", f.read(4))[0]
                    vz4222222 = unpack("<f", f.read(4))[0]
                    type4222222 = unpack("B", f.read(1))[0]
                    value4222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4222222 = unpack("<f", f.read(4))[0]
                    vx5222222 = unpack("<f", f.read(4))[0]
                    vy5222222 = unpack("<f", f.read(4))[0]
                    vz5222222 = unpack("<f", f.read(4))[0]
                    type5222222 = unpack("B", f.read(1))[0]
                    value5222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5222222 = unpack("<f", f.read(4))[0]
                    vx6222222 = unpack("<f", f.read(4))[0]
                    vy6222222 = unpack("<f", f.read(4))[0]
                    vz6222222 = unpack("<f", f.read(4))[0]
                    type6222222 = unpack("B", f.read(1))[0]
                    value6222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6222222 = unpack("<f", f.read(4))[0]
                    vx7222222 = unpack("<f", f.read(4))[0]
                    vy7222222 = unpack("<f", f.read(4))[0]
                    vz7222222 = unpack("<f", f.read(4))[0]
                    type7222222 = unpack("B", f.read(1))[0]
                    value7222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7222222 = unpack("<f", f.read(4))[0]
                    vx8222222 = unpack("<f", f.read(4))[0]
                    vy8222222 = unpack("<f", f.read(4))[0]
                    vz8222222 = unpack("<f", f.read(4))[0]
                    type8222222 = unpack("B", f.read(1))[0]
                    value8222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8222222 = unpack("<f", f.read(4))[0]
                    vx9222222 = unpack("<f", f.read(4))[0]
                    vy9222222 = unpack("<f", f.read(4))[0]
                    vz9222222 = unpack("<f", f.read(4))[0]
                    type9222222 = unpack("B", f.read(1))[0]
                    value9222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9222222 = unpack("<f", f.read(4))[0]
                    vx10222222 = unpack("<f", f.read(4))[0]
                    vy10222222 = unpack("<f", f.read(4))[0]
                    vz10222222 = unpack("<f", f.read(4))[0]
                    type10222222 = unpack("B", f.read(1))[0]
                    value10222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10222222 = unpack("<f", f.read(4))[0]
                    vx11222222 = unpack("<f", f.read(4))[0]
                    vy11222222 = unpack("<f", f.read(4))[0]
                    vz11222222 = unpack("<f", f.read(4))[0]
                    type11222222 = unpack("B", f.read(1))[0]
                    value11222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11222222 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx12222222 = unpack("<f", f.read(4))[0]
                    vy12222222 = unpack("<f", f.read(4))[0]
                    vz12222222 = unpack("<f", f.read(4))[0]
                    type12222222 = unpack("B", f.read(1))[0]
                    value12222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12222222 = unpack("<f", f.read(4))[0]
                    vx22222222 = unpack("<f", f.read(4))[0]
                    vy22222222 = unpack("<f", f.read(4))[0]
                    vz22222222 = unpack("<f", f.read(4))[0]
                    type22222222 = unpack("B", f.read(1))[0]
                    value22222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw22222222 = unpack("<f", f.read(4))[0]
                    vx32222222 = unpack("<f", f.read(4))[0]
                    vy32222222 = unpack("<f", f.read(4))[0]
                    vz32222222 = unpack("<f", f.read(4))[0]
                    type32222222 = unpack("B", f.read(1))[0]
                    value32222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw32222222 = unpack("<f", f.read(4))[0]
                    vx42222222 = unpack("<f", f.read(4))[0]
                    vy42222222 = unpack("<f", f.read(4))[0]
                    vz42222222 = unpack("<f", f.read(4))[0]
                    type42222222 = unpack("B", f.read(1))[0]
                    value42222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw42222222 = unpack("<f", f.read(4))[0]
                    vx52222222 = unpack("<f", f.read(4))[0]
                    vy52222222 = unpack("<f", f.read(4))[0]
                    vz52222222 = unpack("<f", f.read(4))[0]
                    type52222222 = unpack("B", f.read(1))[0]
                    value52222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw52222222 = unpack("<f", f.read(4))[0]
                    vx62222222 = unpack("<f", f.read(4))[0]
                    vy62222222 = unpack("<f", f.read(4))[0]
                    vz62222222 = unpack("<f", f.read(4))[0]
                    type62222222 = unpack("B", f.read(1))[0]
                    value62222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw62222222 = unpack("<f", f.read(4))[0]
                    vx72222222 = unpack("<f", f.read(4))[0]
                    vy72222222 = unpack("<f", f.read(4))[0]
                    vz72222222 = unpack("<f", f.read(4))[0]
                    type72222222 = unpack("B", f.read(1))[0]
                    value72222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw72222222 = unpack("<f", f.read(4))[0]
                    vx82222222 = unpack("<f", f.read(4))[0]
                    vy82222222 = unpack("<f", f.read(4))[0]
                    vz82222222 = unpack("<f", f.read(4))[0]
                    type82222222 = unpack("B", f.read(1))[0]
                    value82222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw82222222 = unpack("<f", f.read(4))[0]
                    vx92222222 = unpack("<f", f.read(4))[0]
                    vy92222222 = unpack("<f", f.read(4))[0]
                    vz92222222 = unpack("<f", f.read(4))[0]
                    type92222222 = unpack("B", f.read(1))[0]
                    value92222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw92222222 = unpack("<f", f.read(4))[0]
                    vx102222222 = unpack("<f", f.read(4))[0]
                    vy102222222 = unpack("<f", f.read(4))[0]
                    vz102222222 = unpack("<f", f.read(4))[0]
                    type102222222 = unpack("B", f.read(1))[0]
                    value102222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw102222222 = unpack("<f", f.read(4))[0]
                    vx112222222 = unpack("<f", f.read(4))[0]
                    vy112222222 = unpack("<f", f.read(4))[0]
                    vz112222222 = unpack("<f", f.read(4))[0]
                    type112222222 = unpack("B", f.read(1))[0]
                    value112222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw112222222 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx122222222 = unpack("<f", f.read(4))[0]
                    vy122222222 = unpack("<f", f.read(4))[0]
                    vz122222222 = unpack("<f", f.read(4))[0]
                    type122222222 = unpack("B", f.read(1))[0]
                    value122222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw122222222 = unpack("<f", f.read(4))[0]
                    vx222222222 = unpack("<f", f.read(4))[0]
                    vy222222222 = unpack("<f", f.read(4))[0]
                    vz222222222 = unpack("<f", f.read(4))[0]
                    type222222222 = unpack("B", f.read(1))[0]
                    value222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw222222222 = unpack("<f", f.read(4))[0]
                    vx322222222 = unpack("<f", f.read(4))[0]
                    vy322222222 = unpack("<f", f.read(4))[0]
                    vz322222222 = unpack("<f", f.read(4))[0]
                    type322222222 = unpack("B", f.read(1))[0]
                    value322222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw322222222 = unpack("<f", f.read(4))[0]
                    vx422222222 = unpack("<f", f.read(4))[0]
                    vy422222222 = unpack("<f", f.read(4))[0]
                    vz422222222 = unpack("<f", f.read(4))[0]
                    type422222222 = unpack("B", f.read(1))[0]
                    value422222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw422222222 = unpack("<f", f.read(4))[0]
                    vx522222222 = unpack("<f", f.read(4))[0]
                    vy522222222 = unpack("<f", f.read(4))[0]
                    vz522222222 = unpack("<f", f.read(4))[0]
                    type522222222 = unpack("B", f.read(1))[0]
                    value522222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw522222222 = unpack("<f", f.read(4))[0]
                    vx622222222 = unpack("<f", f.read(4))[0]
                    vy622222222 = unpack("<f", f.read(4))[0]
                    vz622222222 = unpack("<f", f.read(4))[0]
                    type622222222 = unpack("B", f.read(1))[0]
                    value622222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw622222222 = unpack("<f", f.read(4))[0]
                    vx722222222 = unpack("<f", f.read(4))[0]
                    vy722222222 = unpack("<f", f.read(4))[0]
                    vz722222222 = unpack("<f", f.read(4))[0]
                    type722222222 = unpack("B", f.read(1))[0]
                    value722222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw722222222 = unpack("<f", f.read(4))[0]
                    vx822222222 = unpack("<f", f.read(4))[0]
                    vy822222222 = unpack("<f", f.read(4))[0]
                    vz822222222 = unpack("<f", f.read(4))[0]
                    type822222222 = unpack("B", f.read(1))[0]
                    value822222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw822222222 = unpack("<f", f.read(4))[0]
                    vx922222222 = unpack("<f", f.read(4))[0]
                    vy922222222 = unpack("<f", f.read(4))[0]
                    vz922222222 = unpack("<f", f.read(4))[0]
                    type922222222 = unpack("B", f.read(1))[0]
                    value922222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw922222222 = unpack("<f", f.read(4))[0]
                    vx1022222222 = unpack("<f", f.read(4))[0]
                    vy1022222222 = unpack("<f", f.read(4))[0]
                    vz1022222222 = unpack("<f", f.read(4))[0]
                    type1022222222 = unpack("B", f.read(1))[0]
                    value1022222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1022222222 = unpack("<f", f.read(4))[0]
                    vx1122222222 = unpack("<f", f.read(4))[0]
                    vy1122222222 = unpack("<f", f.read(4))[0]
                    vz1122222222 = unpack("<f", f.read(4))[0]
                    type1122222222 = unpack("B", f.read(1))[0]
                    value1122222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1122222222 = unpack("<f", f.read(4))[0]

                    f.seek(-176,1)

                    vx1222222222 = unpack("<f", f.read(4))[0]
                    vy1222222222 = unpack("<f", f.read(4))[0]
                    vz1222222222 = unpack("<f", f.read(4))[0]
                    type1222222222 = unpack("B", f.read(1))[0]
                    value1222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1222222222 = unpack("<f", f.read(4))[0]
                    vx2222222222 = unpack("<f", f.read(4))[0]
                    vy2222222222 = unpack("<f", f.read(4))[0]
                    vz2222222222 = unpack("<f", f.read(4))[0]
                    type2222222222 = unpack("B", f.read(1))[0]
                    value2222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2222222222 = unpack("<f", f.read(4))[0]
                    vx3222222222 = unpack("<f", f.read(4))[0]
                    vy3222222222 = unpack("<f", f.read(4))[0]
                    vz3222222222 = unpack("<f", f.read(4))[0]
                    type3222222222 = unpack("B", f.read(1))[0]
                    value3222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3222222222 = unpack("<f", f.read(4))[0]
                    vx4222222222 = unpack("<f", f.read(4))[0]
                    vy4222222222 = unpack("<f", f.read(4))[0]
                    vz4222222222 = unpack("<f", f.read(4))[0]
                    type4222222222 = unpack("B", f.read(1))[0]
                    value4222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4222222222 = unpack("<f", f.read(4))[0]
                    vx5222222222 = unpack("<f", f.read(4))[0]
                    vy5222222222 = unpack("<f", f.read(4))[0]
                    vz5222222222 = unpack("<f", f.read(4))[0]
                    type5222222222 = unpack("B", f.read(1))[0]
                    value5222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5222222222 = unpack("<f", f.read(4))[0]
                    vx6222222222 = unpack("<f", f.read(4))[0]
                    vy6222222222 = unpack("<f", f.read(4))[0]
                    vz6222222222 = unpack("<f", f.read(4))[0]
                    type6222222222 = unpack("B", f.read(1))[0]
                    value6222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6222222222 = unpack("<f", f.read(4))[0]
                    vx7222222222 = unpack("<f", f.read(4))[0]
                    vy7222222222 = unpack("<f", f.read(4))[0]
                    vz7222222222 = unpack("<f", f.read(4))[0]
                    type7222222222 = unpack("B", f.read(1))[0]
                    value7222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7222222222 = unpack("<f", f.read(4))[0]
                    vx8222222222 = unpack("<f", f.read(4))[0]
                    vy8222222222 = unpack("<f", f.read(4))[0]
                    vz8222222222 = unpack("<f", f.read(4))[0]
                    type8222222222 = unpack("B", f.read(1))[0]
                    value8222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8222222222 = unpack("<f", f.read(4))[0]
                    vx9222222222 = unpack("<f", f.read(4))[0]
                    vy9222222222 = unpack("<f", f.read(4))[0]
                    vz9222222222 = unpack("<f", f.read(4))[0]
                    type9222222222 = unpack("B", f.read(1))[0]
                    value9222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9222222222 = unpack("<f", f.read(4))[0]
                    vx10222222222 = unpack("<f", f.read(4))[0]
                    vy10222222222 = unpack("<f", f.read(4))[0]
                    vz10222222222 = unpack("<f", f.read(4))[0]
                    type10222222222 = unpack("B", f.read(1))[0]
                    value10222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10222222222 = unpack("<f", f.read(4))[0]
                    vx11222222222 = unpack("<f", f.read(4))[0]
                    vy11222222222 = unpack("<f", f.read(4))[0]
                    vz11222222222 = unpack("<f", f.read(4))[0]
                    type11222222222 = unpack("B", f.read(1))[0]
                    value11222222222 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11222222222 = unpack("<f", f.read(4))[0]

                    fa1222222222 = bm_1gggggggggg.verts.new([-vx1222222222,-vy1222222222,-vz1222222222]) # 0
                    fb1222222222 = bm_1gggggggggg.verts.new([-vx2222222222,-vy2222222222,-vz2222222222]) # 1
                    fc1222222222 = bm_1gggggggggg.verts.new([-vx3222222222,-vy3222222222,-vz3222222222]) # 2
                    fd1222222222 = bm_1gggggggggg.verts.new([-vx4222222222,-vy4222222222,-vz4222222222]) # 3
                    fe1222222222 = bm_1gggggggggg.verts.new([-vx5222222222,-vy5222222222,-vz5222222222]) # 4
                    ff1222222222 = bm_1gggggggggg.verts.new([-vx6222222222,-vy6222222222,-vz6222222222]) # 5
                    fg1222222222 = bm_1gggggggggg.verts.new([-vx7222222222,-vy7222222222,-vz7222222222]) # 6
                    fh1222222222 = bm_1gggggggggg.verts.new([-vx8222222222,-vy8222222222,-vz8222222222]) # 7
                    fi1222222222 = bm_1gggggggggg.verts.new([-vx9222222222,-vy9222222222,-vz9222222222]) # 8
                    fj1222222222 = bm_1gggggggggg.verts.new([-vx10222222222,-vy10222222222,-vz10222222222]) # 9
                    fk1222222222 = bm_1gggggggggg.verts.new([-vx11222222222,-vy11222222222,-vz11222222222]) # 10

                    fa122222222 = bm_1ggggggggg.verts.new([-vx122222222,-vy122222222,-vz122222222]) # 0
                    fb122222222 = bm_1ggggggggg.verts.new([-vx222222222,-vy222222222,-vz222222222]) # 1
                    fc122222222 = bm_1ggggggggg.verts.new([-vx322222222,-vy322222222,-vz322222222]) # 2
                    fd122222222 = bm_1ggggggggg.verts.new([-vx422222222,-vy422222222,-vz422222222]) # 3
                    fe122222222 = bm_1ggggggggg.verts.new([-vx522222222,-vy522222222,-vz522222222]) # 4
                    ff122222222 = bm_1ggggggggg.verts.new([-vx622222222,-vy622222222,-vz622222222]) # 5
                    fg122222222 = bm_1ggggggggg.verts.new([-vx722222222,-vy722222222,-vz722222222]) # 6
                    fh122222222 = bm_1ggggggggg.verts.new([-vx822222222,-vy822222222,-vz822222222]) # 7
                    fi122222222 = bm_1ggggggggg.verts.new([-vx922222222,-vy922222222,-vz922222222]) # 8
                    fj122222222 = bm_1ggggggggg.verts.new([-vx1022222222,-vy1022222222,-vz1022222222]) # 9
                    fk122222222 = bm_1ggggggggg.verts.new([-vx1122222222,-vy1122222222,-vz1122222222]) # 10

                    fa12222222 = bm_1gggggggg.verts.new([-vx12222222,-vy12222222,-vz12222222]) # 0
                    fb12222222 = bm_1gggggggg.verts.new([-vx22222222,-vy22222222,-vz22222222]) # 1
                    fc12222222 = bm_1gggggggg.verts.new([-vx32222222,-vy32222222,-vz32222222]) # 2
                    fd12222222 = bm_1gggggggg.verts.new([-vx42222222,-vy42222222,-vz42222222]) # 3
                    fe12222222 = bm_1gggggggg.verts.new([-vx52222222,-vy52222222,-vz52222222]) # 4
                    ff12222222 = bm_1gggggggg.verts.new([-vx62222222,-vy62222222,-vz62222222]) # 5
                    fg12222222 = bm_1gggggggg.verts.new([-vx72222222,-vy72222222,-vz72222222]) # 6
                    fh12222222 = bm_1gggggggg.verts.new([-vx82222222,-vy82222222,-vz82222222]) # 7
                    fi12222222 = bm_1gggggggg.verts.new([-vx92222222,-vy92222222,-vz92222222]) # 8
                    fj12222222 = bm_1gggggggg.verts.new([-vx102222222,-vy102222222,-vz102222222]) # 9
                    fk12222222 = bm_1gggggggg.verts.new([-vx112222222,-vy112222222,-vz112222222]) # 10

                    fa1222222 = bm_1ggggggg.verts.new([-vx1222222,-vy1222222,-vz1222222]) # 0
                    fb1222222 = bm_1ggggggg.verts.new([-vx2222222,-vy2222222,-vz2222222]) # 1
                    fc1222222 = bm_1ggggggg.verts.new([-vx3222222,-vy3222222,-vz3222222]) # 2
                    fd1222222 = bm_1ggggggg.verts.new([-vx4222222,-vy4222222,-vz4222222]) # 3
                    fe1222222 = bm_1ggggggg.verts.new([-vx5222222,-vy5222222,-vz5222222]) # 4
                    ff1222222 = bm_1ggggggg.verts.new([-vx6222222,-vy6222222,-vz6222222]) # 5
                    fg1222222 = bm_1ggggggg.verts.new([-vx7222222,-vy7222222,-vz7222222]) # 6
                    fh1222222 = bm_1ggggggg.verts.new([-vx8222222,-vy8222222,-vz8222222]) # 7
                    fi1222222 = bm_1ggggggg.verts.new([-vx9222222,-vy9222222,-vz9222222]) # 8
                    fj1222222 = bm_1ggggggg.verts.new([-vx10222222,-vy10222222,-vz10222222]) # 9
                    fk1222222 = bm_1ggggggg.verts.new([-vx11222222,-vy11222222,-vz11222222]) # 10

                    fa122222 = bm_1gggggg.verts.new([-vx122222,-vy122222,-vz122222]) # 0
                    fb122222 = bm_1gggggg.verts.new([-vx222222,-vy222222,-vz222222]) # 1
                    fc122222 = bm_1gggggg.verts.new([-vx322222,-vy322222,-vz322222]) # 2
                    fd122222 = bm_1gggggg.verts.new([-vx422222,-vy422222,-vz422222]) # 3
                    fe122222 = bm_1gggggg.verts.new([-vx522222,-vy522222,-vz522222]) # 4
                    ff122222 = bm_1gggggg.verts.new([-vx622222,-vy622222,-vz622222]) # 5
                    fg122222 = bm_1gggggg.verts.new([-vx722222,-vy722222,-vz722222]) # 6
                    fh122222 = bm_1gggggg.verts.new([-vx822222,-vy822222,-vz822222]) # 7
                    fi122222 = bm_1gggggg.verts.new([-vx922222,-vy922222,-vz922222]) # 8
                    fj122222 = bm_1gggggg.verts.new([-vx1022222,-vy1022222,-vz1022222]) # 9
                    fk122222 = bm_1gggggg.verts.new([-vx1122222,-vy1122222,-vz1122222]) # 10



                    fa12222 = bm_1ggggg.verts.new([-vx12222,-vy12222,-vz12222]) # 0
                    fb12222 = bm_1ggggg.verts.new([-vx22222,-vy22222,-vz22222]) # 1
                    fc12222 = bm_1ggggg.verts.new([-vx32222,-vy32222,-vz32222]) # 2
                    fd12222 = bm_1ggggg.verts.new([-vx42222,-vy42222,-vz42222]) # 3
                    fe12222 = bm_1ggggg.verts.new([-vx52222,-vy52222,-vz52222]) # 4
                    ff12222 = bm_1ggggg.verts.new([-vx62222,-vy62222,-vz62222]) # 5
                    fg12222 = bm_1ggggg.verts.new([-vx72222,-vy72222,-vz72222]) # 6
                    fh12222 = bm_1ggggg.verts.new([-vx82222,-vy82222,-vz82222]) # 7
                    fi12222 = bm_1ggggg.verts.new([-vx92222,-vy92222,-vz92222]) # 8
                    fj12222 = bm_1ggggg.verts.new([-vx102222,-vy102222,-vz102222]) # 9
                    fk12222 = bm_1ggggg.verts.new([-vx112222,-vy112222,-vz112222]) # 10


                    fa1222 = bm_1gggg.verts.new([-vx1222,-vy1222,-vz1222]) # 0
                    fb1222 = bm_1gggg.verts.new([-vx2222,-vy2222,-vz2222]) # 1
                    fc1222 = bm_1gggg.verts.new([-vx3222,-vy3222,-vz3222]) # 2
                    fd1222 = bm_1gggg.verts.new([-vx4222,-vy4222,-vz4222]) # 3
                    fe1222 = bm_1gggg.verts.new([-vx5222,-vy5222,-vz5222]) # 4
                    ff1222 = bm_1gggg.verts.new([-vx6222,-vy6222,-vz6222]) # 5
                    fg1222 = bm_1gggg.verts.new([-vx7222,-vy7222,-vz7222]) # 6
                    fh1222 = bm_1gggg.verts.new([-vx8222,-vy8222,-vz8222]) # 7
                    fi1222 = bm_1gggg.verts.new([-vx9222,-vy9222,-vz9222]) # 8
                    fj1222 = bm_1gggg.verts.new([-vx10222,-vy10222,-vz10222]) # 9
                    fk1222 = bm_1gggg.verts.new([-vx11222,-vy11222,-vz11222]) # 10

                    fa122 = bm_1ggg.verts.new([-vx122,-vy122,-vz122]) # 0
                    fb122 = bm_1ggg.verts.new([-vx222,-vy222,-vz222]) # 1
                    fc122 = bm_1ggg.verts.new([-vx322,-vy322,-vz322]) # 2
                    fd122 = bm_1ggg.verts.new([-vx422,-vy422,-vz422]) # 3
                    fe122 = bm_1ggg.verts.new([-vx522,-vy522,-vz522]) # 4
                    ff122 = bm_1ggg.verts.new([-vx622,-vy622,-vz622]) # 5
                    fg122 = bm_1ggg.verts.new([-vx722,-vy722,-vz722]) # 6
                    fh122 = bm_1ggg.verts.new([-vx822,-vy822,-vz822]) # 7
                    fi122 = bm_1ggg.verts.new([-vx922,-vy922,-vz922]) # 8
                    fj122 = bm_1ggg.verts.new([-vx1022,-vy1022,-vz1022]) # 9
                    fk122 = bm_1ggg.verts.new([-vx1122,-vy1122,-vz1122]) # 10

                    fa12 = bm_1gg.verts.new([-vx12,-vy12,-vz12]) # 0
                    fb12 = bm_1gg.verts.new([-vx22,-vy22,-vz22]) # 1
                    fc12 = bm_1gg.verts.new([-vx32,-vy32,-vz32]) # 2
                    fd12 = bm_1gg.verts.new([-vx42,-vy42,-vz42]) # 3
                    fe12 = bm_1gg.verts.new([-vx52,-vy52,-vz52]) # 4
                    ff12 = bm_1gg.verts.new([-vx62,-vy62,-vz62]) # 5
                    fg12 = bm_1gg.verts.new([-vx72,-vy72,-vz72]) # 6
                    fh12 = bm_1gg.verts.new([-vx82,-vy82,-vz82]) # 7
                    fi12 = bm_1gg.verts.new([-vx92,-vy92,-vz92]) # 8
                    fj12 = bm_1gg.verts.new([-vx102,-vy102,-vz102]) # 9
                    fk12 = bm_1gg.verts.new([-vx112,-vy112,-vz112]) # 10
                    
                    fa1 = bm_1g.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1g.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1g.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1g.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1g.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1g.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1g.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1g.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1g.verts.new([-vx9,-vy9,-vz9]) # 8
                    fj1 = bm_1g.verts.new([-vx10,-vy10,-vz10]) # 9
                    fk1 = bm_1g.verts.new([-vx11,-vy11,-vz11]) # 10

                    if type1222222222 == 1:
                        if type2222222222 == 1:
                            if type3222222222 == 0:
                                if type4222222222 == 1:
                                    if type5222222222 == 1:
                                        if type6222222222 == 0:
                                            if type7222222222 == 0:
                                                if type8222222222 == 1:
                                                    if type9222222222 == 1:
                                                        if type10222222222 == 0:
                                                            if type11222222222 == 0:
                                                                bm_1gggggggggg.faces.new([fa122222222,fb122222222,fc122222222]) # 0 1 2
                                                                bm_1gggggggggg.faces.new([fd122222222,fe122222222,ff122222222]) # 3 4 5
                                                                bm_1gggggggggg.faces.new([fe122222222,ff122222222,fg122222222]) # 4 5 6
                                                                bm_1gggggggggg.faces.new([fh122222222,fi122222222,fj122222222]) # 7 8 9
                                                                bm_1gggggggggg.faces.new([fi122222222,fj122222222,fk122222222]) # 9 10 11
                                    

                    if type122222222 == 1:
                        if type222222222 == 1:
                            if type322222222 == 0:
                                if type422222222 == 0:
                                    if type522222222 == 1:
                                        if type622222222 == 1:
                                            if type722222222 == 0:
                                                if type822222222 == 0:
                                                    if type922222222 == 1:
                                                        if type1022222222 == 1:
                                                            if type1122222222 == 0:
                                                                bm_1ggggggggg.faces.new([fa122222222,fb122222222,fc122222222]) # 0 1 2
                                                                bm_1ggggggggg.faces.new([fb122222222,fc122222222,fd122222222]) # 1 2 3
                                                                bm_1ggggggggg.faces.new([fe122222222,ff122222222,fg122222222]) # 4 5 6
                                                                bm_1ggggggggg.faces.new([ff122222222,fg122222222,fh122222222]) # 7 8 9
                                                                bm_1ggggggggg.faces.new([fi122222222,fj122222222,fk122222222]) # 9 10 11

                    if type12222222 == 1:
                        if type22222222 == 1:
                            if type32222222 == 0:
                                if type42222222 == 1:
                                    if type52222222 == 1:
                                        if type62222222 == 0:
                                            if type72222222 == 1:
                                                if type82222222 == 1:
                                                    if type92222222 == 0:
                                                        if type102222222 == 0:
                                                            if type112222222 == 0:
                                                                bm_1gggggggg.faces.new([fa12222222,fb12222222,fc12222222]) # 0 1 2
                                                                bm_1gggggggg.faces.new([fd12222222,fe12222222,ff12222222]) # 3 4 5
                                                                bm_1gggggggg.faces.new([fg12222222,fh12222222,fi12222222]) # 6 7 8
                                                                bm_1gggggggg.faces.new([fh12222222,fi12222222,fj12222222]) # 7 8 9
                                                                bm_1gggggggg.faces.new([fi12222222,fj12222222,fk12222222]) # 8 9 10

                    if type1222222 == 1:
                        if type2222222 == 1:
                            if type3222222 == 0:
                                if type4222222 == 0:
                                    if type5222222 == 0:
                                        if type6222222 == 0:
                                            if type7222222 == 0:
                                                if type8222222 == 0:
                                                    if type9222222 == 1:
                                                        if type10222222 == 1:
                                                            if type11222222 == 0:
                                                                bm_1ggggggg.faces.new([fa1222222,fb1222222,fc1222222]) # 0 1 2
                                                                bm_1ggggggg.faces.new([fb1222222,fc1222222,fd1222222]) # 1 2 3
                                                                bm_1ggggggg.faces.new([fc1222222,fd1222222,fe1222222]) # 2 3 4
                                                                bm_1ggggggg.faces.new([fd1222222,fe1222222,ff1222222]) # 3 4 5
                                                                bm_1ggggggg.faces.new([fe1222222,ff1222222,fg1222222]) # 6 7 8
                                                                bm_1ggggggg.faces.new([ff1222222,fg1222222,fh1222222]) # 7 8 9
                                                                bm_1ggggggg.faces.new([fi1222222,fj1222222,fk1222222]) # 8 9 10

                    if type122222 == 1:
                        if type222222 == 1:
                            if type322222 == 0:
                                if type422222 == 0:
                                    if type522222 == 0:
                                        if type622222 == 0:
                                            if type722222 == 0:
                                                if type822222 == 1:
                                                    if type922222 == 1:
                                                        if type1022222 == 0:
                                                            if type1122222 == 0:
                                                                bm_1gggggg.faces.new([fa122222,fb122222,fc122222]) # 0 1 2
                                                                bm_1gggggg.faces.new([fb122222,fc122222,fd122222]) # 1 2 3
                                                                bm_1gggggg.faces.new([fc122222,fd122222,fe122222]) # 2 3 4
                                                                bm_1gggggg.faces.new([fd122222,fe122222,ff122222]) # 3 4 5
                                                                bm_1gggggg.faces.new([fe122222,ff122222,fg122222]) # 6 7 8
                                                                bm_1gggggg.faces.new([fh122222,fi122222,fj122222]) # 7 8 9
                                                                bm_1gggggg.faces.new([fi122222,fj122222,fk122222]) # 8 9 10

                    if type12222 == 1:
                        if type22222 == 1:
                            if type32222 == 0:
                                if type42222 == 0:
                                    if type52222 == 0:
                                        if type62222 == 0:
                                            if type72222 == 1:
                                                if type82222 == 1:
                                                    if type92222 == 0:
                                                        if type102222 == 0:
                                                            if type112222 == 0:
                                                                bm_1ggggg.faces.new([fa12222,fb12222,fc12222]) # 0 1 2
                                                                bm_1ggggg.faces.new([fb12222,fc12222,fd12222]) # 1 2 3
                                                                bm_1ggggg.faces.new([fc12222,fd12222,fe12222]) # 2 3 4
                                                                bm_1ggggg.faces.new([fd12222,fe12222,ff12222]) # 3 4 5
                                                                bm_1ggggg.faces.new([fg12222,fh12222,fi12222]) # 6 7 8
                                                                bm_1ggggg.faces.new([fh12222,fi12222,fj12222]) # 7 8 9
                                                                bm_1ggggg.faces.new([fi12222,fj12222,fk12222]) # 8 9 10

                    if type1222 == 1:
                        if type2222 == 1:
                            if type3222 == 0:
                                if type4222 == 0:
                                    if type5222 == 0:
                                        if type6222 == 1:
                                            if type7222 == 1:
                                                if type8222 == 0:
                                                    if type9222 == 0:
                                                        if type10222 == 0:
                                                            if type11222 == 0:
                                                                bm_1gggg.faces.new([fa1222,fb1222,fc1222]) # 0 1 2
                                                                bm_1gggg.faces.new([fb1222,fc1222,fd1222]) # 1 2 3
                                                                bm_1gggg.faces.new([fc1222,fd1222,fe1222]) # 2 3 4
                                                                bm_1gggg.faces.new([ff1222,fg1222,fh1222]) # 5 6 7
                                                                bm_1gggg.faces.new([fg1222,fh1222,fi1222]) # 6 7 8
                                                                bm_1gggg.faces.new([fh1222,fi1222,fj1222]) # 7 8 9
                                                                bm_1gggg.faces.new([fi1222,fj1222,fk1222]) # 8 9 10

                    if type122 == 1:
                        if type222 == 1:
                            if type322 == 0:
                                if type422 == 0:
                                    if type522 == 1:
                                        if type622 == 1:
                                            if type722 == 0:
                                                if type822 == 0:
                                                    if type922 == 0:
                                                        if type1022 == 0:
                                                            if type1122 == 0:
                                                                bm_1ggg.faces.new([fa122,fb122,fc122])
                                                                bm_1ggg.faces.new([fb122,fc122,fd122])
                                                                bm_1ggg.faces.new([fe122,ff122,fg122])
                                                                bm_1ggg.faces.new([ff122,fg122,fh122])
                                                                bm_1ggg.faces.new([fg122,fh122,fi122])
                                                                bm_1ggg.faces.new([fh122,fi122,fj122])
                                                                bm_1ggg.faces.new([fi122,fj122,fk122])

                    if type12 == 1:
                        if type22 == 1:
                            if type32 == 0:
                                if type42 == 1:
                                    if type52 == 1:
                                        if type62 == 0:
                                            if type72 == 0:
                                                if type82 == 0:
                                                    if type92 == 0:
                                                        if type102 == 0:
                                                            if type112 == 0:
                                                                bm_1gg.faces.new([fa12,fb12,fc12])
                                                                bm_1gg.faces.new([fd12,fe12,ff12])
                                                                bm_1gg.faces.new([fe12,ff12,fg12])
                                                                bm_1gg.faces.new([ff12,fg12,fh12])
                                                                bm_1gg.faces.new([fg12,fh12,fi12])
                                                                bm_1gg.faces.new([fh12,fi12,fj12])
                                                                bm_1gg.faces.new([fi12,fj12,fk12])
                    
                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    if type9 == 0:
                                                        if type10 == 0:
                                                            if type11 == 0:
                                                                bm_1g.faces.new([fa1,fb1,fc1])
                                                                bm_1g.faces.new([fb1,fc1,fd1])
                                                                bm_1g.faces.new([fc1,fd1,fe1])
                                                                bm_1g.faces.new([fd1,fe1,ff1])
                                                                bm_1g.faces.new([fe1,ff1,fg1])
                                                                bm_1g.faces.new([ff1,fg1,fh1])
                                                                bm_1g.faces.new([fg1,fh1,fi1])
                                                                bm_1g.faces.new([fh1,fi1,fj1])
                                                                bm_1g.faces.new([fi1,fj1,fk1])

            elif vertexCount == 12:
                for i in range(vertexCount//12):
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
                    vx10 = unpack("<f", f.read(4))[0]
                    vy10 = unpack("<f", f.read(4))[0]
                    vz10 = unpack("<f", f.read(4))[0]
                    type10 = unpack("B", f.read(1))[0]
                    value10 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10 = unpack("<f", f.read(4))[0]
                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    vx12 = unpack("<f", f.read(4))[0]
                    vy12 = unpack("<f", f.read(4))[0]
                    vz12 = unpack("<f", f.read(4))[0]
                    type12 = unpack("B", f.read(1))[0]
                    value12 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12 = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx11a = unpack("<f", f.read(4))[0]
                    vy11a = unpack("<f", f.read(4))[0]
                    vz11a = unpack("<f", f.read(4))[0]
                    type11a = unpack("B", f.read(1))[0]
                    value11a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11a = unpack("<f", f.read(4))[0]
                    vx21a = unpack("<f", f.read(4))[0]
                    vy21a = unpack("<f", f.read(4))[0]
                    vz21a = unpack("<f", f.read(4))[0]
                    type21a = unpack("B", f.read(1))[0]
                    value21a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw21a = unpack("<f", f.read(4))[0]
                    vx31a = unpack("<f", f.read(4))[0]
                    vy31a = unpack("<f", f.read(4))[0]
                    vz31a = unpack("<f", f.read(4))[0]
                    type31a = unpack("B", f.read(1))[0]
                    value31a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw31a = unpack("<f", f.read(4))[0]
                    vx41a = unpack("<f", f.read(4))[0]
                    vy41a = unpack("<f", f.read(4))[0]
                    vz41a = unpack("<f", f.read(4))[0]
                    type41a = unpack("B", f.read(1))[0]
                    value41a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw41a = unpack("<f", f.read(4))[0]
                    vx51a = unpack("<f", f.read(4))[0]
                    vy51a = unpack("<f", f.read(4))[0]
                    vz51a = unpack("<f", f.read(4))[0]
                    type51a = unpack("B", f.read(1))[0]
                    value51a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw51a = unpack("<f", f.read(4))[0]
                    vx61a = unpack("<f", f.read(4))[0]
                    vy61a = unpack("<f", f.read(4))[0]
                    vz61a = unpack("<f", f.read(4))[0]
                    type61a = unpack("B", f.read(1))[0]
                    value61a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw61a = unpack("<f", f.read(4))[0]
                    vx71a = unpack("<f", f.read(4))[0]
                    vy71a = unpack("<f", f.read(4))[0]
                    vz71a = unpack("<f", f.read(4))[0]
                    type71a = unpack("B", f.read(1))[0]
                    value71a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw71a = unpack("<f", f.read(4))[0]
                    vx81a = unpack("<f", f.read(4))[0]
                    vy81a = unpack("<f", f.read(4))[0]
                    vz81a = unpack("<f", f.read(4))[0]
                    type81a = unpack("B", f.read(1))[0]
                    value81a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw81a = unpack("<f", f.read(4))[0]
                    vx91a = unpack("<f", f.read(4))[0]
                    vy91a = unpack("<f", f.read(4))[0]
                    vz91a = unpack("<f", f.read(4))[0]
                    type91a = unpack("B", f.read(1))[0]
                    value91a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw91a = unpack("<f", f.read(4))[0]
                    vx101a = unpack("<f", f.read(4))[0]
                    vy101a = unpack("<f", f.read(4))[0]
                    vz101a = unpack("<f", f.read(4))[0]
                    type101a = unpack("B", f.read(1))[0]
                    value101a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw101a = unpack("<f", f.read(4))[0]
                    vx111a = unpack("<f", f.read(4))[0]
                    vy111a = unpack("<f", f.read(4))[0]
                    vz111a = unpack("<f", f.read(4))[0]
                    type111a = unpack("B", f.read(1))[0]
                    value111a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw111a = unpack("<f", f.read(4))[0]
                    vx121a = unpack("<f", f.read(4))[0]
                    vy121a = unpack("<f", f.read(4))[0]
                    vz121a = unpack("<f", f.read(4))[0]
                    type121a = unpack("B", f.read(1))[0]
                    value121a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw121a = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx111 = unpack("<f", f.read(4))[0]
                    vy111 = unpack("<f", f.read(4))[0]
                    vz111 = unpack("<f", f.read(4))[0]
                    type111 = unpack("B", f.read(1))[0]
                    value111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw111 = unpack("<f", f.read(4))[0]
                    vx211 = unpack("<f", f.read(4))[0]
                    vy211 = unpack("<f", f.read(4))[0]
                    vz211 = unpack("<f", f.read(4))[0]
                    type211 = unpack("B", f.read(1))[0]
                    value211 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw211 = unpack("<f", f.read(4))[0]
                    vx311 = unpack("<f", f.read(4))[0]
                    vy311 = unpack("<f", f.read(4))[0]
                    vz311 = unpack("<f", f.read(4))[0]
                    type311 = unpack("B", f.read(1))[0]
                    value311 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw311 = unpack("<f", f.read(4))[0]
                    vx411 = unpack("<f", f.read(4))[0]
                    vy411 = unpack("<f", f.read(4))[0]
                    vz411 = unpack("<f", f.read(4))[0]
                    type411 = unpack("B", f.read(1))[0]
                    value411 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw411 = unpack("<f", f.read(4))[0]
                    vx511 = unpack("<f", f.read(4))[0]
                    vy511 = unpack("<f", f.read(4))[0]
                    vz511 = unpack("<f", f.read(4))[0]
                    type511 = unpack("B", f.read(1))[0]
                    value511 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw511 = unpack("<f", f.read(4))[0]
                    vx611 = unpack("<f", f.read(4))[0]
                    vy611 = unpack("<f", f.read(4))[0]
                    vz611 = unpack("<f", f.read(4))[0]
                    type611 = unpack("B", f.read(1))[0]
                    value611 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw611 = unpack("<f", f.read(4))[0]
                    vx711 = unpack("<f", f.read(4))[0]
                    vy711 = unpack("<f", f.read(4))[0]
                    vz711 = unpack("<f", f.read(4))[0]
                    type711 = unpack("B", f.read(1))[0]
                    value711 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw711 = unpack("<f", f.read(4))[0]
                    vx811 = unpack("<f", f.read(4))[0]
                    vy811 = unpack("<f", f.read(4))[0]
                    vz811 = unpack("<f", f.read(4))[0]
                    type811 = unpack("B", f.read(1))[0]
                    value811 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw811 = unpack("<f", f.read(4))[0]
                    vx911 = unpack("<f", f.read(4))[0]
                    vy911 = unpack("<f", f.read(4))[0]
                    vz911 = unpack("<f", f.read(4))[0]
                    type911 = unpack("B", f.read(1))[0]
                    value911 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw911 = unpack("<f", f.read(4))[0]
                    vx1011 = unpack("<f", f.read(4))[0]
                    vy1011 = unpack("<f", f.read(4))[0]
                    vz1011 = unpack("<f", f.read(4))[0]
                    type1011 = unpack("B", f.read(1))[0]
                    value1011 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1011 = unpack("<f", f.read(4))[0]
                    vx1111 = unpack("<f", f.read(4))[0]
                    vy1111 = unpack("<f", f.read(4))[0]
                    vz1111 = unpack("<f", f.read(4))[0]
                    type1111 = unpack("B", f.read(1))[0]
                    value1111 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1111 = unpack("<f", f.read(4))[0]
                    vx1211 = unpack("<f", f.read(4))[0]
                    vy1211 = unpack("<f", f.read(4))[0]
                    vz1211 = unpack("<f", f.read(4))[0]
                    type1211 = unpack("B", f.read(1))[0]
                    value1211 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1211 = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1_1 = unpack("<f", f.read(4))[0]
                    vy1_1 = unpack("<f", f.read(4))[0]
                    vz1_1 = unpack("<f", f.read(4))[0]
                    type1_1 = unpack("B", f.read(1))[0]
                    value1_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1_1 = unpack("<f", f.read(4))[0]
                    vx2_1 = unpack("<f", f.read(4))[0]
                    vy2_1 = unpack("<f", f.read(4))[0]
                    vz2_1 = unpack("<f", f.read(4))[0]
                    type2_1 = unpack("B", f.read(1))[0]
                    value2_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2_1 = unpack("<f", f.read(4))[0]
                    vx3_1 = unpack("<f", f.read(4))[0]
                    vy3_1 = unpack("<f", f.read(4))[0]
                    vz3_1 = unpack("<f", f.read(4))[0]
                    type3_1 = unpack("B", f.read(1))[0]
                    value3_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3_1 = unpack("<f", f.read(4))[0]
                    vx4_1 = unpack("<f", f.read(4))[0]
                    vy4_1 = unpack("<f", f.read(4))[0]
                    vz4_1 = unpack("<f", f.read(4))[0]
                    type4_1 = unpack("B", f.read(1))[0]
                    value4_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4_1 = unpack("<f", f.read(4))[0]
                    vx5_1 = unpack("<f", f.read(4))[0]
                    vy5_1 = unpack("<f", f.read(4))[0]
                    vz5_1 = unpack("<f", f.read(4))[0]
                    type5_1 = unpack("B", f.read(1))[0]
                    value5_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5_1 = unpack("<f", f.read(4))[0]
                    vx6_1 = unpack("<f", f.read(4))[0]
                    vy6_1 = unpack("<f", f.read(4))[0]
                    vz6_1 = unpack("<f", f.read(4))[0]
                    type6_1 = unpack("B", f.read(1))[0]
                    value6_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6_1 = unpack("<f", f.read(4))[0]
                    vx7_1 = unpack("<f", f.read(4))[0]
                    vy7_1 = unpack("<f", f.read(4))[0]
                    vz7_1 = unpack("<f", f.read(4))[0]
                    type7_1 = unpack("B", f.read(1))[0]
                    value7_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7_1 = unpack("<f", f.read(4))[0]
                    vx8_1 = unpack("<f", f.read(4))[0]
                    vy8_1 = unpack("<f", f.read(4))[0]
                    vz8_1 = unpack("<f", f.read(4))[0]
                    type8_1 = unpack("B", f.read(1))[0]
                    value8_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8_1 = unpack("<f", f.read(4))[0]
                    vx9_1 = unpack("<f", f.read(4))[0]
                    vy9_1 = unpack("<f", f.read(4))[0]
                    vz9_1 = unpack("<f", f.read(4))[0]
                    type9_1 = unpack("B", f.read(1))[0]
                    value9_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9_1 = unpack("<f", f.read(4))[0]
                    vx10_1 = unpack("<f", f.read(4))[0]
                    vy10_1 = unpack("<f", f.read(4))[0]
                    vz10_1 = unpack("<f", f.read(4))[0]
                    type10_1 = unpack("B", f.read(1))[0]
                    value10_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10_1 = unpack("<f", f.read(4))[0]
                    vx11_1 = unpack("<f", f.read(4))[0]
                    vy11_1 = unpack("<f", f.read(4))[0]
                    vz11_1 = unpack("<f", f.read(4))[0]
                    type11_1 = unpack("B", f.read(1))[0]
                    value11_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11_1 = unpack("<f", f.read(4))[0]
                    vx12_1 = unpack("<f", f.read(4))[0]
                    vy12_1 = unpack("<f", f.read(4))[0]
                    vz12_1 = unpack("<f", f.read(4))[0]
                    type12_1 = unpack("B", f.read(1))[0]
                    value12_1 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12_1 = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1c = unpack("<f", f.read(4))[0]
                    vy1c = unpack("<f", f.read(4))[0]
                    vz1c = unpack("<f", f.read(4))[0]
                    type1c = unpack("B", f.read(1))[0]
                    value1c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1c = unpack("<f", f.read(4))[0]
                    vx2c = unpack("<f", f.read(4))[0]
                    vy2c = unpack("<f", f.read(4))[0]
                    vz2c = unpack("<f", f.read(4))[0]
                    type2c = unpack("B", f.read(1))[0]
                    value2c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2c = unpack("<f", f.read(4))[0]
                    vx3c = unpack("<f", f.read(4))[0]
                    vy3c = unpack("<f", f.read(4))[0]
                    vz3c = unpack("<f", f.read(4))[0]
                    type3c = unpack("B", f.read(1))[0]
                    value3c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3c = unpack("<f", f.read(4))[0]
                    vx4c = unpack("<f", f.read(4))[0]
                    vy4c = unpack("<f", f.read(4))[0]
                    vz4c = unpack("<f", f.read(4))[0]
                    type4c = unpack("B", f.read(1))[0]
                    value4c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4c = unpack("<f", f.read(4))[0]
                    vx5c = unpack("<f", f.read(4))[0]
                    vy5c = unpack("<f", f.read(4))[0]
                    vz5c = unpack("<f", f.read(4))[0]
                    type5c = unpack("B", f.read(1))[0]
                    value5c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5c = unpack("<f", f.read(4))[0]
                    vx6c = unpack("<f", f.read(4))[0]
                    vy6c = unpack("<f", f.read(4))[0]
                    vz6c = unpack("<f", f.read(4))[0]
                    type6c = unpack("B", f.read(1))[0]
                    value6c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6c = unpack("<f", f.read(4))[0]
                    vx7c = unpack("<f", f.read(4))[0]
                    vy7c = unpack("<f", f.read(4))[0]
                    vz7c = unpack("<f", f.read(4))[0]
                    type7c = unpack("B", f.read(1))[0]
                    value7c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7c = unpack("<f", f.read(4))[0]
                    vx8c = unpack("<f", f.read(4))[0]
                    vy8c = unpack("<f", f.read(4))[0]
                    vz8c = unpack("<f", f.read(4))[0]
                    type8c = unpack("B", f.read(1))[0]
                    value8c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8c = unpack("<f", f.read(4))[0]
                    vx9c = unpack("<f", f.read(4))[0]
                    vy9c = unpack("<f", f.read(4))[0]
                    vz9c = unpack("<f", f.read(4))[0]
                    type9c = unpack("B", f.read(1))[0]
                    value9c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9c = unpack("<f", f.read(4))[0]
                    vx10c = unpack("<f", f.read(4))[0]
                    vy10c = unpack("<f", f.read(4))[0]
                    vz10c = unpack("<f", f.read(4))[0]
                    type10c = unpack("B", f.read(1))[0]
                    value10c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10c = unpack("<f", f.read(4))[0]
                    vx11c = unpack("<f", f.read(4))[0]
                    vy11c = unpack("<f", f.read(4))[0]
                    vz11c = unpack("<f", f.read(4))[0]
                    type11c = unpack("B", f.read(1))[0]
                    value11c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11c = unpack("<f", f.read(4))[0]
                    vx12c = unpack("<f", f.read(4))[0]
                    vy12c = unpack("<f", f.read(4))[0]
                    vz12c = unpack("<f", f.read(4))[0]
                    type12c = unpack("B", f.read(1))[0]
                    value12c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12c = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1d = unpack("<f", f.read(4))[0]
                    vy1d = unpack("<f", f.read(4))[0]
                    vz1d = unpack("<f", f.read(4))[0]
                    type1d = unpack("B", f.read(1))[0]
                    value1d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1d = unpack("<f", f.read(4))[0]
                    vx2d = unpack("<f", f.read(4))[0]
                    vy2d = unpack("<f", f.read(4))[0]
                    vz2d = unpack("<f", f.read(4))[0]
                    type2d = unpack("B", f.read(1))[0]
                    value2d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2d = unpack("<f", f.read(4))[0]
                    vx3d = unpack("<f", f.read(4))[0]
                    vy3d = unpack("<f", f.read(4))[0]
                    vz3d = unpack("<f", f.read(4))[0]
                    type3d = unpack("B", f.read(1))[0]
                    value3d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3d = unpack("<f", f.read(4))[0]
                    vx4d = unpack("<f", f.read(4))[0]
                    vy4d = unpack("<f", f.read(4))[0]
                    vz4d = unpack("<f", f.read(4))[0]
                    type4d = unpack("B", f.read(1))[0]
                    value4d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4d = unpack("<f", f.read(4))[0]
                    vx5d = unpack("<f", f.read(4))[0]
                    vy5d = unpack("<f", f.read(4))[0]
                    vz5d = unpack("<f", f.read(4))[0]
                    type5d = unpack("B", f.read(1))[0]
                    value5d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5d = unpack("<f", f.read(4))[0]
                    vx6d = unpack("<f", f.read(4))[0]
                    vy6d = unpack("<f", f.read(4))[0]
                    vz6d = unpack("<f", f.read(4))[0]
                    type6d = unpack("B", f.read(1))[0]
                    value6d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6d = unpack("<f", f.read(4))[0]
                    vx7d = unpack("<f", f.read(4))[0]
                    vy7d = unpack("<f", f.read(4))[0]
                    vz7d = unpack("<f", f.read(4))[0]
                    type7d = unpack("B", f.read(1))[0]
                    value7d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7d = unpack("<f", f.read(4))[0]
                    vx8d = unpack("<f", f.read(4))[0]
                    vy8d = unpack("<f", f.read(4))[0]
                    vz8d = unpack("<f", f.read(4))[0]
                    type8d = unpack("B", f.read(1))[0]
                    value8d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8d = unpack("<f", f.read(4))[0]
                    vx9d = unpack("<f", f.read(4))[0]
                    vy9d = unpack("<f", f.read(4))[0]
                    vz9d = unpack("<f", f.read(4))[0]
                    type9d = unpack("B", f.read(1))[0]
                    value9d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9d = unpack("<f", f.read(4))[0]
                    vx10d = unpack("<f", f.read(4))[0]
                    vy10d = unpack("<f", f.read(4))[0]
                    vz10d = unpack("<f", f.read(4))[0]
                    type10d = unpack("B", f.read(1))[0]
                    value10d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10d = unpack("<f", f.read(4))[0]
                    vx11d = unpack("<f", f.read(4))[0]
                    vy11d = unpack("<f", f.read(4))[0]
                    vz11d = unpack("<f", f.read(4))[0]
                    type11d = unpack("B", f.read(1))[0]
                    value11d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11d = unpack("<f", f.read(4))[0]
                    vx12d = unpack("<f", f.read(4))[0]
                    vy12d = unpack("<f", f.read(4))[0]
                    vz12d = unpack("<f", f.read(4))[0]
                    type12d = unpack("B", f.read(1))[0]
                    value12d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12d = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1e = unpack("<f", f.read(4))[0]
                    vy1e = unpack("<f", f.read(4))[0]
                    vz1e = unpack("<f", f.read(4))[0]
                    type1e = unpack("B", f.read(1))[0]
                    value1e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1e = unpack("<f", f.read(4))[0]
                    vx2e = unpack("<f", f.read(4))[0]
                    vy2e = unpack("<f", f.read(4))[0]
                    vz2e = unpack("<f", f.read(4))[0]
                    type2e = unpack("B", f.read(1))[0]
                    value2e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2e = unpack("<f", f.read(4))[0]
                    vx3e = unpack("<f", f.read(4))[0]
                    vy3e = unpack("<f", f.read(4))[0]
                    vz3e = unpack("<f", f.read(4))[0]
                    type3e = unpack("B", f.read(1))[0]
                    value3e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3e = unpack("<f", f.read(4))[0]
                    vx4e = unpack("<f", f.read(4))[0]
                    vy4e = unpack("<f", f.read(4))[0]
                    vz4e = unpack("<f", f.read(4))[0]
                    type4e = unpack("B", f.read(1))[0]
                    value4e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4e = unpack("<f", f.read(4))[0]
                    vx5e = unpack("<f", f.read(4))[0]
                    vy5e = unpack("<f", f.read(4))[0]
                    vz5e = unpack("<f", f.read(4))[0]
                    type5e = unpack("B", f.read(1))[0]
                    value5e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5e = unpack("<f", f.read(4))[0]
                    vx6e = unpack("<f", f.read(4))[0]
                    vy6e = unpack("<f", f.read(4))[0]
                    vz6e = unpack("<f", f.read(4))[0]
                    type6e = unpack("B", f.read(1))[0]
                    value6e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6e = unpack("<f", f.read(4))[0]
                    vx7e = unpack("<f", f.read(4))[0]
                    vy7e = unpack("<f", f.read(4))[0]
                    vz7e = unpack("<f", f.read(4))[0]
                    type7e = unpack("B", f.read(1))[0]
                    value7e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7e = unpack("<f", f.read(4))[0]
                    vx8e = unpack("<f", f.read(4))[0]
                    vy8e = unpack("<f", f.read(4))[0]
                    vz8e = unpack("<f", f.read(4))[0]
                    type8e = unpack("B", f.read(1))[0]
                    value8e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8e = unpack("<f", f.read(4))[0]
                    vx9e = unpack("<f", f.read(4))[0]
                    vy9e = unpack("<f", f.read(4))[0]
                    vz9e = unpack("<f", f.read(4))[0]
                    type9e = unpack("B", f.read(1))[0]
                    value9e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9e = unpack("<f", f.read(4))[0]
                    vx10e = unpack("<f", f.read(4))[0]
                    vy10e = unpack("<f", f.read(4))[0]
                    vz10e = unpack("<f", f.read(4))[0]
                    type10e = unpack("B", f.read(1))[0]
                    value10e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10e = unpack("<f", f.read(4))[0]
                    vx11e = unpack("<f", f.read(4))[0]
                    vy11e = unpack("<f", f.read(4))[0]
                    vz11e = unpack("<f", f.read(4))[0]
                    type11e = unpack("B", f.read(1))[0]
                    value11e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11e = unpack("<f", f.read(4))[0]
                    vx12e = unpack("<f", f.read(4))[0]
                    vy12e = unpack("<f", f.read(4))[0]
                    vz12e = unpack("<f", f.read(4))[0]
                    type12e = unpack("B", f.read(1))[0]
                    value12e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12e = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1f = unpack("<f", f.read(4))[0]
                    vy1f = unpack("<f", f.read(4))[0]
                    vz1f = unpack("<f", f.read(4))[0]
                    type1f = unpack("B", f.read(1))[0]
                    value1f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1f = unpack("<f", f.read(4))[0]
                    vx2f = unpack("<f", f.read(4))[0]
                    vy2f = unpack("<f", f.read(4))[0]
                    vz2f = unpack("<f", f.read(4))[0]
                    type2f = unpack("B", f.read(1))[0]
                    value2f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2f = unpack("<f", f.read(4))[0]
                    vx3f = unpack("<f", f.read(4))[0]
                    vy3f = unpack("<f", f.read(4))[0]
                    vz3f = unpack("<f", f.read(4))[0]
                    type3f = unpack("B", f.read(1))[0]
                    value3f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3f = unpack("<f", f.read(4))[0]
                    vx4f = unpack("<f", f.read(4))[0]
                    vy4f = unpack("<f", f.read(4))[0]
                    vz4f = unpack("<f", f.read(4))[0]
                    type4f = unpack("B", f.read(1))[0]
                    value4f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4f = unpack("<f", f.read(4))[0]
                    vx5f = unpack("<f", f.read(4))[0]
                    vy5f = unpack("<f", f.read(4))[0]
                    vz5f = unpack("<f", f.read(4))[0]
                    type5f = unpack("B", f.read(1))[0]
                    value5f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5f = unpack("<f", f.read(4))[0]
                    vx6f = unpack("<f", f.read(4))[0]
                    vy6f = unpack("<f", f.read(4))[0]
                    vz6f = unpack("<f", f.read(4))[0]
                    type6f = unpack("B", f.read(1))[0]
                    value6f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6f = unpack("<f", f.read(4))[0]
                    vx7f = unpack("<f", f.read(4))[0]
                    vy7f = unpack("<f", f.read(4))[0]
                    vz7f = unpack("<f", f.read(4))[0]
                    type7f = unpack("B", f.read(1))[0]
                    value7f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7f = unpack("<f", f.read(4))[0]
                    vx8f = unpack("<f", f.read(4))[0]
                    vy8f = unpack("<f", f.read(4))[0]
                    vz8f = unpack("<f", f.read(4))[0]
                    type8f = unpack("B", f.read(1))[0]
                    value8f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8f = unpack("<f", f.read(4))[0]
                    vx9f = unpack("<f", f.read(4))[0]
                    vy9f = unpack("<f", f.read(4))[0]
                    vz9f = unpack("<f", f.read(4))[0]
                    type9f = unpack("B", f.read(1))[0]
                    value9f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9f = unpack("<f", f.read(4))[0]
                    vx10f = unpack("<f", f.read(4))[0]
                    vy10f = unpack("<f", f.read(4))[0]
                    vz10f = unpack("<f", f.read(4))[0]
                    type10f = unpack("B", f.read(1))[0]
                    value10f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10f = unpack("<f", f.read(4))[0]
                    vx11f = unpack("<f", f.read(4))[0]
                    vy11f = unpack("<f", f.read(4))[0]
                    vz11f = unpack("<f", f.read(4))[0]
                    type11f = unpack("B", f.read(1))[0]
                    value11f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11f = unpack("<f", f.read(4))[0]
                    vx12f = unpack("<f", f.read(4))[0]
                    vy12f = unpack("<f", f.read(4))[0]
                    vz12f = unpack("<f", f.read(4))[0]
                    type12f = unpack("B", f.read(1))[0]
                    value12f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12f = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1g = unpack("<f", f.read(4))[0]
                    vy1g = unpack("<f", f.read(4))[0]
                    vz1g = unpack("<f", f.read(4))[0]
                    type1g = unpack("B", f.read(1))[0]
                    value1g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1g = unpack("<f", f.read(4))[0]
                    vx2g = unpack("<f", f.read(4))[0]
                    vy2g = unpack("<f", f.read(4))[0]
                    vz2g = unpack("<f", f.read(4))[0]
                    type2g = unpack("B", f.read(1))[0]
                    value2g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2g = unpack("<f", f.read(4))[0]
                    vx3g = unpack("<f", f.read(4))[0]
                    vy3g = unpack("<f", f.read(4))[0]
                    vz3g = unpack("<f", f.read(4))[0]
                    type3g = unpack("B", f.read(1))[0]
                    value3g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3g = unpack("<f", f.read(4))[0]
                    vx4g = unpack("<f", f.read(4))[0]
                    vy4g = unpack("<f", f.read(4))[0]
                    vz4g = unpack("<f", f.read(4))[0]
                    type4g = unpack("B", f.read(1))[0]
                    value4g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4g = unpack("<f", f.read(4))[0]
                    vx5g = unpack("<f", f.read(4))[0]
                    vy5g = unpack("<f", f.read(4))[0]
                    vz5g = unpack("<f", f.read(4))[0]
                    type5g = unpack("B", f.read(1))[0]
                    value5g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5g = unpack("<f", f.read(4))[0]
                    vx6g = unpack("<f", f.read(4))[0]
                    vy6g = unpack("<f", f.read(4))[0]
                    vz6g = unpack("<f", f.read(4))[0]
                    type6g = unpack("B", f.read(1))[0]
                    value6g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6g = unpack("<f", f.read(4))[0]
                    vx7g = unpack("<f", f.read(4))[0]
                    vy7g = unpack("<f", f.read(4))[0]
                    vz7g = unpack("<f", f.read(4))[0]
                    type7g = unpack("B", f.read(1))[0]
                    value7g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7g = unpack("<f", f.read(4))[0]
                    vx8g = unpack("<f", f.read(4))[0]
                    vy8g = unpack("<f", f.read(4))[0]
                    vz8g = unpack("<f", f.read(4))[0]
                    type8g = unpack("B", f.read(1))[0]
                    value8g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8g = unpack("<f", f.read(4))[0]
                    vx9g = unpack("<f", f.read(4))[0]
                    vy9g = unpack("<f", f.read(4))[0]
                    vz9g = unpack("<f", f.read(4))[0]
                    type9g = unpack("B", f.read(1))[0]
                    value9g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9g = unpack("<f", f.read(4))[0]
                    vx10g = unpack("<f", f.read(4))[0]
                    vy10g = unpack("<f", f.read(4))[0]
                    vz10g = unpack("<f", f.read(4))[0]
                    type10g = unpack("B", f.read(1))[0]
                    value10g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10g = unpack("<f", f.read(4))[0]
                    vx11g = unpack("<f", f.read(4))[0]
                    vy11g = unpack("<f", f.read(4))[0]
                    vz11g = unpack("<f", f.read(4))[0]
                    type11g = unpack("B", f.read(1))[0]
                    value11g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11g = unpack("<f", f.read(4))[0]
                    vx12g = unpack("<f", f.read(4))[0]
                    vy12g = unpack("<f", f.read(4))[0]
                    vz12g = unpack("<f", f.read(4))[0]
                    type12g = unpack("B", f.read(1))[0]
                    value12g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12g = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1h = unpack("<f", f.read(4))[0]
                    vy1h = unpack("<f", f.read(4))[0]
                    vz1h = unpack("<f", f.read(4))[0]
                    type1h = unpack("B", f.read(1))[0]
                    value1h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1h = unpack("<f", f.read(4))[0]
                    vx2h = unpack("<f", f.read(4))[0]
                    vy2h = unpack("<f", f.read(4))[0]
                    vz2h = unpack("<f", f.read(4))[0]
                    type2h = unpack("B", f.read(1))[0]
                    value2h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2h = unpack("<f", f.read(4))[0]
                    vx3h = unpack("<f", f.read(4))[0]
                    vy3h = unpack("<f", f.read(4))[0]
                    vz3h = unpack("<f", f.read(4))[0]
                    type3h = unpack("B", f.read(1))[0]
                    value3h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3h = unpack("<f", f.read(4))[0]
                    vx4h = unpack("<f", f.read(4))[0]
                    vy4h = unpack("<f", f.read(4))[0]
                    vz4h = unpack("<f", f.read(4))[0]
                    type4h = unpack("B", f.read(1))[0]
                    value4h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4h = unpack("<f", f.read(4))[0]
                    vx5h = unpack("<f", f.read(4))[0]
                    vy5h = unpack("<f", f.read(4))[0]
                    vz5h = unpack("<f", f.read(4))[0]
                    type5h = unpack("B", f.read(1))[0]
                    value5h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5h = unpack("<f", f.read(4))[0]
                    vx6h = unpack("<f", f.read(4))[0]
                    vy6h = unpack("<f", f.read(4))[0]
                    vz6h = unpack("<f", f.read(4))[0]
                    type6h = unpack("B", f.read(1))[0]
                    value6h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6h = unpack("<f", f.read(4))[0]
                    vx7h = unpack("<f", f.read(4))[0]
                    vy7h = unpack("<f", f.read(4))[0]
                    vz7h = unpack("<f", f.read(4))[0]
                    type7h = unpack("B", f.read(1))[0]
                    value7h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7h = unpack("<f", f.read(4))[0]
                    vx8h = unpack("<f", f.read(4))[0]
                    vy8h = unpack("<f", f.read(4))[0]
                    vz8h = unpack("<f", f.read(4))[0]
                    type8h = unpack("B", f.read(1))[0]
                    value8h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8h = unpack("<f", f.read(4))[0]
                    vx9h = unpack("<f", f.read(4))[0]
                    vy9h = unpack("<f", f.read(4))[0]
                    vz9h = unpack("<f", f.read(4))[0]
                    type9h = unpack("B", f.read(1))[0]
                    value9h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9h = unpack("<f", f.read(4))[0]
                    vx10h = unpack("<f", f.read(4))[0]
                    vy10h = unpack("<f", f.read(4))[0]
                    vz10h = unpack("<f", f.read(4))[0]
                    type10h = unpack("B", f.read(1))[0]
                    value10h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10h = unpack("<f", f.read(4))[0]
                    vx11h = unpack("<f", f.read(4))[0]
                    vy11h = unpack("<f", f.read(4))[0]
                    vz11h = unpack("<f", f.read(4))[0]
                    type11h = unpack("B", f.read(1))[0]
                    value11h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11h = unpack("<f", f.read(4))[0]
                    vx12h = unpack("<f", f.read(4))[0]
                    vy12h = unpack("<f", f.read(4))[0]
                    vz12h = unpack("<f", f.read(4))[0]
                    type12h = unpack("B", f.read(1))[0]
                    value12h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12h = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1i = unpack("<f", f.read(4))[0]
                    vy1i = unpack("<f", f.read(4))[0]
                    vz1i = unpack("<f", f.read(4))[0]
                    type1i = unpack("B", f.read(1))[0]
                    value1i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1i = unpack("<f", f.read(4))[0]
                    vx2i = unpack("<f", f.read(4))[0]
                    vy2i = unpack("<f", f.read(4))[0]
                    vz2i = unpack("<f", f.read(4))[0]
                    type2i = unpack("B", f.read(1))[0]
                    value2i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2i = unpack("<f", f.read(4))[0]
                    vx3i = unpack("<f", f.read(4))[0]
                    vy3i = unpack("<f", f.read(4))[0]
                    vz3i = unpack("<f", f.read(4))[0]
                    type3i = unpack("B", f.read(1))[0]
                    value3i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3i = unpack("<f", f.read(4))[0]
                    vx4i = unpack("<f", f.read(4))[0]
                    vy4i = unpack("<f", f.read(4))[0]
                    vz4i = unpack("<f", f.read(4))[0]
                    type4i = unpack("B", f.read(1))[0]
                    value4i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4i = unpack("<f", f.read(4))[0]
                    vx5i = unpack("<f", f.read(4))[0]
                    vy5i = unpack("<f", f.read(4))[0]
                    vz5i = unpack("<f", f.read(4))[0]
                    type5i = unpack("B", f.read(1))[0]
                    value5i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5i = unpack("<f", f.read(4))[0]
                    vx6i = unpack("<f", f.read(4))[0]
                    vy6i = unpack("<f", f.read(4))[0]
                    vz6i = unpack("<f", f.read(4))[0]
                    type6i = unpack("B", f.read(1))[0]
                    value6i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6i = unpack("<f", f.read(4))[0]
                    vx7i = unpack("<f", f.read(4))[0]
                    vy7i = unpack("<f", f.read(4))[0]
                    vz7i = unpack("<f", f.read(4))[0]
                    type7i = unpack("B", f.read(1))[0]
                    value7i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7i = unpack("<f", f.read(4))[0]
                    vx8i = unpack("<f", f.read(4))[0]
                    vy8i = unpack("<f", f.read(4))[0]
                    vz8i = unpack("<f", f.read(4))[0]
                    type8i = unpack("B", f.read(1))[0]
                    value8i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8i = unpack("<f", f.read(4))[0]
                    vx9i = unpack("<f", f.read(4))[0]
                    vy9i = unpack("<f", f.read(4))[0]
                    vz9i = unpack("<f", f.read(4))[0]
                    type9i = unpack("B", f.read(1))[0]
                    value9i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9i = unpack("<f", f.read(4))[0]
                    vx10i = unpack("<f", f.read(4))[0]
                    vy10i = unpack("<f", f.read(4))[0]
                    vz10i = unpack("<f", f.read(4))[0]
                    type10i = unpack("B", f.read(1))[0]
                    value10i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10i = unpack("<f", f.read(4))[0]
                    vx11i = unpack("<f", f.read(4))[0]
                    vy11i = unpack("<f", f.read(4))[0]
                    vz11i = unpack("<f", f.read(4))[0]
                    type11i = unpack("B", f.read(1))[0]
                    value11i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11i = unpack("<f", f.read(4))[0]
                    vx12i = unpack("<f", f.read(4))[0]
                    vy12i = unpack("<f", f.read(4))[0]
                    vz12i = unpack("<f", f.read(4))[0]
                    type12i = unpack("B", f.read(1))[0]
                    value12i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12i = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1j = unpack("<f", f.read(4))[0]
                    vy1j = unpack("<f", f.read(4))[0]
                    vz1j = unpack("<f", f.read(4))[0]
                    type1j = unpack("B", f.read(1))[0]
                    value1j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1j = unpack("<f", f.read(4))[0]
                    vx2j = unpack("<f", f.read(4))[0]
                    vy2j = unpack("<f", f.read(4))[0]
                    vz2j = unpack("<f", f.read(4))[0]
                    type2j = unpack("B", f.read(1))[0]
                    value2j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2j = unpack("<f", f.read(4))[0]
                    vx3j = unpack("<f", f.read(4))[0]
                    vy3j = unpack("<f", f.read(4))[0]
                    vz3j = unpack("<f", f.read(4))[0]
                    type3j = unpack("B", f.read(1))[0]
                    value3j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3j = unpack("<f", f.read(4))[0]
                    vx4j = unpack("<f", f.read(4))[0]
                    vy4j = unpack("<f", f.read(4))[0]
                    vz4j = unpack("<f", f.read(4))[0]
                    type4j = unpack("B", f.read(1))[0]
                    value4j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4j = unpack("<f", f.read(4))[0]
                    vx5j = unpack("<f", f.read(4))[0]
                    vy5j = unpack("<f", f.read(4))[0]
                    vz5j = unpack("<f", f.read(4))[0]
                    type5j = unpack("B", f.read(1))[0]
                    value5j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5j = unpack("<f", f.read(4))[0]
                    vx6j = unpack("<f", f.read(4))[0]
                    vy6j = unpack("<f", f.read(4))[0]
                    vz6j = unpack("<f", f.read(4))[0]
                    type6j = unpack("B", f.read(1))[0]
                    value6j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6j = unpack("<f", f.read(4))[0]
                    vx7j = unpack("<f", f.read(4))[0]
                    vy7j = unpack("<f", f.read(4))[0]
                    vz7j = unpack("<f", f.read(4))[0]
                    type7j = unpack("B", f.read(1))[0]
                    value7j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7j = unpack("<f", f.read(4))[0]
                    vx8j = unpack("<f", f.read(4))[0]
                    vy8j = unpack("<f", f.read(4))[0]
                    vz8j = unpack("<f", f.read(4))[0]
                    type8j = unpack("B", f.read(1))[0]
                    value8j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8j = unpack("<f", f.read(4))[0]
                    vx9j = unpack("<f", f.read(4))[0]
                    vy9j = unpack("<f", f.read(4))[0]
                    vz9j = unpack("<f", f.read(4))[0]
                    type9j = unpack("B", f.read(1))[0]
                    value9j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9j = unpack("<f", f.read(4))[0]
                    vx10j = unpack("<f", f.read(4))[0]
                    vy10j = unpack("<f", f.read(4))[0]
                    vz10j = unpack("<f", f.read(4))[0]
                    type10j = unpack("B", f.read(1))[0]
                    value10j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10j = unpack("<f", f.read(4))[0]
                    vx11j = unpack("<f", f.read(4))[0]
                    vy11j = unpack("<f", f.read(4))[0]
                    vz11j = unpack("<f", f.read(4))[0]
                    type11j = unpack("B", f.read(1))[0]
                    value11j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11j = unpack("<f", f.read(4))[0]
                    vx12j = unpack("<f", f.read(4))[0]
                    vy12j = unpack("<f", f.read(4))[0]
                    vz12j = unpack("<f", f.read(4))[0]
                    type12j = unpack("B", f.read(1))[0]
                    value12j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12j = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1k = unpack("<f", f.read(4))[0]
                    vy1k = unpack("<f", f.read(4))[0]
                    vz1k = unpack("<f", f.read(4))[0]
                    type1k = unpack("B", f.read(1))[0]
                    value1k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1k = unpack("<f", f.read(4))[0]
                    vx2k = unpack("<f", f.read(4))[0]
                    vy2k = unpack("<f", f.read(4))[0]
                    vz2k = unpack("<f", f.read(4))[0]
                    type2k = unpack("B", f.read(1))[0]
                    value2k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2k = unpack("<f", f.read(4))[0]
                    vx3k = unpack("<f", f.read(4))[0]
                    vy3k = unpack("<f", f.read(4))[0]
                    vz3k = unpack("<f", f.read(4))[0]
                    type3k = unpack("B", f.read(1))[0]
                    value3k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3k = unpack("<f", f.read(4))[0]
                    vx4k = unpack("<f", f.read(4))[0]
                    vy4k = unpack("<f", f.read(4))[0]
                    vz4k = unpack("<f", f.read(4))[0]
                    type4k = unpack("B", f.read(1))[0]
                    value4k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4k = unpack("<f", f.read(4))[0]
                    vx5k = unpack("<f", f.read(4))[0]
                    vy5k = unpack("<f", f.read(4))[0]
                    vz5k = unpack("<f", f.read(4))[0]
                    type5k = unpack("B", f.read(1))[0]
                    value5k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5k = unpack("<f", f.read(4))[0]
                    vx6k = unpack("<f", f.read(4))[0]
                    vy6k = unpack("<f", f.read(4))[0]
                    vz6k = unpack("<f", f.read(4))[0]
                    type6k = unpack("B", f.read(1))[0]
                    value6k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6k = unpack("<f", f.read(4))[0]
                    vx7k = unpack("<f", f.read(4))[0]
                    vy7k = unpack("<f", f.read(4))[0]
                    vz7k = unpack("<f", f.read(4))[0]
                    type7k = unpack("B", f.read(1))[0]
                    value7k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7k = unpack("<f", f.read(4))[0]
                    vx8k = unpack("<f", f.read(4))[0]
                    vy8k = unpack("<f", f.read(4))[0]
                    vz8k = unpack("<f", f.read(4))[0]
                    type8k = unpack("B", f.read(1))[0]
                    value8k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8k = unpack("<f", f.read(4))[0]
                    vx9k = unpack("<f", f.read(4))[0]
                    vy9k = unpack("<f", f.read(4))[0]
                    vz9k = unpack("<f", f.read(4))[0]
                    type9k = unpack("B", f.read(1))[0]
                    value9k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9k = unpack("<f", f.read(4))[0]
                    vx10k = unpack("<f", f.read(4))[0]
                    vy10k = unpack("<f", f.read(4))[0]
                    vz10k = unpack("<f", f.read(4))[0]
                    type10k = unpack("B", f.read(1))[0]
                    value10k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10k = unpack("<f", f.read(4))[0]
                    vx11k = unpack("<f", f.read(4))[0]
                    vy11k = unpack("<f", f.read(4))[0]
                    vz11k = unpack("<f", f.read(4))[0]
                    type11k = unpack("B", f.read(1))[0]
                    value11k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11k = unpack("<f", f.read(4))[0]
                    vx12k = unpack("<f", f.read(4))[0]
                    vy12k = unpack("<f", f.read(4))[0]
                    vz12k = unpack("<f", f.read(4))[0]
                    type12k = unpack("B", f.read(1))[0]
                    value12k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12k = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1l = unpack("<f", f.read(4))[0]
                    vy1l = unpack("<f", f.read(4))[0]
                    vz1l = unpack("<f", f.read(4))[0]
                    type1l = unpack("B", f.read(1))[0]
                    value1l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1l = unpack("<f", f.read(4))[0]
                    vx2l = unpack("<f", f.read(4))[0]
                    vy2l = unpack("<f", f.read(4))[0]
                    vz2l = unpack("<f", f.read(4))[0]
                    type2l = unpack("B", f.read(1))[0]
                    value2l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2l = unpack("<f", f.read(4))[0]
                    vx3l = unpack("<f", f.read(4))[0]
                    vy3l = unpack("<f", f.read(4))[0]
                    vz3l = unpack("<f", f.read(4))[0]
                    type3l = unpack("B", f.read(1))[0]
                    value3l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3l = unpack("<f", f.read(4))[0]
                    vx4l = unpack("<f", f.read(4))[0]
                    vy4l = unpack("<f", f.read(4))[0]
                    vz4l = unpack("<f", f.read(4))[0]
                    type4l = unpack("B", f.read(1))[0]
                    value4l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4l = unpack("<f", f.read(4))[0]
                    vx5l = unpack("<f", f.read(4))[0]
                    vy5l = unpack("<f", f.read(4))[0]
                    vz5l = unpack("<f", f.read(4))[0]
                    type5l = unpack("B", f.read(1))[0]
                    value5l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5l = unpack("<f", f.read(4))[0]
                    vx6l = unpack("<f", f.read(4))[0]
                    vy6l = unpack("<f", f.read(4))[0]
                    vz6l = unpack("<f", f.read(4))[0]
                    type6l = unpack("B", f.read(1))[0]
                    value6l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6l = unpack("<f", f.read(4))[0]
                    vx7l = unpack("<f", f.read(4))[0]
                    vy7l = unpack("<f", f.read(4))[0]
                    vz7l = unpack("<f", f.read(4))[0]
                    type7l = unpack("B", f.read(1))[0]
                    value7l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7l = unpack("<f", f.read(4))[0]
                    vx8l = unpack("<f", f.read(4))[0]
                    vy8l = unpack("<f", f.read(4))[0]
                    vz8l = unpack("<f", f.read(4))[0]
                    type8l = unpack("B", f.read(1))[0]
                    value8l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8l = unpack("<f", f.read(4))[0]
                    vx9l = unpack("<f", f.read(4))[0]
                    vy9l = unpack("<f", f.read(4))[0]
                    vz9l = unpack("<f", f.read(4))[0]
                    type9l = unpack("B", f.read(1))[0]
                    value9l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9l = unpack("<f", f.read(4))[0]
                    vx10l = unpack("<f", f.read(4))[0]
                    vy10l = unpack("<f", f.read(4))[0]
                    vz10l = unpack("<f", f.read(4))[0]
                    type10l = unpack("B", f.read(1))[0]
                    value10l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10l = unpack("<f", f.read(4))[0]
                    vx11l = unpack("<f", f.read(4))[0]
                    vy11l = unpack("<f", f.read(4))[0]
                    vz11l = unpack("<f", f.read(4))[0]
                    type11l = unpack("B", f.read(1))[0]
                    value11l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11l = unpack("<f", f.read(4))[0]
                    vx12l = unpack("<f", f.read(4))[0]
                    vy12l = unpack("<f", f.read(4))[0]
                    vz12l = unpack("<f", f.read(4))[0]
                    type12l = unpack("B", f.read(1))[0]
                    value12l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12l = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1m = unpack("<f", f.read(4))[0]
                    vy1m = unpack("<f", f.read(4))[0]
                    vz1m = unpack("<f", f.read(4))[0]
                    type1m = unpack("B", f.read(1))[0]
                    value1m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1m = unpack("<f", f.read(4))[0]
                    vx2m = unpack("<f", f.read(4))[0]
                    vy2m = unpack("<f", f.read(4))[0]
                    vz2m = unpack("<f", f.read(4))[0]
                    type2m = unpack("B", f.read(1))[0]
                    value2m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2m = unpack("<f", f.read(4))[0]
                    vx3m = unpack("<f", f.read(4))[0]
                    vy3m = unpack("<f", f.read(4))[0]
                    vz3m = unpack("<f", f.read(4))[0]
                    type3m = unpack("B", f.read(1))[0]
                    value3m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3m = unpack("<f", f.read(4))[0]
                    vx4m = unpack("<f", f.read(4))[0]
                    vy4m = unpack("<f", f.read(4))[0]
                    vz4m = unpack("<f", f.read(4))[0]
                    type4m = unpack("B", f.read(1))[0]
                    value4m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4m = unpack("<f", f.read(4))[0]
                    vx5m = unpack("<f", f.read(4))[0]
                    vy5m = unpack("<f", f.read(4))[0]
                    vz5m = unpack("<f", f.read(4))[0]
                    type5m = unpack("B", f.read(1))[0]
                    value5m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5m = unpack("<f", f.read(4))[0]
                    vx6m = unpack("<f", f.read(4))[0]
                    vy6m = unpack("<f", f.read(4))[0]
                    vz6m = unpack("<f", f.read(4))[0]
                    type6m = unpack("B", f.read(1))[0]
                    value6m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6m = unpack("<f", f.read(4))[0]
                    vx7m = unpack("<f", f.read(4))[0]
                    vy7m = unpack("<f", f.read(4))[0]
                    vz7m = unpack("<f", f.read(4))[0]
                    type7m = unpack("B", f.read(1))[0]
                    value7m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7m = unpack("<f", f.read(4))[0]
                    vx8m = unpack("<f", f.read(4))[0]
                    vy8m = unpack("<f", f.read(4))[0]
                    vz8m = unpack("<f", f.read(4))[0]
                    type8m = unpack("B", f.read(1))[0]
                    value8m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8m = unpack("<f", f.read(4))[0]
                    vx9m = unpack("<f", f.read(4))[0]
                    vy9m = unpack("<f", f.read(4))[0]
                    vz9m = unpack("<f", f.read(4))[0]
                    type9m = unpack("B", f.read(1))[0]
                    value9m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9m = unpack("<f", f.read(4))[0]
                    vx10m = unpack("<f", f.read(4))[0]
                    vy10m = unpack("<f", f.read(4))[0]
                    vz10m = unpack("<f", f.read(4))[0]
                    type10m = unpack("B", f.read(1))[0]
                    value10m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10m = unpack("<f", f.read(4))[0]
                    vx11m = unpack("<f", f.read(4))[0]
                    vy11m = unpack("<f", f.read(4))[0]
                    vz11m = unpack("<f", f.read(4))[0]
                    type11m = unpack("B", f.read(1))[0]
                    value11m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11m = unpack("<f", f.read(4))[0]
                    vx12m = unpack("<f", f.read(4))[0]
                    vy12m = unpack("<f", f.read(4))[0]
                    vz12m = unpack("<f", f.read(4))[0]
                    type12m = unpack("B", f.read(1))[0]
                    value12m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12m = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1n = unpack("<f", f.read(4))[0]
                    vy1n = unpack("<f", f.read(4))[0]
                    vz1n = unpack("<f", f.read(4))[0]
                    type1n = unpack("B", f.read(1))[0]
                    value1n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1n = unpack("<f", f.read(4))[0]
                    vx2n = unpack("<f", f.read(4))[0]
                    vy2n = unpack("<f", f.read(4))[0]
                    vz2n = unpack("<f", f.read(4))[0]
                    type2n = unpack("B", f.read(1))[0]
                    value2n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2n = unpack("<f", f.read(4))[0]
                    vx3n = unpack("<f", f.read(4))[0]
                    vy3n = unpack("<f", f.read(4))[0]
                    vz3n = unpack("<f", f.read(4))[0]
                    type3n = unpack("B", f.read(1))[0]
                    value3n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3n = unpack("<f", f.read(4))[0]
                    vx4n = unpack("<f", f.read(4))[0]
                    vy4n = unpack("<f", f.read(4))[0]
                    vz4n = unpack("<f", f.read(4))[0]
                    type4n = unpack("B", f.read(1))[0]
                    value4n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4n = unpack("<f", f.read(4))[0]
                    vx5n = unpack("<f", f.read(4))[0]
                    vy5n = unpack("<f", f.read(4))[0]
                    vz5n = unpack("<f", f.read(4))[0]
                    type5n = unpack("B", f.read(1))[0]
                    value5n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5n = unpack("<f", f.read(4))[0]
                    vx6n = unpack("<f", f.read(4))[0]
                    vy6n = unpack("<f", f.read(4))[0]
                    vz6n = unpack("<f", f.read(4))[0]
                    type6n = unpack("B", f.read(1))[0]
                    value6n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6n = unpack("<f", f.read(4))[0]
                    vx7n = unpack("<f", f.read(4))[0]
                    vy7n = unpack("<f", f.read(4))[0]
                    vz7n = unpack("<f", f.read(4))[0]
                    type7n = unpack("B", f.read(1))[0]
                    value7n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7n = unpack("<f", f.read(4))[0]
                    vx8n = unpack("<f", f.read(4))[0]
                    vy8n = unpack("<f", f.read(4))[0]
                    vz8n = unpack("<f", f.read(4))[0]
                    type8n = unpack("B", f.read(1))[0]
                    value8n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8n = unpack("<f", f.read(4))[0]
                    vx9n = unpack("<f", f.read(4))[0]
                    vy9n = unpack("<f", f.read(4))[0]
                    vz9n = unpack("<f", f.read(4))[0]
                    type9n = unpack("B", f.read(1))[0]
                    value9n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9n = unpack("<f", f.read(4))[0]
                    vx10n = unpack("<f", f.read(4))[0]
                    vy10n = unpack("<f", f.read(4))[0]
                    vz10n = unpack("<f", f.read(4))[0]
                    type10n = unpack("B", f.read(1))[0]
                    value10n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10n = unpack("<f", f.read(4))[0]
                    vx11n = unpack("<f", f.read(4))[0]
                    vy11n = unpack("<f", f.read(4))[0]
                    vz11n = unpack("<f", f.read(4))[0]
                    type11n = unpack("B", f.read(1))[0]
                    value11n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11n = unpack("<f", f.read(4))[0]
                    vx12n = unpack("<f", f.read(4))[0]
                    vy12n = unpack("<f", f.read(4))[0]
                    vz12n = unpack("<f", f.read(4))[0]
                    type12n = unpack("B", f.read(1))[0]
                    value12n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12n = unpack("<f", f.read(4))[0]

                    f.seek(-192,1)

                    vx1o = unpack("<f", f.read(4))[0]
                    vy1o = unpack("<f", f.read(4))[0]
                    vz1o = unpack("<f", f.read(4))[0]
                    type1o = unpack("B", f.read(1))[0]
                    value1o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1o = unpack("<f", f.read(4))[0]
                    vx2o = unpack("<f", f.read(4))[0]
                    vy2o = unpack("<f", f.read(4))[0]
                    vz2o = unpack("<f", f.read(4))[0]
                    type2o = unpack("B", f.read(1))[0]
                    value2o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2o = unpack("<f", f.read(4))[0]
                    vx3o = unpack("<f", f.read(4))[0]
                    vy3o = unpack("<f", f.read(4))[0]
                    vz3o = unpack("<f", f.read(4))[0]
                    type3o = unpack("B", f.read(1))[0]
                    value3o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3o = unpack("<f", f.read(4))[0]
                    vx4o = unpack("<f", f.read(4))[0]
                    vy4o = unpack("<f", f.read(4))[0]
                    vz4o = unpack("<f", f.read(4))[0]
                    type4o = unpack("B", f.read(1))[0]
                    value4o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4o = unpack("<f", f.read(4))[0]
                    vx5o = unpack("<f", f.read(4))[0]
                    vy5o = unpack("<f", f.read(4))[0]
                    vz5o = unpack("<f", f.read(4))[0]
                    type5o = unpack("B", f.read(1))[0]
                    value5o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5o = unpack("<f", f.read(4))[0]
                    vx6o = unpack("<f", f.read(4))[0]
                    vy6o = unpack("<f", f.read(4))[0]
                    vz6o = unpack("<f", f.read(4))[0]
                    type6o = unpack("B", f.read(1))[0]
                    value6o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6o = unpack("<f", f.read(4))[0]
                    vx7o = unpack("<f", f.read(4))[0]
                    vy7o = unpack("<f", f.read(4))[0]
                    vz7o = unpack("<f", f.read(4))[0]
                    type7o = unpack("B", f.read(1))[0]
                    value7o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7o = unpack("<f", f.read(4))[0]
                    vx8o = unpack("<f", f.read(4))[0]
                    vy8o = unpack("<f", f.read(4))[0]
                    vz8o = unpack("<f", f.read(4))[0]
                    type8o = unpack("B", f.read(1))[0]
                    value8o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8o = unpack("<f", f.read(4))[0]
                    vx9o = unpack("<f", f.read(4))[0]
                    vy9o = unpack("<f", f.read(4))[0]
                    vz9o = unpack("<f", f.read(4))[0]
                    type9o = unpack("B", f.read(1))[0]
                    value9o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9o = unpack("<f", f.read(4))[0]
                    vx10o = unpack("<f", f.read(4))[0]
                    vy10o = unpack("<f", f.read(4))[0]
                    vz10o = unpack("<f", f.read(4))[0]
                    type10o = unpack("B", f.read(1))[0]
                    value10o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10o = unpack("<f", f.read(4))[0]
                    vx11o = unpack("<f", f.read(4))[0]
                    vy11o = unpack("<f", f.read(4))[0]
                    vz11o = unpack("<f", f.read(4))[0]
                    type11o = unpack("B", f.read(1))[0]
                    value11o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11o = unpack("<f", f.read(4))[0]
                    vx12o = unpack("<f", f.read(4))[0]
                    vy12o = unpack("<f", f.read(4))[0]
                    vz12o = unpack("<f", f.read(4))[0]
                    type12o = unpack("B", f.read(1))[0]
                    value12o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12o = unpack("<f", f.read(4))[0]

                    

                    


                    fa_1c = bm_1hhhhh.verts.new([-vx1c,-vy1c,-vz1c]) # 0
                    fb_1c = bm_1hhhhh.verts.new([-vx2c,-vy2c,-vz2c]) # 1
                    fc_1c = bm_1hhhhh.verts.new([-vx3c,-vy3c,-vz3c]) # 2
                    fd_1c = bm_1hhhhh.verts.new([-vx4c,-vy4c,-vz4c]) # 3
                    fe_1c = bm_1hhhhh.verts.new([-vx5c,-vy5c,-vz5c]) # 4
                    ff_1c = bm_1hhhhh.verts.new([-vx6c,-vy6c,-vz6c]) # 5
                    fg_1c = bm_1hhhhh.verts.new([-vx7c,-vy7c,-vz7c]) # 6
                    fh_1c = bm_1hhhhh.verts.new([-vx8c,-vy8c,-vz8c]) # 7
                    fi_1c = bm_1hhhhh.verts.new([-vx9c,-vy9c,-vz9c]) # 8
                    fj_1c = bm_1hhhhh.verts.new([-vx10c,-vy10c,-vz10c]) # 9
                    fk_1c = bm_1hhhhh.verts.new([-vx11c,-vy11c,-vz11c]) # 10
                    fl_1c = bm_1hhhhh.verts.new([-vx12c,-vy12c,-vz12c]) # 11

                    


                    fa111 = bm_1hhh.verts.new([-vx111,-vy111,-vz111]) # 0
                    fb111 = bm_1hhh.verts.new([-vx211,-vy211,-vz211]) # 1
                    fc111 = bm_1hhh.verts.new([-vx311,-vy311,-vz311]) # 2
                    fd111 = bm_1hhh.verts.new([-vx411,-vy411,-vz411]) # 3
                    fe111 = bm_1hhh.verts.new([-vx511,-vy511,-vz511]) # 4
                    ff111 = bm_1hhh.verts.new([-vx611,-vy611,-vz611]) # 5
                    fg111 = bm_1hhh.verts.new([-vx711,-vy711,-vz711]) # 6
                    fh111 = bm_1hhh.verts.new([-vx811,-vy811,-vz811]) # 7
                    fi111 = bm_1hhh.verts.new([-vx911,-vy911,-vz911]) # 8
                    fj111 = bm_1hhh.verts.new([-vx1011,-vy1011,-vz1011]) # 9
                    fk111 = bm_1hhh.verts.new([-vx1111,-vy1111,-vz1111]) # 10
                    fl111 = bm_1hhh.verts.new([-vx1211,-vy1211,-vz1211]) # 11

                    fa1 = bm_1h.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1h.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1h.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1h.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1h.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1h.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1h.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1h.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1h.verts.new([-vx9,-vy9,-vz9]) # 8
                    fj1 = bm_1h.verts.new([-vx10,-vy10,-vz10]) # 9
                    fk1 = bm_1h.verts.new([-vx11,-vy11,-vz11]) # 10
                    fl1 = bm_1h.verts.new([-vx12,-vy12,-vz12]) # 11

                    fa11 = bm_1hh.verts.new([-vx11a,-vy11a,-vz11a]) # 0
                    fb11 = bm_1hh.verts.new([-vx21a,-vy21a,-vz21a]) # 1
                    fc11 = bm_1hh.verts.new([-vx31a,-vy31a,-vz31a]) # 2
                    fd11 = bm_1hh.verts.new([-vx41a,-vy41a,-vz41a]) # 3
                    fe11 = bm_1hh.verts.new([-vx51a,-vy51a,-vz51a]) # 4
                    ff11 = bm_1hh.verts.new([-vx61a,-vy61a,-vz61a]) # 5
                    fg11 = bm_1hh.verts.new([-vx71a,-vy71a,-vz71a]) # 6
                    fh11 = bm_1hh.verts.new([-vx81a,-vy81a,-vz81a]) # 7
                    fi11 = bm_1hh.verts.new([-vx91a,-vy91a,-vz91a]) # 8
                    fj11 = bm_1hh.verts.new([-vx101a,-vy101a,-vz101a]) # 9
                    fk11 = bm_1hh.verts.new([-vx111a,-vy111a,-vz111a]) # 10
                    fl11 = bm_1hh.verts.new([-vx121a,-vy121a,-vz121a]) # 11

                    fa_1 = bm_1hhhh.verts.new([-vx1_1,-vy1_1,-vz1_1]) # 0
                    fb_1 = bm_1hhhh.verts.new([-vx2_1,-vy2_1,-vz2_1]) # 1
                    fc_1 = bm_1hhhh.verts.new([-vx3_1,-vy3_1,-vz3_1]) # 2
                    fd_1 = bm_1hhhh.verts.new([-vx4_1,-vy4_1,-vz4_1]) # 3
                    fe_1 = bm_1hhhh.verts.new([-vx5_1,-vy5_1,-vz5_1]) # 4
                    ff_1 = bm_1hhhh.verts.new([-vx6_1,-vy6_1,-vz6_1]) # 5
                    fg_1 = bm_1hhhh.verts.new([-vx7_1,-vy7_1,-vz7_1]) # 6
                    fh_1 = bm_1hhhh.verts.new([-vx8_1,-vy8_1,-vz8_1]) # 7
                    fi_1 = bm_1hhhh.verts.new([-vx9_1,-vy9_1,-vz9_1]) # 8
                    fj_1 = bm_1hhhh.verts.new([-vx10_1,-vy10_1,-vz10_1]) # 9
                    fk_1 = bm_1hhhh.verts.new([-vx11_1,-vy11_1,-vz11_1]) # 10
                    fl_1 = bm_1hhhh.verts.new([-vx12_1,-vy12_1,-vz12_1]) # 11

                    fa_1d = bm_1hhhhhh.verts.new([-vx1d,-vy1d,-vz1d]) # 0
                    fb_1d = bm_1hhhhhh.verts.new([-vx2d,-vy2d,-vz2d]) # 1
                    fc_1d = bm_1hhhhhh.verts.new([-vx3d,-vy3d,-vz3d]) # 2
                    fd_1d = bm_1hhhhhh.verts.new([-vx4d,-vy4d,-vz4d]) # 3
                    fe_1d = bm_1hhhhhh.verts.new([-vx5d,-vy5d,-vz5d]) # 4
                    ff_1d = bm_1hhhhhh.verts.new([-vx6d,-vy6d,-vz6d]) # 5
                    fg_1d = bm_1hhhhhh.verts.new([-vx7d,-vy7d,-vz7d]) # 6
                    fh_1d = bm_1hhhhhh.verts.new([-vx8d,-vy8d,-vz8d]) # 7
                    fi_1d = bm_1hhhhhh.verts.new([-vx9d,-vy9d,-vz9d]) # 8
                    fj_1d = bm_1hhhhhh.verts.new([-vx10d,-vy10d,-vz10d]) # 9
                    fk_1d = bm_1hhhhhh.verts.new([-vx11d,-vy11d,-vz11d]) # 10
                    fl_1d = bm_1hhhhhh.verts.new([-vx12d,-vy12d,-vz12d]) # 11

                    fa_1e = bm_1hhhhhhh.verts.new([-vx1e,-vy1e,-vz1e]) # 0
                    fb_1e = bm_1hhhhhhh.verts.new([-vx2e,-vy2e,-vz2e]) # 1
                    fc_1e = bm_1hhhhhhh.verts.new([-vx3e,-vy3e,-vz3e]) # 2
                    fd_1e = bm_1hhhhhhh.verts.new([-vx4e,-vy4e,-vz4e]) # 3
                    fe_1e = bm_1hhhhhhh.verts.new([-vx5e,-vy5e,-vz5e]) # 4
                    ff_1e = bm_1hhhhhhh.verts.new([-vx6e,-vy6e,-vz6e]) # 5
                    fg_1e = bm_1hhhhhhh.verts.new([-vx7e,-vy7e,-vz7e]) # 6
                    fh_1e = bm_1hhhhhhh.verts.new([-vx8e,-vy8e,-vz8e]) # 7
                    fi_1e = bm_1hhhhhhh.verts.new([-vx9e,-vy9e,-vz9e]) # 8
                    fj_1e = bm_1hhhhhhh.verts.new([-vx10e,-vy10e,-vz10e]) # 9
                    fk_1e = bm_1hhhhhhh.verts.new([-vx11e,-vy11e,-vz11e]) # 10
                    fl_1e = bm_1hhhhhhh.verts.new([-vx12e,-vy12e,-vz12e]) # 11


                    fa_1f = bm_1hhhhhhhh.verts.new([-vx1f,-vy1f,-vz1f]) # 0
                    fb_1f = bm_1hhhhhhhh.verts.new([-vx2f,-vy2f,-vz2f]) # 1
                    fc_1f = bm_1hhhhhhhh.verts.new([-vx3f,-vy3f,-vz3f]) # 2
                    fd_1f = bm_1hhhhhhhh.verts.new([-vx4f,-vy4f,-vz4f]) # 3
                    fe_1f = bm_1hhhhhhhh.verts.new([-vx5f,-vy5f,-vz5f]) # 4
                    ff_1f = bm_1hhhhhhhh.verts.new([-vx6f,-vy6f,-vz6f]) # 5
                    fg_1f = bm_1hhhhhhhh.verts.new([-vx7f,-vy7f,-vz7f]) # 6
                    fh_1f = bm_1hhhhhhhh.verts.new([-vx8f,-vy8f,-vz8f]) # 7
                    fi_1f = bm_1hhhhhhhh.verts.new([-vx9f,-vy9f,-vz9f]) # 8
                    fj_1f = bm_1hhhhhhhh.verts.new([-vx10f,-vy10f,-vz10f]) # 9
                    fk_1f = bm_1hhhhhhhh.verts.new([-vx11f,-vy11f,-vz11f]) # 10
                    fl_1f = bm_1hhhhhhhh.verts.new([-vx12f,-vy12f,-vz12f]) # 11

                    fa_1g = bm_1hhhhhhhhh.verts.new([-vx1g,-vy1g,-vz1g]) # 0
                    fb_1g = bm_1hhhhhhhhh.verts.new([-vx2g,-vy2g,-vz2g]) # 1
                    fc_1g = bm_1hhhhhhhhh.verts.new([-vx3g,-vy3g,-vz3g]) # 2
                    fd_1g = bm_1hhhhhhhhh.verts.new([-vx4g,-vy4g,-vz4g]) # 3
                    fe_1g = bm_1hhhhhhhhh.verts.new([-vx5g,-vy5g,-vz5g]) # 4
                    ff_1g = bm_1hhhhhhhhh.verts.new([-vx6g,-vy6g,-vz6g]) # 5
                    fg_1g = bm_1hhhhhhhhh.verts.new([-vx7g,-vy7g,-vz7g]) # 6
                    fh_1g = bm_1hhhhhhhhh.verts.new([-vx8g,-vy8g,-vz8g]) # 7
                    fi_1g = bm_1hhhhhhhhh.verts.new([-vx9g,-vy9g,-vz9g]) # 8
                    fj_1g = bm_1hhhhhhhhh.verts.new([-vx10g,-vy10g,-vz10g]) # 9
                    fk_1g = bm_1hhhhhhhhh.verts.new([-vx11g,-vy11g,-vz11g]) # 10
                    fl_1g = bm_1hhhhhhhhh.verts.new([-vx12g,-vy12g,-vz12g]) # 11

                    fa_1h = bm_1hhhhhhhhhh.verts.new([-vx1h,-vy1h,-vz1h]) # 0
                    fb_1h = bm_1hhhhhhhhhh.verts.new([-vx2h,-vy2h,-vz2h]) # 1
                    fc_1h = bm_1hhhhhhhhhh.verts.new([-vx3h,-vy3h,-vz3h]) # 2
                    fd_1h = bm_1hhhhhhhhhh.verts.new([-vx4h,-vy4h,-vz4h]) # 3
                    fe_1h = bm_1hhhhhhhhhh.verts.new([-vx5h,-vy5h,-vz5h]) # 4
                    ff_1h = bm_1hhhhhhhhhh.verts.new([-vx6h,-vy6h,-vz6h]) # 5
                    fg_1h = bm_1hhhhhhhhhh.verts.new([-vx7h,-vy7h,-vz7h]) # 6
                    fh_1h = bm_1hhhhhhhhhh.verts.new([-vx8h,-vy8h,-vz8h]) # 7
                    fi_1h = bm_1hhhhhhhhhh.verts.new([-vx9h,-vy9h,-vz9h]) # 8
                    fj_1h = bm_1hhhhhhhhhh.verts.new([-vx10h,-vy10h,-vz10h]) # 9
                    fk_1h = bm_1hhhhhhhhhh.verts.new([-vx11h,-vy11h,-vz11h]) # 10
                    fl_1h = bm_1hhhhhhhhhh.verts.new([-vx12h,-vy12h,-vz12h]) # 11

                    fa_1i = bm_1hhhhhhhhhhh.verts.new([-vx1i,-vy1i,-vz1i]) # 0
                    fb_1i = bm_1hhhhhhhhhhh.verts.new([-vx2i,-vy2i,-vz2i]) # 1
                    fc_1i = bm_1hhhhhhhhhhh.verts.new([-vx3i,-vy3i,-vz3i]) # 2
                    fd_1i = bm_1hhhhhhhhhhh.verts.new([-vx4i,-vy4i,-vz4i]) # 3
                    fe_1i = bm_1hhhhhhhhhhh.verts.new([-vx5i,-vy5i,-vz5i]) # 4
                    ff_1i = bm_1hhhhhhhhhhh.verts.new([-vx6i,-vy6i,-vz6i]) # 5
                    fg_1i = bm_1hhhhhhhhhhh.verts.new([-vx7i,-vy7i,-vz7i]) # 6
                    fh_1i = bm_1hhhhhhhhhhh.verts.new([-vx8i,-vy8i,-vz8i]) # 7
                    fi_1i = bm_1hhhhhhhhhhh.verts.new([-vx9i,-vy9i,-vz9i]) # 8
                    fj_1i = bm_1hhhhhhhhhhh.verts.new([-vx10i,-vy10i,-vz10i]) # 9
                    fk_1i = bm_1hhhhhhhhhhh.verts.new([-vx11i,-vy11i,-vz11i]) # 10
                    fl_1i = bm_1hhhhhhhhhhh.verts.new([-vx12i,-vy12i,-vz12i]) # 11

                    fa_1j = bm_1hhhhhhhhhhhh.verts.new([-vx1j,-vy1j,-vz1j]) # 0
                    fb_1j = bm_1hhhhhhhhhhhh.verts.new([-vx2j,-vy2j,-vz2j]) # 1
                    fc_1j = bm_1hhhhhhhhhhhh.verts.new([-vx3j,-vy3j,-vz3j]) # 2
                    fd_1j = bm_1hhhhhhhhhhhh.verts.new([-vx4j,-vy4j,-vz4j]) # 3
                    fe_1j = bm_1hhhhhhhhhhhh.verts.new([-vx5j,-vy5j,-vz5j]) # 4
                    ff_1j = bm_1hhhhhhhhhhhh.verts.new([-vx6j,-vy6j,-vz6j]) # 5
                    fg_1j = bm_1hhhhhhhhhhhh.verts.new([-vx7j,-vy7j,-vz7j]) # 6
                    fh_1j = bm_1hhhhhhhhhhhh.verts.new([-vx8j,-vy8j,-vz8j]) # 7
                    fi_1j = bm_1hhhhhhhhhhhh.verts.new([-vx9j,-vy9j,-vz9j]) # 8
                    fj_1j = bm_1hhhhhhhhhhhh.verts.new([-vx10j,-vy10j,-vz10j]) # 9
                    fk_1j = bm_1hhhhhhhhhhhh.verts.new([-vx11j,-vy11j,-vz11j]) # 10
                    fl_1j = bm_1hhhhhhhhhhhh.verts.new([-vx12j,-vy12j,-vz12j]) # 11

                    fa_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx1k,-vy1k,-vz1k]) # 0
                    fb_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx2k,-vy2k,-vz2k]) # 1
                    fc_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx3k,-vy3k,-vz3k]) # 2
                    fd_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx4k,-vy4k,-vz4k]) # 3
                    fe_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx5k,-vy5k,-vz5k]) # 4
                    ff_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx6k,-vy6k,-vz6k]) # 5
                    fg_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx7k,-vy7k,-vz7k]) # 6
                    fh_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx8k,-vy8k,-vz8k]) # 7
                    fi_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx9k,-vy9k,-vz9k]) # 8
                    fj_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx10k,-vy10k,-vz10k]) # 9
                    fk_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx11k,-vy11k,-vz11k]) # 10
                    fl_1k = bm_1hhhhhhhhhhhhh.verts.new([-vx12k,-vy12k,-vz12k]) # 11

                    fa_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx1l,-vy1l,-vz1l]) # 0
                    fb_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx2l,-vy2l,-vz2l]) # 1
                    fc_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx3l,-vy3l,-vz3l]) # 2
                    fd_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx4l,-vy4l,-vz4l]) # 3
                    fe_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx5l,-vy5l,-vz5l]) # 4
                    ff_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx6l,-vy6l,-vz6l]) # 5
                    fg_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx7l,-vy7l,-vz7l]) # 6
                    fh_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx8l,-vy8l,-vz8l]) # 7
                    fi_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx9l,-vy9l,-vz9l]) # 8
                    fj_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx10l,-vy10l,-vz10l]) # 9
                    fk_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx11l,-vy11l,-vz11l]) # 10
                    fl_1l = bm_1hhhhhhhhhhhhhh.verts.new([-vx12l,-vy12l,-vz12l]) # 11

                    fa_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx1m,-vy1m,-vz1m]) # 0
                    fb_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx2m,-vy2m,-vz2m]) # 1
                    fc_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx3m,-vy3m,-vz3m]) # 2
                    fd_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx4m,-vy4m,-vz4m]) # 3
                    fe_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx5m,-vy5m,-vz5m]) # 4
                    ff_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx6m,-vy6m,-vz6m]) # 5
                    fg_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx7m,-vy7m,-vz7m]) # 6
                    fh_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx8m,-vy8m,-vz8m]) # 7
                    fi_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx9m,-vy9m,-vz9m]) # 8
                    fj_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx10m,-vy10m,-vz10m]) # 9
                    fk_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx11m,-vy11m,-vz11m]) # 10
                    fl_1m = bm_1hhhhhhhhhhhhhhh.verts.new([-vx12m,-vy12m,-vz12m]) # 11

                    fa_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx1n,-vy1n,-vz1n]) # 0
                    fb_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx2n,-vy2n,-vz2n]) # 1
                    fc_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx3n,-vy3n,-vz3n]) # 2
                    fd_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx4n,-vy4n,-vz4n]) # 3
                    fe_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx5n,-vy5n,-vz5n]) # 4
                    ff_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx6n,-vy6n,-vz6n]) # 5
                    fg_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx7n,-vy7n,-vz7n]) # 6
                    fh_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx8n,-vy8n,-vz8n]) # 7
                    fi_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx9n,-vy9n,-vz9n]) # 8
                    fj_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx10n,-vy10n,-vz10n]) # 9
                    fk_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx11n,-vy11n,-vz11n]) # 10
                    fl_1n = bm_1hhhhhhhhhhhhhhhh.verts.new([-vx12n,-vy12n,-vz12n]) # 11

                    fa_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx1o,-vy1o,-vz1o]) # 0
                    fb_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx2o,-vy2o,-vz2o]) # 1
                    fc_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx3o,-vy3o,-vz3o]) # 2
                    fd_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx4o,-vy4o,-vz4o]) # 3
                    fe_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx5o,-vy5o,-vz5o]) # 4
                    ff_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx6o,-vy6o,-vz6o]) # 5
                    fg_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx7o,-vy7o,-vz7o]) # 6
                    fh_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx8o,-vy8o,-vz8o]) # 7
                    fi_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx9o,-vy9o,-vz9o]) # 8
                    fj_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx10o,-vy10o,-vz10o]) # 9
                    fk_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx11o,-vy11o,-vz11o]) # 10
                    fl_1o = bm_1hhhhhhhhhhhhhhhhh.verts.new([-vx12o,-vy12o,-vz12o]) # 11

                    if type1o == 1:
                        if type2o == 1:
                            if type3o == 0:
                                if type4o == 0:
                                    if type5o == 0:
                                        if type6o == 0:
                                            if type7o == 1:
                                                if type8o == 1:
                                                    if type9o == 0:
                                                        if type10o == 1:
                                                            if type11o == 1:
                                                                if type12o == 0:
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([fa_1o,fb_1o,fc_1o])
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([fb_1o,fc_1o,fd_1o])
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([fc_1o,fd_1o,fe_1o])
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([ff_1o,fg_1o,fh_1o])
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([fi_1o,fj_1o,fk_1o])
                                                                    bm_1hhhhhhhhhhhhhhhhh.faces.new([fj_1o,fk_1o,fl_1o])

                    if type1n == 1:
                        if type2n == 1:
                            if type3n == 0:
                                if type4n == 0:
                                    if type5n == 0:
                                        if type6n == 1:
                                            if type7n == 1:
                                                if type8n == 0:
                                                    if type9n == 1:
                                                        if type10n == 1:
                                                            if type11n == 0:
                                                                if type12n == 0:
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([fa_1n,fb_1n,fc_1n])
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([fb_1n,fc_1n,fd_1n])
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([fc_1n,fd_1n,fe_1n])
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([ff_1n,fg_1n,fh_1n])
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([fi_1n,fj_1n,fk_1n])
                                                                    bm_1hhhhhhhhhhhhhhhh.faces.new([fj_1n,fk_1n,fl_1n])

                    if type1m == 1:
                        if type2m == 1:
                            if type3m == 0:
                                if type4m == 1:
                                    if type5m == 1:
                                        if type6m == 0:
                                            if type7m == 0:
                                                if type8m == 0:
                                                    if type9m == 0:
                                                        if type10m == 1:
                                                            if type11m == 1:
                                                                if type12m == 0:
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([fa_1m,fb_1m,fc_1m])
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([fd_1m,fe_1m,ff_1m])
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([fe_1m,ff_1m,fg_1m])
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([ff_1m,fg_1m,fh_1m])
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([fg_1m,fh_1m,fi_1m])
                                                                    bm_1hhhhhhhhhhhhhhh.faces.new([fj_1m,fk_1m,fl_1m])

                    if type1l == 1:
                        if type2l == 1:
                            if type3l == 0:
                                if type4l == 1:
                                    if type5l == 1:
                                        if type6l == 0:
                                            if type7l == 0:
                                                if type8l == 0:
                                                    if type9l == 1:
                                                        if type10l == 1:
                                                            if type11l == 0:
                                                                if type12l == 0:
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([fa_1l,fb_1l,fc_1l])
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([fd_1l,fe_1l,ff_1l])
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([fe_1l,ff_1l,fg_1l])
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([ff_1l,fg_1l,fh_1l])
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([fi_1l,fj_1l,fk_1l])
                                                                    bm_1hhhhhhhhhhhhhh.faces.new([fj_1l,fk_1l,fl_1l])

                    if type1k == 1:
                        if type2k == 1:
                            if type3k == 0:
                                if type4k == 1:
                                    if type5k == 1:
                                        if type6k == 0:
                                            if type7k == 0:
                                                if type8k == 1:
                                                    if type9k == 1:
                                                        if type10k == 0:
                                                            if type11k == 0:
                                                                if type12k == 0:
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fa_1k,fb_1k,fc_1k])
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fd_1k,fe_1k,ff_1k])
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fe_1k,ff_1k,fg_1k])
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fh_1k,fi_1k,fj_1k])
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fi_1k,fj_1k,fk_1k])
                                                                    bm_1hhhhhhhhhhhhh.faces.new([fj_1k,fk_1k,fl_1k])

                    if type1j == 1:
                        if type2j == 1:
                            if type3j == 0:
                                if type4j == 1:
                                    if type5j == 1:
                                        if type6j == 0:
                                            if type7j == 1:
                                                if type8j == 1:
                                                    if type9j == 0:
                                                        if type10j == 0:
                                                            if type11j == 0:
                                                                if type12j == 0:
                                                                    bm_1hhhhhhhhhhhh.faces.new([fa_1j,fb_1j,fc_1j])
                                                                    bm_1hhhhhhhhhhhh.faces.new([fd_1j,fe_1j,ff_1j])
                                                                    bm_1hhhhhhhhhhhh.faces.new([fg_1j,fh_1j,fi_1j])
                                                                    bm_1hhhhhhhhhhhh.faces.new([fh_1j,fi_1j,fj_1j])
                                                                    bm_1hhhhhhhhhhhh.faces.new([fj_1j,fk_1j,fl_1j])

                    if type1i == 1:
                        if type2i == 1:
                            if type3i == 0:
                                if type4i == 0:
                                    if type5i == 0:
                                        if type6i == 0:
                                            if type7i == 0:
                                                if type8i == 0:
                                                    if type9i == 0:
                                                        if type10i == 1:
                                                            if type11i == 1:
                                                                if type12i == 0:
                                                                    bm_1hhhhhhhhhhh.faces.new([fa_1i,fb_1i,fc_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fb_1i,fc_1i,fd_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fc_1i,fd_1i,fe_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fd_1i,fe_1i,ff_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fe_1i,ff_1i,fg_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([ff_1i,fg_1i,fh_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fg_1i,fh_1i,fi_1i])
                                                                    bm_1hhhhhhhhhhh.faces.new([fj_1i,fk_1i,fl_1i])

                    if type1h == 1:
                        if type2h == 1:
                            if type3h == 0:
                                if type4h == 0:
                                    if type5h == 0:
                                        if type6h == 0:
                                            if type7h == 0:
                                                if type8h == 0:
                                                    if type9h == 1:
                                                        if type10h == 1:
                                                            if type11h == 0:
                                                                if type12h == 0:
                                                                    bm_1hhhhhhhhhh.faces.new([fa_1h,fb_1h,fc_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fb_1h,fc_1h,fd_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fc_1h,fd_1h,fe_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fd_1h,fe_1h,ff_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fe_1h,ff_1h,fg_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([ff_1h,fg_1h,fh_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fi_1h,fj_1h,fk_1h])
                                                                    bm_1hhhhhhhhhh.faces.new([fj_1h,fk_1h,fl_1h])


                    if type1g == 1:
                        if type2g == 1:
                            if type3g == 0:
                                if type4g == 0:
                                    if type5g == 0:
                                        if type6g == 0:
                                            if type7g == 0:
                                                if type8g == 1:
                                                    if type9g == 1:
                                                        if type10g == 0:
                                                            if type11g == 0:
                                                                if type12g == 0:
                                                                    bm_1hhhhhhhhh.faces.new([fa_1g,fb_1g,fc_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fb_1g,fc_1g,fd_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fc_1g,fd_1g,fe_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fd_1g,fe_1g,ff_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fe_1g,ff_1g,fg_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fh_1g,fi_1g,fj_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fi_1g,fj_1g,fk_1g])
                                                                    bm_1hhhhhhhhh.faces.new([fj_1g,fk_1g,fl_1g])


                    if type1f == 1:
                        if type2f == 1:
                            if type3f == 0:
                                if type4f == 0:
                                    if type5f == 0:
                                        if type6f == 0:
                                            if type7f == 1:
                                                if type8f == 1:
                                                    if type9f == 0:
                                                        if type10f == 0:
                                                            if type11f == 0:
                                                                if type12f == 0:
                                                                    bm_1hhhhhhhh.faces.new([fa_1f,fb_1f,fc_1f])
                                                                    bm_1hhhhhhhh.faces.new([fb_1f,fc_1f,fd_1f])
                                                                    bm_1hhhhhhhh.faces.new([fc_1f,fd_1f,fe_1f])
                                                                    bm_1hhhhhhhh.faces.new([fd_1f,fe_1f,ff_1f])
                                                                    bm_1hhhhhhhh.faces.new([fg_1f,fh_1f,fi_1f])
                                                                    bm_1hhhhhhhh.faces.new([fh_1f,fi_1f,fj_1f])
                                                                    bm_1hhhhhhhh.faces.new([fi_1f,fj_1f,fk_1f])
                                                                    bm_1hhhhhhhh.faces.new([fj_1f,fk_1f,fl_1f])

                    if type1e == 1:
                        if type2e == 1:
                            if type3e == 0:
                                if type4e == 0:
                                    if type5e == 0:
                                        if type6e == 1:
                                            if type7e == 1:
                                                if type8e == 0:
                                                    if type9e == 0:
                                                        if type10e == 0:
                                                            if type11e == 0:
                                                                if type12e == 0:
                                                                    bm_1hhhhhhh.faces.new([fa_1e,fb_1e,fc_1e])
                                                                    bm_1hhhhhhh.faces.new([fb_1e,fc_1e,fd_1e])
                                                                    bm_1hhhhhhh.faces.new([fc_1e,fd_1e,fe_1e])
                                                                    bm_1hhhhhhh.faces.new([ff_1e,fg_1e,fh_1e])
                                                                    bm_1hhhhhhh.faces.new([fg_1e,fh_1e,fi_1e])
                                                                    bm_1hhhhhhh.faces.new([fh_1e,fi_1e,fj_1e])
                                                                    bm_1hhhhhhh.faces.new([fi_1e,fj_1e,fk_1e])
                                                                    bm_1hhhhhhh.faces.new([fj_1e,fk_1e,fl_1e])

                    if type1d == 1:
                        if type2d == 1:
                            if type3d == 0:
                                if type4d == 1:
                                    if type5d == 1:
                                        if type6d == 0:
                                            if type7d == 0:
                                                if type8d == 0:
                                                    if type9d == 0:
                                                        if type10d == 0:
                                                            if type11d == 0:
                                                                if type12d == 0:
                                                                    bm_1hhhhhh.faces.new([fa_1d,fb_1d,fc_1d])
                                                                    bm_1hhhhhh.faces.new([fd_1d,fe_1d,ff_1d])
                                                                    bm_1hhhhhh.faces.new([fe_1d,ff_1d,fg_1d])
                                                                    bm_1hhhhhh.faces.new([ff_1d,fg_1d,fh_1d])
                                                                    bm_1hhhhhh.faces.new([fg_1d,fh_1d,fi_1d])
                                                                    bm_1hhhhhh.faces.new([fh_1d,fi_1d,fj_1d])
                                                                    bm_1hhhhhh.faces.new([fi_1d,fj_1d,fk_1d])
                                                                    bm_1hhhhhh.faces.new([fj_1d,fk_1d,fl_1d])

                    if type1c == 1:
                        if type2c == 1:
                            if type3c == 0:
                                if type4c == 0:
                                    if type5c == 0:
                                        if type6c == 0:
                                            if type7c == 1:
                                                if type8c == 1:
                                                    if type9c == 0:
                                                        if type10c == 0:
                                                            if type11c == 0:
                                                                if type12c == 0:
                                                                    bm_1hhhhh.faces.new([fa_1c,fb_1c,fc_1c])
                                                                    bm_1hhhhh.faces.new([fb_1c,fc_1c,fd_1c])
                                                                    bm_1hhhhh.faces.new([fc_1c,fd_1c,fe_1c])
                                                                    bm_1hhhhh.faces.new([fd_1c,fe_1c,ff_1c])
                                                                    bm_1hhhhh.faces.new([fg_1c,fh_1c,fi_1c])
                                                                    bm_1hhhhh.faces.new([fh_1c,fi_1c,fj_1c])
                                                                    bm_1hhhhh.faces.new([fi_1c,fj_1c,fk_1c])
                                                                    bm_1hhhhh.faces.new([fj_1c,fk_1c,fl_1c])

                    if type1_1 == 1:
                        if type2_1 == 1:
                            if type3_1 == 0:
                                if type4_1 == 0:
                                    if type5_1 == 0:
                                        if type6_1 == 0:
                                            if type7_1 == 0:
                                                if type8_1 == 0:
                                                    if type9_1 == 0:
                                                        if type10_1 == 0:
                                                            if type11_1 == 0:
                                                                if type12_1 == 0:
                                                                    bm_1hhhh.faces.new([fa_1,fb_1,fc_1])
                                                                    bm_1hhhh.faces.new([fb_1,fc_1,fd_1])
                                                                    bm_1hhhh.faces.new([fc_1,fd_1,fe_1])
                                                                    bm_1hhhh.faces.new([fd_1,fe_1,ff_1])
                                                                    bm_1hhhh.faces.new([fe_1,ff_1,fg_1])
                                                                    bm_1hhhh.faces.new([ff_1,fg_1,fh_1])
                                                                    bm_1hhhh.faces.new([fg_1,fh_1,fi_1])
                                                                    bm_1hhhh.faces.new([fh_1,fi_1,fj_1])
                                                                    bm_1hhhh.faces.new([fi_1,fj_1,fk_1])
                                                                    bm_1hhhh.faces.new([fj_1,fk_1,fl_1])

                    if type111 == 1:
                        if type211 == 1:
                            if type311 == 0:
                                if type411 == 1:
                                    if type511 == 1:
                                        if type611 == 0:
                                            if type711 == 1:
                                                if type811 == 1:
                                                    if type911 == 0:
                                                        if type1011 == 1:
                                                            if type1111 == 1:
                                                                if type1211 == 0:
                                                                    bm_1hhh.faces.new([fa111, fb111, fc111])
                                                                    bm_1hhh.faces.new([fd111, fe111, ff111])
                                                                    bm_1hhh.faces.new([fg111, fh111, fi111])
                                                                    bm_1hhh.faces.new([fj111, fk111, fl111])

                    if type11a == 1:
                        if type21a == 1:
                            if type31a == 0:
                                if type41a == 0:
                                    if type51a == 1:
                                        if type61a == 1:
                                            if type71a == 0:
                                                if type81a == 0:
                                                    if type91a == 1:
                                                        if type101a == 1:
                                                            if type111a == 0:
                                                                if type121a == 0:
                                                                    bm_1hh.faces.new([fa11, fb11, fc11])
                                                                    bm_1hh.faces.new([fb11, fc11, fd11])
                                                                    bm_1hh.faces.new([fe11, ff11, fg11])
                                                                    bm_1hh.faces.new([ff11, fg11, fh11])
                                                                    bm_1hh.faces.new([fi11, fj11, fk11])
                                                                    bm_1hh.faces.new([fj11, fk11, fl11])

                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 1:
                                        if type6 == 1:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    if type9 == 0:
                                                        if type10 == 0:
                                                            if type11 == 0:
                                                                if type12 == 0:
                                                                    bm_1h.faces.new([fa1, fb1, fc1])
                                                                    bm_1h.faces.new([fb1, fc1, fd1])
                                                                    bm_1h.faces.new([fe1, ff1, fg1])
                                                                    bm_1h.faces.new([ff1, fg1, fh1])
                                                                    bm_1h.faces.new([fg1, fh1, fi1])
                                                                    bm_1h.faces.new([fh1, fi1, fj1])
                                                                    bm_1h.faces.new([fi1, fj1, fk1])
                                                                    bm_1h.faces.new([fj1, fk1, fl1])

            elif vertexCount == 13:
                for i in range(vertexCount//13):
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
                    vx10 = unpack("<f", f.read(4))[0]
                    vy10 = unpack("<f", f.read(4))[0]
                    vz10 = unpack("<f", f.read(4))[0]
                    type10 = unpack("B", f.read(1))[0]
                    value10 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10 = unpack("<f", f.read(4))[0]
                    vx11 = unpack("<f", f.read(4))[0]
                    vy11 = unpack("<f", f.read(4))[0]
                    vz11 = unpack("<f", f.read(4))[0]
                    type11 = unpack("B", f.read(1))[0]
                    value11 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11 = unpack("<f", f.read(4))[0]
                    vx12 = unpack("<f", f.read(4))[0]
                    vy12 = unpack("<f", f.read(4))[0]
                    vz12 = unpack("<f", f.read(4))[0]
                    type12 = unpack("B", f.read(1))[0]
                    value12 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12 = unpack("<f", f.read(4))[0]
                    vx13 = unpack("<f", f.read(4))[0]
                    vy13 = unpack("<f", f.read(4))[0]
                    vz13 = unpack("<f", f.read(4))[0]
                    type13 = unpack("B", f.read(1))[0]
                    value13 = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13 = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

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
                    vx7a = unpack("<f", f.read(4))[0]
                    vy7a = unpack("<f", f.read(4))[0]
                    vz7a = unpack("<f", f.read(4))[0]
                    type7a = unpack("B", f.read(1))[0]
                    value7a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7a = unpack("<f", f.read(4))[0]
                    vx8a = unpack("<f", f.read(4))[0]
                    vy8a = unpack("<f", f.read(4))[0]
                    vz8a = unpack("<f", f.read(4))[0]
                    type8a = unpack("B", f.read(1))[0]
                    value8a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8a = unpack("<f", f.read(4))[0]
                    vx9a = unpack("<f", f.read(4))[0]
                    vy9a = unpack("<f", f.read(4))[0]
                    vz9a = unpack("<f", f.read(4))[0]
                    type9a = unpack("B", f.read(1))[0]
                    value9a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9a = unpack("<f", f.read(4))[0]
                    vx10a = unpack("<f", f.read(4))[0]
                    vy10a = unpack("<f", f.read(4))[0]
                    vz10a = unpack("<f", f.read(4))[0]
                    type10a = unpack("B", f.read(1))[0]
                    value10a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10a = unpack("<f", f.read(4))[0]
                    vx11a = unpack("<f", f.read(4))[0]
                    vy11a = unpack("<f", f.read(4))[0]
                    vz11a = unpack("<f", f.read(4))[0]
                    type11a = unpack("B", f.read(1))[0]
                    value11a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11a = unpack("<f", f.read(4))[0]
                    vx12a = unpack("<f", f.read(4))[0]
                    vy12a = unpack("<f", f.read(4))[0]
                    vz12a = unpack("<f", f.read(4))[0]
                    type12a = unpack("B", f.read(1))[0]
                    value12a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12a = unpack("<f", f.read(4))[0]
                    vx13a = unpack("<f", f.read(4))[0]
                    vy13a = unpack("<f", f.read(4))[0]
                    vz13a = unpack("<f", f.read(4))[0]
                    type13a = unpack("B", f.read(1))[0]
                    value13a = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13a = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

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
                    vx3b = unpack("<f", f.read(4))[0]
                    vy3b = unpack("<f", f.read(4))[0]
                    vz3b = unpack("<f", f.read(4))[0]
                    type3b = unpack("B", f.read(1))[0]
                    value3b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3b = unpack("<f", f.read(4))[0]
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
                    vx8b = unpack("<f", f.read(4))[0]
                    vy8b = unpack("<f", f.read(4))[0]
                    vz8b = unpack("<f", f.read(4))[0]
                    type8b = unpack("B", f.read(1))[0]
                    value8b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8b = unpack("<f", f.read(4))[0]
                    vx9b = unpack("<f", f.read(4))[0]
                    vy9b = unpack("<f", f.read(4))[0]
                    vz9b = unpack("<f", f.read(4))[0]
                    type9b = unpack("B", f.read(1))[0]
                    value9b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9b = unpack("<f", f.read(4))[0]
                    vx10b = unpack("<f", f.read(4))[0]
                    vy10b = unpack("<f", f.read(4))[0]
                    vz10b = unpack("<f", f.read(4))[0]
                    type10b = unpack("B", f.read(1))[0]
                    value10b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10b = unpack("<f", f.read(4))[0]
                    vx11b = unpack("<f", f.read(4))[0]
                    vy11b = unpack("<f", f.read(4))[0]
                    vz11b = unpack("<f", f.read(4))[0]
                    type11b = unpack("B", f.read(1))[0]
                    value11b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11b = unpack("<f", f.read(4))[0]
                    vx12b = unpack("<f", f.read(4))[0]
                    vy12b = unpack("<f", f.read(4))[0]
                    vz12b = unpack("<f", f.read(4))[0]
                    type12b = unpack("B", f.read(1))[0]
                    value12b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12b = unpack("<f", f.read(4))[0]
                    vx13b = unpack("<f", f.read(4))[0]
                    vy13b = unpack("<f", f.read(4))[0]
                    vz13b = unpack("<f", f.read(4))[0]
                    type13b = unpack("B", f.read(1))[0]
                    value13b = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13b = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1c = unpack("<f", f.read(4))[0]
                    vy1c = unpack("<f", f.read(4))[0]
                    vz1c = unpack("<f", f.read(4))[0]
                    type1c = unpack("B", f.read(1))[0]
                    value1c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1c = unpack("<f", f.read(4))[0]
                    vx2c = unpack("<f", f.read(4))[0]
                    vy2c = unpack("<f", f.read(4))[0]
                    vz2c = unpack("<f", f.read(4))[0]
                    type2c = unpack("B", f.read(1))[0]
                    value2c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2c = unpack("<f", f.read(4))[0]
                    vx3c = unpack("<f", f.read(4))[0]
                    vy3c = unpack("<f", f.read(4))[0]
                    vz3c = unpack("<f", f.read(4))[0]
                    type3c = unpack("B", f.read(1))[0]
                    value3c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3c = unpack("<f", f.read(4))[0]
                    vx4c = unpack("<f", f.read(4))[0]
                    vy4c = unpack("<f", f.read(4))[0]
                    vz4c = unpack("<f", f.read(4))[0]
                    type4c = unpack("B", f.read(1))[0]
                    value4c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4c = unpack("<f", f.read(4))[0]
                    vx5c = unpack("<f", f.read(4))[0]
                    vy5c = unpack("<f", f.read(4))[0]
                    vz5c = unpack("<f", f.read(4))[0]
                    type5c = unpack("B", f.read(1))[0]
                    value5c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5c = unpack("<f", f.read(4))[0]
                    vx6c = unpack("<f", f.read(4))[0]
                    vy6c = unpack("<f", f.read(4))[0]
                    vz6c = unpack("<f", f.read(4))[0]
                    type6c = unpack("B", f.read(1))[0]
                    value6c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6c = unpack("<f", f.read(4))[0]
                    vx7c = unpack("<f", f.read(4))[0]
                    vy7c = unpack("<f", f.read(4))[0]
                    vz7c = unpack("<f", f.read(4))[0]
                    type7c = unpack("B", f.read(1))[0]
                    value7c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7c = unpack("<f", f.read(4))[0]
                    vx8c = unpack("<f", f.read(4))[0]
                    vy8c = unpack("<f", f.read(4))[0]
                    vz8c = unpack("<f", f.read(4))[0]
                    type8c = unpack("B", f.read(1))[0]
                    value8c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8c = unpack("<f", f.read(4))[0]
                    vx9c = unpack("<f", f.read(4))[0]
                    vy9c = unpack("<f", f.read(4))[0]
                    vz9c = unpack("<f", f.read(4))[0]
                    type9c = unpack("B", f.read(1))[0]
                    value9c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9c = unpack("<f", f.read(4))[0]
                    vx10c = unpack("<f", f.read(4))[0]
                    vy10c = unpack("<f", f.read(4))[0]
                    vz10c = unpack("<f", f.read(4))[0]
                    type10c = unpack("B", f.read(1))[0]
                    value10c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10c = unpack("<f", f.read(4))[0]
                    vx11c = unpack("<f", f.read(4))[0]
                    vy11c = unpack("<f", f.read(4))[0]
                    vz11c = unpack("<f", f.read(4))[0]
                    type11c = unpack("B", f.read(1))[0]
                    value11c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11c = unpack("<f", f.read(4))[0]
                    vx12c = unpack("<f", f.read(4))[0]
                    vy12c = unpack("<f", f.read(4))[0]
                    vz12c = unpack("<f", f.read(4))[0]
                    type12c = unpack("B", f.read(1))[0]
                    value12c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12c = unpack("<f", f.read(4))[0]
                    vx13c = unpack("<f", f.read(4))[0]
                    vy13c = unpack("<f", f.read(4))[0]
                    vz13c = unpack("<f", f.read(4))[0]
                    type13c = unpack("B", f.read(1))[0]
                    value13c = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13c = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1d = unpack("<f", f.read(4))[0]
                    vy1d = unpack("<f", f.read(4))[0]
                    vz1d = unpack("<f", f.read(4))[0]
                    type1d = unpack("B", f.read(1))[0]
                    value1d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1d = unpack("<f", f.read(4))[0]
                    vx2d = unpack("<f", f.read(4))[0]
                    vy2d = unpack("<f", f.read(4))[0]
                    vz2d = unpack("<f", f.read(4))[0]
                    type2d = unpack("B", f.read(1))[0]
                    value2d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2d = unpack("<f", f.read(4))[0]
                    vx3d = unpack("<f", f.read(4))[0]
                    vy3d = unpack("<f", f.read(4))[0]
                    vz3d = unpack("<f", f.read(4))[0]
                    type3d = unpack("B", f.read(1))[0]
                    value3d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3d = unpack("<f", f.read(4))[0]
                    vx4d = unpack("<f", f.read(4))[0]
                    vy4d = unpack("<f", f.read(4))[0]
                    vz4d = unpack("<f", f.read(4))[0]
                    type4d = unpack("B", f.read(1))[0]
                    value4d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4d = unpack("<f", f.read(4))[0]
                    vx5d = unpack("<f", f.read(4))[0]
                    vy5d = unpack("<f", f.read(4))[0]
                    vz5d = unpack("<f", f.read(4))[0]
                    type5d = unpack("B", f.read(1))[0]
                    value5d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5d = unpack("<f", f.read(4))[0]
                    vx6d = unpack("<f", f.read(4))[0]
                    vy6d = unpack("<f", f.read(4))[0]
                    vz6d = unpack("<f", f.read(4))[0]
                    type6d = unpack("B", f.read(1))[0]
                    value6d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6d = unpack("<f", f.read(4))[0]
                    vx7d = unpack("<f", f.read(4))[0]
                    vy7d = unpack("<f", f.read(4))[0]
                    vz7d = unpack("<f", f.read(4))[0]
                    type7d = unpack("B", f.read(1))[0]
                    value7d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7d = unpack("<f", f.read(4))[0]
                    vx8d = unpack("<f", f.read(4))[0]
                    vy8d = unpack("<f", f.read(4))[0]
                    vz8d = unpack("<f", f.read(4))[0]
                    type8d = unpack("B", f.read(1))[0]
                    value8d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8d = unpack("<f", f.read(4))[0]
                    vx9d = unpack("<f", f.read(4))[0]
                    vy9d = unpack("<f", f.read(4))[0]
                    vz9d = unpack("<f", f.read(4))[0]
                    type9d = unpack("B", f.read(1))[0]
                    value9d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9d = unpack("<f", f.read(4))[0]
                    vx10d = unpack("<f", f.read(4))[0]
                    vy10d = unpack("<f", f.read(4))[0]
                    vz10d = unpack("<f", f.read(4))[0]
                    type10d = unpack("B", f.read(1))[0]
                    value10d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10d = unpack("<f", f.read(4))[0]
                    vx11d = unpack("<f", f.read(4))[0]
                    vy11d = unpack("<f", f.read(4))[0]
                    vz11d = unpack("<f", f.read(4))[0]
                    type11d = unpack("B", f.read(1))[0]
                    value11d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11d = unpack("<f", f.read(4))[0]
                    vx12d = unpack("<f", f.read(4))[0]
                    vy12d = unpack("<f", f.read(4))[0]
                    vz12d = unpack("<f", f.read(4))[0]
                    type12d = unpack("B", f.read(1))[0]
                    value12d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12d = unpack("<f", f.read(4))[0]
                    vx13d = unpack("<f", f.read(4))[0]
                    vy13d = unpack("<f", f.read(4))[0]
                    vz13d = unpack("<f", f.read(4))[0]
                    type13d = unpack("B", f.read(1))[0]
                    value13d = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13d = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1e = unpack("<f", f.read(4))[0]
                    vy1e = unpack("<f", f.read(4))[0]
                    vz1e = unpack("<f", f.read(4))[0]
                    type1e = unpack("B", f.read(1))[0]
                    value1e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1e = unpack("<f", f.read(4))[0]
                    vx2e = unpack("<f", f.read(4))[0]
                    vy2e = unpack("<f", f.read(4))[0]
                    vz2e = unpack("<f", f.read(4))[0]
                    type2e = unpack("B", f.read(1))[0]
                    value2e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2e = unpack("<f", f.read(4))[0]
                    vx3e = unpack("<f", f.read(4))[0]
                    vy3e = unpack("<f", f.read(4))[0]
                    vz3e = unpack("<f", f.read(4))[0]
                    type3e = unpack("B", f.read(1))[0]
                    value3e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3e = unpack("<f", f.read(4))[0]
                    vx4e = unpack("<f", f.read(4))[0]
                    vy4e = unpack("<f", f.read(4))[0]
                    vz4e = unpack("<f", f.read(4))[0]
                    type4e = unpack("B", f.read(1))[0]
                    value4e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4e = unpack("<f", f.read(4))[0]
                    vx5e = unpack("<f", f.read(4))[0]
                    vy5e = unpack("<f", f.read(4))[0]
                    vz5e = unpack("<f", f.read(4))[0]
                    type5e = unpack("B", f.read(1))[0]
                    value5e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5e = unpack("<f", f.read(4))[0]
                    vx6e = unpack("<f", f.read(4))[0]
                    vy6e = unpack("<f", f.read(4))[0]
                    vz6e = unpack("<f", f.read(4))[0]
                    type6e = unpack("B", f.read(1))[0]
                    value6e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6e = unpack("<f", f.read(4))[0]
                    vx7e = unpack("<f", f.read(4))[0]
                    vy7e = unpack("<f", f.read(4))[0]
                    vz7e = unpack("<f", f.read(4))[0]
                    type7e = unpack("B", f.read(1))[0]
                    value7e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7e = unpack("<f", f.read(4))[0]
                    vx8e = unpack("<f", f.read(4))[0]
                    vy8e = unpack("<f", f.read(4))[0]
                    vz8e = unpack("<f", f.read(4))[0]
                    type8e = unpack("B", f.read(1))[0]
                    value8e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8e = unpack("<f", f.read(4))[0]
                    vx9e = unpack("<f", f.read(4))[0]
                    vy9e = unpack("<f", f.read(4))[0]
                    vz9e = unpack("<f", f.read(4))[0]
                    type9e = unpack("B", f.read(1))[0]
                    value9e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9e = unpack("<f", f.read(4))[0]
                    vx10e = unpack("<f", f.read(4))[0]
                    vy10e = unpack("<f", f.read(4))[0]
                    vz10e = unpack("<f", f.read(4))[0]
                    type10e = unpack("B", f.read(1))[0]
                    value10e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10e = unpack("<f", f.read(4))[0]
                    vx11e = unpack("<f", f.read(4))[0]
                    vy11e = unpack("<f", f.read(4))[0]
                    vz11e = unpack("<f", f.read(4))[0]
                    type11e = unpack("B", f.read(1))[0]
                    value11e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11e = unpack("<f", f.read(4))[0]
                    vx12e = unpack("<f", f.read(4))[0]
                    vy12e = unpack("<f", f.read(4))[0]
                    vz12e = unpack("<f", f.read(4))[0]
                    type12e = unpack("B", f.read(1))[0]
                    value12e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12e = unpack("<f", f.read(4))[0]
                    vx13e = unpack("<f", f.read(4))[0]
                    vy13e = unpack("<f", f.read(4))[0]
                    vz13e = unpack("<f", f.read(4))[0]
                    type13e = unpack("B", f.read(1))[0]
                    value13e = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13e = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1f = unpack("<f", f.read(4))[0]
                    vy1f = unpack("<f", f.read(4))[0]
                    vz1f = unpack("<f", f.read(4))[0]
                    type1f = unpack("B", f.read(1))[0]
                    value1f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1f = unpack("<f", f.read(4))[0]
                    vx2f = unpack("<f", f.read(4))[0]
                    vy2f = unpack("<f", f.read(4))[0]
                    vz2f = unpack("<f", f.read(4))[0]
                    type2f = unpack("B", f.read(1))[0]
                    value2f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2f = unpack("<f", f.read(4))[0]
                    vx3f = unpack("<f", f.read(4))[0]
                    vy3f = unpack("<f", f.read(4))[0]
                    vz3f = unpack("<f", f.read(4))[0]
                    type3f = unpack("B", f.read(1))[0]
                    value3f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3f = unpack("<f", f.read(4))[0]
                    vx4f = unpack("<f", f.read(4))[0]
                    vy4f = unpack("<f", f.read(4))[0]
                    vz4f = unpack("<f", f.read(4))[0]
                    type4f = unpack("B", f.read(1))[0]
                    value4f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4f = unpack("<f", f.read(4))[0]
                    vx5f = unpack("<f", f.read(4))[0]
                    vy5f = unpack("<f", f.read(4))[0]
                    vz5f = unpack("<f", f.read(4))[0]
                    type5f = unpack("B", f.read(1))[0]
                    value5f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5f = unpack("<f", f.read(4))[0]
                    vx6f = unpack("<f", f.read(4))[0]
                    vy6f = unpack("<f", f.read(4))[0]
                    vz6f = unpack("<f", f.read(4))[0]
                    type6f = unpack("B", f.read(1))[0]
                    value6f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6f = unpack("<f", f.read(4))[0]
                    vx7f = unpack("<f", f.read(4))[0]
                    vy7f = unpack("<f", f.read(4))[0]
                    vz7f = unpack("<f", f.read(4))[0]
                    type7f = unpack("B", f.read(1))[0]
                    value7f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7f = unpack("<f", f.read(4))[0]
                    vx8f = unpack("<f", f.read(4))[0]
                    vy8f = unpack("<f", f.read(4))[0]
                    vz8f = unpack("<f", f.read(4))[0]
                    type8f = unpack("B", f.read(1))[0]
                    value8f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8f = unpack("<f", f.read(4))[0]
                    vx9f = unpack("<f", f.read(4))[0]
                    vy9f = unpack("<f", f.read(4))[0]
                    vz9f = unpack("<f", f.read(4))[0]
                    type9f = unpack("B", f.read(1))[0]
                    value9f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9f = unpack("<f", f.read(4))[0]
                    vx10f = unpack("<f", f.read(4))[0]
                    vy10f = unpack("<f", f.read(4))[0]
                    vz10f = unpack("<f", f.read(4))[0]
                    type10f = unpack("B", f.read(1))[0]
                    value10f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10f = unpack("<f", f.read(4))[0]
                    vx11f = unpack("<f", f.read(4))[0]
                    vy11f = unpack("<f", f.read(4))[0]
                    vz11f = unpack("<f", f.read(4))[0]
                    type11f = unpack("B", f.read(1))[0]
                    value11f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11f = unpack("<f", f.read(4))[0]
                    vx12f = unpack("<f", f.read(4))[0]
                    vy12f = unpack("<f", f.read(4))[0]
                    vz12f = unpack("<f", f.read(4))[0]
                    type12f = unpack("B", f.read(1))[0]
                    value12f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12f = unpack("<f", f.read(4))[0]
                    vx13f = unpack("<f", f.read(4))[0]
                    vy13f = unpack("<f", f.read(4))[0]
                    vz13f = unpack("<f", f.read(4))[0]
                    type13f = unpack("B", f.read(1))[0]
                    value13f = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13f = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1g = unpack("<f", f.read(4))[0]
                    vy1g = unpack("<f", f.read(4))[0]
                    vz1g = unpack("<f", f.read(4))[0]
                    type1g = unpack("B", f.read(1))[0]
                    value1g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1g = unpack("<f", f.read(4))[0]
                    vx2g = unpack("<f", f.read(4))[0]
                    vy2g = unpack("<f", f.read(4))[0]
                    vz2g = unpack("<f", f.read(4))[0]
                    type2g = unpack("B", f.read(1))[0]
                    value2g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2g = unpack("<f", f.read(4))[0]
                    vx3g = unpack("<f", f.read(4))[0]
                    vy3g = unpack("<f", f.read(4))[0]
                    vz3g = unpack("<f", f.read(4))[0]
                    type3g = unpack("B", f.read(1))[0]
                    value3g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3g = unpack("<f", f.read(4))[0]
                    vx4g = unpack("<f", f.read(4))[0]
                    vy4g = unpack("<f", f.read(4))[0]
                    vz4g = unpack("<f", f.read(4))[0]
                    type4g = unpack("B", f.read(1))[0]
                    value4g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4g = unpack("<f", f.read(4))[0]
                    vx5g = unpack("<f", f.read(4))[0]
                    vy5g = unpack("<f", f.read(4))[0]
                    vz5g = unpack("<f", f.read(4))[0]
                    type5g = unpack("B", f.read(1))[0]
                    value5g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5g = unpack("<f", f.read(4))[0]
                    vx6g = unpack("<f", f.read(4))[0]
                    vy6g = unpack("<f", f.read(4))[0]
                    vz6g = unpack("<f", f.read(4))[0]
                    type6g = unpack("B", f.read(1))[0]
                    value6g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6g = unpack("<f", f.read(4))[0]
                    vx7g = unpack("<f", f.read(4))[0]
                    vy7g = unpack("<f", f.read(4))[0]
                    vz7g = unpack("<f", f.read(4))[0]
                    type7g = unpack("B", f.read(1))[0]
                    value7g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7g = unpack("<f", f.read(4))[0]
                    vx8g = unpack("<f", f.read(4))[0]
                    vy8g = unpack("<f", f.read(4))[0]
                    vz8g = unpack("<f", f.read(4))[0]
                    type8g = unpack("B", f.read(1))[0]
                    value8g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8g = unpack("<f", f.read(4))[0]
                    vx9g = unpack("<f", f.read(4))[0]
                    vy9g = unpack("<f", f.read(4))[0]
                    vz9g = unpack("<f", f.read(4))[0]
                    type9g = unpack("B", f.read(1))[0]
                    value9g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9g = unpack("<f", f.read(4))[0]
                    vx10g = unpack("<f", f.read(4))[0]
                    vy10g = unpack("<f", f.read(4))[0]
                    vz10g = unpack("<f", f.read(4))[0]
                    type10g = unpack("B", f.read(1))[0]
                    value10g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10g = unpack("<f", f.read(4))[0]
                    vx11g = unpack("<f", f.read(4))[0]
                    vy11g = unpack("<f", f.read(4))[0]
                    vz11g = unpack("<f", f.read(4))[0]
                    type11g = unpack("B", f.read(1))[0]
                    value11g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11g = unpack("<f", f.read(4))[0]
                    vx12g = unpack("<f", f.read(4))[0]
                    vy12g = unpack("<f", f.read(4))[0]
                    vz12g = unpack("<f", f.read(4))[0]
                    type12g = unpack("B", f.read(1))[0]
                    value12g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12g = unpack("<f", f.read(4))[0]
                    vx13g = unpack("<f", f.read(4))[0]
                    vy13g = unpack("<f", f.read(4))[0]
                    vz13g = unpack("<f", f.read(4))[0]
                    type13g = unpack("B", f.read(1))[0]
                    value13g = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13g = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1h = unpack("<f", f.read(4))[0]
                    vy1h = unpack("<f", f.read(4))[0]
                    vz1h = unpack("<f", f.read(4))[0]
                    type1h = unpack("B", f.read(1))[0]
                    value1h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1h = unpack("<f", f.read(4))[0]
                    vx2h = unpack("<f", f.read(4))[0]
                    vy2h = unpack("<f", f.read(4))[0]
                    vz2h = unpack("<f", f.read(4))[0]
                    type2h = unpack("B", f.read(1))[0]
                    value2h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2h = unpack("<f", f.read(4))[0]
                    vx3h = unpack("<f", f.read(4))[0]
                    vy3h = unpack("<f", f.read(4))[0]
                    vz3h = unpack("<f", f.read(4))[0]
                    type3h = unpack("B", f.read(1))[0]
                    value3h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3h = unpack("<f", f.read(4))[0]
                    vx4h = unpack("<f", f.read(4))[0]
                    vy4h = unpack("<f", f.read(4))[0]
                    vz4h = unpack("<f", f.read(4))[0]
                    type4h = unpack("B", f.read(1))[0]
                    value4h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4h = unpack("<f", f.read(4))[0]
                    vx5h = unpack("<f", f.read(4))[0]
                    vy5h = unpack("<f", f.read(4))[0]
                    vz5h = unpack("<f", f.read(4))[0]
                    type5h = unpack("B", f.read(1))[0]
                    value5h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5h = unpack("<f", f.read(4))[0]
                    vx6h = unpack("<f", f.read(4))[0]
                    vy6h = unpack("<f", f.read(4))[0]
                    vz6h = unpack("<f", f.read(4))[0]
                    type6h = unpack("B", f.read(1))[0]
                    value6h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6h = unpack("<f", f.read(4))[0]
                    vx7h = unpack("<f", f.read(4))[0]
                    vy7h = unpack("<f", f.read(4))[0]
                    vz7h = unpack("<f", f.read(4))[0]
                    type7h = unpack("B", f.read(1))[0]
                    value7h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7h = unpack("<f", f.read(4))[0]
                    vx8h = unpack("<f", f.read(4))[0]
                    vy8h = unpack("<f", f.read(4))[0]
                    vz8h = unpack("<f", f.read(4))[0]
                    type8h = unpack("B", f.read(1))[0]
                    value8h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8h = unpack("<f", f.read(4))[0]
                    vx9h = unpack("<f", f.read(4))[0]
                    vy9h = unpack("<f", f.read(4))[0]
                    vz9h = unpack("<f", f.read(4))[0]
                    type9h = unpack("B", f.read(1))[0]
                    value9h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9h = unpack("<f", f.read(4))[0]
                    vx10h = unpack("<f", f.read(4))[0]
                    vy10h = unpack("<f", f.read(4))[0]
                    vz10h = unpack("<f", f.read(4))[0]
                    type10h = unpack("B", f.read(1))[0]
                    value10h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10h = unpack("<f", f.read(4))[0]
                    vx11h = unpack("<f", f.read(4))[0]
                    vy11h = unpack("<f", f.read(4))[0]
                    vz11h = unpack("<f", f.read(4))[0]
                    type11h = unpack("B", f.read(1))[0]
                    value11h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11h = unpack("<f", f.read(4))[0]
                    vx12h = unpack("<f", f.read(4))[0]
                    vy12h = unpack("<f", f.read(4))[0]
                    vz12h = unpack("<f", f.read(4))[0]
                    type12h = unpack("B", f.read(1))[0]
                    value12h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12h = unpack("<f", f.read(4))[0]
                    vx13h = unpack("<f", f.read(4))[0]
                    vy13h = unpack("<f", f.read(4))[0]
                    vz13h = unpack("<f", f.read(4))[0]
                    type13h = unpack("B", f.read(1))[0]
                    value13h = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13h = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1i = unpack("<f", f.read(4))[0]
                    vy1i = unpack("<f", f.read(4))[0]
                    vz1i = unpack("<f", f.read(4))[0]
                    type1i = unpack("B", f.read(1))[0]
                    value1i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1i = unpack("<f", f.read(4))[0]
                    vx2i = unpack("<f", f.read(4))[0]
                    vy2i = unpack("<f", f.read(4))[0]
                    vz2i = unpack("<f", f.read(4))[0]
                    type2i = unpack("B", f.read(1))[0]
                    value2i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2i = unpack("<f", f.read(4))[0]
                    vx3i = unpack("<f", f.read(4))[0]
                    vy3i = unpack("<f", f.read(4))[0]
                    vz3i = unpack("<f", f.read(4))[0]
                    type3i = unpack("B", f.read(1))[0]
                    value3i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3i = unpack("<f", f.read(4))[0]
                    vx4i = unpack("<f", f.read(4))[0]
                    vy4i = unpack("<f", f.read(4))[0]
                    vz4i = unpack("<f", f.read(4))[0]
                    type4i = unpack("B", f.read(1))[0]
                    value4i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4i = unpack("<f", f.read(4))[0]
                    vx5i = unpack("<f", f.read(4))[0]
                    vy5i = unpack("<f", f.read(4))[0]
                    vz5i = unpack("<f", f.read(4))[0]
                    type5i = unpack("B", f.read(1))[0]
                    value5i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5i = unpack("<f", f.read(4))[0]
                    vx6i = unpack("<f", f.read(4))[0]
                    vy6i = unpack("<f", f.read(4))[0]
                    vz6i = unpack("<f", f.read(4))[0]
                    type6i = unpack("B", f.read(1))[0]
                    value6i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6i = unpack("<f", f.read(4))[0]
                    vx7i = unpack("<f", f.read(4))[0]
                    vy7i = unpack("<f", f.read(4))[0]
                    vz7i = unpack("<f", f.read(4))[0]
                    type7i = unpack("B", f.read(1))[0]
                    value7i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7i = unpack("<f", f.read(4))[0]
                    vx8i = unpack("<f", f.read(4))[0]
                    vy8i = unpack("<f", f.read(4))[0]
                    vz8i = unpack("<f", f.read(4))[0]
                    type8i = unpack("B", f.read(1))[0]
                    value8i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8i = unpack("<f", f.read(4))[0]
                    vx9i = unpack("<f", f.read(4))[0]
                    vy9i = unpack("<f", f.read(4))[0]
                    vz9i = unpack("<f", f.read(4))[0]
                    type9i = unpack("B", f.read(1))[0]
                    value9i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9i = unpack("<f", f.read(4))[0]
                    vx10i = unpack("<f", f.read(4))[0]
                    vy10i = unpack("<f", f.read(4))[0]
                    vz10i = unpack("<f", f.read(4))[0]
                    type10i = unpack("B", f.read(1))[0]
                    value10i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10i = unpack("<f", f.read(4))[0]
                    vx11i = unpack("<f", f.read(4))[0]
                    vy11i = unpack("<f", f.read(4))[0]
                    vz11i = unpack("<f", f.read(4))[0]
                    type11i = unpack("B", f.read(1))[0]
                    value11i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11i = unpack("<f", f.read(4))[0]
                    vx12i = unpack("<f", f.read(4))[0]
                    vy12i = unpack("<f", f.read(4))[0]
                    vz12i = unpack("<f", f.read(4))[0]
                    type12i = unpack("B", f.read(1))[0]
                    value12i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12i = unpack("<f", f.read(4))[0]
                    vx13i = unpack("<f", f.read(4))[0]
                    vy13i = unpack("<f", f.read(4))[0]
                    vz13i = unpack("<f", f.read(4))[0]
                    type13i = unpack("B", f.read(1))[0]
                    value13i = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13i = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1j = unpack("<f", f.read(4))[0]
                    vy1j = unpack("<f", f.read(4))[0]
                    vz1j = unpack("<f", f.read(4))[0]
                    type1j = unpack("B", f.read(1))[0]
                    value1j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1j = unpack("<f", f.read(4))[0]
                    vx2j = unpack("<f", f.read(4))[0]
                    vy2j = unpack("<f", f.read(4))[0]
                    vz2j = unpack("<f", f.read(4))[0]
                    type2j = unpack("B", f.read(1))[0]
                    value2j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2j = unpack("<f", f.read(4))[0]
                    vx3j = unpack("<f", f.read(4))[0]
                    vy3j = unpack("<f", f.read(4))[0]
                    vz3j = unpack("<f", f.read(4))[0]
                    type3j = unpack("B", f.read(1))[0]
                    value3j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3j = unpack("<f", f.read(4))[0]
                    vx4j = unpack("<f", f.read(4))[0]
                    vy4j = unpack("<f", f.read(4))[0]
                    vz4j = unpack("<f", f.read(4))[0]
                    type4j = unpack("B", f.read(1))[0]
                    value4j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4j = unpack("<f", f.read(4))[0]
                    vx5j = unpack("<f", f.read(4))[0]
                    vy5j = unpack("<f", f.read(4))[0]
                    vz5j = unpack("<f", f.read(4))[0]
                    type5j = unpack("B", f.read(1))[0]
                    value5j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5j = unpack("<f", f.read(4))[0]
                    vx6j = unpack("<f", f.read(4))[0]
                    vy6j = unpack("<f", f.read(4))[0]
                    vz6j = unpack("<f", f.read(4))[0]
                    type6j = unpack("B", f.read(1))[0]
                    value6j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6j = unpack("<f", f.read(4))[0]
                    vx7j = unpack("<f", f.read(4))[0]
                    vy7j = unpack("<f", f.read(4))[0]
                    vz7j = unpack("<f", f.read(4))[0]
                    type7j = unpack("B", f.read(1))[0]
                    value7j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7j = unpack("<f", f.read(4))[0]
                    vx8j = unpack("<f", f.read(4))[0]
                    vy8j = unpack("<f", f.read(4))[0]
                    vz8j = unpack("<f", f.read(4))[0]
                    type8j = unpack("B", f.read(1))[0]
                    value8j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8j = unpack("<f", f.read(4))[0]
                    vx9j = unpack("<f", f.read(4))[0]
                    vy9j = unpack("<f", f.read(4))[0]
                    vz9j = unpack("<f", f.read(4))[0]
                    type9j = unpack("B", f.read(1))[0]
                    value9j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9j = unpack("<f", f.read(4))[0]
                    vx10j = unpack("<f", f.read(4))[0]
                    vy10j = unpack("<f", f.read(4))[0]
                    vz10j = unpack("<f", f.read(4))[0]
                    type10j = unpack("B", f.read(1))[0]
                    value10j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10j = unpack("<f", f.read(4))[0]
                    vx11j = unpack("<f", f.read(4))[0]
                    vy11j = unpack("<f", f.read(4))[0]
                    vz11j = unpack("<f", f.read(4))[0]
                    type11j = unpack("B", f.read(1))[0]
                    value11j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11j = unpack("<f", f.read(4))[0]
                    vx12j = unpack("<f", f.read(4))[0]
                    vy12j = unpack("<f", f.read(4))[0]
                    vz12j = unpack("<f", f.read(4))[0]
                    type12j = unpack("B", f.read(1))[0]
                    value12j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12j = unpack("<f", f.read(4))[0]
                    vx13j = unpack("<f", f.read(4))[0]
                    vy13j = unpack("<f", f.read(4))[0]
                    vz13j = unpack("<f", f.read(4))[0]
                    type13j = unpack("B", f.read(1))[0]
                    value13j = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13j = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1k = unpack("<f", f.read(4))[0]
                    vy1k = unpack("<f", f.read(4))[0]
                    vz1k = unpack("<f", f.read(4))[0]
                    type1k = unpack("B", f.read(1))[0]
                    value1k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1k = unpack("<f", f.read(4))[0]
                    vx2k = unpack("<f", f.read(4))[0]
                    vy2k = unpack("<f", f.read(4))[0]
                    vz2k = unpack("<f", f.read(4))[0]
                    type2k = unpack("B", f.read(1))[0]
                    value2k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2k = unpack("<f", f.read(4))[0]
                    vx3k = unpack("<f", f.read(4))[0]
                    vy3k = unpack("<f", f.read(4))[0]
                    vz3k = unpack("<f", f.read(4))[0]
                    type3k = unpack("B", f.read(1))[0]
                    value3k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3k = unpack("<f", f.read(4))[0]
                    vx4k = unpack("<f", f.read(4))[0]
                    vy4k = unpack("<f", f.read(4))[0]
                    vz4k = unpack("<f", f.read(4))[0]
                    type4k = unpack("B", f.read(1))[0]
                    value4k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4k = unpack("<f", f.read(4))[0]
                    vx5k = unpack("<f", f.read(4))[0]
                    vy5k = unpack("<f", f.read(4))[0]
                    vz5k = unpack("<f", f.read(4))[0]
                    type5k = unpack("B", f.read(1))[0]
                    value5k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5k = unpack("<f", f.read(4))[0]
                    vx6k = unpack("<f", f.read(4))[0]
                    vy6k = unpack("<f", f.read(4))[0]
                    vz6k = unpack("<f", f.read(4))[0]
                    type6k = unpack("B", f.read(1))[0]
                    value6k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6k = unpack("<f", f.read(4))[0]
                    vx7k = unpack("<f", f.read(4))[0]
                    vy7k = unpack("<f", f.read(4))[0]
                    vz7k = unpack("<f", f.read(4))[0]
                    type7k = unpack("B", f.read(1))[0]
                    value7k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7k = unpack("<f", f.read(4))[0]
                    vx8k = unpack("<f", f.read(4))[0]
                    vy8k = unpack("<f", f.read(4))[0]
                    vz8k = unpack("<f", f.read(4))[0]
                    type8k = unpack("B", f.read(1))[0]
                    value8k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8k = unpack("<f", f.read(4))[0]
                    vx9k = unpack("<f", f.read(4))[0]
                    vy9k = unpack("<f", f.read(4))[0]
                    vz9k = unpack("<f", f.read(4))[0]
                    type9k = unpack("B", f.read(1))[0]
                    value9k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9k = unpack("<f", f.read(4))[0]
                    vx10k = unpack("<f", f.read(4))[0]
                    vy10k = unpack("<f", f.read(4))[0]
                    vz10k = unpack("<f", f.read(4))[0]
                    type10k = unpack("B", f.read(1))[0]
                    value10k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10k = unpack("<f", f.read(4))[0]
                    vx11k = unpack("<f", f.read(4))[0]
                    vy11k = unpack("<f", f.read(4))[0]
                    vz11k = unpack("<f", f.read(4))[0]
                    type11k = unpack("B", f.read(1))[0]
                    value11k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11k = unpack("<f", f.read(4))[0]
                    vx12k = unpack("<f", f.read(4))[0]
                    vy12k = unpack("<f", f.read(4))[0]
                    vz12k = unpack("<f", f.read(4))[0]
                    type12k = unpack("B", f.read(1))[0]
                    value12k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12k = unpack("<f", f.read(4))[0]
                    vx13k = unpack("<f", f.read(4))[0]
                    vy13k = unpack("<f", f.read(4))[0]
                    vz13k = unpack("<f", f.read(4))[0]
                    type13k = unpack("B", f.read(1))[0]
                    value13k = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13k = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1l = unpack("<f", f.read(4))[0]
                    vy1l = unpack("<f", f.read(4))[0]
                    vz1l = unpack("<f", f.read(4))[0]
                    type1l = unpack("B", f.read(1))[0]
                    value1l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1l = unpack("<f", f.read(4))[0]
                    vx2l = unpack("<f", f.read(4))[0]
                    vy2l = unpack("<f", f.read(4))[0]
                    vz2l = unpack("<f", f.read(4))[0]
                    type2l = unpack("B", f.read(1))[0]
                    value2l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2l = unpack("<f", f.read(4))[0]
                    vx3l = unpack("<f", f.read(4))[0]
                    vy3l = unpack("<f", f.read(4))[0]
                    vz3l = unpack("<f", f.read(4))[0]
                    type3l = unpack("B", f.read(1))[0]
                    value3l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3l = unpack("<f", f.read(4))[0]
                    vx4l = unpack("<f", f.read(4))[0]
                    vy4l = unpack("<f", f.read(4))[0]
                    vz4l = unpack("<f", f.read(4))[0]
                    type4l = unpack("B", f.read(1))[0]
                    value4l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4l = unpack("<f", f.read(4))[0]
                    vx5l = unpack("<f", f.read(4))[0]
                    vy5l = unpack("<f", f.read(4))[0]
                    vz5l = unpack("<f", f.read(4))[0]
                    type5l = unpack("B", f.read(1))[0]
                    value5l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5l = unpack("<f", f.read(4))[0]
                    vx6l = unpack("<f", f.read(4))[0]
                    vy6l = unpack("<f", f.read(4))[0]
                    vz6l = unpack("<f", f.read(4))[0]
                    type6l = unpack("B", f.read(1))[0]
                    value6l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6l = unpack("<f", f.read(4))[0]
                    vx7l = unpack("<f", f.read(4))[0]
                    vy7l = unpack("<f", f.read(4))[0]
                    vz7l = unpack("<f", f.read(4))[0]
                    type7l = unpack("B", f.read(1))[0]
                    value7l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7l = unpack("<f", f.read(4))[0]
                    vx8l = unpack("<f", f.read(4))[0]
                    vy8l = unpack("<f", f.read(4))[0]
                    vz8l = unpack("<f", f.read(4))[0]
                    type8l = unpack("B", f.read(1))[0]
                    value8l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8l = unpack("<f", f.read(4))[0]
                    vx9l = unpack("<f", f.read(4))[0]
                    vy9l = unpack("<f", f.read(4))[0]
                    vz9l = unpack("<f", f.read(4))[0]
                    type9l = unpack("B", f.read(1))[0]
                    value9l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9l = unpack("<f", f.read(4))[0]
                    vx10l = unpack("<f", f.read(4))[0]
                    vy10l = unpack("<f", f.read(4))[0]
                    vz10l = unpack("<f", f.read(4))[0]
                    type10l = unpack("B", f.read(1))[0]
                    value10l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10l = unpack("<f", f.read(4))[0]
                    vx11l = unpack("<f", f.read(4))[0]
                    vy11l = unpack("<f", f.read(4))[0]
                    vz11l = unpack("<f", f.read(4))[0]
                    type11l = unpack("B", f.read(1))[0]
                    value11l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11l = unpack("<f", f.read(4))[0]
                    vx12l = unpack("<f", f.read(4))[0]
                    vy12l = unpack("<f", f.read(4))[0]
                    vz12l = unpack("<f", f.read(4))[0]
                    type12l = unpack("B", f.read(1))[0]
                    value12l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12l = unpack("<f", f.read(4))[0]
                    vx13l = unpack("<f", f.read(4))[0]
                    vy13l = unpack("<f", f.read(4))[0]
                    vz13l = unpack("<f", f.read(4))[0]
                    type13l = unpack("B", f.read(1))[0]
                    value13l = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13l = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1m = unpack("<f", f.read(4))[0]
                    vy1m = unpack("<f", f.read(4))[0]
                    vz1m = unpack("<f", f.read(4))[0]
                    type1m = unpack("B", f.read(1))[0]
                    value1m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1m = unpack("<f", f.read(4))[0]
                    vx2m = unpack("<f", f.read(4))[0]
                    vy2m = unpack("<f", f.read(4))[0]
                    vz2m = unpack("<f", f.read(4))[0]
                    type2m = unpack("B", f.read(1))[0]
                    value2m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2m = unpack("<f", f.read(4))[0]
                    vx3m = unpack("<f", f.read(4))[0]
                    vy3m = unpack("<f", f.read(4))[0]
                    vz3m = unpack("<f", f.read(4))[0]
                    type3m = unpack("B", f.read(1))[0]
                    value3m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3m = unpack("<f", f.read(4))[0]
                    vx4m = unpack("<f", f.read(4))[0]
                    vy4m = unpack("<f", f.read(4))[0]
                    vz4m = unpack("<f", f.read(4))[0]
                    type4m = unpack("B", f.read(1))[0]
                    value4m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4m = unpack("<f", f.read(4))[0]
                    vx5m = unpack("<f", f.read(4))[0]
                    vy5m = unpack("<f", f.read(4))[0]
                    vz5m = unpack("<f", f.read(4))[0]
                    type5m = unpack("B", f.read(1))[0]
                    value5m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5m = unpack("<f", f.read(4))[0]
                    vx6m = unpack("<f", f.read(4))[0]
                    vy6m = unpack("<f", f.read(4))[0]
                    vz6m = unpack("<f", f.read(4))[0]
                    type6m = unpack("B", f.read(1))[0]
                    value6m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6m = unpack("<f", f.read(4))[0]
                    vx7m = unpack("<f", f.read(4))[0]
                    vy7m = unpack("<f", f.read(4))[0]
                    vz7m = unpack("<f", f.read(4))[0]
                    type7m = unpack("B", f.read(1))[0]
                    value7m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7m = unpack("<f", f.read(4))[0]
                    vx8m = unpack("<f", f.read(4))[0]
                    vy8m = unpack("<f", f.read(4))[0]
                    vz8m = unpack("<f", f.read(4))[0]
                    type8m = unpack("B", f.read(1))[0]
                    value8m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8m = unpack("<f", f.read(4))[0]
                    vx9m = unpack("<f", f.read(4))[0]
                    vy9m = unpack("<f", f.read(4))[0]
                    vz9m = unpack("<f", f.read(4))[0]
                    type9m = unpack("B", f.read(1))[0]
                    value9m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9m = unpack("<f", f.read(4))[0]
                    vx10m = unpack("<f", f.read(4))[0]
                    vy10m = unpack("<f", f.read(4))[0]
                    vz10m = unpack("<f", f.read(4))[0]
                    type10m = unpack("B", f.read(1))[0]
                    value10m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10m = unpack("<f", f.read(4))[0]
                    vx11m = unpack("<f", f.read(4))[0]
                    vy11m = unpack("<f", f.read(4))[0]
                    vz11m = unpack("<f", f.read(4))[0]
                    type11m = unpack("B", f.read(1))[0]
                    value11m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11m = unpack("<f", f.read(4))[0]
                    vx12m = unpack("<f", f.read(4))[0]
                    vy12m = unpack("<f", f.read(4))[0]
                    vz12m = unpack("<f", f.read(4))[0]
                    type12m = unpack("B", f.read(1))[0]
                    value12m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12m = unpack("<f", f.read(4))[0]
                    vx13m = unpack("<f", f.read(4))[0]
                    vy13m = unpack("<f", f.read(4))[0]
                    vz13m = unpack("<f", f.read(4))[0]
                    type13m = unpack("B", f.read(1))[0]
                    value13m = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13m = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1n = unpack("<f", f.read(4))[0]
                    vy1n = unpack("<f", f.read(4))[0]
                    vz1n = unpack("<f", f.read(4))[0]
                    type1n = unpack("B", f.read(1))[0]
                    value1n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1n = unpack("<f", f.read(4))[0]
                    vx2n = unpack("<f", f.read(4))[0]
                    vy2n = unpack("<f", f.read(4))[0]
                    vz2n = unpack("<f", f.read(4))[0]
                    type2n = unpack("B", f.read(1))[0]
                    value2n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2n = unpack("<f", f.read(4))[0]
                    vx3n = unpack("<f", f.read(4))[0]
                    vy3n = unpack("<f", f.read(4))[0]
                    vz3n = unpack("<f", f.read(4))[0]
                    type3n = unpack("B", f.read(1))[0]
                    value3n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3n = unpack("<f", f.read(4))[0]
                    vx4n = unpack("<f", f.read(4))[0]
                    vy4n = unpack("<f", f.read(4))[0]
                    vz4n = unpack("<f", f.read(4))[0]
                    type4n = unpack("B", f.read(1))[0]
                    value4n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4n = unpack("<f", f.read(4))[0]
                    vx5n = unpack("<f", f.read(4))[0]
                    vy5n = unpack("<f", f.read(4))[0]
                    vz5n = unpack("<f", f.read(4))[0]
                    type5n = unpack("B", f.read(1))[0]
                    value5n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5n = unpack("<f", f.read(4))[0]
                    vx6n = unpack("<f", f.read(4))[0]
                    vy6n = unpack("<f", f.read(4))[0]
                    vz6n = unpack("<f", f.read(4))[0]
                    type6n = unpack("B", f.read(1))[0]
                    value6n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6n = unpack("<f", f.read(4))[0]
                    vx7n = unpack("<f", f.read(4))[0]
                    vy7n = unpack("<f", f.read(4))[0]
                    vz7n = unpack("<f", f.read(4))[0]
                    type7n = unpack("B", f.read(1))[0]
                    value7n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7n = unpack("<f", f.read(4))[0]
                    vx8n = unpack("<f", f.read(4))[0]
                    vy8n = unpack("<f", f.read(4))[0]
                    vz8n = unpack("<f", f.read(4))[0]
                    type8n = unpack("B", f.read(1))[0]
                    value8n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8n = unpack("<f", f.read(4))[0]
                    vx9n = unpack("<f", f.read(4))[0]
                    vy9n = unpack("<f", f.read(4))[0]
                    vz9n = unpack("<f", f.read(4))[0]
                    type9n = unpack("B", f.read(1))[0]
                    value9n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9n = unpack("<f", f.read(4))[0]
                    vx10n = unpack("<f", f.read(4))[0]
                    vy10n = unpack("<f", f.read(4))[0]
                    vz10n = unpack("<f", f.read(4))[0]
                    type10n = unpack("B", f.read(1))[0]
                    value10n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10n = unpack("<f", f.read(4))[0]
                    vx11n = unpack("<f", f.read(4))[0]
                    vy11n = unpack("<f", f.read(4))[0]
                    vz11n = unpack("<f", f.read(4))[0]
                    type11n = unpack("B", f.read(1))[0]
                    value11n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11n = unpack("<f", f.read(4))[0]
                    vx12n = unpack("<f", f.read(4))[0]
                    vy12n = unpack("<f", f.read(4))[0]
                    vz12n = unpack("<f", f.read(4))[0]
                    type12n = unpack("B", f.read(1))[0]
                    value12n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12n = unpack("<f", f.read(4))[0]
                    vx13n = unpack("<f", f.read(4))[0]
                    vy13n = unpack("<f", f.read(4))[0]
                    vz13n = unpack("<f", f.read(4))[0]
                    type13n = unpack("B", f.read(1))[0]
                    value13n = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13n = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1o = unpack("<f", f.read(4))[0]
                    vy1o = unpack("<f", f.read(4))[0]
                    vz1o = unpack("<f", f.read(4))[0]
                    type1o = unpack("B", f.read(1))[0]
                    value1o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1o = unpack("<f", f.read(4))[0]
                    vx2o = unpack("<f", f.read(4))[0]
                    vy2o = unpack("<f", f.read(4))[0]
                    vz2o = unpack("<f", f.read(4))[0]
                    type2o = unpack("B", f.read(1))[0]
                    value2o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2o = unpack("<f", f.read(4))[0]
                    vx3o = unpack("<f", f.read(4))[0]
                    vy3o = unpack("<f", f.read(4))[0]
                    vz3o = unpack("<f", f.read(4))[0]
                    type3o = unpack("B", f.read(1))[0]
                    value3o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3o = unpack("<f", f.read(4))[0]
                    vx4o = unpack("<f", f.read(4))[0]
                    vy4o = unpack("<f", f.read(4))[0]
                    vz4o = unpack("<f", f.read(4))[0]
                    type4o = unpack("B", f.read(1))[0]
                    value4o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4o = unpack("<f", f.read(4))[0]
                    vx5o = unpack("<f", f.read(4))[0]
                    vy5o = unpack("<f", f.read(4))[0]
                    vz5o = unpack("<f", f.read(4))[0]
                    type5o = unpack("B", f.read(1))[0]
                    value5o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5o = unpack("<f", f.read(4))[0]
                    vx6o = unpack("<f", f.read(4))[0]
                    vy6o = unpack("<f", f.read(4))[0]
                    vz6o = unpack("<f", f.read(4))[0]
                    type6o = unpack("B", f.read(1))[0]
                    value6o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6o = unpack("<f", f.read(4))[0]
                    vx7o = unpack("<f", f.read(4))[0]
                    vy7o = unpack("<f", f.read(4))[0]
                    vz7o = unpack("<f", f.read(4))[0]
                    type7o = unpack("B", f.read(1))[0]
                    value7o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7o = unpack("<f", f.read(4))[0]
                    vx8o = unpack("<f", f.read(4))[0]
                    vy8o = unpack("<f", f.read(4))[0]
                    vz8o = unpack("<f", f.read(4))[0]
                    type8o = unpack("B", f.read(1))[0]
                    value8o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8o = unpack("<f", f.read(4))[0]
                    vx9o = unpack("<f", f.read(4))[0]
                    vy9o = unpack("<f", f.read(4))[0]
                    vz9o = unpack("<f", f.read(4))[0]
                    type9o = unpack("B", f.read(1))[0]
                    value9o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9o = unpack("<f", f.read(4))[0]
                    vx10o = unpack("<f", f.read(4))[0]
                    vy10o = unpack("<f", f.read(4))[0]
                    vz10o = unpack("<f", f.read(4))[0]
                    type10o = unpack("B", f.read(1))[0]
                    value10o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10o = unpack("<f", f.read(4))[0]
                    vx11o = unpack("<f", f.read(4))[0]
                    vy11o = unpack("<f", f.read(4))[0]
                    vz11o = unpack("<f", f.read(4))[0]
                    type11o = unpack("B", f.read(1))[0]
                    value11o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11o = unpack("<f", f.read(4))[0]
                    vx12o = unpack("<f", f.read(4))[0]
                    vy12o = unpack("<f", f.read(4))[0]
                    vz12o = unpack("<f", f.read(4))[0]
                    type12o = unpack("B", f.read(1))[0]
                    value12o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12o = unpack("<f", f.read(4))[0]
                    vx13o = unpack("<f", f.read(4))[0]
                    vy13o = unpack("<f", f.read(4))[0]
                    vz13o = unpack("<f", f.read(4))[0]
                    type13o = unpack("B", f.read(1))[0]
                    value13o = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13o = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1p = unpack("<f", f.read(4))[0]
                    vy1p = unpack("<f", f.read(4))[0]
                    vz1p = unpack("<f", f.read(4))[0]
                    type1p = unpack("B", f.read(1))[0]
                    value1p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1p = unpack("<f", f.read(4))[0]
                    vx2p = unpack("<f", f.read(4))[0]
                    vy2p = unpack("<f", f.read(4))[0]
                    vz2p = unpack("<f", f.read(4))[0]
                    type2p = unpack("B", f.read(1))[0]
                    value2p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2p = unpack("<f", f.read(4))[0]
                    vx3p = unpack("<f", f.read(4))[0]
                    vy3p = unpack("<f", f.read(4))[0]
                    vz3p = unpack("<f", f.read(4))[0]
                    type3p = unpack("B", f.read(1))[0]
                    value3p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3p = unpack("<f", f.read(4))[0]
                    vx4p = unpack("<f", f.read(4))[0]
                    vy4p = unpack("<f", f.read(4))[0]
                    vz4p = unpack("<f", f.read(4))[0]
                    type4p = unpack("B", f.read(1))[0]
                    value4p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4p = unpack("<f", f.read(4))[0]
                    vx5p = unpack("<f", f.read(4))[0]
                    vy5p = unpack("<f", f.read(4))[0]
                    vz5p = unpack("<f", f.read(4))[0]
                    type5p = unpack("B", f.read(1))[0]
                    value5p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5p = unpack("<f", f.read(4))[0]
                    vx6p = unpack("<f", f.read(4))[0]
                    vy6p = unpack("<f", f.read(4))[0]
                    vz6p = unpack("<f", f.read(4))[0]
                    type6p = unpack("B", f.read(1))[0]
                    value6p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6p = unpack("<f", f.read(4))[0]
                    vx7p = unpack("<f", f.read(4))[0]
                    vy7p = unpack("<f", f.read(4))[0]
                    vz7p = unpack("<f", f.read(4))[0]
                    type7p = unpack("B", f.read(1))[0]
                    value7p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7p = unpack("<f", f.read(4))[0]
                    vx8p = unpack("<f", f.read(4))[0]
                    vy8p = unpack("<f", f.read(4))[0]
                    vz8p = unpack("<f", f.read(4))[0]
                    type8p = unpack("B", f.read(1))[0]
                    value8p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8p = unpack("<f", f.read(4))[0]
                    vx9p = unpack("<f", f.read(4))[0]
                    vy9p = unpack("<f", f.read(4))[0]
                    vz9p = unpack("<f", f.read(4))[0]
                    type9p = unpack("B", f.read(1))[0]
                    value9p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9p = unpack("<f", f.read(4))[0]
                    vx10p = unpack("<f", f.read(4))[0]
                    vy10p = unpack("<f", f.read(4))[0]
                    vz10p = unpack("<f", f.read(4))[0]
                    type10p = unpack("B", f.read(1))[0]
                    value10p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10p = unpack("<f", f.read(4))[0]
                    vx11p = unpack("<f", f.read(4))[0]
                    vy11p = unpack("<f", f.read(4))[0]
                    vz11p = unpack("<f", f.read(4))[0]
                    type11p = unpack("B", f.read(1))[0]
                    value11p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11p = unpack("<f", f.read(4))[0]
                    vx12p = unpack("<f", f.read(4))[0]
                    vy12p = unpack("<f", f.read(4))[0]
                    vz12p = unpack("<f", f.read(4))[0]
                    type12p = unpack("B", f.read(1))[0]
                    value12p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12p = unpack("<f", f.read(4))[0]
                    vx13p = unpack("<f", f.read(4))[0]
                    vy13p = unpack("<f", f.read(4))[0]
                    vz13p = unpack("<f", f.read(4))[0]
                    type13p = unpack("B", f.read(1))[0]
                    value13p = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13p = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1q = unpack("<f", f.read(4))[0]
                    vy1q = unpack("<f", f.read(4))[0]
                    vz1q = unpack("<f", f.read(4))[0]
                    type1q = unpack("B", f.read(1))[0]
                    value1q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1q = unpack("<f", f.read(4))[0]
                    vx2q = unpack("<f", f.read(4))[0]
                    vy2q = unpack("<f", f.read(4))[0]
                    vz2q = unpack("<f", f.read(4))[0]
                    type2q = unpack("B", f.read(1))[0]
                    value2q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2q = unpack("<f", f.read(4))[0]
                    vx3q = unpack("<f", f.read(4))[0]
                    vy3q = unpack("<f", f.read(4))[0]
                    vz3q = unpack("<f", f.read(4))[0]
                    type3q = unpack("B", f.read(1))[0]
                    value3q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3q = unpack("<f", f.read(4))[0]
                    vx4q = unpack("<f", f.read(4))[0]
                    vy4q = unpack("<f", f.read(4))[0]
                    vz4q = unpack("<f", f.read(4))[0]
                    type4q = unpack("B", f.read(1))[0]
                    value4q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4q = unpack("<f", f.read(4))[0]
                    vx5q = unpack("<f", f.read(4))[0]
                    vy5q = unpack("<f", f.read(4))[0]
                    vz5q = unpack("<f", f.read(4))[0]
                    type5q = unpack("B", f.read(1))[0]
                    value5q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5q = unpack("<f", f.read(4))[0]
                    vx6q = unpack("<f", f.read(4))[0]
                    vy6q = unpack("<f", f.read(4))[0]
                    vz6q = unpack("<f", f.read(4))[0]
                    type6q = unpack("B", f.read(1))[0]
                    value6q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6q = unpack("<f", f.read(4))[0]
                    vx7q = unpack("<f", f.read(4))[0]
                    vy7q = unpack("<f", f.read(4))[0]
                    vz7q = unpack("<f", f.read(4))[0]
                    type7q = unpack("B", f.read(1))[0]
                    value7q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7q = unpack("<f", f.read(4))[0]
                    vx8q = unpack("<f", f.read(4))[0]
                    vy8q = unpack("<f", f.read(4))[0]
                    vz8q = unpack("<f", f.read(4))[0]
                    type8q = unpack("B", f.read(1))[0]
                    value8q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8q = unpack("<f", f.read(4))[0]
                    vx9q = unpack("<f", f.read(4))[0]
                    vy9q = unpack("<f", f.read(4))[0]
                    vz9q = unpack("<f", f.read(4))[0]
                    type9q = unpack("B", f.read(1))[0]
                    value9q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9q = unpack("<f", f.read(4))[0]
                    vx10q = unpack("<f", f.read(4))[0]
                    vy10q = unpack("<f", f.read(4))[0]
                    vz10q = unpack("<f", f.read(4))[0]
                    type10q = unpack("B", f.read(1))[0]
                    value10q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10q = unpack("<f", f.read(4))[0]
                    vx11q = unpack("<f", f.read(4))[0]
                    vy11q = unpack("<f", f.read(4))[0]
                    vz11q = unpack("<f", f.read(4))[0]
                    type11q = unpack("B", f.read(1))[0]
                    value11q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11q = unpack("<f", f.read(4))[0]
                    vx12q = unpack("<f", f.read(4))[0]
                    vy12q = unpack("<f", f.read(4))[0]
                    vz12q = unpack("<f", f.read(4))[0]
                    type12q = unpack("B", f.read(1))[0]
                    value12q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12q = unpack("<f", f.read(4))[0]
                    vx13q = unpack("<f", f.read(4))[0]
                    vy13q = unpack("<f", f.read(4))[0]
                    vz13q = unpack("<f", f.read(4))[0]
                    type13q = unpack("B", f.read(1))[0]
                    value13q = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13q = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1r = unpack("<f", f.read(4))[0]
                    vy1r = unpack("<f", f.read(4))[0]
                    vz1r = unpack("<f", f.read(4))[0]
                    type1r = unpack("B", f.read(1))[0]
                    value1r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1r = unpack("<f", f.read(4))[0]
                    vx2r = unpack("<f", f.read(4))[0]
                    vy2r = unpack("<f", f.read(4))[0]
                    vz2r = unpack("<f", f.read(4))[0]
                    type2r = unpack("B", f.read(1))[0]
                    value2r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2r = unpack("<f", f.read(4))[0]
                    vx3r = unpack("<f", f.read(4))[0]
                    vy3r = unpack("<f", f.read(4))[0]
                    vz3r = unpack("<f", f.read(4))[0]
                    type3r = unpack("B", f.read(1))[0]
                    value3r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3r = unpack("<f", f.read(4))[0]
                    vx4r = unpack("<f", f.read(4))[0]
                    vy4r = unpack("<f", f.read(4))[0]
                    vz4r = unpack("<f", f.read(4))[0]
                    type4r = unpack("B", f.read(1))[0]
                    value4r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4r = unpack("<f", f.read(4))[0]
                    vx5r = unpack("<f", f.read(4))[0]
                    vy5r = unpack("<f", f.read(4))[0]
                    vz5r = unpack("<f", f.read(4))[0]
                    type5r = unpack("B", f.read(1))[0]
                    value5r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5r = unpack("<f", f.read(4))[0]
                    vx6r = unpack("<f", f.read(4))[0]
                    vy6r = unpack("<f", f.read(4))[0]
                    vz6r = unpack("<f", f.read(4))[0]
                    type6r = unpack("B", f.read(1))[0]
                    value6r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6r = unpack("<f", f.read(4))[0]
                    vx7r = unpack("<f", f.read(4))[0]
                    vy7r = unpack("<f", f.read(4))[0]
                    vz7r = unpack("<f", f.read(4))[0]
                    type7r = unpack("B", f.read(1))[0]
                    value7r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7r = unpack("<f", f.read(4))[0]
                    vx8r = unpack("<f", f.read(4))[0]
                    vy8r = unpack("<f", f.read(4))[0]
                    vz8r = unpack("<f", f.read(4))[0]
                    type8r = unpack("B", f.read(1))[0]
                    value8r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8r = unpack("<f", f.read(4))[0]
                    vx9r = unpack("<f", f.read(4))[0]
                    vy9r = unpack("<f", f.read(4))[0]
                    vz9r = unpack("<f", f.read(4))[0]
                    type9r = unpack("B", f.read(1))[0]
                    value9r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9r = unpack("<f", f.read(4))[0]
                    vx10r = unpack("<f", f.read(4))[0]
                    vy10r = unpack("<f", f.read(4))[0]
                    vz10r = unpack("<f", f.read(4))[0]
                    type10r = unpack("B", f.read(1))[0]
                    value10r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10r = unpack("<f", f.read(4))[0]
                    vx11r = unpack("<f", f.read(4))[0]
                    vy11r = unpack("<f", f.read(4))[0]
                    vz11r = unpack("<f", f.read(4))[0]
                    type11r = unpack("B", f.read(1))[0]
                    value11r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11r = unpack("<f", f.read(4))[0]
                    vx12r = unpack("<f", f.read(4))[0]
                    vy12r = unpack("<f", f.read(4))[0]
                    vz12r = unpack("<f", f.read(4))[0]
                    type12r = unpack("B", f.read(1))[0]
                    value12r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12r = unpack("<f", f.read(4))[0]
                    vx13r = unpack("<f", f.read(4))[0]
                    vy13r = unpack("<f", f.read(4))[0]
                    vz13r = unpack("<f", f.read(4))[0]
                    type13r = unpack("B", f.read(1))[0]
                    value13r = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13r = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1s = unpack("<f", f.read(4))[0]
                    vy1s = unpack("<f", f.read(4))[0]
                    vz1s = unpack("<f", f.read(4))[0]
                    type1s = unpack("B", f.read(1))[0]
                    value1s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1s = unpack("<f", f.read(4))[0]
                    vx2s = unpack("<f", f.read(4))[0]
                    vy2s = unpack("<f", f.read(4))[0]
                    vz2s = unpack("<f", f.read(4))[0]
                    type2s = unpack("B", f.read(1))[0]
                    value2s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2s = unpack("<f", f.read(4))[0]
                    vx3s = unpack("<f", f.read(4))[0]
                    vy3s = unpack("<f", f.read(4))[0]
                    vz3s = unpack("<f", f.read(4))[0]
                    type3s = unpack("B", f.read(1))[0]
                    value3s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3s = unpack("<f", f.read(4))[0]
                    vx4s = unpack("<f", f.read(4))[0]
                    vy4s = unpack("<f", f.read(4))[0]
                    vz4s = unpack("<f", f.read(4))[0]
                    type4s = unpack("B", f.read(1))[0]
                    value4s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4s = unpack("<f", f.read(4))[0]
                    vx5s = unpack("<f", f.read(4))[0]
                    vy5s = unpack("<f", f.read(4))[0]
                    vz5s = unpack("<f", f.read(4))[0]
                    type5s = unpack("B", f.read(1))[0]
                    value5s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5s = unpack("<f", f.read(4))[0]
                    vx6s = unpack("<f", f.read(4))[0]
                    vy6s = unpack("<f", f.read(4))[0]
                    vz6s = unpack("<f", f.read(4))[0]
                    type6s = unpack("B", f.read(1))[0]
                    value6s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6s = unpack("<f", f.read(4))[0]
                    vx7s = unpack("<f", f.read(4))[0]
                    vy7s = unpack("<f", f.read(4))[0]
                    vz7s = unpack("<f", f.read(4))[0]
                    type7s = unpack("B", f.read(1))[0]
                    value7s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7s = unpack("<f", f.read(4))[0]
                    vx8s = unpack("<f", f.read(4))[0]
                    vy8s = unpack("<f", f.read(4))[0]
                    vz8s = unpack("<f", f.read(4))[0]
                    type8s = unpack("B", f.read(1))[0]
                    value8s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8s = unpack("<f", f.read(4))[0]
                    vx9s = unpack("<f", f.read(4))[0]
                    vy9s = unpack("<f", f.read(4))[0]
                    vz9s = unpack("<f", f.read(4))[0]
                    type9s = unpack("B", f.read(1))[0]
                    value9s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9s = unpack("<f", f.read(4))[0]
                    vx10s = unpack("<f", f.read(4))[0]
                    vy10s = unpack("<f", f.read(4))[0]
                    vz10s = unpack("<f", f.read(4))[0]
                    type10s = unpack("B", f.read(1))[0]
                    value10s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10s = unpack("<f", f.read(4))[0]
                    vx11s = unpack("<f", f.read(4))[0]
                    vy11s = unpack("<f", f.read(4))[0]
                    vz11s = unpack("<f", f.read(4))[0]
                    type11s = unpack("B", f.read(1))[0]
                    value11s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11s = unpack("<f", f.read(4))[0]
                    vx12s = unpack("<f", f.read(4))[0]
                    vy12s = unpack("<f", f.read(4))[0]
                    vz12s = unpack("<f", f.read(4))[0]
                    type12s = unpack("B", f.read(1))[0]
                    value12s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12s = unpack("<f", f.read(4))[0]
                    vx13s = unpack("<f", f.read(4))[0]
                    vy13s = unpack("<f", f.read(4))[0]
                    vz13s = unpack("<f", f.read(4))[0]
                    type13s = unpack("B", f.read(1))[0]
                    value13s = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13s = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1t = unpack("<f", f.read(4))[0]
                    vy1t = unpack("<f", f.read(4))[0]
                    vz1t = unpack("<f", f.read(4))[0]
                    type1t = unpack("B", f.read(1))[0]
                    value1t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1t = unpack("<f", f.read(4))[0]
                    vx2t = unpack("<f", f.read(4))[0]
                    vy2t = unpack("<f", f.read(4))[0]
                    vz2t = unpack("<f", f.read(4))[0]
                    type2t = unpack("B", f.read(1))[0]
                    value2t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2t = unpack("<f", f.read(4))[0]
                    vx3t = unpack("<f", f.read(4))[0]
                    vy3t = unpack("<f", f.read(4))[0]
                    vz3t = unpack("<f", f.read(4))[0]
                    type3t = unpack("B", f.read(1))[0]
                    value3t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3t = unpack("<f", f.read(4))[0]
                    vx4t = unpack("<f", f.read(4))[0]
                    vy4t = unpack("<f", f.read(4))[0]
                    vz4t = unpack("<f", f.read(4))[0]
                    type4t = unpack("B", f.read(1))[0]
                    value4t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4t = unpack("<f", f.read(4))[0]
                    vx5t = unpack("<f", f.read(4))[0]
                    vy5t = unpack("<f", f.read(4))[0]
                    vz5t = unpack("<f", f.read(4))[0]
                    type5t = unpack("B", f.read(1))[0]
                    value5t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5t = unpack("<f", f.read(4))[0]
                    vx6t = unpack("<f", f.read(4))[0]
                    vy6t = unpack("<f", f.read(4))[0]
                    vz6t = unpack("<f", f.read(4))[0]
                    type6t = unpack("B", f.read(1))[0]
                    value6t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6t = unpack("<f", f.read(4))[0]
                    vx7t = unpack("<f", f.read(4))[0]
                    vy7t = unpack("<f", f.read(4))[0]
                    vz7t = unpack("<f", f.read(4))[0]
                    type7t = unpack("B", f.read(1))[0]
                    value7t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7t = unpack("<f", f.read(4))[0]
                    vx8t = unpack("<f", f.read(4))[0]
                    vy8t = unpack("<f", f.read(4))[0]
                    vz8t = unpack("<f", f.read(4))[0]
                    type8t = unpack("B", f.read(1))[0]
                    value8t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8t = unpack("<f", f.read(4))[0]
                    vx9t = unpack("<f", f.read(4))[0]
                    vy9t = unpack("<f", f.read(4))[0]
                    vz9t = unpack("<f", f.read(4))[0]
                    type9t = unpack("B", f.read(1))[0]
                    value9t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9t = unpack("<f", f.read(4))[0]
                    vx10t = unpack("<f", f.read(4))[0]
                    vy10t = unpack("<f", f.read(4))[0]
                    vz10t = unpack("<f", f.read(4))[0]
                    type10t = unpack("B", f.read(1))[0]
                    value10t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10t = unpack("<f", f.read(4))[0]
                    vx11t = unpack("<f", f.read(4))[0]
                    vy11t = unpack("<f", f.read(4))[0]
                    vz11t = unpack("<f", f.read(4))[0]
                    type11t = unpack("B", f.read(1))[0]
                    value11t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11t = unpack("<f", f.read(4))[0]
                    vx12t = unpack("<f", f.read(4))[0]
                    vy12t = unpack("<f", f.read(4))[0]
                    vz12t = unpack("<f", f.read(4))[0]
                    type12t = unpack("B", f.read(1))[0]
                    value12t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12t = unpack("<f", f.read(4))[0]
                    vx13t = unpack("<f", f.read(4))[0]
                    vy13t = unpack("<f", f.read(4))[0]
                    vz13t = unpack("<f", f.read(4))[0]
                    type13t = unpack("B", f.read(1))[0]
                    value13t = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13t = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1u = unpack("<f", f.read(4))[0]
                    vy1u = unpack("<f", f.read(4))[0]
                    vz1u = unpack("<f", f.read(4))[0]
                    type1u = unpack("B", f.read(1))[0]
                    value1u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1u = unpack("<f", f.read(4))[0]
                    vx2u = unpack("<f", f.read(4))[0]
                    vy2u = unpack("<f", f.read(4))[0]
                    vz2u = unpack("<f", f.read(4))[0]
                    type2u = unpack("B", f.read(1))[0]
                    value2u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2u = unpack("<f", f.read(4))[0]
                    vx3u = unpack("<f", f.read(4))[0]
                    vy3u = unpack("<f", f.read(4))[0]
                    vz3u = unpack("<f", f.read(4))[0]
                    type3u = unpack("B", f.read(1))[0]
                    value3u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3u = unpack("<f", f.read(4))[0]
                    vx4u = unpack("<f", f.read(4))[0]
                    vy4u = unpack("<f", f.read(4))[0]
                    vz4u = unpack("<f", f.read(4))[0]
                    type4u = unpack("B", f.read(1))[0]
                    value4u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4u = unpack("<f", f.read(4))[0]
                    vx5u = unpack("<f", f.read(4))[0]
                    vy5u = unpack("<f", f.read(4))[0]
                    vz5u = unpack("<f", f.read(4))[0]
                    type5u = unpack("B", f.read(1))[0]
                    value5u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5u = unpack("<f", f.read(4))[0]
                    vx6u = unpack("<f", f.read(4))[0]
                    vy6u = unpack("<f", f.read(4))[0]
                    vz6u = unpack("<f", f.read(4))[0]
                    type6u = unpack("B", f.read(1))[0]
                    value6u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6u = unpack("<f", f.read(4))[0]
                    vx7u = unpack("<f", f.read(4))[0]
                    vy7u = unpack("<f", f.read(4))[0]
                    vz7u = unpack("<f", f.read(4))[0]
                    type7u = unpack("B", f.read(1))[0]
                    value7u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7u = unpack("<f", f.read(4))[0]
                    vx8u = unpack("<f", f.read(4))[0]
                    vy8u = unpack("<f", f.read(4))[0]
                    vz8u = unpack("<f", f.read(4))[0]
                    type8u = unpack("B", f.read(1))[0]
                    value8u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8u = unpack("<f", f.read(4))[0]
                    vx9u = unpack("<f", f.read(4))[0]
                    vy9u = unpack("<f", f.read(4))[0]
                    vz9u = unpack("<f", f.read(4))[0]
                    type9u = unpack("B", f.read(1))[0]
                    value9u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9u = unpack("<f", f.read(4))[0]
                    vx10u = unpack("<f", f.read(4))[0]
                    vy10u = unpack("<f", f.read(4))[0]
                    vz10u = unpack("<f", f.read(4))[0]
                    type10u = unpack("B", f.read(1))[0]
                    value10u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10u = unpack("<f", f.read(4))[0]
                    vx11u = unpack("<f", f.read(4))[0]
                    vy11u = unpack("<f", f.read(4))[0]
                    vz11u = unpack("<f", f.read(4))[0]
                    type11u = unpack("B", f.read(1))[0]
                    value11u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11u = unpack("<f", f.read(4))[0]
                    vx12u = unpack("<f", f.read(4))[0]
                    vy12u = unpack("<f", f.read(4))[0]
                    vz12u = unpack("<f", f.read(4))[0]
                    type12u = unpack("B", f.read(1))[0]
                    value12u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12u = unpack("<f", f.read(4))[0]
                    vx13u = unpack("<f", f.read(4))[0]
                    vy13u = unpack("<f", f.read(4))[0]
                    vz13u = unpack("<f", f.read(4))[0]
                    type13u = unpack("B", f.read(1))[0]
                    value13u = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13u = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1v = unpack("<f", f.read(4))[0]
                    vy1v = unpack("<f", f.read(4))[0]
                    vz1v = unpack("<f", f.read(4))[0]
                    type1v = unpack("B", f.read(1))[0]
                    value1v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1v = unpack("<f", f.read(4))[0]
                    vx2v = unpack("<f", f.read(4))[0]
                    vy2v = unpack("<f", f.read(4))[0]
                    vz2v = unpack("<f", f.read(4))[0]
                    type2v = unpack("B", f.read(1))[0]
                    value2v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2v = unpack("<f", f.read(4))[0]
                    vx3v = unpack("<f", f.read(4))[0]
                    vy3v = unpack("<f", f.read(4))[0]
                    vz3v = unpack("<f", f.read(4))[0]
                    type3v = unpack("B", f.read(1))[0]
                    value3v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3v = unpack("<f", f.read(4))[0]
                    vx4v = unpack("<f", f.read(4))[0]
                    vy4v = unpack("<f", f.read(4))[0]
                    vz4v = unpack("<f", f.read(4))[0]
                    type4v = unpack("B", f.read(1))[0]
                    value4v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4v = unpack("<f", f.read(4))[0]
                    vx5v = unpack("<f", f.read(4))[0]
                    vy5v = unpack("<f", f.read(4))[0]
                    vz5v = unpack("<f", f.read(4))[0]
                    type5v = unpack("B", f.read(1))[0]
                    value5v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5v = unpack("<f", f.read(4))[0]
                    vx6v = unpack("<f", f.read(4))[0]
                    vy6v = unpack("<f", f.read(4))[0]
                    vz6v = unpack("<f", f.read(4))[0]
                    type6v = unpack("B", f.read(1))[0]
                    value6v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6v = unpack("<f", f.read(4))[0]
                    vx7v = unpack("<f", f.read(4))[0]
                    vy7v = unpack("<f", f.read(4))[0]
                    vz7v = unpack("<f", f.read(4))[0]
                    type7v = unpack("B", f.read(1))[0]
                    value7v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7v = unpack("<f", f.read(4))[0]
                    vx8v = unpack("<f", f.read(4))[0]
                    vy8v = unpack("<f", f.read(4))[0]
                    vz8v = unpack("<f", f.read(4))[0]
                    type8v = unpack("B", f.read(1))[0]
                    value8v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8v = unpack("<f", f.read(4))[0]
                    vx9v = unpack("<f", f.read(4))[0]
                    vy9v = unpack("<f", f.read(4))[0]
                    vz9v = unpack("<f", f.read(4))[0]
                    type9v = unpack("B", f.read(1))[0]
                    value9v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9v = unpack("<f", f.read(4))[0]
                    vx10v = unpack("<f", f.read(4))[0]
                    vy10v = unpack("<f", f.read(4))[0]
                    vz10v = unpack("<f", f.read(4))[0]
                    type10v = unpack("B", f.read(1))[0]
                    value10v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10v = unpack("<f", f.read(4))[0]
                    vx11v = unpack("<f", f.read(4))[0]
                    vy11v = unpack("<f", f.read(4))[0]
                    vz11v = unpack("<f", f.read(4))[0]
                    type11v = unpack("B", f.read(1))[0]
                    value11v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11v = unpack("<f", f.read(4))[0]
                    vx12v = unpack("<f", f.read(4))[0]
                    vy12v = unpack("<f", f.read(4))[0]
                    vz12v = unpack("<f", f.read(4))[0]
                    type12v = unpack("B", f.read(1))[0]
                    value12v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12v = unpack("<f", f.read(4))[0]
                    vx13v = unpack("<f", f.read(4))[0]
                    vy13v = unpack("<f", f.read(4))[0]
                    vz13v = unpack("<f", f.read(4))[0]
                    type13v = unpack("B", f.read(1))[0]
                    value13v = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13v = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1w = unpack("<f", f.read(4))[0]
                    vy1w = unpack("<f", f.read(4))[0]
                    vz1w = unpack("<f", f.read(4))[0]
                    type1w = unpack("B", f.read(1))[0]
                    value1w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1w = unpack("<f", f.read(4))[0]
                    vx2w = unpack("<f", f.read(4))[0]
                    vy2w = unpack("<f", f.read(4))[0]
                    vz2w = unpack("<f", f.read(4))[0]
                    type2w = unpack("B", f.read(1))[0]
                    value2w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2w = unpack("<f", f.read(4))[0]
                    vx3w = unpack("<f", f.read(4))[0]
                    vy3w = unpack("<f", f.read(4))[0]
                    vz3w = unpack("<f", f.read(4))[0]
                    type3w = unpack("B", f.read(1))[0]
                    value3w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3w = unpack("<f", f.read(4))[0]
                    vx4w = unpack("<f", f.read(4))[0]
                    vy4w = unpack("<f", f.read(4))[0]
                    vz4w = unpack("<f", f.read(4))[0]
                    type4w = unpack("B", f.read(1))[0]
                    value4w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4w = unpack("<f", f.read(4))[0]
                    vx5w = unpack("<f", f.read(4))[0]
                    vy5w = unpack("<f", f.read(4))[0]
                    vz5w = unpack("<f", f.read(4))[0]
                    type5w = unpack("B", f.read(1))[0]
                    value5w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5w = unpack("<f", f.read(4))[0]
                    vx6w = unpack("<f", f.read(4))[0]
                    vy6w = unpack("<f", f.read(4))[0]
                    vz6w = unpack("<f", f.read(4))[0]
                    type6w = unpack("B", f.read(1))[0]
                    value6w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6w = unpack("<f", f.read(4))[0]
                    vx7w = unpack("<f", f.read(4))[0]
                    vy7w = unpack("<f", f.read(4))[0]
                    vz7w = unpack("<f", f.read(4))[0]
                    type7w = unpack("B", f.read(1))[0]
                    value7w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7w = unpack("<f", f.read(4))[0]
                    vx8w = unpack("<f", f.read(4))[0]
                    vy8w = unpack("<f", f.read(4))[0]
                    vz8w = unpack("<f", f.read(4))[0]
                    type8w = unpack("B", f.read(1))[0]
                    value8w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8w = unpack("<f", f.read(4))[0]
                    vx9w = unpack("<f", f.read(4))[0]
                    vy9w = unpack("<f", f.read(4))[0]
                    vz9w = unpack("<f", f.read(4))[0]
                    type9w = unpack("B", f.read(1))[0]
                    value9w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9w = unpack("<f", f.read(4))[0]
                    vx10w = unpack("<f", f.read(4))[0]
                    vy10w = unpack("<f", f.read(4))[0]
                    vz10w = unpack("<f", f.read(4))[0]
                    type10w = unpack("B", f.read(1))[0]
                    value10w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10w = unpack("<f", f.read(4))[0]
                    vx11w = unpack("<f", f.read(4))[0]
                    vy11w = unpack("<f", f.read(4))[0]
                    vz11w = unpack("<f", f.read(4))[0]
                    type11w = unpack("B", f.read(1))[0]
                    value11w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11w = unpack("<f", f.read(4))[0]
                    vx12w = unpack("<f", f.read(4))[0]
                    vy12w = unpack("<f", f.read(4))[0]
                    vz12w = unpack("<f", f.read(4))[0]
                    type12w = unpack("B", f.read(1))[0]
                    value12w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12w = unpack("<f", f.read(4))[0]
                    vx13w = unpack("<f", f.read(4))[0]
                    vy13w = unpack("<f", f.read(4))[0]
                    vz13w = unpack("<f", f.read(4))[0]
                    type13w = unpack("B", f.read(1))[0]
                    value13w = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13w = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)



                    vx1x = unpack("<f", f.read(4))[0]
                    vy1x = unpack("<f", f.read(4))[0]
                    vz1x = unpack("<f", f.read(4))[0]
                    type1x = unpack("B", f.read(1))[0]
                    value1x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1x = unpack("<f", f.read(4))[0]
                    vx2x = unpack("<f", f.read(4))[0]
                    vy2x = unpack("<f", f.read(4))[0]
                    vz2x = unpack("<f", f.read(4))[0]
                    type2x = unpack("B", f.read(1))[0]
                    value2x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2x = unpack("<f", f.read(4))[0]
                    vx3x = unpack("<f", f.read(4))[0]
                    vy3x = unpack("<f", f.read(4))[0]
                    vz3x = unpack("<f", f.read(4))[0]
                    type3x = unpack("B", f.read(1))[0]
                    value3x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3x = unpack("<f", f.read(4))[0]
                    vx4x = unpack("<f", f.read(4))[0]
                    vy4x = unpack("<f", f.read(4))[0]
                    vz4x = unpack("<f", f.read(4))[0]
                    type4x = unpack("B", f.read(1))[0]
                    value4x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4x = unpack("<f", f.read(4))[0]
                    vx5x = unpack("<f", f.read(4))[0]
                    vy5x = unpack("<f", f.read(4))[0]
                    vz5x = unpack("<f", f.read(4))[0]
                    type5x = unpack("B", f.read(1))[0]
                    value5x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5x = unpack("<f", f.read(4))[0]
                    vx6x = unpack("<f", f.read(4))[0]
                    vy6x = unpack("<f", f.read(4))[0]
                    vz6x = unpack("<f", f.read(4))[0]
                    type6x = unpack("B", f.read(1))[0]
                    value6x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6x = unpack("<f", f.read(4))[0]
                    vx7x = unpack("<f", f.read(4))[0]
                    vy7x = unpack("<f", f.read(4))[0]
                    vz7x = unpack("<f", f.read(4))[0]
                    type7x = unpack("B", f.read(1))[0]
                    value7x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7x = unpack("<f", f.read(4))[0]
                    vx8x = unpack("<f", f.read(4))[0]
                    vy8x = unpack("<f", f.read(4))[0]
                    vz8x = unpack("<f", f.read(4))[0]
                    type8x = unpack("B", f.read(1))[0]
                    value8x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8x = unpack("<f", f.read(4))[0]
                    vx9x = unpack("<f", f.read(4))[0]
                    vy9x = unpack("<f", f.read(4))[0]
                    vz9x = unpack("<f", f.read(4))[0]
                    type9x = unpack("B", f.read(1))[0]
                    value9x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9x = unpack("<f", f.read(4))[0]
                    vx10x = unpack("<f", f.read(4))[0]
                    vy10x = unpack("<f", f.read(4))[0]
                    vz10x = unpack("<f", f.read(4))[0]
                    type10x = unpack("B", f.read(1))[0]
                    value10x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10x = unpack("<f", f.read(4))[0]
                    vx11x = unpack("<f", f.read(4))[0]
                    vy11x = unpack("<f", f.read(4))[0]
                    vz11x = unpack("<f", f.read(4))[0]
                    type11x = unpack("B", f.read(1))[0]
                    value11x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11x = unpack("<f", f.read(4))[0]
                    vx12x = unpack("<f", f.read(4))[0]
                    vy12x = unpack("<f", f.read(4))[0]
                    vz12x = unpack("<f", f.read(4))[0]
                    type12x = unpack("B", f.read(1))[0]
                    value12x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12x = unpack("<f", f.read(4))[0]
                    vx13x = unpack("<f", f.read(4))[0]
                    vy13x = unpack("<f", f.read(4))[0]
                    vz13x = unpack("<f", f.read(4))[0]
                    type13x = unpack("B", f.read(1))[0]
                    value13x = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13x = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1y = unpack("<f", f.read(4))[0]
                    vy1y = unpack("<f", f.read(4))[0]
                    vz1y = unpack("<f", f.read(4))[0]
                    type1y = unpack("B", f.read(1))[0]
                    value1y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1y = unpack("<f", f.read(4))[0]
                    vx2y = unpack("<f", f.read(4))[0]
                    vy2y = unpack("<f", f.read(4))[0]
                    vz2y = unpack("<f", f.read(4))[0]
                    type2y = unpack("B", f.read(1))[0]
                    value2y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2y = unpack("<f", f.read(4))[0]
                    vx3y = unpack("<f", f.read(4))[0]
                    vy3y = unpack("<f", f.read(4))[0]
                    vz3y = unpack("<f", f.read(4))[0]
                    type3y = unpack("B", f.read(1))[0]
                    value3y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3y = unpack("<f", f.read(4))[0]
                    vx4y = unpack("<f", f.read(4))[0]
                    vy4y = unpack("<f", f.read(4))[0]
                    vz4y = unpack("<f", f.read(4))[0]
                    type4y = unpack("B", f.read(1))[0]
                    value4y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4y = unpack("<f", f.read(4))[0]
                    vx5y = unpack("<f", f.read(4))[0]
                    vy5y = unpack("<f", f.read(4))[0]
                    vz5y = unpack("<f", f.read(4))[0]
                    type5y = unpack("B", f.read(1))[0]
                    value5y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5y = unpack("<f", f.read(4))[0]
                    vx6y = unpack("<f", f.read(4))[0]
                    vy6y = unpack("<f", f.read(4))[0]
                    vz6y = unpack("<f", f.read(4))[0]
                    type6y = unpack("B", f.read(1))[0]
                    value6y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6y = unpack("<f", f.read(4))[0]
                    vx7y = unpack("<f", f.read(4))[0]
                    vy7y = unpack("<f", f.read(4))[0]
                    vz7y = unpack("<f", f.read(4))[0]
                    type7y = unpack("B", f.read(1))[0]
                    value7y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7y = unpack("<f", f.read(4))[0]
                    vx8y = unpack("<f", f.read(4))[0]
                    vy8y = unpack("<f", f.read(4))[0]
                    vz8y = unpack("<f", f.read(4))[0]
                    type8y = unpack("B", f.read(1))[0]
                    value8y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8y = unpack("<f", f.read(4))[0]
                    vx9y = unpack("<f", f.read(4))[0]
                    vy9y = unpack("<f", f.read(4))[0]
                    vz9y = unpack("<f", f.read(4))[0]
                    type9y = unpack("B", f.read(1))[0]
                    value9y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9y = unpack("<f", f.read(4))[0]
                    vx10y = unpack("<f", f.read(4))[0]
                    vy10y = unpack("<f", f.read(4))[0]
                    vz10y = unpack("<f", f.read(4))[0]
                    type10y = unpack("B", f.read(1))[0]
                    value10y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10y = unpack("<f", f.read(4))[0]
                    vx11y = unpack("<f", f.read(4))[0]
                    vy11y = unpack("<f", f.read(4))[0]
                    vz11y = unpack("<f", f.read(4))[0]
                    type11y = unpack("B", f.read(1))[0]
                    value11y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11y = unpack("<f", f.read(4))[0]
                    vx12y = unpack("<f", f.read(4))[0]
                    vy12y = unpack("<f", f.read(4))[0]
                    vz12y = unpack("<f", f.read(4))[0]
                    type12y = unpack("B", f.read(1))[0]
                    value12y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12y = unpack("<f", f.read(4))[0]
                    vx13y = unpack("<f", f.read(4))[0]
                    vy13y = unpack("<f", f.read(4))[0]
                    vz13y = unpack("<f", f.read(4))[0]
                    type13y = unpack("B", f.read(1))[0]
                    value13y = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13y = unpack("<f", f.read(4))[0]

                    f.seek(-208,1)

                    vx1z = unpack("<f", f.read(4))[0]
                    vy1z = unpack("<f", f.read(4))[0]
                    vz1z = unpack("<f", f.read(4))[0]
                    type1z = unpack("B", f.read(1))[0]
                    value1z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw1z = unpack("<f", f.read(4))[0]
                    vx2z = unpack("<f", f.read(4))[0]
                    vy2z = unpack("<f", f.read(4))[0]
                    vz2z = unpack("<f", f.read(4))[0]
                    type2z = unpack("B", f.read(1))[0]
                    value2z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw2z = unpack("<f", f.read(4))[0]
                    vx3z = unpack("<f", f.read(4))[0]
                    vy3z = unpack("<f", f.read(4))[0]
                    vz3z = unpack("<f", f.read(4))[0]
                    type3z = unpack("B", f.read(1))[0]
                    value3z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw3z = unpack("<f", f.read(4))[0]
                    vx4z = unpack("<f", f.read(4))[0]
                    vy4z = unpack("<f", f.read(4))[0]
                    vz4z = unpack("<f", f.read(4))[0]
                    type4z = unpack("B", f.read(1))[0]
                    value4z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw4z = unpack("<f", f.read(4))[0]
                    vx5z = unpack("<f", f.read(4))[0]
                    vy5z = unpack("<f", f.read(4))[0]
                    vz5z = unpack("<f", f.read(4))[0]
                    type5z = unpack("B", f.read(1))[0]
                    value5z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw5z = unpack("<f", f.read(4))[0]
                    vx6z = unpack("<f", f.read(4))[0]
                    vy6z = unpack("<f", f.read(4))[0]
                    vz6z = unpack("<f", f.read(4))[0]
                    type6z = unpack("B", f.read(1))[0]
                    value6z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw6z = unpack("<f", f.read(4))[0]
                    vx7z = unpack("<f", f.read(4))[0]
                    vy7z = unpack("<f", f.read(4))[0]
                    vz7z = unpack("<f", f.read(4))[0]
                    type7z = unpack("B", f.read(1))[0]
                    value7z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw7z = unpack("<f", f.read(4))[0]
                    vx8z = unpack("<f", f.read(4))[0]
                    vy8z = unpack("<f", f.read(4))[0]
                    vz8z = unpack("<f", f.read(4))[0]
                    type8z = unpack("B", f.read(1))[0]
                    value8z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw8z = unpack("<f", f.read(4))[0]
                    vx9z = unpack("<f", f.read(4))[0]
                    vy9z = unpack("<f", f.read(4))[0]
                    vz9z = unpack("<f", f.read(4))[0]
                    type9z = unpack("B", f.read(1))[0]
                    value9z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw9z = unpack("<f", f.read(4))[0]
                    vx10z = unpack("<f", f.read(4))[0]
                    vy10z = unpack("<f", f.read(4))[0]
                    vz10z = unpack("<f", f.read(4))[0]
                    type10z = unpack("B", f.read(1))[0]
                    value10z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw10z = unpack("<f", f.read(4))[0]
                    vx11z = unpack("<f", f.read(4))[0]
                    vy11z = unpack("<f", f.read(4))[0]
                    vz11z = unpack("<f", f.read(4))[0]
                    type11z = unpack("B", f.read(1))[0]
                    value11z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw11z = unpack("<f", f.read(4))[0]
                    vx12z = unpack("<f", f.read(4))[0]
                    vy12z = unpack("<f", f.read(4))[0]
                    vz12z = unpack("<f", f.read(4))[0]
                    type12z = unpack("B", f.read(1))[0]
                    value12z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw12z = unpack("<f", f.read(4))[0]
                    vx13z = unpack("<f", f.read(4))[0]
                    vy13z = unpack("<f", f.read(4))[0]
                    vz13z = unpack("<f", f.read(4))[0]
                    type13z = unpack("B", f.read(1))[0]
                    value13z = unpack("B", f.read(1))[0]
                    f.seek(-2,1)
                    vw13z = unpack("<f", f.read(4))[0]

                    

                    fa1 = bm_1i.verts.new([-vx1,-vy1,-vz1]) # 0
                    fb1 = bm_1i.verts.new([-vx2,-vy2,-vz2]) # 1
                    fc1 = bm_1i.verts.new([-vx3,-vy3,-vz3]) # 2
                    fd1 = bm_1i.verts.new([-vx4,-vy4,-vz4]) # 3
                    fe1 = bm_1i.verts.new([-vx5,-vy5,-vz5]) # 4
                    ff1 = bm_1i.verts.new([-vx6,-vy6,-vz6]) # 5
                    fg1 = bm_1i.verts.new([-vx7,-vy7,-vz7]) # 6
                    fh1 = bm_1i.verts.new([-vx8,-vy8,-vz8]) # 7
                    fi1 = bm_1i.verts.new([-vx9,-vy9,-vz9]) # 8
                    fj1 = bm_1i.verts.new([-vx10,-vy10,-vz10]) # 9
                    fk1 = bm_1i.verts.new([-vx11,-vy11,-vz11]) # 10
                    fl1 = bm_1i.verts.new([-vx12,-vy12,-vz12]) # 11
                    fm1 = bm_1i.verts.new([-vx13,-vy13,-vz13]) # 12

                    fa1a = bm_1ii.verts.new([-vx1a,-vy1a,-vz1a]) # 0
                    fb1a = bm_1ii.verts.new([-vx2a,-vy2a,-vz2a]) # 1
                    fc1a = bm_1ii.verts.new([-vx3a,-vy3a,-vz3a]) # 2
                    fd1a = bm_1ii.verts.new([-vx4a,-vy4a,-vz4a]) # 3
                    fe1a = bm_1ii.verts.new([-vx5a,-vy5a,-vz5a]) # 4
                    ff1a = bm_1ii.verts.new([-vx6a,-vy6a,-vz6a]) # 5
                    fg1a = bm_1ii.verts.new([-vx7a,-vy7a,-vz7a]) # 6
                    fh1a = bm_1ii.verts.new([-vx8a,-vy8a,-vz8a]) # 7
                    fi1a = bm_1ii.verts.new([-vx9a,-vy9a,-vz9a]) # 8
                    fj1a = bm_1ii.verts.new([-vx10a,-vy10a,-vz10a]) # 9
                    fk1a = bm_1ii.verts.new([-vx11a,-vy11a,-vz11a]) # 10
                    fl1a = bm_1ii.verts.new([-vx12a,-vy12a,-vz12a]) # 11
                    fm1a = bm_1ii.verts.new([-vx13a,-vy13a,-vz13a]) # 12

                    fa1b = bm_1iii.verts.new([-vx1b,-vy1b,-vz1b]) # 0
                    fb1b = bm_1iii.verts.new([-vx2b,-vy2b,-vz2b]) # 1
                    fc1b = bm_1iii.verts.new([-vx3b,-vy3b,-vz3b]) # 2
                    fd1b = bm_1iii.verts.new([-vx4b,-vy4b,-vz4b]) # 3
                    fe1b = bm_1iii.verts.new([-vx5b,-vy5b,-vz5b]) # 4
                    ff1b = bm_1iii.verts.new([-vx6b,-vy6b,-vz6b]) # 5
                    fg1b = bm_1iii.verts.new([-vx7b,-vy7b,-vz7b]) # 6
                    fh1b = bm_1iii.verts.new([-vx8b,-vy8b,-vz8b]) # 7
                    fi1b = bm_1iii.verts.new([-vx9b,-vy9b,-vz9b]) # 8
                    fj1b = bm_1iii.verts.new([-vx10b,-vy10b,-vz10b]) # 9
                    fk1b = bm_1iii.verts.new([-vx11b,-vy11b,-vz11b]) # 10
                    fl1b = bm_1iii.verts.new([-vx12b,-vy12b,-vz12b]) # 11
                    fm1b = bm_1iii.verts.new([-vx13b,-vy13b,-vz13b]) # 12

                    fa1c = bm_1iiii.verts.new([-vx1c,-vy1c,-vz1c]) # 0
                    fb1c = bm_1iiii.verts.new([-vx2c,-vy2c,-vz2c]) # 1
                    fc1c = bm_1iiii.verts.new([-vx3c,-vy3c,-vz3c]) # 2
                    fd1c = bm_1iiii.verts.new([-vx4c,-vy4c,-vz4c]) # 3
                    fe1c = bm_1iiii.verts.new([-vx5c,-vy5c,-vz5c]) # 4
                    ff1c = bm_1iiii.verts.new([-vx6c,-vy6c,-vz6c]) # 5
                    fg1c = bm_1iiii.verts.new([-vx7c,-vy7c,-vz7c]) # 6
                    fh1c = bm_1iiii.verts.new([-vx8c,-vy8c,-vz8c]) # 7
                    fi1c = bm_1iiii.verts.new([-vx9c,-vy9c,-vz9c]) # 8
                    fj1c = bm_1iiii.verts.new([-vx10c,-vy10c,-vz10c]) # 9
                    fk1c = bm_1iiii.verts.new([-vx11c,-vy11c,-vz11c]) # 10
                    fl1c = bm_1iiii.verts.new([-vx12c,-vy12c,-vz12c]) # 11
                    fm1c = bm_1iiii.verts.new([-vx13c,-vy13c,-vz13c]) # 12

                    fa1d = bm_1iiiii.verts.new([-vx1d,-vy1d,-vz1d]) # 0
                    fb1d = bm_1iiiii.verts.new([-vx2d,-vy2d,-vz2d]) # 1
                    fc1d = bm_1iiiii.verts.new([-vx3d,-vy3d,-vz3d]) # 2
                    fd1d = bm_1iiiii.verts.new([-vx4d,-vy4d,-vz4d]) # 3
                    fe1d = bm_1iiiii.verts.new([-vx5d,-vy5d,-vz5d]) # 4
                    ff1d = bm_1iiiii.verts.new([-vx6d,-vy6d,-vz6d]) # 5
                    fg1d = bm_1iiiii.verts.new([-vx7d,-vy7d,-vz7d]) # 6
                    fh1d = bm_1iiiii.verts.new([-vx8d,-vy8d,-vz8d]) # 7
                    fi1d = bm_1iiiii.verts.new([-vx9d,-vy9d,-vz9d]) # 8
                    fj1d = bm_1iiiii.verts.new([-vx10d,-vy10d,-vz10d]) # 9
                    fk1d = bm_1iiiii.verts.new([-vx11d,-vy11d,-vz11d]) # 10
                    fl1d = bm_1iiiii.verts.new([-vx12d,-vy12d,-vz12d]) # 11
                    fm1d = bm_1iiiii.verts.new([-vx13d,-vy13d,-vz13d]) # 12

                    fa1e = bm_1iiiiii.verts.new([-vx1e,-vy1e,-vz1e]) # 0
                    fb1e = bm_1iiiiii.verts.new([-vx2e,-vy2e,-vz2e]) # 1
                    fc1e = bm_1iiiiii.verts.new([-vx3e,-vy3e,-vz3e]) # 2
                    fd1e = bm_1iiiiii.verts.new([-vx4e,-vy4e,-vz4e]) # 3
                    fe1e = bm_1iiiiii.verts.new([-vx5e,-vy5e,-vz5e]) # 4
                    ff1e = bm_1iiiiii.verts.new([-vx6e,-vy6e,-vz6e]) # 5
                    fg1e = bm_1iiiiii.verts.new([-vx7e,-vy7e,-vz7e]) # 6
                    fh1e = bm_1iiiiii.verts.new([-vx8e,-vy8e,-vz8e]) # 7
                    fi1e = bm_1iiiiii.verts.new([-vx9e,-vy9e,-vz9e]) # 8
                    fj1e = bm_1iiiiii.verts.new([-vx10e,-vy10e,-vz10e]) # 9
                    fk1e = bm_1iiiiii.verts.new([-vx11e,-vy11e,-vz11e]) # 10
                    fl1e = bm_1iiiiii.verts.new([-vx12e,-vy12e,-vz12e]) # 11
                    fm1e = bm_1iiiiii.verts.new([-vx13e,-vy13e,-vz13e]) # 12

                    fa1f = bm_1iiiiiii.verts.new([-vx1f,-vy1f,-vz1f]) # 0
                    fb1f = bm_1iiiiiii.verts.new([-vx2f,-vy2f,-vz2f]) # 1
                    fc1f = bm_1iiiiiii.verts.new([-vx3f,-vy3f,-vz3f]) # 2
                    fd1f = bm_1iiiiiii.verts.new([-vx4f,-vy4f,-vz4f]) # 3
                    fe1f = bm_1iiiiiii.verts.new([-vx5f,-vy5f,-vz5f]) # 4
                    ff1f = bm_1iiiiiii.verts.new([-vx6f,-vy6f,-vz6f]) # 5
                    fg1f = bm_1iiiiiii.verts.new([-vx7f,-vy7f,-vz7f]) # 6
                    fh1f = bm_1iiiiiii.verts.new([-vx8f,-vy8f,-vz8f]) # 7
                    fi1f = bm_1iiiiiii.verts.new([-vx9f,-vy9f,-vz9f]) # 8
                    fj1f = bm_1iiiiiii.verts.new([-vx10f,-vy10f,-vz10f]) # 9
                    fk1f = bm_1iiiiiii.verts.new([-vx11f,-vy11f,-vz11f]) # 10
                    fl1f = bm_1iiiiiii.verts.new([-vx12f,-vy12f,-vz12f]) # 11
                    fm1f = bm_1iiiiiii.verts.new([-vx13f,-vy13f,-vz13f]) # 12

                    fa1g = bm_1iiiiiiii.verts.new([-vx1g,-vy1g,-vz1g]) # 0
                    fb1g = bm_1iiiiiiii.verts.new([-vx2g,-vy2g,-vz2g]) # 1
                    fc1g = bm_1iiiiiiii.verts.new([-vx3g,-vy3g,-vz3g]) # 2
                    fd1g = bm_1iiiiiiii.verts.new([-vx4g,-vy4g,-vz4g]) # 3
                    fe1g = bm_1iiiiiiii.verts.new([-vx5g,-vy5g,-vz5g]) # 4
                    ff1g = bm_1iiiiiiii.verts.new([-vx6g,-vy6g,-vz6g]) # 5
                    fg1g = bm_1iiiiiiii.verts.new([-vx7g,-vy7g,-vz7g]) # 6
                    fh1g = bm_1iiiiiiii.verts.new([-vx8g,-vy8g,-vz8g]) # 7
                    fi1g = bm_1iiiiiiii.verts.new([-vx9g,-vy9g,-vz9g]) # 8
                    fj1g = bm_1iiiiiiii.verts.new([-vx10g,-vy10g,-vz10g]) # 9
                    fk1g = bm_1iiiiiiii.verts.new([-vx11g,-vy11g,-vz11g]) # 10
                    fl1g = bm_1iiiiiiii.verts.new([-vx12g,-vy12g,-vz12g]) # 11
                    fm1g = bm_1iiiiiiii.verts.new([-vx13g,-vy13g,-vz13g]) # 12

                    fa1h = bm_1iiiiiiiii.verts.new([-vx1h,-vy1h,-vz1h]) # 0
                    fb1h = bm_1iiiiiiiii.verts.new([-vx2h,-vy2h,-vz2h]) # 1
                    fc1h = bm_1iiiiiiiii.verts.new([-vx3h,-vy3h,-vz3h]) # 2
                    fd1h = bm_1iiiiiiiii.verts.new([-vx4h,-vy4h,-vz4h]) # 3
                    fe1h = bm_1iiiiiiiii.verts.new([-vx5h,-vy5h,-vz5h]) # 4
                    ff1h = bm_1iiiiiiiii.verts.new([-vx6h,-vy6h,-vz6h]) # 5
                    fg1h = bm_1iiiiiiiii.verts.new([-vx7h,-vy7h,-vz7h]) # 6
                    fh1h = bm_1iiiiiiiii.verts.new([-vx8h,-vy8h,-vz8h]) # 7
                    fi1h = bm_1iiiiiiiii.verts.new([-vx9h,-vy9h,-vz9h]) # 8
                    fj1h = bm_1iiiiiiiii.verts.new([-vx10h,-vy10h,-vz10h]) # 9
                    fk1h = bm_1iiiiiiiii.verts.new([-vx11h,-vy11h,-vz11h]) # 10
                    fl1h = bm_1iiiiiiiii.verts.new([-vx12h,-vy12h,-vz12h]) # 11
                    fm1h = bm_1iiiiiiiii.verts.new([-vx13h,-vy13h,-vz13h]) # 12

                    fa1i = bm_1iiiiiiiiii.verts.new([-vx1i,-vy1i,-vz1i]) # 0
                    fb1i = bm_1iiiiiiiiii.verts.new([-vx2i,-vy2i,-vz2i]) # 1
                    fc1i = bm_1iiiiiiiiii.verts.new([-vx3i,-vy3i,-vz3i]) # 2
                    fd1i = bm_1iiiiiiiiii.verts.new([-vx4i,-vy4i,-vz4i]) # 3
                    fe1i = bm_1iiiiiiiiii.verts.new([-vx5i,-vy5i,-vz5i]) # 4
                    ff1i = bm_1iiiiiiiiii.verts.new([-vx6i,-vy6i,-vz6i]) # 5
                    fg1i = bm_1iiiiiiiiii.verts.new([-vx7i,-vy7i,-vz7i]) # 6
                    fh1i = bm_1iiiiiiiiii.verts.new([-vx8i,-vy8i,-vz8i]) # 7
                    fi1i = bm_1iiiiiiiiii.verts.new([-vx9i,-vy9i,-vz9i]) # 8
                    fj1i = bm_1iiiiiiiiii.verts.new([-vx10i,-vy10i,-vz10i]) # 9
                    fk1i = bm_1iiiiiiiiii.verts.new([-vx11i,-vy11i,-vz11i]) # 10
                    fl1i = bm_1iiiiiiiiii.verts.new([-vx12i,-vy12i,-vz12i]) # 11
                    fm1i = bm_1iiiiiiiiii.verts.new([-vx13i,-vy13i,-vz13i]) # 12

                    fa1j = bm_1iiiiiiiiiii.verts.new([-vx1j,-vy1j,-vz1j]) # 0
                    fb1j = bm_1iiiiiiiiiii.verts.new([-vx2j,-vy2j,-vz2j]) # 1
                    fc1j = bm_1iiiiiiiiiii.verts.new([-vx3j,-vy3j,-vz3j]) # 2
                    fd1j = bm_1iiiiiiiiiii.verts.new([-vx4j,-vy4j,-vz4j]) # 3
                    fe1j = bm_1iiiiiiiiiii.verts.new([-vx5j,-vy5j,-vz5j]) # 4
                    ff1j = bm_1iiiiiiiiiii.verts.new([-vx6j,-vy6j,-vz6j]) # 5
                    fg1j = bm_1iiiiiiiiiii.verts.new([-vx7j,-vy7j,-vz7j]) # 6
                    fh1j = bm_1iiiiiiiiiii.verts.new([-vx8j,-vy8j,-vz8j]) # 7
                    fi1j = bm_1iiiiiiiiiii.verts.new([-vx9j,-vy9j,-vz9j]) # 8
                    fj1j = bm_1iiiiiiiiiii.verts.new([-vx10j,-vy10j,-vz10j]) # 9
                    fk1j = bm_1iiiiiiiiiii.verts.new([-vx11j,-vy11j,-vz11j]) # 10
                    fl1j = bm_1iiiiiiiiiii.verts.new([-vx12j,-vy12j,-vz12j]) # 11
                    fm1j = bm_1iiiiiiiiiii.verts.new([-vx13j,-vy13j,-vz13j]) # 12

                    fa1k = bm_1iiiiiiiiiiii.verts.new([-vx1k,-vy1k,-vz1k]) # 0
                    fb1k = bm_1iiiiiiiiiiii.verts.new([-vx2k,-vy2k,-vz2k]) # 1
                    fc1k = bm_1iiiiiiiiiiii.verts.new([-vx3k,-vy3k,-vz3k]) # 2
                    fd1k = bm_1iiiiiiiiiiii.verts.new([-vx4k,-vy4k,-vz4k]) # 3
                    fe1k = bm_1iiiiiiiiiiii.verts.new([-vx5k,-vy5k,-vz5k]) # 4
                    ff1k = bm_1iiiiiiiiiiii.verts.new([-vx6k,-vy6k,-vz6k]) # 5
                    fg1k = bm_1iiiiiiiiiiii.verts.new([-vx7k,-vy7k,-vz7k]) # 6
                    fh1k = bm_1iiiiiiiiiiii.verts.new([-vx8k,-vy8k,-vz8k]) # 7
                    fi1k = bm_1iiiiiiiiiiii.verts.new([-vx9k,-vy9k,-vz9k]) # 8
                    fj1k = bm_1iiiiiiiiiiii.verts.new([-vx10k,-vy10k,-vz10k]) # 9
                    fk1k = bm_1iiiiiiiiiiii.verts.new([-vx11k,-vy11k,-vz11k]) # 10
                    fl1k = bm_1iiiiiiiiiiii.verts.new([-vx12k,-vy12k,-vz12k]) # 11
                    fm1k = bm_1iiiiiiiiiiii.verts.new([-vx13k,-vy13k,-vz13k]) # 12

                    fa1l = bm_1iiiiiiiiiiiii.verts.new([-vx1l,-vy1l,-vz1l]) # 0
                    fb1l = bm_1iiiiiiiiiiiii.verts.new([-vx2l,-vy2l,-vz2l]) # 1
                    fc1l = bm_1iiiiiiiiiiiii.verts.new([-vx3l,-vy3l,-vz3l]) # 2
                    fd1l = bm_1iiiiiiiiiiiii.verts.new([-vx4l,-vy4l,-vz4l]) # 3
                    fe1l = bm_1iiiiiiiiiiiii.verts.new([-vx5l,-vy5l,-vz5l]) # 4
                    ff1l = bm_1iiiiiiiiiiiii.verts.new([-vx6l,-vy6l,-vz6l]) # 5
                    fg1l = bm_1iiiiiiiiiiiii.verts.new([-vx7l,-vy7l,-vz7l]) # 6
                    fh1l = bm_1iiiiiiiiiiiii.verts.new([-vx8l,-vy8l,-vz8l]) # 7
                    fi1l = bm_1iiiiiiiiiiiii.verts.new([-vx9l,-vy9l,-vz9l]) # 8
                    fj1l = bm_1iiiiiiiiiiiii.verts.new([-vx10l,-vy10l,-vz10l]) # 9
                    fk1l = bm_1iiiiiiiiiiiii.verts.new([-vx11l,-vy11l,-vz11l]) # 10
                    fl1l = bm_1iiiiiiiiiiiii.verts.new([-vx12l,-vy12l,-vz12l]) # 11
                    fm1l = bm_1iiiiiiiiiiiii.verts.new([-vx13l,-vy13l,-vz13l]) # 12

                    fa1m = bm_1iiiiiiiiiiiiii.verts.new([-vx1m,-vy1m,-vz1m]) # 0
                    fb1m = bm_1iiiiiiiiiiiiii.verts.new([-vx2m,-vy2m,-vz2m]) # 1
                    fc1m = bm_1iiiiiiiiiiiiii.verts.new([-vx3m,-vy3m,-vz3m]) # 2
                    fd1m = bm_1iiiiiiiiiiiiii.verts.new([-vx4m,-vy4m,-vz4m]) # 3
                    fe1m = bm_1iiiiiiiiiiiiii.verts.new([-vx5m,-vy5m,-vz5m]) # 4
                    ff1m = bm_1iiiiiiiiiiiiii.verts.new([-vx6m,-vy6m,-vz6m]) # 5
                    fg1m = bm_1iiiiiiiiiiiiii.verts.new([-vx7m,-vy7m,-vz7m]) # 6
                    fh1m = bm_1iiiiiiiiiiiiii.verts.new([-vx8m,-vy8m,-vz8m]) # 7
                    fi1m = bm_1iiiiiiiiiiiiii.verts.new([-vx9m,-vy9m,-vz9m]) # 8
                    fj1m = bm_1iiiiiiiiiiiiii.verts.new([-vx10m,-vy10m,-vz10m]) # 9
                    fk1m = bm_1iiiiiiiiiiiiii.verts.new([-vx11m,-vy11m,-vz11m]) # 10
                    fl1m = bm_1iiiiiiiiiiiiii.verts.new([-vx12m,-vy12m,-vz12m]) # 11
                    fm1m = bm_1iiiiiiiiiiiiii.verts.new([-vx13m,-vy13m,-vz13m]) # 12

                    fa1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx1n,-vy1n,-vz1n]) # 0
                    fb1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx2n,-vy2n,-vz2n]) # 1
                    fc1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx3n,-vy3n,-vz3n]) # 2
                    fd1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx4n,-vy4n,-vz4n]) # 3
                    fe1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx5n,-vy5n,-vz5n]) # 4
                    ff1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx6n,-vy6n,-vz6n]) # 5
                    fg1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx7n,-vy7n,-vz7n]) # 6
                    fh1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx8n,-vy8n,-vz8n]) # 7
                    fi1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx9n,-vy9n,-vz9n]) # 8
                    fj1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx10n,-vy10n,-vz10n]) # 9
                    fk1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx11n,-vy11n,-vz11n]) # 10
                    fl1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx12n,-vy12n,-vz12n]) # 11
                    fm1n = bm_1iiiiiiiiiiiiiii.verts.new([-vx13n,-vy13n,-vz13n]) # 12

                    fa1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx1o,-vy1o,-vz1o]) # 0
                    fb1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx2o,-vy2o,-vz2o]) # 1
                    fc1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx3o,-vy3o,-vz3o]) # 2
                    fd1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx4o,-vy4o,-vz4o]) # 3
                    fe1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx5o,-vy5o,-vz5o]) # 4
                    ff1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx6o,-vy6o,-vz6o]) # 5
                    fg1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx7o,-vy7o,-vz7o]) # 6
                    fh1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx8o,-vy8o,-vz8o]) # 7
                    fi1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx9o,-vy9o,-vz9o]) # 8
                    fj1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx10o,-vy10o,-vz10o]) # 9
                    fk1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx11o,-vy11o,-vz11o]) # 10
                    fl1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx12o,-vy12o,-vz12o]) # 11
                    fm1o = bm_1iiiiiiiiiiiiiiii.verts.new([-vx13o,-vy13o,-vz13o]) # 12

                    fa1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx1p,-vy1p,-vz1p]) # 0
                    fb1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx2p,-vy2p,-vz2p]) # 1
                    fc1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx3p,-vy3p,-vz3p]) # 2
                    fd1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx4p,-vy4p,-vz4p]) # 3
                    fe1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx5p,-vy5p,-vz5p]) # 4
                    ff1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx6p,-vy6p,-vz6p]) # 5
                    fg1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx7p,-vy7p,-vz7p]) # 6
                    fh1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx8p,-vy8p,-vz8p]) # 7
                    fi1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx9p,-vy9p,-vz9p]) # 8
                    fj1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx10p,-vy10p,-vz10p]) # 9
                    fk1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx11p,-vy11p,-vz11p]) # 10
                    fl1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx12p,-vy12p,-vz12p]) # 11
                    fm1p = bm_1iiiiiiiiiiiiiiiii.verts.new([-vx13p,-vy13p,-vz13p]) # 12

                    fa1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx1q,-vy1q,-vz1q]) # 0
                    fb1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx2q,-vy2q,-vz2q]) # 1
                    fc1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx3q,-vy3q,-vz3q]) # 2
                    fd1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx4q,-vy4q,-vz4q]) # 3
                    fe1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx5q,-vy5q,-vz5q]) # 4
                    ff1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx6q,-vy6q,-vz6q]) # 5
                    fg1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx7q,-vy7q,-vz7q]) # 6
                    fh1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx8q,-vy8q,-vz8q]) # 7
                    fi1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx9q,-vy9q,-vz9q]) # 8
                    fj1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx10q,-vy10q,-vz10q]) # 9
                    fk1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx11q,-vy11q,-vz11q]) # 10
                    fl1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx12q,-vy12q,-vz12q]) # 11
                    fm1q = bm_1iiiiiiiiiiiiiiiiii.verts.new([-vx13q,-vy13q,-vz13q]) # 12

                    fa1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx1r,-vy1r,-vz1r]) # 0
                    fb1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx2r,-vy2r,-vz2r]) # 1
                    fc1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx3r,-vy3r,-vz3r]) # 2
                    fd1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx4r,-vy4r,-vz4r]) # 3
                    fe1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx5r,-vy5r,-vz5r]) # 4
                    ff1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx6r,-vy6r,-vz6r]) # 5
                    fg1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx7r,-vy7r,-vz7r]) # 6
                    fh1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx8r,-vy8r,-vz8r]) # 7
                    fi1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx9r,-vy9r,-vz9r]) # 8
                    fj1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx10r,-vy10r,-vz10r]) # 9
                    fk1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx11r,-vy11r,-vz11r]) # 10
                    fl1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx12r,-vy12r,-vz12r]) # 11
                    fm1r = bm_1iiiiiiiiiiiiiiiiiii.verts.new([-vx13r,-vy13r,-vz13r]) # 12

                    fa1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx1s,-vy1s,-vz1s]) # 0
                    fb1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx2s,-vy2s,-vz2s]) # 1
                    fc1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx3s,-vy3s,-vz3s]) # 2
                    fd1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx4s,-vy4s,-vz4s]) # 3
                    fe1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx5s,-vy5s,-vz5s]) # 4
                    ff1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx6s,-vy6s,-vz6s]) # 5
                    fg1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx7s,-vy7s,-vz7s]) # 6
                    fh1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx8s,-vy8s,-vz8s]) # 7
                    fi1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx9s,-vy9s,-vz9s]) # 8
                    fj1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx10s,-vy10s,-vz10s]) # 9
                    fk1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx11s,-vy11s,-vz11s]) # 10
                    fl1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx12s,-vy12s,-vz12s]) # 11
                    fm1s = bm_1iiiiiiiiiiiiiiiiiiii.verts.new([-vx13s,-vy13s,-vz13s]) # 12

                    fa1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx1t,-vy1t,-vz1t]) # 0
                    fb1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx2t,-vy2t,-vz2t]) # 1
                    fc1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx3t,-vy3t,-vz3t]) # 2
                    fd1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx4t,-vy4t,-vz4t]) # 3
                    fe1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx5t,-vy5t,-vz5t]) # 4
                    ff1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx6t,-vy6t,-vz6t]) # 5
                    fg1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx7t,-vy7t,-vz7t]) # 6
                    fh1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx8t,-vy8t,-vz8t]) # 7
                    fi1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx9t,-vy9t,-vz9t]) # 8
                    fj1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx10t,-vy10t,-vz10t]) # 9
                    fk1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx11t,-vy11t,-vz11t]) # 10
                    fl1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx12t,-vy12t,-vz12t]) # 11
                    fm1t = bm_1iiiiiiiiiiiiiiiiiiiii.verts.new([-vx13t,-vy13t,-vz13t]) # 12

                    fa1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1u,-vy1u,-vz1u]) # 0
                    fb1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2u,-vy2u,-vz2u]) # 1
                    fc1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3u,-vy3u,-vz3u]) # 2
                    fd1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4u,-vy4u,-vz4u]) # 3
                    fe1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5u,-vy5u,-vz5u]) # 4
                    ff1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6u,-vy6u,-vz6u]) # 5
                    fg1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7u,-vy7u,-vz7u]) # 6
                    fh1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8u,-vy8u,-vz8u]) # 7
                    fi1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9u,-vy9u,-vz9u]) # 8
                    fj1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10u,-vy10u,-vz10u]) # 9
                    fk1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11u,-vy11u,-vz11u]) # 10
                    fl1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12u,-vy12u,-vz12u]) # 11
                    fm1u = bm_1iiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13u,-vy13u,-vz13u]) # 12

                    fa1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1v,-vy1v,-vz1v]) # 0
                    fb1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2v,-vy2v,-vz2v]) # 1
                    fc1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3v,-vy3v,-vz3v]) # 2
                    fd1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4v,-vy4v,-vz4v]) # 3
                    fe1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5v,-vy5v,-vz5v]) # 4
                    ff1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6v,-vy6v,-vz6v]) # 5
                    fg1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7v,-vy7v,-vz7v]) # 6
                    fh1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8v,-vy8v,-vz8v]) # 7
                    fi1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9v,-vy9v,-vz9v]) # 8
                    fj1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10v,-vy10v,-vz10v]) # 9
                    fk1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11v,-vy11v,-vz11v]) # 10
                    fl1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12v,-vy12v,-vz12v]) # 11
                    fm1v = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13v,-vy13v,-vz13v]) # 12

                    fa1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1w,-vy1w,-vz1w]) # 0
                    fb1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2w,-vy2w,-vz2w]) # 1
                    fc1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3w,-vy3w,-vz3w]) # 2
                    fd1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4w,-vy4w,-vz4w]) # 3
                    fe1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5w,-vy5w,-vz5w]) # 4
                    ff1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6w,-vy6w,-vz6w]) # 5
                    fg1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7w,-vy7w,-vz7w]) # 6
                    fh1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8w,-vy8w,-vz8w]) # 7
                    fi1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9w,-vy9w,-vz9w]) # 8
                    fj1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10w,-vy10w,-vz10w]) # 9
                    fk1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11w,-vy11w,-vz11w]) # 10
                    fl1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12w,-vy12w,-vz12w]) # 11
                    fm1w = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13w,-vy13w,-vz13w]) # 12

                    fa1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1x,-vy1x,-vz1x]) # 0
                    fb1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2x,-vy2x,-vz2x]) # 1
                    fc1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3x,-vy3x,-vz3x]) # 2
                    fd1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4x,-vy4x,-vz4x]) # 3
                    fe1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5x,-vy5x,-vz5x]) # 4
                    ff1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6x,-vy6x,-vz6x]) # 5
                    fg1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7x,-vy7x,-vz7x]) # 6
                    fh1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8x,-vy8x,-vz8x]) # 7
                    fi1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9x,-vy9x,-vz9x]) # 8
                    fj1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10x,-vy10x,-vz10x]) # 9
                    fk1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11x,-vy11x,-vz11x]) # 10
                    fl1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12x,-vy12x,-vz12x]) # 11
                    fm1x = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13x,-vy13x,-vz13x]) # 12

                    fa1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1y,-vy1y,-vz1y]) # 0
                    fb1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2y,-vy2y,-vz2y]) # 1
                    fc1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3y,-vy3y,-vz3y]) # 2
                    fd1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4y,-vy4y,-vz4y]) # 3
                    fe1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5y,-vy5y,-vz5y]) # 4
                    ff1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6y,-vy6y,-vz6y]) # 5
                    fg1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7y,-vy7y,-vz7y]) # 6
                    fh1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8y,-vy8y,-vz8y]) # 7
                    fi1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9y,-vy9y,-vz9y]) # 8
                    fj1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10y,-vy10y,-vz10y]) # 9
                    fk1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11y,-vy11y,-vz11y]) # 10
                    fl1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12y,-vy12y,-vz12y]) # 11
                    fm1y = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13y,-vy13y,-vz13y]) # 12

                    fa1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx1z,-vy1z,-vz1z]) # 0
                    fb1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx2z,-vy2z,-vz2z]) # 1
                    fc1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx3z,-vy3z,-vz3z]) # 2
                    fd1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx4z,-vy4z,-vz4z]) # 3
                    fe1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx5z,-vy5z,-vz5z]) # 4
                    ff1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx6z,-vy6z,-vz6z]) # 5
                    fg1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx7z,-vy7z,-vz7z]) # 6
                    fh1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx8z,-vy8z,-vz8z]) # 7
                    fi1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx9z,-vy9z,-vz9z]) # 8
                    fj1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx10z,-vy10z,-vz10z]) # 9
                    fk1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx11z,-vy11z,-vz11z]) # 10
                    fl1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx12z,-vy12z,-vz12z]) # 11
                    fm1z = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts.new([-vx13z,-vy13z,-vz13z]) # 12

                    if type1z == 1:
                        if type2z == 1:
                            if type3z == 0:
                                if type4z == 1:
                                    if type5z == 1:
                                        if type6z == 0:
                                            if type7z == 0:
                                                if type8z == 1:
                                                    if type9z == 1:
                                                        if type10z == 0:
                                                            if type11z == 1:
                                                                if type12z == 1:
                                                                    if type13z == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fa1z,fb1z,fc1z])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fd1z,fe1z,ff1z])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fe1z,ff1z,fg1z])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fh1z,fi1z,fj1z])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fk1z,fl1z,fm1z])

                    if type1y == 1:
                        if type2y == 1:
                            if type3y == 0:
                                if type4y == 0:
                                    if type5y == 1:
                                        if type6y == 1:
                                            if type7y == 0:
                                                if type8y == 1:
                                                    if type9y == 1:
                                                        if type10y == 0:
                                                            if type11y == 1:
                                                                if type12y == 1:
                                                                    if type13y == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fa1y,fb1y,fc1y])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fb1y,fc1y,fd1y])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fe1y,ff1y,fg1y])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fh1y,fi1y,fj1y])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fk1y,fl1y,fm1y])

                    if type1x == 1:
                        if type2x == 1:
                            if type3x == 0:
                                if type4x == 1:
                                    if type5x == 1:
                                        if type6x == 0:
                                            if type7x == 1:
                                                if type8x == 1:
                                                    if type9x == 0:
                                                        if type10x == 0:
                                                            if type11x == 1:
                                                                if type12x == 1:
                                                                    if type13x == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fa1x,fb1x,fc1x])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fd1x,fe1x,ff1x])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fg1x,fh1x,fi1x])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fh1x,fi1x,fj1x])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiiii.faces.new([fk1x,fl1x,fm1x])

                    if type1w == 1:
                        if type2w == 1:
                            if type3w == 0:
                                if type4w == 1:
                                    if type5w == 1:
                                        if type6w == 0:
                                            if type7w == 1:
                                                if type8w == 1:
                                                    if type9w == 0:
                                                        if type10w == 1:
                                                            if type11w == 1:
                                                                if type12w == 0:
                                                                    if type13w == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiii.faces.new([fa1w,fb1w,fc1w])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiii.faces.new([fd1w,fe1w,ff1w])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiii.faces.new([fg1w,fh1w,fi1w])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiii.faces.new([fj1w,fk1w,fl1w])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiiii.faces.new([fk1w,fl1w,fm1w])

                    if type1v == 1:
                        if type2v == 1:
                            if type3v == 0:
                                if type4v == 0:
                                    if type5v == 0:
                                        if type6v == 0:
                                            if type7v == 1:
                                                if type8v == 1:
                                                    if type9v == 0:
                                                        if type10v == 0:
                                                            if type11v == 1:
                                                                if type12v == 1:
                                                                    if type13v == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fa1v,fb1v,fc1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fb1v,fc1v,fd1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fc1v,fd1v,fe1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fd1v,fe1v,ff1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fg1v,fh1v,fi1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fh1v,fi1v,fj1v])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiiii.faces.new([fk1v,fl1v,fm1v])

                    if type1u == 1:
                        if type2u == 1:
                            if type3u == 0:
                                if type4u == 0:
                                    if type5u == 0:
                                        if type6u == 0:
                                            if type7u == 1:
                                                if type8u == 1:
                                                    if type9u == 0:
                                                        if type10u == 1:
                                                            if type11u == 1:
                                                                if type12u == 0:
                                                                    if type13u == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fa1u,fb1u,fc1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fb1u,fc1u,fd1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fc1u,fd1u,fe1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fd1u,fe1u,ff1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fg1u,fh1u,fi1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fj1u,fk1u,fl1u])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiiii.faces.new([fk1u,fl1u,fm1u])

                    if type1t == 1:
                        if type2t == 1:
                            if type3t == 0:
                                if type4t == 0:
                                    if type5t == 0:
                                        if type6t == 1:
                                            if type7t == 1:
                                                if type8t == 0:
                                                    if type9t == 0:
                                                        if type10t == 0:
                                                            if type11t == 1:
                                                                if type12t == 1:
                                                                    if type13t == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fa1t,fb1t,fc1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fb1t,fc1t,fd1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fc1t,fd1t,fe1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([ff1t,fg1t,fh1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fg1t,fh1t,fi1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fh1t,fi1t,fj1t])
                                                                        bm_1iiiiiiiiiiiiiiiiiiiii.faces.new([fk1t,fl1t,fm1t])

                    if type1s == 1:
                        if type2s == 1:
                            if type3s == 0:
                                if type4s == 0:
                                    if type5s == 0:
                                        if type6s == 1:
                                            if type7s == 1:
                                                if type8s == 0:
                                                    if type9s == 0:
                                                        if type10s == 1:
                                                            if type11s == 1:
                                                                if type12s == 0:
                                                                    if type13s == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fa1s,fb1s,fc1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fb1s,fc1s,fd1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fc1s,fd1s,fe1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([ff1s,fg1s,fh1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fg1s,fh1s,fi1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fj1s,fk1s,fl1s])
                                                                        bm_1iiiiiiiiiiiiiiiiiiii.faces.new([fk1s,fl1s,fm1s])

                    if type1r == 1:
                        if type2r == 1:
                            if type3r == 0:
                                if type4r == 0:
                                    if type5r == 0:
                                        if type6r == 1:
                                            if type7r == 1:
                                                if type8r == 0:
                                                    if type9r == 1:
                                                        if type10r == 1:
                                                            if type11r == 0:
                                                                if type12r == 0:
                                                                    if type13r == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fa1r,fb1r,fc1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fb1r,fc1r,fd1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fc1r,fd1r,fe1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([ff1r,fg1r,fh1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fi1r,fj1r,fk1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fj1r,fk1r,fl1r])
                                                                        bm_1iiiiiiiiiiiiiiiiiii.faces.new([fk1r,fl1r,fm1r])

                    if type1q == 1:
                        if type2q == 1:
                            if type3q == 0:
                                if type4q == 0:
                                    if type5q == 1:
                                        if type6q == 1:
                                            if type7q == 0:
                                                if type8q == 0:
                                                    if type9q == 0:
                                                        if type10q == 0:
                                                            if type11q == 1:
                                                                if type12q == 1:
                                                                    if type13q == 0:
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fa1q,fb1q,fc1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fb1q,fc1q,fd1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fe1q,ff1q,fg1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([ff1q,fg1q,fh1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fg1q,fh1q,fi1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fh1q,fi1q,fj1q])
                                                                        bm_1iiiiiiiiiiiiiiiiii.faces.new([fk1q,fl1q,fm1q])

                    if type1p == 1:
                        if type2p == 1:
                            if type3p == 0:
                                if type4p == 0:
                                    if type5p == 1:
                                        if type6p == 1:
                                            if type7p == 0:
                                                if type8p == 0:
                                                    if type9p == 0:
                                                        if type10p == 1:
                                                            if type11p == 1:
                                                                if type12p == 0:
                                                                    if type13p == 0:
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fa1p,fb1p,fc1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fb1p,fc1p,fd1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fe1p,ff1p,fg1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([ff1p,fg1p,fh1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fg1p,fh1p,fi1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fj1p,fk1p,fl1p])
                                                                        bm_1iiiiiiiiiiiiiiiii.faces.new([fk1p,fl1p,fm1p])

                    if type1o == 1:
                        if type2o == 1:
                            if type3o == 0:
                                if type4o == 0:
                                    if type5o == 1:
                                        if type6o == 1:
                                            if type7o == 0:
                                                if type8o == 0:
                                                    if type9o == 1:
                                                        if type10o == 1:
                                                            if type11o == 0:
                                                                if type12o == 0:
                                                                    if type13o == 0:
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fa1o,fb1o,fc1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fb1o,fc1o,fd1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fe1o,ff1o,fg1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([ff1o,fg1o,fh1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fi1o,fj1o,fk1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fj1o,fk1o,fl1o])
                                                                        bm_1iiiiiiiiiiiiiiii.faces.new([fk1o,fl1o,fm1o])

                    if type1n == 1:
                        if type2n == 1:
                            if type3n == 0:
                                if type4n == 0:
                                    if type5n == 1:
                                        if type6n == 1:
                                            if type7n == 0:
                                                if type8n == 1:
                                                    if type9n == 1:
                                                        if type10n == 0:
                                                            if type11n == 0:
                                                                if type12n == 0:
                                                                    if type13n == 0:
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fa1n,fb1n,fc1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fb1n,fc1n,fd1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fe1n,ff1n,fg1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([ff1n,fg1n,fh1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fg1n,fh1n,fi1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fh1n,fi1n,fj1n])
                                                                        bm_1iiiiiiiiiiiiiii.faces.new([fk1n,fl1n,fm1n])

                    if type1m == 1:
                        if type2m == 1:
                            if type3m == 0:
                                if type4m == 1:
                                    if type5m == 1:
                                        if type6m == 0:
                                            if type7m == 0:
                                                if type8m == 0:
                                                    if type9m == 0:
                                                        if type10m == 0:
                                                            if type11m == 1:
                                                                if type12m == 1:
                                                                    if type13m == 0:
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fa1m,fb1m,fc1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fd1m,fe1m,ff1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fe1m,ff1m,fg1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([ff1m,fg1m,fh1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fg1m,fh1m,fi1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fh1m,fi1m,fj1m])
                                                                        bm_1iiiiiiiiiiiiii.faces.new([fk1m,fl1m,fm1m])

                    if type1l == 1:
                        if type2l == 1:
                            if type3l == 0:
                                if type4l == 1:
                                    if type5l == 1:
                                        if type6l == 0:
                                            if type7l == 0:
                                                if type8l == 0:
                                                    if type9l == 0:
                                                        if type10l == 1:
                                                            if type11l == 1:
                                                                if type12l == 0:
                                                                    if type13l == 0:
                                                                        bm_1iiiiiiiiiiiii.faces.new([fa1l,fb1l,fc1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([fd1l,fe1l,ff1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([fe1l,ff1l,fg1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([ff1l,fg1l,fh1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([fg1l,fh1l,fi1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([fj1l,fk1l,fl1l])
                                                                        bm_1iiiiiiiiiiiii.faces.new([fk1l,fl1l,fm1l])

                    if type1k == 1:
                        if type2k == 1:
                            if type3k == 0:
                                if type4k == 1:
                                    if type5k == 1:
                                        if type6k == 0:
                                            if type7k == 0:
                                                if type8k == 0:
                                                    if type9k == 1:
                                                        if type10k == 1:
                                                            if type11k == 0:
                                                                if type12k == 0:
                                                                    if type13k == 0:
                                                                        bm_1iiiiiiiiiiii.faces.new([fa1k,fb1k,fc1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([fd1k,fe1k,ff1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([fe1k,ff1k,fg1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([ff1k,fg1k,fh1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([fi1k,fj1k,fk1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([fj1k,fk1k,fl1k])
                                                                        bm_1iiiiiiiiiiii.faces.new([fk1k,fl1k,fm1k])


                    if type1j == 1:
                        if type2j == 1:
                            if type3j == 0:
                                if type4j == 1:
                                    if type5j == 1:
                                        if type6j == 0:
                                            if type7j == 0:
                                                if type8j == 1:
                                                    if type9j == 1:
                                                        if type10j == 0:
                                                            if type11j == 0:
                                                                if type12j == 0:
                                                                    if type13j == 0:
                                                                        bm_1iiiiiiiiiii.faces.new([fa1j,fb1j,fc1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fd1j,fe1j,ff1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fe1j,ff1j,fg1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fh1j,fi1j,fj1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fi1j,fj1j,fk1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fj1j,fk1j,fl1j])
                                                                        bm_1iiiiiiiiiii.faces.new([fk1j,fl1j,fm1j])

                    if type1i == 1:
                        if type2i == 1:
                            if type3i == 0:
                                if type4i == 1:
                                    if type5i == 1:
                                        if type6i == 0:
                                            if type7i == 1:
                                                if type8i == 1:
                                                    if type9i == 0:
                                                        if type10i == 0:
                                                            if type11i == 0:
                                                                if type12i == 0:
                                                                    if type13i == 0:
                                                                        bm_1iiiiiiiiii.faces.new([fa1i,fb1i,fc1i])
                                                                        bm_1iiiiiiiiii.faces.new([fd1i,fe1i,ff1i])
                                                                        bm_1iiiiiiiiii.faces.new([fg1i,fh1i,fi1i])
                                                                        bm_1iiiiiiiiii.faces.new([fh1i,fi1i,fj1i])
                                                                        bm_1iiiiiiiiii.faces.new([fi1i,fj1i,fk1i])
                                                                        bm_1iiiiiiiiii.faces.new([fj1i,fk1i,fl1i])
                                                                        bm_1iiiiiiiiii.faces.new([fk1i,fl1i,fm1i])

                    if type1h == 1:
                        if type2h == 1:
                            if type3h == 0:
                                if type4h == 0:
                                    if type5h == 0:
                                        if type6h == 0:
                                            if type7h == 0:
                                                if type8h == 0:
                                                    if type9h == 0:
                                                        if type10h == 0:
                                                            if type11h == 1:
                                                                if type12h == 1:
                                                                    if type13h == 0:
                                                                        bm_1iiiiiiiii.faces.new([fa1h,fb1h,fc1h])
                                                                        bm_1iiiiiiiii.faces.new([fb1h,fc1h,fd1h])
                                                                        bm_1iiiiiiiii.faces.new([fc1h,fd1h,fe1h])
                                                                        bm_1iiiiiiiii.faces.new([fd1h,fe1h,ff1h])
                                                                        bm_1iiiiiiiii.faces.new([fe1h,ff1h,fg1h])
                                                                        bm_1iiiiiiiii.faces.new([ff1h,fg1h,fh1h])
                                                                        bm_1iiiiiiiii.faces.new([fg1h,fh1h,fi1h])
                                                                        bm_1iiiiiiiii.faces.new([fh1h,fi1h,fj1h])
                                                                        bm_1iiiiiiiii.faces.new([fk1h,fl1h,fm1h])

                    if type1g == 1:
                        if type2g == 1:
                            if type3g == 0:
                                if type4g == 0:
                                    if type5g == 0:
                                        if type6g == 0:
                                            if type7g == 0:
                                                if type8g == 0:
                                                    if type9g == 0:
                                                        if type10g == 1:
                                                            if type11g == 1:
                                                                if type12g == 0:
                                                                    if type13g == 0:
                                                                        bm_1iiiiiiii.faces.new([fa1g,fb1g,fc1g])
                                                                        bm_1iiiiiiii.faces.new([fb1g,fc1g,fd1g])
                                                                        bm_1iiiiiiii.faces.new([fc1g,fd1g,fe1g])
                                                                        bm_1iiiiiiii.faces.new([fd1g,fe1g,ff1g])
                                                                        bm_1iiiiiiii.faces.new([fe1g,ff1g,fg1g])
                                                                        bm_1iiiiiiii.faces.new([ff1g,fg1g,fh1g])
                                                                        bm_1iiiiiiii.faces.new([fg1g,fh1g,fi1g])
                                                                        bm_1iiiiiiii.faces.new([fj1g,fk1g,fl1g])
                                                                        bm_1iiiiiiii.faces.new([fk1g,fl1g,fm1g])

                    

                    if type1f == 1:
                        if type2f == 1:
                            if type3f == 0:
                                if type4f == 0:
                                    if type5f == 0:
                                        if type6f == 0:
                                            if type7f == 0:
                                                if type8f == 0:
                                                    if type9f == 1:
                                                        if type10f == 1:
                                                            if type11f == 0:
                                                                if type12f == 0:
                                                                    if type13f == 0:
                                                                        bm_1iiiiiii.faces.new([fa1f,fb1f,fc1f])
                                                                        bm_1iiiiiii.faces.new([fb1f,fc1f,fd1f])
                                                                        bm_1iiiiiii.faces.new([fc1f,fd1f,fe1f])
                                                                        bm_1iiiiiii.faces.new([fd1f,fe1f,ff1f])
                                                                        bm_1iiiiiii.faces.new([fe1f,ff1f,fg1f])
                                                                        bm_1iiiiiii.faces.new([ff1f,fg1f,fh1f])
                                                                        bm_1iiiiiii.faces.new([fi1f,fj1f,fk1f])
                                                                        bm_1iiiiiii.faces.new([fj1f,fk1f,fl1f])
                                                                        bm_1iiiiiii.faces.new([fk1f,fl1f,fm1f])

                    if type1e == 1:
                        if type2e == 1:
                            if type3e == 0:
                                if type4e == 0:
                                    if type5e == 0:
                                        if type6e == 0:
                                            if type7e == 0:
                                                if type8e == 1:
                                                    if type9e == 1:
                                                        if type10e == 0:
                                                            if type11e == 0:
                                                                if type12e == 0:
                                                                    if type13e == 0:
                                                                        bm_1iiiiii.faces.new([fa1e,fb1e,fc1e])
                                                                        bm_1iiiiii.faces.new([fb1e,fc1e,fd1e])
                                                                        bm_1iiiiii.faces.new([fc1e,fd1e,fe1e])
                                                                        bm_1iiiiii.faces.new([fd1e,fe1e,ff1e])
                                                                        bm_1iiiiii.faces.new([fe1e,ff1e,fg1e])
                                                                        bm_1iiiiii.faces.new([fh1e,fi1e,fj1e])
                                                                        bm_1iiiiii.faces.new([fi1e,fj1e,fk1e])
                                                                        bm_1iiiiii.faces.new([fj1e,fk1e,fl1e])
                                                                        bm_1iiiiii.faces.new([fk1e,fl1e,fm1e])

                    if type1d == 1:
                        if type2d == 1:
                            if type3d == 0:
                                if type4d == 0:
                                    if type5d == 0:
                                        if type6d == 0:
                                            if type7d == 1:
                                                if type8d == 1:
                                                    if type9d == 0:
                                                        if type10d == 0:
                                                            if type11d == 0:
                                                                if type12d == 0:
                                                                    if type13d == 0:
                                                                        bm_1iiiii.faces.new([fa1d,fb1d,fc1d])
                                                                        bm_1iiiii.faces.new([fb1d,fc1d,fd1d])
                                                                        bm_1iiiii.faces.new([fc1d,fd1d,fe1d])
                                                                        bm_1iiiii.faces.new([fd1d,fe1d,ff1d])
                                                                        bm_1iiiii.faces.new([fg1d,fh1d,fi1d])
                                                                        bm_1iiiii.faces.new([fh1d,fi1d,fj1d])
                                                                        bm_1iiiii.faces.new([fi1d,fj1d,fk1d])
                                                                        bm_1iiiii.faces.new([fj1d,fk1d,fl1d])
                                                                        bm_1iiiii.faces.new([fk1d,fl1d,fm1d])

                    if type1c == 1:
                        if type2c == 1:
                            if type3c == 0:
                                if type4c == 0:
                                    if type5c == 0:
                                        if type6c == 1:
                                            if type7c == 1:
                                                if type8c == 0:
                                                    if type9c == 0:
                                                        if type10c == 0:
                                                            if type11c == 0:
                                                                if type12c == 0:
                                                                    if type13c == 0:
                                                                        bm_1iiii.faces.new([fa1c,fb1c,fc1c])
                                                                        bm_1iiii.faces.new([fb1c,fc1c,fd1c])
                                                                        bm_1iiii.faces.new([fc1c,fd1c,fe1c])
                                                                        bm_1iiii.faces.new([ff1c,fg1c,fh1c])
                                                                        bm_1iiii.faces.new([fg1c,fh1c,fi1c])
                                                                        bm_1iiii.faces.new([fh1c,fi1c,fj1c])
                                                                        bm_1iiii.faces.new([fi1c,fj1c,fk1c])
                                                                        bm_1iiii.faces.new([fj1c,fk1c,fl1c])
                                                                        bm_1iiii.faces.new([fk1c,fl1c,fm1c])

                    if type1b == 1:
                        if type2b == 1:
                            if type3b == 0:
                                if type4b == 0:
                                    if type5b == 1:
                                        if type6b == 1:
                                            if type7b == 0:
                                                if type8b == 0:
                                                    if type9b == 0:
                                                        if type10b == 0:
                                                            if type11b == 0:
                                                                if type12b == 0:
                                                                    if type13b == 0:
                                                                        bm_1iii.faces.new([fa1b,fb1b,fc1a])
                                                                        bm_1iii.faces.new([fb1b,fc1b,fd1b])
                                                                        bm_1iii.faces.new([fe1b,ff1b,fg1b])
                                                                        bm_1iii.faces.new([ff1b,fg1b,fh1b])
                                                                        bm_1iii.faces.new([fg1b,fh1b,fi1b])
                                                                        bm_1iii.faces.new([fh1b,fi1b,fj1b])
                                                                        bm_1iii.faces.new([fi1b,fj1b,fk1b])
                                                                        bm_1iii.faces.new([fj1b,fk1b,fl1b])
                                                                        bm_1iii.faces.new([fk1b,fl1b,fm1b])

                    if type1a == 1:
                        if type2a == 1:
                            if type3a == 0:
                                if type4a == 1:
                                    if type5a == 1:
                                        if type6a == 0:
                                            if type7a == 0:
                                                if type8a == 0:
                                                    if type9a == 0:
                                                        if type10a == 0:
                                                            if type11a == 0:
                                                                if type12a == 0:
                                                                    if type13a == 0:
                                                                        bm_1ii.faces.new([fa1a,fb1a,fc1a])
                                                                        bm_1ii.faces.new([fd1a,fe1a,ff1a])
                                                                        bm_1ii.faces.new([fe1a,ff1a,fg1a])
                                                                        bm_1ii.faces.new([ff1a,fg1a,fh1a])
                                                                        bm_1ii.faces.new([fg1a,fh1a,fi1a])
                                                                        bm_1ii.faces.new([fh1a,fi1a,fj1a])
                                                                        bm_1ii.faces.new([fi1a,fj1a,fk1a])
                                                                        bm_1ii.faces.new([fj1a,fk1a,fl1a])
                                                                        bm_1ii.faces.new([fk1a,fl1a,fm1a])

                    if type1 == 1:
                        if type2 == 1:
                            if type3 == 0:
                                if type4 == 0:
                                    if type5 == 0:
                                        if type6 == 0:
                                            if type7 == 0:
                                                if type8 == 0:
                                                    if type9 == 0:
                                                        if type10 == 0:
                                                            if type11 == 0:
                                                                if type12 == 0:
                                                                    if type13 == 0:
                                                                        bm_1i.faces.new([fa1,fb1,fc1])
                                                                        bm_1i.faces.new([fb1,fc1,fd1])
                                                                        bm_1i.faces.new([fc1,fd1,fe1])
                                                                        bm_1i.faces.new([fd1,fe1,ff1])
                                                                        bm_1i.faces.new([fe1,ff1,fg1])
                                                                        bm_1i.faces.new([ff1,fg1,fh1])
                                                                        bm_1i.faces.new([fg1,fh1,fi1])
                                                                        bm_1i.faces.new([fh1,fi1,fj1])
                                                                        bm_1i.faces.new([fi1,fj1,fk1])
                                                                        bm_1i.faces.new([fj1,fk1,fl1])
                                                                        bm_1i.faces.new([fk1,fl1,fm1])
                    
                                                                    
                                
                    
                
                                        
                                    
                
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

    mesh__5a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1dd.from_mesh(mesh__5a)
    objects1dd_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__5a)
    collection.objects.link(objects1dd_)
    bmesh.ops.remove_doubles(bm_1dd, verts = bm_1dd.verts, dist = 0.0001)
    bm_1dd.to_mesh(mesh__5a)

    objects1dd_.parent = arma
    armamodifier1dd_ = objects1dd_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1dd_.object = arma

    vgroups1dd_ = [objects1dd_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #########################################################################################

    mesh__5b = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ddd.from_mesh(mesh__5b)
    objects1ddd_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__5b)
    collection.objects.link(objects1ddd_)
    bmesh.ops.remove_doubles(bm_1ddd, verts = bm_1ddd.verts, dist = 0.0001)
    bm_1ddd.to_mesh(mesh__5b)

    objects1ddd_.parent = arma
    armamodifier1ddd_ = objects1ddd_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ddd_.object = arma

    vgroups1ddd_ = [objects1ddd_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ########################################################################################


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

    mesh__6a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ee.from_mesh(mesh__6a)
    objects1ee_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__6a)
    collection.objects.link(objects1ee_)
    bmesh.ops.remove_doubles(bm_1ee, verts = bm_1ee.verts, dist = 0.0001)
    bm_1ee.to_mesh(mesh__6a)

    objects1ee_.parent = arma
    armamodifier1ee_ = objects1ee_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ee_.object = arma

    vgroups1ee_ = [objects1ee_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__6aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1eee.from_mesh(mesh__6aa)
    objects1eee_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__6aa)
    collection.objects.link(objects1eee_)
    bmesh.ops.remove_doubles(bm_1eee, verts = bm_1eee.verts, dist = 0.0001)
    bm_1eee.to_mesh(mesh__6aa)

    objects1eee_.parent = arma
    armamodifier1eee_ = objects1eee_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1eee_.object = arma

    vgroups1eee_ = [objects1eee_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__6aaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1eeee.from_mesh(mesh__6aaa)
    objects1eeee_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__6aaa)
    collection.objects.link(objects1eeee_)
    bmesh.ops.remove_doubles(bm_1eeee, verts = bm_1eeee.verts, dist = 0.0001)
    bm_1eeee.to_mesh(mesh__6aaa)

    objects1eeee_.parent = arma
    armamodifier1eeee_ = objects1eeee_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1eeee_.object = arma

    vgroups1eeee_ = [objects1eeee_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###########################################################################################
    ###########################################################################################

    mesh__7 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1f.from_mesh(mesh__7)
    objects1f_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__7)
    collection.objects.link(objects1f_)
    bmesh.ops.remove_doubles(bm_1f, verts = bm_1f.verts, dist = 0.0001)
    bm_1f.to_mesh(mesh__7)

    objects1f_.parent = arma
    armamodifier1f_ = objects1f_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1f_.object = arma

    vgroups1f_ = [objects1f_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__7a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ff.from_mesh(mesh__7a)
    objects1ff_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__7a)
    collection.objects.link(objects1ff_)
    bmesh.ops.remove_doubles(bm_1ff, verts = bm_1ff.verts, dist = 0.0001)
    bm_1ff.to_mesh(mesh__7a)

    objects1ff_.parent = arma
    armamodifier1ff_ = objects1ff_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ff_.object = arma

    vgroups1ff_ = [objects1ff_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__7aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1fff.from_mesh(mesh__7aa)
    objects1fff_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__7aa)
    collection.objects.link(objects1fff_)
    bmesh.ops.remove_doubles(bm_1fff, verts = bm_1fff.verts, dist = 0.0001)
    bm_1fff.to_mesh(mesh__7aa)

    objects1fff_.parent = arma
    armamodifier1fff_ = objects1fff_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1fff_.object = arma

    vgroups1fff_ = [objects1fff_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    

    ###########################################################################################
    ###########################################################################################

    mesh__8 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1g.from_mesh(mesh__8)
    objects1g_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8)
    collection.objects.link(objects1g_)
    bmesh.ops.remove_doubles(bm_1g, verts = bm_1g.verts, dist = 0.0001)
    bm_1g.to_mesh(mesh__8)

    objects1g_.parent = arma
    armamodifier1g_ = objects1g_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1g_.object = arma

    vgroups1g_ = [objects1g_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    

    ###########################################################################################

    mesh__8a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1gg.from_mesh(mesh__8a)
    objects1gg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8a)
    collection.objects.link(objects1gg_)
    bmesh.ops.remove_doubles(bm_1gg, verts = bm_1gg.verts, dist = 0.0001)
    bm_1gg.to_mesh(mesh__8a)

    objects1gg_.parent = arma
    armamodifier1gg_ = objects1gg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1gg_.object = arma

    vgroups1gg_ = [objects1gg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    
    ###########################################################################################

    mesh__8aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ggg.from_mesh(mesh__8aa)
    objects1ggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aa)
    collection.objects.link(objects1ggg_)
    bmesh.ops.remove_doubles(bm_1ggg, verts = bm_1ggg.verts, dist = 0.0001)
    bm_1ggg.to_mesh(mesh__8aa)

    objects1ggg_.parent = arma
    armamodifier1ggg_ = objects1ggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ggg_.object = arma

    vgroups1ggg_ = [objects1ggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__8aaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1gggg.from_mesh(mesh__8aaa)
    objects1gggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaa)
    collection.objects.link(objects1gggg_)
    bmesh.ops.remove_doubles(bm_1gggg, verts = bm_1gggg.verts, dist = 0.0001)
    bm_1gggg.to_mesh(mesh__8aaa)

    objects1gggg_.parent = arma
    armamodifier1gggg_ = objects1gggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1gggg_.object = arma

    vgroups1gggg_ = [objects1gggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    mesh__8aaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ggggg.from_mesh(mesh__8aaaa)
    objects1ggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaa)
    collection.objects.link(objects1ggggg_)
    bmesh.ops.remove_doubles(bm_1ggggg, verts = bm_1ggggg.verts, dist = 0.0001)
    bm_1ggggg.to_mesh(mesh__8aaaa)

    objects1ggggg_.parent = arma
    armamodifier1ggggg_ = objects1ggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ggggg_.object = arma

    vgroups1ggggg_ = [objects1ggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__8aaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1gggggg.from_mesh(mesh__8aaaaa)
    objects1gggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaaa)
    collection.objects.link(objects1gggggg_)
    bmesh.ops.remove_doubles(bm_1gggggg, verts = bm_1gggggg.verts, dist = 0.0001)
    bm_1gggggg.to_mesh(mesh__8aaaaa)

    objects1gggggg_.parent = arma
    armamodifier1gggggg_ = objects1gggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1gggggg_.object = arma

    vgroups1gggggg_ = [objects1gggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###############################################################

    mesh__8aaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ggggggg.from_mesh(mesh__8aaaaaa)
    objects1ggggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaaaa)
    collection.objects.link(objects1ggggggg_)
    bmesh.ops.remove_doubles(bm_1ggggggg, verts = bm_1ggggggg.verts, dist = 0.0001)
    bm_1ggggggg.to_mesh(mesh__8aaaaaa)

    objects1ggggggg_.parent = arma
    armamodifier1ggggggg_ = objects1ggggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ggggggg_.object = arma

    vgroups1ggggggg_ = [objects1ggggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__8aaaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1gggggggg.from_mesh(mesh__8aaaaaaa)
    objects1gggggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaaaaa)
    collection.objects.link(objects1gggggggg_)
    bmesh.ops.remove_doubles(bm_1gggggggg, verts = bm_1gggggggg.verts, dist = 0.0001)
    bm_1gggggggg.to_mesh(mesh__8aaaaaaa)

    objects1gggggggg_.parent = arma
    armamodifier1gggggggg_ = objects1gggggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1gggggggg_.object = arma

    vgroups1gggggggg_ = [objects1gggggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__8aaaaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ggggggggg.from_mesh(mesh__8aaaaaaaa)
    objects1ggggggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaaaaaa)
    collection.objects.link(objects1ggggggggg_)
    bmesh.ops.remove_doubles(bm_1ggggggggg, verts = bm_1ggggggggg.verts, dist = 0.0001)
    bm_1ggggggggg.to_mesh(mesh__8aaaaaaaa)

    objects1ggggggggg_.parent = arma
    armamodifier1ggggggggg_ = objects1ggggggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ggggggggg_.object = arma

    vgroups1ggggggggg_ = [objects1ggggggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    
    ###############################################################

    mesh__8aaaaaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1gggggggggg.from_mesh(mesh__8aaaaaaaaa)
    objects1gggggggggg_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__8aaaaaaaaa)
    collection.objects.link(objects1gggggggggg_)
    bmesh.ops.remove_doubles(bm_1gggggggggg, verts = bm_1gggggggggg.verts, dist = 0.0001)
    bm_1gggggggggg.to_mesh(mesh__8aaaaaaaaa)

    objects1gggggggggg_.parent = arma
    armamodifier1gggggggggg_ = objects1gggggggggg_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1gggggggggg_.object = arma

    vgroups1gggggggggg_ = [objects1gggggggggg_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
    
    ###############################################################


    ###############################################################

    mesh__9aaaaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhhhhhhh.from_mesh(mesh__9aaaaaaaa)
    objects1hhhhhhhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaaaaaaa)
    collection.objects.link(objects1hhhhhhhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhhhhhhh.to_mesh(mesh__9aaaaaaaa)

    objects1hhhhhhhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhhhhhhh_ = objects1hhhhhhhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhhhhhhh_ = [objects1hhhhhhhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    ###############################################################

    mesh__9aaaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhhhhhh.from_mesh(mesh__9aaaaaaa)
    objects1hhhhhhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaaaaaa)
    collection.objects.link(objects1hhhhhhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhhhhhh.to_mesh(mesh__9aaaaaaa)

    objects1hhhhhhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhhhhhh_ = objects1hhhhhhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhhhhhh_ = [objects1hhhhhhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__9aaaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhhhhh.from_mesh(mesh__9aaaaaa)
    objects1hhhhhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaaaaa)
    collection.objects.link(objects1hhhhhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhhhhh.to_mesh(mesh__9aaaaaa)

    objects1hhhhhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhhhhh_ = objects1hhhhhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhhhhh_ = [objects1hhhhhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ####################################
    ####################################

    mesh__9aaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhhhh.from_mesh(mesh__9aaaaa)
    objects1hhhhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaaaa)
    collection.objects.link(objects1hhhhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhhhh.to_mesh(mesh__9aaaaa)

    objects1hhhhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhhhh_ = objects1hhhhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhhhh_ = [objects1hhhhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###################
    ###################

    mesh__9aaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhhh.from_mesh(mesh__9aaaa)
    objects1hhhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaaa)
    collection.objects.link(objects1hhhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhhh.to_mesh(mesh__9aaaa)

    objects1hhhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhhh_ = objects1hhhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhhh_ = [objects1hhhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ##########

    mesh__9aaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhhh.from_mesh(mesh__9aaa)
    objects1hhhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aaa)
    collection.objects.link(objects1hhhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhhh, verts = bm_1hhhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhhh.to_mesh(mesh__9aaa)

    objects1hhhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhhh_ = objects1hhhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhhh_ = [objects1hhhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###############
    ###############

    mesh__9aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhhh.from_mesh(mesh__9aa)
    objects1hhhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9aa)
    collection.objects.link(objects1hhhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhhh, verts = bm_1hhhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhhh.to_mesh(mesh__9aa)

    objects1hhhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhhh_ = objects1hhhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhhh_ = [objects1hhhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__9_a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhhh.from_mesh(mesh__9_a)
    objects1hhhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_a)
    collection.objects.link(objects1hhhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhhh, verts = bm_1hhhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhhh.to_mesh(mesh__9_a)

    objects1hhhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhhh_ = objects1hhhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhhh_.object = arma

    vgroups1hhhhhhhhhh_ = [objects1hhhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    ##########################
    ##########################
    ##########################

    mesh__9_aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhhh.from_mesh(mesh__9_aa)
    objects1hhhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aa)
    collection.objects.link(objects1hhhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhhh, verts = bm_1hhhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhhh.to_mesh(mesh__9_aa)

    objects1hhhhhhhhh_.parent = arma
    armamodifier1hhhhhhhhh_ = objects1hhhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhhh_.object = arma

    vgroups1hhhhhhhhh_ = [objects1hhhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###############################
    ###############################

    mesh__9_aaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhhh.from_mesh(mesh__9_aaa)
    objects1hhhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaa)
    collection.objects.link(objects1hhhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhhh, verts = bm_1hhhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhhh.to_mesh(mesh__9_aaa)

    objects1hhhhhhhh_.parent = arma
    armamodifier1hhhhhhhh_ = objects1hhhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhhh_.object = arma

    vgroups1hhhhhhhh_ = [objects1hhhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    ########################################

    ########################################

    mesh__9_aaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhhh.from_mesh(mesh__9_aaaa)
    objects1hhhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa)
    collection.objects.link(objects1hhhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhhh, verts = bm_1hhhhhhh.verts, dist = 0.0001)
    bm_1hhhhhhh.to_mesh(mesh__9_aaaa)

    objects1hhhhhhh_.parent = arma
    armamodifier1hhhhhhh_ = objects1hhhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhhh_.object = arma

    vgroups1hhhhhhh_ = [objects1hhhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #############################################

    mesh__9_aaaa_ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhhh.from_mesh(mesh__9_aaaa_)
    objects1hhhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_)
    collection.objects.link(objects1hhhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhhh, verts = bm_1hhhhhh.verts, dist = 0.0001)
    bm_1hhhhhh.to_mesh(mesh__9_aaaa_)

    objects1hhhhhh_.parent = arma
    armamodifier1hhhhhh_ = objects1hhhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhhh_.object = arma

    vgroups1hhhhhh_ = [objects1hhhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###########################

    mesh__9_aaaa_a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhhh.from_mesh(mesh__9_aaaa_a)
    objects1hhhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_a)
    collection.objects.link(objects1hhhhh_)
    bmesh.ops.remove_doubles(bm_1hhhhh, verts = bm_1hhhhh.verts, dist = 0.0001)
    bm_1hhhhh.to_mesh(mesh__9_aaaa_a)

    objects1hhhhh_.parent = arma
    armamodifier1hhhhh_ = objects1hhhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhhh_.object = arma

    vgroups1hhhhh_ = [objects1hhhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__9_aaaa_aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhhh.from_mesh(mesh__9_aaaa_aa)
    objects1hhhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_aa)
    collection.objects.link(objects1hhhh_)
    bmesh.ops.remove_doubles(bm_1hhhh, verts = bm_1hhhh.verts, dist = 0.0001)
    bm_1hhhh.to_mesh(mesh__9_aaaa_aa)

    objects1hhhh_.parent = arma
    armamodifier1hhhh_ = objects1hhhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhhh_.object = arma

    vgroups1hhhh_ = [objects1hhhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ##############################################

    mesh__9_aaaa_aaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hhh.from_mesh(mesh__9_aaaa_aaa)
    objects1hhh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_aaa)
    collection.objects.link(objects1hhh_)
    bmesh.ops.remove_doubles(bm_1hhh, verts = bm_1hhh.verts, dist = 0.0001)
    bm_1hhh.to_mesh(mesh__9_aaaa_aaa)

    objects1hhh_.parent = arma
    armamodifier1hhh_ = objects1hhh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hhh_.object = arma

    vgroups1hhh_ = [objects1hhh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ####################################################

    mesh__9_aaaa_aaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1hh.from_mesh(mesh__9_aaaa_aaaa)
    objects1hh_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_aaaa)
    collection.objects.link(objects1hh_)
    bmesh.ops.remove_doubles(bm_1hh, verts = bm_1hh.verts, dist = 0.0001)
    bm_1hh.to_mesh(mesh__9_aaaa_aaaa)

    objects1hh_.parent = arma
    armamodifier1hh_ = objects1hh_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1hh_.object = arma

    vgroups1hh_ = [objects1hh_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #############################
    #############################

    mesh__9_aaaa_aaaaa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1h.from_mesh(mesh__9_aaaa_aaaaa)
    objects1h_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__9_aaaa_aaaaa)
    collection.objects.link(objects1h_)
    bmesh.ops.remove_doubles(bm_1h, verts = bm_1h.verts, dist = 0.0001)
    bm_1h.to_mesh(mesh__9_aaaa_aaaaa)

    objects1h_.parent = arma
    armamodifier1h_ = objects1h_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1h_.object = arma

    vgroups1h_ = [objects1h_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    ###############################################################

    mesh__10a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10a)
    objects1iiiiiiiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10a)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10a)

    objects1iiiiiiiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #######################################################################
    #######################################################################

    

    mesh__10b = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10b)
    objects1iiiiiiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10b)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10b)

    objects1iiiiiiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10c = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10c)
    objects1iiiiiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10c)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10c)

    objects1iiiiiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10d = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10d)
    objects1iiiiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10d)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10d)

    objects1iiiiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #############################################################################

    mesh__10e = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10e)
    objects1iiiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10e)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10e)

    objects1iiiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###################################################################################

    mesh__10f = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10f)
    objects1iiiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10f)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10f)

    objects1iiiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###################################################################################

    mesh__10g = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10g)
    objects1iiiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10g)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10g)

    objects1iiiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10h = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiiii.from_mesh(mesh__10h)
    objects1iiiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10h)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiiii.to_mesh(mesh__10h)

    objects1iiiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ##############################################################

    mesh__10i = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiiii.from_mesh(mesh__10i)
    objects1iiiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10i)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiiii.to_mesh(mesh__10i)

    objects1iiiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10j = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiiii.from_mesh(mesh__10j)
    objects1iiiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10j)
    collection.objects.link(objects1iiiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiiii.to_mesh(mesh__10j)

    objects1iiiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10k = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiiii.from_mesh(mesh__10k)
    objects1iiiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10k)
    collection.objects.link(objects1iiiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiiii.to_mesh(mesh__10k)

    objects1iiiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###################################
    ###################################

    mesh__10l = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiiii.from_mesh(mesh__10l)
    objects1iiiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10l)
    collection.objects.link(objects1iiiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiiii.to_mesh(mesh__10l)

    objects1iiiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ####################################
    ####################################

    mesh__10m = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiiii.from_mesh(mesh__10m)
    objects1iiiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10m)
    collection.objects.link(objects1iiiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiiii.to_mesh(mesh__10m)

    objects1iiiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #######################################

    mesh__10n = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiiii.from_mesh(mesh__10n)
    objects1iiiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10n)
    collection.objects.link(objects1iiiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiiii.to_mesh(mesh__10n)

    objects1iiiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiiii_ = objects1iiiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiiii_ = [objects1iiiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #########################################
    #########################################

    mesh__10o = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiiii.from_mesh(mesh__10o)
    objects1iiiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10o)
    collection.objects.link(objects1iiiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiiii, verts = bm_1iiiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiiii.to_mesh(mesh__10o)

    objects1iiiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiiii_ = objects1iiiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiiii_ = [objects1iiiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###############################################

    mesh__10p = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiiii.from_mesh(mesh__10p)
    objects1iiiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10p)
    collection.objects.link(objects1iiiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiiii, verts = bm_1iiiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiiii.to_mesh(mesh__10p)

    objects1iiiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiiii_ = objects1iiiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiiii_ = [objects1iiiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10q = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiiii.from_mesh(mesh__10q)
    objects1iiiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10q)
    collection.objects.link(objects1iiiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiiii, verts = bm_1iiiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiiii.to_mesh(mesh__10q)

    objects1iiiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiiii_ = objects1iiiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiiii_.object = arma

    vgroups1iiiiiiiiiii_ = [objects1iiiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ######################################
    ######################################

    mesh__10r = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiiii.from_mesh(mesh__10r)
    objects1iiiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10r)
    collection.objects.link(objects1iiiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiiii, verts = bm_1iiiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiiii.to_mesh(mesh__10r)

    objects1iiiiiiiiii_.parent = arma
    armamodifier1iiiiiiiiii_ = objects1iiiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiiii_.object = arma

    vgroups1iiiiiiiiii_ = [objects1iiiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    #######################################
    #######################################

    mesh__10s = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiiii.from_mesh(mesh__10s)
    objects1iiiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10s)
    collection.objects.link(objects1iiiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiiii, verts = bm_1iiiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiiii.to_mesh(mesh__10s)

    objects1iiiiiiiii_.parent = arma
    armamodifier1iiiiiiiii_ = objects1iiiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiiii_.object = arma

    vgroups1iiiiiiiii_ = [objects1iiiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ##############################################################

    mesh__10t = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiiii.from_mesh(mesh__10t)
    objects1iiiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10t)
    collection.objects.link(objects1iiiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiiii, verts = bm_1iiiiiiii.verts, dist = 0.0001)
    bm_1iiiiiiii.to_mesh(mesh__10t)

    objects1iiiiiiii_.parent = arma
    armamodifier1iiiiiiii_ = objects1iiiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiiii_.object = arma

    vgroups1iiiiiiii_ = [objects1iiiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ######################################################################################################

    mesh__10u = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiiii.from_mesh(mesh__10u)
    objects1iiiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10u)
    collection.objects.link(objects1iiiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiiii, verts = bm_1iiiiiii.verts, dist = 0.0001)
    bm_1iiiiiii.to_mesh(mesh__10u)

    objects1iiiiiii_.parent = arma
    armamodifier1iiiiiii_ = objects1iiiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiiii_.object = arma

    vgroups1iiiiiii_ = [objects1iiiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ###############################################################

    mesh__10v = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiiii.from_mesh(mesh__10v)
    objects1iiiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10v)
    collection.objects.link(objects1iiiiii_)
    bmesh.ops.remove_doubles(bm_1iiiiii, verts = bm_1iiiiii.verts, dist = 0.0001)
    bm_1iiiiii.to_mesh(mesh__10v)

    objects1iiiiii_.parent = arma
    armamodifier1iiiiii_ = objects1iiiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiiii_.object = arma

    vgroups1iiiiii_ = [objects1iiiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ####################################################################

    mesh__10w = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiiii.from_mesh(mesh__10w)
    objects1iiiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10w)
    collection.objects.link(objects1iiiii_)
    bmesh.ops.remove_doubles(bm_1iiiii, verts = bm_1iiiii.verts, dist = 0.0001)
    bm_1iiiii.to_mesh(mesh__10w)

    objects1iiiii_.parent = arma
    armamodifier1iiiii_ = objects1iiiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiiii_.object = arma

    vgroups1iiiii_ = [objects1iiiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10x = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iiii.from_mesh(mesh__10x)
    objects1iiii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10x)
    collection.objects.link(objects1iiii_)
    bmesh.ops.remove_doubles(bm_1iiii, verts = bm_1iiii.verts, dist = 0.0001)
    bm_1iiii.to_mesh(mesh__10x)

    objects1iiii_.parent = arma
    armamodifier1iiii_ = objects1iiii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iiii_.object = arma

    vgroups1iiii_ = [objects1iiii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    ##############################################################

    mesh__10y = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1iii.from_mesh(mesh__10y)
    objects1iii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10y)
    collection.objects.link(objects1iii_)
    bmesh.ops.remove_doubles(bm_1iii, verts = bm_1iii.verts, dist = 0.0001)
    bm_1iii.to_mesh(mesh__10y)

    objects1iii_.parent = arma
    armamodifier1iii_ = objects1iii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1iii_.object = arma

    vgroups1iii_ = [objects1iii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10z = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1ii.from_mesh(mesh__10z)
    objects1ii_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10z)
    collection.objects.link(objects1ii_)
    bmesh.ops.remove_doubles(bm_1ii, verts = bm_1ii.verts, dist = 0.0001)
    bm_1ii.to_mesh(mesh__10z)

    objects1ii_.parent = arma
    armamodifier1ii_ = objects1ii_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1ii_.object = arma

    vgroups1ii_ = [objects1ii_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh__10aa = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm_1i.from_mesh(mesh__10aa)
    objects1i_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh__10aa)
    collection.objects.link(objects1i_)
    bmesh.ops.remove_doubles(bm_1i, verts = bm_1i.verts, dist = 0.0001)
    bm_1i.to_mesh(mesh__10aa)

    objects1i_.parent = arma
    armamodifier1i_ = objects1i_.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier1i_.object = arma

    vgroups1i_ = [objects1i_.vertex_groups.new(name = bone.name) for bone in arma.data.bones]




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
            
            
                
            
    
