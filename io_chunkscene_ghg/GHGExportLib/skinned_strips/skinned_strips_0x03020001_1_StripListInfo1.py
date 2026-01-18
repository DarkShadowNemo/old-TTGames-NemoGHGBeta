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
