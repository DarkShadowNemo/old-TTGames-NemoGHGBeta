from struct import unpack, pack, error
import os
import math
import bpy
import mathutils
from io import BytesIO as bio

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

    fa1_cb=-5
    fb1_cb=-4
    fc1_cb=-3

    fa1_ca=-5
    fb1_ca=-4
    fc1_ca=-3
    fd1_ca=-2
    fe1_ca=-1

    fa1_c=-5
    fb1_c=-4
    fc1_c=-3
    fd1_c=-2
    fe1_c=-1

    vertices3c=[]
    faces3c=[]
    uvs3c=[]

    vertices3ca=[]
    faces3ca=[]
    uvs3ca=[]

    vertices3cb=[]
    faces3cb=[]
    uvs3cb=[]

    vertices4=[]

    fa1_ba=-4
    fb1_ba=-3
    fc1_ba=-2

    fa1_b=-4
    fb1_b=-3
    fc1_b=-2
    fd1_b=-1

    fa1_a=-3
    fb1_a=-2
    fc1_a=-1

    skininfos={}

    idx1a=0

    baseFace=[]

    faceA=-4
    faceB=-2
    faceC=-1

    bone_parentlist=[]
    bone_names=[]

    vertices=[]
    faces=[]
    uvs1=[]

    fa=-1
    fb=0
    fc=1

    vertices3a=[]
    faces3a=[]
    uvs3a=[]

    vertices3b=[]
    faces3b=[]
    uvs3b=[]

    vertices3ba=[]
    faces3ba=[]
    uvs3ba=[]

    
    vertices3=[]
    faces3=[]
    uvs3=[]

    faces3a=[]

    faa=-1
    fba=0
    fca=1

    faa1=-3
    fba1=-2
    fca1=-1

    idx_ = 0

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
                bone_names.append(bone_name)
                

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
                    vertexCount2 = unpack("B", f.read(1))[0]
                    flag_2 = unpack("B", f.read(1))[0]
                    if flag_2 == 0x6C:
                        if vertexCount2 == 0:
                            pass
                        elif vertexCount2 == 1:
                            pass
                        elif vertexCount2 == 2:
                            pass
                        elif vertexCount2:
                            for j in range(vertexCount2):
                                vx = unpack("<f", f.read(4))[0]
                                vy = unpack("<f", f.read(4))[0]
                                vz = unpack("<f", f.read(4))[0]
                                type4 = unpack("B", f.read(1))[0]==False
                                value1a = unpack("B", f.read(1))[0]
                                normalZ_ = unpack("<h", f.read(2))[0]
                                static_vx = round(vx,3)
                                static_vy = round(vy,3)
                                static_vz = round(vz,3)
                                
                                vertices.append([static_vx,static_vz,static_vy])
                                fa+=1
                                fb+=1
                                fc+=1
                                if type4 > 0:
                                    faces.append([abs(j+j+type4-type4-1+fa-j-j-1+j%2),abs(j-j+type4-type4+1+fb-2-1+j-j-j%2),abs(j+type4-type4+fc-j+2-4)])

                elif Chunk == b"\x03\x02\x00\x01":
                    f.seek(2,1)
                    vertexCount2b = unpack("B", f.read(1))[0]//2
                    flag_3b = unpack("B", f.read(1))[0]
                    if flag_3b == 0x6D:
                        if vertexCount2b == 0:
                            pass
                        elif vertexCount2b == 1:
                            pass
                        elif vertexCount2b == 2:
                            pass
                        elif vertexCount2b == 3:
                            for i in range(vertexCount2b):
                                vxb = unpack("<h", f.read(2))[0]/4096
                                vyb = unpack("<h", f.read(2))[0]/4096
                                vzb = unpack("<h", f.read(2))[0]/4096
                                fnz = unpack("<h", f.read(2))[0]/4096
                                uvxb = unpack("<h", f.read(2))[0]/4096
                                uvyb = unpack("<h", f.read(2))[0]/4096
                                f.seek(4,1)
                                static_vxb = round(vxb,3)
                                static_vyb = round(vyb,3)
                                static_vzb = round(vzb,3)
                                vertices3a.append([static_vxb,static_vzb,static_vyb])
                                uvs3a.append([uvxb,-uvyb])
                            f.seek(78,1)
                            facecount = unpack("B", f.read(1))[0]
                            fflag1 = unpack("B", f.read(1))[0]
                            if fflag1 == 0x6E:
                                if facecount == 0:
                                    pass
                                elif facecount == 1:
                                    id1 = unpack("B", f.read(1))[0]
                                    if id1 == 0x09:
                                        fa1_a = unpack("B", f.read(1))[0]&0x0F
                                        fb1_a = unpack("B", f.read(1))[0]&0x0F
                                        fc1_a = unpack("B", f.read(1))[0]&0x0F
                                        fa1_a//=3
                                        fb1_a//=3
                                        fc1_a//=3
                                        fa1_a-=3
                                        fb1_a-=3
                                        fc1_a-=3
                                        fa1_a+=1*len(vertices3a)
                                        fb1_a+=1*len(vertices3a)
                                        fc1_a+=1*len(vertices3a)
                                        faces3a.append([fa1_a,fb1_a,fc1_a])
                        elif vertexCount2b == 4:
                            for i in range(vertexCount2b):
                                vxba = unpack("<h", f.read(2))[0]/4096
                                vyba = unpack("<h", f.read(2))[0]/4096
                                vzba = unpack("<h", f.read(2))[0]/4096
                                fnza = unpack("<h", f.read(2))[0]/4096
                                uvxba = unpack("<h", f.read(2))[0]/4096
                                uvyba = unpack("<h", f.read(2))[0]/4096
                                f.seek(4,1)
                                static_vxba = round(vxba,3)
                                static_vyba = round(vyba,3)
                                static_vzba = round(vzba,3)
                                vertices3b.append([static_vxba,static_vzba,static_vyba])
                                uvs3b.append([uvxba,-uvyba])

                                vertices3ba.append([static_vxba,static_vzba,static_vyba])
                                uvs3ba.append([uvxba,-uvyba])
                            f.seek(82,1)
                            facecount1 = unpack("B", f.read(1))[0]
                            fflag2 = unpack("B", f.read(1))[0]
                            if fflag2 == 0x6E:
                                if facecount1 == 0:
                                    pass
                                elif facecount1 == 1:
                                    id2a = unpack("B", f.read(1))[0]
                                    if id2a == 0x09:
                                        fa1_ba = unpack("B", f.read(1))[0]&0x0F
                                        fb1_ba = unpack("B", f.read(1))[0]&0x0F
                                        fc1_ba = unpack("B", f.read(1))[0]&0x0F
                                        fa1_ba//=3
                                        fb1_ba//=3
                                        fc1_ba//=3
                                        fa1_ba-=4
                                        fb1_ba-=4
                                        fc1_ba-=4
                                        fa1_ba+=1*len(vertices3ba)
                                        fb1_ba+=1*len(vertices3ba)
                                        fc1_ba+=1*len(vertices3ba)
                                        faces3ba.append([fa1_ba,fb1_ba,fc1_ba])
                                elif facecount1 == 2:
                                    id2 = unpack("B", f.read(1))[0]
                                    if id2 == 0x09:
                                        fa1_b = unpack("B", f.read(1))[0]&0x0F
                                        fb1_b = unpack("B", f.read(1))[0]&0x0F
                                        fc1_b = unpack("B", f.read(1))[0]&0x0F
                                        fd1_b = unpack("B", f.read(1))[0]&0x0F
                                        f.seek(3,1)
                                        fa1_b//=3
                                        fb1_b//=3
                                        fc1_b//=3
                                        fd1_b//=3
                                        fa1_b-=4
                                        fb1_b-=4
                                        fc1_b-=4
                                        fd1_b-=4
                                        fa1_b+=1*len(vertices3b)
                                        fb1_b+=1*len(vertices3b)
                                        fc1_b+=1*len(vertices3b)
                                        fd1_b+=1*len(vertices3b)
                                        faces3b.append([fa1_b,fb1_b,fc1_b])
                                        faces3b.append([fb1_b,fc1_b,fd1_b])

                        elif vertexCount2b == 5:
                            for i in range(vertexCount2b):
                                vxbb = unpack("<h", f.read(2))[0]/4096
                                vybb = unpack("<h", f.read(2))[0]/4096
                                vzbb = unpack("<h", f.read(2))[0]/4096
                                fnzb = unpack("<h", f.read(2))[0]/4096
                                uvxbb = unpack("<h", f.read(2))[0]/4096
                                uvybb = unpack("<h", f.read(2))[0]/4096
                                f.seek(4,1)
                                static_vxbb = round(vxbb,3)
                                static_vybb = round(vybb,3)
                                static_vzbb = round(vzbb,3)
                                vertices3c.append([static_vxbb,static_vzbb,static_vybb])
                                uvs3c.append([uvxbb,-uvybb])

                                vertices3ca.append([static_vxbb,static_vzbb,static_vybb])
                                uvs3ca.append([uvxbb,-uvybb])

                                vertices3cb.append([static_vxbb,static_vzbb,static_vybb])
                                uvs3cb.append([uvxbb,-uvybb])
                            f.seek(86,1)
                            facecount2 = unpack("B", f.read(1))[0]
                            fflag3 = unpack("B", f.read(1))[0]
                            if fflag3 == 0x6E:
                                if facecount2 == 0:
                                    pass
                                elif facecount2 == 1:
                                    id3b = unpack("B", f.read(1))[0]
                                    if id3b == 0x09:
                                        fa1_cb = unpack("B", f.read(1))[0]&0x0F
                                        fb1_cb = unpack("B", f.read(1))[0]&0x0F
                                        fc1_cb = unpack("B", f.read(1))[0]&0x0F
                                        fa1_cb//=3
                                        fb1_cb//=3
                                        fc1_cb//=3
                                        fa1_cb-=5
                                        fb1_cb-=5
                                        fc1_cb-=5
                                        fa1_cb+=1*len(vertices3cb)
                                        fb1_cb+=1*len(vertices3cb)
                                        fc1_cb+=1*len(vertices3cb)
                                        faces3cb.append([fa1_cb,fb1_cb,fc1_cb])
                                elif facecount2 == 2:
                                    id3a = unpack("B", f.read(1))[0]
                                    if id3a == 0x09:
                                        fa1_ca = unpack("B", f.read(1))[0]&0x0F
                                        fb1_ca = unpack("B", f.read(1))[0]&0x0F
                                        fc1_ca = unpack("B", f.read(1))[0]&0x0F
                                        fd1_ca = unpack("B", f.read(1))[0]&0x0F
                                        fe1_ca = unpack("B", f.read(1))[0]&0x0F
                                        f.seek(2,1)
                                        fa1_ca//=3
                                        fb1_ca//=3
                                        fc1_ca//=3
                                        fd1_ca//=3
                                        fe1_ca//=3
                                        fa1_ca-=5
                                        fb1_ca-=5
                                        fc1_ca-=5
                                        fd1_ca-=5
                                        fe1_ca-=5
                                        fa1_ca+=1*len(vertices3ca)
                                        fb1_ca+=1*len(vertices3ca)
                                        fc1_ca+=1*len(vertices3ca)
                                        fd1_ca+=1*len(vertices3ca)
                                        fe1_ca+=1*len(vertices3ca)
                                        faces3ca.append([fa1_ca,fb1_ca,fc1_ca])
                                        faces3ca.append([fb1_ca,fc1_ca,fd1_ca])
                                        faces3ca.append([fc1_ca,fd1_ca,fe1_ca])
                                    
                                    

                elif Chunk == b"\x04\x02\x00\x01":
                    f.seek(2,1)
                    vertexCount2a = unpack("B", f.read(1))[0]//2
                    flag_2a = unpack("B", f.read(1))[0]
                    if flag_2a == 0x6C:
                        pointer3 = f.tell()
                        if vertexCount2a == 0:
                            pass
                        elif vertexCount2a == 1:
                            pass
                        elif vertexCount2a == 2:
                            pass
                        elif vertexCount2a:
                            for j in range(vertexCount2a):
                                vxa = unpack("<f", f.read(4))[0]
                                vya = unpack("<f", f.read(4))[0]
                                vza = unpack("<f", f.read(4))[0]
                                brightness = unpack("<f", f.read(4))[0]
                                uvx3a = unpack("<f", f.read(4))[0]
                                uvy3a = unpack("<f", f.read(4))[0]
                                unk3a = unpack("<f", f.read(4))[0]
                                type4a = unpack("B", f.read(1))[0]==False
                                value1aa = unpack("B", f.read(1))[0]
                                normalZa_ = unpack("<h", f.read(2))[0]
                                static_vxa = round(vxa,3)
                                static_vya = round(vya,3)
                                static_vza = round(vza,3)
                                
                                
                                vertices3.append([static_vxa,static_vza,static_vya])
                                uvs3.append([uvx3a,-uvy3a])
                                faa+=1
                                fba+=1
                                fca+=1
                                if type4a > 0:
                                    faces3.append([abs(j+j+type4a-type4a-1+faa-j-j-1+j%2),abs(j-j+type4a-type4a+1+fba-2-1+j-j-j%2),abs(j+type4a-type4a+fca-j+2-4)])

                elif Chunk == b"\x02\x00\x01\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4 = unpack("B", f.read(1))[0]//2
                        flagg4a = unpack("B", f.read(1))[0]
                        if flagg4a == 0x6C:
                            if vertexCount4 == 0:
                                pass
                            elif vertexCount4 == 1:
                                for i in range(vertexCount4):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4 == 2:
                                for i in range(vertexCount4):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4 == 3:
                                for i in range(vertexCount4):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4 == 13:
                                for i in range(vertexCount4):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error
                elif Chunk == b"\x04\x00\x00\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4a = unpack("B", f.read(1))[0]//2
                        flagg4aa = unpack("B", f.read(1))[0]
                        if flagg4aa == 0x6C:
                            if vertexCount4a == 0:
                                pass
                            elif vertexCount4a == 1:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 2:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 3:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 4:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 7:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 9:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4a == 10:
                                for i in range(vertexCount4a):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error

                elif Chunk == b"\x06\x00\x01\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4b = unpack("B", f.read(1))[0]//2
                        flagg4ab = unpack("B", f.read(1))[0]
                        if flagg4ab == 0x6C:
                            if vertexCount4b == 0:
                                pass
                            elif vertexCount4b == 1:
                                for i in range(vertexCount4b):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4b == 3:
                                for i in range(vertexCount4b):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error

                elif Chunk == b"\x08\x00\x00\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4c = unpack("B", f.read(1))[0]//2
                        flagg4ac = unpack("B", f.read(1))[0]
                        if flagg4ac == 0x6C:
                            if vertexCount4c == 0:
                                pass
                            elif vertexCount4c == 1:
                                for i in range(vertexCount4c):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4c == 9:
                                for i in range(vertexCount4c):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error
                elif Chunk == b"\x04\x00\x01\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4d = unpack("B", f.read(1))[0]//2
                        flagg4ad = unpack("B", f.read(1))[0]
                        if flagg4ad == 0x6C:
                            if vertexCount4d == 0:
                                pass
                            elif vertexCount4d == 1:
                                for i in range(vertexCount4d):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4d == 3:
                                for i in range(vertexCount4d):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4d == 2:
                                for i in range(vertexCount4d):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4d == 4:
                                for i in range(vertexCount4d):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4d == 6:
                                for i in range(vertexCount4d):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error

                elif Chunk == b"\x06\x00\x00\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4e = unpack("B", f.read(1))[0]//2
                        flagg4ae = unpack("B", f.read(1))[0]
                        if flagg4ae == 0x6C:
                            if vertexCount4e == 0:
                                pass
                            elif vertexCount4e == 1:
                                for i in range(vertexCount4e):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4e == 3:
                                for i in range(vertexCount4e):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4e == 4:
                                for i in range(vertexCount4e):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4e == 6:
                                for i in range(vertexCount4e):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error

                elif Chunk == b"\x09\x00\x01\x00":
                    try:
                        
                        f.seek(2,1)
                        vertexCount4f = unpack("B", f.read(1))[0]//2
                        flagg4af = unpack("B", f.read(1))[0]
                        if flagg4af == 0x6C:
                            if vertexCount4f == 0:
                                pass
                            elif vertexCount4f == 1:
                                for i in range(vertexCount4f):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4f == 2:
                                for i in range(vertexCount4f):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4f == 10:
                                for i in range(vertexCount4f):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                            elif vertexCount4f == 12:
                                for i in range(vertexCount4f):
                                    vx4a = unpack("<f", f.read(4))[0]
                                    vy4a = unpack("<f", f.read(4))[0]
                                    vz4a = unpack("<f", f.read(4))[0]
                                    faceoff = unpack("B", f.read(1))[0]
                                    f.seek(3,1)
                                    f.seek(16,1)
                                    vertices4.append([vx4a,vz4a,vy4a])
                    except:
                        error

                                    
                                                
                                            
                                            
                                            
                                        
                                    
                                                    

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3.from_pydata(vertices3, [], faces3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)

    objects3.parent = arma
    armamodifier3 = objects3.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3.object = arma

    arma.show_in_front = True

    vtxgrps = {}
    for bone in arma.data.bones:
        vtxgrps[bone.name] = objects3.vertex_groups.new(name = bone.name)

    idxuv1=0

    if idxuv1 == 0:

        uv_layer = mesh3.uv_layers.new(name="UVMap")

        for loop in mesh3.loops:
            vi = loop.vertex_index

            if vi < len(uvs3):
                uv_layer.data[loop.index].uv = uvs3[vi]
            else:
                idxuv1+=1
                if idxuv1 == 1:
                    uv_tex3 = mesh3.uv_layers.new()
                    uv_layer3 = mesh3.uv_layers[0].data
                    vert_loops3 = {}
                    for l in mesh3.loops:
                        vert_loops3.setdefault(l.vertex_index, []).append(l.index)
                    for i, coord in enumerate(uvs3):
                        for li in vert_loops3[i]:
                            uv_layer3[li].uv = coord

    mesh3a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3a.from_pydata(vertices3a, [], faces3a)
    objects3a = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3a)
    collection.objects.link(objects3a)

    uv_tex3a = mesh3a.uv_layers.new()
    uv_layer3a = mesh3a.uv_layers[0].data
    vert_loops3a = {}
    for l in mesh3a.loops:
        vert_loops3a.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3a):
        for li in vert_loops3a[i]:
            uv_layer3a[li].uv = coord

    objects3a.parent = arma
    armamodifier3a = objects3a.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3a.object = arma

    arma.show_in_front = True

    vtxgrpsa = {}
    for bone in arma.data.bones:
        vtxgrpsa[bone.name] = objects3a.vertex_groups.new(name = bone.name)

    mesh3b = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3b.from_pydata(vertices3b, [], faces3b)
    objects3b = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3b)
    collection.objects.link(objects3b)

    idxuv2=0

    if idxuv2 == 0:

        uv_layer = mesh3b.uv_layers.new(name="UVMap")

        for loop in mesh3b.loops:
            vi1 = loop.vertex_index

            if vi1 < len(uvs3b):
                uv_layer.data[loop.index].uv = uvs3b[vi1]
            else:
                idxuv2+=1
                if idxuv2 == 1:
                    uv_tex3b = mesh3b.uv_layers.new()
                    uv_layer3b = mesh3b.uv_layers[0].data
                    vert_loops3b = {}
                    for l in mesh3b.loops:
                        vert_loops3b.setdefault(l.vertex_index, []).append(l.index)
                    for i, coord in enumerate(uvs3b):
                        for li in vert_loops3b[i]:
                            uv_layer3b[li].uv = coord

    objects3b.parent = arma
    armamodifier3b = objects3b.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3b.object = arma

    arma.show_in_front = True

    vtxgrpsb = {}
    for bone in arma.data.bones:
        vtxgrpsb[bone.name] = objects3b.vertex_groups.new(name = bone.name)

    mesh3ba = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ba.from_pydata(vertices3ba, [], faces3ba)
    objects3ba = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ba)
    collection.objects.link(objects3ba)

    mesh4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4.from_pydata(vertices4, [], [])
    objects4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4)
    collection.objects.link(objects4)
            


