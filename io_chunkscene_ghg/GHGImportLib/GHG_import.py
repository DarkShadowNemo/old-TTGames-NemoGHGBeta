from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio
from .pearl import *

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

    idx1A=0

    bone_names=[]
    bone_parentlist=[]

    idx1=0
    idx1_=0

    vertices2=[]
    vertices2pt2=[]
    vertices2_=[]
    faces2=[]

    vertices1=[]
    faces1=[]

    vertices3=[]
    faces3=[]

    vertices3pt2a=[]
    faces3pt2a=[]

    vertices3pt2=[]
    faces3pt2=[]
    
    vertices2pt2=[]
    faces2pt2=[]

    fa1=-3
    fb1=-2
    fc1=-1

    fa3=-3
    fb3=-2
    fc3=-1

    fa3a=-4
    fb3a=-3
    fc3a=-2
    fd3a=-1
    
    fa1_=-4
    fb1_=-3
    fc1_=-2
    
    fa1pt2=-4
    fb1pt2=-3
    fc1pt2=-2
    fd1pt2=-1

    fa=-1
    fb=0
    fc=1

    uvs3=[]
    uvs3pt2=[]

    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')

    f.seek(0)
    FileSize_ = unpack("<I", f.read(4))[0]
    null1_ = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    TextureEntrySize1 = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    f.seek(-4,1)
    MaterialCount2 = unpack("<I", f.read(4))[0]
    MaterialEntrySize1 = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    RotSclBoneEntrySize1 = unpack("<I", f.read(4))[0]
    SclBoneEntrySize1 = unpack("<I", f.read(4))[0]
    PosBoneEntrySize1 = unpack("<I", f.read(4))[0]
    ObjectCount = unpack("<I", f.read(4))[0]
    ObjectCountEntrySize1 = unpack("<I", f.read(4))[0]
    NamedtableEntrySize1 = unpack("<I", f.read(4))[0]
    NamedtableLength1,=unpack("<I", f.read(4))
    UnkCount1 = unpack("<I", f.read(4))[0]
    UnkCountEntrySize1 = unpack("<I", f.read(4))[0]
    UnkCount2 = unpack("<I", f.read(4))[0]
    UnkCountEntrySize2 = unpack("<I", f.read(4))[0]
    defaultlayercount = unpack("<I", f.read(4))[0]
    defaultlayerEntrySize1 = unpack("<I", f.read(4))[0]
    bsaEntrySize1 = unpack("<I", f.read(4))[0]
    for i in range(11):
        float01 = unpack("<f", f.read(4))[0]
        float01-=float01
    size01 = unpack("<I", f.read(4))[0]
    float02 = unpack("<f", f.read(4))[0]
    type01 = unpack("<I", f.read(4))[0]
    typeSize1 = unpack("<I", f.read(4))[0]
    if TextureCount == 0:
        pass
    elif TextureCount != 0:
        if TextureEntrySize1 == 144 or TextureEntrySize1 == 148 or TextureEntrySize1 == 152:
            f.seek(0)
            f.seek(NamedtableEntrySize1,0)
            ntbl_buffer = bio(f.read(NamedtableEntrySize1))
            name_i = 0
            while 1:
                name = fetch_cstr(ntbl_buffer).decode('ascii')
                if not name: break
                name_i+=1
            f.seek(0)
            f.seek(RotSclBoneEntrySize1,0)
            for i in range(BoneCount):
                mrscl1 = unpack("<f", f.read(4))[0]
                mrscl2 = unpack("<f", f.read(4))[0]
                mrscl3 = unpack("<f", f.read(4))[0]
                mrscl4 = unpack("<f", f.read(4))[0]
                mrscl5 = unpack("<f", f.read(4))[0]
                mrscl6 = unpack("<f", f.read(4))[0]
                mrscl7 = unpack("<f", f.read(4))[0]
                mrscl8 = unpack("<f", f.read(4))[0]
                mrscl9 = unpack("<f", f.read(4))[0]
                mrsc20 = unpack("<f", f.read(4))[0]
                mrsc21 = unpack("<f", f.read(4))[0]
                mrsc22 = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                bdiv4_v00 = unpack("<f", f.read(4))[0]
                bdiv4_v04 = unpack("<f", f.read(4))[0]
                bdiv4_v08 = unpack("<f", f.read(4))[0]
                f.seek(4,1)
                bone_parent,=unpack("b", f.read(1))
                bone_parentlist.append(bone_parent)

                name_offset,=unpack("<L", f.read(4)) # WHAT doesnt work
                f.seek(11,1)
                try:
                    ntbl_buffer.seek(name_offset-1)
                except:
                    ValueError
            f.seek(0)
            f.seek(PosBoneEntrySize1,0)
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
                posx = -unpack("<f", f.read(4))[0]
                posy = -unpack("<f", f.read(4))[0]
                posz = -unpack("<f", f.read(4))[0]
                ScaleW = unpack("<f", f.read(4))[0]
                m1 = ([ScaleX,rotationz,rotationy,null1])
                m2 = ([nrotationz,ScaleY,rotationx,nrotationy])
                m3 = ([null2,nrotationx,ScaleZ,null3])
                m4 = ([posx,posy,posz,ScaleW])

                matrix = mathutils.Matrix([m1,m3,m2,m4]).inverted().to_3x3().transposed()
                bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
                bone_names.append([bone_name])
                

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
            Chunks = f.read()
            f.seek(0)

            while f.tell() < len(Chunks):
                Chunk = f.read(4)
                if Chunk == b"\x03\x01\x00\x01":
                    f.seek(2,1)
                    stripcount = unpack("B", f.read(1))[0]
                    flag001 = unpack("B", f.read(1))[0]
                    if flag001 == 0x6C:
                        if stripcount == 0:
                            pass
                        elif stripcount == 1:
                            pass
                        elif stripcount == 2:
                            pass
                        elif stripcount:
                            for j in range(stripcount):
                                vx = unpack("<f", f.read(4))[0]
                                vy = unpack("<f", f.read(4))[0]
                                vz = unpack("<f", f.read(4))[0]
                                faceon = unpack("B", f.read(1))[0]==False
                                valueon = unpack("B", f.read(1))[0]
                                nz = unpack("<h", f.read(2))[0]
                                vertices1.append([vx,vz,vy])
                                fa+=1
                                fb+=1
                                fc+=1
                                if faceon > 0:
                                    faces1.append([j+j+faceon-faceon-1+fa-j-j-1+j%2,j-j+faceon-faceon+1+fb-2-1+j-j-j%2,j+faceon-faceon+fc-j+2-4])
                        
                elif Chunk == b"\x03\x02\x00\x01":
                    f.seek(2,1)
                    VertexCount = unpack("B", f.read(1))[0]//2
                    flag01 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6D:
                        if VertexCount == 0:
                            pass
                        elif VertexCount == 1:
                            pass
                        elif VertexCount == 2:
                            pass
                        elif VertexCount == 3:
                            for i in range(VertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                fn = unpack("<h", f.read(2))[0] / 4096
                                ux = unpack("<h", f.read(2))[0] / 4096
                                uy = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2.append([vx,vz,vy])
                            for i in range(VertexCount-2):
                                fa1+=1*3
                                fb1+=1*3
                                fc1+=1*3
                                faces2.append([fa1,fb1,fc1])
                        elif VertexCount:
                            for i in range(VertexCount):
                                vx_ = unpack("<h", f.read(2))[0] / 4096
                                vy_ = unpack("<h", f.read(2))[0] / 4096
                                vz_ = unpack("<h", f.read(2))[0] / 4096
                                fn_ = unpack("<h", f.read(2))[0] / 4096
                                ux_ = unpack("<h", f.read(2))[0] / 4096
                                uy_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2pt2.append([vx_,vz_,vy_])
                            for i in range(VertexCount):
                                f.seek(-16,1)
                            for i in range(VertexCount):
                                vx1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fa1_
                                vy1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fb1_
                                vz1 = unpack("<h", f.read(2))[0] / 4096 / 10 + fc1_
                                fn1 = unpack("<h", f.read(2))[0] / 4096
                                ux1 = unpack("<h", f.read(2))[0] / 4096
                                uy1 = unpack("<h", f.read(2))[0] / 4096
                                vx2 = vx1
                                vy2 = vy1
                                vz2 = vz1
                                f.seek(4,1)
                                fa1_+=1*4
                                fb1_+=1*4
                                fc1_+=1*4
                                idx1+=1
                                
                                if idx1 == 1:
                                    vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))
                                    
                                elif idx1 == 2:
                                    vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))
                                elif idx1 == 3:
                                    vertices2_.append(set([round(vx1,3),round(vz1,3),round(vy1,3)]))

                elif Chunk == b"\x04\x02\x00\x01":
                    f.seek(2,1)
                    stripcount = unpack("B", f.read(1))[0]//2
                    flag001 = unpack("B", f.read(1))[0]
                    if flag001 == 0x6C:
                        if stripcount == 0:
                            pass
                        elif stripcount == 1:
                            pass
                        elif stripcount == 2:
                            pass
                        elif stripcount == 3:
                            for i in range(1):
                                vx1_ = unpack("<f", f.read(4))[0];vy1_ = unpack("<f", f.read(4))[0];vz1_ = unpack("<f", f.read(4))[0];brightness1_ = unpack("<f", f.read(4))[0];uvx1_ = unpack("<f", f.read(4))[0];uvy1_ = unpack("<f", f.read(4))[0];unk1_ = unpack("<f", f.read(4))[0];faceon1_ = unpack("B", f.read(1))[0];valueon1_ = unpack("B", f.read(1))[0];nz1_ = unpack("<h", f.read(2))[0];vx2_ = unpack("<f", f.read(4))[0];vy2_ = unpack("<f", f.read(4))[0];vz2_ = unpack("<f", f.read(4))[0];brightness2_ = unpack("<f", f.read(4))[0];uvx2_ = unpack("<f", f.read(4))[0];uvy2_ = unpack("<f", f.read(4))[0];unk2_ = unpack("<f", f.read(4))[0];faceon2_ = unpack("B", f.read(1))[0];valueon2_ = unpack("B", f.read(1))[0];nz2_ = unpack("<h", f.read(2))[0];vx3_ = unpack("<f", f.read(4))[0];vy3_ = unpack("<f", f.read(4))[0];vz3_ = unpack("<f", f.read(4))[0];brightness3_ = unpack("<f", f.read(4))[0];uvx3_ = unpack("<f", f.read(4))[0];uvy3_ = unpack("<f", f.read(4))[0];unk3_ = unpack("<f", f.read(4))[0];faceon3_ = unpack("B", f.read(1))[0];valueon3_ = unpack("B", f.read(1))[0];nz3_ = unpack("<h", f.read(2))[0]
                            offset1 = unpack("<I", f.read(4))[0]
                            if offset1 == 16777473:
                                if faceon1_ == 1:
                                    if faceon2_ == 1:
                                        if faceon3_ == 0:
                                            vertices3.append([vx1_,vz1_,vy1_]);vertices3.append([vx2_,vz2_,vy2_]);vertices3.append([vx3_,vz3_,vy3_]);fa3+=1*3;fb3+=1*3;fc3+=1*3;faces3.append([fa3,fb3,fc3]);uvs3.append([uvx1_,-uvy1_]);uvs3.append([uvx2_,-uvy2_]);uvs3.append([uvx3_,-uvy3_])
                        elif stripcount == 4:
                            for i in range(1):
                                vx4_ = unpack("<f", f.read(4))[0];vy4_ = unpack("<f", f.read(4))[0];vz4_ = unpack("<f", f.read(4))[0];brightness4_ = unpack("<f", f.read(4))[0];uvx4_ = unpack("<f", f.read(4))[0];uvy4_ = unpack("<f", f.read(4))[0];unk4_ = unpack("<f", f.read(4))[0];faceon4_ = unpack("B", f.read(1))[0];valueon4_ = unpack("B", f.read(1))[0];nz4_ = unpack("<h", f.read(2))[0];vx5_ = unpack("<f", f.read(4))[0];vy5_ = unpack("<f", f.read(4))[0];vz5_ = unpack("<f", f.read(4))[0];brightness5_ = unpack("<f", f.read(4))[0];uvx5_ = unpack("<f", f.read(4))[0];uvy5_ = unpack("<f", f.read(4))[0];unk5_ = unpack("<f", f.read(4))[0];faceon5_ = unpack("B", f.read(1))[0];valueon5_ = unpack("B", f.read(1))[0];nz5_ = unpack("<h", f.read(2))[0];vx6_ = unpack("<f", f.read(4))[0];vy6_ = unpack("<f", f.read(4))[0];vz6_ = unpack("<f", f.read(4))[0];brightness6_ = unpack("<f", f.read(4))[0];uvx6_ = unpack("<f", f.read(4))[0];uvy6_ = unpack("<f", f.read(4))[0];unk6_ = unpack("<f", f.read(4))[0];faceon6_ = unpack("B", f.read(1))[0];valueon6_ = unpack("B", f.read(1))[0];nz6_ = unpack("<h", f.read(2))[0];vx7_ = unpack("<f", f.read(4))[0];vy7_ = unpack("<f", f.read(4))[0];vz7_ = unpack("<f", f.read(4))[0];brightness7_ = unpack("<f", f.read(4))[0];uvx7_ = unpack("<f", f.read(4))[0];uvy7_ = unpack("<f", f.read(4))[0];unk7_ = unpack("<f", f.read(4))[0];faceon7_ = unpack("B", f.read(1))[0];valueon7_ = unpack("B", f.read(1))[0];nz7_ = unpack("<h", f.read(2))[0]
                            for i in range(1):
                                f.seek(-128,1)#
                            for i in range(1):
                                vx4_a = unpack("<f", f.read(4))[0];vy4_a = unpack("<f", f.read(4))[0];vz4_a = unpack("<f", f.read(4))[0];brightness4_a = unpack("<f", f.read(4))[0];uvx4_a = unpack("<f", f.read(4))[0];uvy4_a = unpack("<f", f.read(4))[0];unk4_a = unpack("<f", f.read(4))[0];faceon4_a = unpack("B", f.read(1))[0];valueon4_a = unpack("B", f.read(1))[0];nz4_a = unpack("<h", f.read(2))[0];vx5_a = unpack("<f", f.read(4))[0];vy5_a = unpack("<f", f.read(4))[0];vz5_a = unpack("<f", f.read(4))[0];brightness5_a = unpack("<f", f.read(4))[0];uvx5_a = unpack("<f", f.read(4))[0];uvy5_a = unpack("<f", f.read(4))[0];unk5_a = unpack("<f", f.read(4))[0];faceon5_a = unpack("B", f.read(1))[0];valueon5_a = unpack("B", f.read(1))[0];nz5_a = unpack("<h", f.read(2))[0];vx6_a = unpack("<f", f.read(4))[0];vy6_a = unpack("<f", f.read(4))[0];vz6_a = unpack("<f", f.read(4))[0];brightness6_a = unpack("<f", f.read(4))[0];uvx6_a = unpack("<f", f.read(4))[0];uvy6_a = unpack("<f", f.read(4))[0];unk6_a = unpack("<f", f.read(4))[0];faceon6_a = unpack("B", f.read(1))[0];valueon6_a = unpack("B", f.read(1))[0];nz6_a = unpack("<h", f.read(2))[0];vx7_a = unpack("<f", f.read(4))[0];vy7_a = unpack("<f", f.read(4))[0];vz7_a = unpack("<f", f.read(4))[0];brightness7_a = unpack("<f", f.read(4))[0];uvx7_a = unpack("<f", f.read(4))[0];uvy7_a = unpack("<f", f.read(4))[0];unk7_a = unpack("<f", f.read(4))[0];faceon7_a = unpack("B", f.read(1))[0];valueon7_a = unpack("B", f.read(1))[0];nz7_a = unpack("<h", f.read(2))[0]
                            for i in range(1):
                                f.seek(-128,1)
                            for i in range(1):
                                vx4_a_ = unpack("<f", f.read(4))[0];vy4_a_ = unpack("<f", f.read(4))[0];vz4_a_ = unpack("<f", f.read(4))[0];brightness4_a_ = unpack("<f", f.read(4))[0];uvx4_a_ = unpack("<f", f.read(4))[0];uvy4_a_ = unpack("<f", f.read(4))[0];unk4_a_ = unpack("<f", f.read(4))[0];faceon4_a_ = unpack("B", f.read(1))[0];valueon4_a_ = unpack("B", f.read(1))[0];nz4_a_ = unpack("<h", f.read(2))[0];vx5_a_ = unpack("<f", f.read(4))[0];vy5_a_ = unpack("<f", f.read(4))[0];vz5_a_ = unpack("<f", f.read(4))[0];brightness5_a_ = unpack("<f", f.read(4))[0];uvx5_a_ = unpack("<f", f.read(4))[0];uvy5_a_ = unpack("<f", f.read(4))[0];unk5_a_ = unpack("<f", f.read(4))[0];faceon5_a_ = unpack("B", f.read(1))[0];valueon5_a_ = unpack("B", f.read(1))[0];nz5_a_ = unpack("<h", f.read(2))[0];vx6_a_ = unpack("<f", f.read(4))[0];vy6_a_ = unpack("<f", f.read(4))[0];vz6_a_ = unpack("<f", f.read(4))[0];brightness6_a_ = unpack("<f", f.read(4))[0];uvx6_a_ = unpack("<f", f.read(4))[0];uvy6_a_ = unpack("<f", f.read(4))[0];unk6_a_ = unpack("<f", f.read(4))[0];faceon6_a_ = unpack("B", f.read(1))[0];valueon6_a_ = unpack("B", f.read(1))[0];nz6_a_ = unpack("<h", f.read(2))[0];vx7_a_ = unpack("<f", f.read(4))[0];vy7_a_ = unpack("<f", f.read(4))[0];vz7_a_ = unpack("<f", f.read(4))[0];brightness7_a_ = unpack("<f", f.read(4))[0];uvx7_a_ = unpack("<f", f.read(4))[0];uvy7_a_ = unpack("<f", f.read(4))[0];unk7_a_ = unpack("<f", f.read(4))[0];faceon7_a_ = unpack("B", f.read(1))[0];valueon7_a_ = unpack("B", f.read(1))[0];nz7_a_ = unpack("<h", f.read(2))[0]
                            offset4 = unpack("<I", f.read(4))[0]
                            f.seek(-4,1)
                            offset2 = unpack("<I", f.read(4))[0]
                            f.seek(-4,1)
                            offset3 = unpack("<I", f.read(4))[0]
                            if offset4 == 1627553811:
                                offset4a = unpack("<I", f.read(4))[0]
                                if offset4a == 65540:
                                    f.seek(2,1)
                                    vertexCount4a = unpack("B", f.read(1))[0]//2
                                    flag4a = unpack("B", f.read(1))[0]
                                    if flag4a == 0x6C:
                                        if vertexCount4a == 1:
                                            for i in range(1):
                                                vx4_offaa = unpack("<f", f.read(4))[0];vy4_offaa = unpack("<f", f.read(4))[0];vz4_offaa = unpack("<f", f.read(4))[0];face_offaa = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offaa = unpack("<f", f.read(4))[0];uvy4_offaa = unpack("<f", f.read(4))[0];f.seek(8,1)
                                            offset4b = unpack("<I", f.read(4))[0]
                                            if offset4b == 1627553819:
                                                offset4c = unpack("<I", f.read(4))[0]
                                                if offset4c == 2:
                                                    f.seek(2,1)
                                                    vertexCount4c = unpack("B", f.read(1))[0]//2
                                                    flag4c = unpack("B", f.read(1))[0]
                                                    if flag4c == 0x6C:
                                                        if vertexCount4c == 12:
                                                            vx4_offbb = unpack("<f", f.read(4))[0];vy4_offbb = unpack("<f", f.read(4))[0];vz4_offbb = unpack("<f", f.read(4))[0];face_offbb = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb = unpack("<f", f.read(4))[0];uvy4_offbb = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb1 = unpack("<f", f.read(4))[0]
                            if offset3 == 1627553811:
                                offset3a = unpack("<I", f.read(4))[0]
                                if offset3a == 65538:
                                    offset3b = unpack("<I", f.read(4))[0]
                                    if offset3b == 1627553815:
                                        offset3c = unpack("<I", f.read(4))[0]
                                        if offset3c == 65540:
                                            f.seek(2,1)
                                            vertexCount3c = unpack("B", f.read(1))[0]//2
                                            flag3c = unpack("B", f.read(1))[0]
                                            if flag3c == 0x6C:
                                                if vertexCount3c == 2:
                                                    #0x65960
                                                    for i in range(1):
                                                        vx4_off = unpack("<f", f.read(4))[0];vy4_off = unpack("<f", f.read(4))[0];vz4_off = unpack("<f", f.read(4))[0];face_off1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_off1 = unpack("<f", f.read(4))[0];uvy4_off1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_off_ = unpack("<f", f.read(4))[0];vy4_off_ = unpack("<f", f.read(4))[0];vz4_off_ = unpack("<f", f.read(4))[0];face_off = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_off = unpack("<f", f.read(4))[0];uvy4_off = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                    offset3d = unpack("<I", f.read(4))[0]
                                                    if offset3d == 1627553827:
                                                        offset3e = unpack("<I", f.read(4))[0]
                                                        if offset3e == 65540:
                                                            offset3f = unpack("<I", f.read(4))[0]
                                                            if offset3f == 1627553831:
                                                                offset3g = unpack("<I", f.read(4))[0]
                                                                if offset3g == 65544:
                                                                    f.seek(2,1)
                                                                    vertexCount3g = unpack("B", f.read(1))[0]//2
                                                                    flag3g = unpack("B", f.read(1))[0]
                                                                    if flag3g == 0x6C:
                                                                        if vertexCount3g == 3:
                                                                            for i in range(1):
                                                                                vx4_offa = unpack("<f", f.read(4))[0];vy4_offa = unpack("<f", f.read(4))[0];vz4_offa = unpack("<f", f.read(4))[0];face_off1a = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offa = unpack("<f", f.read(4))[0];uvy4_offa = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_off1a = unpack("<f", f.read(4))[0];vy4_off1a = unpack("<f", f.read(4))[0];vz4_off1a = unpack("<f", f.read(4))[0];face_off1a_ = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_off1a = unpack("<f", f.read(4))[0];uvy4_off1a = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_off2a = unpack("<f", f.read(4))[0];vy4_off2a = unpack("<f", f.read(4))[0];vz4_off2a = unpack("<f", f.read(4))[0];face_off2a = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_off2a = unpack("<f", f.read(4))[0];uvy4_off2a = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                            offset3h = unpack("<I", f.read(4))[0]
                                                                            if offset3h == 1627553847:
                                                                                offset3i = unpack("<I", f.read(4))[0]
                                                                                if offset3i == 65547:
                                                                                    f.seek(2,1)
                                                                                    vertexCount3i = unpack("B", f.read(1))[0]//2
                                                                                    flag3i = unpack("B", f.read(1))[0]
                                                                                    if flag3i == 0x6C:
                                                                                        #0x3F80026100000000
                                                                                        if vertexCount3i == 1:
                                                                                            for i in range(1):
                                                                                                vx4_offb = unpack("<f", f.read(4))[0];vy4_offb = unpack("<f", f.read(4))[0];vz4_offb = unpack("<f", f.read(4))[0];face_off1b = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offb = unpack("<f", f.read(4))[0];uvy4_offb = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                            offset3j = unpack("<I", f.read(4))[0]
                                                                                            if offset3j == 1627553855:
                                                                                                offset3k = unpack("<I", f.read(4))[0]
                                                                                                if offset3k == 13:
                                                                                                    f.seek(2,1)
                                                                                                    vertexCount3k = unpack("B", f.read(1))[0]//2
                                                                                                    flag3k = unpack("B", f.read(1))[0]
                                                                                                    if flag3k == 0x6C:
                                                                                                        if vertexCount3k == 1:
                                                                                                            for i in range(1):
                                                                                                                vx4_offc = unpack("<f", f.read(4))[0];vy4_offc = unpack("<f", f.read(4))[0];vz4_offc = unpack("<f", f.read(4))[0];face_off1c = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offc = unpack("<f", f.read(4))[0];uvy4_offc = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                            offset3l = unpack("<I", f.read(4))[0]
                                                                                                            if offset3l == 1627553863:
                                                                                                                offset3m = unpack("<I", f.read(4))[0]
                                                                                                                if offset3m == 65553:
                                                                                                                    offset3n = unpack("<I", f.read(4))[0]
                                                                                                                    if offset3n == 1627553867:
                                                                                                                        offset3o = unpack("<I", f.read(4))[0]
                                                                                                                        if offset3o == 65551:
                                                                                                                            f.seek(2,1)
                                                                                                                            vertexCount3o = unpack("B", f.read(1))[0]//2
                                                                                                                            flag3o = unpack("B", f.read(1))[0]
                                                                                                                            if flag3o == 0x6C:
                                                                                                                                if vertexCount3o == 2:
                                                                                                                                    for i in range(1):
                                                                                                                                        vx4_offd = unpack("<f", f.read(4))[0];vy4_offd = unpack("<f", f.read(4))[0];vz4_offd = unpack("<f", f.read(4))[0];face_off1d = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offd = unpack("<f", f.read(4))[0];uvy4_offd = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offe = unpack("<f", f.read(4))[0];vy4_offe = unpack("<f", f.read(4))[0];vz4_offe = unpack("<f", f.read(4))[0];face_off1e = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offe = unpack("<f", f.read(4))[0];uvy4_offe = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                                                    offset3p = unpack("<I", f.read(4))[0]
                                                                                                                                    if offset3p == 1627553879:
                                                                                                                                        offset3q = unpack("<I", f.read(4))[0]
                                                                                                                                        if offset3q == 1:
                                                                                                                                            offset3r = unpack("<I", f.read(4))[0]
                                                                                                                                            if offset3r == 16777473:
                                                                                                                                                if faceon4_a == 1:
                                                                                                                                                    if faceon5_a == 1:
                                                                                                                                                        if faceon6_a == 0:
                                                                                                                                                            if faceon7_a == 0:
                                                                                                                                                                if face_off1 == 0:
                                                                                                                                                                    if face_off == 0:
                                                                                                                                                                        if face_off1a == 0:
                                                                                                                                                                            if face_off1a_ == 0:
                                                                                                                                                                                if face_off2a == 0:
                                                                                                                                                                                    if face_off1b == 0:
                                                                                                                                                                                        if face_off1c == 0:
                                                                                                                                                                                            if face_off1d == 0:
                                                                                                                                                                                                if face_off1e == 0:
                                                                                                                                                                                                    vertices3pt2a.append([vx4_a,vz4_a,vy4_a])
                                                                                                                                                                                                    vertices3pt2a.append([vx5_a,vz5_a,vy5_a])
                                                                                                                                                                                                    vertices3pt2a.append([vx6_a,vz6_a,vy6_a])
                                                                                                                                                                                                    vertices3pt2a.append([vx7_a,vz7_a,vy7_a])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_off,vz4_off,vy4_off])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_off_,vz4_off_,vy4_off_])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_offa,vz4_offa,vy4_offa])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_off1a,vz4_off1a,vy4_off1a])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_off2a,vz4_off2a,vy4_off2a])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_offb,vz4_offb,vy4_offb])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_offc,vz4_offc,vy4_offc])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_offd,vz4_offd,vy4_offd])
                                                                                                                                                                                                    vertices3pt2a.append([vx4_offe,vz4_offe,vy4_offe])
                                                                                                                                                                                                    faces3pt2a.append([0,1,2])
                                                                                                                                                                                                    faces3pt2a.append([1,2,3])
                                                                                                                                                                                                    faces3pt2a.append([1,3,4])
                                                                                                                                                                                                    faces3pt2a.append([3,4,5])
                                                                                                                                                                                                    faces3pt2a.append([5,3,6])
                                                                                                                                                                                                    faces3pt2a.append([5,6,7])
                                                                                                                                                                                                    faces3pt2a.append([6,7,8])
                                                                                                                                                                                                    faces3pt2a.append([6,8,9])
                                                                                                                                                                                                    faces3pt2a.append([8,9,10])
                                                                                                                                                                                                    faces3pt2a.append([9,10,11])
                                                                                                                                                                                                    faces3pt2a.append([9,11,12])
                                                                                                                                                                                                    faces3pt2a.append([11,12,0])
                                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                                                                
                                                                                                                                                                    

                
                                                                                                                        


                            if offset2 == 16777473:
                                if faceon4_ == 1:
                                    if faceon5_ == 1:
                                        if faceon6_ == 0:
                                            if faceon7_ == 0:
                                                vertices3pt2.append([vx4_,vz4_,vy4_])
                                                vertices3pt2.append([vx5_,vz5_,vy5_])
                                                vertices3pt2.append([vx6_,vz6_,vy6_])
                                                vertices3pt2.append([vx7_,vz7_,vy7_])
                                                fa3a+=1*4
                                                fb3a+=1*4
                                                fc3a+=1*4
                                                fd3a+=1*4
                                                faces3pt2.append([fa3a,fb3a,fc3a])
                                                faces3pt2.append([fb3a,fc3a,fd3a])
                                                uvs3pt2.append([uvx4_,-uvy4_])
                                                uvs3pt2.append([uvx5_,-uvy5_])
                                                uvs3pt2.append([uvx6_,-uvy6_])
                                                uvs3pt2.append([uvx7_,-uvy7_])
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2.from_pydata(vertices2, [], faces2)
    object2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(object2)
    
    mesh2_ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2_.from_pydata(vertices2pt2, [], [])
    object2_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2_)
    collection.objects.link(object2_)

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3.from_pydata(vertices3, [], faces3)
    object3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(object3)

    mesh3pt2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3pt2.from_pydata(vertices3pt2a, [], faces3pt2a)
    object3pt2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3pt2)
    collection.objects.link(object3pt2)

    mesh3pt2a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3pt2a.from_pydata(vertices3pt2, [], faces3pt2)
    object3pt2a = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3pt2a)
    collection.objects.link(object3pt2a)

    uv_tex3 = mesh3.uv_layers.new()
    uv_layer3 = mesh3.uv_layers[0].data
    vert_loops3 = {}
    for l in mesh3.loops:
        vert_loops3.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3):
        for li in vert_loops3[i]:
            uv_layer3[li].uv = coord

    uv_tex3a = mesh3pt2a.uv_layers.new()
    uv_layer3a = mesh3pt2a.uv_layers[0].data
    vert_loops3a = {}
    for l in mesh3pt2a.loops:
        vert_loops3a.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3pt2):
        for li in vert_loops3a[i]:
            uv_layer3a[li].uv = coord
    
    #if vertices2_[0:3] == [{-3.069, -3.962, -2.021}, {0.036, 1.975, 0.944}, {4.036, 5.975, 4.944}]:
    #pearl_(filepath)



