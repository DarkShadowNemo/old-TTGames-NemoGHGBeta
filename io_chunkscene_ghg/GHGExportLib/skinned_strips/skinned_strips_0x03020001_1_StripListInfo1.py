import bpy
from struct import unpack, pack
import mathutils
import math

def ghg_skinned_0x030200010380XX6D_STRIPLISTINFO(f, filepath):
    ob = bpy.context.object
    byte1=0
    for pbone in ob.pose.bones:
        byte1+=16
    FileSize = 0
    FileSize2 = 0
    FileSize3 = 0
    FileSize4 = 0
    FileSize5 = 0
    FileSize6 = 0
    FileSize7 = 0
    FileSize8 = 0
    FileSize9 = 0
    FileSize10 = 0
    FileSize10a = 0
    FileSize11 = 0
    positions1=[]
    positions2=[]
    FileSize12 = 0
    FileSize13 = 0
    FileSize14 = 0
    FileSize15 = 0
    FileSize16 = 0
    FileSize17 = 0
    FileSize18 = 0
    FileSize19 = 0
    FileSize20 = 0
    FileSize21 = 0
    FileSize22 = 0
    FileSize23 = 0
    FileSize24 = 0
    FileSize25 = 0
    FileSize26 = 0
    FileSize27 = 0
    f.write(pack("<I", FileSize))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", len(bpy.data.meshes)))
    f.write(pack("<I", 144))
    f.write(pack("<I", len(ob.pose.bones)))
    f.write(pack("<I", FileSize3))
    f.write(pack("<I", FileSize4))
    f.write(pack("<I", FileSize5))
    f.write(pack("<I", 0)) #objectcount
    f.write(pack("<I", FileSize6))
    f.write(pack("<I", FileSize7))
    f.write(pack("<I", byte1+16))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 1))
    f.write(pack("<I", FileSize8))
    f.write(pack("<I", 0))
    for i in range(11):
        f.write(pack("<f", 0))
    f.write(pack("<I", 0))
    f.write(pack("<f", 1))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))

    test7=0
    test2=0
    test3=0
    test4=0
    size1=0

    for i, msh in enumerate(bpy.data.meshes):
        f.write(pack("<I", size1+144+16+test2))
        test2+=464

    pad_len = f.tell() % 16
    if pad_len > 0:
        f.write(b"\0" * (16-pad_len))
        size2 = f.seek(size1,1)
        f.seek(0)
        f.seek(144,1)
        for i, msh in enumerate(bpy.data.meshes):
            f.write(pack("<I", size2+test3))
            test3+=464
            
        pad_len77 = f.tell() % 16
        if pad_len77 > 0:
            f.write(b"\0" * (16-pad_len77))

    matID=0

    for i, mshs in enumerate(bpy.data.meshes):
        f.write(pack("B", 13))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 16))
        f.write(pack("B", 8))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x50))
        f.write(pack("B", 7))
        f.write(pack("B", 0x80))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 16))
        f.write(pack("B", 14))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x48))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x1B))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x44))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x42))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x4E))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xDB))
        f.write(pack("B", 0x37))
        f.write(pack("B", 5))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x47))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x7F))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))#1
        f.write(pack("B", 0))#2
        f.write(pack("B", 0))#3
        f.write(pack("B", 0))#4
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x13))
        f.write(pack("B", 0))
        f.write(pack("B", 3))
        f.write(pack("B", 0x6C))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        for i in range(19):
            f.write(pack("B", 0))
        f.write(pack("B", 0x30))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        for i in range(128):
            f.write(pack("B", 0))
        f.write(pack("B", 0x19))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("<I", 16384))
        f.write(pack("B", 0xB0))
        f.write(pack("B", 0xE2))
        f.write(pack("B", 0xA3))
        f.write(pack("B", 0))
        f.write(pack("B", 0x80))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0x49))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x3D))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x58))
        f.write(pack("B", 0xE3))
        f.write(pack("B", 0xA3))
        f.write(pack("B", 0))
        f.write(pack("B", 0xB0))
        f.write(pack("B", 0xDD))
        f.write(pack("B", 0x87))
        f.write(pack("B", 0))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0x7B))
        f.write(pack("B", 0x98))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<f", 0))
        f.write(pack("B", 0x13))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<f", 0.5))
        f.write(pack("<f", 0.5))
        f.write(pack("<f", 0.5))
        f.write(pack("<f", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<f", 1))
        f.write(pack("<I", 0))
        f.write(pack("<I", matID))
        f.write(pack("B", 0xA6))
        f.write(pack("B", 255))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xFF))

        matID+=1
    namedt = f.seek(FileSize7,1)

    for pbone in ob.pose.bones:
        f.write(bytes(pbone.name, "utf-8"))
        f.write(pack("B", 0))

        pad_len2 = f.tell() % 16
        if pad_len2 > 0:
            f.write(b"\0" * (16-pad_len2))

    if len(pbone.name) >= 16:
        raise Exception("must be length 16 name bones")

    f.write(bytes("defaultLayer\x00\x00\x00\x00", "utf-8"))

    rotm1 = f.seek(FileSize3,1)
    characternamelength = 0
    for pbone in ob.pose.bones:
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<I", 144+FileSize7+464*len(bpy.data.meshes)+characternamelength+16))
        f.write(pack("b", ob.data.bones.find(pbone.parent.name) if pbone.parent is not None else -1))
        f.write(pack("<I", 1))
        for i in range(11):
            f.write(pack("B", 0))
        characternamelength+=16
    sclm1 = f.seek(FileSize4,1)

    for pbone in ob.pose.bones:
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))

    posm1 = f.seek(FileSize5,1)

    for pbone in ob.pose.bones:
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", -pbone.head[0]))
        f.write(pack("<f", -pbone.head[2]))
        f.write(pack("<f", -pbone.head[1]))
        f.write(pack("<f", 1))

    msh1s = f.seek(FileSize6,1)

    msh2s = f.seek(FileSize8,1)

    f.write(pack("<I", FileSize23))
    f.write(pack("<I", 0))
    f.write(pack("<I", FileSize24))
    f.write(pack("<I", FileSize25))
    f.write(pack("<I", 0))
    dsize1 = f.seek(FileSize23,1)
    f.seek(-20,1)
    f.write(pack("<I", dsize1))
    f.seek(16,1)
    f.write(bytes("defaultLayer\x00\x00\x00\x00", "utf-8"))

    dsize2 = f.seek(FileSize24,1)
    dsize2a = f.seek(FileSize25,1)
    f.seek(-36,1)
    f.seek(8,1)
    f.write(pack("<I", dsize2+24))
    f.write(pack("<I", dsize2a))
    f.seek(20,1)
    
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", FileSize26))
    f.write(pack("<I", 0))
    for i in range(16):
        f.write(pack("<f", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))

    dsize3a = f.seek(FileSize26,1)
    f.seek(-80,1)
    f.write(pack("<I", dsize3a))
    f.write(pack("<I", 0))
    for i in range(16):
        f.write(pack("<f", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))

    modelid=0

    for i, mm_mat in enumerate(bpy.data.meshes):
        if len(mm_mat.vertices) == 28:
            if len(mm_mat.polygons) == 26:
                
                f.write(pack("<I", 0))
                f.write(pack("<I", modelid))
                f.write(pack("<I", 0))
                f.write(pack("<I", FileSize27))
                dsize9 = f.seek(FileSize27,1)
                f.seek(-4,1)
                f.write(pack("<I", dsize9+8))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 268894208))
                f.write(pack("<I", 0))
                f.write(pack("<I", 16777480))
                f.write(pack("<I", 0))
                f.write(pack("<I", 805830660))
                f.write(pack("<I", 320))
                f.write(pack("<I", 268435456))
                f.write(pack("<I", 1812201496))
                f.write(pack("<I", 805830660))
                f.write(pack("<I", 64))
                f.write(pack("<I", 268435456))
                f.write(pack("<I", 1812201497))
                f.write(pack("<I", 805830660))
                f.write(pack("<I", 256))
                f.write(pack("<I", 268435456))
                f.write(pack("<I", 1812201498))
                f.write(pack("<I", 805830660))
                f.write(pack("<I", 192))
                f.write(pack("<I", 268435456))
                f.write(pack("<I", 1812201499))
                f.write(pack("<I", 805830660))
                f.write(pack("<I", 128))
                f.write(pack("<I", 268435456))
                f.write(pack("<I", 1812201500))
                f.write(pack("<I", 1342177280))
                f.write(pack("<I", 128))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 1610612736))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))

                f.write(pack("<H", 48))
                f.write(pack("B", 6))
                f.write(pack("B", 96))
                f.write(pack("<I", 0))
                f.write(pack("<I", 16777473))
                f.write(pack("<I", 0))
                f.write(pack("<I", 1812037842))
                f.write(pack("<I", 32796))
                f.write(pack("<I", 805437440))
                f.write(pack("<I", 1298))
                f.write(pack("<I", 0))
                f.write(pack("<I", 1828814850))
                f.write(pack("<I", 393300))
                f.write(pack("<I", 2949153))
                f.write(pack("B", 3))
                f.write(pack("B", 2))
                f.write(pack("B", 0))
                f.write(pack("B", 1))
                f.write(pack("B", 3))
                f.write(pack("B", 128))
                f.write(pack("B", len(mm_mat.vertices)*2))
                f.write(pack("B", 109))
                for v in mm_mat.vertices:
                    f.write(pack("<h", int(4096*v.co.x)))
                    f.write(pack("<h", int(4096*v.co.z)))
                    f.write(pack("<h", int(4096*v.co.y)))
                    f.write(pack("<h", int(4096*v.normal.z)))
                    f.write(pack("<h", 0))
                    f.write(pack("<h", 0))
                    f.write(pack("<h", 0))
                    f.write(pack("<h", 0))
                f.write(pack("<I", 16777475))
                f.write(pack("<I", 83886081))
                f.write(pack("<I", 805306368))
                f.write(pack("<f", bpy.context.object.scale[0]*65536))
                f.write(pack("<f", bpy.context.object.scale[1]*65536))
                f.write(pack("<f", bpy.context.object.scale[2]*65536))
                f.write(pack("<f", 65536))

                f.write(pack("B", 5))
                f.write(pack("B", 0xC0))
                f.write(pack("B", 28))
                f.write(pack("B", 110))

                for v in mm_mat.vertices:
                    f.write(pack("B", 255))
                    f.write(pack("B", 127))
                    f.write(pack("B", 127))
                    f.write(pack("B", 0))
                f.write(pack("<I", 16777473))
                f.write(pack("<I", 83886080))
                f.write(pack("<I", 83886081))
                f.write(pack("<I", 805306368))
                f.write(pack("<f", 1.00389099121094))
                f.write(pack("<f", 1.00389099121094))
                f.write(pack("<f", 1.00389099121094))
                f.write(pack("<f", 1.00389099121094))

                f.write(pack("B", 0x83))
                f.write(pack("B", 0xC0))
                f.write(pack("B", 7))
                f.write(pack("B", 110))
                faces0=[]
                for facs in mm_mat.polygons:
                    a=facs.vertices[0]
                    b=facs.vertices[1]
                    c=facs.vertices[2]
                    faces0.append([a,b,c])
                    if faces0[0:74] == [[0, 1, 2], [2, 3, 4], [2, 1, 3], [4, 5, 6], [4, 3, 5], [6, 7, 8], [6, 5, 7], [8, 9, 10], [8, 7, 9], [10, 11, 12], [10, 9, 11], [12, 13, 14], [12, 11, 13], [14, 15, 16], [14, 13, 15], [16, 17, 18], [16, 15, 17], [18, 19, 20], [18, 17, 19], [20, 19, 21], [20, 21, 22], [22, 23, 24], [22, 21, 23], [24, 25, 26], [24, 23, 25], [26, 25, 27]]:
                        f.write(pack("B", 117))
                        f.write(pack("B", 0))
                        f.write(pack("B", 3))
                        f.write(pack("B", 6))
                        
                        f.write(pack("B", 9))
                        f.write(pack("B", 12))
                        f.write(pack("B", 15))
                        f.write(pack("B", 18))
                        f.write(pack("B", 21))
                        f.write(pack("B", 24))
                        f.write(pack("B", 27))
                        f.write(pack("B", 30))
                        f.write(pack("B", 33))
                        f.write(pack("B", 36))
                        f.write(pack("B", 39))
                        f.write(pack("B", 42))
                        f.write(pack("B", 45))
                        f.write(pack("B", 48))
                        f.write(pack("B", 51))
                        f.write(pack("B", 54))
                        f.write(pack("B", 57))
                        f.write(pack("B", 60))
                        f.write(pack("B", 63))
                        f.write(pack("B", 66))
                        f.write(pack("B", 69))
                        f.write(pack("B", 72))
                        f.write(pack("B", 75))
                        f.write(pack("B", 78))

                f.write(pack("<I", 83886080))
                f.write(pack("<I", 1342177282))
                f.write(pack("<I", 32769))
                f.write(pack("<I", 268582912))
                f.write(pack("<I", 2))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 335545102))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                f.write(pack("<I", 0))
                    
        modelid+=1
    f.seek(0)
    f.seek(44,1)
    f.write(pack("<I", msh1s))
    
    f.seek(0)
    f.seek(76,1)
    f.write(pack("<I", msh2s))
    
    
    
    
    f.seek(0)
    f.seek(36,1)
    f.write(pack("<I", posm1))
        
    f.seek(0)
    f.seek(32,1)
    f.write(pack("<I", sclm1))
    f.seek(0)
    f.seek(28,1)
    f.write(pack("<I", rotm1))
    f.seek(0)
    f.seek(48,1)
    f.write(pack("<I", namedt))

    f.seek(0)
    size2 = f.seek(FileSize,2)
    f.seek(0)
    f.write(pack("<I", size2))
    f.seek(0)

    
