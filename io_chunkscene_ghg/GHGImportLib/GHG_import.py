from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio
from .nigel import *

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
    
    vertices2pt2=[]
    faces2pt2=[]

    fa1=-3
    fb1=-2
    fc1=-1
    
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

            f.seek(0)
            nigel_(f)
    
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

