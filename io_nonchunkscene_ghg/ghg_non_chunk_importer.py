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
                pass
                                
                    
                
                                        
                                    
                
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
            
            
                
            
    
