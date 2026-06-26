from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio
#from .pearl import *

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
    uvs2=[]

    vertices1=[]
    faces1=[]
    uvs1=[]

    vertices3=[]
    faces3=[]

    vertices3pt5a=[]
    faces3pt5a=[]
    
    vertices3pt4a=[]
    faces3pt4a=[]
    
    vertices3pt3a=[]
    faces3pt3a=[]
    
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
    
    fa1_=-1
    fb1_=0
    fc1_=1
    
    fa1pt2=-4
    fb1pt2=-3
    fc1pt2=-2
    fd1pt2=-1

    fa=-1
    fb=0
    fc=1

    uvs3=[]
    uvs3pt2=[]

    ii=1

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
                            Chunk_ = unpack("<H", f.read(2))[0]
                            if Chunk_ == 1:
                                f.seek(4,1)
                                uvcount = unpack("B", f.read(1))[0]
                                uvflag = unpack("B", f.read(1))[0]
                                if uvflag == 0x6D:
                                    if uvcount == 0:
                                        pass
                                    elif uvcount == 1:
                                        pass
                                    elif uvcount == 2:
                                        pass
                                    elif uvcount:
                                        for i in range(uvcount):
                                            uvx = unpack("<h", f.read(2))[0]/4096
                                            uvy = unpack("<h", f.read(2))[0]/4096
                                            f.seek(4,1)
                                            uvs1.append([uvx,-uvy])
                        
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
                            for j in range(1):
                                vx1 = unpack("<h", f.read(2))[0] / 4096
                                vy1 = unpack("<h", f.read(2))[0] / 4096
                                vz1 = unpack("<h", f.read(2))[0] / 4096
                                fn1 = unpack("<h", f.read(2))[0] / 4096
                                ux1 = unpack("<h", f.read(2))[0] / 4096
                                uy1 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vx2 = unpack("<h", f.read(2))[0] / 4096
                                vy2 = unpack("<h", f.read(2))[0] / 4096
                                vz2 = unpack("<h", f.read(2))[0] / 4096
                                fn2 = unpack("<h", f.read(2))[0] / 4096
                                ux2 = unpack("<h", f.read(2))[0] / 4096
                                uy2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vx3 = unpack("<h", f.read(2))[0] / 4096
                                vy3 = unpack("<h", f.read(2))[0] / 4096
                                vz3 = unpack("<h", f.read(2))[0] / 4096
                                fn3 = unpack("<h", f.read(2))[0] / 4096
                                ux3 = unpack("<h", f.read(2))[0] / 4096
                                uy3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2.append([vx1,vz1,vy1])
                                vertices2.append([vx2,vz2,vy2])
                                vertices2.append([vx3,vz3,vy3])
                                uvs2.append([ux1,-uy1])
                                uvs2.append([ux2,-uy2])
                                uvs2.append([ux3,-uy3])
                            f.seek(78,1)
                            facecount = unpack("B", f.read(1))[0]
                            flagsFace = unpack("B", f.read(1))[0]
                            if flagsFace == 0x6E:
                                if facecount == 1:
                                    id1 = unpack("B", f.read(1))[0]
                                    if id1 == 9:
                                        faceA = unpack("B", f.read(1))[0]&0x0F
                                        faceB = unpack("B", f.read(1))[0]&0x0F
                                        faceC = unpack("B", f.read(1))[0]&0x0F
                                        faceA//=3
                                        faceB//=3
                                        faceC//=3
                                        if faceA == 0 and faceB == 0 and faceC == 0:
                                            fa1+=1*3
                                            faces2.append([fa1,fa1,fa1])
                                        elif faceA == 1 and faceB == 1 and faceC == 1:
                                            fb1+=1*3
                                            faces2.append([fb1,fb1,fb1])
                                        elif faceA == 2 and faceB == 2 and faceC == 2:
                                            fc1+=1*3
                                            faces2.append([fc1,fc1,fc1])
                                        elif faceA == 0 and faceB == 1 and faceC == 1:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fb1,fb1])
                                        elif faceA == 1 and faceB == 1 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fb1,fb1])
                                        elif faceA == 0 and faceB == 1 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fb1,fa1])
                                        elif faceA == 0 and faceB == 2 and faceC == 0:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fc1,fa1])
                                        elif faceA == 1 and faceB == 0 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fb1,fb1])
                                        elif faceA == 2 and faceB == 0 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fc1,fa1,fb1])
                                        elif faceA == 2 and faceB == 2 and faceC == 0:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fc1,fc1])
                                        elif faceA == 0 and faceB == 2 and faceC == 2:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fc1,fc1])
                                        elif faceA == 0 and faceB == 0 and faceC == 1:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fa1,fb1])
                                        elif faceA == 0 and faceB == 0 and faceC == 2:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fa1,fc1])
                                        elif faceA == 1 and faceB == 2 and faceC == 2:
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fb1,fc1,fc1])
                                        elif faceA == 2 and faceB == 0 and faceC == 2:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fc1,fc1])
                                        elif faceA == 1 and faceB == 0 and faceC == 1:
                                            fa1+=1*3
                                            fb1+=1*3
                                            faces2.append([fa1,fb1,fb1])
                                        elif faceA == 1 and faceB == 2 and faceC == 1:
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fb1,fc1,fb1])
                                        elif faceA == 2 and faceB == 2 and faceC == 1:
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fc1,fc1,fb1])
                                        elif faceA == 2 and faceB == 2 and faceC == 0:
                                            fa1+=1*3
                                            fc1+=1*3
                                            faces2.append([fc1,fc1,fa1])
                                        elif faceA == 0 and faceB == 1 and faceC == 2:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                                        elif faceA == 2 and faceB == 0 and faceC == 1:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                                        elif faceA == 1 and faceB == 0 and faceC == 2:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                                        elif faceA == 1 and faceB == 2 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                                        elif faceA == 2 and faceB == 1 and faceC == 0:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                                        elif faceA == 0 and faceB == 2 and faceC == 1:
                                            fa1+=1*3
                                            fb1+=1*3
                                            fc1+=1*3
                                            faces2.append([fa1,fb1,fc1])
                        elif VertexCount == 4:
                            pass

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
                            for i in range(1):
                                f.seek(-128,1)
                            for i in range(1):
                                vx4_a_a = unpack("<f", f.read(4))[0];vy4_a_a = unpack("<f", f.read(4))[0];vz4_a_a = unpack("<f", f.read(4))[0];brightness4_a_a = unpack("<f", f.read(4))[0];uvx4_a_a = unpack("<f", f.read(4))[0];uvy4_a_a = unpack("<f", f.read(4))[0];unk4_a_a = unpack("<f", f.read(4))[0];faceon4_a_a = unpack("B", f.read(1))[0];valueon4_a_a = unpack("B", f.read(1))[0];nz4_a_a = unpack("<h", f.read(2))[0];vx5_a_a = unpack("<f", f.read(4))[0];vy5_a_a = unpack("<f", f.read(4))[0];vz5_a_a = unpack("<f", f.read(4))[0];brightness5_a_a = unpack("<f", f.read(4))[0];uvx5_a_a = unpack("<f", f.read(4))[0];uvy5_a_a = unpack("<f", f.read(4))[0];unk5_a_a = unpack("<f", f.read(4))[0];faceon5_a_a = unpack("B", f.read(1))[0];valueon5_a_a = unpack("B", f.read(1))[0];nz5_a_a = unpack("<h", f.read(2))[0];vx6_a_a = unpack("<f", f.read(4))[0];vy6_a_a = unpack("<f", f.read(4))[0];vz6_a_a = unpack("<f", f.read(4))[0];brightness6_a_a = unpack("<f", f.read(4))[0];uvx6_a_a = unpack("<f", f.read(4))[0];uvy6_a_a = unpack("<f", f.read(4))[0];unk6_a_a = unpack("<f", f.read(4))[0];faceon6_a_a = unpack("B", f.read(1))[0];valueon6_a_a = unpack("B", f.read(1))[0];nz6_a_a = unpack("<h", f.read(2))[0];vx7_a_a = unpack("<f", f.read(4))[0];vy7_a_a = unpack("<f", f.read(4))[0];vz7_a_a = unpack("<f", f.read(4))[0];brightness7_a_a = unpack("<f", f.read(4))[0];uvx7_a_a = unpack("<f", f.read(4))[0];uvy7_a_a = unpack("<f", f.read(4))[0];unk7_a_a = unpack("<f", f.read(4))[0];faceon7_a_a = unpack("B", f.read(1))[0];valueon7_a_a = unpack("B", f.read(1))[0];nz7_a_a = unpack("<h", f.read(2))[0]
                            for i in range(1):
                                f.seek(-128,1)
                            for i in range(1):
                                vx4_a_a_ = unpack("<f", f.read(4))[0];vy4_a_a_ = unpack("<f", f.read(4))[0];vz4_a_a_ = unpack("<f", f.read(4))[0];brightness4_a_a_ = unpack("<f", f.read(4))[0];uvx4_a_a_ = unpack("<f", f.read(4))[0];uvy4_a_a_ = unpack("<f", f.read(4))[0];unk4_a_a_ = unpack("<f", f.read(4))[0];faceon4_a_a_ = unpack("B", f.read(1))[0];valueon4_a_a_ = unpack("B", f.read(1))[0];nz4_a_a_ = unpack("<h", f.read(2))[0];vx5_a_a_ = unpack("<f", f.read(4))[0];vy5_a_a_ = unpack("<f", f.read(4))[0];vz5_a_a_ = unpack("<f", f.read(4))[0];brightness5_a_a_ = unpack("<f", f.read(4))[0];uvx5_a_a_ = unpack("<f", f.read(4))[0];uvy5_a_a_ = unpack("<f", f.read(4))[0];unk5_a_a_ = unpack("<f", f.read(4))[0];faceon5_a_a_ = unpack("B", f.read(1))[0];valueon5_a_a_ = unpack("B", f.read(1))[0];nz5_a_a_ = unpack("<h", f.read(2))[0];vx6_a_a_ = unpack("<f", f.read(4))[0];vy6_a_a_ = unpack("<f", f.read(4))[0];vz6_a_a_ = unpack("<f", f.read(4))[0];brightness6_a_a_ = unpack("<f", f.read(4))[0];uvx6_a_a_ = unpack("<f", f.read(4))[0];uvy6_a_a_ = unpack("<f", f.read(4))[0];unk6_a_a_ = unpack("<f", f.read(4))[0];faceon6_a_a_ = unpack("B", f.read(1))[0];valueon6_a_a_ = unpack("B", f.read(1))[0];nz6_a_a_ = unpack("<h", f.read(2))[0];vx7_a_a_ = unpack("<f", f.read(4))[0];vy7_a_a_ = unpack("<f", f.read(4))[0];vz7_a_a_ = unpack("<f", f.read(4))[0];brightness7_a_a_ = unpack("<f", f.read(4))[0];uvx7_a_a_ = unpack("<f", f.read(4))[0];uvy7_a_a_ = unpack("<f", f.read(4))[0];unk7_a_a_ = unpack("<f", f.read(4))[0];faceon7_a_a_ = unpack("B", f.read(1))[0];valueon7_a_a_ = unpack("B", f.read(1))[0];nz7_a_a_ = unpack("<h", f.read(2))[0]
                            for i in range(1):
                                f.seek(-128,1)
                            for i in range(1):
                                vx4_a_a_a = unpack("<f", f.read(4))[0];vy4_a_a_a = unpack("<f", f.read(4))[0];;vz4_a_a_a = unpack("<f", f.read(4))[0];;brightness4_a_a_a = unpack("<f", f.read(4))[0];uvx4_a_a_a = unpack("<f", f.read(4))[0];uvy4_a_a_a = unpack("<f", f.read(4))[0];unk4_a_a_a = unpack("<f", f.read(4))[0];faceon4_a_a_a = unpack("B", f.read(1))[0];valueon4_a_a_a = unpack("B", f.read(1))[0];nz4_a_a_ = unpack("<h", f.read(2))[0];vx5_a_a_a = unpack("<f", f.read(4))[0];vy5_a_a_a = unpack("<f", f.read(4))[0];vz5_a_a_ = unpack("<f", f.read(4))[0];brightness5_a_a_a = unpack("<f", f.read(4))[0];uvx5_a_a_a = unpack("<f", f.read(4))[0];uvy5_a_a_a = unpack("<f", f.read(4))[0];unk5_a_a_a = unpack("<f", f.read(4))[0];faceon5_a_a_a = unpack("B", f.read(1))[0];valueon5_a_a_a = unpack("B", f.read(1))[0];nz5_a_a_a = unpack("<h", f.read(2))[0];vx6_a_a_a = unpack("<f", f.read(4))[0];vy6_a_a_a = unpack("<f", f.read(4))[0];vz6_a_a_a = unpack("<f", f.read(4))[0];brightness6_a_a_a = unpack("<f", f.read(4))[0];uvx6_a_a_a = unpack("<f", f.read(4))[0];uvy6_a_a_a = unpack("<f", f.read(4))[0];unk6_a_a_a = unpack("<f", f.read(4))[0];faceon6_a_a_a = unpack("B", f.read(1))[0];valueon6_a_a_a = unpack("B", f.read(1))[0];nz6_a_a_a = unpack("<h", f.read(2))[0];vx7_a_a_a = unpack("<f", f.read(4))[0];vy7_a_a_a = unpack("<f", f.read(4))[0];vz7_a_a_a = unpack("<f", f.read(4))[0];brightness7_a_a_a = unpack("<f", f.read(4))[0];uvx7_a_a_a = unpack("<f", f.read(4))[0];uvy7_a_a_a = unpack("<f", f.read(4))[0];faceon7_a_a_a = unpack("B", f.read(1))[0];valueon7_a_a_a = unpack("B", f.read(1))[0];nz7_a_a_a = unpack("<h", f.read(2))[0]
                            offset2 = unpack("<I", f.read(4))[0]
                            f.seek(-4,1)
                            offset3 = unpack("<I", f.read(4))[0]
                            if offset3 == 1627553811:
                                offset3a = unpack("<I", f.read(4))[0]
                                if offset3a == 65540:
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
                                                            for i in range(1):
                                                                vx4_offbb = unpack("<f", f.read(4))[0];vy4_offbb = unpack("<f", f.read(4))[0];vz4_offbb = unpack("<f", f.read(4))[0];face_offbb = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb = unpack("<f", f.read(4))[0];uvy4_offbb = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb1 = unpack("<f", f.read(4))[0];vy4_offbb1 = unpack("<f", f.read(4))[0];vz4_offbb1 = unpack("<f", f.read(4))[0];face_offbb1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb1 = unpack("<f", f.read(4))[0];uvy4_offbb1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb2 = unpack("<f", f.read(4))[0];vy4_offbb2 = unpack("<f", f.read(4))[0];vz4_offbb2 = unpack("<f", f.read(4))[0];face_offbb2 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb2 = unpack("<f", f.read(4))[0];uvy4_offbb2 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb3 = unpack("<f", f.read(4))[0];vy4_offbb3 = unpack("<f", f.read(4))[0];vz4_offbb3 = unpack("<f", f.read(4))[0];face_offbb3 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb3 = unpack("<f", f.read(4))[0];uvy4_offbb3 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb4 = unpack("<f", f.read(4))[0];vy4_offbb4 = unpack("<f", f.read(4))[0];vz4_offbb4 = unpack("<f", f.read(4))[0];face_offbb4 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb4 = unpack("<f", f.read(4))[0];uvy4_offbb4 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb5 = unpack("<f", f.read(4))[0];vy4_offbb5 = unpack("<f", f.read(4))[0];vz4_offbb5 = unpack("<f", f.read(4))[0];face_offbb5 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb5 = unpack("<f", f.read(4))[0];uvy4_offbb5 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb6 = unpack("<f", f.read(4))[0];vy4_offbb6 = unpack("<f", f.read(4))[0];vz4_offbb6 = unpack("<f", f.read(4))[0];face_offbb6 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb6 = unpack("<f", f.read(4))[0];uvy4_offbb6 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb7 = unpack("<f", f.read(4))[0];vy4_offbb7 = unpack("<f", f.read(4))[0];vz4_offbb7 = unpack("<f", f.read(4))[0];face_offbb7 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb7 = unpack("<f", f.read(4))[0];uvy4_offbb7 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb8 = unpack("<f", f.read(4))[0];vy4_offbb8 = unpack("<f", f.read(4))[0];vz4_offbb8 = unpack("<f", f.read(4))[0];face_offbb8 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb8 = unpack("<f", f.read(4))[0];uvy4_offbb8 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb9 = unpack("<f", f.read(4))[0];vy4_offbb9 = unpack("<f", f.read(4))[0];vz4_offbb9 = unpack("<f", f.read(4))[0];face_offbb9 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb9 = unpack("<f", f.read(4))[0];uvy4_offbb9 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb10 = unpack("<f", f.read(4))[0];vy4_offbb10 = unpack("<f", f.read(4))[0];vz4_offbb10 = unpack("<f", f.read(4))[0];face_offbb10 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb10 = unpack("<f", f.read(4))[0];uvy4_offbb10 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offbb11 = unpack("<f", f.read(4))[0];vy4_offbb11 = unpack("<f", f.read(4))[0];vz4_offbb11 = unpack("<f", f.read(4))[0];face_offbb11 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offbb11 = unpack("<f", f.read(4))[0];uvy4_offbb11 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                            offset4d = unpack("<I", f.read(4))[0]
                                                            if offset4d == 1627553871:
                                                                offset4e = unpack("<I", f.read(4))[0]
                                                                if offset4e == 11:
                                                                    offset4f = unpack("<I", f.read(4))[0]
                                                                    if offset4f == 1627553875:
                                                                        offset4g = unpack("<I", f.read(4))[0]
                                                                        if offset4g == 13:
                                                                            f.seek(2,1)
                                                                            vertexCount4g = unpack("B", f.read(1))[0]//2
                                                                            flag4g = unpack("B", f.read(1))[0]
                                                                            if flag4g == 0x6C:
                                                                                if vertexCount4g == 9:
                                                                                    for i in range(1):
                                                                                        vx4_offcc = unpack("<f", f.read(4))[0];vy4_offcc = unpack("<f", f.read(4))[0];vz4_offcc = unpack("<f", f.read(4))[0];face_offcc = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc = unpack("<f", f.read(4))[0];uvy4_offcc = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc2 = unpack("<f", f.read(4))[0];vy4_offcc2 = unpack("<f", f.read(4))[0];vz4_offcc2 = unpack("<f", f.read(4))[0];face_offcc2 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc2 = unpack("<f", f.read(4))[0];uvy4_offcc2 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc3 = unpack("<f", f.read(4))[0];vy4_offcc3 = unpack("<f", f.read(4))[0];vz4_offcc3 = unpack("<f", f.read(4))[0];face_offcc3 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc3 = unpack("<f", f.read(4))[0];uvy4_offcc3 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc4 = unpack("<f", f.read(4))[0];vy4_offcc4 = unpack("<f", f.read(4))[0];vz4_offcc4 = unpack("<f", f.read(4))[0];face_offcc4 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc4 = unpack("<f", f.read(4))[0];uvy4_offcc4 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc5 = unpack("<f", f.read(4))[0];vy4_offcc5 = unpack("<f", f.read(4))[0];vz4_offcc5 = unpack("<f", f.read(4))[0];face_offcc5 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc5 = unpack("<f", f.read(4))[0];uvy4_offcc5 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc6 = unpack("<f", f.read(4))[0];vy4_offcc6 = unpack("<f", f.read(4))[0];vz4_offcc6 = unpack("<f", f.read(4))[0];face_offcc6 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc6 = unpack("<f", f.read(4))[0];uvy4_offcc6 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc7 = unpack("<f", f.read(4))[0];vy4_offcc7 = unpack("<f", f.read(4))[0];vz4_offcc7 = unpack("<f", f.read(4))[0];face_offcc7 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc7 = unpack("<f", f.read(4))[0];uvy4_offcc7 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc8 = unpack("<f", f.read(4))[0];vy4_offcc8 = unpack("<f", f.read(4))[0];vz4_offcc8 = unpack("<f", f.read(4))[0];face_offcc8 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc8 = unpack("<f", f.read(4))[0];uvy4_offcc8 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offcc9 = unpack("<f", f.read(4))[0];vy4_offcc9 = unpack("<f", f.read(4))[0];vz4_offcc9 = unpack("<f", f.read(4))[0];face_offcc9 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offcc9 = unpack("<f", f.read(4))[0];uvy4_offcc9 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                    offset4h = unpack("<I", f.read(4))[0]
                                                                                    if offset4h == 16777473:
                                                                                        if faceon4_a_ == 1:
                                                                                            if faceon5_a_ == 1:
                                                                                                if faceon6_a_ == 0:
                                                                                                    if faceon7_a_ == 0:
                                                                                                        if face_offaa == 0:
                                                                                                            if face_offbb == 0:
                                                                                                                if face_offbb1 == 0:
                                                                                                                    if face_offbb2 == 0:
                                                                                                                        if face_offbb3 == 0:
                                                                                                                            if face_offbb4 == 0:
                                                                                                                                if face_offbb5 == 0:
                                                                                                                                    if face_offbb6 == 0:
                                                                                                                                        if face_offbb7 == 0:
                                                                                                                                            if face_offbb8 == 0:
                                                                                                                                                if face_offbb9 == 0:
                                                                                                                                                    if face_offbb10 == 0:
                                                                                                                                                        if face_offbb11 == 0:
                                                                                                                                                            if face_offcc == 0:
                                                                                                                                                                if face_offcc2 == 0:
                                                                                                                                                                    if face_offcc3 == 0:
                                                                                                                                                                        if face_offcc4 == 0:
                                                                                                                                                                            if face_offcc5 == 0:
                                                                                                                                                                                if face_offcc6 == 0:
                                                                                                                                                                                    if face_offcc7 == 0:
                                                                                                                                                                                        if face_offcc8 == 0:
                                                                                                                                                                                            if face_offcc9 == 0:
                                                                                                                                                                                                vertices3pt3a.append([vx4_a_,vz4_a_,vy4_a_])
                                                                                                                                                                                                vertices3pt3a.append([vx5_a_,vz5_a_,vy5_a_])
                                                                                                                                                                                                vertices3pt3a.append([vx6_a_,vz6_a_,vy6_a_])
                                                                                                                                                                                                vertices3pt3a.append([vx7_a_,vz7_a_,vy7_a_])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offaa,vz4_offaa,vy4_offaa])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb,vz4_offbb,vy4_offbb])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb1,vz4_offbb1,vy4_offbb1])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb2,vz4_offbb2,vy4_offbb2])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb3,vz4_offbb3,vy4_offbb3])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb4,vz4_offbb4,vy4_offbb4])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb5,vz4_offbb5,vy4_offbb5])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb6,vz4_offbb6,vy4_offbb6])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb7,vz4_offbb7,vy4_offbb7])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb8,vz4_offbb8,vy4_offbb8])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb9,vz4_offbb9,vy4_offbb9])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb10,vz4_offbb10,vy4_offbb10])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offbb11,vz4_offbb11,vy4_offbb11])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc,vz4_offcc,vy4_offcc])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc2,vz4_offcc2,vy4_offcc2])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc3,vz4_offcc3,vy4_offcc3])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc4,vz4_offcc4,vy4_offcc4])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc5,vz4_offcc5,vy4_offcc5])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc6,vz4_offcc6,vy4_offcc6])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc7,vz4_offcc7,vy4_offcc7])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc8,vz4_offcc8,vy4_offcc8])
                                                                                                                                                                                                vertices3pt3a.append([vx4_offcc9,vz4_offcc9,vy4_offcc9])
                                                                                                                                                                                                faces3pt3a.append([0,1,2])
                                                                                                                                                                                                faces3pt3a.append([1,2,3])
                                                                                                                                                                                                faces3pt3a.append([1,3,4])
                                                                                                                                                                                                faces3pt3a.append([1,4,5])
                                                                                                                                                                                                faces3pt3a.append([1,5,6])
                                                                                                                                                                                                faces3pt3a.append([1,6,11])
                                                                                                                                                                                                faces3pt3a.append([1,11,9])
                                                                                                                                                                                                faces3pt3a.append([0,1,9])
                                                                                                                                                                                                faces3pt3a.append([0,9,10])
                                                                                                                                                                                                faces3pt3a.append([6,11,12])
                                                                                                                                                                                                faces3pt3a.append([6,12,17])
                                                                                                                                                                                                faces3pt3a.append([7,8,10])
                                                                                                                                                                                                faces3pt3a.append([7,9,10])
                                                                                                                                                                                                faces3pt3a.append([7,9,13])
                                                                                                                                                                                                faces3pt3a.append([9,11,13])
                                                                                                                                                                                                faces3pt3a.append([11,12,13])
                                                                                                                                                                                                faces3pt3a.append([12,13,14])
                                                                                                                                                                                                faces3pt3a.append([12,14,17])
                                                                                                                                                                                                faces3pt3a.append([14,17,18])
                                                                                                                                                                                                faces3pt3a.append([17,18,19])
                                                                                                                                                                                                faces3pt3a.append([20,21,22])
                                                                                                                                                                                                faces3pt3a.append([15,21,25])
                                                                                                                                                                                                faces3pt3a.append([15,21,25])
                                                                                                                                                                                                faces3pt3a.append([15,21,22])
                                                                                                                                                                                                faces3pt3a.append([25,15,24])
                                elif offset3a == 65538:
                                    offset3b = unpack("<I", f.read(4))[0]
                                    if offset3b == 1812103191:
                                        for i in range(1):
                                            vx4_offdd = unpack("<f", f.read(4))[0];vy4_offdd = unpack("<f", f.read(4))[0];vz4_offdd = unpack("<f", f.read(4))[0];face_offdd1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offdd1 = unpack("<f", f.read(4))[0];uvy4_offdd1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offdd_ = unpack("<f", f.read(4))[0];vy4_offdd_ = unpack("<f", f.read(4))[0];vz4_offdd_ = unpack("<f", f.read(4))[0];face_offdd = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offdd = unpack("<f", f.read(4))[0];uvy4_offdd = unpack("<f", f.read(4))[0];f.seek(8,1)
                                        offset3a_ = unpack("<I", f.read(4))[0]
                                        if offset3a_ != 1627553819:
                                            f.seek(-36,1)
                                            offset3a__ = unpack("<I", f.read(4))[0]
                                            if offset3a__ == 1627553819:
                                                
                                                offset3b_ = unpack("<I", f.read(4))[0]
                                                if offset3b_ == 4:
                                                    f.seek(2,1)
                                                    vertexCount3b_ = unpack("B", f.read(1))[0]//2
                                                    flag3b_ = unpack("B", f.read(1))[0]
                                                    if flag3b_ == 0x6C:
                                                        if vertexCount3b_ == 3:
                                                            for i in range(1):
                                                                vx4_offee = unpack("<f", f.read(4))[0];vy4_offee = unpack("<f", f.read(4))[0];vz4_offee = unpack("<f", f.read(4))[0];face_offee1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offee1 = unpack("<f", f.read(4))[0];uvy4_offee1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offee_ = unpack("<f", f.read(4))[0];vy4_offee_ = unpack("<f", f.read(4))[0];vz4_offee_ = unpack("<f", f.read(4))[0];face_offee = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offee = unpack("<f", f.read(4))[0];uvy4_offee = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offff = unpack("<f", f.read(4))[0];vy4_offff = unpack("<f", f.read(4))[0];vz4_offff = unpack("<f", f.read(4))[0];face_offff1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offff1 = unpack("<f", f.read(4))[0];uvy4_offff1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                            offset3c_a = unpack("<I", f.read(4))[0]
                                                            if offset3c_a == 1627553835:
                                                                offset3c_ = unpack("<I", f.read(4))[0]
                                                                if offset3c_ == 65542:
                                                                    
                                                                    f.seek(2,1)
                                                                    vertexCount3d_ = unpack("B", f.read(1))[0]//2
                                                                    flag3d_ = unpack("B", f.read(1))[0]
                                                                    if flag3d_ == 0x6C:
                                                                        if vertexCount3d_ == 1:
                                                                            for i in range(1):
                                                                                vx4_offhh = unpack("<f", f.read(4))[0];vy4_offhh = unpack("<f", f.read(4))[0];vz4_offhh = unpack("<f", f.read(4))[0];face_offhh1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offhh1 = unpack("<f", f.read(4))[0];uvy4_offhh1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                            offset3c_b = unpack("<I", f.read(4))[0]
                                                                            if offset3c_b == 1627553843:
                                                                                
                                                                                offset3d_ = unpack("<I", f.read(4))[0]
                                                                                if offset3d_ == 8:
                                                                                    f.seek(2,1)
                                                                                    vertexCount3d_ = unpack("B", f.read(1))[0]//2
                                                                                    flag3d_ = unpack("B", f.read(1))[0]
                                                                                    if flag3d_ == 0x6C:
                                                                                        if vertexCount3d_ == 1:
                                                                                            for i in range(1):
                                                                                                vx4_offhha = unpack("<f", f.read(4))[0];vy4_offhha = unpack("<f", f.read(4))[0];vz4_offhha = unpack("<f", f.read(4))[0];face_offhh1a = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offhh1 = unpack("<f", f.read(4))[0];uvy4_offhh1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                            offset3d_a = unpack("<I", f.read(4))[0]
                                                                                            if offset3d_a == 1627553851:
                                                                                                offset3d_aaa = unpack("<I", f.read(4))[0]
                                                                                                if offset3d_aaa == 65548:
                                                                                                    f.seek(2,1)
                                                                                                    vertexCount3e_ = unpack("B", f.read(1))[0]//2
                                                                                                    flag3e_ = unpack("B", f.read(1))[0]
                                                                                                    if flag3e_ == 0x6C:
                                                                                                        if vertexCount3e_ == 1:
                                                                                                            for i in range(1):
                                                                                                                vx4_offii = unpack("<f", f.read(4))[0];vy4_offii = unpack("<f", f.read(4))[0];vz4_offii = unpack("<f", f.read(4))[0];face_offii1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offii1 = unpack("<f", f.read(4))[0];uvy4_offii1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                            offset3f_ = unpack("<I", f.read(4))[0]
                                                                                                            if offset3f_ == 1627553859:
                                                                                                                offset3f_aa = unpack("<I", f.read(4))[0]
                                                                                                                if offset3f_aa == 14:
                                                                                                                    f.seek(2,1)
                                                                                                                    vertexCount3i_ = unpack("B", f.read(1))[0]//2
                                                                                                                    flag3i_ = unpack("B", f.read(1))[0]
                                                                                                                    if flag3i_ == 0x6C:
                                                                                                                        if vertexCount3i_ == 3:
                                                                                                                            for i in range(1):
                                                                                                                                vx4_offkk = unpack("<f", f.read(4))[0];vy4_offkk = unpack("<f", f.read(4))[0];vz4_offkk = unpack("<f", f.read(4))[0];face_offkk1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offkk1 = unpack("<f", f.read(4))[0];uvy4_offkk1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offkk_ = unpack("<f", f.read(4))[0];vy4_offkk_ = unpack("<f", f.read(4))[0];vz4_offkk_ = unpack("<f", f.read(4))[0];face_offkk = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offkk = unpack("<f", f.read(4))[0];uvy4_offkk = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offll = unpack("<f", f.read(4))[0];vy4_offll = unpack("<f", f.read(4))[0];vz4_offll = unpack("<f", f.read(4))[0];face_offll1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offll1 = unpack("<f", f.read(4))[0];uvy4_offll1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                                            offset3k_ = unpack("<I", f.read(4))[0]
                                                                                                                            print(f.tell())
                                                                                                                            if offset3k_ == 1627553875:
                                                                                                                                offset3l_ = unpack("<I", f.read(4))[0]
                                                                                                                                if offset3l_ == 65556:
                                                                                                                                    offset3m_ = unpack("<I", f.read(4))[0]
                                                                                                                                    if offset3m_ == 1627553879:
                                                                                                                                        offset3n_ = unpack("<I", f.read(4))[0]
                                                                                                                                        if offset3n_ == 65554:
                                                                                                                                            f.seek(2,1)
                                                                                                                                            vertexCount3m_ = unpack("B", f.read(1))[0]//2
                                                                                                                                            flag3m_ = unpack("B", f.read(1))[0]
                                                                                                                                            if flag3m_ == 0x6C:
                                                                                                                                                if vertexCount3m_ == 2:
                                                                                                                                                    for i in range(1):
                                                                                                                                                        vx4_offnn = unpack("<f", f.read(4))[0];vy4_offnn = unpack("<f", f.read(4))[0];vz4_offnn = unpack("<f", f.read(4))[0];face_offnn1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offnn1 = unpack("<f", f.read(4))[0];uvy4_offnn1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offnn_ = unpack("<f", f.read(4))[0];vy4_offnn_ = unpack("<f", f.read(4))[0];vz4_offnn_ = unpack("<f", f.read(4))[0];face_offnn = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offnn = unpack("<f", f.read(4))[0];uvy4_offnn = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                                                                    offset3n_ = unpack("<I", f.read(4))[0]
                                                                                                                                                    if offset3n_ == 16777473:
                                                                                                                                                        if faceon4_a_a == 1:
                                                                                                                                                            if faceon5_a_a == 1:
                                                                                                                                                                if faceon6_a_a == 0:
                                                                                                                                                                    if faceon7_a_a == 0:
                                                                                                                                                                        if face_offdd1 == 0:
                                                                                                                                                                            if face_offee1 == 0:
                                                                                                                                                                                if face_offee1 == 0:
                                                                                                                                                                                    if face_offee == 0:
                                                                                                                                                                                        if face_offff1 == 0:
                                                                                                                                                                                            if face_offhh1 == 0:
                                                                                                                                                                                                if face_offhh1a == 0:
                                                                                                                                                                                                    if face_offii1 == 0:
                                                                                                                                                                                                        if face_offkk1 == 0:
                                                                                                                                                                                                            if face_offkk == 0:
                                                                                                                                                                                                                if face_offll1 == 0:
                                                                                                                                                                                                                    if face_offnn1 == 0:
                                                                                                                                                                                                                        if face_offnn == 0:
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_a_a,vz4_a_a,vy4_a_a])
                                                                                                                                                                                                                            vertices3pt4a.append([vx5_a_a,vz5_a_a,vy5_a_a])
                                                                                                                                                                                                                            vertices3pt4a.append([vx6_a_a,vz6_a_a,vy6_a_a])
                                                                                                                                                                                                                            vertices3pt4a.append([vx7_a_a,vz7_a_a,vy7_a_a])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offdd,vz4_offdd,vy4_offdd])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offee,vz4_offee,vy4_offee])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offee_,vz4_offee_,vy4_offee_])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offff,vz4_offff,vy4_offff])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offhh,vz4_offhh,vy4_offhh])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offhha,vz4_offhha,vy4_offhha])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offii,vz4_offii,vy4_offii])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offkk,vz4_offkk,vy4_offkk])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offkk_,vz4_offkk_,vy4_offkk_])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offll,vz4_offll,vy4_offll])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offnn,vz4_offnn,vy4_offnn])
                                                                                                                                                                                                                            vertices3pt4a.append([vx4_offnn_,vz4_offnn_,vy4_offnn_])
                                                                                                                                                                                                                            faces3pt4a.append([0,1,2])
                                                                                                                                                                                                                            faces3pt4a.append([1,2,3])
                                                                                                                                                                                                                            faces3pt4a.append([1,3,4])
                                                                                                                                                                                                                            faces3pt4a.append([3,4,5])
                                                                                                                                                                                                                            faces3pt4a.append([3,5,6])
                                                                                                                                                                                                                            faces3pt4a.append([4,5,8])
                                                                                                                                                                                                                            faces3pt4a.append([5,6,7])
                                                                                                                                                                                                                            faces3pt4a.append([5,8,9])
                                                                                                                                                                                                                            faces3pt4a.append([5,7,9])
                                                                                                                                                                                                                            faces3pt4a.append([7,9,12])
                                                                                                                                                                                                                            faces3pt4a.append([8,9,10])
                                                                                                                                                                                                                            faces3pt4a.append([9,10,11])
                                                                                                                                                                                                                            faces3pt4a.append([9,11,12])
                                                                                                                                                                                                                            faces3pt4a.append([11,12,13])
                                                                                                                                                                                                                            faces3pt4a.append([11,13,15])
                                                                                                                                                                                                                            faces3pt4a.append([13,14,15])
                                                                elif offset3c_ != 65542:
                                                                    f.seek(-152,1)
                                                                    f.seek(2,1)
                                                                    vertexCount3bbb3 = unpack("B", f.read(1))[0]//2
                                                                    flag3bbb3 = unpack("B", f.read(1))[0]
                                                                    if flag3bbb3 == 0x6C:
                                                                        if vertexCount3bbb3 == 1:
                                                                            for i in range(1):
                                                                                vx4_offu = unpack("<f", f.read(4))[0];vy4_offu = unpack("<f", f.read(4))[0];vz4_offu = unpack("<f", f.read(4))[0];face_offu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offu = unpack("<f", f.read(4))[0];uvy4_offu1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                            offset3bbb4a = unpack("<I", f.read(4))[0]
                                                                            if offset3bbb4a == 1627553819:
                                                                                offset3bbb4ab = unpack("<I", f.read(4))[0]
                                                                                if offset3bbb4ab == 4:
                                                                                    f.seek(2,1)
                                                                                    vertexCount3bbb4 = unpack("B", f.read(1))[0]//2
                                                                                    flag3bbb4 = unpack("B", f.read(1))[0]
                                                                                    if flag3bbb4 == 0x6C:
                                                                                        if vertexCount3bbb4 == 3:
                                                                                            for i in range(1):
                                                                                                vx4_offu_ = unpack("<f", f.read(4))[0];vy4_offu_ = unpack("<f", f.read(4))[0];vz4_offu_ = unpack("<f", f.read(4))[0];face_offu_1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offu_ = unpack("<f", f.read(4))[0];uvy4_offu_1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuu = unpack("<f", f.read(4))[0];vy4_offuu = unpack("<f", f.read(4))[0];vz4_offuu = unpack("<f", f.read(4))[0];face_offuu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuu = unpack("<f", f.read(4))[0];uvy4_offuu1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuu = unpack("<f", f.read(4))[0];vy4_offuuu = unpack("<f", f.read(4))[0];vz4_offuuu = unpack("<f", f.read(4))[0];face_offuuu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuu = unpack("<f", f.read(4))[0];uvy4_offuuu1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                            offset3bbb4aa = unpack("<I", f.read(4))[0]
                                                                                            if offset3bbb4aa == 1627553835:
                                                                                                offset3bbb4aaa = unpack("<I", f.read(4))[0]
                                                                                                if offset3bbb4aaa == 8:
                                                                                                    offset3bbb4aaaa = unpack("<I", f.read(4))[0]
                                                                                                    if offset3bbb4aaaa == 1627553839:
                                                                                                        offset3bbb4 = unpack("<I", f.read(4))[0]
                                                                                                        if offset3bbb4 == 6:
                                                                                                            offset3bbb5 = unpack("<I", f.read(4))[0]
                                                                                                            if offset3bbb5 == 1627553843:
                                                                                                                offset3bbb6 = unpack("<I", f.read(4))[0]
                                                                                                                if offset3bbb6 == 65537:
                                                                                                                    f.seek(2,1)
                                                                                                                    vertexCount3bbb6 = unpack("B", f.read(1))[0]//2
                                                                                                                    flag3bbb6 = unpack("B", f.read(1))[0]
                                                                                                                    if flag3bbb6 == 0x6C:
                                                                                                                        if vertexCount3bbb6 == 13:
                                                                                                                            for i in range(1):
                                                                                                                                vx4_offuuuu = unpack("<f", f.read(4))[0];vy4_offuuuu = unpack("<f", f.read(4))[0];vz4_offuuuu = unpack("<f", f.read(4))[0];face_offuuuu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuu1 = unpack("<f", f.read(4))[0];uvy4_offuuuu1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuu_ = unpack("<f", f.read(4))[0];vy4_offuuuu_ = unpack("<f", f.read(4))[0];vz4_offuuuu_ = unpack("<f", f.read(4))[0];face_offuuuu = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuu = unpack("<f", f.read(4))[0];uvy4_offuuuu = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuu = unpack("<f", f.read(4))[0];vy4_offuuuuu = unpack("<f", f.read(4))[0];vz4_offuuuuu = unpack("<f", f.read(4))[0];face_offuuuuu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuu1 = unpack("<f", f.read(4))[0];uvy4_offuuuuu1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuu_ = unpack("<f", f.read(4))[0];vy4_offuuuuu_ = unpack("<f", f.read(4))[0];vz4_offuuuuu_ = unpack("<f", f.read(4))[0];face_offuuuuu = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuu = unpack("<f", f.read(4))[0];uvy4_offuuuuu = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuu = unpack("<f", f.read(4))[0];vy4_offuuuuuu = unpack("<f", f.read(4))[0];vz4_offuuuuuu = unpack("<f", f.read(4))[0];face_offuuuuuu1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuu1 = unpack("<f", f.read(4))[0];uvy4_offuuuuuu1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuu_ = unpack("<f", f.read(4))[0];vy4_offuuuuuu_ = unpack("<f", f.read(4))[0];vz4_offuuuuuu_ = unpack("<f", f.read(4))[0];face_offuuuuuu = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuu = unpack("<f", f.read(4))[0];uvy4_offuuuuuu = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuum = unpack("<f", f.read(4))[0];vy4_offuuuuuum = unpack("<f", f.read(4))[0];vz4_offuuuuuum = unpack("<f", f.read(4))[0];face_offuuuuuum1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuum1 = unpack("<f", f.read(4))[0];uvy4_offuuuuuum1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuum_ = unpack("<f", f.read(4))[0];vy4_offuuuuuum_ = unpack("<f", f.read(4))[0];vz4_offuuuuuum_ = unpack("<f", f.read(4))[0];face_offuuuuuum = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuum = unpack("<f", f.read(4))[0];uvy4_offuuuuuum = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuumm = unpack("<f", f.read(4))[0];vy4_offuuuuuumm = unpack("<f", f.read(4))[0];vz4_offuuuuuumm = unpack("<f", f.read(4))[0];face_offuuuuuumm1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuumm1 = unpack("<f", f.read(4))[0];uvy4_offuuuuuumm1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuumm_ = unpack("<f", f.read(4))[0];vy4_offuuuuuumm_ = unpack("<f", f.read(4))[0];vz4_offuuuuuumm_ = unpack("<f", f.read(4))[0];face_offuuuuuumm = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuumm = unpack("<f", f.read(4))[0];uvy4_offuuuuuumm = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuummm = unpack("<f", f.read(4))[0];vy4_offuuuuuummm = unpack("<f", f.read(4))[0];vz4_offuuuuuummm = unpack("<f", f.read(4))[0];face_offuuuuuummm1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuummm1 = unpack("<f", f.read(4))[0];uvy4_offuuuuuummm1 = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuummm_ = unpack("<f", f.read(4))[0];vy4_offuuuuuummm_ = unpack("<f", f.read(4))[0];vz4_offuuuuuummm_ = unpack("<f", f.read(4))[0];face_offuuuuuummm = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuummm = unpack("<f", f.read(4))[0];uvy4_offuuuuuummm = unpack("<f", f.read(4))[0];f.seek(8,1);vx4_offuuuuuummmm = unpack("<f", f.read(4))[0];vy4_offuuuuuummmm = unpack("<f", f.read(4))[0];vz4_offuuuuuummmm = unpack("<f", f.read(4))[0];face_offuuuuuummmm1 = unpack("B", f.read(1))[0];f.seek(3,1);uvx4_offuuuuuummmm1 = unpack("<f", f.read(4))[0];uvy4_offuuuuuummmm1 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                                                                                                            offset3bbb7 = unpack("<I", f.read(4))[0]
                                                                                                                            if offset3bbb7 == 16777473:
                                                                                                                                if faceon4_a_a_ == 1:
                                                                                                                                    if faceon5_a_a_ == 1:
                                                                                                                                        if faceon6_a_a_ == 0:
                                                                                                                                            if faceon7_a_a_ == 0:
                                                                                                                                                if face_offu1 == 0:
                                                                                                                                                    if face_offu_1 == 0:
                                                                                                                                                        if face_offuu1 == 0:
                                                                                                                                                            if face_offuuu1 == 0:
                                                                                                                                                                if face_offuuuu1 == 0:
                                                                                                                                                                    if face_offuuuu == 0:
                                                                                                                                                                        if face_offuuuuu1 == 0:
                                                                                                                                                                            if face_offuuuuu == 0:
                                                                                                                                                                                if face_offuuuuuu1 == 0:
                                                                                                                                                                                    if face_offuuuuuu == 0:
                                                                                                                                                                                        if face_offuuuuuum1 == 0:
                                                                                                                                                                                            if face_offuuuuuum == 0:
                                                                                                                                                                                                if face_offuuuuuumm1 == 0:
                                                                                                                                                                                                    if face_offuuuuuumm == 0:
                                                                                                                                                                                                        if face_offuuuuuummm1 == 0:
                                                                                                                                                                                                            if face_offuuuuuummm == 0:
                                                                                                                                                                                                                if face_offuuuuuummmm1 == 0:
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_a_a_,vz4_a_a_,vy4_a_a_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx5_a_a_,vz5_a_a_,vy5_a_a_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx6_a_a_,vz6_a_a_,vy6_a_a_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx7_a_a_,vz7_a_a_,vy7_a_a_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offu,vz4_offu,vy4_offu])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offu_,vz4_offu_,vy4_offu_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuu,vz4_offuu,vy4_offuu])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuu,vz4_offuuu,vy4_offuuu])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuu,vz4_offuuuu,vy4_offuuuu])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuu_,vz4_offuuuu_,vy4_offuuuu_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuu_,vz4_offuuuuu_,vy4_offuuuuu_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuu,vz4_offuuuuuu,vy4_offuuuuuu])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuu_,vz4_offuuuuuu_,vy4_offuuuuuu_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuum,vz4_offuuuuuum,vy4_offuuuuuum])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuumm,vz4_offuuuuuumm,vy4_offuuuuuumm])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuummm,vz4_offuuuuuummm,vy4_offuuuuuummm])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuummm_,vz4_offuuuuuummm_,vy4_offuuuuuummm_])
                                                                                                                                                                                                                    vertices3pt5a.append([vx4_offuuuuuummmm,vz4_offuuuuuummmm,vy4_offuuuuuummmm])
                                                                                                                                                                                                                    faces3pt5a.append([0,1,2])
                                                                                                                                                                                                                    faces3pt5a.append([1,2,3])
                                                                                                                                                                                                                    faces3pt5a.append([1,3,4])
                                                                                                                                                                                                                    faces3pt5a.append([3,4,11])
                                                                                                                                                                                                                    faces3pt5a.append([11,7,4])
                                                                                                                                                                                                                    faces3pt5a.append([13,11,7])
                                                                                                                                                                                                                    faces3pt5a.append([13,11,12])
                                                                                                                                                                                                                    faces3pt5a.append([11,3,10])
                                                                                                                                                                                                                    faces3pt5a.append([11,10,12])
                                                                                                                                                                                                                    faces3pt5a.append([3,10,9])
                                                                                                                                                                                                                    faces3pt5a.append([3,9,8])
                                                                                                                                                                                                                    faces3pt5a.append([8,9,0])
                                                                                                                                                                                                                    faces3pt5a.append([14,12,10])
                                                                                                                                                                                                                    faces3pt5a.append([14,7,4])
                                                                                                                                                                                                                    faces3pt5a.append([0,15,17])
                                                                                                                                                                                                                    faces3pt5a.append([15,16,17])
                                                                                                                                                                    
                                                                                                                                                                
                                                                                                                                                            
                                                                                                                                                    
                                                                                                                                            
                                                                                                                                        
                                                                                                                                    
                                                                                                                            
                                                                                                                        
                                                                                                            
                                                                                
                                                                        
                                    elif offset3b == 1627553815:
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

    uv_tex2 = mesh2.uv_layers.new()
    uv_layer2 = mesh2.uv_layers[0].data
    vert_loops2 = {}
    for l in mesh2.loops:
        vert_loops2.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2):
        for li in vert_loops2[i]:
            uv_layer2[li].uv = coord
    
    mesh2_ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh2_.from_pydata(vertices2pt2, [], faces2pt2)
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

    mesh3pt3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3pt3.from_pydata(vertices3pt3a, [], faces3pt3a)
    object3pt3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3pt3)
    collection.objects.link(object3pt3)

    mesh3pt4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3pt4.from_pydata(vertices3pt4a, [], faces3pt4a)
    object3pt4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3pt4)
    collection.objects.link(object3pt4)

    mesh3pt5 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3pt5.from_pydata(vertices3pt5a, [], faces3pt5a)
    object3pt5 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3pt5)
    collection.objects.link(object3pt5)

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



