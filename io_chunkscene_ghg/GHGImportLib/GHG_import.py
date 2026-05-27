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
    
    vertices2pt2=[]
    faces2pt2=[]

    fa1=-3
    fb1=-2
    fc1=-1

    fa3=-3
    fb3=-2
    fc3=-1
    
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
                                vx4_a = unpack("<f", f.read(4))[0];vy4_a = unpack("<f", f.read(4))[0];vz4_a = unpack("<f", f.read(4))[0];brightness4_a = unpack("<f", f.read(4))[0];uvx4_a = unpack("<f", f.read(4))[0];uvy4_a = unpack("<f", f.read(4))[0];unk4_a = unpack("<f", f.read(4))[0];faceon4_a = unpack("B", f.read(1))[0];valueon4_a = unpack("B", f.read(1))[0];nz4_a = unpack("<h", f.read(2))[0];vx5_a = unpack("<f", f.read(4))[0];vy5_a = unpack("<f", f.read(4))[0];vz5_a = unpack("<f", f.read(4))[0];brightness5_a = unpack("<f", f.read(4))[0];uvx5_a = unpack("<f", f.read(4))[0];uvy5_a = unpack("<f", f.read(4))[0];unk5_a = unpack("<f", f.read(4))[0];faceon5_a = unpack("B", f.read(1))[0];valueon5_a = unpack("B", f.read(1))[0];nz5_a = unpack("<h", f.read(2))[0];vx6_a = unpack("<f", f.read(4))[0];vy6_a = unpack("<f", f.read(4))[0];vz6_a = unpack("<f", f.read(4))[0];brightness6_a = unpack("<f", f.read(4))[0];uvx6_a = unpack("<f", f.read(4))[0];uvy6_a = unpack("<f", f.read(4))[0];unk6_a = unpack("<f", f.read(4))[0];faceon6_a = unpack("B", f.read(1))[0];valueon6_a = unpack("B", f.read(1))[0];nz6_a = unpack("<h", f.read(2))[0]
                            offset2 = unpack("<I", f.read(4))[0]
                            f.seek(-4,1)
                            offset3 = unpack("<I", f.read(4))[0]
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
                                                    for i in range(1):
                                                        vx4_off = unpack("<f", f.read(4))[0]
                                                        vy4_off = unpack("<f", f.read(4))[0]
                                                        vz4_off = unpack("<f", f.read(4))[0]
                                                    #todo
                            if offset2 == 16777473:
                                if faceon4_ == 1:
                                    if faceon5_ == 1:
                                        if faceon6_ == 0:
                                            if faceon7_ == 0:
                                                pass
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

    uv_tex3 = mesh3.uv_layers.new()
    uv_layer3 = mesh3.uv_layers[0].data
    vert_loops3 = {}
    for l in mesh3.loops:
        vert_loops3.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3):
        for li in vert_loops3[i]:
            uv_layer3[li].uv = coord
    
    #if vertices2_[0:3] == [{-3.069, -3.962, -2.021}, {0.036, 1.975, 0.944}, {4.036, 5.975, 4.944}]:
    #pearl_(filepath)



