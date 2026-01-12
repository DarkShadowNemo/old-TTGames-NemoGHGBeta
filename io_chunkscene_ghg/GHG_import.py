from struct import unpack, pack
import os
import bmesh
import math
import bpy
import mathutils
from io import BytesIO as bio
import sys

#adding this incase it doesn't work so you can play around with it

#does not work ghg decoding textures

#single by name
"""
ob = bpy.context.scene.objects.get("Cube")  # Replace "Cube" with the desired object name
if ob:
    ob.select_set(True)"""

#multiple by name

"""
for obj_name in ["Cube", "Camera", "Light"]:
      obj = bpy.context.scene.objects.get(obj_name)
      if obj:
          obj.select_set(True)"""

"""
for obj in bpy.context.scene.objects:
    if obj.name.startswith("pad"):
        obj.select_set(True)"""

"""
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.object.mode_set(mode='OBJECT')
        
        obj.data.vertices[0].select = True
        obj.data.vertices[1].select = True
        obj.data.vertices[2].select = True
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.edge_face_add()
        bpy.ops.object.editmode_toggle()

"""

def get_size_from_sub_hdr(f, is_pallete):
    size_ = unpack("<H", f.read(2))[0]
    f.seek(14,1)

    if is_pallete == True:
        if size_ == 0x8008:
            return 16
        elif size_ == 0x8080:
            return 256
        else:
            print("unsupported pallete size %d" % size_)
    return abs(0x8000 - size_) << 4

def read_pallete(f, amt):
    global g_pallete1
    global g_pallete2
    global g_pallete3
    global g_pallete4
    g_pallete1=[]
    g_pallete2=[]
    g_pallete3=[]
    g_pallete4=[]
    for i in range(0, amt):
        r = unpack("B", f.read(1))[0]*0+255/255
        g = unpack("B", f.read(1))[0]*0+255/255
        b = unpack("B", f.read(1))[0]*0+255/255
        a = unpack("B", f.read(1))[0]*0+255/255
        
        g_pallete1.append(r)
        g_pallete2.append(g)
        g_pallete3.append(b)
        g_pallete4.append(a)
                    
                    
    
    

def GHG_Blend_Object(f, filepath):
    ob = bpy.context.object
    blends=[]
    BlendShapes = 1
    f.seek(0)
    BlendChunks = f.read()
    readBlendChunks = BlendChunks.find(b"\x38\x00\x01\x6E")
    if BlendChunks != 0:
        f.seek(readBlendChunks,0)
        f.seek(4,1)
        f.seek(4,1)
        f.seek(2,1)
        blendshapecount = unpack("B", f.read(1))[0]
        flag = unpack("B", f.read(1))[0]
        for i in range(blendshapecount):
            blend_vx = unpack("<f", f.read(4))[0]
            blend_vy = unpack("<f", f.read(4))[0]
            blend_vz = unpack("<f", f.read(4))[0]
            blend_indices = unpack("<I", f.read(4))[0]
            blends.append([blend_vx,blend_vy,blend_vz,blend_indices])

        ob.shape_key_add(name = 'BlendShape Base')
        blendshape = ob.shape_key_add(name = "GHG BlendShape Key")

        for i, bl_ in enumerate(blends):
            if bl_[3]:
                blendshape.data[0].co.x += bl_[0]
                blendshape.data[1].co.y += bl_[2]
                blendshape.data[2].co.z += bl_[1]
    

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

    voffsets=[]

    skininfos={}
    f.seek(0)

    fad7_=-1
    fbd7_=0
    fcd7_=1
    fdd7_=2
    fed7_=3
    ffd7_=4
    fgd7_=5

    vertices2=[]
    faces2=[]

    vertices2a=[]
    faces2a=[]
    

    vertices2b=[]
    faces2b=[]

    vertices2c=[]
    faces2c=[]

    vertices2d=[]
    faces2d=[]

    vertices2e=[]
    faces2e=[]

    vertices2f=[]
    faces2f=[]

    vertices2g=[]
    faces2g=[]

    vertices2h=[]
    faces2h=[]

    vertices2i=[]
    faces2i=[]

    vertices2j=[]
    faces2j=[]

    vertices2k=[]
    faces2k=[]

    vertices2l=[]
    faces2l=[]

    vertices2m=[]
    faces2m=[]

    vertices2n=[]
    faces2n=[]

    vertices2o=[]
    faces2o=[]

    vertices2p=[]
    faces2p=[]

    vertices2q=[]
    faces2q=[]

    vertices2r=[]
    faces2r=[]

    vertices2s=[]
    faces2s=[]

    vertices2t=[]
    faces2t=[]

    vertices2u=[]
    faces2u=[]

    vertices2v=[]
    faces2v=[]

    vertices2w=[]
    faces2w=[]

    vertices2x=[]
    faces2x=[]

    vertices2y=[]
    faces2y=[]

    vertices2z=[]
    faces2z=[]

    vertices2zz=[]
    faces2zz=[]

    vertices2zzz=[]
    faces2zzz=[]

    vertices2zzzz=[]
    faces2zzzz=[]

    vertices2zzzzz=[]
    faces2zzzzz=[]

    vertices2zzzzzz=[]
    faces2zzzzzz=[]

    vertices2zzzzzzz=[]
    faces2zzzzzzz=[]

    vertices2zzzzzzzz=[]
    faces2zzzzzzzz=[]

    vertices2zzzzzzzzz=[]
    faces2zzzzzzzzz=[]

    vertices2zzzzzzzzzz=[]
    faces2zzzzzzzzzz=[]

    vertices2zzzzzzzzzzzzzz=[]
    faces2zzzzzzzzzzzzzz=[]

    vertices2zzzzzzzzzzzzz=[]
    faces2zzzzzzzzzzzzz=[]

    vertices2zzzzzzzzzzzz=[]
    faces2zzzzzzzzzzzz=[]

    vertices2zzzzzzzzzzz=[]
    faces2zzzzzzzzzzz=[]

    vertices3 = []
    faces3 = []

    uv_coords = []

    vertices3A = []
    faces3A = []

    vertices3Aaq = []
    faces3Aaq = []

    vertices3Baq = []
    faces3Baq = []

    vertices3Caq = []
    faces3Caq = []

    vertices3Daq = []
    faces3Daq = []

    vertices3Daqa=[]
    faces3Daqa=[]

    vertices3Daqaq=[]
    faces3Daqaq=[]

    vertices3Daqaqaqe=[]
    faces3Daqaqaqe=[]

    vertices3Daqaqaq=[]
    faces3Daqaqaq=[]

    vertices3Daqaqa=[]
    faces3Daqaqa=[]

    cocoVerts02 =[]
    cocoFaces02 =[]

    cocoVerts01 =[]
    cocoFaces01 =[]

    overlordverts01=[]
    overlordfaces01=[]

    overlordverts02=[]
    overlordfaces02=[]

    overlordverts03=[]
    overlordfaces03=[]

    overlordverts04=[]
    overlordfaces04=[]

    overlordverts05=[]
    overlordfaces05=[]

    overlordverts06=[]
    overlordfaces06=[]

    overlordverts07=[]
    overlordfaces07=[]

    overlordverts08=[]
    overlordfaces08=[]

    overlordA8=-21
    overlordB8=-20
    overlordC8=-19
    overlordD8=-18
    overlordE8=-9

    overlordA7=-6
    overlordB7=-5
    overlordC7=-4
    overlordD7=-3
    overlordE7=-1
    overlordF7=-2

    overlordA6=-7
    overlordB6=-6
    overlordC6=-5
    overlordD6=-4
    overlordE6=-3
    overlordF6=-2
    overlordG6=-1

    overlordA5=-7
    overlordB5=-6
    overlordC5=-5
    overlordD5=-4
    overlordE5=-3
    overlordF5=-2
    overlordG5=-1

    overlordA4=-20
    overlordB4=-19
    overlordC4=-18
    overlordD4=-17
    overlordE4=-16
    overlordF4=-15
    overlordG4=-13
    overlordH4=-12
    overlordI4=-11
    overlordJ4=-10
    overlordK4=-9
    overlordL4=-6
    overlordM4=-5
    overlordN4=-4
    overlordO4=-1

    overlordA3=-24
    overlordB3=-23
    overlordC3=-22
    overlordD3=-21
    overlordE3=-20
    overlordF3=-19
    overlordG3=-18
    overlordH3=-17
    overlordI3=-16
    overlordJ3=-15
    overlordK3=-14
    overlordL3=-13
    overlordM3=-12
    overlordN3=-11
    overlordO3=-10
    overlordP3=-8
    overlordQ3=-6
    overlordR3=-7
    overlordS3=-5
    overlordT3=-4
    overlordU3=-3
    overlordV3=-1
    overlordW3=-9

    
    overlordA2=-7
    overlordB2=-6
    overlordC2=-5
    overlordD2=-4
    overlordE2=-3
    overlordF2=-2
    overlordG2=-1

    overlordA1=-7
    overlordB1=-6
    overlordC1=-5
    overlordD1=-4
    overlordE1=-3
    overlordF1=-2
    overlordG1=-1

    cocoA=-12
    cocoB=-11
    cocoC=-10
    cocoD=-9
    cocoE=-8
    cocoF=-7
    cocoG=-6
    cocoH=-5
    cocoI=-4
    cocoJ=-3
    cocoK=-2
    cocoL=-1

    cocoAa=-17
    cocoBa=-16
    cocoCa=-15
    cocoDa=-14
    cocoEa=-13
    cocoFa=-12
    cocoGa=-11
    cocoHa=-10
    cocoIa=-2
    cocoJa=-1
    cocoKa=-9
    cocoLa=-8
    cocoMa=-7
    cocoNa=-6
    cocoOa=-5
    cocoPa=-4
    cocoQa=-3
    

    vertices3AA = []
    faces3AA = []

    vertices3AAx = []
    faces3AAx = []

    vertices3AApt2 = []
    faces3AApt2 = []

    vertices3AApt3 = []
    faces3AApt3 = []

    vertices3BBpt2 = []
    faces3BBpt2 = []

    vertices3BB = []
    faces3BB = []

    vertices3BBd = []
    faces3BBd = []

    vertices3CC = []
    faces3CC = []

    vertices3DD = []
    faces3DD = []

    vertices3EE = []
    faces3EE = []

    vertices3FF = []
    faces3FF = []

    vertices3GG = []
    faces3GG = []

    vertices3HH = []
    faces3HH = []

    vertices3II = []
    faces3II = []

    vertices3JJ = []
    faces3JJ = []

    vertices3KK = []
    faces3KK = []

    vertices3LL = []
    faces3LL = []

    vertices3MM = []
    faces3MM = []

    vertices3NN = []
    faces3NN = []

    vertices3OO = []
    faces3OO = []

    vertices3PP = []
    faces3PP = []

    vertices3QQ = []
    faces3QQ = []

    vertices3RR = []
    faces3RR = []

    vertices3SS = []
    faces3SS = []

    vertices3TT = []
    faces3TT = []

    vertices3UU = []
    faces3UU = []

    vertices3VV = []
    faces3VV = []

    vertices3WW = []
    faces3WW = []

    vertices3XX = []
    faces3XX = []

    vertices3YY = []
    faces3YY = []

    vertices3ZZ = []
    faces3ZZ = []

    vertices3ZZZ = []
    faces3ZZZ = []

    vertices3ZZZ1 = []
    faces3ZZZ1 = []

    vertices3ZZZ2 = []
    faces3ZZZ2 = []

    vertices3ZZZ3 = []
    faces3ZZZ3 = []

    vertices3ZZZ4 = []
    faces3ZZZ4 = []

    vertices3ZZZ5 = []
    faces3ZZZ5 = []

    vertices3ZZZ6 = []
    faces3ZZZ6 = []

    vertices4 = []
    faces4 = []

    vertices4_1 = []
    vertices4_2 = []
    vertices4_3 = []
    vertices4_4 = []
    faces4_4 = []
    faces4_3 = []
    edges4_2 = []
    vertices4_7 = []
    faces4_7 = []

    vertices4_11=[]
    faces4_11=[]

    vertices4_12 = []
    faces4_12 = []

    vertices4_5 = []
    faces4_5 = []

    vertices4_6 = []
    faces4_6 = []

    fa4_3=-3
    fb4_3=-2
    fc4_3=-1
    
    fa4_4=-3
    fb4_4=-2
    fc4_4=-1

    fa4a_4=-3
    fb4a_4=-2
    fc4a_4=-1

    fa4_5=-3
    fb4_5=-2
    fc4_5=-1

    fa4_6=-3
    fb4_6=-2
    fc4_6=-1

    fa4_5a=-3
    fb4_5a=-2
    fc4_5a=-1

    fa4_5b=-3
    fb4_5b=-2
    fc4_5b=-1

    fa4_7a=-4
    fb4_7a=-3
    fc4_7a=-2

    fa4_7=-3
    fb4_7=-2
    fc4_7=-1

    fa4_12=-3
    fb4_12=-2
    fc4_12=-1

    #fa4_7a=-3
    #fb4_7a=-2
    #fc4_7a=-1

    brightt1=[]
    brightt2=[]

    ea=-2
    eb=-1

    fa = -1
    fb = 0
    fc = 1

    faqqqqa=-4
    fbqqqqa=-3
    fcqqqqa=-2
    fdqqqqa=-1

    faqqqqaaaaaaa=-4
    fbqqqqaaaaaaa=-2
    fcqqqqaaaaaaa=-3
    fdqqqqaaaaaaa=-1

    faqqqqaaaaaaaa=-4
    fbqqqqaaaaaaaa=-1
    fcqqqqaaaaaaaa=-2
    fdqqqqaaaaaaaa=-3

    faqqqqaaaaaaaaa=-4
    fbqqqqaaaaaaaaa=-1
    fcqqqqaaaaaaaaa=-3
    fdqqqqaaaaaaaaa=-2

    faqqqqaaaaaaaaaa=-4
    fbqqqqaaaaaaaaaa=-3
    fcqqqqaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaa=-2

    faqqqqaaaaaaaaaaa=-4
    fbqqqqaaaaaaaaaaa=-2
    fcqqqqaaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaaa=-3

    faqqqqaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaa=-4
    fcqqqqaaaaaaaaaaaa=-2
    fdqqqqaaaaaaaaaaaa=-1

    faqqqqaaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaaa=-2
    fcqqqqaaaaaaaaaaaaa=-4
    fdqqqqaaaaaaaaaaaaa=-1

    faqqqqaaaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaaaa=-4
    fcqqqqaaaaaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaaaaaa=-2

    faqqqqaaaaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaaaaa=-2
    fcqqqqaaaaaaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaaaaaaa=-4

    faqqqqaaaaaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaaaaaa=-1
    fcqqqqaaaaaaaaaaaaaaaa=-4
    fdqqqqaaaaaaaaaaaaaaaa=-2

    faqqqqaaaaaaaaaaaaaaaaa=-3
    fbqqqqaaaaaaaaaaaaaaaaa=-1
    fcqqqqaaaaaaaaaaaaaaaaa=-2
    fdqqqqaaaaaaaaaaaaaaaaa=-4

    faqqqqaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaa=-4
    fcqqqqaaaaaaaaaaaaaaaaaa=-3
    fdqqqqaaaaaaaaaaaaaaaaaa=-1

    faqqqqaaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaaa=-3
    fcqqqqaaaaaaaaaaaaaaaaaaa=-4
    fdqqqqaaaaaaaaaaaaaaaaaaa=-1

    faqqqqaaaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaaaa=-4
    fcqqqqaaaaaaaaaaaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaaaaaaaaaaaa=-3

    faqqqqaaaaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaaaaa=-3
    fcqqqqaaaaaaaaaaaaaaaaaaaaa=-1
    fdqqqqaaaaaaaaaaaaaaaaaaaaa=-4

    faqqqqaaaaaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaaaaaa=-1
    fcqqqqaaaaaaaaaaaaaaaaaaaaaa=-4
    fdqqqqaaaaaaaaaaaaaaaaaaaaaa=-3

    faqqqqaaaaaaaaaaaaaaaaaaaaaaa=-2
    fbqqqqaaaaaaaaaaaaaaaaaaaaaaa=-1
    fcqqqqaaaaaaaaaaaaaaaaaaaaaaa=-3
    fdqqqqaaaaaaaaaaaaaaaaaaaaaaa=-4

    faqqqqaaaaaaaaaaaaaaaaaaaaaaaa=-1
    fbqqqqaaaaaaaaaaaaaaaaaaaaaaaa=-4
    fcqqqqaaaaaaaaaaaaaaaaaaaaaaaa=-2
    fdqqqqaaaaaaaaaaaaaaaaaaaaaaaa=-3

    faqqqqaa=-1
    fbqqqqaa=-4
    fcqqqqaa=-3
    fdqqqqaa=-2

    faqqqqaaa=-1
    fbqqqqaaa=-3
    fcqqqqaaa=-4
    fdqqqqaaa=-2

    faqqqqaaaa=-1
    fbqqqqaaaa=-3
    fcqqqqaaaa=-2
    fdqqqqaaaa=-4

    faqqqqaaaaa=-1
    fbqqqqaaaaa=-2
    fcqqqqaaaaa=-3
    fdqqqqaaaaa=-4

    faqqqqaaaaaa=-1
    fbqqqqaaaaaa=-2
    fcqqqqaaaaaa=-4
    fdqqqqaaaaaa=-3

    faqqqqb=-5
    fbqqqqb=-4
    fcqqqqb=-3
    fdqqqqb=-2
    feqqqqb=-1

    faqqqq=-3
    fbqqqq=-2
    fcqqqq=-1

    fa2Ta_a=-5

    fb2Ta_a=-4
    fc2Ta_a=-3

    fd2Ta_a=-2

    fe2Ta_a=-1

    fa2Ta_b=-5

    fb2Ta_b=-4
    fc2Ta_b=-3

    fd2Ta_b=-2

    fe2Ta_b=-1

    fa2Ta_c=-6

    fb2Ta_c=-5
    fc2Ta_c=-4

    fd2Ta_c=-3

    fe2Ta_c=-2
    ff2Ta_c=-1


    fa2Ta_d=-5

    fb2Ta_d=-4
    fc2Ta_d=-3

    fd2Ta_d=-2
    fe2Ta_d=-1

    fa2Ta_daTaT=-19
    fb2Ta_daTaT=-18
    fc2Ta_daTaT=-17
    fd2Ta_daTaT=-16
    fe2Ta_daTaT=-15
    ff2Ta_daTaT=-14
    fg2Ta_daTaT=-13
    fh2Ta_daTaT=-12
    fi2Ta_daTaT=-11
    fj2Ta_daTaT=-10
    fk2Ta_daTaT=-9
    fl2Ta_daTaT=-8
    fm2Ta_daTaT=-7
    fn2Ta_daTaT=-6
    fo2Ta_daTaT=-5
    fp2Ta_daTaT=-4
    fq2Ta_daTaT=-3
    fr2Ta_daTaT=-2
    fs2Ta_daTaT=-1


    fa2Ta_daTaD=-12
    fb2Ta_daTaD=-11
    fc2Ta_daTaD=-10
    fd2Ta_daTaD=-9
    fe2Ta_daTaD=-8

    fa2Ta_daTa=-8
    fb2Ta_daTa=-7
    fc2Ta_daTa=-6
    fd2Ta_daTa=-5

    fa2Ta_daT=-16
    fb2Ta_daT=-15
    fc2Ta_daT=-14
    fd2Ta_daT=-13
    fe2Ta_daT=-12

    ff2Ta_daT=-11
    fg2Ta_daT=-10
    fh2Ta_daT=-9
    fi2Ta_daT=-8

    fj2Ta_daT=-7
    fk2Ta_daT=-6
    fl2Ta_daT=-5
    fm2Ta_daT=-4

    fa2Ta_da=-28

    fb2Ta_da=-27
    fc2Ta_da=-26

    fd2Ta_da=-25
    fe2Ta_da=-24
    ff2Ta_da=-23

    fg2Ta_da=-22

    fh2Ta_da=-21
    fi2Ta_da=-13

    fj2Ta_da=-20
    fk2Ta_da=-19
    fl2Ta_da=-18

    fm2Ta_da=-17
    fn2Ta_da=-16
    fo2Ta_da=-15

    fp2Ta_da=-6

    fa2CAQ=-4
    fb2CAQ=-3
    fc2CAQ=-2
    fa3CAQ=-1

    fau = -1
    fbu = 0
    fcu = 1

    #fad1 = -4
    #fbd1 = -3
    #fcd1 = -2
    #fad2 = -3
    #fbd2 = -2
    #fcd2 = -1

    fad = -3
    fbd = -2
    fcd = -1

    fad1abc = -1
    fbd1abc = 0
    fcd1abc = 1

    fad5 = -1
    fbd5 = 0
    fcd5 = 1
    fdd5 = 2
    fed5 = 3

    fa1 = -3
    fb1 = -2
    fc1 = -1

    fa2 = -3
    fb2 = -2
    fc2 = -1


    fa2_=-9
    fb2_=-7
    fc2_=-6

    fa2c = -1
    fb2c = 0
    fc2c = 1

    fa2AA_a = -4
    fb2AA_a = -3
    fc2AA_a = -2
    fa2AA__a = -4
    fb2AA__a = -2
    fc2AA__a = -1

    fa2AAx = -4
    fb2AAx = -3
    fc2AAx = -2
    fa2AAx_ = -3
    fb2AAx_ = -2
    fc2AAx_ = -1

    fa2AA = -4
    fb2AA = -3
    fc2AA = -2
    fa2AA_ = -3
    fb2AA_ = -2
    fc2AA_ = -1

    fa2AApt2 = -3
    fb2AApt2 = -2
    fc2AApt2 = -1

    fa2AApt3 = -3
    fb2AApt3 = -2
    fc2AApt3 = -1

    fa2BBpt2a = -5#0
    fb2BBpt2a = -4#1
    fc2BBpt2a = -3#2
    fa2BBpt2a_ = -5#0
    fb2BBpt2a_ = -3#2
    fc2BBpt2a_ = -2#3
    fa2BBpt2a__ = -3#2
    fb2BBpt2a__ = -2#3
    fc2BBpt2a__ = -1#4
    

    fa2BBpt2 = -5
    fb2BBpt2 = -4
    fc2BBpt2 = -3

    fa2BBpt2_ = -4
    fb2BBpt2_ = -3
    fc2BBpt2_ = -2

    fa2BBpt2__ = -3
    fb2BBpt2__ = -2
    fc2BBpt2__ = -1

    fa2BB = -1
    fb2BB = 0
    fc2BB = 1

    fa2CC = -1
    fb2CC = 0
    fc2CC = 1

    fa2DD = -1
    fb2DD = 0
    fc2DD = 1

    fa2EE = -1
    fb2EE = 0
    fc2EE = 1

    fa2FF = -1
    fb2FF = 0
    fc2FF = 1

    fa2GG = -1
    fb2GG = 0
    fc2GG = 1

    fa2HH = -1
    fb2HH = 0
    fc2HH = 1

    fa2II = -1
    fb2II = 0
    fc2II = 1

    fa2JJ = -1
    fb2JJ = 0
    fc2JJ = 1

    fa2KK = -1
    fb2KK = 0
    fc2KK = 1

    fa2LL = -1
    fb2LL = 0
    fc2LL = 1

    fa2MM = -1
    fb2MM = 0
    fc2MM = 1

    fa2NN = -1
    fb2NN = 0
    fc2NN = 1

    fa2OO = -1
    fb2OO = 0
    fc2OO = 1

    fa2PP = -1
    fb2PP = 0
    fc2PP = 1

    fa2QQ = -1
    fb2QQ = 0
    fc2QQ = 1

    fa2RR = -1
    fb2RR = 0
    fc2RR = 1

    fa2SS = -1
    fb2SS = 0
    fc2SS = 1

    fa2TT = -1
    fb2TT = 0
    fc2TT = 1

    fa2UU = -1
    fb2UU = 0
    fc2UU = 1

    fa2VV = -1
    fb2VV = 0
    fc2VV = 1

    fa2WW = -1
    fb2WW = 0
    fc2WW = 1

    fa2XX = -1
    fb2XX = 0
    fc2XX = 1

    fa2YY = -1
    fb2YY = 0
    fc2YY = 1

    fa2ZZ = -1
    fb2ZZ = 0
    fc2ZZ = 1

    fa2ZZZ = -1
    fb2ZZZ = 0
    fc2ZZZ = 1

    fa2ZZZ1 = -1
    fb2ZZZ1 = 0
    fc2ZZZ1 = 1

    fa2ZZZ2 = -1
    fb2ZZZ2 = 0
    fc2ZZZ2 = 1

    fa2ZZZ3 = -1
    fb2ZZZ3 = 0
    fc2ZZZ3 = 1

    fa2ZZZ4 = -1
    fb2ZZZ4 = 0
    fc2ZZZ4 = 1

    fa2ZZZ5 = -1
    fb2ZZZ5 = 0
    fc2ZZZ5 = 1

    fa2ZZZ6 = -1
    fb2ZZZ6 = 0
    fc2ZZZ6 = 1

    uvs=[]
    uvs3=[]
    uvs3AA=[]
    uvs3AApt2=[]
    uvs3AApt3=[]
    uvs3BBpt2=[]
    uvs3BB=[]
    uvs3BBd=[]
    uvs3CC=[]
    uvs3DD=[]
    uvs3EE=[]
    uvs3FF=[]
    uvs3GG=[]
    uvs3HH=[]
    uvs3II=[]
    uvs3JJ=[]
    uvs3KK=[]
    uvs3LL=[]
    uvs3MM=[]
    uvs3NN=[]
    uvs3OO=[]
    uvs3PP=[]
    uvs3QQ=[]
    uvs3RR=[]
    uvs3SS=[]
    uvs3TT=[]
    uvs3UU=[]
    uvs3VV=[]
    uvs3WW=[]
    uvs3XX=[]
    uvs3YY=[]
    uvs3ZZ=[]
    uvs3ZZZ=[]
    uvs3ZZZ1=[]
    uvs3ZZZ2=[]
    uvs3ZZZ3=[]
    uvs3ZZZ4=[]
    uvs3ZZZ5=[]
    uvs3ZZZ6=[]
    uvs2zzzzzzzzzzzzzz=[]
    uvs2zzzzzzzzzzzzz=[]
    uvs2zzzzzzzzzzzz=[]
    uvs2zzzzzzzzzzz=[]
    uvs2zzzzzzzzzz=[]
    uvs2zzzzzzzzz=[]
    uvs2zzzzzzzz=[]
    uvs2zzzzzzz=[]
    uvs2zzzzzz=[]
    uvs2zzzzz=[]
    uvs2zzzz=[]
    uvs2zzz=[]
    uvs2zz=[]
    uvs2z=[]
    uvs2y=[]
    uvs2x=[]
    uvs2w=[]
    uvs2v=[]
    uvs2u=[]
    uvs2t=[]
    uvs2s=[]
    uvs2r=[]
    uvs2q=[]
    uvs2p=[]
    uvs2o=[]
    uvs2n=[]
    uvs2m=[]
    uvs2l=[]
    uvs2k=[]
    uvs2j=[]
    uvs2i=[]
    uvs2h=[]
    uvs2g=[]
    uvs2f=[]
    uvs2e=[]
    uvs2d=[]
    uvs2c=[]
    uvs2b=[]
    uvs2a=[]
    uvs2apt2=[]
    uvs2=[]
    normals2=[]
    normals2a=[]
    normals2b=[]

    #fad2=-3
    #fbd2=-2
    #fcd2=-1

    fad6=-1
    fbd6=0
    fcd6=1
    fdd7=2
    fed7=3
    ffd7=4

    fad10aa=-1
    fbd10aa=0
    fcd10aa=1



    fad10=-7
    fbd10=-6
    fcd10=-5
    fad11=-6
    fbd11=-5
    fcd11=-4
    fad12=-5
    fbd12=-4
    fcd12=-3
    fad13=-4
    fbd13=-3
    fcd13=-2
    fad14=-3
    fbd14=-2
    fcd14=-1

    fad15=-8
    fbd15=-7
    fcd15=-6
    fad16=-7
    fbd16=-6
    fcd16=-5
    fad17=-6
    fbd17=-5
    fcd17=-4
    fad18=-5
    fbd18=-4
    fcd18=-3
    fad19=-4
    fbd19=-3
    fcd19=-2
    fad20=-3
    fbd20=-2
    fcd20=-1


    fad21=-9
    fbd21=-8
    fcd21=-7
    fad22=-8
    fbd22=-7
    fcd22=-6
    fad23=-7
    fbd23=-6
    fcd23=-5
    fad24=-6
    fbd24=-5
    fcd24=-4
    fad25=-5
    fbd25=-4
    fcd25=-3
    fad26=-4
    fbd26=-3
    fcd26=-2
    fad27=-3
    fbd27=-2
    fcd27=-1

    fad28=-10
    fbd28=-9
    fcd28=-8
    fad29=-9
    fbd29=-8
    fcd29=-7
    fad30=-8
    fbd30=-7
    fcd30=-6
    fad31=-7
    fbd31=-6
    fcd31=-5
    fad32=-6
    fbd32=-5
    fcd32=-4
    fad33=-5
    fbd33=-4
    fcd33=-3
    fad34=-4
    fbd34=-3
    fcd34=-2
    fad35=-3
    fbd35=-2
    fcd35=-1


    fad36=-11
    fbd36=-10
    fcd36=-9
    fad37=-10
    fbd37=-9
    fcd37=-8
    fad38=-9
    fbd38=-8
    fcd38=-7
    fad39=-8
    fbd39=-7
    fcd39=-6
    fad40=-7
    fbd40=-6
    fcd40=-5
    fad41=-6
    fbd41=-5
    fcd41=-4
    fad42=-5
    fbd42=-4
    fcd42=-3
    fad43=-4
    fbd43=-3
    fcd43=-2
    fad44=-3
    fbd44=-2
    fcd44=-1

    fad45=-12
    fbd45=-11
    fcd45=-10
    fad46=-11
    fbd46=-10
    fcd46=-9
    fad47=-10
    fbd47=-9
    fcd47=-8
    fad48=-9
    fbd48=-8
    fcd48=-7
    fad49=-8
    fbd49=-7
    fcd49=-6
    fad50=-7
    fbd50=-6
    fcd50=-5
    fad51=-6
    fbd51=-5
    fcd51=-4
    fad52=-5
    fbd52=-4
    fcd52=-3
    fad53=-4
    fbd53=-3
    fcd53=-2
    fad54=-3
    fbd54=-2
    fcd54=-1

    fad55=-13
    fbd55=-12
    fcd55=-11
    fad56=-12
    fbd56=-11
    fcd56=-10
    fad57=-11
    fbd57=-10
    fcd57=-9
    fad58=-10
    fbd58=-9
    fcd58=-8
    fad59=-9
    fbd59=-8
    fcd59=-7
    fad60=-8
    fbd60=-7
    fcd60=-6
    fad61=-7
    fbd61=-6
    fcd61=-5
    fad62=-6
    fbd62=-5
    fcd62=-4
    fad63=-5
    fbd63=-4
    fcd63=-3
    fad64=-4
    fbd64=-3
    fcd64=-2
    fad65=-3
    fbd65=-2
    fcd65=-1

    fad66=-14
    fbd66=-13
    fcd66=-12
    fad67=-13
    fbd67=-12
    fcd67=-11
    fad68=-12
    fbd68=-11
    fcd68=-10
    fad69=-11
    fbd69=-10
    fcd69=-9
    fad70=-10
    fbd70=-9
    fcd70=-8
    fad71=-9
    fbd71=-8
    fcd71=-7
    fad72=-8
    fbd72=-7
    fcd72=-6
    fad73=-7
    fbd73=-6
    fcd73=-5
    fad74=-6
    fbd74=-5
    fcd74=-4
    fad75=-5
    fbd75=-4
    fcd75=-3
    fad76=-4
    fbd76=-3
    fcd76=-2
    fad77=-3
    fbd77=-2
    fcd77=-1

    fad78=-15
    fbd78=-14
    fcd78=-13
    fad79=-14
    fbd79=-13
    fcd79=-12
    fad80=-13
    fbd80=-12
    fcd80=-11
    fad81=-12
    fbd81=-11
    fcd81=-10
    fad82=-11
    fbd82=-10
    fcd82=-9
    fad83=-10
    fbd83=-9
    fcd83=-8
    fad84=-9
    fbd84=-8
    fcd84=-7
    fad85=-8
    fbd85=-7
    fcd85=-6
    fad86=-7
    fbd86=-6
    fcd86=-5
    fad87=-6
    fbd87=-5
    fcd87=-4
    fad88=-5
    fbd88=-4
    fcd88=-3
    fad89=-4
    fbd89=-3
    fcd89=-2
    fad90=-3
    fbd90=-2
    fcd90=-1

    fad91=-16
    fbd91=-15
    fcd91=-14
    fad92=-15
    fbd92=-14
    fcd92=-13
    fad93=-14
    fbd93=-13
    fcd93=-12
    fad94=-13
    fbd94=-12
    fcd94=-11
    fad95=-12
    fbd95=-11
    fcd95=-10
    fad96=-11
    fbd96=-10
    fcd96=-9
    fad97=-10
    fbd97=-9
    fcd97=-8
    fad98=-9
    fbd98=-8
    fcd98=-7
    fad99=-8
    fbd99=-7
    fcd99=-6
    fad100=-7
    fbd100=-6
    fcd100=-5
    fad101=-6
    fbd101=-5
    fcd101=-4
    fad102=-5
    fbd102=-4
    fcd102=-3
    fad103=-4
    fbd103=-3
    fcd103=-2
    fad104=-3
    fbd104=-2
    fcd104=-1

    fad105=-17
    fbd105=-16
    fcd105=-15
    fad106=-16
    fbd106=-15
    fcd106=-14
    fad107=-15
    fbd107=-14
    fcd107=-13
    fad108=-14
    fbd108=-13
    fcd108=-12
    fad109=-13
    fbd109=-12
    fcd109=-11
    fad110=-12
    fbd110=-11
    fcd110=-10
    fad111=-11
    fbd111=-10
    fcd111=-9
    fad112=-10
    fbd112=-9
    fcd112=-8
    fad113=-9
    fbd113=-8
    fcd113=-7
    fad114=-8
    fbd114=-7
    fcd114=-6
    fad115=-7
    fbd115=-6
    fcd115=-5
    fad116=-6
    fbd116=-5
    fcd116=-4
    fad117=-5
    fbd117=-4
    fcd117=-3
    fad118=-4
    fbd118=-3
    fcd118=-2
    fad119=-3
    fbd119=-2
    fcd119=-1


    fad120=-18
    fbd120=-17
    fcd120=-16
    fad121=-17
    fbd121=-16
    fcd121=-15
    fad122=-16
    fbd122=-15
    fcd122=-14
    fad123=-15
    fbd123=-14
    fcd123=-13
    fad124=-14
    fbd124=-13
    fcd124=-12
    fad125=-13
    fbd125=-12
    fcd125=-11
    fad126=-12
    fbd126=-11
    fcd126=-10
    fad127=-11
    fbd127=-10
    fcd127=-9
    fad128=-10
    fbd128=-9
    fcd128=-8
    fad129=-9
    fbd129=-8
    fcd129=-7
    fad130=-8
    fbd130=-7
    fcd130=-6
    fad131=-7
    fbd131=-6
    fcd131=-5
    fad132=-6
    fbd132=-5
    fcd132=-4
    fad133=-5
    fbd133=-4
    fcd133=-3
    fad134=-4
    fbd134=-3
    fcd134=-2
    fad135=-3
    fbd135=-2
    fcd135=-1


    fad136=-19
    fbd136=-18
    fcd136=-17
    fad137=-18
    fbd137=-17
    fcd137=-16
    fad138=-17
    fbd138=-16
    fcd138=-15
    fad139=-16
    fbd139=-15
    fcd139=-14
    fad140=-15
    fbd140=-14
    fcd140=-13
    fad141=-14
    fbd141=-13
    fcd141=-12
    fad142=-13
    fbd142=-12
    fcd142=-11
    fad143=-12
    fbd143=-11
    fcd143=-10
    fad144=-11
    fbd144=-10
    fcd144=-9
    fad145=-10
    fbd145=-9
    fcd145=-8
    fad146=-9
    fbd146=-8
    fcd146=-7
    fad147=-8
    fbd147=-7
    fcd147=-6
    fad148=-7
    fbd148=-6
    fcd148=-5
    fad149=-6
    fbd149=-5
    fcd149=-4
    fad150=-5
    fbd150=-4
    fcd150=-3
    fad151=-4
    fbd151=-3
    fcd151=-2
    fad152=-3
    fbd152=-2
    fcd152=-1

    fad153=-20
    fbd153=-19
    fcd153=-18
    fad154=-19
    fbd154=-18
    fcd154=-17
    fad155=-18
    fbd155=-17
    fcd155=-16
    fad156=-17
    fbd156=-16
    fcd156=-15
    fad157=-16
    fbd157=-15
    fcd157=-14
    fad158=-15
    fbd158=-14
    fcd158=-13
    fad159=-14
    fbd159=-13
    fcd159=-12
    fad160=-13
    fbd160=-12
    fcd160=-11
    fad161=-12
    fbd161=-11
    fcd161=-10
    fad162=-11
    fbd162=-10
    fcd162=-9
    fad163=-10
    fbd163=-9
    fcd163=-8
    fad164=-9
    fbd164=-8
    fcd164=-7
    fad165=-8
    fbd165=-7
    fcd165=-6
    fad166=-7
    fbd166=-6
    fcd166=-5
    fad167=-6
    fbd167=-5
    fcd167=-4
    fad168=-5
    fbd168=-4
    fcd168=-3
    fad169=-4
    fbd169=-3
    fcd169=-2
    fad170=-3
    fbd170=-2
    fcd170=-1


    fad171=-21
    fbd171=-20
    fcd171=-19
    fad172=-20
    fbd172=-19
    fcd172=-18
    fad173=-19
    fbd173=-18
    fcd173=-17
    fad174=-18
    fbd174=-17
    fcd174=-16
    fad175=-17
    fbd175=-16
    fcd175=-15
    fad176=-16
    fbd176=-15
    fcd176=-14
    fad177=-15
    fbd177=-14
    fcd177=-13
    fad178=-14
    fbd178=-13
    fcd178=-12
    fad179=-13
    fbd179=-12
    fcd179=-11
    fad180=-12
    fbd180=-11
    fcd180=-10
    fad181=-11
    fbd181=-10
    fcd181=-9
    fad182=-10
    fbd182=-9
    fcd182=-8
    fad183=-9
    fbd183=-8
    fcd183=-7
    fad184=-8
    fbd184=-7
    fcd184=-6
    fad185=-7
    fbd185=-6
    fcd185=-5
    fad186=-6
    fbd186=-5
    fcd186=-4
    fad187=-5
    fbd187=-4
    fcd187=-3
    fad188=-4
    fbd188=-3
    fcd188=-2
    fad189=-3
    fbd189=-2
    fcd189=-1


    fad190=-22
    fbd190=-21
    fcd190=-20
    fad191=-21
    fbd191=-20
    fcd191=-19
    fad192=-20
    fbd192=-19
    fcd192=-18
    fad193=-19
    fbd193=-18
    fcd193=-17
    fad194=-18
    fbd194=-17
    fcd194=-16
    fad195=-17
    fbd195=-16
    fcd195=-15
    fad196=-16
    fbd196=-15
    fcd196=-14
    fad197=-15
    fbd197=-14
    fcd197=-13
    fad198=-14
    fbd198=-13
    fcd198=-12
    fad199=-13
    fbd199=-12
    fcd199=-11
    fad200=-12
    fbd200=-11
    fcd200=-10
    fad201=-11
    fbd201=-10
    fcd201=-9
    fad202=-10
    fbd202=-9
    fcd202=-8
    fad203=-9
    fbd203=-8
    fcd203=-7
    fad204=-8
    fbd204=-7
    fcd204=-6
    fad205=-7
    fbd205=-6
    fcd205=-5
    fad206=-6
    fbd206=-5
    fcd206=-4
    fad207=-5
    fbd207=-4
    fcd207=-3
    fad208=-4
    fbd208=-3
    fcd208=-2
    fad209=-3
    fbd209=-2
    fcd209=-1

    fad210=-23
    fbd210=-22
    fcd210=-21
    fad211=-22
    fbd211=-21
    fcd211=-20
    fad212=-21
    fbd212=-20
    fcd212=-19
    fad213=-20
    fbd213=-19
    fcd213=-18
    fad214=-19
    fbd214=-18
    fcd214=-17
    fad215=-18
    fbd215=-17
    fcd215=-16
    fad216=-17
    fbd216=-16
    fcd216=-15
    fad217=-16
    fbd217=-15
    fcd217=-14
    fad218=-15
    fbd218=-14
    fcd218=-13
    fad219=-14
    fbd219=-13
    fcd219=-12
    fad220=-13
    fbd220=-12
    fcd220=-11
    fad221=-12
    fbd221=-11
    fcd221=-10
    fad222=-11
    fbd222=-10
    fcd222=-9
    fad223=-10
    fbd223=-9
    fcd223=-8
    fad224=-9
    fbd224=-8
    fcd224=-7
    fad225=-8
    fbd225=-7
    fcd225=-6
    fad226=-7
    fbd226=-6
    fcd226=-5
    fad227=-6
    fbd227=-5
    fcd227=-4
    fad228=-5
    fbd228=-4
    fcd228=-3
    fad229=-4
    fbd229=-3
    fcd229=-2
    fad230=-3
    fbd230=-2
    fcd230=-1



    fad231=-24
    fbd231=-23
    fcd231=-22
    fad232=-23
    fbd232=-22
    fcd232=-21
    fad233=-22
    fbd233=-21
    fcd233=-20
    fad234=-21
    fbd234=-20
    fcd234=-19
    fad235=-20
    fbd235=-19
    fcd235=-18
    fad236=-19
    fbd236=-18
    fcd236=-17
    fad237=-18
    fbd237=-17
    fcd237=-16
    fad238=-17
    fbd238=-16
    fcd238=-15
    fad239=-16
    fbd239=-15
    fcd239=-14
    fad240=-15
    fbd240=-14
    fcd240=-13
    fad241=-14
    fbd241=-13
    fcd241=-12
    fad242=-13
    fbd242=-12
    fcd242=-11
    fad243=-12
    fbd243=-11
    fcd243=-10
    fad244=-11
    fbd244=-10
    fcd244=-9
    fad245=-10
    fbd245=-9
    fcd245=-8
    fad246=-9
    fbd246=-8
    fcd246=-7
    fad247=-8
    fbd247=-7
    fcd247=-6
    fad248=-7
    fbd248=-6
    fcd248=-5
    fad249=-6
    fbd249=-5
    fcd249=-4
    fad250=-5
    fbd250=-4
    fcd250=-3
    fad251=-4
    fbd251=-3
    fcd251=-2
    fad252=-3
    fbd252=-2
    fcd252=-1

    fad253=-25
    fbd253=-24
    fcd253=-23
    fad254=-24
    fbd254=-23
    fcd254=-22
    fad255=-23
    fbd255=-22
    fcd255=-21
    fad256=-22
    fbd256=-21
    fcd256=-20
    fad257=-21
    fbd257=-20
    fcd257=-19
    fad258=-20
    fbd258=-19
    fcd258=-18
    fad259=-19
    fbd259=-18
    fcd259=-17
    fad260=-18
    fbd260=-17
    fcd260=-16
    fad261=-17
    fbd261=-16
    fcd261=-15
    fad262=-16
    fbd262=-15
    fcd262=-14
    fad263=-15
    fbd263=-14
    fcd263=-13
    fad264=-14
    fbd264=-13
    fcd264=-12
    fad265=-13
    fbd265=-12
    fcd265=-11
    fad266=-12
    fbd266=-11
    fcd266=-10
    fad267=-11
    fbd267=-10
    fcd267=-9
    fad268=-10
    fbd268=-9
    fcd268=-8
    fad269=-9
    fbd269=-8
    fcd269=-7
    fad270=-8
    fbd270=-7
    fcd270=-6
    fad271=-7
    fbd271=-6
    fcd271=-5
    fad272=-6
    fbd272=-5
    fcd272=-4
    fad273=-5
    fbd273=-4
    fcd273=-3
    fad274=-4
    fbd274=-3
    fcd274=-2
    fad275=-3
    fbd275=-2
    fcd275=-1

    fad276=-26
    fbd276=-25
    fcd276=-24
    fad277=-25
    fbd277=-24
    fcd277=-23
    fad278=-24
    fbd278=-23
    fcd278=-22
    fad279=-23
    fbd279=-22
    fcd279=-21
    fad280=-22
    fbd280=-21
    fcd280=-20
    fad281=-21
    fbd281=-20
    fcd281=-19
    fad282=-20
    fbd282=-19
    fcd282=-18
    fad283=-19
    fbd283=-18
    fcd283=-17
    fad284=-18
    fbd284=-17
    fcd284=-16
    fad285=-17
    fbd285=-16
    fcd285=-15
    fad286=-16
    fbd286=-15
    fcd286=-14
    fad287=-15
    fbd287=-14
    fcd287=-13
    fad288=-14
    fbd288=-13
    fcd288=-12
    fad289=-13
    fbd289=-12
    fcd289=-11
    fad290=-12
    fbd290=-11
    fcd290=-10
    fad291=-11
    fbd291=-10
    fcd291=-9
    fad292=-10
    fbd292=-9
    fcd292=-8
    fad293=-9
    fbd293=-8
    fcd293=-7
    fad294=-8
    fbd294=-7
    fcd294=-6
    fad295=-7
    fbd295=-6
    fcd295=-5
    fad296=-6
    fbd296=-5
    fcd296=-4
    fad297=-5
    fbd297=-4
    fcd297=-3
    fad298=-4
    fbd298=-3
    fcd298=-2
    fad299=-3
    fbd299=-2
    fcd299=-1

    fad300=-27
    fbd300=-26
    fcd300=-25
    fad301=-26
    fbd301=-25
    fcd301=-24
    fad302=-25
    fbd302=-24
    fcd302=-23
    fad303=-24
    fbd303=-23
    fcd303=-22
    fad304=-23
    fbd304=-22
    fcd304=-21
    fad305=-22
    fbd305=-21
    fcd305=-20
    fad306=-21
    fbd306=-20
    fcd306=-19
    fad307=-20
    fbd307=-19
    fcd307=-18
    fad308=-19
    fbd308=-18
    fcd308=-17
    fad309=-18
    fbd309=-17
    fcd309=-16
    fad310=-17
    fbd310=-16
    fcd310=-15
    fad311=-16
    fbd311=-15
    fcd311=-14
    fad312=-15
    fbd312=-14
    fcd312=-13
    fad313=-14
    fbd313=-13
    fcd313=-12
    fad314=-13
    fbd314=-12
    fcd314=-11
    fad315=-12
    fbd315=-11
    fcd315=-10
    fad316=-11
    fbd316=-10
    fcd316=-9
    fad317=-10
    fbd317=-9
    fcd317=-8
    fad318=-9
    fbd318=-8
    fcd318=-7
    fad319=-8
    fbd319=-7
    fcd319=-6
    fad320=-7
    fbd320=-6
    fcd320=-5
    fad321=-6
    fbd321=-5
    fcd321=-4
    fad322=-5
    fbd322=-4
    fcd322=-3
    fad323=-4
    fbd323=-3
    fcd323=-2
    fad324=-3
    fbd324=-2
    fcd324=-1

    fad325=-28
    fbd325=-27
    fcd325=-26
    fad326=-27
    fbd326=-26
    fcd326=-25
    fad327=-26
    fbd327=-25
    fcd327=-24
    fad328=-25
    fbd328=-24
    fcd328=-23
    fad329=-24
    fbd329=-23
    fcd329=-22
    fad330=-23
    fbd330=-22
    fcd330=-21
    fad331=-22
    fbd331=-21
    fcd331=-20
    fad332=-21
    fbd332=-20
    fcd332=-19
    fad333=-20
    fbd333=-19
    fcd333=-18
    fad334=-19
    fbd334=-18
    fcd334=-17
    fad335=-18
    fbd335=-17
    fcd335=-16
    fad336=-17
    fbd336=-16
    fcd336=-15
    fad337=-16
    fbd337=-15
    fcd337=-14
    fad338=-15
    fbd338=-14
    fcd338=-13
    fad339=-14
    fbd339=-13
    fcd339=-12
    fad340=-13
    fbd340=-12
    fcd340=-11
    fad341=-12
    fbd341=-11
    fcd341=-10
    fad342=-11
    fbd342=-10
    fcd342=-9
    fad343=-10
    fbd343=-9
    fcd343=-8
    fad344=-9
    fbd344=-8
    fcd344=-7
    fad345=-8
    fbd345=-7
    fcd345=-6
    fad346=-7
    fbd346=-6
    fcd346=-5
    fad347=-6
    fbd347=-5
    fcd347=-4
    fad348=-5
    fbd348=-4
    fcd348=-3
    fad349=-4
    fbd349=-3
    fcd349=-2
    fad350=-3
    fbd350=-2
    fcd350=-1

    fad351=-29
    fbd351=-28
    fcd351=-27
    fad352=-28
    fbd352=-27
    fcd352=-26
    fad353=-27
    fbd353=-26
    fcd353=-25
    fad354=-26
    fbd354=-25
    fcd354=-24
    fad355=-25
    fbd355=-24
    fcd355=-23
    fad356=-24
    fbd356=-23
    fcd356=-22
    fad357=-23
    fbd357=-22
    fcd357=-21
    fad358=-22
    fbd358=-21
    fcd358=-20
    fad359=-21
    fbd359=-20
    fcd359=-19
    fad360=-20
    fbd360=-19
    fcd360=-18
    fad361=-19
    fbd361=-18
    fcd361=-17
    fad362=-18
    fbd362=-17
    fcd362=-16
    fad363=-17
    fbd363=-16
    fcd363=-15
    fad364=-16
    fbd364=-15
    fcd364=-14
    fad365=-15
    fbd365=-14
    fcd365=-13
    fad366=-14
    fbd366=-13
    fcd366=-12
    fad367=-13
    fbd367=-12
    fcd367=-11
    fad368=-12
    fbd368=-11
    fcd368=-10
    fad369=-11
    fbd369=-10
    fcd369=-9
    fad370=-10
    fbd370=-9
    fcd370=-8
    fad371=-9
    fbd371=-8
    fcd371=-7
    fad372=-8
    fbd372=-7
    fcd372=-6
    fad373=-7
    fbd373=-6
    fcd373=-5
    fad374=-6
    fbd374=-5
    fcd374=-4
    fad375=-5
    fbd375=-4
    fcd375=-3
    fad376=-4
    fbd376=-3
    fcd376=-2
    fad377=-3
    fbd377=-2
    fcd377=-1

    fad378=-30
    fbd378=-29
    fcd378=-28
    fad379=-29
    fbd379=-28
    fcd379=-27
    fad380=-28
    fbd380=-27
    fcd380=-26
    fad381=-27
    fbd381=-26
    fcd381=-25
    fad382=-26
    fbd382=-25
    fcd382=-24
    fad383=-25
    fbd383=-24
    fcd383=-23
    fad384=-24
    fbd384=-23
    fcd384=-22
    fad385=-23
    fbd385=-22
    fcd385=-21
    fad386=-22
    fbd386=-21
    fcd386=-20
    fad387=-21
    fbd387=-20
    fcd387=-19
    fad388=-20
    fbd388=-19
    fcd388=-18
    fad389=-19
    fbd389=-18
    fcd389=-17
    fad390=-18
    fbd390=-17
    fcd390=-16
    fad391=-17
    fbd391=-16
    fcd391=-15
    fad392=-16
    fbd392=-15
    fcd392=-14
    fad393=-15
    fbd393=-14
    fcd393=-13
    fad394=-14
    fbd394=-13
    fcd394=-12
    fad395=-13
    fbd395=-12
    fcd395=-11
    fad396=-12
    fbd396=-11
    fcd396=-10
    fad397=-11
    fbd397=-10
    fcd397=-9
    fad398=-10
    fbd398=-9
    fcd398=-8
    fad399=-9
    fbd399=-8
    fcd399=-7
    fad400=-8
    fbd400=-7
    fcd400=-6
    fad401=-7
    fbd401=-6
    fcd401=-5
    fad402=-6
    fbd402=-5
    fcd402=-4
    fad403=-5
    fbd403=-4
    fcd403=-3
    fad404=-4
    fbd404=-3
    fcd404=-2
    fad405=-3
    fbd405=-2
    fcd405=-1

    fad406=-31
    fbd406=-30
    fcd406=-29
    fad407=-30
    fbd407=-29
    fcd407=-28
    fad408=-29
    fbd408=-28
    fcd408=-27
    fad409=-28
    fbd409=-27
    fcd409=-26
    fad410=-27
    fbd410=-26
    fcd410=-25
    fad411=-26
    fbd411=-25
    fcd411=-24
    fad412=-25
    fbd412=-24
    fcd412=-23
    fad413=-24
    fbd413=-23
    fcd413=-22
    fad414=-23
    fbd414=-22
    fcd414=-21
    fad415=-22
    fbd415=-21
    fcd415=-20
    fad416=-21
    fbd416=-20
    fcd416=-19
    fad417=-20
    fbd417=-19
    fcd417=-18
    fad418=-19
    fbd418=-18
    fcd418=-17
    fad419=-18
    fbd419=-17
    fcd419=-16
    fad420=-17
    fbd420=-16
    fcd420=-15
    fad421=-16
    fbd421=-15
    fcd421=-14
    fad422=-15
    fbd422=-14
    fcd422=-13
    fad423=-14
    fbd423=-13
    fcd423=-12
    fad424=-13
    fbd424=-12
    fcd424=-11
    fad425=-10
    fbd425=-11
    fcd425=-10
    fad426=-11
    fbd426=-10
    fcd426=-9
    fad427=-10
    fbd427=-9
    fcd427=-8
    fad428=-9
    fbd428=-8
    fcd428=-7
    fad429=-8
    fbd429=-7
    fcd429=-6
    fad430=-7
    fbd430=-6
    fcd430=-5
    fad431=-6
    fbd431=-5
    fcd431=-4
    fad432=-5
    fbd432=-4
    fcd432=-3
    fad433=-4
    fbd433=-3
    fcd433=-2
    fad434=-3
    fbd434=-2
    fcd434=-1

    fad435=-32
    fbd435=-31
    fcd435=-30
    fad436=-31
    fbd436=-30
    fcd436=-29
    fad437=-30
    fbd437=-29
    fcd437=-28
    fad438=-29
    fbd438=-28
    fcd438=-27
    fad439=-28
    fbd439=-27
    fcd439=-26
    fad440=-27
    fbd440=-26
    fcd440=-25
    fad441=-26
    fbd441=-25
    fcd441=-24
    fad442=-25
    fbd442=-24
    fcd442=-23
    fad443=-24
    fbd443=-23
    fcd443=-22
    fad444=-23
    fbd444=-22
    fcd444=-21
    fad445=-22
    fbd445=-21
    fcd445=-20
    fad446=-21
    fbd446=-20
    fcd446=-19
    fad447=-20
    fbd447=-19
    fcd447=-18
    fad448=-19
    fbd448=-18
    fcd448=-17
    fad449=-18
    fbd449=-17
    fcd449=-16
    fad450=-17
    fbd450=-16
    fcd450=-15
    fad451=-16
    fbd451=-15
    fcd451=-14
    fad452=-15
    fbd452=-14
    fcd452=-13
    fad453=-14
    fbd453=-13
    fcd453=-12
    fad454=-13
    fbd454=-12
    fcd454=-11
    fad455=-12
    fbd455=-11
    fcd455=-10
    fad456=-11
    fbd456=-10
    fcd456=-9
    fad457=-10
    fbd457=-9
    fcd457=-8
    fad458=-9
    fbd458=-8
    fcd458=-7
    fad459=-8
    fbd459=-7
    fcd459=-6
    fad460=-7
    fbd460=-6
    fcd460=-5
    fad461=-6
    fbd461=-5
    fcd461=-4
    fad462=-5
    fbd462=-4
    fcd462=-3
    fad463=-4
    fbd463=-3
    fcd463=-2
    fad464=-3
    fbd464=-2
    fcd464=-1

    fad465=-33
    fbd465=-32
    fcd465=-31
    fad466=-32
    fbd466=-31
    fcd466=-30
    fad467=-31
    fbd467=-30
    fcd467=-29
    fad468=-30
    fbd468=-29
    fcd468=-28
    fad469=-29
    fbd469=-28
    fcd469=-27
    fad470=-28
    fbd470=-27
    fcd470=-26
    fad471=-27
    fbd471=-26
    fcd471=-25
    fad472=-26
    fbd472=-25
    fcd472=-24
    fad473=-25
    fbd473=-24
    fcd473=-23
    fad474=-24
    fbd474=-23
    fcd474=-22
    fad475=-23
    fbd475=-22
    fcd475=-21
    fad476=-22
    fbd476=-21
    fcd476=-20
    fad477=-21
    fbd477=-20
    fcd477=-19
    fad478=-20
    fbd478=-19
    fcd478=-18
    fad479=-19
    fbd479=-18
    fcd479=-17
    fad480=-18
    fbd480=-17
    fcd480=-16
    fad481=-17
    fbd481=-16
    fcd481=-15
    fad482=-16
    fbd482=-15
    fcd482=-14
    fad483=-15
    fbd483=-14
    fcd483=-13
    fad484=-14
    fbd484=-13
    fcd484=-12
    fad485=-13
    fbd485=-12
    fcd485=-11
    fad486=-12
    fbd486=-11
    fcd486=-10
    fad487=-11
    fbd487=-10
    fcd487=-9
    fad488=-10
    fbd488=-9
    fcd488=-8
    fad489=-9
    fbd489=-8
    fcd489=-7
    fad490=-8
    fbd490=-7
    fcd490=-6
    fad491=-7
    fbd491=-6
    fcd491=-5
    fad492=-6
    fbd492=-5
    fcd492=-4
    fad493=-5
    fbd493=-4
    fcd493=-3
    fad494=-4
    fbd494=-3
    fcd494=-2
    fad495=-3
    fbd495=-2
    fcd495=-1

    fad496=-34
    fbd496=-33
    fcd496=-32
    fad497=-33
    fbd497=-32
    fcd497=-31
    fad498=-32
    fbd498=-31
    fcd498=-30
    fad499=-31
    fbd499=-30
    fcd499=-29
    fad500=-30
    fbd500=-29
    fcd500=-28
    fad501=-29
    fbd501=-28
    fcd501=-27
    fad502=-28
    fbd502=-27
    fcd502=-26
    fad503=-27
    fbd503=-26
    fcd503=-25
    fad504=-26
    fbd504=-25
    fcd504=-24
    fad505=-25
    fbd505=-24
    fcd505=-23
    fad506=-24
    fbd506=-23
    fcd506=-22
    fad507=-23
    fbd507=-22
    fcd507=-21
    fad508=-22
    fbd508=-21
    fcd508=-20
    fad509=-21
    fbd509=-20
    fcd509=-19
    fad510=-20
    fbd510=-19
    fcd510=-18
    fad511=-19
    fbd511=-18
    fcd511=-17
    fad512=-18
    fbd512=-17
    fcd512=-16
    fad513=-17
    fbd513=-16
    fcd513=-15
    fad514=-16
    fbd514=-15
    fcd514=-14
    fad515=-15
    fbd515=-14
    fcd515=-13
    fad516=-14
    fbd516=-13
    fcd516=-12
    fad517=-13
    fbd517=-12
    fcd517=-11
    fad518=-12
    fbd518=-11
    fcd518=-10
    fad519=-11
    fbd519=-10
    fcd519=-9
    fad520=-10
    fbd520=-9
    fcd520=-8
    fad521=-9
    fbd521=-8
    fcd521=-7
    fad522=-8
    fbd522=-7
    fcd522=-6
    fad523=-7
    fbd523=-6
    fcd523=-5
    fad524=-6
    fbd524=-5
    fcd524=-4
    fad525=-5
    fbd525=-4
    fcd525=-3
    fad526=-4
    fbd526=-3
    fcd526=-2
    fad527=-3
    fbd527=-2
    fcd527=-1

    fad528=-35
    fbd528=-34
    fcd528=-33
    fad529=-34
    fbd529=-33
    fcd529=-32
    fad530=-33
    fbd530=-32
    fcd530=-31
    fad531=-32
    fbd531=-31
    fcd531=-30
    fad532=-31
    fbd532=-30
    fcd532=-29
    fad533=-30
    fbd533=-29
    fcd533=-28
    fad534=-29
    fbd534=-28
    fcd534=-27
    fad535=-28
    fbd535=-27
    fcd535=-26
    fad536=-27
    fbd536=-26
    fcd536=-25
    fad537=-26
    fbd537=-25
    fcd537=-24
    fad538=-25
    fbd538=-24
    fcd538=-23
    fad539=-24
    fbd539=-23
    fcd539=-22
    fad540=-23
    fbd540=-22
    fcd540=-21
    fad541=-22
    fbd541=-21
    fcd541=-20
    fad542=-21
    fbd542=-20
    fcd542=-19
    fad543=-20
    fbd543=-19
    fcd543=-18
    fad544=-19
    fbd544=-18
    fcd544=-17
    fad545=-18
    fbd545=-17
    fcd545=-16
    fad546=-17
    fbd546=-16
    fcd546=-15
    fad547=-16
    fbd547=-15
    fcd547=-14
    fad548=-15
    fbd548=-14
    fcd548=-13
    fad549=-14
    fbd549=-13
    fcd549=-12
    fad550=-13
    fbd550=-12
    fcd550=-11
    fad551=-12
    fbd551=-11
    fcd551=-10
    fad552=-11
    fbd552=-10
    fcd552=-9
    fad553=-10
    fbd553=-9
    fcd553=-8
    fad554=-9
    fbd554=-8
    fcd554=-7
    fad555=-8
    fbd555=-7
    fcd555=-6
    fad556=-7
    fbd556=-6
    fcd556=-5
    fad557=-6
    fbd557=-5
    fcd557=-4
    fad558=-5
    fbd558=-4
    fcd558=-3
    fad559=-4
    fbd559=-3
    fcd559=-2
    fad560=-3
    fbd560=-2
    fcd560=-1

    fad561=-36
    fbd561=-35
    fcd561=-34
    fad562=-35
    fbd562=-34
    fcd562=-33
    fad563=-34
    fbd563=-33
    fcd563=-32
    fad564=-33
    fbd564=-32
    fcd564=-31
    fad565=-32
    fbd565=-31
    fcd565=-30
    fad566=-31
    fbd566=-30
    fcd566=-29
    fad567=-30
    fbd567=-29
    fcd567=-28
    fad568=-29
    fbd568=-28
    fcd568=-27
    fad569=-28
    fbd569=-27
    fcd569=-26
    fad570=-27
    fbd570=-26
    fcd570=-25
    fad571=-26
    fbd571=-25
    fcd571=-24
    fad572=-25
    fbd572=-24
    fcd572=-23
    fad573=-24
    fbd573=-23
    fcd573=-22
    fad574=-23
    fbd574=-22
    fcd574=-21
    fad575=-22
    fbd575=-21
    fcd575=-20
    fad576=-21
    fbd576=-20
    fcd576=-19
    fad577=-20
    fbd577=-19
    fcd577=-18
    fad578=-19
    fbd578=-18
    fcd578=-17
    fad579=-18
    fbd579=-17
    fcd579=-16
    fad580=-17
    fbd580=-16
    fcd580=-15
    fad581=-16
    fbd581=-15
    fcd581=-14
    fad582=-15
    fbd582=-14
    fcd582=-13
    fad583=-14
    fbd583=-13
    fcd583=-12
    fad584=-13
    fbd584=-12
    fcd584=-11
    fad585=-12
    fbd585=-11
    fcd585=-10
    fad586=-11
    fbd586=-10
    fcd586=-9
    fad587=-10
    fbd587=-9
    fcd587=-8
    fad588=-9
    fbd588=-8
    fcd588=-7
    fad589=-8
    fbd589=-7
    fcd589=-6
    fad590=-7
    fbd590=-6
    fcd590=-5
    fad591=-6
    fbd591=-5
    fcd591=-4
    fad592=-5
    fbd592=-4
    fcd592=-3
    fad593=-4
    fbd593=-3
    fcd593=-2
    fad594=-3
    fbd594=-2
    fcd594=-1

    fad595=-37
    fbd595=-36
    fcd595=-35
    fad596=-36
    fbd596=-35
    fcd596=-34
    fad597=-35
    fbd597=-34
    fcd597=-33
    fad598=-34
    fbd598=-33
    fcd598=-32
    fad599=-33
    fbd599=-32
    fcd599=-31
    fad600=-32
    fbd600=-31
    fcd600=-30
    fad601=-31
    fbd601=-30
    fcd601=-29
    fad602=-30
    fbd602=-29
    fcd602=-28
    fad603=-29
    fbd603=-28
    fcd603=-27
    fad604=-28
    fbd604=-27
    fcd604=-26
    fad605=-27
    fbd605=-26
    fcd605=-25
    fad606=-26
    fbd606=-25
    fcd606=-24
    fad607=-25
    fbd607=-24
    fcd607=-23
    fad608=-24
    fbd608=-23
    fcd608=-22
    fad609=-23
    fbd609=-22
    fcd609=-21
    fad610=-22
    fbd610=-21
    fcd610=-20
    fad611=-21
    fbd611=-20
    fcd611=-19
    fad612=-20
    fbd612=-19
    fcd612=-18
    fad613=-19
    fbd613=-18
    fcd613=-17
    fad614=-18
    fbd614=-17
    fcd614=-16
    fad615=-17
    fbd615=-16
    fcd615=-15
    fad616=-16
    fbd616=-15
    fcd616=-14
    fad617=-15
    fbd617=-14
    fcd617=-13
    fad618=-14
    fbd618=-13
    fcd618=-12
    fad619=-13
    fbd619=-12
    fcd619=-11
    fad620=-12
    fbd620=-11
    fcd620=-10
    fad621=-11
    fbd621=-10
    fcd621=-9
    fad622=-10
    fbd622=-9
    fcd622=-8
    fad623=-9
    fbd623=-8
    fcd623=-7
    fad624=-8
    fbd624=-7
    fcd624=-6
    fad625=-7
    fbd625=-6
    fcd625=-5
    fad626=-6
    fbd626=-5
    fcd626=-4
    fad627=-5
    fbd627=-4
    fcd627=-3
    fad628=-4
    fbd628=-3
    fcd628=-2
    fad629=-3
    fbd629=-2
    fcd629=-1

    fad630=-38
    fbd630=-37
    fcd630=-36
    fad631=-37
    fbd631=-36
    fcd631=-35
    fad632=-36
    fbd632=-35
    fcd632=-34
    fad633=-35
    fbd633=-34
    fcd633=-33
    fad634=-34
    fbd634=-33
    fcd634=-32
    fad635=-33
    fbd635=-32
    fcd635=-31
    fad636=-32
    fbd636=-31
    fcd636=-30
    fad637=-31
    fbd637=-30
    fcd637=-29
    fad638=-30
    fbd638=-29
    fcd638=-28
    fad639=-29
    fbd639=-28
    fcd639=-27
    fad640=-28
    fbd640=-27
    fcd640=-26
    fad641=-27
    fbd641=-26
    fcd641=-25
    fad642=-26
    fbd642=-25
    fcd642=-24
    fad643=-25
    fbd643=-24
    fcd643=-23
    fad644=-24
    fbd644=-23
    fcd644=-22
    fad645=-23
    fbd645=-22
    fcd645=-21
    fad646=-22
    fbd646=-21
    fcd646=-20
    fad647=-21
    fbd647=-20
    fcd647=-19
    fad648=-20
    fbd648=-19
    fcd648=-18
    fad649=-19
    fbd649=-18
    fcd649=-17
    fad650=-18
    fbd650=-17
    fcd650=-16
    fad651=-17
    fbd651=-16
    fcd651=-15
    fad652=-16
    fbd652=-15
    fcd652=-14
    fad653=-15
    fbd653=-14
    fcd653=-13
    fad654=-14
    fbd654=-13
    fcd654=-12
    fad655=-13
    fbd655=-12
    fcd655=-11
    fad656=-12
    fbd656=-11
    fcd656=-10
    fad657=-11
    fbd657=-10
    fcd657=-9
    fad658=-10
    fbd658=-9
    fcd658=-8
    fad659=-9
    fbd659=-8
    fcd659=-7
    fad660=-8
    fbd660=-7
    fcd660=-6
    fad661=-7
    fbd661=-6
    fcd661=-5
    fad662=-6
    fbd662=-5
    fcd662=-4
    fad663=-5
    fbd663=-4
    fcd663=-3
    fad664=-4
    fbd664=-3
    fcd664=-2
    fad665=-3
    fbd665=-2
    fcd665=-1

    fad666=-39
    fbd666=-38
    fcd666=-37
    fad667=-38
    fbd667=-37
    fcd667=-36
    fad668=-37
    fbd668=-36
    fcd668=-35
    fad669=-36
    fbd669=-35
    fcd669=-34
    fad670=-35
    fbd670=-34
    fcd670=-33
    fad671=-34
    fbd671=-33
    fcd671=-32
    fad672=-33
    fbd672=-32
    fcd672=-31
    fad673=-32
    fbd673=-31
    fcd673=-30
    fad674=-31
    fbd674=-30
    fcd674=-29
    fad675=-30
    fbd675=-29
    fcd675=-28
    fad676=-29
    fbd676=-28
    fcd676=-27
    fad677=-28
    fbd677=-27
    fcd677=-26
    fad678=-27
    fbd678=-26
    fcd678=-25
    fad679=-26
    fbd679=-25
    fcd679=-24
    fad680=-25
    fbd680=-24
    fcd680=-23
    fad681=-24
    fbd681=-23
    fcd681=-22
    fad682=-23
    fbd682=-22
    fcd682=-21
    fad683=-22
    fbd683=-21
    fcd683=-20
    fad684=-21
    fbd684=-20
    fcd684=-19
    fad685=-20
    fbd685=-19
    fcd685=-18
    fad686=-19
    fbd686=-18
    fcd686=-17
    fad687=-18
    fbd687=-17
    fcd687=-16
    fad688=-17
    fbd688=-16
    fcd688=-15
    fad689=-16
    fbd689=-15
    fcd689=-14
    fad690=-15
    fbd690=-14
    fcd690=-13
    fad691=-14
    fbd691=-13
    fcd691=-12
    fad692=-13
    fbd692=-12
    fcd692=-11
    fad693=-12
    fbd693=-11
    fcd693=-10
    fad694=-11
    fbd694=-10
    fcd694=-9
    fad695=-10
    fbd695=-9
    fcd695=-8
    fad696=-9
    fbd696=-8
    fcd696=-7
    fad697=-8
    fbd697=-7
    fcd697=-6
    fad698=-7
    fbd698=-6
    fcd698=-5
    fad699=-6
    fbd699=-5
    fcd699=-4
    fad700=-5
    fbd700=-4
    fcd700=-3
    fad701=-4
    fbd701=-3
    fcd701=-2
    fad702=-3
    fbd702=-2
    fcd702=-1

    fad703=-40
    fbd703=-39
    fcd703=-38
    fad704=-39
    fbd704=-38
    fcd704=-37
    fad705=-38
    fbd705=-37
    fcd705=-36
    fad706=-37
    fbd706=-36
    fcd706=-35
    fad707=-36
    fbd707=-35
    fcd707=-34
    fad708=-35
    fbd708=-34
    fcd708=-33
    fad709=-34
    fbd709=-33
    fcd709=-32
    fad710=-33
    fbd710=-32
    fcd710=-31
    fad711=-32
    fbd711=-31
    fcd711=-30
    fad712=-31
    fbd712=-30
    fcd712=-29
    fad713=-30
    fbd713=-29
    fcd713=-28
    fad714=-29
    fbd714=-28
    fcd714=-27
    fad715=-28
    fbd715=-27
    fcd715=-26
    fad716=-27
    fbd716=-26
    fcd716=-25
    fad717=-26
    fbd717=-25
    fcd717=-24
    fad718=-25
    fbd718=-24
    fcd718=-23
    fad719=-24
    fbd719=-23
    fcd719=-22
    fad720=-23
    fbd720=-22
    fcd720=-21
    fad721=-22
    fbd721=-21
    fcd721=-20
    fad722=-21
    fbd722=-20
    fcd722=-19
    fad723=-20
    fbd723=-19
    fcd723=-18
    fad724=-19
    fbd724=-18
    fcd724=-17
    fad725=-18
    fbd725=-17
    fcd725=-16
    fad726=-17
    fbd726=-16
    fcd726=-15
    fad727=-16
    fbd727=-15
    fcd727=-14
    fad728=-15
    fbd728=-14
    fcd728=-13
    fad729=-14
    fbd729=-13
    fcd729=-12
    fad730=-13
    fbd730=-12
    fcd730=-11
    fad731=-12
    fbd731=-11
    fcd731=-10
    fad732=-11
    fbd732=-10
    fcd732=-9
    fad733=-10
    fbd733=-9
    fcd733=-8
    fad734=-9
    fbd734=-8
    fcd734=-7
    fad735=-8
    fbd735=-7
    fcd735=-6
    fad736=-7
    fbd736=-6
    fcd736=-5
    fad737=-6
    fbd737=-5
    fcd737=-4
    fad738=-5
    fbd738=-4
    fcd738=-3
    fad739=-4
    fbd739=-3
    fcd739=-2
    fad740=-3
    fbd740=-2
    fcd740=-1

    fad741=-41
    fbd741=-40
    fcd741=-39
    fad742=-40
    fbd742=-39
    fcd742=-38
    fad743=-39
    fbd743=-38
    fcd743=-37
    fad744=-38
    fbd744=-37
    fcd744=-36
    fad745=-37
    fbd745=-36
    fcd745=-35
    fad746=-36
    fbd746=-35
    fcd746=-34
    fad747=-35
    fbd747=-34
    fcd747=-33
    fad748=-34
    fbd748=-33
    fcd748=-32
    fad749=-33
    fbd749=-32
    fcd749=-31
    fad750=-32
    fbd750=-31
    fcd750=-30
    fad751=-31
    fbd751=-30
    fcd751=-29
    fad752=-30
    fbd752=-29
    fcd752=-28
    fad753=-29
    fbd753=-28
    fcd753=-27
    fad754=-28
    fbd754=-27
    fcd754=-26
    fad755=-27
    fbd755=-26
    fcd755=-25
    fad756=-26
    fbd756=-25
    fcd756=-24
    fad757=-25
    fbd757=-24
    fcd757=-23
    fad758=-24
    fbd758=-23
    fcd758=-22
    fad759=-23
    fbd759=-22
    fcd759=-21
    fad760=-22
    fbd760=-21
    fcd760=-20
    fad761=-21
    fbd761=-20
    fcd761=-19
    fad762=-20
    fbd762=-19
    fcd762=-18
    fad763=-19
    fbd763=-18
    fcd763=-17
    fad764=-18
    fbd764=-17
    fcd764=-16
    fad765=-17
    fbd765=-16
    fcd765=-15
    fad766=-16
    fbd766=-15
    fcd766=-14
    fad767=-15
    fbd767=-14
    fcd767=-13
    fad768=-14
    fbd768=-13
    fcd768=-12
    fad769=-13
    fbd769=-12
    fcd769=-11
    fad770=-12
    fbd770=-11
    fcd770=-10
    fad771=-11
    fbd771=-10
    fcd771=-9
    fad772=-10
    fbd772=-9
    fcd772=-8
    fad773=-9
    fbd773=-8
    fcd773=-7
    fad774=-8
    fbd774=-7
    fcd774=-6
    fad775=-7
    fbd775=-6
    fcd775=-5
    fad776=-6
    fbd776=-5
    fcd776=-4
    fad777=-5
    fbd777=-4
    fcd777=-3
    fad778=-4
    fbd778=-3
    fcd778=-2
    fad779=-3
    fbd779=-2
    fcd779=-1

    fad780=-42
    fbd780=-41
    fcd780=-40
    fad781=-41
    fbd781=-40
    fcd781=-39
    fad782=-40
    fbd782=-39
    fcd782=-38
    fad783=-39
    fbd783=-38
    fcd783=-37
    fad784=-38
    fbd784=-37
    fcd784=-36
    fad785=-37
    fbd785=-36
    fcd785=-35
    fad786=-36
    fbd786=-35
    fcd786=-34
    fad787=-35
    fbd787=-34
    fcd787=-33
    fad788=-34
    fbd788=-33
    fcd788=-32
    fad789=-33
    fbd789=-32
    fcd789=-31
    fad790=-32
    fbd790=-31
    fcd790=-30
    fad791=-31
    fbd791=-30
    fcd791=-29
    fad792=-30
    fbd792=-29
    fcd792=-28
    fad793=-29
    fbd793=-28
    fcd793=-27
    fad794=-28
    fbd794=-27
    fcd794=-26
    fad795=-27
    fbd795=-26
    fcd795=-25
    fad796=-26
    fbd796=-25
    fcd796=-24
    fad797=-25
    fbd797=-24
    fcd797=-23
    fad798=-24
    fbd798=-23
    fcd798=-22
    fad799=-23
    fbd799=-22
    fcd799=-21
    fad800=-22
    fbd800=-21
    fcd800=-20
    fad801=-21
    fbd801=-20
    fcd801=-19
    fad802=-20
    fbd802=-19
    fcd802=-18
    fad803=-19
    fbd803=-18
    fcd803=-17
    fad804=-18
    fbd804=-17
    fcd804=-16
    fad805=-17
    fbd805=-16
    fcd805=-15
    fad806=-16
    fbd806=-15
    fcd806=-14
    fad807=-15
    fbd807=-14
    fcd807=-13
    fad808=-14
    fbd808=-13
    fcd808=-12
    fad809=-13
    fbd809=-12
    fcd809=-11
    fad810=-12
    fbd810=-11
    fcd810=-10
    fad811=-11
    fbd811=-10
    fcd811=-9
    fad812=-10
    fbd812=-9
    fcd812=-8
    fad813=-9
    fbd813=-8
    fcd813=-7
    fad814=-8
    fbd814=-7
    fcd814=-6
    fad815=-7
    fbd815=-6
    fcd815=-5
    fad816=-6
    fbd816=-5
    fcd816=-4
    fad817=-5
    fbd817=-4
    fcd817=-3
    fad818=-4
    fbd818=-3
    fcd818=-2
    fad819=-3
    fbd819=-2
    fcd819=-1

    alp=[]
    alp2=[]

    vertices=[]
    faces=[]

    vertices_=[]
    faces_=[]

    #blend_vertices=[]

    #blend shape offset 0x13380001

    blendshapeinfos = {} # you don't have to use dictionarys if you want to it does work with lists
    #skininfos = {}

    #########################################
    
    boneIndex = -1

    texttures=[]

    bones_=[]

    bone_parentlist=[]

    matttListt = []

    materials=[]

    vertices3restoreA=[]
    faces3restoreA=[]

    texxxListt = []

    restoreFewFaceA=-2
    restoreFewFaceB=0
    restoreFewFaceC=1

    #this does not work when during importing the model and texture at the same time when i seek it back using enumerate with a function # not supporting textures because it will freeze blender

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
        if MaterialEntrySize1 == 144 or MaterialEntrySize1 == 148:
            f.seek(MaterialEntrySize1,0)
            for i in range(MaterialCount):
                matentrysizelist1 = unpack("<I", f.read(4))[0]
                matttListt.append([matentrysizelist1])
            for i, mxxxxx in enumerate(matttListt):
                f.seek(mxxxxx[0],0)
                f.seek(288,1)
                matFlg = unpack("<I", f.read(4))[0]
                RNDRSTREAMrs = unpack("<I", f.read(4))[0]
                f.seek(28,1)
                AnimatedRed = unpack("<I", f.read(4))[0]
                AnimatedGreen = unpack("<I", f.read(4))[0]
                AnimatedBlue = unpack("<I", f.read(4))[0]
                f.seek(4,1)
                matFlg2 = unpack("<I", f.read(4))[0]
                f.seek(4,1)
                VARIPTR = unpack("<I", f.read(4))[0]
                snext = unpack("<I", f.read(4))[0]
                slast = unpack("<I", f.read(4))[0]
                next1 = unpack("<I", f.read(4))[0]
                attrib = unpack("<f", f.read(4))[0]
                matFlg3 = unpack("<I", f.read(4))[0]
                ambientR = unpack("<f", f.read(4))[0]
                ambientG = unpack("<f", f.read(4))[0]
                ambientB = unpack("<f", f.read(4))[0]
                diffuseR = unpack("<f", f.read(4))[0]
                diffuseG = unpack("<f", f.read(4))[0]
                diffuseB = unpack("<f", f.read(4))[0]
                fx1 = unpack("<f", f.read(4))[0]
                fx2 = unpack("<f", f.read(4))[0]
                fx3 = unpack("<f", f.read(4))[0]
                fx4 = unpack("<f", f.read(4))[0]
                power = unpack("<f", f.read(4))[0]
                allpha = unpack("<f", f.read(4))[0]
                tid = unpack("<I", f.read(4))[0]
                mid = unpack("<I", f.read(4))[0]
                k = unpack("<H", f.read(2))[0]
                L = unpack("B", f.read(1))[0]
                uvanmmode = unpack("B", f.read(1))[0]
                du = unpack("<f", f.read(4))[0]
                dv = unpack("<f", f.read(4))[0]
                su = unpack("<f", f.read(4))[0]
                sv = unpack("<f", f.read(4))[0]
                multi_next = unpack("<I", f.read(4))[0]
                contt = unpack("B", f.read(1))[0]
                fxid = unpack("B", f.read(1))[0]
                specialid = unpack("B", f.read(1))[0]
                pad01 = unpack("B", f.read(1))[0]
                pad02 = unpack("B", f.read(1))[0]
                pad03 = unpack("B", f.read(1))[0]
                pad04 = unpack("B", f.read(1))[0]
                pad05 = unpack("B", f.read(1))[0]
                pad06 = unpack("B", f.read(1))[0]
                pad07 = unpack("B", f.read(1))[0]
                pad08 = unpack("B", f.read(1))[0]
                pad09 = unpack("B", f.read(1))[0]

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
                try:
                    ntbl_buffer.seek(name_offset)
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
            while f.tell() < len(Chunk):
                Chunks = f.read(4)
                if Chunks == b"\x03\x01\x00\x01":
                    f.seek(1,1)
                    value1 = unpack("B", f.read(1))[0]
                    vertexCount = unpack("B", f.read(1))[0]
                    flag2a = unpack("B", f.read(1))[0]
                    if flag2a == 0x6C:
                        if vertexCount == 0:
                            pass
                        elif vertexCount == 1:
                            pass
                        elif vertexCount == 2:
                            pass
                        elif vertexCount:
                            for j in range(vertexCount):
                                vx = unpack("<f", f.read(4))[0]
                                vy = unpack("<f", f.read(4))[0]
                                vz = unpack("<f", f.read(4))[0]
                                type4 = unpack("B", f.read(1))[0]==False
                                value1 = unpack("B", f.read(1))[0]
                                nz = unpack("<h", f.read(2))[0]
                                vertices.append([vx,vz,vy])
                                fa+=1
                                fb+=1
                                fc+=1
                                if type4 > 0:
                                    faces.append([j+j+type4-type4-1+fa-j-j-1+j%2,j-j+type4-type4+1+fb-2-1+j-j-j%2,j+type4-type4+fc-j+2-4])
                elif Chunks == b"\x03\x02\x00\x01":
                    f.seek(1,1)
                    value1 = unpack("B", f.read(1))[0]
                    vertexCount = unpack("B", f.read(1))[0] // 2
                    flag2a = unpack("B", f.read(1))[0]
                    if flag2a == 0x6D:
                        if vertexCount == 3:
                            for i in range(vertexCount):
                                vxaa = unpack("<h", f.read(2))[0] / 4096
                                vyaa = unpack("<h", f.read(2))[0] / 4096
                                vzaa = unpack("<h", f.read(2))[0] / 4096
                                vwaa = unpack("<h", f.read(2))[0] / 4096
                                uvxaa = unpack("<h", f.read(2))[0] / 4096
                                uvyaa = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2.append([vxaa,vzaa,vyaa])

                            for i in range(vertexCount-2):
                                fad+=1*3
                                fbd+=1*3
                                fcd+=1*3

                                faces2.append([fad,fbd,fcd])

                        elif vertexCount == 4:
                            for i in range(vertexCount):
                                vxaa = unpack("<h", f.read(2))[0] / 4096
                                vyaa = unpack("<h", f.read(2))[0] / 4096
                                vzaa = unpack("<h", f.read(2))[0] / 4096
                                vwaa = unpack("<h", f.read(2))[0] / 4096
                                uvxaa = unpack("<h", f.read(2))[0] / 4096
                                uvyaa = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2a.append([vxaa,vzaa,vyaa])
                            for i in range(vertexCount-3):
                                fad1abc+=1
                                fbd1abc+=1
                                fcd1abc+=1

                                faces2a.append(set([fad1abc,fbd1abc,fcd1abc]))
                            
                            
                            
                            
                                        
                            
                        
                elif Chunks == b"\x04\x02\x00\x01":
                    f.seek(1,1)
                    value1 = unpack("B", f.read(1))[0]
                    vertexCount = unpack("B", f.read(1))[0] // 2
                    flag2 = unpack("B", f.read(1))[0]
                    if flag2 == 0x6C:
                        if vertexCount == 0:
                            pass
                        elif vertexCount == 1:
                            pass
                        elif vertexCount == 2:
                            pass
                        elif vertexCount == 3:
                            for j in range(1):
                                
                                vx0001__ = unpack("<f", f.read(4))[0]
                                vy0001__ = unpack("<f", f.read(4))[0]
                                vz0001__ = unpack("<f", f.read(4))[0]
                                brightness1__ = unpack("<f", f.read(4))[0]
                                uvx0001__ = unpack("<f", f.read(4))[0]
                                uvy0001__ = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4 = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__A = unpack("<f", f.read(4))[0]
                                vy0001__A = unpack("<f", f.read(4))[0]
                                vz0001__A = unpack("<f", f.read(4))[0]
                                brightness1__A = unpack("<f", f.read(4))[0]
                                uvx0001__A = unpack("<f", f.read(4))[0]
                                uvy0001__A = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4A = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__B = unpack("<f", f.read(4))[0]
                                vy0001__B = unpack("<f", f.read(4))[0]
                                vz0001__B = unpack("<f", f.read(4))[0]
                                brightness1__B = unpack("<f", f.read(4))[0]
                                uvx0001__B = unpack("<f", f.read(4))[0]
                                uvy0001__B = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4B = unpack("B", f.read(1))[0]
                                f.seek(3,1)
                            for i in range(vertexCount):
                                f.seek(-32,1)
                            for i in range(1):
                                vx0001__C = unpack("<f", f.read(4))[0]
                                vy0001__C = unpack("<f", f.read(4))[0]
                                vz0001__C = unpack("<f", f.read(4))[0]
                                brightness1__C = unpack("<f", f.read(4))[0]
                                uvx0001__C = unpack("<f", f.read(4))[0]
                                uvy0001__C = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4C = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__D = unpack("<f", f.read(4))[0]
                                vy0001__D = unpack("<f", f.read(4))[0]
                                vz0001__D = unpack("<f", f.read(4))[0]
                                brightness1__D = unpack("<f", f.read(4))[0]
                                uvx0001__D = unpack("<f", f.read(4))[0]
                                uvy0001__D = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4D = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__E = unpack("<f", f.read(4))[0]
                                vy0001__E = unpack("<f", f.read(4))[0]
                                vz0001__E = unpack("<f", f.read(4))[0]
                                brightness1__E = unpack("<f", f.read(4))[0]
                                uvx0001__E = unpack("<f", f.read(4))[0]
                                uvy0001__E = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4E = unpack("B", f.read(1))[0]
                                f.seek(3,1)
                            for i in range(vertexCount):
                                f.seek(-32,1)
                            for i in range(1):
                                vx0001__N = unpack("<f", f.read(4))[0]
                                vy0001__N = unpack("<f", f.read(4))[0]
                                vz0001__N = unpack("<f", f.read(4))[0]
                                brightness1__N = unpack("<f", f.read(4))[0]
                                uvx0001__N = unpack("<f", f.read(4))[0]
                                uvy0001__N = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4N = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__O = unpack("<f", f.read(4))[0]
                                vy0001__O = unpack("<f", f.read(4))[0]
                                vz0001__O = unpack("<f", f.read(4))[0]
                                brightness1__O = unpack("<f", f.read(4))[0]
                                uvx0001__O = unpack("<f", f.read(4))[0]
                                uvy0001__O = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4O = unpack("B", f.read(1))[0]
                                f.seek(3,1)

                                vx0001__P = unpack("<f", f.read(4))[0]
                                vy0001__P = unpack("<f", f.read(4))[0]
                                vz0001__P = unpack("<f", f.read(4))[0]
                                brightness1__P = unpack("<f", f.read(4))[0]
                                uvx0001__P = unpack("<f", f.read(4))[0]
                                uvy0001__P = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4P = unpack("B", f.read(1))[0]
                                f.seek(3,1)
                            offsettA = unpack("<I", f.read(4))[0]
                            if offsettA == 1627553807:
                                offsetB = unpack("<I", f.read(4))[0]
                                if offsetB != 65538:
                                    f.seek(-4,1)
                                    offsetC = unpack("<I", f.read(4))[0]
                                    if offsetC == 65539:
                                        f.seek(2,1)
                                        vcount2 = unpack("B", f.read(1))[0]
                                        vflag2 = unpack("B", f.read(1))[0]
                                        if vflag2 == 0x6C:
                                            #missing verts
                                            if vcount2 == 4:
                                                for i in range(1):
                                                    vx0001__J = unpack("<f", f.read(4))[0]
                                                    vy0001__J = unpack("<f", f.read(4))[0]
                                                    vz0001__J = unpack("<f", f.read(4))[0]
                                                    type4J = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__K = unpack("<f", f.read(4))[0]
                                                    vy0001__K = unpack("<f", f.read(4))[0]
                                                    vz0001__K = unpack("<f", f.read(4))[0]
                                                    type4K = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__L = unpack("<f", f.read(4))[0]
                                                    vy0001__L = unpack("<f", f.read(4))[0]
                                                    vz0001__L = unpack("<f", f.read(4))[0]
                                                    type4L = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__M = unpack("<f", f.read(4))[0]
                                                    vy0001__M = unpack("<f", f.read(4))[0]
                                                    vz0001__M = unpack("<f", f.read(4))[0]
                                                    type4M = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                offsettC = unpack("<I", f.read(4))[0]
                                                if offsettC == 16777473:
                                                    if type4J == 0:
                                                        if type4K == 1:
                                                            if type4L == 0:
                                                                if type4M == 0:
                                                                    vertices3Aaq.append([vx0001__N,vz0001__N,vy0001__N])
                                                                    vertices3Aaq.append([vx0001__O,vz0001__O,vy0001__O])
                                                                    vertices3Aaq.append([vx0001__P,vz0001__P,vy0001__P])

                                                                    vertices3Aaq.append([vx0001__J,vz0001__J,vy0001__J])
                                                                    vertices3Aaq.append([vx0001__L,vz0001__L,vy0001__L])
                                                                    vertices3Aaq.append([vx0001__M,vz0001__M,vy0001__M])

                                                                    fa2Ta_b+=1*5
                                                                    fb2Ta_b+=1*5
                                                                    fc2Ta_b+=1*5
                                                                    fd2Ta_b+=1*5
                                                                    fe2Ta_b+=1*5

                                                                    faces3Aaq.append([fa2Ta_b,fb2Ta_b,fc2Ta_b])
                                                                    faces3Aaq.append([fb2Ta_b,fc2Ta_b,fd2Ta_b])
                                                                    faces3Aaq.append([fc2Ta_b,fd2Ta_b,fe2Ta_b])
                                elif offsetB == 65538:
                                    f.seek(2,1)
                                    vcount1 = unpack("B", f.read(1))[0]
                                    vflag1 = unpack("B", f.read(1))[0]
                                    if vflag1 == 0x6C:
                                        #missing verts
                                        if vcount1 == 4:
                                            for i in range(1):
                                                vx0001__F = unpack("<f", f.read(4))[0]
                                                vy0001__F = unpack("<f", f.read(4))[0]
                                                vz0001__F = unpack("<f", f.read(4))[0]
                                                type4F = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__G = unpack("<f", f.read(4))[0]
                                                vy0001__G = unpack("<f", f.read(4))[0]
                                                vz0001__G = unpack("<f", f.read(4))[0]
                                                type4G = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__H = unpack("<f", f.read(4))[0]
                                                vy0001__H = unpack("<f", f.read(4))[0]
                                                vz0001__H = unpack("<f", f.read(4))[0]
                                                type4H = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__I = unpack("<f", f.read(4))[0]
                                                vy0001__I = unpack("<f", f.read(4))[0]
                                                vz0001__I = unpack("<f", f.read(4))[0]
                                                type4I = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                            offsettB = unpack("<I", f.read(4))[0]
                                            if offsettB == 16777473:
                                                if type4F == 0:
                                                    if type4G == 1:
                                                        if type4H == 0:
                                                            if type4I == 0:
                                                                vertices3A.append([vx0001__C,vz0001__C,vy0001__C])
                                                                vertices3A.append([vx0001__D,vz0001__D,vy0001__D])
                                                                vertices3A.append([vx0001__E,vz0001__E,vy0001__E])

                                                                vertices3A.append([vx0001__F,vz0001__F,vy0001__F])
                                                                vertices3A.append([vx0001__H,vz0001__H,vy0001__H])
                                                                vertices3A.append([vx0001__I,vz0001__I,vy0001__I])

                                                                fa2Ta_a+=1*5
                                                                fb2Ta_a+=1*5
                                                                fc2Ta_a+=1*5
                                                                fd2Ta_a+=1*5
                                                                fe2Ta_a+=1*5

                                                                faces3A.append([fa2Ta_a,fb2Ta_a,fc2Ta_a])
                                                                faces3A.append([fb2Ta_a,fc2Ta_a,fd2Ta_a])
                                                                faces3A.append([fc2Ta_a,fd2Ta_a,fe2Ta_a])
                            elif offsettA == 16777473:
                                if type4 == 1:
                                    if type4A == 1:
                                        if type4B == 0:

                                            vertices3.append([vx0001__,vz0001__,vy0001__])
                                            vertices3.append([vx0001__A,vz0001__A,vy0001__A])
                                            vertices3.append([vx0001__B,vz0001__B,vy0001__B])
                                            uv_coords.append([uvx0001__,-uvy0001__])
                                            uv_coords.append([uvx0001__A,-uvy0001__A])
                                            uv_coords.append([uvx0001__B,-uvy0001__B])

                                            fa2+=1*3
                                            fb2+=1*3
                                            fc2+=1*3

                                            faces3.append([fa2,fb2,fc2])                
    elif TextureCount != 0:
        if TextureEntrySize1 == 144 or TextureEntrySize1 == 148 or TextureEntrySize1 == 152:
            idxA_=0
            f.seek(TextureEntrySize1,0)
            """for i in range(TextureCount):
                imgentrysizelist1 = unpack("<I", f.read(4))[0]
                texxxListt.append([imgentrysizelist1])
            for i, txxxxx in enumerate(texxxListt):
                f.seek(txxxxx[0],0)
                width1 = unpack("<H", f.read(2))[0]
                type001 = unpack("<H", f.read(2))[0]
                height1 = unpack("<H", f.read(2))[0]
                type002 = unpack("<H", f.read(2))[0]
                pitch = unpack("<I", f.read(4))[0]
                flag01 = unpack("B", f.read(1))[0]
                flag02 = unpack("B", f.read(1))[0]
                flag03 = unpack("B", f.read(1))[0]
                flag04 = unpack("B", f.read(1))[0]
                ssize1 = unpack("<I", f.read(4))[0]
                ssize2 = unpack("<I", f.read(4))[0]
                type2 = unpack("<I", f.read(4))[0]
                type3 = unpack("<I", f.read(4))[0]
                if type3 != 0:
                    padsize1 = unpack("<I", f.read(4))[0]
                    f.seek(padsize1,1)
                    
                    textureRumble1 = unpack("B", f.read(1))[0]
                    textureBrightness1 = unpack("B", f.read(1))[0]
                    textureZero1 = unpack("B", f.read(1))[0]
                    textureFlag1 = unpack("B", f.read(1))[0]

                    zero1a = unpack("<I", f.read(4))[0]
                    zero2a = unpack("<I", f.read(4))[0]

                    textureRumble1 = unpack("B", f.read(1))[0]
                    textureBrightness1 = unpack("B", f.read(1))[0]
                    textureZero1 = unpack("B", f.read(1))[0]
                    textureFlag1 = unpack("B", f.read(1))[0]
                    type4 = unpack("B", f.read(1))[0]
                    val01 = unpack("B", f.read(1))[0]
                    zero3a = unpack("<H", f.read(2))[0]
                    depth01 = unpack(">I", f.read(4))[0]
                    
                    flg01 = unpack("<I", f.read(4))[0]
                    zero1aa = unpack("<I", f.read(4))[0]
                    zero2aa = unpack("<I", f.read(4))[0]
                    zero3aa = unpack("<I", f.read(4))[0]
                    flg02 = unpack("<I", f.read(4))[0]
                    zero4aa = unpack("<I", f.read(4))[0]
                    comprW = unpack("<I", f.read(4))[0]
                    comprH = unpack("<I", f.read(4))[0]
                    flg03 = unpack("<I", f.read(4))[0]
                    zero5aa = unpack("<I", f.read(4))[0]
                    zero6aa = unpack("<I", f.read(4))[0]
                    zero7aa = unpack("<I", f.read(4))[0]
                    flg04 = unpack("<I", f.read(4))[0]
                    zero8aa = unpack("<I", f.read(4))[0]
                    
                    palleteOffset = unpack("<H", f.read(2))[0]
                    zero9aa = unpack("<H", f.read(2))[0]
                    zero10aa = unpack("<H", f.read(2))[0]
                    palletelen = unpack("<I", f.read(4))[0]
                    zero11aa = unpack("<H", f.read(2))[0]
                    zero12aa = unpack("<H", f.read(2))[0]
                    zero13aa = unpack("<H", f.read(2))[0]
                    if palleteOffset == 0x8300:
                        image_test = bpy.data.images.new(name="GHG Image", width=64, height=64, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 64*y
                        def drawPixel(x,y, R,G,B):
                            pixelNumber = grid(x,y) * 4

                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                        for x in range(64):
                            for y in range(64):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                drawPixel(-x,y,r,g,b)
                    elif palleteOffset == 0x8400:
                        image_test = bpy.data.images.new(name="GHG Image", width=64, height=64, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 64*y
                        def drawPixel(x,y, R,G,B,A):
                            pixelNumber = grid(x,y) * 4

                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                        for x in range(64):
                            for y in range(64):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0x9000:
                        image_test = bpy.data.images.new(name="GHG Image", width=64, height=256, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 64*y
                        def drawPixel(x,y, R,G,B,A):
                            pixelNumber = grid(x,y) * 4

                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                        for x in range(64):
                            for y in range(256):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0xA000:
                        image_test = bpy.data.images.new(name="GHG Image", width=128, height=256, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 128*y
                        def drawPixel(x,y, R,G,B,A):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                
                
            
                        for x in range(128):
                            for y in range(256):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0xC000:
                        image_test = bpy.data.images.new(name="GHG Image", width=256, height=256, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 256*y
                        def drawPixel(x,y, R,G,B,A):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                
                
            
                        for x in range(256):
                            for y in range(256):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0x8100:
                        image_test = bpy.data.images.new(name="GHG Image", width=32, height=32, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 32*y
                        def drawPixel(x,y, R,G,B,A):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                                    
                                    
                                
                        for x in range(32):
                            for y in range(32):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0x80C0:
                        image_test = bpy.data.images.new(name="GHG Image", width=32, height=32, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 32*y
                        def drawPixel(x,y, R,G,B):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                                    
                                    
                                
                        for x in range(32):
                            for y in range(32):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                drawPixel(-x,y,r,g,b)

                    elif palleteOffset == 0x8800:
                        image_test = bpy.data.images.new(name="GHG Image", width=64, height=128, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 64*y
                        def drawPixel(x,y, R,G,B,A):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                                    
                                    
                                
                        for x in range(64):
                            for y in range(128):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                a = unpack("B", f.read(1))[0]/127
                                drawPixel(-x,y,r,g,b,a)

                    elif palleteOffset == 0x9800:
                        image_test = bpy.data.images.new(name="GHG Image", width=128, height=256, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 128*y
                        def drawPixel(x,y, R,G,B):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                                    
                                    
                                
                        for x in range(128):
                            for y in range(256):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                drawPixel(-x,y,r,g,b)

                    elif palleteOffset == 0x8600:
                        image_test = bpy.data.images.new(name="GHG Image", width=128, height=64, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + 128*y
                        def drawPixel(x,y, R,G,B):

                            pixelNumber = grid(x,y) * 4
                                


                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                                    
                                    
                                
                        for x in range(128):
                            for y in range(64):
                                r = unpack("B", f.read(1))[0]/255
                                g = unpack("B", f.read(1))[0]/255
                                b = unpack("B", f.read(1))[0]/255
                                drawPixel(-x,y,r,g,b)
                        
                        
                elif type3 == 0:
                    textureRumble1 = unpack("B", f.read(1))[0]
                    textureBrightness1 = unpack("B", f.read(1))[0]
                    textureZero1 = unpack("B", f.read(1))[0]
                    textureFlag1 = unpack("B", f.read(1))[0]

                    zero1a = unpack("<I", f.read(4))[0]
                    zero2a = unpack("<I", f.read(4))[0]

                    textureRumble1 = unpack("B", f.read(1))[0]
                    textureBrightness1 = unpack("B", f.read(1))[0]
                    textureZero1 = unpack("B", f.read(1))[0]
                    textureFlag1 = unpack("B", f.read(1))[0]
                    type4 = unpack("B", f.read(1))[0]
                    val01 = unpack("B", f.read(1))[0]
                    zero3a = unpack("<H", f.read(2))[0]
                    depth01 = unpack(">I", f.read(4))[0]
                    
                    flg01 = unpack("<I", f.read(4))[0]
                    zero1aa = unpack("<I", f.read(4))[0]
                    zero2aa = unpack("<I", f.read(4))[0]
                    zero3aa = unpack("<I", f.read(4))[0]
                    flg02 = unpack("<I", f.read(4))[0]
                    zero4aa = unpack("<I", f.read(4))[0]
                    comprW = unpack("<I", f.read(4))[0]
                    comprH = unpack("<I", f.read(4))[0]
                    flg03 = unpack("<I", f.read(4))[0]
                    zero5aa = unpack("<I", f.read(4))[0]
                    zero6aa = unpack("<I", f.read(4))[0]
                    zero7aa = unpack("<I", f.read(4))[0]
                    flg04 = unpack("<I", f.read(4))[0]
                    zero8aa = unpack("<I", f.read(4))[0]

                    palleteOffset = unpack("<H", f.read(2))[0]
                    zero9aa = unpack("<H", f.read(2))[0]
                    zero10aa = unpack("<H", f.read(2))[0]
                    palletelen = unpack("<I", f.read(4))[0]
                    zero11aa = unpack("<H", f.read(2))[0]
                    zero12aa = unpack("<H", f.read(2))[0]
                    zero13aa = unpack("<H", f.read(2))[0]
                    if palleteOffset == 0x8080:
                        image_test = bpy.data.images.new(name="GHG Image", width=height1, height=width1, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + width1*y
                        def drawPixel(x,y, R,G,B,A):
                            pixelNumber = grid(x,y) * 4

                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                        for x in range(16):
                            for y in range(16):
                                r = unpack("B", f.read(1))[0]
                                g = unpack("B", f.read(1))[0]
                                b = unpack("B", f.read(1))[0]
                                a = unpack("B", f.read(1))[0]

                                r1 = r
                                g1 = g
                                b1 = b
                                a1 = a

                                r1*=0
                                g1*=0
                                b1*=0
                                a1*=0

                                r1+=255
                                g1+=255
                                b1+=255
                                a1+=255

                                r1/=255
                                g1/=255
                                b1/=255
                                a1/=255

                                alp,=[a]

                                texttures.append([r,g,b,a])

                        for i in range(32):
                            cdpad01 = unpack("B", f.read(1))[0]

                        sizze1 = unpack("<I", f.read(4))[0]
                        sizze2 = unpack("<I", f.read(4))[0]
                        type5 = unpack("<I", f.read(4))[0]
                        type6 = unpack("<I", f.read(4))[0]
                        if type6 != 0:
                            padssize01 = unpack("<I", f.read(4))[0]
                            f.seek(padssize01,1)
                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]

                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            type4a = unpack("B", f.read(1))[0]
                            val01a = unpack("B", f.read(1))[0]
                            zero3aa = unpack("<H", f.read(2))[0]
                            depth01a = unpack(">I", f.read(4))[0]
                            
                            flg01a = unpack("<I", f.read(4))[0]
                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]
                            zero3aaa = unpack("<I", f.read(4))[0]
                            flg02a = unpack("<I", f.read(4))[0]
                            zero4aaa = unpack("<I", f.read(4))[0]
                            comprWa = unpack("<I", f.read(4))[0]
                            comprHa = unpack("<I", f.read(4))[0]
                            flg03a = unpack("<I", f.read(4))[0]
                            zero5aaa = unpack("<I", f.read(4))[0]
                            zero6aaa = unpack("<I", f.read(4))[0]
                            zero7aaa = unpack("<I", f.read(4))[0]
                            flg04a = unpack("<I", f.read(4))[0]
                            zero8aaa = unpack("<I", f.read(4))[0]

                            idxOffset = unpack("<H", f.read(2))[0]
                            zero9aaa = unpack("<H", f.read(2))[0]
                            zero10aaa = unpack("<H", f.read(2))[0]
                            idxlen = unpack("<I", f.read(4))[0]
                            zero11aaa = unpack("<H", f.read(2))[0]
                            zero12aaa = unpack("<H", f.read(2))[0]
                            zero13aaa = unpack("<H", f.read(2))[0]
                                                     
                            for xi in range(comprHa):
                                for yi in range(comprWa):
                                    iidx = unpack("B", f.read(1))[0]
                                    iidx2 = iidx
                                    iidx3 = iidx
                                    iidx4 = iidx
                                    if alp == 127:
                                        iidx3-=iidx3
                                        iidx3+=127

                                    elif alp:
                                        iidx4-=iidx4
                                        iidx4+=alp
                                        
                                        
                                    if iidx == 1:
                                        iidx2+=254
                                    drawPixel(yi,xi,iidx2/255,iidx2/255,iidx2/255,iidx3/127+iidx4/127)
                            for i in range(80):
                                cddddpad01 = unpack("B", f.read(1))[0]
                                            
                        elif type6 == 0:
                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]

                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            type4a = unpack("B", f.read(1))[0]
                            val01a = unpack("B", f.read(1))[0]
                            zero3aa = unpack("<H", f.read(2))[0]
                            depth01a = unpack(">I", f.read(4))[0]
                            
                            flg01a = unpack("<I", f.read(4))[0]
                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]
                            zero3aaa = unpack("<I", f.read(4))[0]
                            flg02a = unpack("<I", f.read(4))[0]
                            zero4aaa = unpack("<I", f.read(4))[0]
                            comprWa = unpack("<I", f.read(4))[0]
                            comprHa = unpack("<I", f.read(4))[0]
                            flg03a = unpack("<I", f.read(4))[0]
                            zero5aaa = unpack("<I", f.read(4))[0]
                            zero6aaa = unpack("<I", f.read(4))[0]
                            zero7aaa = unpack("<I", f.read(4))[0]
                            flg04a = unpack("<I", f.read(4))[0]
                            zero8aaa = unpack("<I", f.read(4))[0]

                            idxOffset = unpack("<H", f.read(2))[0]
                            zero9aaa = unpack("<H", f.read(2))[0]
                            zero10aaa = unpack("<H", f.read(2))[0]
                            idxlen = unpack("<I", f.read(4))[0]
                            zero11aaa = unpack("<H", f.read(2))[0]
                            zero12aaa = unpack("<H", f.read(2))[0]
                            zero13aaa = unpack("<H", f.read(2))[0]

                            for xi in range(comprHa):
                                for yi in range(comprWa):
                                    iidx = unpack("B", f.read(1))[0]
                                    iidx2 = iidx
                                    iidx3 = iidx
                                    iidx4 = iidx
                                    if alp == 127:
                                        iidx3-=iidx3
                                        iidx3+=127

                                    elif alp:
                                        iidx4-=iidx4
                                        iidx4+=alp
                                        
                                        
                                    if iidx == 1:
                                        iidx2+=254
                                    drawPixel(yi,xi,iidx2/255,iidx2/255,iidx2/255,iidx3/127+iidx4/127)
                            for i in range(80):
                                cddddpad01 = unpack("B", f.read(1))[0]
                    elif palleteOffset == 0x8008:
                        image_test = bpy.data.images.new(name="GHG Image", width=height1, height=width1, alpha=True)
                        num_Pixels = len(image_test.pixels)
                        def grid(x,y):
                            return x + width1*y
                        def drawPixel(x,y, R,G,B,A):
                            pixelNumber = grid(x,y) * 4

                            image_test.pixels[pixelNumber] = R
                            image_test.pixels[pixelNumber+1] = G
                            image_test.pixels[pixelNumber+2] = B
                            image_test.pixels[pixelNumber+3] = A
                        for x in range(8):
                            for y in range(2):
                                r = unpack("B", f.read(1))[0]
                                g = unpack("B", f.read(1))[0]
                                b = unpack("B", f.read(1))[0]
                                a = unpack("B", f.read(1))[0]

                                r1 = r
                                g1 = g
                                b1 = b
                                a1 = a

                                r1*=0
                                g1*=0
                                b1*=0
                                a1*=0

                                r1+=255
                                g1+=255
                                b1+=255
                                a1+=255

                                r1/=255
                                g1/=255
                                b1/=255
                                a1/=255

                                alp2,=[a]

                                texttures.append([r,g,b,a])

                        for i in range(32):
                            cdpad01 = unpack("B", f.read(1))[0]

                        sizze1aa = unpack("<I", f.read(4))[0]
                        sizze2aa = unpack("<I", f.read(4))[0]
                        type5aa = unpack("<I", f.read(4))[0]
                        type6aa = unpack("<I", f.read(4))[0]

                        if type6aa != 0:
                            padssize01 = unpack("<I", f.read(4))[0]
                            f.seek(padssize01,1)
                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]

                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            type4a = unpack("B", f.read(1))[0]
                            val01a = unpack("B", f.read(1))[0]
                            zero3aa = unpack("<H", f.read(2))[0]
                            depth01a = unpack(">I", f.read(4))[0]
                            
                            flg01a = unpack("<I", f.read(4))[0]
                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]
                            zero3aaa = unpack("<I", f.read(4))[0]
                            flg02a = unpack("<I", f.read(4))[0]
                            zero4aaa = unpack("<I", f.read(4))[0]
                            comprWa = unpack("<I", f.read(4))[0]
                            comprHa = unpack("<I", f.read(4))[0]
                            flg03a = unpack("<I", f.read(4))[0]
                            zero5aaa = unpack("<I", f.read(4))[0]
                            zero6aaa = unpack("<I", f.read(4))[0]
                            zero7aaa = unpack("<I", f.read(4))[0]
                            flg04a = unpack("<I", f.read(4))[0]
                            zero8aaa = unpack("<I", f.read(4))[0]

                            idxOffset = unpack("<H", f.read(2))[0]
                            zero9aaa = unpack("<H", f.read(2))[0]
                            zero10aaa = unpack("<H", f.read(2))[0]
                            idxlen = unpack("<I", f.read(4))[0]
                            zero11aaa = unpack("<H", f.read(2))[0]
                            zero12aaa = unpack("<H", f.read(2))[0]
                            zero13aaa = unpack("<H", f.read(2))[0]
                                                     
                            for xi in range(comprWa):
                                for yi in range(comprHa//2):
                                    iidx = unpack("B", f.read(1))[0]
                                    iidx2 = iidx
                                    iidx3 = iidx
                                    iidx4 = iidx
                                    if alp2 == 127:
                                        iidx3-=iidx3
                                        iidx3+=127

                                    elif alp2:
                                        iidx4-=iidx4
                                        iidx4+=alp2
                                        
                                        
                                    if iidx == 1:
                                        iidx2+=254
                                    drawPixel(yi,xi,iidx2/255,iidx2/255,iidx2/255,iidx3/127+iidx4/127)
                            for i in range(80):
                                cddddpad01 = unpack("B", f.read(1))[0]

                        elif type6aa == 0:
                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]

                            textureRumble2 = unpack("B", f.read(1))[0]
                            textureBrightness2 = unpack("B", f.read(1))[0]
                            textureZero2 = unpack("B", f.read(1))[0]
                            textureFlag2 = unpack("B", f.read(1))[0]

                            type4a = unpack("B", f.read(1))[0]
                            val01a = unpack("B", f.read(1))[0]
                            zero3aa = unpack("<H", f.read(2))[0]
                            depth01a = unpack(">I", f.read(4))[0]
                            
                            flg01a = unpack("<I", f.read(4))[0]
                            zero1aaa = unpack("<I", f.read(4))[0]
                            zero2aaa = unpack("<I", f.read(4))[0]
                            zero3aaa = unpack("<I", f.read(4))[0]
                            flg02a = unpack("<I", f.read(4))[0]
                            zero4aaa = unpack("<I", f.read(4))[0]
                            comprWa = unpack("<I", f.read(4))[0]
                            comprHa = unpack("<I", f.read(4))[0]
                            flg03a = unpack("<I", f.read(4))[0]
                            zero5aaa = unpack("<I", f.read(4))[0]
                            zero6aaa = unpack("<I", f.read(4))[0]
                            zero7aaa = unpack("<I", f.read(4))[0]
                            flg04a = unpack("<I", f.read(4))[0]
                            zero8aaa = unpack("<I", f.read(4))[0]

                            idxOffset = unpack("<H", f.read(2))[0]
                            zero9aaa = unpack("<H", f.read(2))[0]
                            zero10aaa = unpack("<H", f.read(2))[0]
                            idxlen = unpack("<I", f.read(4))[0]
                            zero11aaa = unpack("<H", f.read(2))[0]
                            zero12aaa = unpack("<H", f.read(2))[0]
                            zero13aaa = unpack("<H", f.read(2))[0]
                                                     
                            for xi in range(comprWa):
                                for yi in range(comprHa//comprH):
                                    iidx = unpack("B", f.read(1))[0]
                                    iidx2 = iidx
                                    iidx3 = iidx
                                    iidx4 = iidx
                                    if alp2 == 127:
                                        iidx3-=iidx3
                                        iidx3+=127

                                    elif alp2:
                                        iidx4-=iidx4
                                        iidx4+=alp2
                                        
                                        
                                    if iidx == 1:
                                        iidx2+=254
                                    drawPixel(yi,xi,iidx2/255,iidx2/255,iidx2/255,iidx3/127+iidx4/127)
                            for i in range(80):
                                cddddpad01 = unpack("B", f.read(1))[0]"""

                        

            f.seek(0)
            f.seek(MaterialEntrySize1,0)
            
            for i in range(MaterialCount):
                matentrysizelist1 = unpack("<I", f.read(4))[0]
                matttListt.append([matentrysizelist1])
            for i, mxxxxx in enumerate(matttListt):
                f.seek(mxxxxx[0],0)
                f.seek(288,1)
                matFlg = unpack("<I", f.read(4))[0]
                RNDRSTREAMrs = unpack("<I", f.read(4))[0]
                f.seek(28,1)
                AnimatedRed = unpack("<I", f.read(4))[0]
                AnimatedGreen = unpack("<I", f.read(4))[0]
                AnimatedBlue = unpack("<I", f.read(4))[0]
                f.seek(4,1)
                matFlg2 = unpack("<I", f.read(4))[0]
                f.seek(4,1)
                VARIPTR = unpack("<I", f.read(4))[0]
                snext = unpack("<I", f.read(4))[0]
                slast = unpack("<I", f.read(4))[0]
                next1 = unpack("<I", f.read(4))[0]
                attrib = unpack("<f", f.read(4))[0]
                matFlg3 = unpack("<I", f.read(4))[0]
                ambientR = unpack("<f", f.read(4))[0]
                ambientG = unpack("<f", f.read(4))[0]
                ambientB = unpack("<f", f.read(4))[0]
                diffuseR = unpack("<f", f.read(4))[0]
                diffuseG = unpack("<f", f.read(4))[0]
                diffuseB = unpack("<f", f.read(4))[0]
                fx1 = unpack("<f", f.read(4))[0]
                fx2 = unpack("<f", f.read(4))[0]
                fx3 = unpack("<f", f.read(4))[0]
                fx4 = unpack("<f", f.read(4))[0]
                power = unpack("<f", f.read(4))[0]
                allpha = unpack("<f", f.read(4))[0]
                tid = unpack("<I", f.read(4))[0]
                mid = unpack("<I", f.read(4))[0]
                k = unpack("<H", f.read(2))[0]
                L = unpack("B", f.read(1))[0]
                uvanmmode = unpack("B", f.read(1))[0]
                du = unpack("<f", f.read(4))[0]
                dv = unpack("<f", f.read(4))[0]
                su = unpack("<f", f.read(4))[0]
                sv = unpack("<f", f.read(4))[0]
                multi_next = unpack("<I", f.read(4))[0]
                contt = unpack("B", f.read(1))[0]
                fxid = unpack("B", f.read(1))[0]
                specialid = unpack("B", f.read(1))[0]
                pad01 = unpack("B", f.read(1))[0]
                pad02 = unpack("B", f.read(1))[0]
                pad03 = unpack("B", f.read(1))[0]
                pad04 = unpack("B", f.read(1))[0]
                pad05 = unpack("B", f.read(1))[0]
                pad06 = unpack("B", f.read(1))[0]
                pad07 = unpack("B", f.read(1))[0]
                pad08 = unpack("B", f.read(1))[0]
                pad09 = unpack("B", f.read(1))[0]
                m = bpy.data.materials.new('GHG Material')
                if tid >= 0:
                    m.use_nodes = True
                    m.blend_method = 'HASHED'
                    targetnode = m.node_tree.nodes.get('Principled BSDF')
                    assert targetnode, 'Failed to locate target node.'
                    n = m.node_tree.nodes.new('ShaderNodeTexImage')
                        

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
                try:
                    ntbl_buffer.seek(name_offset)
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
    while f.tell() < len(Chunk):
        Chunks = f.read(4)
        if Chunks == b"\x03\x01\x00\x01":
            f.seek(1,1)
            value1 = unpack("B", f.read(1))[0]
            vertexCount = unpack("B", f.read(1))[0]
            flag2a = unpack("B", f.read(1))[0]
            if flag2a == 0x6C:
                if vertexCount == 0:
                    pass
                elif vertexCount == 1:
                    pass
                elif vertexCount == 2:
                    pass
                elif vertexCount:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1 = unpack("B", f.read(1))[0]
                        nz = unpack("<h", f.read(2))[0]
                        vertices.append([vx,vz,vy])
                        fa+=1
                        fb+=1
                        fc+=1
                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1+j%2,j-j+type4-type4+1+fb-2-1+j-j-j%2,j+type4-type4+fc-j+2-4])
        elif Chunks == b"\x03\x02\x00\x01":
            f.seek(1,1)
            value1 = unpack("B", f.read(1))[0]
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2a = unpack("B", f.read(1))[0]
            if flag2a == 0x6D:
                if vertexCount == 0:
                    pass
                elif vertexCount == 1:
                    pass
                elif vertexCount == 2:
                    pass
                elif vertexCount == 3:
                    for i in range(vertexCount):
                        vxaa = unpack("<h", f.read(2))[0] / 4096
                        vyaa = unpack("<h", f.read(2))[0] / 4096
                        vzaa = unpack("<h", f.read(2))[0] / 4096
                        vwaa = unpack("<h", f.read(2))[0] / 4096
                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2.append([vxaa,vzaa,vyaa])
                        uvs2.append([uvxaa,-uvyaa])

                    f.seek(78,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsB = unpack("B", f.read(1))[0]
                    if flagsB == 0x6E:
                        id1 = unpack("B", f.read(1))[0]
                        fad = unpack("B", f.read(1))[0] & 0x0F
                        fbd = unpack("B", f.read(1))[0] & 0x0F
                        fcd = unpack("B", f.read(1))[0] & 0x0F
                            
                        fad//=3
                        fbd//=3
                        fcd//=3

                        fad+=1*len(vertices2)-3
                        fbd+=1*len(vertices2)-3
                        fcd+=1*len(vertices2)-3

                        faces2.append([fad,fbd,fcd])

                elif vertexCount == 4:
                    for i in range(vertexCount):
                        vxaa1 = unpack("<h", f.read(2))[0] / 4096
                        vyaa1 = unpack("<h", f.read(2))[0] / 4096
                        vzaa1 = unpack("<h", f.read(2))[0] / 4096
                        vwaa1 = unpack("<h", f.read(2))[0] / 4096
                        uvxaa1 = unpack("<h", f.read(2))[0] / 4096
                        uvyaa1 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2a.append([vxaa1,vzaa1,vyaa1])
                        #uvs2a.append([uvxaa1,-uvyaa1])

                    f.seek(82,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag01 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6E:
                        if facecount == 2:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaa = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaa = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaa = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaa = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(3,1)

                            fa1aaa//=3
                            fb1aaa//=3
                            fc1aaa//=3
                            fd1aaa//=3

                            fa1aaa+=1*len(vertices2a)-4
                            fb1aaa+=1*len(vertices2a)-4
                            fc1aaa+=1*len(vertices2a)-4
                            fd1aaa+=1*len(vertices2a)-4

                            faces2a.append([fa1aaa,fb1aaa,fc1aaa])
                            faces2a.append([fb1aaa,fc1aaa,fd1aaa])

                elif vertexCount == 5:
                    for i in range(vertexCount):
                        vx1_2 = unpack("<h", f.read(2))[0] / 4096
                        vy1_2 = unpack("<h", f.read(2))[0] / 4096
                        vz1_2 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_2 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_2 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2b.append([vx1_2,vz1_2,vy1_2])

                    
                    f.seek(86,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsB = unpack("B", f.read(1))[0]
                    if flagsB == 0x6E:
                        if facecount == 2:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaab = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaab = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaab = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaab = unpack("B", f.read(1))[0] & 0x0F
                            fe1aaab = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(2,1)
                            
                            fa1aaab//=3
                            fb1aaab//=3
                            fc1aaab//=3
                            fd1aaab//=3
                            fe1aaab//=3

                            fa1aaab+=1*len(vertices2b)-5
                            fb1aaab+=1*len(vertices2b)-5
                            fc1aaab+=1*len(vertices2b)-5
                            fd1aaab+=1*len(vertices2b)-5
                            fe1aaab+=1*len(vertices2b)-5

                            faces2b.append([fa1aaab,fb1aaab,fc1aaab])
                            faces2b.append([fb1aaab,fc1aaab,fd1aaab])
                            faces2b.append([fc1aaab,fd1aaab,fe1aaab])
                        elif facecount == 3:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaxb = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaaxb = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaaxb = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaaxb = unpack("B", f.read(1))[0] & 0x0F
                            fe1aaaxb = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(2,1)
                            
                            fa1aaaxb//=3
                            fb1aaaxb//=3
                            fc1aaaxb//=3
                            fd1aaaxb//=3
                            fe1aaaxb//=3

                            fa1aaaxb+=1*len(vertices2b)-5
                            fb1aaaxb+=1*len(vertices2b)-5
                            fc1aaaxb+=1*len(vertices2b)-5
                            fd1aaaxb+=1*len(vertices2b)-5
                            fe1aaaxb+=1*len(vertices2b)-5

                            faces2b.append([fa1aaaxb,fb1aaaxb,fc1aaaxb])
                            faces2b.append([fb1aaaxb,fc1aaaxb,fd1aaaxb])
                            faces2b.append([fc1aaaxb,fd1aaaxb,fe1aaaxb])

                elif vertexCount == 6:
                    for i in range(vertexCount):
                        vx1_3 = unpack("<h", f.read(2))[0] / 4096
                        vy1_3 = unpack("<h", f.read(2))[0] / 4096
                        vz1_3 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_3 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_3 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2c.append([vx1_3,vz1_3,vy1_3])
                    for i in range(vertexCount):
                        f.seek(-16,1)
                    for i in range(1):
                        vx1_3a = unpack("<H", f.read(2))[0]
                        vy1_3a = unpack("<H", f.read(2))[0]
                        vz1_3a = unpack("<H", f.read(2))[0]
                        nz_3a = unpack("<H", f.read(2))[0]
                        uvx1_3a = unpack("<H", f.read(2))[0]
                        uvy1_3a = unpack("<H", f.read(2))[0]
                        unk1_3a = unpack("<I", f.read(4))[0]
                        vx1_3b = unpack("<H", f.read(2))[0]
                        vy1_3b = unpack("<H", f.read(2))[0]
                        vz1_3b = unpack("<H", f.read(2))[0]
                        nz_3b = unpack("<H", f.read(2))[0]
                        uvx1_3b = unpack("<H", f.read(2))[0]
                        uvy1_3b = unpack("<H", f.read(2))[0]
                        unk1_3b = unpack("<I", f.read(4))[0]
                        vx1_3c = unpack("<H", f.read(2))[0]
                        vy1_3c = unpack("<H", f.read(2))[0]
                        vz1_3c = unpack("<H", f.read(2))[0]
                        nz_3c = unpack("<H", f.read(2))[0]
                        uvx1_3c = unpack("<H", f.read(2))[0]
                        uvy1_3c = unpack("<H", f.read(2))[0]
                        unk1_3c = unpack("<I", f.read(4))[0]
                        vx1_3d = unpack("<H", f.read(2))[0]
                        vy1_3d = unpack("<H", f.read(2))[0]
                        vz1_3d = unpack("<H", f.read(2))[0]
                        nz_3d = unpack("<H", f.read(2))[0]
                        uvx1_3d = unpack("<H", f.read(2))[0]
                        uvy1_3d = unpack("<H", f.read(2))[0]
                        unk1_3d = unpack("<I", f.read(4))[0]
                        vx1_3e = unpack("<H", f.read(2))[0]
                        vy1_3e = unpack("<H", f.read(2))[0]
                        vz1_3e = unpack("<H", f.read(2))[0]
                        nz_3e = unpack("<H", f.read(2))[0]
                        uvx1_3e = unpack("<H", f.read(2))[0]
                        uvy1_3e = unpack("<H", f.read(2))[0]
                        unk1_3e = unpack("<I", f.read(4))[0]
                        vx1_3f = unpack("<H", f.read(2))[0]
                        vy1_3f = unpack("<H", f.read(2))[0]
                        vz1_3f = unpack("<H", f.read(2))[0]
                        nz_3f = unpack("<H", f.read(2))[0]
                        uvx1_3f = unpack("<H", f.read(2))[0]
                        uvy1_3f = unpack("<H", f.read(2))[0]
                        unk1_3f = unpack("<I", f.read(4))[0]
                        

                    f.seek(90,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 2:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaac = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaac = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaac = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaac = unpack("B", f.read(1))[0] & 0x0F
                            fe1aaac = unpack("B", f.read(1))[0] & 0x0F
                            ff1aaac = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(1,1)
                            
                            fa1aaac//=3
                            fb1aaac//=3
                            fc1aaac//=3
                            fd1aaac//=3
                            fe1aaac//=3
                            ff1aaac//=3

                            fa1aaac+=1*len(vertices2c)-6
                            fb1aaac+=1*len(vertices2c)-6
                            fc1aaac+=1*len(vertices2c)-6
                            fd1aaac+=1*len(vertices2c)-6
                            fe1aaac+=1*len(vertices2c)-6
                            ff1aaac+=1*len(vertices2c)-6

                            faces2c.append([fa1aaac,fb1aaac,fc1aaac])
                            faces2c.append([fd1aaac,fe1aaac,ff1aaac])

                        elif facecount == 3:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fe1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            ff1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fg1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fh1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            fi1aaaca = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(2,1)
                            
                            fa1aaaca//=3
                            fb1aaaca//=3
                            fc1aaaca//=3
                            fd1aaaca//=3
                            fe1aaaca//=3
                            ff1aaaca//=3

                            fa1aaaca+=1*len(vertices2c)-6
                            fb1aaaca+=1*len(vertices2c)-6
                            fc1aaaca+=1*len(vertices2c)-6
                            fd1aaaca+=1*len(vertices2c)-6
                            fe1aaaca+=1*len(vertices2c)-6
                            ff1aaaca+=1*len(vertices2c)-6

                            faces2c.append([fa1aaaca,fb1aaaca,fc1aaaca])
                            faces2c.append([fb1aaaca,fc1aaaca,fd1aaaca])
                            faces2c.append([fc1aaaca,fd1aaaca,fe1aaaca])
                            faces2c.append([fd1aaaca,fe1aaaca,ff1aaaca])
                            faces2c.append([fe1aaaca,ff1aaaca,fg1aaaca])
                            faces2c.append([fg1aaaca,fh1aaaca,fi1aaaca])

                        elif facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            fb1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            fc1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            fd1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            fe1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            ff1aaacax = unpack("B", f.read(1))[0] & 0x0F
                            f.seek(2,1)
                            
                            fa1aaacax//=3
                            fb1aaacax//=3
                            fc1aaacax//=3
                            fd1aaacax//=3
                            fe1aaacax//=3
                            ff1aaacax//=3 

                            fa1aaacax+=1*len(vertices2c)-6
                            fb1aaacax+=1*len(vertices2c)-6
                            fc1aaacax+=1*len(vertices2c)-6
                            fd1aaacax+=1*len(vertices2c)-6
                            fe1aaacax+=1*len(vertices2c)-6
                            ff1aaacax+=1*len(vertices2c)-6

                            faces2c.append([fa1aaacax,fb1aaacax,fc1aaacax])
                            faces2c.append([fb1aaacax,fc1aaacax,fd1aaacax])
                            faces2c.append([fb1aaacax,fc1aaacax,fd1aaacax])
                            faces2c.append([fc1aaacax,fd1aaacax,fe1aaacax])

                elif vertexCount == 7:
                    for i in range(vertexCount):
                        vx1_3 = unpack("<h", f.read(2))[0] / 4096
                        vy1_3 = unpack("<h", f.read(2))[0] / 4096
                        vz1_3 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_3 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_3 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2d.append([vx1_3,vz1_3,vy1_3])

                    f.seek(94,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 2:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaad = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaad = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaad = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaad = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaad = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaad = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaad = unpack("B", f.read(1))[0] & 0x1F
                            
                            fa1aaad//=3
                            fb1aaad//=3
                            fc1aaad//=3
                            fd1aaad//=3
                            fe1aaad//=3
                            ff1aaad//=3
                            fg1aaad//=3

                            fa1aaad+=1*len(vertices2d)-7
                            fb1aaad+=1*len(vertices2d)-7
                            fc1aaad+=1*len(vertices2d)-7
                            fd1aaad+=1*len(vertices2d)-7
                            fe1aaad+=1*len(vertices2d)-7
                            ff1aaad+=1*len(vertices2d)-7

                            faces2d.append([fa1aaad,fb1aaad,fc1aaad])
                            faces2d.append([fd1aaad,fe1aaad,ff1aaad])
                            faces2d.append([fe1aaad,ff1aaad,fg1aaad])

                        elif facecount == 5:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaadx = unpack("B", f.read(1))[0] & 0x1F
                            
                            fa1aaadx//=3
                            fb1aaadx//=3
                            fc1aaadx//=3
                            fd1aaadx//=3
                            fe1aaadx//=3
                            ff1aaadx//=3
                            fg1aaadx//=3

                            fa1aaadx+=1*len(vertices2d)-7
                            fb1aaadx+=1*len(vertices2d)-7
                            fc1aaadx+=1*len(vertices2d)-7
                            fd1aaadx+=1*len(vertices2d)-7
                            fe1aaadx+=1*len(vertices2d)-7
                            ff1aaadx+=1*len(vertices2d)-7

                            faces2d.append([fa1aaadx,fb1aaadx,fc1aaadx])
                            faces2d.append([fd1aaadx,fe1aaadx,ff1aaadx])
                            faces2d.append([fe1aaadx,ff1aaadx,fg1aaadx])

                elif vertexCount == 8:
                    for i in range(vertexCount):
                        vx1_4 = unpack("<h", f.read(2))[0] / 4096
                        vy1_4 = unpack("<h", f.read(2))[0] / 4096
                        vz1_4 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_4 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_4 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2e.append([vx1_4,vz1_4,vy1_4])

                    f.seek(98,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 3:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaae = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaae = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaae = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(3,1)
                            
                            fa1aaae//=3
                            fb1aaae//=3
                            fc1aaae//=3
                            fd1aaae//=3
                            fe1aaae//=3
                            ff1aaae//=3
                            fg1aaae//=3
                            fh1aaae//=3

                            fa1aaae+=1*len(vertices2e)-8
                            fb1aaae+=1*len(vertices2e)-8
                            fc1aaae+=1*len(vertices2e)-8
                            fd1aaae+=1*len(vertices2e)-8
                            fe1aaae+=1*len(vertices2e)-8
                            ff1aaae+=1*len(vertices2e)-8
                            fg1aaae+=1*len(vertices2e)-8
                            fh1aaae+=1*len(vertices2e)-8

                            faces2e.append([fa1aaae,fb1aaae,fc1aaae])
                            faces2e.append([fb1aaae,fc1aaae,fd1aaae])
                            faces2e.append([fc1aaae,fd1aaae,fe1aaae])
                            faces2e.append([fd1aaae,fe1aaae,ff1aaae])
                            faces2e.append([fe1aaae,ff1aaae,fg1aaae])
                            faces2e.append([ff1aaae,fg1aaae,fh1aaae])

                elif vertexCount == 9:
                    for i in range(vertexCount):
                        vx1_5 = unpack("<h", f.read(2))[0] / 4096
                        vy1_5 = unpack("<h", f.read(2))[0] / 4096
                        vz1_5 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_5 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_5 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2f.append([vx1_5,vz1_5,vy1_5])

                    f.seek(98,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 3:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            fi1aaaf = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(2,1)
                            
                            fa1aaaf//=3
                            fb1aaaf//=3
                            fc1aaaf//=3
                            fd1aaaf//=3
                            fe1aaaf//=3
                            ff1aaaf//=3
                            fg1aaaf//=3
                            fh1aaaf//=3
                            fi1aaaf//=3

                            fa1aaaf+=1*len(vertices2f)-9
                            fb1aaaf+=1*len(vertices2f)-9
                            fc1aaaf+=1*len(vertices2f)-9
                            fd1aaaf+=1*len(vertices2f)-9
                            fe1aaaf+=1*len(vertices2f)-9
                            ff1aaaf+=1*len(vertices2f)-9
                            fg1aaaf+=1*len(vertices2f)-9
                            fh1aaaf+=1*len(vertices2f)-9
                            fi1aaaf+=1*len(vertices2f)-9

                            faces2f.append([fa1aaaf,fb1aaaf,fc1aaaf])
                            faces2f.append([fd1aaaf,fe1aaaf,ff1aaaf])
                            faces2f.append([fg1aaaf,fh1aaaf,fi1aaaf])

                elif vertexCount == 10:
                    for i in range(vertexCount):
                        vx1_6 = unpack("<h", f.read(2))[0] / 4096
                        vy1_6 = unpack("<h", f.read(2))[0] / 4096
                        vz1_6 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_6 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_6 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2g.append([vx1_6,vz1_6,vy1_6])

                    f.seek(106,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 3:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaag = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fi1aaag = unpack("B", f.read(1))[0] & 0x1F
                            fj1aaag = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(1,1)
                            
                            fa1aaag//=3
                            fb1aaag//=3
                            fc1aaag//=3
                            fd1aaag//=3
                            fe1aaag//=3
                            ff1aaag//=3
                            fg1aaag//=3
                            fh1aaag//=3
                            fi1aaag//=3
                            fj1aaag//=3

                            fa1aaag+=1*len(vertices2g)-10
                            fb1aaag+=1*len(vertices2g)-10
                            fc1aaag+=1*len(vertices2g)-10
                            fd1aaag+=1*len(vertices2g)-10
                            fe1aaag+=1*len(vertices2g)-10
                            ff1aaag+=1*len(vertices2g)-10
                            fg1aaag+=1*len(vertices2g)-10
                            fh1aaag+=1*len(vertices2g)-10
                            fi1aaag+=1*len(vertices2g)-10
                            fj1aaag+=1*len(vertices2g)-10

                            faces2g.append([fa1aaag,fb1aaag,fc1aaag])
                            faces2g.append([fb1aaag,fc1aaag,fd1aaag])
                            faces2g.append([fd1aaag,fe1aaag,ff1aaag])
                            faces2g.append([fg1aaag,fh1aaag,fi1aaag])
                            faces2g.append([fh1aaag,fi1aaag,fj1aaag])

                        elif facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fi1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fj1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fk1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            fl1aaag1 = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(3,1)
                            
                            fa1aaag1//=3
                            fb1aaag1//=3
                            fc1aaag1//=3
                            fd1aaag1//=3
                            fe1aaag1//=3
                            ff1aaag1//=3
                            fg1aaag1//=3
                            fh1aaag1//=3
                            fi1aaag1//=3
                            fj1aaag1//=3
                            fk1aaag1//=3
                            fl1aaag1//=3

                            fa1aaag1+=1*len(vertices2g)-10
                            fb1aaag1+=1*len(vertices2g)-10
                            fc1aaag1+=1*len(vertices2g)-10
                            fd1aaag1+=1*len(vertices2g)-10
                            fe1aaag1+=1*len(vertices2g)-10
                            ff1aaag1+=1*len(vertices2g)-10
                            fg1aaag1+=1*len(vertices2g)-10
                            fh1aaag1+=1*len(vertices2g)-10
                            fi1aaag1+=1*len(vertices2g)-10
                            fj1aaag1+=1*len(vertices2g)-10
                            fk1aaag1+=1*len(vertices2g)-10
                            fl1aaag1+=1*len(vertices2g)-10

                            faces2g.append([fa1aaag1,fb1aaag1,fc1aaag1])
                            faces2g.append([fb1aaag1,fc1aaag1,fd1aaag1])
                            faces2g.append([fd1aaag1,fe1aaag1,ff1aaag1])
                            faces2g.append([fg1aaag1,fh1aaag1,fi1aaag1])
                            faces2g.append([fh1aaag1,fi1aaag1,fj1aaag1])
                            faces2g.append([fi1aaag1,fj1aaag1,fk1aaag1])
                            faces2g.append([fj1aaag1,fk1aaag1,fl1aaag1])

                elif vertexCount == 11:
                    for i in range(vertexCount):
                        vx1_7 = unpack("<h", f.read(2))[0] / 4096
                        vy1_7 = unpack("<h", f.read(2))[0] / 4096
                        vz1_7 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_7 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_7 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2h.append([vx1_7,vz1_7,vy1_7])

                    f.seek(110,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 3:
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            fi1aaahi = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(2,1)
                            
                            fa1aaahi//=3
                            fb1aaahi//=3
                            fc1aaahi//=3
                            fd1aaahi//=3
                            fe1aaahi//=3
                            ff1aaahi//=3
                            fg1aaahi//=3
                            fh1aaahi//=3
                            fi1aaahi//=3

                            fa1aaahi+=1*len(vertices2h)-11
                            fb1aaahi+=1*len(vertices2h)-11
                            fc1aaahi+=1*len(vertices2h)-11
                            fd1aaahi+=1*len(vertices2h)-11
                            fe1aaahi+=1*len(vertices2h)-11
                            ff1aaahi+=1*len(vertices2h)-11
                            fg1aaahi+=1*len(vertices2h)-11
                            fh1aaahi+=1*len(vertices2h)-11
                            fi1aaahi+=1*len(vertices2h)-11

                            faces2h.append([fa1aaahi,fb1aaahi,fc1aaahi])
                            faces2h.append([fb1aaahi,fc1aaahi,fd1aaahi])
                            faces2h.append([fc1aaahi,fd1aaahi,fe1aaahi])
                            faces2h.append([fd1aaahi,fe1aaahi,ff1aaahi])
                            faces2h.append([fe1aaahi,ff1aaahi,fg1aaahi])
                            faces2h.append([ff1aaahi,fg1aaahi,fh1aaahi])
                            faces2h.append([fg1aaahi,fh1aaahi,fi1aaahi])
                        elif facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fb1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fc1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fd1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fe1aaah = unpack("B", f.read(1))[0] & 0x1F
                            ff1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fg1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fh1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fi1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fj1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fk1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fl1aaah = unpack("B", f.read(1))[0] & 0x1F
                            fm1aaah = unpack("B", f.read(1))[0] & 0x1F
                            f.seek(2,1)
                            
                            fa1aaah//=3
                            fb1aaah//=3
                            fc1aaah//=3
                            fd1aaah//=3
                            fe1aaah//=3
                            ff1aaah//=3
                            fg1aaah//=3
                            fh1aaah//=3
                            fi1aaah//=3
                            fj1aaah//=3
                            fk1aaah//=3
                            fl1aaah//=3
                            fm1aaah//=3

                            fa1aaah+=1*len(vertices2h)-11
                            fb1aaah+=1*len(vertices2h)-11
                            fc1aaah+=1*len(vertices2h)-11
                            fd1aaah+=1*len(vertices2h)-11
                            fe1aaah+=1*len(vertices2h)-11
                            ff1aaah+=1*len(vertices2h)-11
                            fg1aaah+=1*len(vertices2h)-11
                            fh1aaah+=1*len(vertices2h)-11
                            fi1aaah+=1*len(vertices2h)-11
                            fj1aaah+=1*len(vertices2h)-11
                            fk1aaah+=1*len(vertices2h)-11
                            fl1aaah+=1*len(vertices2h)-11
                            fm1aaah+=1*len(vertices2h)-11

                            faces2h.append([fa1aaah,fb1aaah,fc1aaah])
                            faces2h.append([fb1aaah,fc1aaah,fd1aaah])
                            faces2h.append([fc1aaah,fd1aaah,fe1aaah])
                            faces2h.append([fd1aaah,fe1aaah,ff1aaah])
                            faces2h.append([fe1aaah,ff1aaah,fg1aaah])
                            faces2h.append([ff1aaah,fg1aaah,fh1aaah])
                            faces2h.append([fg1aaah,fh1aaah,fi1aaah])
                            faces2h.append([fh1aaah,fi1aaah,fj1aaah])
                            faces2h.append([fi1aaah,fj1aaah,fk1aaah])
                            faces2h.append([fj1aaah,fk1aaah,fl1aaah])
                            faces2h.append([fk1aaah,fl1aaah,fm1aaah])

                elif vertexCount == 12:
                    for i in range(vertexCount):
                        vx1_8 = unpack("<h", f.read(2))[0] / 4096
                        vy1_8 = unpack("<h", f.read(2))[0] / 4096
                        vz1_8 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_8 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_8 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2i.append([vx1_8,vz1_8,vy1_8])

                    f.seek(114,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaai = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaai = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaai = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(3,1)
                            
                            fa1aaai//=3
                            fb1aaai//=3
                            fc1aaai//=3
                            fd1aaai//=3
                            fe1aaai//=3
                            ff1aaai//=3
                            fg1aaai//=3
                            fh1aaai//=3
                            fi1aaai//=3
                            fj1aaai//=3
                            fk1aaai//=3
                            fl1aaai//=3

                            fa1aaai+=1*len(vertices2i)-12
                            fb1aaai+=1*len(vertices2i)-12
                            fc1aaai+=1*len(vertices2i)-12
                            fd1aaai+=1*len(vertices2i)-12
                            fe1aaai+=1*len(vertices2i)-12
                            ff1aaai+=1*len(vertices2i)-12
                            fg1aaai+=1*len(vertices2i)-12
                            fh1aaai+=1*len(vertices2i)-12
                            fi1aaai+=1*len(vertices2i)-12
                            fj1aaai+=1*len(vertices2i)-12
                            fk1aaai+=1*len(vertices2i)-12
                            fl1aaai+=1*len(vertices2i)-12

                            faces2i.append([fa1aaai,fb1aaai,fc1aaai])
                            faces2i.append([fb1aaai,fc1aaai,fd1aaai])
                            faces2i.append([fd1aaai,fe1aaai,ff1aaai])
                            faces2i.append([fg1aaai,fh1aaai,fi1aaai])
                            faces2i.append([fh1aaai,fi1aaai,fj1aaai])
                            faces2i.append([fi1aaai,fj1aaai,fk1aaai])
                            faces2i.append([fj1aaai,fk1aaai,fl1aaai])

                        elif facecount == 5:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaaii = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(7,1)
                            
                            fa1aaaii//=3
                            fb1aaaii//=3
                            fc1aaaii//=3
                            fd1aaaii//=3
                            fe1aaaii//=3
                            ff1aaaii//=3
                            fg1aaaii//=3
                            fh1aaaii//=3
                            fi1aaaii//=3
                            fj1aaaii//=3
                            fk1aaaii//=3
                            fl1aaaii//=3

                            fa1aaaii+=1*len(vertices2i)-12
                            fb1aaaii+=1*len(vertices2i)-12
                            fc1aaaii+=1*len(vertices2i)-12
                            fd1aaaii+=1*len(vertices2i)-12
                            fe1aaaii+=1*len(vertices2i)-12
                            ff1aaaii+=1*len(vertices2i)-12
                            fg1aaaii+=1*len(vertices2i)-12
                            fh1aaaii+=1*len(vertices2i)-12
                            fi1aaaii+=1*len(vertices2i)-12
                            fj1aaaii+=1*len(vertices2i)-12
                            fk1aaaii+=1*len(vertices2i)-12
                            fl1aaaii+=1*len(vertices2i)-12

                            faces2i.append([fa1aaaii,fb1aaaii,fc1aaaii])
                            faces2i.append([fb1aaaii,fc1aaaii,fd1aaaii])
                            faces2i.append([fd1aaaii,fe1aaaii,ff1aaaii])
                            faces2i.append([fg1aaaii,fh1aaaii,fi1aaaii])
                            faces2i.append([fh1aaaii,fi1aaaii,fj1aaaii])
                            faces2i.append([fi1aaaii,fj1aaaii,fk1aaaii])
                            faces2i.append([fj1aaaii,fk1aaaii,fl1aaaii])

                elif vertexCount == 13:
                    for i in range(vertexCount):
                        vx1_9 = unpack("<h", f.read(2))[0] / 4096
                        vy1_9 = unpack("<h", f.read(2))[0] / 4096
                        vz1_9 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_9 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_9 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2j.append([vx1_9,vz1_9,vy1_9])

                    f.seek(118,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 5:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fm1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fn1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            fo1aaaj = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(4,1)
                            
                            fa1aaaj//=3
                            fb1aaaj//=3
                            fc1aaaj//=3
                            fd1aaaj//=3
                            fe1aaaj//=3
                            ff1aaaj//=3
                            fg1aaaj//=3
                            fh1aaaj//=3
                            fi1aaaj//=3
                            fj1aaaj//=3
                            fk1aaaj//=3
                            fl1aaaj//=3
                            fm1aaaj//=3
                            fn1aaaj//=3
                            fo1aaaj//=3

                            fa1aaaj+=1*len(vertices2j)-13
                            fb1aaaj+=1*len(vertices2j)-13
                            fc1aaaj+=1*len(vertices2j)-13
                            fd1aaaj+=1*len(vertices2j)-13
                            fe1aaaj+=1*len(vertices2j)-13
                            ff1aaaj+=1*len(vertices2j)-13
                            fg1aaaj+=1*len(vertices2j)-13
                            fh1aaaj+=1*len(vertices2j)-13
                            fi1aaaj+=1*len(vertices2j)-13
                            fj1aaaj+=1*len(vertices2j)-13
                            fk1aaaj+=1*len(vertices2j)-13
                            fl1aaaj+=1*len(vertices2j)-13
                            fm1aaaj+=1*len(vertices2j)-13
                            fn1aaaj+=1*len(vertices2j)-13
                            fo1aaaj+=1*len(vertices2j)-13

                            faces2j.append([fa1aaaj,fb1aaaj,fc1aaaj])
                            faces2j.append([fb1aaaj,fc1aaaj,fd1aaaj])
                            faces2j.append([fd1aaaj,fe1aaaj,ff1aaaj])
                            faces2j.append([fg1aaaj,fh1aaaj,fi1aaaj])
                            faces2j.append([fh1aaaj,fi1aaaj,fj1aaaj])
                            faces2j.append([fi1aaaj,fj1aaaj,fk1aaaj])
                            faces2j.append([fj1aaaj,fk1aaaj,fl1aaaj])
                            faces2j.append([fk1aaaj,fl1aaaj,fm1aaaj])
                            faces2j.append([fl1aaaj,fm1aaaj,fn1aaaj])
                            faces2j.append([fm1aaaj,fn1aaaj,fo1aaaj])

                        elif facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaaja = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(3,1)
                            
                            fa1aaaja//=3
                            fb1aaaja//=3
                            fc1aaaja//=3
                            fd1aaaja//=3
                            fe1aaaja//=3
                            ff1aaaja//=3
                            fg1aaaja//=3
                            fh1aaaja//=3
                            fi1aaaja//=3
                            fj1aaaja//=3
                            fk1aaaja//=3
                            fl1aaaja//=3

                            fa1aaaja+=1*len(vertices2j)-13
                            fb1aaaja+=1*len(vertices2j)-13
                            fc1aaaja+=1*len(vertices2j)-13
                            fd1aaaja+=1*len(vertices2j)-13
                            fe1aaaja+=1*len(vertices2j)-13
                            ff1aaaja+=1*len(vertices2j)-13
                            fg1aaaja+=1*len(vertices2j)-13
                            fh1aaaja+=1*len(vertices2j)-13
                            fi1aaaja+=1*len(vertices2j)-13
                            fj1aaaja+=1*len(vertices2j)-13
                            fk1aaaja+=1*len(vertices2j)-13
                            fl1aaaja+=1*len(vertices2j)-13

                            faces2j.append([fa1aaaja,fb1aaaja,fc1aaaja])
                            faces2j.append([fb1aaaja,fc1aaaja,fd1aaaja])
                            faces2j.append([fc1aaaja,fd1aaaja,fe1aaaja])
                            faces2j.append([fd1aaaja,fe1aaaja,ff1aaaja])
                            faces2j.append([fe1aaaja,ff1aaaja,fg1aaaja])
                            faces2j.append([ff1aaaja,fg1aaaja,fh1aaaja])
                            faces2j.append([fg1aaaja,fh1aaaja,fi1aaaja])
                            faces2j.append([fh1aaaja,fi1aaaja,fj1aaaja])
                            faces2j.append([fi1aaaja,fj1aaaja,fk1aaaja])
                            faces2j.append([fj1aaaja,fk1aaaja,fl1aaaja])

                        elif facecount == 6:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fm1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fn1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fo1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fp1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fq1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            fr1aaajb = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(5,1)
                            
                            fa1aaajb//=3
                            fb1aaajb//=3
                            fc1aaajb//=3
                            fd1aaajb//=3
                            fe1aaajb//=3
                            ff1aaajb//=3
                            fg1aaajb//=3
                            fh1aaajb//=3
                            fi1aaajb//=3
                            fj1aaajb//=3
                            fk1aaajb//=3
                            fl1aaajb//=3
                            fm1aaajb//=3
                            fn1aaajb//=3
                            fo1aaajb//=3
                            fp1aaajb//=3
                            fq1aaajb//=3
                            fr1aaajb//=3

                            fa1aaajb+=1*len(vertices2j)-13
                            fb1aaajb+=1*len(vertices2j)-13
                            fc1aaajb+=1*len(vertices2j)-13
                            fd1aaajb+=1*len(vertices2j)-13
                            fe1aaajb+=1*len(vertices2j)-13
                            ff1aaajb+=1*len(vertices2j)-13
                            fg1aaajb+=1*len(vertices2j)-13
                            fh1aaajb+=1*len(vertices2j)-13
                            fi1aaajb+=1*len(vertices2j)-13
                            fj1aaajb+=1*len(vertices2j)-13
                            fk1aaajb+=1*len(vertices2j)-13
                            fl1aaajb+=1*len(vertices2j)-13
                            fm1aaajb+=1*len(vertices2j)-13
                            fn1aaajb+=1*len(vertices2j)-13
                            fo1aaajb+=1*len(vertices2j)-13
                            fp1aaajb+=1*len(vertices2j)-13
                            fq1aaajb+=1*len(vertices2j)-13
                            fr1aaajb+=1*len(vertices2j)-13

                            faces2j.append([fa1aaajb,fb1aaajb,fc1aaajb])
                            faces2j.append([fb1aaajb,fc1aaajb,fd1aaajb])
                            faces2j.append([fc1aaajb,fd1aaajb,fe1aaajb])
                            faces2j.append([fd1aaajb,fe1aaajb,ff1aaajb])
                            faces2j.append([fe1aaajb,ff1aaajb,fg1aaajb])
                            faces2j.append([ff1aaajb,fg1aaajb,fh1aaajb])
                            faces2j.append([fg1aaajb,fh1aaajb,fi1aaajb])
                            faces2j.append([fh1aaajb,fi1aaajb,fj1aaajb])
                            faces2j.append([fi1aaajb,fj1aaajb,fk1aaajb])
                            faces2j.append([fj1aaajb,fk1aaajb,fl1aaajb])
                            faces2j.append([fk1aaajb,fl1aaajb,fm1aaajb])
                            faces2j.append([fl1aaajb,fm1aaajb,fn1aaajb])
                            faces2j.append([fm1aaajb,fn1aaajb,fo1aaajb])
                            faces2j.append([fn1aaajb,fo1aaajb,fp1aaajb])
                            faces2j.append([fo1aaajb,fp1aaajb,fq1aaajb])
                            faces2j.append([fp1aaajb,fq1aaajb,fr1aaajb])

                elif vertexCount == 14:
                    for i in range(vertexCount):
                        vx1_10 = unpack("<h", f.read(2))[0] / 4096
                        vy1_10 = unpack("<h", f.read(2))[0] / 4096
                        vz1_10 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(2,1)
                        uvx1_10 = unpack("<h", f.read(2))[0] / 4096
                        uvy1_10 = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        vertices2k.append([vx1_10,vz1_10,vy1_10])

                    f.seek(122,1)
                    facecount = unpack("B", f.read(1))[0]
                    flagsC = unpack("B", f.read(1))[0]
                    if flagsC == 0x6E:
                        if facecount == 5:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaak = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fm1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fn1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fo1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fp1aaak = unpack("B", f.read(1))[0] & 0x2F
                            fq1aaak = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(2,1)
                            
                            fa1aaak//=3
                            fb1aaak//=3
                            fc1aaak//=3
                            fd1aaak//=3
                            fe1aaak//=3
                            ff1aaak//=3
                            fg1aaak//=3
                            fh1aaak//=3
                            fi1aaak//=3
                            fj1aaak//=3
                            fk1aaak//=3
                            fl1aaak//=3
                            fm1aaak//=3
                            fn1aaak//=3
                            fo1aaak//=3
                            fp1aaak//=3
                            fq1aaak//=3

                            fa1aaak+=1*len(vertices2k)-14
                            fb1aaak+=1*len(vertices2k)-14
                            fc1aaak+=1*len(vertices2k)-14
                            fd1aaak+=1*len(vertices2k)-14
                            fe1aaak+=1*len(vertices2k)-14
                            ff1aaak+=1*len(vertices2k)-14
                            fg1aaak+=1*len(vertices2k)-14
                            fh1aaak+=1*len(vertices2k)-14
                            fi1aaak+=1*len(vertices2k)-14
                            fj1aaak+=1*len(vertices2k)-14
                            fk1aaak+=1*len(vertices2k)-14
                            fl1aaak+=1*len(vertices2k)-14
                            fm1aaak+=1*len(vertices2k)-14
                            fn1aaak+=1*len(vertices2k)-14
                            fo1aaak+=1*len(vertices2k)-14
                            fp1aaak+=1*len(vertices2k)-14
                            fq1aaak+=1*len(vertices2k)-14

                            faces2k.append([fa1aaak,fb1aaak,fc1aaak])
                            faces2k.append([fb1aaak,fc1aaak,fd1aaak])
                            faces2k.append([fd1aaak,fe1aaak,ff1aaak])
                            faces2k.append([fg1aaak,fh1aaak,fi1aaak])
                            faces2k.append([fh1aaak,fi1aaak,fj1aaak])
                            faces2k.append([fi1aaak,fj1aaak,fk1aaak])
                            faces2k.append([fj1aaak,fk1aaak,fl1aaak])
                            faces2k.append([fk1aaak,fl1aaak,fm1aaak])
                            faces2k.append([fl1aaak,fm1aaak,fn1aaak])
                            faces2k.append([fm1aaak,fn1aaak,fo1aaak])
                            faces2k.append([fn1aaak,fo1aaak,fp1aaak])
                            faces2k.append([fo1aaak,fp1aaak,fq1aaak])

                        elif facecount == 4:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaaka = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(3,1)
                            
                            fa1aaaka//=3
                            fb1aaaka//=3
                            fc1aaaka//=3
                            fd1aaaka//=3
                            fe1aaaka//=3
                            ff1aaaka//=3
                            fg1aaaka//=3
                            fh1aaaka//=3
                            fi1aaaka//=3
                            fj1aaaka//=3
                            fk1aaaka//=3
                            fl1aaaka//=3

                            fa1aaaka+=1*len(vertices2k)-14
                            fb1aaaka+=1*len(vertices2k)-14
                            fc1aaaka+=1*len(vertices2k)-14
                            fd1aaaka+=1*len(vertices2k)-14
                            fe1aaaka+=1*len(vertices2k)-14
                            ff1aaaka+=1*len(vertices2k)-14
                            fg1aaaka+=1*len(vertices2k)-14
                            fh1aaaka+=1*len(vertices2k)-14
                            fi1aaaka+=1*len(vertices2k)-14
                            fj1aaaka+=1*len(vertices2k)-14
                            fk1aaaka+=1*len(vertices2k)-14
                            fl1aaaka+=1*len(vertices2k)-14

                            faces2k.append([fa1aaaka,fb1aaaka,fc1aaaka])
                            faces2k.append([fb1aaaka,fc1aaaka,fd1aaaka])
                            faces2k.append([fd1aaaka,fe1aaaka,ff1aaaka])
                            faces2k.append([fg1aaaka,fh1aaaka,fi1aaaka])
                            faces2k.append([fh1aaaka,fi1aaaka,fj1aaaka])
                            faces2k.append([fi1aaaka,fj1aaaka,fk1aaaka])
                            faces2k.append([fj1aaaka,fk1aaaka,fl1aaaka])

                        elif facecount == 6:
                            
                            id1 = unpack("B", f.read(1))[0]
                            fa1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fb1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fc1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fd1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fe1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            ff1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fg1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fh1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fi1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fj1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fk1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            fl1aaakb = unpack("B", f.read(1))[0] & 0x2F
                            f.seek(5,1)
                            
                            fa1aaakb//=3
                            fb1aaakb//=3
                            fc1aaakb//=3
                            fd1aaakb//=3
                            fe1aaakb//=3
                            ff1aaakb//=3
                            fg1aaakb//=3
                            fh1aaakb//=3
                            fi1aaakb//=3
                            fj1aaakb//=3
                            fk1aaakb//=3
                            fl1aaakb//=3

                            fa1aaakb+=1*len(vertices2k)-14
                            fb1aaakb+=1*len(vertices2k)-14
                            fc1aaakb+=1*len(vertices2k)-14
                            fd1aaakb+=1*len(vertices2k)-14
                            fe1aaakb+=1*len(vertices2k)-14
                            ff1aaakb+=1*len(vertices2k)-14
                            fg1aaakb+=1*len(vertices2k)-14
                            fh1aaakb+=1*len(vertices2k)-14
                            fi1aaakb+=1*len(vertices2k)-14
                            fj1aaakb+=1*len(vertices2k)-14
                            fk1aaakb+=1*len(vertices2k)-14
                            fl1aaakb+=1*len(vertices2k)-14

                            faces2k.append([fa1aaakb,fb1aaakb,fc1aaakb])
                            faces2k.append([fb1aaakb,fc1aaakb,fd1aaakb])
                            faces2k.append([fd1aaakb,fe1aaakb,ff1aaakb])
                            faces2k.append([fg1aaakb,fh1aaakb,fi1aaakb])
                            faces2k.append([fh1aaakb,fi1aaakb,fj1aaakb])
                            faces2k.append([fi1aaakb,fj1aaakb,fk1aaakb])
                            faces2k.append([fj1aaakb,fk1aaakb,fl1aaakb])

                        

                    
                            
                    
                    
                    
                    
                                
                    
                
        elif Chunks == b"\x04\x02\x00\x01":
            f.seek(1,1)
            value1 = unpack("B", f.read(1))[0]
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2 = unpack("B", f.read(1))[0]
            if flag2 == 0x6C:
                if vertexCount == 0:
                    pass
                elif vertexCount == 1:
                    pass
                elif vertexCount == 2:
                    pass
                elif vertexCount == 3:
                    for j in range(1):
                        
                        vx0001__ = unpack("<f", f.read(4))[0]
                        vy0001__ = unpack("<f", f.read(4))[0]
                        vz0001__ = unpack("<f", f.read(4))[0]
                        brightness1__ = unpack("<f", f.read(4))[0]
                        uvx0001__ = unpack("<f", f.read(4))[0]
                        uvy0001__ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__A = unpack("<f", f.read(4))[0]
                        vy0001__A = unpack("<f", f.read(4))[0]
                        vz0001__A = unpack("<f", f.read(4))[0]
                        brightness1__A = unpack("<f", f.read(4))[0]
                        uvx0001__A = unpack("<f", f.read(4))[0]
                        uvy0001__A = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4A = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__B = unpack("<f", f.read(4))[0]
                        vy0001__B = unpack("<f", f.read(4))[0]
                        vz0001__B = unpack("<f", f.read(4))[0]
                        brightness1__B = unpack("<f", f.read(4))[0]
                        uvx0001__B = unpack("<f", f.read(4))[0]
                        uvy0001__B = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4B = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for i in range(1):
                        vx0001__C = unpack("<f", f.read(4))[0]
                        vy0001__C = unpack("<f", f.read(4))[0]
                        vz0001__C = unpack("<f", f.read(4))[0]
                        brightness1__C = unpack("<f", f.read(4))[0]
                        uvx0001__C = unpack("<f", f.read(4))[0]
                        uvy0001__C = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4C = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__D = unpack("<f", f.read(4))[0]
                        vy0001__D = unpack("<f", f.read(4))[0]
                        vz0001__D = unpack("<f", f.read(4))[0]
                        brightness1__D = unpack("<f", f.read(4))[0]
                        uvx0001__D = unpack("<f", f.read(4))[0]
                        uvy0001__D = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4D = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__E = unpack("<f", f.read(4))[0]
                        vy0001__E = unpack("<f", f.read(4))[0]
                        vz0001__E = unpack("<f", f.read(4))[0]
                        brightness1__E = unpack("<f", f.read(4))[0]
                        uvx0001__E = unpack("<f", f.read(4))[0]
                        uvy0001__E = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4E = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for i in range(1):
                        vx0001__N = unpack("<f", f.read(4))[0]
                        vy0001__N = unpack("<f", f.read(4))[0]
                        vz0001__N = unpack("<f", f.read(4))[0]
                        brightness1__N = unpack("<f", f.read(4))[0]
                        uvx0001__N = unpack("<f", f.read(4))[0]
                        uvy0001__N = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4N = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__O = unpack("<f", f.read(4))[0]
                        vy0001__O = unpack("<f", f.read(4))[0]
                        vz0001__O = unpack("<f", f.read(4))[0]
                        brightness1__O = unpack("<f", f.read(4))[0]
                        uvx0001__O = unpack("<f", f.read(4))[0]
                        uvy0001__O = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4O = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__P = unpack("<f", f.read(4))[0]
                        vy0001__P = unpack("<f", f.read(4))[0]
                        vz0001__P = unpack("<f", f.read(4))[0]
                        brightness1__P = unpack("<f", f.read(4))[0]
                        uvx0001__P = unpack("<f", f.read(4))[0]
                        uvy0001__P = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4P = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    offsettA = unpack("<I", f.read(4))[0]
                    if offsettA == 1627553807:
                        offsetB = unpack("<I", f.read(4))[0]
                        if offsetB != 65538:
                            f.seek(-4,1)
                            offsetC = unpack("<I", f.read(4))[0]
                            if offsetC == 65539:
                                f.seek(2,1)
                                vcount2 = unpack("B", f.read(1))[0]
                                vflag2 = unpack("B", f.read(1))[0]
                                if vflag2 == 0x6C:
                                    #missing verts
                                    if vcount2 == 4:
                                        for i in range(1):
                                            vx0001__J = unpack("<f", f.read(4))[0]
                                            vy0001__J = unpack("<f", f.read(4))[0]
                                            vz0001__J = unpack("<f", f.read(4))[0]
                                            type4J = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                            vx0001__K = unpack("<f", f.read(4))[0]
                                            vy0001__K = unpack("<f", f.read(4))[0]
                                            vz0001__K = unpack("<f", f.read(4))[0]
                                            type4K = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                            vx0001__L = unpack("<f", f.read(4))[0]
                                            vy0001__L = unpack("<f", f.read(4))[0]
                                            vz0001__L = unpack("<f", f.read(4))[0]
                                            type4L = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                            vx0001__M = unpack("<f", f.read(4))[0]
                                            vy0001__M = unpack("<f", f.read(4))[0]
                                            vz0001__M = unpack("<f", f.read(4))[0]
                                            type4M = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                        offsettC = unpack("<I", f.read(4))[0]
                                        if offsettC == 16777473:
                                            if type4J == 0:
                                                if type4K == 1:
                                                    if type4L == 0:
                                                        if type4M == 0:
                                                            vertices3Aaq.append([vx0001__N,vz0001__N,vy0001__N])
                                                            vertices3Aaq.append([vx0001__O,vz0001__O,vy0001__O])
                                                            vertices3Aaq.append([vx0001__P,vz0001__P,vy0001__P])

                                                            vertices3Aaq.append([vx0001__J,vz0001__J,vy0001__J])
                                                            vertices3Aaq.append([vx0001__L,vz0001__L,vy0001__L])
                                                            vertices3Aaq.append([vx0001__M,vz0001__M,vy0001__M])

                                                            fa2Ta_b+=1*5
                                                            fb2Ta_b+=1*5
                                                            fc2Ta_b+=1*5
                                                            fd2Ta_b+=1*5
                                                            fe2Ta_b+=1*5

                                                            faces3Aaq.append([fa2Ta_b,fb2Ta_b,fc2Ta_b])
                                                            faces3Aaq.append([fb2Ta_b,fc2Ta_b,fd2Ta_b])
                                                            faces3Aaq.append([fc2Ta_b,fd2Ta_b,fe2Ta_b])
                        elif offsetB == 65538:
                            f.seek(2,1)
                            vcount1 = unpack("B", f.read(1))[0]
                            vflag1 = unpack("B", f.read(1))[0]
                            if vflag1 == 0x6C:
                                #missing verts
                                if vcount1 == 4:
                                    for i in range(1):
                                        vx0001__F = unpack("<f", f.read(4))[0]
                                        vy0001__F = unpack("<f", f.read(4))[0]
                                        vz0001__F = unpack("<f", f.read(4))[0]
                                        type4F = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__G = unpack("<f", f.read(4))[0]
                                        vy0001__G = unpack("<f", f.read(4))[0]
                                        vz0001__G = unpack("<f", f.read(4))[0]
                                        type4G = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__H = unpack("<f", f.read(4))[0]
                                        vy0001__H = unpack("<f", f.read(4))[0]
                                        vz0001__H = unpack("<f", f.read(4))[0]
                                        type4H = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__I = unpack("<f", f.read(4))[0]
                                        vy0001__I = unpack("<f", f.read(4))[0]
                                        vz0001__I = unpack("<f", f.read(4))[0]
                                        type4I = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                    offsettB = unpack("<I", f.read(4))[0]
                                    if offsettB == 16777473:
                                        if type4F == 0:
                                            if type4G == 1:
                                                if type4H == 0:
                                                    if type4I == 0:
                                                        vertices3A.append([vx0001__C,vz0001__C,vy0001__C])
                                                        vertices3A.append([vx0001__D,vz0001__D,vy0001__D])
                                                        vertices3A.append([vx0001__E,vz0001__E,vy0001__E])

                                                        vertices3A.append([vx0001__F,vz0001__F,vy0001__F])
                                                        vertices3A.append([vx0001__H,vz0001__H,vy0001__H])
                                                        vertices3A.append([vx0001__I,vz0001__I,vy0001__I])

                                                        fa2Ta_a+=1*5
                                                        fb2Ta_a+=1*5
                                                        fc2Ta_a+=1*5
                                                        fd2Ta_a+=1*5
                                                        fe2Ta_a+=1*5

                                                        faces3A.append([fa2Ta_a,fb2Ta_a,fc2Ta_a])
                                                        faces3A.append([fb2Ta_a,fc2Ta_a,fd2Ta_a])
                                                        faces3A.append([fc2Ta_a,fd2Ta_a,fe2Ta_a])
                    elif offsettA == 16777473:
                        if type4 == 1:
                            if type4A == 1:
                                if type4B == 0:

                                    vertices3.append([vx0001__,vz0001__,vy0001__])
                                    vertices3.append([vx0001__A,vz0001__A,vy0001__A])
                                    vertices3.append([vx0001__B,vz0001__B,vy0001__B])
                                    uv_coords.append([uvx0001__,-uvy0001__])
                                    uv_coords.append([uvx0001__A,-uvy0001__A])
                                    uv_coords.append([uvx0001__B,-uvy0001__B])

                                    fa2+=1*3
                                    fb2+=1*3
                                    fc2+=1*3

                                    faces3.append([fa2,fb2,fc2])

                elif vertexCount == 4:
                    for j in range(1):
                        vx0001__AA = unpack("<f", f.read(4))[0]
                        vy0001__AA = unpack("<f", f.read(4))[0]
                        vz0001__AA = unpack("<f", f.read(4))[0]
                        brightness1__AA = unpack("<f", f.read(4))[0]
                        uvx0001__AA = unpack("<f", f.read(4))[0]
                        uvy0001__AA = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB = unpack("<f", f.read(4))[0]
                        vy0001__AB = unpack("<f", f.read(4))[0]
                        vz0001__AB = unpack("<f", f.read(4))[0]
                        brightness1__AB = unpack("<f", f.read(4))[0]
                        uvx0001__AB = unpack("<f", f.read(4))[0]
                        uvy0001__AB = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC = unpack("<f", f.read(4))[0]
                        vy0001__AC = unpack("<f", f.read(4))[0]
                        vz0001__AC = unpack("<f", f.read(4))[0]
                        brightness1__AC = unpack("<f", f.read(4))[0]
                        uvx0001__AC = unpack("<f", f.read(4))[0]
                        uvy0001__AC = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD = unpack("<f", f.read(4))[0]
                        vy0001__AD = unpack("<f", f.read(4))[0]
                        vz0001__AD = unpack("<f", f.read(4))[0]
                        brightness1__AD = unpack("<f", f.read(4))[0]
                        uvx0001__AD = unpack("<f", f.read(4))[0]
                        uvy0001__AD = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA_ = unpack("<f", f.read(4))[0]
                        vy0001__AA_ = unpack("<f", f.read(4))[0]
                        vz0001__AA_ = unpack("<f", f.read(4))[0]
                        brightness1__AA_ = unpack("<f", f.read(4))[0]
                        uvx0001__AA_ = unpack("<f", f.read(4))[0]
                        uvy0001__AA_ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA_ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB_ = unpack("<f", f.read(4))[0]
                        vy0001__AB_ = unpack("<f", f.read(4))[0]
                        vz0001__AB_ = unpack("<f", f.read(4))[0]
                        brightness1__AB_ = unpack("<f", f.read(4))[0]
                        uvx0001__AB_ = unpack("<f", f.read(4))[0]
                        uvy0001__AB_ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB_ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC_ = unpack("<f", f.read(4))[0]
                        vy0001__AC_ = unpack("<f", f.read(4))[0]
                        vz0001__AC_ = unpack("<f", f.read(4))[0]
                        brightness1__AC_ = unpack("<f", f.read(4))[0]
                        uvx0001__AC_ = unpack("<f", f.read(4))[0]
                        uvy0001__AC_ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC_ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD_ = unpack("<f", f.read(4))[0]
                        vy0001__AD_ = unpack("<f", f.read(4))[0]
                        vz0001__AD_ = unpack("<f", f.read(4))[0]
                        brightness1__AD_ = unpack("<f", f.read(4))[0]
                        uvx0001__AD_ = unpack("<f", f.read(4))[0]
                        uvy0001__AD_ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD_ = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA__ = unpack("<f", f.read(4))[0]
                        vy0001__AA__ = unpack("<f", f.read(4))[0]
                        vz0001__AA__ = unpack("<f", f.read(4))[0]
                        brightness1__AA__ = unpack("<f", f.read(4))[0]
                        uvx0001__AA__ = unpack("<f", f.read(4))[0]
                        uvy0001__AA__ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA__ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB__ = unpack("<f", f.read(4))[0]
                        vy0001__AB__ = unpack("<f", f.read(4))[0]
                        vz0001__AB__ = unpack("<f", f.read(4))[0]
                        brightness1__AB__ = unpack("<f", f.read(4))[0]
                        uvx0001__AB__ = unpack("<f", f.read(4))[0]
                        uvy0001__AB__ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB__ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC__ = unpack("<f", f.read(4))[0]
                        vy0001__AC__ = unpack("<f", f.read(4))[0]
                        vz0001__AC__ = unpack("<f", f.read(4))[0]
                        brightness1__AC__ = unpack("<f", f.read(4))[0]
                        uvx0001__AC__ = unpack("<f", f.read(4))[0]
                        uvy0001__AC__ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC__ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD__ = unpack("<f", f.read(4))[0]
                        vy0001__AD__ = unpack("<f", f.read(4))[0]
                        vz0001__AD__ = unpack("<f", f.read(4))[0]
                        brightness1__AD__ = unpack("<f", f.read(4))[0]
                        uvx0001__AD__ = unpack("<f", f.read(4))[0]
                        uvy0001__AD__ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD__ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___ = unpack("<f", f.read(4))[0]
                        vy0001__AA___ = unpack("<f", f.read(4))[0]
                        vz0001__AA___ = unpack("<f", f.read(4))[0]
                        brightness1__AA___ = unpack("<f", f.read(4))[0]
                        uvx0001__AA___ = unpack("<f", f.read(4))[0]
                        uvy0001__AA___ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___ = unpack("<f", f.read(4))[0]
                        vy0001__AB___ = unpack("<f", f.read(4))[0]
                        vz0001__AB___ = unpack("<f", f.read(4))[0]
                        brightness1__AB___ = unpack("<f", f.read(4))[0]
                        uvx0001__AB___ = unpack("<f", f.read(4))[0]
                        uvy0001__AB___ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___ = unpack("<f", f.read(4))[0]
                        vy0001__AC___ = unpack("<f", f.read(4))[0]
                        vz0001__AC___ = unpack("<f", f.read(4))[0]
                        brightness1__AC___ = unpack("<f", f.read(4))[0]
                        uvx0001__AC___ = unpack("<f", f.read(4))[0]
                        uvy0001__AC___ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___ = unpack("<f", f.read(4))[0]
                        vy0001__AD___ = unpack("<f", f.read(4))[0]
                        vz0001__AD___ = unpack("<f", f.read(4))[0]
                        brightness1__AD___ = unpack("<f", f.read(4))[0]
                        uvx0001__AD___ = unpack("<f", f.read(4))[0]
                        uvy0001__AD___ = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___ = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1a = unpack("<f", f.read(4))[0]
                        vy0001__AA___1a = unpack("<f", f.read(4))[0]
                        vz0001__AA___1a = unpack("<f", f.read(4))[0]
                        brightness1__AA___1a = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1a = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1a = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1a = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1a = unpack("<f", f.read(4))[0]
                        vy0001__AB___1a = unpack("<f", f.read(4))[0]
                        vz0001__AB___1a = unpack("<f", f.read(4))[0]
                        brightness1__AB___1a = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1a = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1a = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1a = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1a = unpack("<f", f.read(4))[0]
                        vy0001__AC___1a = unpack("<f", f.read(4))[0]
                        vz0001__AC___1a = unpack("<f", f.read(4))[0]
                        brightness1__AC___1a = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1a = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1a = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1a = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1a = unpack("<f", f.read(4))[0]
                        vy0001__AD___1a = unpack("<f", f.read(4))[0]
                        vz0001__AD___1a = unpack("<f", f.read(4))[0]
                        brightness1__AD___1a = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1a = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1a = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1a = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aa = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aa = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aa = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aa = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aa = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aa = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aa = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aa = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aa = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aa = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aa = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aa = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aa = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aa = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aa = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aa = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aa = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aa = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aa = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aa = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aa = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aa = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aa = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aa = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aa = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aa = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aa = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aa = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaCoco = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaCoco = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaCoco = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaCoco = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaCoco = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaCoco = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaCoco = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaCoco = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaCoco1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaCoco1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaCoco1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaCoco1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaCoco1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaCoco1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaCoco1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaCoco1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord1 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord1 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord2 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord2 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord2 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord2 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord2 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord3 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord3 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord3 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord3 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord3 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord4 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord4 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord4 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord4 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord4 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord5 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord5 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord5 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord5 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord5 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord6 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord6 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord6 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord6 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord6 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                    for i in range(vertexCount):
                        f.seek(-32,1)
                    for j in range(1):
                        vx0001__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vy0001__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vz0001__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        brightness1__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvx0001__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvy0001__AA___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AA___1aaOverlord7 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vy0001__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vz0001__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        brightness1__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvx0001__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvy0001__AB___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AB___1aaOverlord7 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vy0001__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vz0001__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        brightness1__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvx0001__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvy0001__AC___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AC___1aaOverlord7 = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vy0001__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        vz0001__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        brightness1__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvx0001__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        uvy0001__AD___1aaOverlord7 = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4AD___1aaOverlord7 = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                    offffsetA = unpack("<I", f.read(4))[0]
                    if offffsetA == 16777473:
                        if type4AA_ == 1:
                            if type4AB_ == 1:
                                if type4AC_ == 0:
                                    if type4AD_ == 0:
                                        vertices3Caq.append([vx0001__AA_,vz0001__AA_,vy0001__AA_])
                                        vertices3Caq.append([vx0001__AB_,vz0001__AB_,vy0001__AB_])
                                        vertices3Caq.append([vx0001__AC_,vz0001__AC_,vy0001__AC_])
                                        vertices3Caq.append([vx0001__AD_,vz0001__AD_,vy0001__AD_])

                                        fa2CAQ+=1*4
                                        fb2CAQ+=1*4
                                        fc2CAQ+=1*4

                                        fa3CAQ+=1*4

                                        faces3Caq.append([fa2CAQ,fb2CAQ,fc2CAQ])
                                        faces3Caq.append([fb2CAQ,fc2CAQ,fa3CAQ])
                    elif offffsetA == 1627553811:
                        offffsetB = unpack("<I", f.read(4))[0]
                        if offffsetB == 65540:
                            ofssetA = unpack("<I", f.read(4))[0]
                            if ofssetA != 1627553815:
                                f.seek(-4,1)
                                f.seek(2,1)
                                vaao01 = unpack("B", f.read(1))[0]
                                vaaoFlag01 = unpack("B", f.read(1))[0]
                                if vaaoFlag01 == 0x6C:
                                    if vaao01 == 8:
                                        for i in range(1):
                                            vx0001__AF_8aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_8aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_8aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_8aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_9aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_9aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_9aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_9aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_10aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_10aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_10aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_10aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_11aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_11aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_11aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_11aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_12aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_12aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_12aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_12aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_13aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_13aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_13aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_13aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_14aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_14aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_14aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_14aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_15aOverlord = unpack("<f", f.read(4))[0]
                                            vy0001__AF_15aOverlord = unpack("<f", f.read(4))[0]
                                            vz0001__AF_15aOverlord = unpack("<f", f.read(4))[0]
                                            type1__AF_15aOverlord = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                        overlordthehedgeoffset01 = unpack("<I", f.read(4))[0]
                                        if overlordthehedgeoffset01 == 1627553831:
                                            overlordhedgenum01 = unpack("<I", f.read(4))[0]
                                            if overlordhedgenum01 == 65544:
                                                f.seek(2,1)
                                                ovverlordccountty = unpack("B", f.read(1))[0]
                                                ovverlordfflagg01 = unpack("B", f.read(1))[0]
                                                if ovverlordfflagg01 == 0x6C:
                                                    if ovverlordccountty == 2:
                                                        #0x29504
                                                        for i in range(1):
                                                            vx0001__AF_15aOverlorda = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_15aOverlorda = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_15aOverlorda = unpack("<f", f.read(4))[0]
                                                            type1__AF_15aOverlorda = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_16aOverlorda = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_16aOverlorda = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_16aOverlorda = unpack("<f", f.read(4))[0]
                                                            type1__AF_16aOverlorda = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                        overlordVoffset01 = unpack("<I", f.read(4))[0]
                                                        if overlordVoffset01 == 1627553839:
                                                            overlordis6yrsold = unpack("<I", f.read(4))[0]
                                                            if overlordis6yrsold == 6:
                                                                f.seek(2,1)
                                                                ovverlordccountty01 = unpack("B", f.read(1))[0]
                                                                ovverlordfflagg001 = unpack("B", f.read(1))[0]
                                                                if ovverlordfflagg001 == 0x6C:
                                                                    if ovverlordccountty01 == 16:
                                                                        for i in range(1):
                                                                            vx0001__AF_17aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_17aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_17aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_17aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_18aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_18aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_18aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_18aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_19aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_19aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_19aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_19aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_20aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_20aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_20aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_20aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_21aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_21aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_21aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_21aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_22aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_22aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_22aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_22aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_23aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_23aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_23aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_23aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_24aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_24aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_24aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_24aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_25aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_26aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_25aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_25aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_26aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_26aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_27aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_27aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_27aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_27aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_28aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_28aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_28aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_28aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_29aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_29aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_29aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_29aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                            vx0001__AF_30aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vy0001__AF_30aOverlorda = unpack("<f", f.read(4))[0]
                                                                            vz0001__AF_30aOverlorda = unpack("<f", f.read(4))[0]
                                                                            type1__AF_30aOverlorda = unpack("B", f.read(1))[0]
                                                                            f.seek(3,1)

                                                                        overlordSEnd01 = unpack("<I", f.read(4))[0]
                                                                        if overlordSEnd01 == 1627553875:
                                                                            overlordSEndNUM01 = unpack("<I", f.read(4))[0]
                                                                            if overlordSEndNUM01 == 65538:
                                                                                overlordSEEnd01 = unpack("<I", f.read(4))[0]
                                                                                if overlordSEEnd01 == 1627553879:
                                                                                    overlordis4yrsolds = unpack("<I", f.read(4))[0]
                                                                                    if overlordis4yrsolds == 4:
                                                                                        f.seek(2,1)
                                                                                        #29620
                                                                                        overlordcount6 = unpack("B", f.read(1))[0]
                                                                                        overlordflag6 = unpack("B", f.read(1))[0]
                                                                                        if overlordflag6 == 0x6C:
                                                                                            if overlordcount6 == 6:
                                                                                                for i in range(1):
                                                                                                    vx0001__AF_31aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_31aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_31aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_31aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                    vx0001__AF_32aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_32aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_32aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_32aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                    vx0001__AF_33aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_33aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_33aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_33aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                    vx0001__AF_34aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_34aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_34aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_34aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                    vx0001__AF_35aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_35aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_35aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_35aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                    vx0001__AF_36aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vy0001__AF_36aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    vz0001__AF_36aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                    type1__AF_36aOverlorda = unpack("B", f.read(1))[0]
                                                                                                    f.seek(3,1)

                                                                                                overlorddmm = unpack("<I", f.read(4))[0]
                                                                                                if overlorddmm == 1627553895:
                                                                                                    #0x296D0
                                                                                                    overlloort01 = unpack("<I", f.read(4))[0]
                                                                                                    if overlloort01 == 65561:
                                                                                                        f.seek(2,1)
                                                                                                        overlorddmmCount01 = unpack("B", f.read(1))[0]
                                                                                                        overlorddmmFlsg01 = unpack("B", f.read(1))[0]
                                                                                                        if overlorddmmFlsg01 == 0x6C:
                                                                                                            if overlorddmmCount01 == 4:
                                                                                                                for i in range(1):
                                                                                                                    vx0001__AF_37aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vy0001__AF_37aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vz0001__AF_37aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    type1__AF_37aOverlorda = unpack("B", f.read(1))[0]
                                                                                                                    f.seek(3,1)

                                                                                                                    vx0001__AF_38aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vy0001__AF_38aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vz0001__AF_38aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    type1__AF_38aOverlorda = unpack("B", f.read(1))[0]
                                                                                                                    f.seek(3,1)

                                                                                                                    vx0001__AF_39aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vy0001__AF_39aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vz0001__AF_39aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    type1__AF_39aOverlorda = unpack("B", f.read(1))[0]
                                                                                                                    f.seek(3,1)

                                                                                                                    vx0001__AF_40aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vy0001__AF_40aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    vz0001__AF_40aOverlorda = unpack("<f", f.read(4))[0]
                                                                                                                    type1__AF_40aOverlorda = unpack("B", f.read(1))[0]
                                                                                                                    f.seek(3,1)

                                                                                                                ovveerrrrrrrrlord = unpack("<I", f.read(4))[0]
                                                                                                                if ovveerrrrrrrrlord == 16777473:
                                                                                                                    if type4AA___1aaOverlord7 == 1:
                                                                                                                        if type4AB___1aaOverlord7 == 1:
                                                                                                                            if type4AC___1aaOverlord7 == 0:
                                                                                                                                if type4AD___1aaOverlord7 == 0:
                                                                                                                                    if type1__AF_8aOverlord == 0:
                                                                                                                                        if type1__AF_9aOverlord == 1:
                                                                                                                                            if type1__AF_10aOverlord == 0:
                                                                                                                                                if type1__AF_11aOverlord == 0:
                                                                                                                                                    if type1__AF_12aOverlord == 0:
                                                                                                                                                        if type1__AF_13aOverlord == 0:
                                                                                                                                                            if type1__AF_14aOverlord == 0:
                                                                                                                                                                if type1__AF_15aOverlord == 1:
                                                                                                                                                                    if type1__AF_15aOverlorda == 0:
                                                                                                                                                                        if type1__AF_16aOverlorda == 0:
                                                                                                                                                                            if type1__AF_17aOverlorda == 0:
                                                                                                                                                                                if type1__AF_18aOverlorda == 0:
                                                                                                                                                                                    if type1__AF_19aOverlorda == 0:
                                                                                                                                                                                        if type1__AF_20aOverlorda == 0:
                                                                                                                                                                                            if type1__AF_21aOverlorda == 0:
                                                                                                                                                                                                if type1__AF_22aOverlorda == 0:
                                                                                                                                                                                                    if type1__AF_23aOverlorda == 0:
                                                                                                                                                                                                        if type1__AF_24aOverlorda == 1:
                                                                                                                                                                                                            if type1__AF_25aOverlorda == 0:
                                                                                                                                                                                                                if type1__AF_26aOverlorda == 0:
                                                                                                                                                                                                                    if type1__AF_27aOverlorda == 0:
                                                                                                                                                                                                                        if type1__AF_28aOverlorda == 0:
                                                                                                                                                                                                                            if type1__AF_29aOverlorda == 0:
                                                                                                                                                                                                                                if type1__AF_30aOverlorda == 1:
                                                                                                                                                                                                                                    if type1__AF_31aOverlorda == 0:
                                                                                                                                                                                                                                        if type1__AF_32aOverlorda == 1:
                                                                                                                                                                                                                                            if type1__AF_33aOverlorda == 0:
                                                                                                                                                                                                                                                if type1__AF_34aOverlorda == 1:
                                                                                                                                                                                                                                                    if type1__AF_35aOverlorda == 0:
                                                                                                                                                                                                                                                        if type1__AF_36aOverlorda == 0:
                                                                                                                                                                                                                                                            if type1__AF_37aOverlorda == 0:
                                                                                                                                                                                                                                                                if type1__AF_38aOverlorda == 1:
                                                                                                                                                                                                                                                                    if type1__AF_39aOverlorda == 0:
                                                                                                                                                                                                                                                                        if type1__AF_40aOverlorda == 0:
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AA___1aaOverlord7,vz0001__AA___1aaOverlord7,vy0001__AA___1aaOverlord7])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AB___1aaOverlord7,vz0001__AB___1aaOverlord7,vy0001__AB___1aaOverlord7])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AC___1aaOverlord7,vz0001__AC___1aaOverlord7,vy0001__AC___1aaOverlord7])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AD___1aaOverlord7,vz0001__AD___1aaOverlord7,vy0001__AD___1aaOverlord7])

                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_8aOverlord,vz0001__AF_8aOverlord,vy0001__AF_8aOverlord])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_10aOverlord,vz0001__AF_10aOverlord,vy0001__AF_10aOverlord])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_12aOverlord,vz0001__AF_12aOverlord,vy0001__AF_12aOverlord])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_14aOverlord,vz0001__AF_14aOverlord,vy0001__AF_14aOverlord])

                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_15aOverlorda,vz0001__AF_15aOverlorda,vy0001__AF_15aOverlorda])

                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_17aOverlorda,vz0001__AF_17aOverlorda,vy0001__AF_17aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_19aOverlorda,vz0001__AF_19aOverlorda,vy0001__AF_19aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_21aOverlorda,vz0001__AF_21aOverlorda,vy0001__AF_21aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_23aOverlorda,vz0001__AF_23aOverlorda,vy0001__AF_23aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_25aOverlorda,vz0001__AF_25aOverlorda,vy0001__AF_25aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_27aOverlorda,vz0001__AF_27aOverlorda,vy0001__AF_27aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_29aOverlorda,vz0001__AF_29aOverlorda,vy0001__AF_29aOverlorda])

                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_31aOverlorda,vz0001__AF_31aOverlorda,vy0001__AF_31aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_33aOverlorda,vz0001__AF_33aOverlorda,vy0001__AF_33aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_35aOverlorda,vz0001__AF_35aOverlorda,vy0001__AF_35aOverlorda])

                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_37aOverlorda,vz0001__AF_37aOverlorda,vy0001__AF_37aOverlorda])
                                                                                                                                                                                                                                                                            overlordverts08.append([vx0001__AF_39aOverlorda,vz0001__AF_39aOverlorda,vy0001__AF_39aOverlorda])

                                                                                                                                                                                                                                                                            overlordA8+=1*21
                                                                                                                                                                                                                                                                            overlordB8+=1*21
                                                                                                                                                                                                                                                                            overlordC8+=1*21
                                                                                                                                                                                                                                                                            overlordD8+=1*21
                                                                                                                                                                                                                                                                            overlordE8+=1*21

                                                                                                                                                                                                                                                                            overlordfaces08.append([overlordA8,overlordB8,overlordC8])
                                                                                                                                                                                                                                                                            overlordfaces08.append([overlordB8,overlordC8,overlordD8])
                                                                                                                                                                                                                                                                            overlordfaces08.append([overlordA8,overlordC8,overlordE8])
                                    elif vaao01 == 12:
                                        for i in range(1):
                                            vx0001__AF_8a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_8a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_8a = unpack("<f", f.read(4))[0]
                                            type1__AF_8a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_9a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_9a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_9a = unpack("<f", f.read(4))[0]
                                            type1__AF_9a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_10a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_10a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_10a = unpack("<f", f.read(4))[0]
                                            type1__AF_10a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_11a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_11a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_11a = unpack("<f", f.read(4))[0]
                                            type1__AF_11a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_12a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_12a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_12a = unpack("<f", f.read(4))[0]
                                            type1__AF_12a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_13a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_13a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_13a = unpack("<f", f.read(4))[0]
                                            type1__AF_13a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_14a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_14a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_14a = unpack("<f", f.read(4))[0]
                                            type1__AF_14a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_15a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_15a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_15a = unpack("<f", f.read(4))[0]
                                            type1__AF_15a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_16a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_16a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_16a = unpack("<f", f.read(4))[0]
                                            type1__AF_16a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_17a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_17a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_17a = unpack("<f", f.read(4))[0]
                                            type1__AF_17a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_18a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_18a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_18a = unpack("<f", f.read(4))[0]
                                            type1__AF_18a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                            vx0001__AF_19a = unpack("<f", f.read(4))[0]
                                            vy0001__AF_19a = unpack("<f", f.read(4))[0]
                                            vz0001__AF_19a = unpack("<f", f.read(4))[0]
                                            type1__AF_19a = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                        ofssetBXa1 = unpack("<I", f.read(4))[0]
                                        if ofssetBXa1 == 1627553839:
                                            numX1 = unpack("<I", f.read(4))[0]
                                            if numX1 == 7:
                                                ofssetBXa2 = unpack("<I", f.read(4))[0]
                                                if ofssetBXa2 == 1627553843:
                                                    numX2 = unpack("<I", f.read(4))[0]
                                                    if numX2 == 9:
                                                        f.seek(2,1)
                                                        vvvcount1xx = unpack("B", f.read(1))[0]
                                                        ffflag1xx = unpack("B", f.read(1))[0]
                                                        if ffflag1xx == 0x6C:
                                                            if vvvcount1xx == 2:
                                                                for i in range(1):
                                                                    vx0001__AF_20a = unpack("<f", f.read(4))[0]
                                                                    vy0001__AF_20a = unpack("<f", f.read(4))[0]
                                                                    vz0001__AF_20a = unpack("<f", f.read(4))[0]
                                                                    type1__AF_20a = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AF_21a = unpack("<f", f.read(4))[0]
                                                                    vy0001__AF_21a = unpack("<f", f.read(4))[0]
                                                                    vz0001__AF_21a = unpack("<f", f.read(4))[0]
                                                                    type1__AF_21a = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                ofssetBXa2 = unpack("<I", f.read(4))[0]
                                                                if ofssetBXa2 == 1627553851:
                                                                    numX2 = unpack("<I", f.read(4))[0]
                                                                    if numX2 == 65546:
                                                                        f.seek(2,1)
                                                                        vvvcount2xx = unpack("B", f.read(1))[0]
                                                                        ffflag2xx = unpack("B", f.read(1))[0]
                                                                        if ffflag2xx == 0x6C:
                                                                            if vvvcount2xx == 2:
                                                                                for i in range(1):
                                                                                    vx0001__AF_22a = unpack("<f", f.read(4))[0]
                                                                                    vy0001__AF_22a = unpack("<f", f.read(4))[0]
                                                                                    vz0001__AF_22a = unpack("<f", f.read(4))[0]
                                                                                    type1__AF_22a = unpack("B", f.read(1))[0]
                                                                                    f.seek(3,1)

                                                                                    vx0001__AF_23a = unpack("<f", f.read(4))[0]
                                                                                    vy0001__AF_23a = unpack("<f", f.read(4))[0]
                                                                                    vz0001__AF_23a = unpack("<f", f.read(4))[0]
                                                                                    type1__AF_23a = unpack("B", f.read(1))[0]
                                                                                    f.seek(3,1)

                                                                                EdgesEnd01 = unpack("<I", f.read(4))[0]
                                                                                if EdgesEnd01 == 16777473:
                                                                                    if type4AA___1aa == 1:
                                                                                        if type4AB___1aa == 1:
                                                                                            if type4AC___1aa == 0:
                                                                                                if type4AD___1aa == 0:
                                                                                                    if type1__AF_8a == 0:
                                                                                                        if type1__AF_9a == 1:
                                                                                                            if type1__AF_10a == 0:
                                                                                                                if type1__AF_11a == 0:
                                                                                                                    if type1__AF_12a == 0:
                                                                                                                        if type1__AF_13a == 0:
                                                                                                                            if type1__AF_14a == 0:
                                                                                                                                if type1__AF_15a == 0:
                                                                                                                                    if type1__AF_16a == 0:
                                                                                                                                        if type1__AF_17a == 1:
                                                                                                                                            if type1__AF_18a == 0:
                                                                                                                                                if type1__AF_19a == 1:
                                                                                                                                                    if type1__AF_20a == 0:
                                                                                                                                                        if type1__AF_21a == 1:
                                                                                                                                                            if type1__AF_22a == 0:
                                                                                                                                                                if type1__AF_23a == 0:
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AA___1aa,vz0001__AA___1aa,vy0001__AA___1aa])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AB___1aa,vz0001__AB___1aa,vy0001__AB___1aa])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AC___1aa,vz0001__AC___1aa,vy0001__AC___1aa])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AD___1aa,vz0001__AD___1aa,vy0001__AD___1aa])

                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_8a,vz0001__AF_8a,vy0001__AF_8a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_10a,vz0001__AF_10a,vy0001__AF_10a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_12a,vz0001__AF_12a,vy0001__AF_12a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_14a,vz0001__AF_14a,vy0001__AF_14a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_16a,vz0001__AF_16a,vy0001__AF_16a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_18a,vz0001__AF_18a,vy0001__AF_18a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_19a,vz0001__AF_19a,vy0001__AF_19a])
                                                                                                                                                                    vertices3Daqaqaqe.append([vx0001__AF_21a,vz0001__AF_21a,vy0001__AF_21a])

                                                                                                                                                                    fa2Ta_daTaD+=1*12
                                                                                                                                                                    fb2Ta_daTaD+=1*12
                                                                                                                                                                    fc2Ta_daTaD+=1*12
                                                                                                                                                                    fd2Ta_daTaD+=1*12
                                                                                                                                                                    fe2Ta_daTaD+=1*12

                                                                                                                                                                    faces3Daqaqaqe.append([fa2Ta_daTaD,fa2Ta_daTaD,fa2Ta_daTaD])
                                                                                                                                                                    faces3Daqaqaqe.append([fb2Ta_daTaD,fc2Ta_daTaD,fd2Ta_daTaD])
                                                                                                                                                                    faces3Daqaqaqe.append([fc2Ta_daTaD,fd2Ta_daTaD,fe2Ta_daTaD])
                                    elif vaao01 == 2:
                                        for i in range(1):
                                            vx0001__AE_1 = unpack("<f", f.read(4))[0]
                                            vy0001__AE_1 = unpack("<f", f.read(4))[0]
                                            vz0001__AE_1 = unpack("<f", f.read(4))[0]
                                            type1__AE_1 = unpack("B", f.read(1))[0]
                                            f.seek(3,1)
                                            vx0001__AF_1 = unpack("<f", f.read(4))[0]
                                            vy0001__AF_1 = unpack("<f", f.read(4))[0]
                                            vz0001__AF_1 = unpack("<f", f.read(4))[0]
                                            type1__AF_1 = unpack("B", f.read(1))[0]
                                            f.seek(3,1)

                                        noi01 = unpack("<I", f.read(4))[0]
                                        if noi01 == 1627553819:
                                            noiNum01 = unpack("<I", f.read(4))[0]
                                            if noiNum01 == 2:
                                                f.seek(2,1)
                                                vaao02 = unpack("B", f.read(1))[0]
                                                vaaoFlag02 = unpack("B", f.read(1))[0]
                                                if vaaoFlag02 == 0x6C:
                                                    if vaao02 == 4:
                                                        for i in range(1):
                                                            vx0001__AF_2overlord = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_2overlord = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_2overlord = unpack("<f", f.read(4))[0]
                                                            type1__AF_2overlord = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_3overlord = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_3overlord = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_3overlord = unpack("<f", f.read(4))[0]
                                                            type1__AF_3overlord = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_4overlord = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_4overlord = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_4overlord = unpack("<f", f.read(4))[0]
                                                            type1__AF_4overlord = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_5overlord = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_5overlord = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_5overlord = unpack("<f", f.read(4))[0]
                                                            type1__AF_5overlord = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)
                                                        overlordDrunk = unpack("<I", f.read(4))[0]
                                                        if overlordDrunk == 1627553831:
                                                            overlordBeer = unpack("<I", f.read(4))[0]
                                                            if overlordBeer == 65542:
                                                                overlordTheRowdyRuffBoys = unpack("<I", f.read(4))[0]
                                                                if overlordTheRowdyRuffBoys == 1627553835:
                                                                    overlordShorty = unpack("<I", f.read(4))[0]
                                                                    if overlordShorty == 8:
                                                                        overlordEnd01 = unpack("<I", f.read(4))[0]
                                                                        if overlordEnd01 == 16777473:
                                                                            if type4AA___1aaOverlord == 1:
                                                                                if type4AB___1aaOverlord == 1:
                                                                                    if type4AC___1aaOverlord == 0:
                                                                                        if type4AD___1aaOverlord == 0:
                                                                                            if type1__AE_1 == 0:
                                                                                                if type1__AF_1 == 1:
                                                                                                    if type1__AF_2overlord == 0:
                                                                                                        if type1__AF_3overlord == 0:
                                                                                                            if type1__AF_4overlord == 0:
                                                                                                                if type1__AF_5overlord == 1:
                                                                                                                    overlordverts01.append([vx0001__AA___1aaOverlord,vz0001__AA___1aaOverlord,vy0001__AA___1aaOverlord])
                                                                                                                    overlordverts01.append([vx0001__AB___1aaOverlord,vz0001__AB___1aaOverlord,vy0001__AB___1aaOverlord])
                                                                                                                    overlordverts01.append([vx0001__AC___1aaOverlord,vz0001__AC___1aaOverlord,vy0001__AC___1aaOverlord])
                                                                                                                    overlordverts01.append([vx0001__AD___1aaOverlord,vz0001__AD___1aaOverlord,vy0001__AD___1aaOverlord])

                                                                                                                    overlordverts01.append([vx0001__AE_1,vz0001__AE_1,vy0001__AE_1])

                                                                                                                    overlordverts01.append([vx0001__AF_2overlord,vz0001__AF_2overlord,vy0001__AF_2overlord])
                                                                                                                    overlordverts01.append([vx0001__AF_4overlord,vz0001__AF_4overlord,vy0001__AF_4overlord])

                                                                                                                    overlordA1+=1*7
                                                                                                                    overlordB1+=1*7
                                                                                                                    overlordC1+=1*7
                                                                                                                    overlordD1+=1*7
                                                                                                                    overlordE1+=1*7
                                                                                                                    overlordF1+=1*7
                                                                                                                    overlordG1+=1*7

                                                                                                                    overlordfaces01.append([overlordA1,overlordB1,overlordC1])
                                                                                                                    overlordfaces01.append([overlordB1,overlordC1,overlordD1])
                                                                                                                    overlordfaces01.append([overlordB1,overlordD1,overlordE1])
                                                                                                                    overlordfaces01.append([overlordB1,overlordE1,overlordF1])
                                                                                                                    overlordfaces01.append([overlordF1,overlordE1,overlordG1])
                                                    elif vaao02 == 6:
                                                        for i in range(1):
                                                            vx0001__AF_2 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_2 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_2 = unpack("<f", f.read(4))[0]
                                                            type1__AF_2 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_3 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_3 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_3 = unpack("<f", f.read(4))[0]
                                                            type1__AF_3 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_4 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_4 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_4 = unpack("<f", f.read(4))[0]
                                                            type1__AF_4 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_5 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_5 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_5 = unpack("<f", f.read(4))[0]
                                                            type1__AF_5 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_6 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_6 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_6 = unpack("<f", f.read(4))[0]
                                                            type1__AF_6 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                            vx0001__AF_7 = unpack("<f", f.read(4))[0]
                                                            vy0001__AF_7 = unpack("<f", f.read(4))[0]
                                                            vz0001__AF_7 = unpack("<f", f.read(4))[0]
                                                            type1__AF_7 = unpack("B", f.read(1))[0]
                                                            f.seek(3,1)

                                                        noi02 = unpack("<I", f.read(4))[0]
                                                        if noi02 == 1627553835:
                                                            noiNum02 = unpack("<I", f.read(4))[0]
                                                            if noiNum02 == 65540:
                                                                noi03 = unpack("<I", f.read(4))[0]
                                                                if noi03 == 1627553839:
                                                                    noiNum03 = unpack("<I", f.read(4))[0]
                                                                    if noiNum03 == 65546:
                                                                        noi04 = unpack("<I", f.read(4))[0]
                                                                        if noi04 == 1627553843:
                                                                            noiNum04 = unpack("<I", f.read(4))[0]
                                                                            if noiNum04 == 6:
                                                                                noi05 = unpack("<I", f.read(4))[0]
                                                                                if noi05 == 1627553847:
                                                                                    noiNum05 = unpack("<I", f.read(4))[0]
                                                                                    if noiNum05 == 8:
                                                                                        noi05End01 = unpack("<I", f.read(4))[0]
                                                                                        if noi05End01 == 16777473:
                                                                                            if type4AA___1 == 1:
                                                                                                if type4AB___1 == 1:
                                                                                                    if type4AC___1 == 0:
                                                                                                        if type4AD___1 == 0:
                                                                                                            if type1__AE_1 == 0:
                                                                                                                if type1__AF_1 == 1:
                                                                                                                    if type1__AF_2 == 0:
                                                                                                                        if type1__AF_3 == 0:
                                                                                                                            if type1__AF_4 == 0:
                                                                                                                                if type1__AF_5 == 0:
                                                                                                                                    if type1__AF_6 == 0:
                                                                                                                                        if type1__AF_7 == 0:
                                                                                                                                            vertices3Daqaqa.append([vx0001__AA___1,vz0001__AA___1,vy0001__AA___1])
                                                                                                                                            vertices3Daqaqa.append([vx0001__AB___1,vz0001__AB___1,vy0001__AB___1])
                                                                                                                                            vertices3Daqaqa.append([vx0001__AC___1,vz0001__AC___1,vy0001__AC___1])
                                                                                                                                            vertices3Daqaqa.append([vx0001__AD___1,vz0001__AD___1,vy0001__AD___1])

                                                                                                                                            vertices3Daqaqa.append([vx0001__AE_1,vz0001__AE_1,vy0001__AE_1])

                                                                                                                                            vertices3Daqaqa.append([vx0001__AF_2,vz0001__AF_2,vy0001__AF_2])
                                                                                                                                            vertices3Daqaqa.append([vx0001__AF_4,vz0001__AF_4,vy0001__AF_4])
                                                                                                                                            vertices3Daqaqa.append([vx0001__AF_6,vz0001__AF_6,vy0001__AF_6])

                                                                                                                                            fa2Ta_daTa+=1*8
                                                                                                                                            fb2Ta_daTa+=1*8
                                                                                                                                            fc2Ta_daTa+=1*8
                                                                                                                                            fd2Ta_daTa+=1*8

                                                                                                                                            faces3Daqaqa.append([fa2Ta_daT,fb2Ta_daT,fc2Ta_daT])
                                                                                                                                            faces3Daqaqa.append([fb2Ta_daT,fc2Ta_daT,fd2Ta_daT])

                                                                                                                                            
                                                                    
                                                            
                            elif ofssetA == 1627553815:
                                ofssetB = unpack("<I", f.read(4))[0]
                                if ofssetB == 65540:
                                    pass
                                elif ofssetB == 65538:
                                    f.seek(2,1)
                                    vvvcount1y = unpack("B", f.read(1))[0]
                                    ffflag1y = unpack("B", f.read(1))[0]

                                    if ffflag1y == 0x6C:
                                        if vvvcount1y == 26:
                                            for i in range(1):
                                                vx0001__AF_8 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_8 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_8 = unpack("<f", f.read(4))[0]
                                                type1__AF_8 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_9 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_9 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_9 = unpack("<f", f.read(4))[0]
                                                type1__AF_9 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_10 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_10 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_10 = unpack("<f", f.read(4))[0]
                                                type1__AF_10 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_11 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_11 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_11 = unpack("<f", f.read(4))[0]
                                                type1__AF_11 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_12 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_12 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_12 = unpack("<f", f.read(4))[0]
                                                type1__AF_12 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_13 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_13 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_13 = unpack("<f", f.read(4))[0]
                                                type1__AF_13 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_14 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_14 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_14 = unpack("<f", f.read(4))[0]
                                                type1__AF_14 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_15 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_15 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_15 = unpack("<f", f.read(4))[0]
                                                type1__AF_15 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_16 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_16 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_16 = unpack("<f", f.read(4))[0]
                                                type1__AF_16 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_17 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_17 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_17 = unpack("<f", f.read(4))[0]
                                                type1__AF_17 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_18 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_18 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_18 = unpack("<f", f.read(4))[0]
                                                type1__AF_18 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_19 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_19 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_19 = unpack("<f", f.read(4))[0]
                                                type1__AF_19 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_20 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_20 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_20 = unpack("<f", f.read(4))[0]
                                                type1__AF_20 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_21 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_21 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_21 = unpack("<f", f.read(4))[0]
                                                type1__AF_21 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_22 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_22 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_22 = unpack("<f", f.read(4))[0]
                                                type1__AF_22 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_23 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_23 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_23 = unpack("<f", f.read(4))[0]
                                                type1__AF_23 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_24 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_24 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_24 = unpack("<f", f.read(4))[0]
                                                type1__AF_24 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_25 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_25 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_25 = unpack("<f", f.read(4))[0]
                                                type1__AF_25 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_26 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_26 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_26 = unpack("<f", f.read(4))[0]
                                                type1__AF_26 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_27 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_27 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_27 = unpack("<f", f.read(4))[0]
                                                type1__AF_27 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_28 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_28 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_28 = unpack("<f", f.read(4))[0]
                                                type1__AF_28 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_29 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_29 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_29 = unpack("<f", f.read(4))[0]
                                                type1__AF_29 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_30 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_30 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_30 = unpack("<f", f.read(4))[0]
                                                type1__AF_30 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_31 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_31 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_31 = unpack("<f", f.read(4))[0]
                                                type1__AF_31 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_32 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_32 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_32 = unpack("<f", f.read(4))[0]
                                                type1__AF_32 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                                vx0001__AF_33 = unpack("<f", f.read(4))[0]
                                                vy0001__AF_33 = unpack("<f", f.read(4))[0]
                                                vz0001__AF_33 = unpack("<f", f.read(4))[0]
                                                type1__AF_33 = unpack("B", f.read(1))[0]
                                                f.seek(3,1)

                                            ofssetBX = unpack("<I", f.read(4))[0]
                                            if ofssetBX == 1627553871:
                                                Bxa01 = unpack("<I", f.read(4))[0]
                                                if Bxa01 == 65549:
                                                    ofssetBX2 = unpack("<I", f.read(4))[0]
                                                    if ofssetBX2 == 1627553875:
                                                        BxaNum01 = unpack("<I", f.read(4))[0]
                                                        if BxaNum01 == 15:
                                                            f.seek(2,1)
                                                            xvvvcount1 = unpack("B", f.read(1))[0]
                                                            xffflag1 = unpack("B", f.read(1))[0]
                                                            if xffflag1 == 0x6C:
                                                                if xvvvcount1 == 4:
                                                                    for i in range(1):
                                                                        vx0001__AF_34 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AF_34 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AF_34 = unpack("<f", f.read(4))[0]
                                                                        type1__AF_34 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AF_35 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AF_35 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AF_35 = unpack("<f", f.read(4))[0]
                                                                        type1__AF_35 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AF_36 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AF_36 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AF_36 = unpack("<f", f.read(4))[0]
                                                                        type1__AF_36 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AF_37 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AF_37 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AF_37 = unpack("<f", f.read(4))[0]
                                                                        type1__AF_37 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                    ofssetBX1 = unpack("<I", f.read(4))[0]
                                                                    if ofssetBX1 == 1627553887:
                                                                        Bxa01a = unpack("<I", f.read(4))[0]
                                                                        if Bxa01a == 19:
                                                                            ofssetBXEnd = unpack("<I", f.read(4))[0]
                                                                            if ofssetBXEnd == 16777473:
                                                                                if type4AA___1a == 1:
                                                                                    if type4AB___1a == 1:
                                                                                        if type4AC___1a == 0:
                                                                                            if type4AD___1a == 0:
                                                                                                if type1__AF_8 == 0:
                                                                                                    if type1__AF_9 == 0:
                                                                                                        if type1__AF_10 == 0:
                                                                                                            if type1__AF_11 == 0:
                                                                                                                if type1__AF_12 == 0:
                                                                                                                    if type1__AF_13 == 0:
                                                                                                                        if type1__AF_14 == 0:
                                                                                                                            if type1__AF_15 == 0:
                                                                                                                                if type1__AF_16 == 0:
                                                                                                                                    if type1__AF_17 == 0:
                                                                                                                                        if type1__AF_18 == 0:
                                                                                                                                            if type1__AF_19 == 0:
                                                                                                                                                if type1__AF_20 == 0:
                                                                                                                                                    if type1__AF_21 == 0:
                                                                                                                                                        if type1__AF_22 == 0:
                                                                                                                                                            if type1__AF_23 == 0:
                                                                                                                                                                if type1__AF_24 == 0:
                                                                                                                                                                    if type1__AF_25 == 0:
                                                                                                                                                                        if type1__AF_26 == 0:
                                                                                                                                                                            if type1__AF_27 == 1:
                                                                                                                                                                                if type1__AF_28 == 0:
                                                                                                                                                                                    if type1__AF_29 == 1:
                                                                                                                                                                                        if type1__AF_30 == 0:
                                                                                                                                                                                            if type1__AF_31 == 0:
                                                                                                                                                                                                if type1__AF_32 == 0:
                                                                                                                                                                                                    if type1__AF_33 == 1:
                                                                                                                                                                                                        if type1__AF_34 == 0:
                                                                                                                                                                                                            if type1__AF_35 == 1:
                                                                                                                                                                                                                if type1__AF_36 == 0:
                                                                                                                                                                                                                    if type1__AF_37 == 1:
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AA___1a,vz0001__AA___1a,vy0001__AA___1a])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AB___1a,vz0001__AB___1a,vy0001__AB___1a])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AC___1a,vz0001__AC___1a,vy0001__AC___1a])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AD___1a,vz0001__AD___1a,vy0001__AD___1a])

                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_8,vz0001__AF_8,vy0001__AF_8])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_10,vz0001__AF_10,vy0001__AF_10])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_12,vz0001__AF_12,vy0001__AF_12])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_14,vz0001__AF_14,vy0001__AF_14])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_16,vz0001__AF_16,vy0001__AF_16])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_18,vz0001__AF_18,vy0001__AF_18])

                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_20,vz0001__AF_20,vy0001__AF_20])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_22,vz0001__AF_22,vy0001__AF_22])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_24,vz0001__AF_24,vy0001__AF_24])

                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_26,vz0001__AF_26,vy0001__AF_26])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_28,vz0001__AF_28,vy0001__AF_28])

                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_30,vz0001__AF_30,vy0001__AF_30])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_32,vz0001__AF_32,vy0001__AF_32])

                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_34,vz0001__AF_34,vy0001__AF_34])
                                                                                                                                                                                                                        vertices3Daqaqaq.append([vx0001__AF_36,vz0001__AF_36,vy0001__AF_36])

                                                                                                                                                                                                                        fa2Ta_daTaT+=1*19
                                                                                                                                                                                                                        fb2Ta_daTaT+=1*19
                                                                                                                                                                                                                        fc2Ta_daTaT+=1*19
                                                                                                                                                                                                                        fd2Ta_daTaT+=1*19

                                                                                                                                                                                                                        fe2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        ff2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fg2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fh2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fi2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fj2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fk2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fl2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fm2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fn2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fo2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fp2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fq2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fr2Ta_daTaT+=1*19#
                                                                                                                                                                                                                        fs2Ta_daTaT+=1*19#

                                                                                                                                                                                                                        faces3Daqaqaq.append([fa2Ta_daTaT,fb2Ta_daTaT,fc2Ta_daTaT])
                                                                                                                                                                                                                        faces3Daqaqaq.append([fb2Ta_daTaT,fc2Ta_daTaT,fd2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fc2Ta_daTaT,fd2Ta_daTaT,fe2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fd2Ta_daTaT,fe2Ta_daTaT,ff2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fe2Ta_daTaT,ff2Ta_daTaT,fg2Ta_daTaT])
                                                                                                                                                                                                                        faces3Daqaqaq.append([ff2Ta_daTaT,fg2Ta_daTaT,fh2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fg2Ta_daTaT,fh2Ta_daTaT,fi2Ta_daTaT])
                                                                                                                                                                                                                        faces3Daqaqaq.append([fh2Ta_daTaT,fi2Ta_daTaT,fj2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fi2Ta_daTaT,fj2Ta_daTaT,fk2Ta_daTaT])
                                                                                                                                                                                                                        faces3Daqaqaq.append([fj2Ta_daTaT,fk2Ta_daTaT,fl2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fk2Ta_daTaT,fl2Ta_daTaT,fm2Ta_daTaT])

                                                                                                                                                                                                                        #faces3Daqaqaq.append([fm2Ta_daTaT,fo2Ta_daTaT,fk2Ta_daTaT])

                                                                                                                                                                                                                        #faces3Daqaqaq.append([fm2Ta_daTaT,fn2Ta_daTaT,fo2Ta_daTaT])

                                                                                                                                                                                                                        faces3Daqaqaq.append([fn2Ta_daTaT,fo2Ta_daTaT,fp2Ta_daTaT])
                                                                                                                                                                                                                        faces3Daqaqaq.append([fq2Ta_daTaT,fr2Ta_daTaT,fs2Ta_daTaT])

                                                                                                                                                                                                                        #0x16738
                                                                                                                                                                                                                        
                                                                                                    
                                                                        
                                                            

                                            
                                        elif vvvcount1y == 4:
                                            for i in range(1):
                                                vx0001__AE_ = unpack("<f", f.read(4))[0]
                                                vy0001__AE_ = unpack("<f", f.read(4))[0]
                                                vz0001__AE_ = unpack("<f", f.read(4))[0]
                                                type1__AE_ = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__AF_ = unpack("<f", f.read(4))[0]
                                                vy0001__AF_ = unpack("<f", f.read(4))[0]
                                                vz0001__AF_ = unpack("<f", f.read(4))[0]
                                                type1__AF_ = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__AG_ = unpack("<f", f.read(4))[0]
                                                vy0001__AG_ = unpack("<f", f.read(4))[0]
                                                vz0001__AG_ = unpack("<f", f.read(4))[0]
                                                type1__AG_ = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                                vx0001__AH_ = unpack("<f", f.read(4))[0]
                                                vy0001__AH_ = unpack("<f", f.read(4))[0]
                                                vz0001__AH_ = unpack("<f", f.read(4))[0]
                                                type1__AH_ = unpack("B", f.read(1))[0]
                                                f.seek(3,1)
                                            ofssetC = unpack("<I", f.read(4))[0]
                                            if ofssetC == 16777473:
                                                if type4AA_ == 1:
                                                    if type4AB_ == 1:
                                                        if type4AC_ == 0:
                                                            if type4AD_ == 0:
                                                                if type1__AE_ == 0:
                                                                    if type1__AF_ == 0:
                                                                        if type1__AG_ == 0:
                                                                            if type1__AH_ == 0:
                                                                                vertices3Daq.append([vx0001__AA_,vz0001__AA_,vy0001__AA_])
                                                                                vertices3Daq.append([vx0001__AC_,vz0001__AC_,vy0001__AC_])
                                                                                vertices3Daq.append([vx0001__AD_,vz0001__AD_,vy0001__AD_])
                                                                                vertices3Daq.append([vx0001__AE_,vz0001__AE_,vy0001__AE_])
                                                                                vertices3Daq.append([vx0001__AG_,vz0001__AG_,vy0001__AG_])

                                                                                fa2Ta_d+=1*5
                                                                                fb2Ta_d+=1*5
                                                                                fc2Ta_d+=1*5
                                                                                fd2Ta_d+=1*5
                                                                                fe2Ta_d+=1*5

                                                                                faces3Daq.append([fa2Ta_d,fb2Ta_d,fc2Ta_d])
                                                                                faces3Daq.append([fb2Ta_d,fc2Ta_d,fd2Ta_d])
                                                                                faces3Daq.append([fc2Ta_d,fd2Ta_d,fe2Ta_d])

                        elif offffsetB == 65538:
                            f.seek(2,1)
                            vvavC = unpack("B", f.read(1))[0]
                            fvflag1 = unpack("B", f.read(1))[0]
                            if fvflag1 != 0x6C:
                                f.seek(-4,1)
                                overlordofffsset1 = unpack("<I", f.read(4))[0]
                                if overlordofffsset1 == 1627553815:
                                    overlordd01 = unpack("<I", f.read(4))[0]
                                    if overlordd01 == 65540:
                                        f.seek(2,1)
                                        overlordTimeCount01 = unpack("B", f.read(1))[0]
                                        overlordTimeFlag01 = unpack("B", f.read(1))[0]
                                        if overlordTimeFlag01 == 0x6C:
                                            if overlordTimeCount01 == 4:
                                                for i in range(1):
                                                    vx0001__AO__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vy0001__AO__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vz0001__AO__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    type1__AO__overlordShadow01 = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__AP__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vy0001__AP__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vz0001__AP__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    type1__AP__overlordShadow01 = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__AQ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vy0001__AQ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vz0001__AQ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    type1__AQ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                    vx0001__AR__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vy0001__AR__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    vz0001__AR__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                    type1__AR__overlordShadow01 = unpack("B", f.read(1))[0]
                                                    f.seek(3,1)
                                                overlordShadowOffset01 = unpack("<I", f.read(4))[0]
                                                if overlordShadowOffset01 == 1627553827:
                                                    overlordShadowNUM01 = unpack("<I", f.read(4))[0]
                                                    if overlordShadowNUM01 == 65544:
                                                        f.seek(2,1)
                                                        overlordCShadowCount01 = unpack("B", f.read(1))[0]
                                                        overlordCShadowFlag01 = unpack("B", f.read(1))[0]
                                                        if overlordCShadowFlag01 == 0x6C:
                                                            if overlordCShadowCount01 == 6:
                                                                for i in range(1):
                                                                    vx0001__AS__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AS__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AS__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AS__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AT__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AT__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AT__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AT__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AU__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AU__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AU__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AU__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AV__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AV__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AV__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AV__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AW__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AW__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AW__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AW__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                    vx0001__AX__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vy0001__AX__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    vz0001__AX__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                    type1__AX__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                    f.seek(3,1)

                                                                overlordMasterOffset01 = unpack("<I", f.read(4))[0]
                                                                if overlordMasterOffset01 == 1627553843:
                                                                    overlordMasterNUM01 = unpack("<I", f.read(4))[0]
                                                                    if overlordMasterNUM01 == 65546:
                                                                        f.seek(2,1)
                                                                        overlordCShadowwCount01 = unpack("B", f.read(1))[0]
                                                                        overlordCShadowwFlag01 = unpack("B", f.read(1))[0]
                                                                        #256B4
                                                                        if overlordCShadowwFlag01 == 0x6C:
                                                                            if overlordCShadowwCount01 == 2:
                                                                                for i in range(1):
                                                                                    vx0001__AZZZZZZZZZ11__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    vy0001__AZZZZZZZZZ11__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    vz0001__AZZZZZZZZZ11__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    type1__AZZZZZZZZZ11__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                    f.seek(3,1)

                                                                                    vx0001__AZZZZZZZZZ12__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    vy0001__AZZZZZZZZZ12__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    vz0001__AZZZZZZZZZ12__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                    type1__AZZZZZZZZZ12__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                    f.seek(3,1)

                                                                                oveerlorrrd = unpack("<I", f.read(4))[0]
                                                                                if oveerlorrrd == 1627553851:
                                                                                    overlord12 = unpack("<I", f.read(4))[0]
                                                                                    if overlord12 == 12:
                                                                                        f.seek(2,1)
                                                                                        overlordCsShadowwCount01 = unpack("B", f.read(1))[0]
                                                                                        overlordCsShadowwFlag01 = unpack("B", f.read(1))[0]
                                                                                        if overlordCsShadowwFlag01 == 0x6C:
                                                                                            if overlordCsShadowwCount01 == 10:
                                                                                                
                                                                                                if overlordCsShadowwCount01 == 10:
                                                                                                    for i in range(1):
                                                                                                        vx0001__AY__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AY__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AY__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AY__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AZZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AZZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AZZZZZZZZZ__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AZZZZZZZZZ__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                    overLordMword01 = unpack("<I", f.read(4))[0]
                                                                                                    if overLordMword01 == 1627553875:
                                                                                                        overllord01 = unpack("<I", f.read(4))[0]
                                                                                                        if overllord01 == 65554:
                                                                                                            overlloord01 = unpack("<I", f.read(4))[0]
                                                                                                            if overlloord01 == 1627553879:
                                                                                                                overlloorrd01 = unpack("<I", f.read(4))[0]
                                                                                                                if overlloorrd01 == 65556:
                                                                                                                    f.seek(2,1)
                                                                                                                    overlordCShadowwwCount01 = unpack("B", f.read(1))[0]
                                                                                                                    overlordCShadowwwFlag01 = unpack("B", f.read(1))[0]
                                                                                                                    if overlordCShadowwwFlag01 == 0x6C:
                                                                                                                        if overlordCShadowwwCount01 == 10:
                                                                                                                            for i in range(1):
                                                                                                                                vx0001__AZZZZZZZZZ1__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ1__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ1__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ1__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ2__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ2__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ2__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ2__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ3__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ3__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ3__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ3__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ4__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ4__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ4__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ4__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ5__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ5__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ5__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ5__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ6__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ6__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ6__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ6__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ7__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ7__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ7__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ7__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ8__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ8__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ8__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ8__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ9__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ9__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ9__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ9__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AZZZZZZZZZ10__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AZZZZZZZZZ10__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AZZZZZZZZZ10__overlordShadow01 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AZZZZZZZZZ10__overlordShadow01 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                            overlordyEnd01 = unpack("<I", f.read(4))[0]
                                                                                                                            if overlordyEnd01 == 16777473:
                                                                                                                                if type4AA___1aaOverlord3 == 1:
                                                                                                                                    if type4AB___1aaOverlord3 == 1:
                                                                                                                                        if type4AC___1aaOverlord3 == 0:
                                                                                                                                            if type4AD___1aaOverlord3 == 0:
                                                                                                                                                if type1__AO__overlordShadow01 == 0:
                                                                                                                                                    if type1__AP__overlordShadow01 == 0:
                                                                                                                                                        if type1__AQ__overlordShadow01 == 0:
                                                                                                                                                            if type1__AR__overlordShadow01 == 0:
                                                                                                                                                                if type1__AS__overlordShadow01 == 0:
                                                                                                                                                                    if type1__AT__overlordShadow01 == 1:
                                                                                                                                                                        if type1__AU__overlordShadow01 == 0:
                                                                                                                                                                            if type1__AV__overlordShadow01 == 0:
                                                                                                                                                                                if type1__AW__overlordShadow01 == 0:
                                                                                                                                                                                    if type1__AX__overlordShadow01 == 0:
                                                                                                                                                                                        if type1__AZZZZZZZZZ11__overlordShadow01 == 0:
                                                                                                                                                                                            if type1__AZZZZZZZZZ12__overlordShadow01 == 1:
                                                                                                                                                                                                if type1__AY__overlordShadow01 == 0:
                                                                                                                                                                                                    if type1__AZ__overlordShadow01 == 0:
                                                                                                                                                                                                        if type1__AZZ__overlordShadow01 == 0:
                                                                                                                                                                                                            if type1__AZZZ__overlordShadow01 == 1:
                                                                                                                                                                                                                if type1__AZZZZ__overlordShadow01 == 0:
                                                                                                                                                                                                                    if type1__AZZZZZ__overlordShadow01 == 1:
                                                                                                                                                                                                                        if type1__AZZZZZZ__overlordShadow01 == 0:
                                                                                                                                                                                                                            if type1__AZZZZZZZ__overlordShadow01 == 0:
                                                                                                                                                                                                                                if type1__AZZZZZZZZ__overlordShadow01 == 0:
                                                                                                                                                                                                                                    if type1__AZZZZZZZZZ__overlordShadow01 == 0:
                                                                                                                                                                                                                                        if type1__AZZZZZZZZZ1__overlordShadow01 == 0:
                                                                                                                                                                                                                                            if type1__AZZZZZZZZZ2__overlordShadow01 == 0:
                                                                                                                                                                                                                                                if type1__AZZZZZZZZZ3__overlordShadow01 == 0:
                                                                                                                                                                                                                                                    if type1__AZZZZZZZZZ4__overlordShadow01 == 0:
                                                                                                                                                                                                                                                        if type1__AZZZZZZZZZ5__overlordShadow01 == 0:
                                                                                                                                                                                                                                                            if type1__AZZZZZZZZZ6__overlordShadow01 == 1:
                                                                                                                                                                                                                                                                if type1__AZZZZZZZZZ7__overlordShadow01 == 0:
                                                                                                                                                                                                                                                                    if type1__AZZZZZZZZZ8__overlordShadow01 == 1:
                                                                                                                                                                                                                                                                        if type1__AZZZZZZZZZ9__overlordShadow01 == 0:
                                                                                                                                                                                                                                                                            if type1__AZZZZZZZZZ10__overlordShadow01 == 0:
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AA___1aaOverlord3,vz0001__AA___1aaOverlord3,vy0001__AA___1aaOverlord3])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AB___1aaOverlord3,vz0001__AB___1aaOverlord3,vy0001__AB___1aaOverlord3])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AC___1aaOverlord3,vz0001__AC___1aaOverlord3,vy0001__AC___1aaOverlord3])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AD___1aaOverlord3,vz0001__AD___1aaOverlord3,vy0001__AD___1aaOverlord3])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AO__overlordShadow01,vz0001__AO__overlordShadow01,vy0001__AO__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AQ__overlordShadow01,vz0001__AQ__overlordShadow01,vy0001__AQ__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AS__overlordShadow01,vz0001__AS__overlordShadow01,vy0001__AS__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AU__overlordShadow01,vz0001__AU__overlordShadow01,vy0001__AU__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AW__overlordShadow01,vz0001__AW__overlordShadow01,vy0001__AW__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ11__overlordShadow01,vz0001__AZZZZZZZZZ11__overlordShadow01,vy0001__AZZZZZZZZZ11__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AY__overlordShadow01,vz0001__AY__overlordShadow01,vy0001__AY__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZ__overlordShadow01,vz0001__AZZ__overlordShadow01,vy0001__AZZ__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZ__overlordShadow01,vz0001__AZZZZ__overlordShadow01,vy0001__AZZZZ__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZ__overlordShadow01,vz0001__AZZZZZZ__overlordShadow01,vy0001__AZZZZZZ__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZ__overlordShadow01,vz0001__AZZZZZZZZ__overlordShadow01,vy0001__AZZZZZZZZ__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ1__overlordShadow01,vz0001__AZZZZZZZZZ1__overlordShadow01,vy0001__AZZZZZZZZZ1__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ3__overlordShadow01,vz0001__AZZZZZZZZZ3__overlordShadow01,vy0001__AZZZZZZZZZ3__overlordShadow01])
                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ5__overlordShadow01,vz0001__AZZZZZZZZZ5__overlordShadow01,vy0001__AZZZZZZZZZ5__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ7__overlordShadow01,vz0001__AZZZZZZZZZ7__overlordShadow01,vy0001__AZZZZZZZZZ7__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordverts04.append([vx0001__AZZZZZZZZZ9__overlordShadow01,vz0001__AZZZZZZZZZ9__overlordShadow01,vy0001__AZZZZZZZZZ9__overlordShadow01])

                                                                                                                                                                                                                                                                                overlordA4+=1*20
                                                                                                                                                                                                                                                                                overlordB4+=1*20
                                                                                                                                                                                                                                                                                overlordC4+=1*20
                                                                                                                                                                                                                                                                                overlordD4+=1*20
                                                                                                                                                                                                                                                                                overlordE4+=1*20
                                                                                                                                                                                                                                                                                overlordF4+=1*20
                                                                                                                                                                                                                                                                                overlordG4+=1*20
                                                                                                                                                                                                                                                                                overlordH4+=1*20
                                                                                                                                                                                                                                                                                overlordI4+=1*20
                                                                                                                                                                                                                                                                                overlordJ4+=1*20
                                                                                                                                                                                                                                                                                overlordK4+=1*20
                                                                                                                                                                                                                                                                                overlordL4+=1*20
                                                                                                                                                                                                                                                                                overlordM4+=1*20
                                                                                                                                                                                                                                                                                overlordN4+=1*20
                                                                                                                                                                                                                                                                                overlordO4+=1*20

                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordA4,overlordB4,overlordC4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordB4,overlordC4,overlordD4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordB4,overlordD4,overlordE4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordD4,overlordE4,overlordF4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordE4,overlordF4,overlordG4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordE4,overlordG4,overlordH4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordE4,overlordH4,overlordI4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordH4,overlordI4,overlordJ4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordB4,overlordE4,overlordI4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordB4,overlordI4,overlordL4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordB4,overlordL4,overlordM4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordA4,overlordM4,overlordN4])
                                                                                                                                                                                                                                                                                overlordfaces04.append([overlordA4,overlordN4,overlordL4])
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                    

                                                                                                            
                                                                                            
                                                    
                            elif fvflag1 == 0x6C:
                                if vvavC == 2:
                                    for i in range(1):
                                        vx0001__AO__ = unpack("<f", f.read(4))[0]
                                        vy0001__AO__ = unpack("<f", f.read(4))[0]
                                        vz0001__AO__ = unpack("<f", f.read(4))[0]
                                        type1__AO__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AP__ = unpack("<f", f.read(4))[0]
                                        vy0001__AP__ = unpack("<f", f.read(4))[0]
                                        vz0001__AP__ = unpack("<f", f.read(4))[0]
                                        type1__AP__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                    fvflag2 = unpack("<I", f.read(4))[0]
                                    if fvflag2 == 1627553819:
                                        
                                        num01 = unpack("<I", f.read(4))[0]
                                        if num01 == 4:
                                            f.seek(2,1)
                                            vvavC3 = unpack("B", f.read(1))[0]
                                            fvflag3 = unpack("B", f.read(1))[0]
                                            if fvflag3 == 0x6C:
                                                if vvavC3 == 4:
                                                    for i in range(1):
                                                        vx0001__AQ___2overlord = unpack("<f", f.read(4))[0]
                                                        vy0001__AQ___2overlord = unpack("<f", f.read(4))[0]
                                                        vz0001__AQ___2overlord = unpack("<f", f.read(4))[0]
                                                        type1__AQ___2overlord = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR___2overlord = unpack("<f", f.read(4))[0]
                                                        vx0001__AR___2overlord = unpack("<f", f.read(4))[0]
                                                        vx0001__AR___2overlord = unpack("<f", f.read(4))[0]
                                                        type1__AR___2overlord = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AS___2overlord = unpack("<f", f.read(4))[0]
                                                        vy0001__AS___2overlord = unpack("<f", f.read(4))[0]
                                                        vz0001__AS___2overlord = unpack("<f", f.read(4))[0]
                                                        type1__AS___2overlord = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AT___2overlord = unpack("<f", f.read(4))[0]
                                                        vx0001__AT___2overlord = unpack("<f", f.read(4))[0]
                                                        vx0001__AT___2overlord = unpack("<f", f.read(4))[0]
                                                        type1__AT___2overlord = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    for i in range(vvavC3):
                                                        f.seek(-16,1)
                                                    for i in range(1):
                                                        vx0001__AQ___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AQ___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AQ___2overlord2 = unpack("<f", f.read(4))[0]
                                                        type1__AQ___2overlord2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___2overlord2 = unpack("<f", f.read(4))[0]
                                                        type1__AR___2overlord2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AS___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AS___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AS___2overlord2 = unpack("<f", f.read(4))[0]
                                                        type1__AS___2overlord2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AT___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AT___2overlord2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AT___2overlord2 = unpack("<f", f.read(4))[0]
                                                        type1__AT___2overlord2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    overlordEndhere01 = unpack("<I", f.read(4))[0]
                                                    if overlordEndhere01 == 1627553831:
                                                        overkklord1 = unpack("<I", f.read(4))[0]
                                                        if overkklord1 == 65544:
                                                            overkklords1 = unpack("<I", f.read(4))[0]
                                                            if overkklords1 == 1627553835:
                                                                overkklords1num6 = unpack("<I", f.read(4))[0]
                                                                if overkklords1num6 == 6:
                                                                    overkklords1num6End01 = unpack("<I", f.read(4))[0]
                                                                    if overkklords1num6End01 == 16777473:
                                                                        if type4AA___1aaOverlord5 == 1:
                                                                            if type4AB___1aaOverlord5 == 1:
                                                                                if type4AC___1aaOverlord5 == 0:
                                                                                    if type4AD___1aaOverlord5 == 0:
                                                                                        if type1__AO__ == 0:
                                                                                            if type1__AP__ == 1:
                                                                                                if type1__AQ___2overlord2 == 0:
                                                                                                    if type1__AR___2overlord2 == 0:
                                                                                                        if type1__AS___2overlord2 == 0:
                                                                                                            if type1__AT___2overlord2 == 1:
                                                                                                                overlordverts06.append([vx0001__AA___1aaOverlord5,vz0001__AA___1aaOverlord5,vy0001__AA___1aaOverlord5])
                                                                                                                overlordverts06.append([vx0001__AB___1aaOverlord5,vz0001__AB___1aaOverlord5,vy0001__AB___1aaOverlord5])
                                                                                                                overlordverts06.append([vx0001__AC___1aaOverlord5,vz0001__AC___1aaOverlord5,vy0001__AC___1aaOverlord5])
                                                                                                                overlordverts06.append([vx0001__AD___1aaOverlord5,vz0001__AD___1aaOverlord5,vy0001__AD___1aaOverlord5])

                                                                                                                overlordverts06.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])

                                                                                                                overlordverts06.append([vx0001__AQ___2overlord2,vz0001__AQ___2overlord2,vy0001__AQ___2overlord2])

                                                                                                                overlordverts06.append([vx0001__AS___2overlord2,vz0001__AS___2overlord2,vy0001__AS___2overlord2])

                                                                                                                overlordA6+=1*7
                                                                                                                overlordB6+=1*7
                                                                                                                overlordC6+=1*7
                                                                                                                overlordD6+=1*7
                                                                                                                overlordE6+=1*7
                                                                                                                overlordF6+=1*7
                                                                                                                overlordG6+=1*7
                                                                                                                

                                                                                                                overlordfaces06.append([overlordA6,overlordB6,overlordC6])
                                                                                                                overlordfaces06.append([overlordB6,overlordC6,overlordD6])
                                                                                                                overlordfaces06.append([overlordB6,overlordD6,overlordE6])
                                                                                                                overlordfaces06.append([overlordD6,overlordE6,overlordF6])
                                                                                                                overlordfaces06.append([overlordE6,overlordF6,overlordG6])
                                                                                                                
                                                                                                    
                                                    elif overlordEndhere01 == 16777473:
                                                        if type4AA___1aaOverlord1 == 1:
                                                            if type4AB___1aaOverlord1 == 1:
                                                                if type4AC___1aaOverlord1 == 0:
                                                                    if type4AD___1aaOverlord1 == 0:
                                                                        if type1__AO__ == 0:
                                                                            if type1__AP__ == 1:
                                                                                if type1__AQ___2overlord == 0:
                                                                                    if type1__AR___2overlord == 0:
                                                                                        if type1__AS___2overlord == 0:
                                                                                            if type1__AT___2overlord == 0:
                                                                                                overlordverts02.append([vx0001__AA___1aaOverlord1,vz0001__AA___1aaOverlord1,vy0001__AA___1aaOverlord1])
                                                                                                overlordverts02.append([vx0001__AB___1aaOverlord1,vz0001__AB___1aaOverlord1,vy0001__AB___1aaOverlord1])
                                                                                                overlordverts02.append([vx0001__AC___1aaOverlord1,vz0001__AC___1aaOverlord1,vy0001__AC___1aaOverlord1])
                                                                                                overlordverts02.append([vx0001__AD___1aaOverlord1,vz0001__AD___1aaOverlord1,vy0001__AD___1aaOverlord1])

                                                                                                overlordverts02.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])

                                                                                                overlordverts02.append([vx0001__AQ___2overlord,vz0001__AQ___2overlord,vy0001__AQ___2overlord])
                                                                                                overlordverts02.append([vx0001__AS___2overlord,vz0001__AS___2overlord,vy0001__AS___2overlord])

                                                                                                overlordA2+=1*7
                                                                                                overlordB2+=1*7
                                                                                                overlordC2+=1*7
                                                                                                overlordD2+=1*7
                                                                                                overlordE2+=1*7
                                                                                                overlordF2+=1*7
                                                                                                overlordG2+=1*7

                                                                                                overlordfaces02.append([overlordA2,overlordB2,overlordC2])
                                                                                                overlordfaces02.append([overlordB2,overlordC2,overlordD2])
                                                                                                overlordfaces02.append([overlordB2,overlordD2,overlordE2])
                                                                                                overlordfaces02.append([overlordD2,overlordE2,overlordF2])
                                                                                                overlordfaces02.append([overlordD2,overlordF2,overlordG2])
                                                elif vvavC3 == 2:
                                                    for i in range(1):
                                                        vx0001__AQ___2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AQ___2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AQ___2 = unpack("<f", f.read(4))[0]
                                                        type1__AQ___2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR___2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___2 = unpack("<f", f.read(4))[0]
                                                        type1__AR___2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    cocoO = unpack("<I", f.read(4))[0]
                                                    if cocoO == 16777473:
                                                        if type4AA___1aaOverlord6 == 1:
                                                            if type4AB___1aaOverlord6 == 1:
                                                                if type4AC___1aaOverlord6 == 0:
                                                                    if type4AD___1aaOverlord6 == 0:
                                                                        if type1__AO__ == 0:
                                                                            if type1__AP__ == 1:
                                                                                if type1__AQ___2 == 0:
                                                                                    if type1__AR___2 == 0:
                                                                                        overlordverts07.append([vx0001__AA___1aaOverlord6,vz0001__AA___1aaOverlord6,vy0001__AA___1aaOverlord6])
                                                                                        overlordverts07.append([vx0001__AB___1aaOverlord6,vz0001__AB___1aaOverlord6,vy0001__AB___1aaOverlord6])
                                                                                        overlordverts07.append([vx0001__AC___1aaOverlord6,vz0001__AC___1aaOverlord6,vy0001__AC___1aaOverlord6])
                                                                                        overlordverts07.append([vx0001__AD___1aaOverlord6,vz0001__AD___1aaOverlord6,vy0001__AD___1aaOverlord6])

                                                                                        overlordverts07.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])
                                                                                        overlordverts07.append([vx0001__AQ___2,vz0001__AQ___2,vy0001__AQ___2])

                                                                                        overlordA7+=1*6
                                                                                        overlordB7+=1*6
                                                                                        overlordC7+=1*6
                                                                                        overlordD7+=1*6
                                                                                        overlordE7+=1*6
                                                                                        overlordF7+=1*6

                                                                                        overlordfaces07.append([overlordA7,overlordB7,overlordC7])
                                                                                        overlordfaces07.append([overlordB7,overlordC7,overlordD7])

                                                                                        overlordfaces07.append([overlordB7,overlordD7,overlordE7])
                                                                                        overlordfaces07.append([overlordB7,overlordE7,overlordF7])
                                                    elif cocoO == 1627553827:
                                                        cocoOffsetL = unpack("<I", f.read(4))[0]
                                                        if cocoOffsetL == 65542:
                                                            f.seek(2,1)
                                                            cocoTwoCount = unpack("B", f.read(1))[0]
                                                            cocoTwoFlag = unpack("B", f.read(1))[0]
                                                            if cocoTwoFlag == 0x6C:
                                                                if cocoTwoCount == 2:
                                                                    for i in range(1):
                                                                        vx0001__AQ___2coco = unpack("<f", f.read(4))[0]
                                                                        vy0001__AQ___2coco = unpack("<f", f.read(4))[0]
                                                                        vz0001__AQ___2coco = unpack("<f", f.read(4))[0]
                                                                        type1__AQ___2coco = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AR___2coco = unpack("<f", f.read(4))[0]
                                                                        vy0001__AR___2coco = unpack("<f", f.read(4))[0]
                                                                        vz0001__AR___2coco = unpack("<f", f.read(4))[0]
                                                                        type1__AR___2coco = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                    cocoPLS = unpack("<I", f.read(4))[0]
                                                                    if cocoPLS == 1627553835:
                                                                        cocoNUM = unpack("<I", f.read(4))[0]
                                                                        if cocoNUM == 8:
                                                                            f.seek(2,1)
                                                                            cocoTwoCount1 = unpack("B", f.read(1))[0]
                                                                            cocoTwoFlag1 = unpack("B", f.read(1))[0]
                                                                            if cocoTwoFlag1 == 0x6C:
                                                                                if cocoTwoCount1 == 16:
                                                                                    for i in range(1):
                                                                                        vx0001__AS___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AS___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AS___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AS___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AT___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AT___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AT___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AT___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AU___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AU___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AU___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AU___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AV___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AV___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AV___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AV___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AW___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AW___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AW___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AW___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AX___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AX___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AX___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AX___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AY___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AY___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AY___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AY___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                    cocoCartoon1 = unpack("<I", f.read(4))[0]
                                                                                    if cocoCartoon1 == 1627553871:
                                                                                        cocorunny = unpack("<I", f.read(4))[0]
                                                                                        if cocorunny == 1:
                                                                                            f.seek(2,1)
                                                                                            cocoStreetCount1 = unpack("B", f.read(1))[0]
                                                                                            cocoStreetFlag1 = unpack("B", f.read(1))[0]
                                                                                            if cocoStreetFlag1 == 0x6C:
                                                                                                if cocoStreetCount1 == 2:
                                                                                                    #0xFE9C
                                                                                                    for i in range(1):
                                                                                                        vx0001__AS___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AS___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AS___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AS___2cocococo1 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AT___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AT___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AT___2cocococo1 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AT___2cocococo1 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)
                                                                                                    cocoKFC1 = unpack("<I", f.read(4))[0]
                                                                                                    if cocoKFC1 == 1627553879:
                                                                                                        cocomessedup1 = unpack("<I", f.read(4))[0]
                                                                                                        if cocomessedup1 == 65546:
                                                                                                            cocomediumup1 = unpack("<I", f.read(4))[0]
                                                                                                            if cocomediumup1 == 1627553883:
                                                                                                                cocotwelve = unpack("<I", f.read(4))[0]
                                                                                                                if cocotwelve == 12:
                                                                                                                    f.seek(2,1)
                                                                                                                    coco2pounds = unpack("B", f.read(1))[0]
                                                                                                                    coco2poundsFlag = unpack("B", f.read(1))[0]
                                                                                                                    if coco2poundsFlag == 0x6C:
                                                                                                                        if coco2pounds == 2:
                                                                                                                            for i in range(1):
                                                                                                                                vx0001__AS___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AS___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AS___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AS___2cocococo2 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                                vx0001__AT___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                vy0001__AT___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                vz0001__AT___2cocococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                type1__AT___2cocococo2 = unpack("B", f.read(1))[0]
                                                                                                                                f.seek(3,1)

                                                                                                                            cocolostcoin01 = unpack("<I", f.read(4))[0]
                                                                                                                            if cocolostcoin01 == 1627553891:
                                                                                                                                cocoislost01 = unpack("<I", f.read(4))[0]
                                                                                                                                if cocoislost01 == 65557:
                                                                                                                                    cocosugar01 = unpack("<I", f.read(4))[0]
                                                                                                                                    if cocosugar01 == 1627553895:
                                                                                                                                        cocoGranted01 = unpack("<I", f.read(4))[0]
                                                                                                                                        if cocoGranted01 == 13:
                                                                                                                                            cocoExist01 = unpack("<I", f.read(4))[0]
                                                                                                                                            if cocoExist01 == 16777473:
                                                                                                                                                if type4AA___1aaCoco1 == 1:
                                                                                                                                                    if type4AB___1aaCoco1 == 1:
                                                                                                                                                        if type4AC___1aaCoco1 == 0:
                                                                                                                                                            if type4AD___1aaCoco1 == 0:
                                                                                                                                                                if type1__AO__ == 0:
                                                                                                                                                                    if type1__AP__ == 1:
                                                                                                                                                                        if type1__AQ___2 == 0:
                                                                                                                                                                            if type1__AR___2 == 0:
                                                                                                                                                                                if type1__AQ___2coco == 0:
                                                                                                                                                                                    if type1__AR___2coco == 1:
                                                                                                                                                                                        if type1__AS___2cocococo == 0:
                                                                                                                                                                                            if type1__AT___2cocococo == 0:
                                                                                                                                                                                                if type1__AU___2cocococo == 0:
                                                                                                                                                                                                    if type1__AV___2cocococo == 1:
                                                                                                                                                                                                        if type1__AW___2cocococo == 0:
                                                                                                                                                                                                            if type1__AX___2cocococo == 1:
                                                                                                                                                                                                                if type1__AY___2cocococo == 0:
                                                                                                                                                                                                                    if type1__AZ___2cocococo == 0:
                                                                                                                                                                                                                        if type1__AZZ___2cocococo == 0:
                                                                                                                                                                                                                            if type1__AZZZ___2cocococo == 0:
                                                                                                                                                                                                                                if type1__AZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                    if type1__AZZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                        if type1__AZZZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                            if type1__AZZZZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                                if type1__AZZZZZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                                    if type1__AZZZZZZZZZ___2cocococo == 0:
                                                                                                                                                                                                                                                        if type1__AS___2cocococo1 == 0:
                                                                                                                                                                                                                                                            if type1__AT___2cocococo1 == 1:
                                                                                                                                                                                                                                                                if type1__AS___2cocococo2 == 0:
                                                                                                                                                                                                                                                                    if type1__AT___2cocococo2 == 1:
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AA___1aaCoco1,vz0001__AA___1aaCoco1,vy0001__AA___1aaCoco1])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AB___1aaCoco1,vz0001__AB___1aaCoco1,vy0001__AB___1aaCoco1])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AC___1aaCoco1,vz0001__AC___1aaCoco1,vy0001__AC___1aaCoco1])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AD___1aaCoco1,vz0001__AD___1aaCoco1,vy0001__AD___1aaCoco1])

                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AQ___2,vz0001__AQ___2,vy0001__AQ___2])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AQ___2coco,vz0001__AQ___2coco,vy0001__AQ___2coco])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AS___2cocococo,vz0001__AS___2cocococo,vy0001__AS___2cocococo])

                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AU___2cocococo,vz0001__AU___2cocococo,vy0001__AU___2cocococo])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AW___2cocococo,vz0001__AW___2cocococo,vy0001__AW___2cocococo])

                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AY___2cocococo,vz0001__AY___2cocococo,vy0001__AY___2cocococo])

                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AZZ___2cocococo,vz0001__AZZ___2cocococo,vy0001__AZZ___2cocococo])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AZZZZ___2cocococo,vz0001__AZZZZ___2cocococo,vy0001__AZZZZ___2cocococo])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AZZZZZZ___2cocococo,vz0001__AZZZZZZ___2cocococo,vy0001__AZZZZZZ___2cocococo])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AZZZZZZZZ___2cocococo,vz0001__AZZZZZZZZ___2cocococo,vy0001__AZZZZZZZZ___2cocococo])

                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AS___2cocococo1,vz0001__AS___2cocococo1,vy0001__AS___2cocococo1])
                                                                                                                                                                                                                                                                        cocoVerts02.append([vx0001__AS___2cocococo2,vz0001__AS___2cocococo2,vy0001__AS___2cocococo2])

                                                                                                                                                                                                                                                                        cocoAa+=1*17
                                                                                                                                                                                                                                                                        cocoBa+=1*17
                                                                                                                                                                                                                                                                        cocoCa+=1*17
                                                                                                                                                                                                                                                                        cocoDa+=1*17
                                                                                                                                                                                                                                                                        cocoEa+=1*17
                                                                                                                                                                                                                                                                        cocoFa+=1*17
                                                                                                                                                                                                                                                                        cocoGa+=1*17
                                                                                                                                                                                                                                                                        cocoHa+=1*17
                                                                                                                                                                                                                                                                        cocoIa+=1*17
                                                                                                                                                                                                                                                                        cocoJa+=1*17
                                                                                                                                                                                                                                                                        cocoKa+=1*17
                                                                                                                                                                                                                                                                        cocoLa+=1*17
                                                                                                                                                                                                                                                                        cocoMa+=1*17
                                                                                                                                                                                                                                                                        cocoNa+=1*17
                                                                                                                                                                                                                                                                        cocoOa+=1*17
                                                                                                                                                                                                                                                                        cocoPa+=1*17
                                                                                                                                                                                                                                                                        cocoQa+=1*17

                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoAa,cocoBa,cocoCa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoBa,cocoCa,cocoEa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoCa,cocoDa,cocoEa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoDa,cocoEa,cocoFa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoEa,cocoFa,cocoGa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoFa,cocoGa,cocoHa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoGa,cocoHa,cocoIa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoGa,cocoIa,cocoJa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoIa,cocoJa,cocoKa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoIa,cocoKa,cocoLa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoKa,cocoLa,cocoMa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoLa,cocoMa,cocoNa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoMa,cocoNa,cocoOa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoNa,cocoOa,cocoPa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoOa,cocoPa,cocoQa])
                                                                                                                                                                                                                                                                        cocoFaces02.append([cocoPa,cocoQa,cocoAa])

                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                        
                                                                                                                                
                                                                                                                    
                                                                                                                

                                                                                                        
                                                                                elif cocoTwoCount1 == 2:
                                                                                    for i in range(1):
                                                                                        vx0001__AQ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AQ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AQ___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AQ___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AR___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AR___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AR___2cocococo = unpack("<f", f.read(4))[0]
                                                                                        type1__AR___2cocococo = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                    cocoFatherOffset1 = unpack("<I", f.read(4))[0]
                                                                                    if cocoFatherOffset1 == 1627553843:
                                                                                        cocoMumCount1 = unpack("<I", f.read(4))[0]
                                                                                        if cocoMumCount1 == 65546:
                                                                                            f.seek(2,1)
                                                                                            cocoMINIMECount = unpack("B", f.read(1))[0]
                                                                                            cocoMINIMEFlag = unpack("B", f.read(1))[0]
                                                                                            if cocoMINIMEFlag == 0x6C:
                                                                                                if cocoMINIMECount == 2:
                                                                                                    for i in range(1):
                                                                                                        vx0001__AQ___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AQ___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AQ___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        type1__AQ___2cocococococo = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)
                                                                                                        vx0001__AR___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AR___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AR___2cocococococo = unpack("<f", f.read(4))[0]
                                                                                                        type1__AR___2cocococococo = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)
                                                                                                    cocoDoom01 = unpack("<I", f.read(4))[0]
                                                                                                    if cocoDoom01 == 1627553851:
                                                                                                        cocoNounsNum01 = unpack("<I", f.read(4))[0]
                                                                                                        if cocoNounsNum01 == 12:
                                                                                                            f.seek(2,1)
                                                                                                            cocoDoomCount1 = unpack("B", f.read(1))[0]
                                                                                                            cocoDoomFlag1 = unpack("B", f.read(1))[0]
                                                                                                            if cocoDoomFlag1 == 0x6C:
                                                                                                                if cocoDoomCount1 == 2:
                                                                                                                    for i in range(1):
                                                                                                                        vx0001__AQ___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        vy0001__AQ___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        vz0001__AQ___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        type1__AQ___2cocococococo1 = unpack("B", f.read(1))[0]
                                                                                                                        f.seek(3,1)
                                                                                                                        vx0001__AR___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        vy0001__AR___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        vz0001__AR___2cocococococo1 = unpack("<f", f.read(4))[0]
                                                                                                                        type1__AR___2cocococococo1 = unpack("B", f.read(1))[0]
                                                                                                                        f.seek(3,1)
                                                                                                                    cocoisaPowerPuffGirl = unpack("<I", f.read(4))[0]
                                                                                                                    if cocoisaPowerPuffGirl == 1627553859:
                                                                                                                        cocoisnotgood = unpack("<I", f.read(4))[0]
                                                                                                                        if cocoisnotgood == 65550:
                                                                                                                            f.seek(2,1)
                                                                                                                            cocoisnotHealthyCount = unpack("B", f.read(1))[0]
                                                                                                                            cocoisnotHealthyFlag = unpack("B", f.read(1))[0]
                                                                                                                            if cocoisnotHealthyFlag == 0x6C:
                                                                                                                                if cocoisnotHealthyCount == 2:
                                                                                                                                    for i in range(1):
                                                                                                                                        vx0001__AQ___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        vy0001__AQ___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        vz0001__AQ___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        type1__AQ___2cocococococo2 = unpack("B", f.read(1))[0]
                                                                                                                                        f.seek(3,1)
                                                                                                                                        vx0001__AR___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        vy0001__AR___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        vz0001__AR___2cocococococo2 = unpack("<f", f.read(4))[0]
                                                                                                                                        type1__AR___2cocococococo2 = unpack("B", f.read(1))[0]
                                                                                                                                        f.seek(3,1)
                                                                                                                                    cocotooluv = unpack("<I", f.read(4))[0]
                                                                                                                                    if cocotooluv == 1627553867:
                                                                                                                                        cocoTooCrash1 = unpack("<I", f.read(4))[0]
                                                                                                                                        if cocoTooCrash1 == 16:
                                                                                                                                            f.seek(2,1)
                                                                                                                                            cocotooshortycount1 = unpack("B", f.read(1))[0]
                                                                                                                                            cocotooshortyflag1 = unpack("B", f.read(1))[0]
                                                                                                                                            if cocotooshortyflag1 == 0x6C:
                                                                                                                                                if cocotooshortycount1 == 2:
                                                                                                                                                    for i in range(1):
                                                                                                                                                        vx0001__AQ___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        vy0001__AQ___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        vz0001__AQ___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        type1__AQ___2cocococococo3 = unpack("B", f.read(1))[0]
                                                                                                                                                        f.seek(3,1)
                                                                                                                                                        vx0001__AR___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        vy0001__AR___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        vz0001__AR___2cocococococo3 = unpack("<f", f.read(4))[0]
                                                                                                                                                        type1__AR___2cocococococo3 = unpack("B", f.read(1))[0]
                                                                                                                                                        f.seek(3,1)

                                                                                                                                                    cocoEnd01 = unpack("<I", f.read(4))[0]
                                                                                                                                                    if cocoEnd01 == 16777473:
                                                                                                                                                        if type4AA___1aaCoco == 1:
                                                                                                                                                            if type4AB___1aaCoco == 1:
                                                                                                                                                                if type4AC___1aaCoco == 0:
                                                                                                                                                                    if type4AD___1aaCoco == 0:
                                                                                                                                                                        if type1__AO__ == 0:
                                                                                                                                                                            if type1__AP__ == 1:
                                                                                                                                                                                if type1__AQ___2 == 0:
                                                                                                                                                                                    if type1__AR___2 == 0:#0xdb50
                                                                                                                                                                                        if type1__AQ___2coco == 0:
                                                                                                                                                                                            if type1__AR___2coco == 1:
                                                                                                                                                                                                if type1__AQ___2cocococo == 0:
                                                                                                                                                                                                    if type1__AR___2cocococo == 0:#0xdbA8
                                                                                                                                                                                                        if type1__AQ___2cocococococo == 0:
                                                                                                                                                                                                            if type1__AR___2cocococococo == 1:
                                                                                                                                                                                                                if type1__AQ___2cocococococo1 == 0:
                                                                                                                                                                                                                    if type1__AR___2cocococococo1 == 0:
                                                                                                                                                                                                                        if type1__AQ___2cocococococo2 == 0:
                                                                                                                                                                                                                            if type1__AR___2cocococococo2 == 1:
                                                                                                                                                                                                                                if type1__AQ___2cocococococo3 == 0:
                                                                                                                                                                                                                                    if type1__AR___2cocococococo3 == 0:
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AA___1aaCoco,vz0001__AA___1aaCoco,vy0001__AA___1aaCoco])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AB___1aaCoco,vz0001__AB___1aaCoco,vy0001__AB___1aaCoco])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AC___1aaCoco,vz0001__AC___1aaCoco,vy0001__AC___1aaCoco])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AD___1aaCoco,vz0001__AD___1aaCoco,vy0001__AD___1aaCoco])

                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2,vz0001__AQ___2,vy0001__AQ___2])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2coco,vz0001__AQ___2coco,vy0001__AQ___2coco])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2cocococo,vz0001__AQ___2cocococo,vy0001__AQ___2cocococo])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2cocococococo,vz0001__AQ___2cocococococo,vy0001__AQ___2cocococococo])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2cocococococo1,vz0001__AQ___2cocococococo1,vy0001__AQ___2cocococococo1])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2cocococococo2,vz0001__AQ___2cocococococo2,vy0001__AQ___2cocococococo2])
                                                                                                                                                                                                                                        cocoVerts01.append([vx0001__AQ___2cocococococo3,vz0001__AQ___2cocococococo3,vy0001__AQ___2cocococococo3])

                                                                                                                                                                                                                                        cocoA+=1*12
                                                                                                                                                                                                                                        cocoB+=1*12
                                                                                                                                                                                                                                        cocoC+=1*12
                                                                                                                                                                                                                                        cocoD+=1*12
                                                                                                                                                                                                                                        cocoE+=1*12
                                                                                                                                                                                                                                        cocoF+=1*12
                                                                                                                                                                                                                                        cocoG+=1*12
                                                                                                                                                                                                                                        cocoH+=1*12
                                                                                                                                                                                                                                        cocoI+=1*12
                                                                                                                                                                                                                                        cocoJ+=1*12
                                                                                                                                                                                                                                        cocoK+=1*12
                                                                                                                                                                                                                                        cocoL+=1*12

                                                                                                                                                                                                                                        cocoFaces01.append([cocoA,cocoB,cocoC])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoB,cocoC,cocoE])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoC,cocoD,cocoE])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoD,cocoE,cocoF])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoE,cocoF,cocoG])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoF,cocoG,cocoH])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoG,cocoH,cocoI])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoH,cocoI,cocoJ])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoI,cocoJ,cocoK])
                                                                                                                                                                                                                                        cocoFaces01.append([cocoJ,cocoK,cocoL])
                                                                                                                                                        
                                                                                                                                                    
                                                                                                                                        
                                                                                                                            
                                                                                        
                                                elif vvavC3 == 14:
                                                    for i in range(1):
                                                        vx0001__AQ___ = unpack("<f", f.read(4))[0]
                                                        vy0001__AQ___ = unpack("<f", f.read(4))[0]
                                                        vz0001__AQ___ = unpack("<f", f.read(4))[0]
                                                        type1__AQ___ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR___ = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___ = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___ = unpack("<f", f.read(4))[0]
                                                        type1__AR___ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR___pt1 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt1 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt1 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt1 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt2 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt2 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt2 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt2 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt3 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt3 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt3 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt3 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt4 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt4 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt4 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt4 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt5 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt5 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt5 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt5 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt6 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt6 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt6 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt6 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt7 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt7 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt7 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt7 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt8 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt8 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt8 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt8 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt9 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt9 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt9 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt9 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt10 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt10 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt10 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt10 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt11 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt11 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt11 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt11 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AR___pt12 = unpack("<f", f.read(4))[0]
                                                        vy0001__AR___pt12 = unpack("<f", f.read(4))[0]
                                                        vz0001__AR___pt12 = unpack("<f", f.read(4))[0]
                                                        type1__AR___pt12 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                    vavy01 = unpack("<I", f.read(4))[0]
                                                    if vavy01 == 1627553851:
                                                        vvav = unpack("<I", f.read(4))[0]
                                                        if vvav == 65548:
                                                            f.seek(2,1)
                                                            vvavCount01 = unpack("B", f.read(1))[0]
                                                            vvavCount01Flag = unpack("B", f.read(1))[0]
                                                            if vvavCount01Flag == 0x6C:
                                                                if vvavCount01 == 2:
                                                                    for i in range(1):
                                                                        vx0001__AR___pt13 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AR___pt13 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AR___pt13 = unpack("<f", f.read(4))[0]
                                                                        type1__AR___pt13 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AR___pt14 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AR___pt14 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AR___pt14 = unpack("<f", f.read(4))[0]
                                                                        type1__AR___pt14 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                    vavy02 = unpack("<I", f.read(4))[0]
                                                                    if vavy02 == 1627553859:
                                                                        nnnum01 = unpack("<I", f.read(4))[0]
                                                                        if nnnum01 == 14:
                                                                            f.seek(2,1)
                                                                            vvavCount02 = unpack("B", f.read(1))[0]
                                                                            vvavCount02Flag = unpack("B", f.read(1))[0]
                                                                            if vvavCount02Flag == 0x6C:
                                                                                if vvavCount02 == 2:
                                                                                    for i in range(1):
                                                                                        vx0001__AR___pt15 = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AR___pt15 = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AR___pt15 = unpack("<f", f.read(4))[0]
                                                                                        type1__AR___pt15 = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AR___pt16 = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AR___pt16 = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AR___pt16 = unpack("<f", f.read(4))[0]
                                                                                        type1__AR___pt16 = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                    vavy03 = unpack("<I", f.read(4))[0]
                                                                                    if vavy03 == 1627553867:
                                                                                        vavy02 = unpack("<I", f.read(4))[0]
                                                                                        if vavy02 == 65554:
                                                                                            f.seek(2,1)
                                                                                            vvavCount03 = unpack("B", f.read(1))[0]
                                                                                            vvavCount03Flag = unpack("B", f.read(1))[0]
                                                                                            if vvavCount03Flag == 0x6C:
                                                                                                if vvavCount03 == 2:
                                                                                                    for i in range(1):
                                                                                                        vx0001__AR___pt17 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AR___pt17 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AR___pt17 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AR___pt17 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)

                                                                                                        vx0001__AR___pt18 = unpack("<f", f.read(4))[0]
                                                                                                        vy0001__AR___pt18 = unpack("<f", f.read(4))[0]
                                                                                                        vz0001__AR___pt18 = unpack("<f", f.read(4))[0]
                                                                                                        type1__AR___pt18 = unpack("B", f.read(1))[0]
                                                                                                        f.seek(3,1)
                                                                                                    vavy04 = unpack("<I", f.read(4))[0]
                                                                                                    if vavy04 == 1627553875:
                                                                                                        nnnum02 = unpack("<I", f.read(4))[0]
                                                                                                        if nnnum02 == 16:
                                                                                                            f.seek(2,1)
                                                                                                            vvavCount04 = unpack("B", f.read(1))[0]
                                                                                                            vvavCount04Flag = unpack("B", f.read(1))[0]
                                                                                                            if vvavCount04Flag == 0x6C:
                                                                                                                if vvavCount04 == 2:
                                                                                                                    for i in range(1):
                                                                                                                        vx0001__AR___pt19 = unpack("<f", f.read(4))[0]
                                                                                                                        vy0001__AR___pt19 = unpack("<f", f.read(4))[0]
                                                                                                                        vz0001__AR___pt19 = unpack("<f", f.read(4))[0]
                                                                                                                        type1__AR___pt19 = unpack("B", f.read(1))[0]
                                                                                                                        f.seek(3,1)

                                                                                                                        vx0001__AR___pt20 = unpack("<f", f.read(4))[0]
                                                                                                                        vy0001__AR___pt20 = unpack("<f", f.read(4))[0]
                                                                                                                        vz0001__AR___pt20 = unpack("<f", f.read(4))[0]
                                                                                                                        type1__AR___pt20 = unpack("B", f.read(1))[0]
                                                                                                                        f.seek(3,1)

                                                                                                                    EdEndoffse1 = unpack("<I", f.read(4))[0]
                                                                                                                    if EdEndoffse1 == 16777473:
                                                                                                                        if type4AA___ == 1:
                                                                                                                            if type4AB___ == 1:
                                                                                                                                if type4AC___ == 0:
                                                                                                                                    if type4AD___ == 0:
                                                                                                                                        if type1__AO__ == 0:
                                                                                                                                            if type1__AP__ == 1:
                                                                                                                                                if type1__AQ___ == 0:
                                                                                                                                                    if type1__AR___ == 0:
                                                                                                                                                        if type1__AR___pt1 == 0:
                                                                                                                                                            if type1__AR___pt2 == 0:
                                                                                                                                                                if type1__AR___pt3 == 0:
                                                                                                                                                                    if type1__AR___pt4 == 0:
                                                                                                                                                                        if type1__AR___pt5 == 0:
                                                                                                                                                                            if type1__AR___pt6 == 0:
                                                                                                                                                                                if type1__AR___pt7 == 0:
                                                                                                                                                                                    if type1__AR___pt8 == 0:
                                                                                                                                                                                        if type1__AR___pt9 == 0:
                                                                                                                                                                                            if type1__AR___pt10 == 0:
                                                                                                                                                                                                if type1__AR___pt11 == 0:
                                                                                                                                                                                                    if type1__AR___pt12 == 0:
                                                                                                                                                                                                        if type1__AR___pt13 == 0:
                                                                                                                                                                                                            if type1__AR___pt14 == 1:
                                                                                                                                                                                                                if type1__AR___pt15 == 0:
                                                                                                                                                                                                                    if type1__AR___pt16 == 0:
                                                                                                                                                                                                                        if type1__AR___pt17 == 0:
                                                                                                                                                                                                                            if type1__AR___pt18 == 1:
                                                                                                                                                                                                                                if type1__AR___pt19 == 0:
                                                                                                                                                                                                                                    if type1__AR___pt20 == 0:
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AA___,vz0001__AA___,vy0001__AA___])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AB___,vz0001__AB___,vy0001__AB___])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AC___,vz0001__AC___,vy0001__AC___])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AD___,vz0001__AD___,vy0001__AD___])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AQ___,vz0001__AQ___,vy0001__AQ___])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt1,vz0001__AR___pt1,vy0001__AR___pt1])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt3,vz0001__AR___pt3,vy0001__AR___pt3])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt5,vz0001__AR___pt5,vy0001__AR___pt5])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt7,vz0001__AR___pt7,vy0001__AR___pt7])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt9,vz0001__AR___pt9,vy0001__AR___pt9])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt11,vz0001__AR___pt11,vy0001__AR___pt11])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt13,vz0001__AR___pt13,vy0001__AR___pt13])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt15,vz0001__AR___pt15,vy0001__AR___pt15])
                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt17,vz0001__AR___pt17,vy0001__AR___pt17])

                                                                                                                                                                                                                                        vertices3Daqaq.append([vx0001__AR___pt19,vz0001__AR___pt19,vy0001__AR___pt19])

                                                                                                                                                                                                                                        fa2Ta_daT+=1*16
                                                                                                                                                                                                                                        fb2Ta_daT+=1*16
                                                                                                                                                                                                                                        fc2Ta_daT+=1*16
                                                                                                                                                                                                                                        fd2Ta_daT+=1*16
                                                                                                                                                                                                                                        fe2Ta_daT+=1*16

                                                                                                                                                                                                                                        ff2Ta_daT+=1*16
                                                                                                                                                                                                                                        fg2Ta_daT+=1*16
                                                                                                                                                                                                                                        fh2Ta_daT+=1*16
                                                                                                                                                                                                                                        fi2Ta_daT+=1*16

                                                                                                                                                                                                                                        fj2Ta_daT+=1*16
                                                                                                                                                                                                                                        fk2Ta_daT+=1*16
                                                                                                                                                                                                                                        fl2Ta_daT+=1*16

                                                                                                                                                                                                                                        fm2Ta_daT+=1*16

                                                                                                                                                                                                                                        faces3Daqaq.append([fa2Ta_daT,fb2Ta_daT,fc2Ta_daT])
                                                                                                                                                                                                                                        faces3Daqaq.append([fb2Ta_daT,fc2Ta_daT,fd2Ta_daT])
                                                                                                                                                                                                                                        faces3Daqaq.append([fb2Ta_daT,fd2Ta_daT,fe2Ta_daT])

                                                                                                                                                                                                                                        faces3Daqaq.append([ff2Ta_daT,fg2Ta_daT,fh2Ta_daT])
                                                                                                                                                                                                                                        faces3Daqaq.append([fg2Ta_daT,fh2Ta_daT,fi2Ta_daT])

                                                                                                                                                                                                                                        faces3Daqaq.append([fj2Ta_daT,fk2Ta_daT,fl2Ta_daT])
                                                                                                                                                                                                                                        faces3Daqaq.append([fj2Ta_daT,fl2Ta_daT,fm2Ta_daT])

                                                                                                                                                                                                                                        faces3Daqaq.append([fj2Ta_daT,fh2Ta_daT,fi2Ta_daT])
                                                                                                                                                                                                                
                                                                                                                                                        
                                                                                                                                            
                                                                                                                        
                                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                        
                                                                        
                                                        
                                                elif vvavC3 == 2:
                                                    for i in range(1):
                                                        vx0001__AQ__ = unpack("<f", f.read(4))[0]
                                                        vy0001__AQ__ = unpack("<f", f.read(4))[0]
                                                        vz0001__AQ__ = unpack("<f", f.read(4))[0]
                                                        type1__AQ__ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AR__ = unpack("<f", f.read(4))[0]
                                                        vy0001__AR__ = unpack("<f", f.read(4))[0]
                                                        vz0001__AR__ = unpack("<f", f.read(4))[0]
                                                        type1__AR__ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    fvflag4 = unpack("<I", f.read(4))[0]
                                                    if fvflag4 == 1627553827:
                                                        num02 = unpack("<I", f.read(4))[0]
                                                        if num02 == 65542:
                                                            f.seek(2,1)
                                                            vvavC5 = unpack("B", f.read(1))[0]
                                                            fvflag5 = unpack("B", f.read(1))[0]
                                                            if fvflag5 == 0x6C:
                                                                if vvavC5 == 2:
                                                                    for i in range(1):
                                                                        vx0001__AS__ = unpack("<f", f.read(4))[0]
                                                                        vy0001__AS__ = unpack("<f", f.read(4))[0]
                                                                        vz0001__AS__ = unpack("<f", f.read(4))[0]
                                                                        type1__AS__ = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AT__ = unpack("<f", f.read(4))[0]
                                                                        vy0001__AT__ = unpack("<f", f.read(4))[0]
                                                                        vz0001__AT__ = unpack("<f", f.read(4))[0]
                                                                        type1__AT__ = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                    fvflag6 = unpack("<I", f.read(4))[0]
                                                                    if fvflag6 == 1627553835:
                                                                        num03 = unpack("<I", f.read(4))[0]
                                                                        if num03 == 8:
                                                                            f.seek(2,1)
                                                                            vvavC7 = unpack("B", f.read(1))[0]
                                                                            fvflag7 = unpack("B", f.read(1))[0]
                                                                            if fvflag7 == 0x6C:
                                                                                if vvavC7 == 18:
                                                                                    for i in range(1):
                                                                                        vx0001__AU__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AU__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AU__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AU__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AV__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AV__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AV__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AV__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AW__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AW__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AW__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AW__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AX__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AX__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AX__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AX__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AY__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AY__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AY__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AY__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                        vx0001__AZZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AZZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AZZZZZZZZZZZZZ__ = unpack("<f", f.read(4))[0]
                                                                                        type1__AZZZZZZZZZZZZZ__ = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                    fvflag8 = unpack("<I", f.read(4))[0]
                                                                                    if fvflag8 == 1627553875:
                                                                                        num04 = unpack("<I", f.read(4))[0]
                                                                                        if num04 == 65548:
                                                                                            fvflag9 = unpack("<I", f.read(4))[0]
                                                                                            if fvflag9 == 1627553879:
                                                                                                num05 = unpack("<I", f.read(4))[0]
                                                                                                if num05 == 10:
                                                                                                    EEEndoffszett = unpack("<I", f.read(4))[0]
                                                                                                    if EEEndoffszett == 16777473:
                                                                                                        if type4AA__ == 1:
                                                                                                            if type4AB__ == 1:
                                                                                                                if type4AC__ == 0:
                                                                                                                    if type4AD__ == 0:
                                                                                                                        if type1__AO__ == 0:
                                                                                                                            if type1__AP__ == 1:
                                                                                                                                if type1__AQ__ == 0:
                                                                                                                                    if type1__AR__ == 0:
                                                                                                                                        if type1__AS__ == 0:
                                                                                                                                            if type1__AT__ == 1:
                                                                                                                                                if type1__AU__ == 0:
                                                                                                                                                    if type1__AV__ == 0:
                                                                                                                                                        if type1__AW__ == 0:
                                                                                                                                                            if type1__AX__ == 1:
                                                                                                                                                                if type1__AY__ == 0:
                                                                                                                                                                    if type1__AZ__ == 1:
                                                                                                                                                                        if type1__AZZ__ == 0:
                                                                                                                                                                            if type1__AZZZ__ == 0:
                                                                                                                                                                                if type1__AZZZZ__ == 0:
                                                                                                                                                                                    if type1__AZZZZZ__ == 0:
                                                                                                                                                                                        if type1__AZZZZZZ__ == 0:
                                                                                                                                                                                            if type1__AZZZZZZZ__ == 0:
                                                                                                                                                                                                if type1__AZZZZZZZZ__ == 0:
                                                                                                                                                                                                    if type1__AZZZZZZZZZ__ == 0:
                                                                                                                                                                                                        if type1__AZZZZZZZZZZ__ == 0:
                                                                                                                                                                                                            if type1__AZZZZZZZZZZZ__ == 0:
                                                                                                                                                                                                                if type1__AZZZZZZZZZZZZ__ == 0:
                                                                                                                                                                                                                    if type1__AZZZZZZZZZZZZZ__ == 1:
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AA__,vz0001__AA__,vy0001__AA__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AB__,vz0001__AB__,vy0001__AB__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AC__,vz0001__AC__,vy0001__AC__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AD__,vz0001__AD__,vy0001__AD__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AO__,vz0001__AO__,vy0001__AO__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AQ__,vz0001__AQ__,vy0001__AQ__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AS__,vz0001__AS__,vy0001__AS__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AU__,vz0001__AU__,vy0001__AU__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AW__,vz0001__AW__,vy0001__AW__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AY__,vz0001__AY__,vy0001__AY__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZ__,vz0001__AZZ__,vy0001__AZZ__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZZZ__,vz0001__AZZZZ__,vy0001__AZZZZ__])
                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZZZZZ__,vz0001__AZZZZZZ__,vy0001__AZZZZZZ__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZZZZZZZ__,vz0001__AZZZZZZZZ__,vy0001__AZZZZZZZZ__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZZZZZZZZZ__,vz0001__AZZZZZZZZZZ__,vy0001__AZZZZZZZZZZ__])

                                                                                                                                                                                                                        vertices3Daqa.append([vx0001__AZZZZZZZZZZZZ__,vz0001__AZZZZZZZZZZZZ__,vy0001__AZZZZZZZZZZZZ__])

                                                                                                                                                                                                                        fa2Ta_da+=1*28
                                                                                                                                                                                                                        fb2Ta_da+=1*28
                                                                                                                                                                                                                        fc2Ta_da+=1*28
                                                                                                                                                                                                                        fd2Ta_da+=1*28
                                                                                                                                                                                                                        fe2Ta_da+=1*28
                                                                                                                                                                                                                        ff2Ta_da+=1*28
                                                                                                                                                                                                                        fg2Ta_da+=1*28
                                                                                                                                                                                                                        fh2Ta_da+=1*28
                                                                                                                                                                                                                        fi2Ta_da+=1*28

                                                                                                                                                                                                                        fj2Ta_da+=1*28
                                                                                                                                                                                                                        fk2Ta_da+=1*28
                                                                                                                                                                                                                        fl2Ta_da+=1*28
                                                                                                                                                                                                                        fm2Ta_da+=1*28
                                                                                                                                                                                                                        fn2Ta_da+=1*28

                                                                                                                                                                                                                        fo2Ta_da+=1*28

                                                                                                                                                                                                                        faces3Daqa.append([fa2Ta_da,fb2Ta_da,fc2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fb2Ta_da,fc2Ta_da,fd2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fb2Ta_da,fd2Ta_da,fe2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fd2Ta_da,fe2Ta_da,ff2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fe2Ta_da,ff2Ta_da,fg2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([ff2Ta_da,fg2Ta_da,fh2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fg2Ta_da,fh2Ta_da,fi2Ta_da])

                                                                                                                                                                                                                        faces3Daqa.append([fj2Ta_da,fk2Ta_da,fl2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fk2Ta_da,fl2Ta_da,fm2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fl2Ta_da,fm2Ta_da,fn2Ta_da])
                                                                                                                                                                                                                        faces3Daqa.append([fm2Ta_da,fn2Ta_da,fo2Ta_da])

                                                                                                                                                                                                                        #faces3Daqa.append([fm2Ta_da,fo2Ta_da,fp2Ta_da])
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                        
                                                                                                        
                                                                                                    
                                                                                                    
                                                                                                
                                                                                        
                                                                                    
                                                                                
                                                                                
                                        
                        elif offffsetB == 65537:
                            f.seek(2,1)
                            vvcount1 = unpack("B", f.read(1))[0]
                            fflag1 = unpack("B", f.read(1))[0]
                            if fflag1 == 0x6C:
                                if vvcount1 == 28:
                                    for i in range(1):
                                        vx0001__AE__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AE__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AE__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AE__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AF__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AF__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AF__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AF__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AG__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AG__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AG__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AG__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AH__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AH__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AH__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AH__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AI__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AI__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AI__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AI__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AJ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AJ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AJ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AJ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AK__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AK__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AK__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AK__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AL__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AL__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AL__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AL__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AM__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AM__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AM__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AM__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AN__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AN__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AN__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AN__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AO__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AO__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AO__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AO__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AP__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AP__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AP__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AP__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AQ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AQ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AQ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AQ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AR__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AR__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AR__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AR__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AS__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AS__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AS__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AS__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AT__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AT__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AT__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AT__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AU__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AU__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AU__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AU__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AV__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AV__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AV__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AV__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AW__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AW__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AW__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AW__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AX__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AX__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AX__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AX__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AY__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AY__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AY__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AY__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZZZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZZZZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AZZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vy0001__AZZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        vz0001__AZZZZZZZ__overlord1 = unpack("<f", f.read(4))[0]
                                        type1__AZZZZZZZ__overlord1 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                    overlordSword1 = unpack("<I", f.read(4))[0]
                                    if overlordSword1 == 1627553871:
                                        overlordnear1 = unpack("<I", f.read(4))[0]
                                        if overlordnear1 == 65550:
                                            f.seek(2,1)
                                            overlordCount01 = unpack("B", f.read(1))[0]
                                            overlordCountFlag01 = unpack("B", f.read(1))[0]
                                            if overlordCountFlag01 == 0x6C:
                                                if overlordCount01 == 2:
                                                    for i in range(1):
                                                        vx0001__AZZZZZZZ1__overlord1 = unpack("<f", f.read(4))[0]
                                                        vy0001__AZZZZZZZ1__overlord1 = unpack("<f", f.read(4))[0]
                                                        vz0001__AZZZZZZZ1__overlord1 = unpack("<f", f.read(4))[0]
                                                        type1__AZZZZZZZ1__overlord1 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AZZZZZZZ2__overlord1 = unpack("<f", f.read(4))[0]
                                                        vy0001__AZZZZZZZ2__overlord1 = unpack("<f", f.read(4))[0]
                                                        vz0001__AZZZZZZZ2__overlord1 = unpack("<f", f.read(4))[0]
                                                        type1__AZZZZZZZ2__overlord1 = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                    overlordOffsett1 = unpack("<I", f.read(4))[0]
                                                    if overlordOffsett1 == 1627553879:
                                                        overlordCountC1 = unpack("<I", f.read(4))[0]
                                                        if overlordCountC1 == 12:
                                                            f.seek(2,1)
                                                            overlordmsgCount01 = unpack("B", f.read(1))[0]
                                                            overlordmsgFlag01 = unpack("B", f.read(1))[0]
                                                            if overlordmsgFlag01 == 0x6C:
                                                                if overlordmsgCount01 == 10:
                                                                    for i in range(1):
                                                                        vx0001__AZZZZZZZ3__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ3__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ3__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ3__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AZZZZZZZ4__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ4__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ4__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ4__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AZZZZZZZ5__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ5__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ5__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ5__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AZZZZZZZ6__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ6__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ6__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ6__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ7__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ7__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ7__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ7__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ8__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ8__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ8__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ8__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ9__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ9__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ9__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ9__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ10__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ10__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ10__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ10__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ11__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ11__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ11__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ11__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AZZZZZZZ12__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vy0001__AZZZZZZZ12__overlord1 = unpack("<f", f.read(4))[0]
                                                                        vz0001__AZZZZZZZ12__overlord1 = unpack("<f", f.read(4))[0]
                                                                        type1__AZZZZZZZ12__overlord1 = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                    if type4AA___1aaOverlord2 == 1:
                                                                        if type4AB___1aaOverlord2 == 1:
                                                                            if type4AC___1aaOverlord2 == 0:
                                                                                if type4AD___1aaOverlord2 == 0:
                                                                                    if type1__AE__overlord1 == 0:
                                                                                        if type1__AF__overlord1 == 1:
                                                                                            if type1__AG__overlord1 == 0:
                                                                                                if type1__AH__overlord1 == 0:
                                                                                                    if type1__AI__overlord1 == 0:
                                                                                                        if type1__AJ__overlord1 == 0:
                                                                                                            if type1__AK__overlord1 == 0:
                                                                                                                if type1__AL__overlord1 == 0:
                                                                                                                    if type1__AM__overlord1 == 0:
                                                                                                                        if type1__AN__overlord1 == 0:
                                                                                                                            if type1__AO__overlord1 == 0:
                                                                                                                                if type1__AP__overlord1 == 1:
                                                                                                                                    if type1__AQ__overlord1 == 0:
                                                                                                                                        if type1__AR__overlord1 == 1:
                                                                                                                                            if type1__AS__overlord1 == 0:
                                                                                                                                                if type1__AT__overlord1 == 0:
                                                                                                                                                    if type1__AU__overlord1 == 0:
                                                                                                                                                        if type1__AV__overlord1 == 0:
                                                                                                                                                            if type1__AW__overlord1 == 0:
                                                                                                                                                                if type1__AX__overlord1 == 1:
                                                                                                                                                                    if type1__AY__overlord1 == 0:
                                                                                                                                                                        if type1__AZ__overlord1 == 1:
                                                                                                                                                                            if type1__AZZ__overlord1 == 0:
                                                                                                                                                                                if type1__AZZZ__overlord1 == 0:
                                                                                                                                                                                    if type1__AZZZZ__overlord1 == 0:
                                                                                                                                                                                        if type1__AZZZZZ__overlord1 == 0:
                                                                                                                                                                                            if type1__AZZZZZZ__overlord1 == 0:
                                                                                                                                                                                                if type1__AZZZZZZZ__overlord1 == 1:
                                                                                                                                                                                                    if type1__AZZZZZZZ1__overlord1 == 0:
                                                                                                                                                                                                        if type1__AZZZZZZZ2__overlord1 == 0:
                                                                                                                                                                                                            if type1__AZZZZZZZ3__overlord1 == 0:
                                                                                                                                                                                                                if type1__AZZZZZZZ4__overlord1 == 1:
                                                                                                                                                                                                                    if type1__AZZZZZZZ5__overlord1 == 0:
                                                                                                                                                                                                                        if type1__AZZZZZZZ6__overlord1 == 1:
                                                                                                                                                                                                                            if type1__AZZZZZZZ7__overlord1 == 0:
                                                                                                                                                                                                                                if type1__AZZZZZZZ8__overlord1 == 0:
                                                                                                                                                                                                                                    if type1__AZZZZZZZ9__overlord1 == 0:
                                                                                                                                                                                                                                        if type1__AZZZZZZZ10__overlord1 == 1:
                                                                                                                                                                                                                                            if type1__AZZZZZZZ11__overlord1 == 0:
                                                                                                                                                                                                                                                if type1__AZZZZZZZ12__overlord1 == 1:
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AA___1aaOverlord2,vz0001__AA___1aaOverlord2,vy0001__AA___1aaOverlord2])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AB___1aaOverlord2,vz0001__AB___1aaOverlord2,vy0001__AB___1aaOverlord2])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AC___1aaOverlord2,vz0001__AC___1aaOverlord2,vy0001__AC___1aaOverlord2])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AD___1aaOverlord2,vz0001__AD___1aaOverlord2,vy0001__AD___1aaOverlord2])

                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AE__overlord1,vz0001__AE__overlord1,vy0001__AE__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AG__overlord1,vz0001__AG__overlord1,vy0001__AG__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AI__overlord1,vz0001__AI__overlord1,vy0001__AI__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AK__overlord1,vz0001__AK__overlord1,vy0001__AK__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AM__overlord1,vz0001__AM__overlord1,vy0001__AM__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AO__overlord1,vz0001__AO__overlord1,vy0001__AO__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AQ__overlord1,vz0001__AQ__overlord1,vy0001__AQ__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AS__overlord1,vz0001__AS__overlord1,vy0001__AS__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AU__overlord1,vz0001__AU__overlord1,vy0001__AU__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AW__overlord1,vz0001__AW__overlord1,vy0001__AW__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AY__overlord1,vz0001__AY__overlord1,vy0001__AY__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZ__overlord1,vz0001__AZZ__overlord1,vy0001__AZZ__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZ__overlord1,vz0001__AZZZZ__overlord1,vy0001__AZZZZ__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZ__overlord1,vz0001__AZZZZZZ__overlord1,vy0001__AZZZZZZ__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ1__overlord1,vz0001__AZZZZZZZ1__overlord1,vy0001__AZZZZZZZ1__overlord1])
                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ3__overlord1,vz0001__AZZZZZZZ3__overlord1,vy0001__AZZZZZZZ3__overlord1])

                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ5__overlord1,vz0001__AZZZZZZZ5__overlord1,vy0001__AZZZZZZZ5__overlord1])

                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ7__overlord1,vz0001__AZZZZZZZ7__overlord1,vy0001__AZZZZZZZ7__overlord1])

                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ9__overlord1,vz0001__AZZZZZZZ9__overlord1,vy0001__AZZZZZZZ9__overlord1])

                                                                                                                                                                                                                                                    overlordverts03.append([vx0001__AZZZZZZZ11__overlord1,vz0001__AZZZZZZZ11__overlord1,vy0001__AZZZZZZZ11__overlord1])

                                                                                                                                                                                                                                                    overlordA3+=1*24
                                                                                                                                                                                                                                                    overlordB3+=1*24
                                                                                                                                                                                                                                                    overlordC3+=1*24
                                                                                                                                                                                                                                                    overlordD3+=1*24
                                                                                                                                                                                                                                                    overlordE3+=1*24
                                                                                                                                                                                                                                                    overlordF3+=1*24
                                                                                                                                                                                                                                                    overlordG3+=1*24
                                                                                                                                                                                                                                                    overlordH3+=1*24
                                                                                                                                                                                                                                                    overlordI3+=1*24

                                                                                                                                                                                                                                                    overlordJ3+=1*24
                                                                                                                                                                                                                                                    overlordK3+=1*24
                                                                                                                                                                                                                                                    overlordL3+=1*24
                                                                                                                                                                                                                                                    overlordM3+=1*24

                                                                                                                                                                                                                                                    overlordN3+=1*24
                                                                                                                                                                                                                                                    overlordO3+=1*24
                                                                                                                                                                                                                                                    overlordP3+=1*24
                                                                                                                                                                                                                                                    overlordQ3+=1*24
                                                                                                                                                                                                                                                    overlordR3+=1*24

                                                                                                                                                                                                                                                    overlordS3+=1*24
                                                                                                                                                                                                                                                    overlordT3+=1*24
                                                                                                                                                                                                                                                    overlordU3+=1*24
                                                                                                                                                                                                                                                    overlordV3+=1*24

                                                                                                                                                                                                                                                    overlordW3+=1*24

                                                                                                                                                                                                                                                    overlordfaces03.append([overlordA3,overlordB3,overlordC3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordB3,overlordC3,overlordD3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordA3,overlordC3,overlordE3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordA3,overlordE3,overlordF3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordE3,overlordF3,overlordG3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordF3,overlordG3,overlordH3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordG3,overlordH3,overlordI3])

                                                                                                                                                                                                                                                    overlordfaces03.append([overlordJ3,overlordK3,overlordL3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordK3,overlordL3,overlordM3])

                                                                                                                                                                                                                                                    overlordfaces03.append([overlordN3,overlordO3,overlordP3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordN3,overlordP3,overlordW3])
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordK3,overlordM3,overlordQ3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordM3,overlordQ3,overlordR3])

                                                                                                                                                                                                                                                    overlordfaces03.append([overlordS3,overlordT3,overlordU3])
                                                                                                                                                                                                                                                    overlordfaces03.append([overlordS3,overlordT3,overlordV3])
                                                                                                                                                                                                

                                                        
                                                        
                                            
                                    
                                elif vvcount1 == 6:
                                    for i in range(1):
                                        vx0001__AE__ = unpack("<f", f.read(4))[0]
                                        vy0001__AE__ = unpack("<f", f.read(4))[0]
                                        vz0001__AE__ = unpack("<f", f.read(4))[0]
                                        type1__AE__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AF__ = unpack("<f", f.read(4))[0]
                                        vy0001__AF__ = unpack("<f", f.read(4))[0]
                                        vz0001__AF__ = unpack("<f", f.read(4))[0]
                                        type1__AF__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AG__ = unpack("<f", f.read(4))[0]
                                        vy0001__AG__ = unpack("<f", f.read(4))[0]
                                        vz0001__AG__ = unpack("<f", f.read(4))[0]
                                        type1__AG__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AH__ = unpack("<f", f.read(4))[0]
                                        vy0001__AH__ = unpack("<f", f.read(4))[0]
                                        vz0001__AH__ = unpack("<f", f.read(4))[0]
                                        type1__AH__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)

                                        vx0001__AI__ = unpack("<f", f.read(4))[0]
                                        vy0001__AI__ = unpack("<f", f.read(4))[0]
                                        vz0001__AI__ = unpack("<f", f.read(4))[0]
                                        type1__AI__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AJ__ = unpack("<f", f.read(4))[0]
                                        vy0001__AJ__ = unpack("<f", f.read(4))[0]
                                        vz0001__AJ__ = unpack("<f", f.read(4))[0]
                                        type1__AJ__ = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                    for i in range(vvcount1):
                                        f.seek(-16,1)
                                    for i in range(1):
                                        vx0001__AE__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AE__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AE__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AE__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AF__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AF__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AF__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AF__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AG__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AG__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AG__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AG__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AH__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AH__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AH__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AH__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AI__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AI__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AI__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AI__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AJ__overlord01 = unpack("<f", f.read(4))[0]
                                        vy0001__AJ__overlord01 = unpack("<f", f.read(4))[0]
                                        vz0001__AJ__overlord01 = unpack("<f", f.read(4))[0]
                                        type1__AJ__overlord01 = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                    offffsetCC = unpack("<I", f.read(4))[0]
                                    if offffsetCC == 1627553827:
                                        offffsetDD = unpack("<I", f.read(4))[0]
                                        if offffsetDD == 65542:
                                            f.seek(2,1)
                                            vvacount1 = unpack("B", f.read(1))[0]
                                            faflag1A = unpack("B", f.read(1))[0]
                                            if faflag1A != 0x6C:
                                                f.seek(-4,1)
                                                overlorddemandoffset01 = unpack("<I", f.read(4))[0]
                                                if overlorddemandoffset01 == 1627553831:
                                                    overlordis4 = unpack("<I", f.read(4))[0]
                                                    if overlordis4 == 4:
                                                        overlordisnot4End01 = unpack("<I", f.read(4))[0]
                                                        if overlordisnot4End01 == 16777473:
                                                            if type4AA___1aaOverlord4 == 1:
                                                                if type4AB___1aaOverlord4 == 1:
                                                                    if type4AC___1aaOverlord4 == 0:
                                                                        if type4AD___1aaOverlord4 == 0:
                                                                            if type1__AE__overlord01 == 0:
                                                                                if type1__AF__overlord01 == 1:
                                                                                    if type1__AG__overlord01 == 0:
                                                                                        if type1__AH__overlord01 == 0:
                                                                                            if type1__AI__overlord01 == 0:
                                                                                                if type1__AJ__overlord01 == 1:
                                                                                                    overlordverts05.append([vx0001__AA___1aaOverlord4,vz0001__AA___1aaOverlord4,vy0001__AA___1aaOverlord4])
                                                                                                    overlordverts05.append([vx0001__AB___1aaOverlord4,vz0001__AB___1aaOverlord4,vy0001__AB___1aaOverlord4])
                                                                                                    overlordverts05.append([vx0001__AC___1aaOverlord4,vz0001__AC___1aaOverlord4,vy0001__AC___1aaOverlord4])
                                                                                                    overlordverts05.append([vx0001__AD___1aaOverlord4,vz0001__AD___1aaOverlord4,vy0001__AD___1aaOverlord4])

                                                                                                    overlordverts05.append([vx0001__AE__overlord01,vz0001__AE__overlord01,vy0001__AE__overlord01])
                                                                                                    overlordverts05.append([vx0001__AG__overlord01,vz0001__AG__overlord01,vy0001__AG__overlord01])
                                                                                                    overlordverts05.append([vx0001__AI__overlord01,vz0001__AI__overlord01,vy0001__AI__overlord01])

                                                                                                    overlordA5+=1*7
                                                                                                    overlordB5+=1*7
                                                                                                    overlordC5+=1*7
                                                                                                    overlordD5+=1*7
                                                                                                    overlordE5+=1*7
                                                                                                    overlordF5+=1*7
                                                                                                    overlordG5+=1*7

                                                                                                    overlordfaces05.append([overlordA5,overlordB5,overlordC5])
                                                                                                    overlordfaces05.append([overlordB5,overlordC5,overlordD5])
                                                                                                    overlordfaces05.append([overlordC5,overlordD5,overlordE5])
                                                                                                    overlordfaces05.append([overlordA5,overlordE5,overlordF5])
                                                                                                    overlordfaces05.append([overlordD5,overlordC5,overlordG5])
                                            elif faflag1A == 0x6C:
                                                if vvacount1 == 2:
                                                    for i in range(1):
                                                        vx0001__AK__ = unpack("<f", f.read(4))[0]
                                                        vy0001__AK__ = unpack("<f", f.read(4))[0]
                                                        vz0001__AK__ = unpack("<f", f.read(4))[0]
                                                        type1__AK__ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                        vx0001__AL__ = unpack("<f", f.read(4))[0]
                                                        vy0001__AL__ = unpack("<f", f.read(4))[0]
                                                        vz0001__AL__ = unpack("<f", f.read(4))[0]
                                                        type1__AL__ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    offffsetEE = unpack("<I", f.read(4))[0]
                                                    if offffsetEE == 1627553835:
                                                        offffsetFF = unpack("<I", f.read(4))[0]
                                                        if offffsetFF == 8:
                                                            f.seek(2,1)
                                                            vvbcount1 = unpack("B", f.read(1))[0]
                                                            fbflag1A = unpack("B", f.read(1))[0]
                                                            if fbflag1A == 0x6C:
                                                                if vvbcount1 == 2:
                                                                    for i in range(1):
                                                                        vx0001__AM__ = unpack("<f", f.read(4))[0]
                                                                        vy0001__AM__ = unpack("<f", f.read(4))[0]
                                                                        vz0001__AM__ = unpack("<f", f.read(4))[0]
                                                                        type1__AM__ = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                        vx0001__AN__ = unpack("<f", f.read(4))[0]
                                                                        vy0001__AN__ = unpack("<f", f.read(4))[0]
                                                                        vz0001__AN__ = unpack("<f", f.read(4))[0]
                                                                        type1__AN__ = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                    offffsetGG = unpack("<I", f.read(4))[0]
                                                                    if offffsetGG == 1627553843:
                                                                        offffsetHH = unpack("<I", f.read(4))[0]
                                                                        if offffsetHH == 65546:
                                                                            #0x25730
                                                                            f.seek(2,1)
                                    
                                elif vvcount1 == 2:
                                    
                                    for i in range(1):
                                        vx0001__AE = unpack("<f", f.read(4))[0]
                                        vy0001__AE = unpack("<f", f.read(4))[0]
                                        vz0001__AE = unpack("<f", f.read(4))[0]
                                        type1__AE = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                        vx0001__AF = unpack("<f", f.read(4))[0]
                                        vy0001__AF = unpack("<f", f.read(4))[0]
                                        vz0001__AF = unpack("<f", f.read(4))[0]
                                        type1__AF = unpack("B", f.read(1))[0]
                                        f.seek(3,1)
                                    offffsetC = unpack("<I", f.read(4))[0]
                                    if offffsetC == 1627553819:
                                        offffsetD = unpack("<I", f.read(4))[0]
                                        if offffsetD == 2:
                                            f.seek(2,1)
                                            vvcount1A = unpack("B", f.read(1))[0]
                                            fflag1A = unpack("B", f.read(1))[0]
                                            if fflag1A == 0x6C:
                                                if vvcount1A == 4:
                                                    for i in range(1):
                                                        vx0001__AG = unpack("<f", f.read(4))[0]
                                                        vy0001__AG = unpack("<f", f.read(4))[0]
                                                        vz0001__AG = unpack("<f", f.read(4))[0]
                                                        type1__AG = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AH = unpack("<f", f.read(4))[0]
                                                        vy0001__AH = unpack("<f", f.read(4))[0]
                                                        vz0001__AH = unpack("<f", f.read(4))[0]
                                                        type1__AH = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AI = unpack("<f", f.read(4))[0]
                                                        vy0001__AI = unpack("<f", f.read(4))[0]
                                                        vz0001__AI = unpack("<f", f.read(4))[0]
                                                        type1__AI = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)

                                                        vx0001__AJ = unpack("<f", f.read(4))[0]
                                                        vy0001__AJ = unpack("<f", f.read(4))[0]
                                                        vz0001__AJ = unpack("<f", f.read(4))[0]
                                                        type1__AJ = unpack("B", f.read(1))[0]
                                                        f.seek(3,1)
                                                    offffsetE = unpack("<I", f.read(4))[0]
                                                    if offffsetE == 1627553831:
                                                        offffsetF = unpack("<I", f.read(4))[0]
                                                        if offffsetF == 65540:
                                                            f.seek(2,1)
                                                            vvcount1B = unpack("B", f.read(1))[0]
                                                            fflag1B = unpack("B", f.read(1))[0]
                                                            if fflag1B == 0x6C:
                                                                if vvcount1B == 2:
                                                                    for i in range(1):
                                                                        vx0001__AK = unpack("<f", f.read(4))[0]
                                                                        vy0001__AK = unpack("<f", f.read(4))[0]
                                                                        vz0001__AK = unpack("<f", f.read(4))[0]
                                                                        type1__AK = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)

                                                                        vx0001__AL = unpack("<f", f.read(4))[0]
                                                                        vy0001__AL = unpack("<f", f.read(4))[0]
                                                                        vz0001__AL = unpack("<f", f.read(4))[0]
                                                                        type1__AL = unpack("B", f.read(1))[0]
                                                                        f.seek(3,1)
                                                                    offffsetF = unpack("<I", f.read(4))[0]
                                                                    if offffsetF == 1627553839:
                                                                        offffsetG = unpack("<I", f.read(4))[0]
                                                                        if offffsetG == 2:
                                                                            f.seek(2,1)
                                                                            vvcount1C = unpack("B", f.read(1))[0]
                                                                            fflag1C = unpack("B", f.read(1))[0]
                                                                            if fflag1C == 0x6C:
                                                                                if vvcount1C == 2:
                                                                                    for i in range(1):
                                                                                        vx0001__AM = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AM = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AM = unpack("<f", f.read(4))[0]
                                                                                        type1__AM = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)

                                                                                        vx0001__AN = unpack("<f", f.read(4))[0]
                                                                                        vy0001__AN = unpack("<f", f.read(4))[0]
                                                                                        vz0001__AN = unpack("<f", f.read(4))[0]
                                                                                        type1__AN = unpack("B", f.read(1))[0]
                                                                                        f.seek(3,1)
                                                                                    offffsetG = unpack("<I", f.read(4))[0]
                                                                                    if offffsetG == 1627553847:
                                                                                        offffsetH = unpack("<I", f.read(4))[0]
                                                                                        if offffsetH == 9:
                                                                                            offffsetI = unpack("<I", f.read(4))[0]
                                                                                            if offffsetI == 16777473:
                                                                                                if type4AA == 1:
                                                                                                    if type4AB == 1:
                                                                                                        if type4AC == 0:
                                                                                                            if type4AD == 0:
                                                                                                                if type1__AE == 0:
                                                                                                                    if type1__AF == 1:
                                                                                                                        if type1__AG == 0:
                                                                                                                            if type1__AH == 0:
                                                                                                                                if type1__AI == 0:
                                                                                                                                    if type1__AJ == 0:
                                                                                                                                        if type1__AK == 0:
                                                                                                                                            if type1__AL == 1:
                                                                                                                                                if type1__AM == 0:
                                                                                                                                                    if type1__AN == 0:
                                                                                                                                                        vertices3Baq.append([vx0001__AA,vz0001__AA,vy0001__AA])
                                                                                                                                                        vertices3Baq.append([vx0001__AB,vz0001__AB,vy0001__AB])
                                                                                                                                                        vertices3Baq.append([vx0001__AC,vz0001__AC,vy0001__AC])

                                                                                                                                                        vertices3Baq.append([vx0001__AD,vz0001__AD,vy0001__AD])

                                                                                                                                                        vertices3Baq.append([vx0001__AE,vz0001__AE,vy0001__AE])

                                                                                                                                                        vertices3Baq.append([vx0001__AG,vz0001__AG,vy0001__AG])

                                                                                                                                                        fa2Ta_c+=1*6
                                                                                                                                                        fb2Ta_c+=1*6
                                                                                                                                                        fc2Ta_c+=1*6
                                                                                                                                                        fd2Ta_c+=1*6
                                                                                                                                                        fe2Ta_c+=1*6
                                                                                                                                                        ff2Ta_c+=1*6

                                                                                                                                                        faces3Baq.append([fa2Ta_c,fb2Ta_c,fc2Ta_c])
                                                                                                                                                        faces3Baq.append([fb2Ta_c,fc2Ta_c,fd2Ta_c])

                elif vertexCount == 5:
                    for j in range(1):
                        vx0001__BA = unpack("<f", f.read(4))[0]
                        vy0001__BA = unpack("<f", f.read(4))[0]
                        vz0001__BA = unpack("<f", f.read(4))[0]
                        brightness__BA = unpack("<f", f.read(4))[0]
                        uvx0001__BA = unpack("<f", f.read(4))[0]
                        uvy0001__BA = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4BA = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__BB = unpack("<f", f.read(4))[0]
                        vy0001__BB = unpack("<f", f.read(4))[0]
                        vz0001__BB = unpack("<f", f.read(4))[0]
                        brightness__BB = unpack("<f", f.read(4))[0]
                        uvx0001__BB = unpack("<f", f.read(4))[0]
                        uvy0001__BB = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4BB = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__BC = unpack("<f", f.read(4))[0]
                        vy0001__BC = unpack("<f", f.read(4))[0]
                        vz0001__BC = unpack("<f", f.read(4))[0]
                        brightness__BC = unpack("<f", f.read(4))[0]
                        uvx0001__BC = unpack("<f", f.read(4))[0]
                        uvy0001__BC = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4BC = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__BD = unpack("<f", f.read(4))[0]
                        vy0001__BD = unpack("<f", f.read(4))[0]
                        vz0001__BD = unpack("<f", f.read(4))[0]
                        brightness__BD = unpack("<f", f.read(4))[0]
                        uvx0001__BD = unpack("<f", f.read(4))[0]
                        uvy0001__BD = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4BD = unpack("B", f.read(1))[0]
                        f.seek(3,1)

                        vx0001__BE = unpack("<f", f.read(4))[0]
                        vy0001__BE = unpack("<f", f.read(4))[0]
                        vz0001__BE = unpack("<f", f.read(4))[0]
                        brightness__BE = unpack("<f", f.read(4))[0]
                        uvx0001__BE = unpack("<f", f.read(4))[0]
                        uvy0001__BE = unpack("<f", f.read(4))[0]
                        f.seek(4,1)
                        type4BE = unpack("B", f.read(1))[0]
                        f.seek(3,1)
                                                                                                                                
                                                                                                        
                                                                            
                                                            
                                                    

    
    
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    meshh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    meshh.from_pydata(vertices, [], faces)
    objectsh = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), meshh)
    collection.objects.link(objectsh)

    mesh3FF = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3FF.from_pydata(vertices3FF, [], faces3FF)
    objects3FF = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3FF)
    collection.objects.link(objects3FF)

    uv_tex3FF = mesh3FF.uv_layers.new()
    uv_layer3FF = mesh3FF.uv_layers[0].data
    vert_loops3FF = {}
    for l in mesh3FF.loops:
        vert_loops3FF.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3FF):
        for li in vert_loops3FF[i]:
            uv_layer3FF[li].uv = coord

    mesh3GG = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3GG.from_pydata(vertices3GG, [], faces3GG)
    objects3GG = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3GG)
    collection.objects.link(objects3GG)

    uv_tex3GG = mesh3GG.uv_layers.new()
    uv_layer3GG = mesh3GG.uv_layers[0].data
    vert_loops3GG = {}
    for l in mesh3GG.loops:
        vert_loops3GG.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3GG):
        for li in vert_loops3GG[i]:
            uv_layer3GG[li].uv = coord

    mesh3HH = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3HH.from_pydata(vertices3HH, [], faces3HH)
    objects3HH = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3HH)
    collection.objects.link(objects3HH)

    uv_tex3HH = mesh3HH.uv_layers.new()
    uv_layer3HH = mesh3HH.uv_layers[0].data
    vert_loops3HH = {}
    for l in mesh3HH.loops:
        vert_loops3HH.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3HH):
        for li in vert_loops3HH[i]:
            uv_layer3HH[li].uv = coord

    mesh3II = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3II.from_pydata(vertices3II, [], faces3II)
    objects3II = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3II)
    collection.objects.link(objects3II)

    uv_tex3II = mesh3II.uv_layers.new()
    uv_layer3II = mesh3II.uv_layers[0].data
    vert_loops3II = {}
    for l in mesh3II.loops:
        vert_loops3II.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3II):
        for li in vert_loops3II[i]:
            uv_layer3II[li].uv = coord

    mesh3JJ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3JJ.from_pydata(vertices3JJ, [], faces3JJ)
    objects3JJ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3JJ)
    collection.objects.link(objects3JJ)

    uv_tex3JJ = mesh3JJ.uv_layers.new()
    uv_layer3JJ = mesh3JJ.uv_layers[0].data
    vert_loops3JJ = {}
    for l in mesh3JJ.loops:
        vert_loops3JJ.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3JJ):
        for li in vert_loops3JJ[i]:
            uv_layer3JJ[li].uv = coord


    mesh3KK = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3KK.from_pydata(vertices3KK, [], faces3KK)
    objects3KK = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3KK)
    collection.objects.link(objects3KK)

    uv_tex3KK = mesh3KK.uv_layers.new()
    uv_layer3KK = mesh3KK.uv_layers[0].data
    vert_loops3KK = {}
    for l in mesh3KK.loops:
        vert_loops3KK.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3KK):
        for li in vert_loops3KK[i]:
            uv_layer3KK[li].uv = coord

    mesh3LL = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3LL.from_pydata(vertices3LL, [], faces3LL)
    objects3LL = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3LL)
    collection.objects.link(objects3LL)

    uv_tex3LL = mesh3LL.uv_layers.new()
    uv_layer3LL = mesh3LL.uv_layers[0].data
    vert_loops3LL = {}
    for l in mesh3LL.loops:
        vert_loops3LL.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3LL):
        for li in vert_loops3LL[i]:
            uv_layer3LL[li].uv = coord


    mesh3MM = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3MM.from_pydata(vertices3MM, [], faces3MM)
    objects3MM = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3MM)
    collection.objects.link(objects3MM)

    uv_tex3MM = mesh3MM.uv_layers.new()
    uv_layer3MM = mesh3MM.uv_layers[0].data
    vert_loops3MM = {}
    for l in mesh3MM.loops:
        vert_loops3MM.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3MM):
        for li in vert_loops3MM[i]:
            uv_layer3MM[li].uv = coord


    mesh3NN = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3NN.from_pydata(vertices3NN, [], faces3NN)
    objects3NN = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3NN)
    collection.objects.link(objects3NN)

    uv_tex3NN = mesh3NN.uv_layers.new()
    uv_layer3NN = mesh3NN.uv_layers[0].data
    vert_loops3NN = {}
    for l in mesh3NN.loops:
        vert_loops3NN.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3NN):
        for li in vert_loops3NN[i]:
            uv_layer3NN[li].uv = coord


    mesh3OO = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3OO.from_pydata(vertices3OO, [], faces3OO)
    objects3OO = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3OO)
    collection.objects.link(objects3OO)

    uv_tex3OO = mesh3OO.uv_layers.new()
    uv_layer3OO = mesh3OO.uv_layers[0].data
    vert_loops3OO = {}
    for l in mesh3OO.loops:
        vert_loops3OO.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3OO):
        for li in vert_loops3OO[i]:
            uv_layer3OO[li].uv = coord


    mesh3PP = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3PP.from_pydata(vertices3PP, [], faces3PP)
    objects3PP = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3PP)
    collection.objects.link(objects3PP)

    uv_tex3PP = mesh3PP.uv_layers.new()
    uv_layer3PP = mesh3PP.uv_layers[0].data
    vert_loops3PP = {}
    for l in mesh3PP.loops:
        vert_loops3PP.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3PP):
        for li in vert_loops3PP[i]:
            uv_layer3PP[li].uv = coord


    mesh3QQ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3QQ.from_pydata(vertices3QQ, [], faces3QQ)
    objects3QQ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3QQ)
    collection.objects.link(objects3QQ)

    uv_tex3QQ = mesh3QQ.uv_layers.new()
    uv_layer3QQ = mesh3QQ.uv_layers[0].data
    vert_loops3QQ = {}
    for l in mesh3QQ.loops:
        vert_loops3QQ.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3QQ):
        for li in vert_loops3QQ[i]:
            uv_layer3QQ[li].uv = coord

    mesh3RR = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3RR.from_pydata(vertices3RR, [], faces3RR)
    objects3RR = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3RR)
    collection.objects.link(objects3RR)

    uv_tex3RR = mesh3RR.uv_layers.new()
    uv_layer3RR = mesh3RR.uv_layers[0].data
    vert_loops3RR = {}
    for l in mesh3RR.loops:
        vert_loops3RR.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3RR):
        for li in vert_loops3RR[i]:
            uv_layer3RR[li].uv = coord


    mesh3SS = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3SS.from_pydata(vertices3SS, [], faces3SS)
    objects3SS = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3SS)
    collection.objects.link(objects3SS)

    uv_tex3SS = mesh3SS.uv_layers.new()
    uv_layer3SS = mesh3SS.uv_layers[0].data
    vert_loops3SS = {}
    for l in mesh3SS.loops:
        vert_loops3SS.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3SS):
        for li in vert_loops3SS[i]:
            uv_layer3SS[li].uv = coord


    mesh3TT = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3TT.from_pydata(vertices3TT, [], faces3TT)
    objects3TT = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3TT)
    collection.objects.link(objects3TT)

    uv_tex3TT = mesh3TT.uv_layers.new()
    uv_layer3TT = mesh3TT.uv_layers[0].data
    vert_loops3TT = {}
    for l in mesh3TT.loops:
        vert_loops3TT.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3TT):
        for li in vert_loops3TT[i]:
            uv_layer3TT[li].uv = coord


    mesh3UU = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3UU.from_pydata(vertices3UU, [], faces3UU)
    objects3UU = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3UU)
    collection.objects.link(objects3UU)

    uv_tex3UU = mesh3UU.uv_layers.new()
    uv_layer3UU = mesh3UU.uv_layers[0].data
    vert_loops3UU = {}
    for l in mesh3UU.loops:
        vert_loops3UU.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3UU):
        for li in vert_loops3UU[i]:
            uv_layer3UU[li].uv = coord


    mesh3VV = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3VV.from_pydata(vertices3VV, [], faces3VV)
    objects3VV = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3VV)
    collection.objects.link(objects3VV)

    uv_tex3VV = mesh3VV.uv_layers.new()
    uv_layer3VV = mesh3VV.uv_layers[0].data
    vert_loops3VV = {}
    for l in mesh3VV.loops:
        vert_loops3VV.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3VV):
        for li in vert_loops3VV[i]:
            uv_layer3VV[li].uv = coord

    mesh3WW = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3WW.from_pydata(vertices3WW, [], faces3WW)
    objects3WW = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3WW)
    collection.objects.link(objects3WW)

    uv_tex3WW = mesh3WW.uv_layers.new()
    uv_layer3WW = mesh3WW.uv_layers[0].data
    vert_loops3WW = {}
    for l in mesh3WW.loops:
        vert_loops3WW.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3WW):
        for li in vert_loops3WW[i]:
            uv_layer3WW[li].uv = coord


    mesh3XX = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3XX.from_pydata(vertices3XX, [], faces3XX)
    objects3XX = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3XX)
    collection.objects.link(objects3XX)

    uv_tex3XX = mesh3XX.uv_layers.new()
    uv_layer3XX = mesh3XX.uv_layers[0].data
    vert_loops3XX = {}
    for l in mesh3XX.loops:
        vert_loops3XX.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3XX):
        for li in vert_loops3XX[i]:
            uv_layer3XX[li].uv = coord



    mesh3YY = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3YY.from_pydata(vertices3YY, [], faces3YY)
    objects3YY = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3YY)
    collection.objects.link(objects3YY)

    uv_tex3YY = mesh3YY.uv_layers.new()
    uv_layer3YY = mesh3YY.uv_layers[0].data
    vert_loops3YY = {}
    for l in mesh3YY.loops:
        vert_loops3YY.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3YY):
        for li in vert_loops3YY[i]:
            uv_layer3YY[li].uv = coord


    mesh3ZZ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZ.from_pydata(vertices3ZZ, [], faces3ZZ)
    objects3ZZ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZ)
    collection.objects.link(objects3ZZ)

    uv_tex3ZZ = mesh3ZZ.uv_layers.new()
    uv_layer3ZZ = mesh3ZZ.uv_layers[0].data
    vert_loops3ZZ = {}
    for l in mesh3ZZ.loops:
        vert_loops3ZZ.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZ):
        for li in vert_loops3ZZ[i]:
            uv_layer3ZZ[li].uv = coord


    mesh3ZZZ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ.from_pydata(vertices3ZZZ, [], faces3ZZZ)
    objects3ZZZ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ)
    collection.objects.link(objects3ZZZ)

    uv_tex3ZZZ = mesh3ZZZ.uv_layers.new()
    uv_layer3ZZZ = mesh3ZZZ.uv_layers[0].data
    vert_loops3ZZZ = {}
    for l in mesh3ZZZ.loops:
        vert_loops3ZZZ.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ):
        for li in vert_loops3ZZZ[i]:
            uv_layer3ZZZ[li].uv = coord


    mesh3ZZZ1 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ1.from_pydata(vertices3ZZZ1, [], faces3ZZZ1)
    objects3ZZZ1 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ1)
    collection.objects.link(objects3ZZZ1)

    uv_tex3ZZZ1 = mesh3ZZZ1.uv_layers.new()
    uv_layer3ZZZ1 = mesh3ZZZ1.uv_layers[0].data
    vert_loops3ZZZ1 = {}
    for l in mesh3ZZZ1.loops:
        vert_loops3ZZZ1.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ1):
        for li in vert_loops3ZZZ1[i]:
            uv_layer3ZZZ1[li].uv = coord


    mesh3ZZZ2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ2.from_pydata(vertices3ZZZ2, [], faces3ZZZ2)
    objects3ZZZ2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ2)
    collection.objects.link(objects3ZZZ2)

    uv_tex3ZZZ2 = mesh3ZZZ2.uv_layers.new()
    uv_layer3ZZZ2 = mesh3ZZZ2.uv_layers[0].data
    vert_loops3ZZZ2 = {}
    for l in mesh3ZZZ2.loops:
        vert_loops3ZZZ2.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ2):
        for li in vert_loops3ZZZ2[i]:
            uv_layer3ZZZ2[li].uv = coord


    mesh3ZZZ3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ3.from_pydata(vertices3ZZZ3, [], faces3ZZZ3)
    objects3ZZZ3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ3)
    collection.objects.link(objects3ZZZ3)

    uv_tex3ZZZ3 = mesh3ZZZ3.uv_layers.new()
    uv_layer3ZZZ3 = mesh3ZZZ3.uv_layers[0].data
    vert_loops3ZZZ3 = {}
    for l in mesh3ZZZ3.loops:
        vert_loops3ZZZ3.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ3):
        for li in vert_loops3ZZZ3[i]:
            uv_layer3ZZZ3[li].uv = coord

    mesh3ZZZ4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ4.from_pydata(vertices3ZZZ4, [], faces3ZZZ4)
    objects3ZZZ4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ4)
    collection.objects.link(objects3ZZZ4)

    uv_tex3ZZZ4 = mesh3ZZZ4.uv_layers.new()
    uv_layer3ZZZ4 = mesh3ZZZ4.uv_layers[0].data
    vert_loops3ZZZ4 = {}
    for l in mesh3ZZZ4.loops:
        vert_loops3ZZZ4.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ4):
        for li in vert_loops3ZZZ4[i]:
            uv_layer3ZZZ4[li].uv = coord

    mesh3ZZZ5 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ5.from_pydata(vertices3ZZZ5, [], faces3ZZZ5)
    objects3ZZZ5 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ5)
    collection.objects.link(objects3ZZZ5)

    uv_tex3ZZZ5 = mesh3ZZZ5.uv_layers.new()
    uv_layer3ZZZ5 = mesh3ZZZ5.uv_layers[0].data
    vert_loops3ZZZ5 = {}
    for l in mesh3ZZZ5.loops:
        vert_loops3ZZZ5.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ5):
        for li in vert_loops3ZZZ5[i]:
            uv_layer3ZZZ5[li].uv = coord


    mesh3ZZZ6 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3ZZZ6.from_pydata(vertices3ZZZ6, [], faces3ZZZ6)
    objects3ZZZ6 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3ZZZ6)
    collection.objects.link(objects3ZZZ6)

    uv_tex3ZZZ6 = mesh3ZZZ6.uv_layers.new()
    uv_layer3ZZZ6 = mesh3ZZZ6.uv_layers[0].data
    vert_loops3ZZZ6 = {}
    for l in mesh3ZZZ6.loops:
        vert_loops3ZZZ6.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3ZZZ6):
        for li in vert_loops3ZZZ6[i]:
            uv_layer3ZZZ6[li].uv = coord


    mesh3BBpt2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3BBpt2.from_pydata(vertices3BBpt2, [], faces3BBpt2)
    objects3BBpt2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3BBpt2)
    collection.objects.link(objects3BBpt2)

    uv_tex3BBpt2 = mesh3BBpt2.uv_layers.new()
    uv_layer3BBpt2 = mesh3BBpt2.uv_layers[0].data
    vert_loops3BBpt2 = {}
    for l in mesh3BBpt2.loops:
        vert_loops3BBpt2.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3BBpt2):
        for li in vert_loops3BBpt2[i]:
            uv_layer3BBpt2[li].uv = coord

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3.from_pydata(vertices3, [], faces3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)

    mesh3yyA = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyA.from_pydata(vertices3A, [], faces3A)
    objects3yyA = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyA)
    collection.objects.link(objects3yyA)

    mesh3yyB = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyB.from_pydata(vertices3Aaq, [], faces3Aaq)
    objects3yyB = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyB)
    collection.objects.link(objects3yyB)

    mesh3yyC = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyC.from_pydata(vertices3Baq, [], faces3Baq)
    objects3yyC = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyC)
    collection.objects.link(objects3yyC)

    mesh3yyC = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyC.from_pydata(vertices3Baq, [], faces3Baq)
    objects3yyC = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyC)
    collection.objects.link(objects3yyC)

    mesh3yyD = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyD.from_pydata(vertices3Caq, [], faces3Caq)
    objects3yyD = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyD)
    collection.objects.link(objects3yyD)

    mesh3yyE = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyE.from_pydata(vertices3Daq, [], faces3Daq)
    objects3yyE = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyE)
    collection.objects.link(objects3yyE)

    mesh3yyF = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyF.from_pydata(vertices3Daqa, [], faces3Daqa)
    objects3yyF = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyF)
    collection.objects.link(objects3yyF)

    mesh3yyG = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyG.from_pydata(vertices3Daqaq, [], faces3Daqaq)
    objects3yyG = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyG)
    collection.objects.link(objects3yyG)

    mesh3yyH = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyH.from_pydata(vertices3Daqaqa, [], faces3Daqaqa)
    objects3yyH = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyH)
    collection.objects.link(objects3yyH)

    mesh3yyI = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyI.from_pydata(vertices3Daqaqaq, [], faces3Daqaqaq)
    objects3yyI = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyI)
    collection.objects.link(objects3yyI)

    mesh3yyJ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyJ.from_pydata(vertices3Daqaqaqe, [], faces3Daqaqaqe)
    objects3yyJ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyJ)
    collection.objects.link(objects3yyJ)

    mesh3yyK = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyK.from_pydata(cocoVerts01, [], cocoFaces01)
    objects3yyK = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyK)
    collection.objects.link(objects3yyK)

    mesh3yyL = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyL.from_pydata(cocoVerts02, [], cocoFaces02)
    objects3yyL = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyL)
    collection.objects.link(objects3yyL)

    mesh3yyM = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyM.from_pydata(overlordverts01, [], overlordfaces01)
    objects3yyM = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyM)
    collection.objects.link(objects3yyM)

    mesh3yyN = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyN.from_pydata(overlordverts02, [], overlordfaces02)
    objects3yyN = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyN)
    collection.objects.link(objects3yyN)

    mesh3yyO = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyO.from_pydata(overlordverts03, [], overlordfaces03)
    objects3yyO = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyO)
    collection.objects.link(objects3yyO)

    mesh3yyP = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyP.from_pydata(overlordverts04, [], overlordfaces04)
    objects3yyP = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyP)
    collection.objects.link(objects3yyP)

    mesh3yyQ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyQ.from_pydata(overlordverts05, [], overlordfaces05)
    objects3yyQ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyQ)
    collection.objects.link(objects3yyQ)

    mesh3yyR = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyR.from_pydata(overlordverts06, [], overlordfaces06)
    objects3yyR = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyR)
    collection.objects.link(objects3yyR)

    mesh3yyS = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyS.from_pydata(overlordverts07, [], overlordfaces07)
    objects3yyS = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyS)
    collection.objects.link(objects3yyS)

    mesh3yyT = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3yyT.from_pydata(overlordverts08, [], overlordfaces08)
    objects3yyT = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3yyT)
    collection.objects.link(objects3yyT)

    """for obj in bpy.context.scene.objects:
        if obj.name.startswith("nigel"):
            obj.select_set(True)

            bpy.ops.object.mode_set(mode='OBJECT')

            mesh = obj.data
    
    # Example: Create a face by specifying vertex indices
    # Ensure you have at least 3 vertices selected to form a polygon
        new_face = (0, 1, 2, 3)  # Replace with your vertex indices
        
        # Add the face to the mesh
        mesh.polygons.add(1)
        mesh.polygons[-1].vertices = new_face
        
        # Update the mesh to reflect changes
        mesh.update()
        
        # Switch back to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
    else:
        print("Please select a mesh object in edit mode.")"""


    objects3.parent = arma
    armamodifier3 = objects3.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3.object = arma

    vgroups3 = [objects3.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4.from_pydata(vertices2, [], faces2)
    objects4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4)
    collection.objects.link(objects4)

    uv_texauuu = mesh4.uv_layers.new()
    uv_layerauuu = mesh4.uv_layers[0].data
    vert_loopsauuu = {}
    try:
        
        for l in mesh4.loops:
            vert_loopsauuu.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs2):
            for li in vert_loopsauuu[i]:
                uv_layerauuu[li].uv = coord
    except:
        KeyError

    vindex = 0

    try:
        

        for vertex in mesh4.vertices:
            vertex.normal = normals2[vindex] # where "normals" is a list of normals
            vindex += 1
    except:
        AttributeError

    objects4.parent = arma
    armamodifier4 = objects4.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier4.object = arma

    vgroups4 = [objects4.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
            
    """obj = bpy.context.object

    obj.vertex_groups[0].add([0], 1, 'ADD')"""

    mesh4a = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4a.from_pydata(vertices2a, [], faces2a)
    objects4a = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4a)
    collection.objects.link(objects4a)

    uv_texa = mesh4a.uv_layers.new()
    uv_layera = mesh4a.uv_layers[0].data
    vert_loopsa = {}
    try:
        
        for l in mesh4a.loops:
            vert_loopsa.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs2a):
            for li in vert_loopsa[i]:
                uv_layera[li].uv = coord
    except:
        KeyError

    vindex = 0

    try:
        

        for vertex in mesh4a.vertices:
            vertex.normal = normals2a[vindex] # where "normals" is a list of normals
            vindex += 1
    except:
        AttributeError

    mesh4b = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4b.from_pydata(vertices2b, [], faces2b)
    objects4b = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4b)
    collection.objects.link(objects4b)

    uv_texb = mesh4b.uv_layers.new()
    uv_layerb = mesh4b.uv_layers[0].data
    vert_loopsb = {}
    try:
        
        for l in mesh4b.loops:
            vert_loopsb.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs2b):
            for li in vert_loopsb[i]:
                uv_layerb[li].uv = coord
    except:
        KeyError

    vindex = 0

    try:
        

        for vertex in mesh4b.vertices:
            vertex.normal = normals2b[vindex] # where "normals" is a list of normals
            vindex += 1
    except:
        AttributeError

    mesh4c = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4c.from_pydata(vertices2c, [], faces2c)
    objects4c = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4c)
    collection.objects.link(objects4c)

    uv_texc = mesh4c.uv_layers.new()
    uv_layerc = mesh4c.uv_layers[0].data
    vert_loopsc = {}
    for l in mesh4c.loops:
        vert_loopsc.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2c):
        for li in vert_loopsc[i]:
            uv_layerc[li].uv = coord

    mesh4d = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4d.from_pydata(vertices2d, [], faces2d)
    objects4d = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4d)
    collection.objects.link(objects4d)

    uv_texd = mesh4d.uv_layers.new()
    uv_layerd = mesh4d.uv_layers[0].data
    vert_loopsd = {}
    for l in mesh4d.loops:
        vert_loopsd.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2d):
        for li in vert_loopsd[i]:
            uv_layerd[li].uv = coord

    mesh4e = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4e.from_pydata(vertices2e, [], faces2e)
    objects4e = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4e)
    collection.objects.link(objects4e)

    uv_texe = mesh4e.uv_layers.new()
    uv_layere = mesh4e.uv_layers[0].data
    vert_loopse = {}
    for l in mesh4e.loops:
        vert_loopse.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2e):
        for li in vert_loopse[i]:
            uv_layere[li].uv = coord

    mesh4f = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4f.from_pydata(vertices2f, [], faces2f)
    objects4f = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4f)
    collection.objects.link(objects4f)

    uv_texf = mesh4f.uv_layers.new()
    uv_layerf = mesh4f.uv_layers[0].data
    vert_loopsf = {}
    for l in mesh4f.loops:
        vert_loopsf.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2f):
        for li in vert_loopsf[i]:
            uv_layerf[li].uv = coord

    mesh4g = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4g.from_pydata(vertices2g, [], faces2g)
    objects4g = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4g)
    collection.objects.link(objects4g)

    uv_texg = mesh4g.uv_layers.new()
    uv_layerg = mesh4g.uv_layers[0].data
    vert_loopsg = {}
    for l in mesh4g.loops:
        vert_loopsg.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2g):
        for li in vert_loopsg[i]:
            uv_layerg[li].uv = coord

    mesh4h = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4h.from_pydata(vertices2h, [], faces2h)
    objects4h = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4h)
    collection.objects.link(objects4h)

    uv_texh = mesh4h.uv_layers.new()
    uv_layerh = mesh4h.uv_layers[0].data
    vert_loopsh = {}
    for l in mesh4h.loops:
        vert_loopsh.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2h):
        for li in vert_loopsh[i]:
            uv_layerh[li].uv = coord

    mesh4i = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4i.from_pydata(vertices2i, [], faces2i)
    objects4i = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4i)
    collection.objects.link(objects4i)

    uv_texi = mesh4i.uv_layers.new()
    uv_layeri = mesh4i.uv_layers[0].data
    vert_loopsi = {}
    for l in mesh4i.loops:
        vert_loopsi.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2i):
        for li in vert_loopsi[i]:
            uv_layeri[li].uv = coord

    mesh4j = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4j.from_pydata(vertices2j, [], faces2j)
    objects4j = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4j)
    collection.objects.link(objects4j)

    uv_texj = mesh4j.uv_layers.new()
    uv_layerj = mesh4j.uv_layers[0].data
    vert_loopsj = {}
    for l in mesh4j.loops:
        vert_loopsj.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2j):
        for li in vert_loopsj[i]:
            uv_layerj[li].uv = coord

    mesh4k = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4k.from_pydata(vertices2k, [], faces2k)
    objects4k = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4k)
    collection.objects.link(objects4k)

    uv_texk = mesh4k.uv_layers.new()
    uv_layerk = mesh4k.uv_layers[0].data
    vert_loopsk = {}
    for l in mesh4k.loops:
        vert_loopsk.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2k):
        for li in vert_loopsk[i]:
            uv_layerk[li].uv = coord

    mesh4l = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4l.from_pydata(vertices2l, [], faces2l)
    objects4l = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4l)
    collection.objects.link(objects4l)

    uv_texl = mesh4l.uv_layers.new()
    uv_layerl = mesh4l.uv_layers[0].data
    vert_loopsl = {}
    for l in mesh4l.loops:
        vert_loopsl.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2l):
        for li in vert_loopsl[i]:
            uv_layerl[li].uv = coord

    mesh4m = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4m.from_pydata(vertices2m, [], faces2m)
    objects4m = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4m)
    collection.objects.link(objects4m)

    uv_texm = mesh4m.uv_layers.new()
    uv_layerm = mesh4m.uv_layers[0].data
    vert_loopsm = {}
    for l in mesh4m.loops:
        vert_loopsm.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2m):
        for li in vert_loopsm[i]:
            uv_layerm[li].uv = coord

    mesh4n = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4n.from_pydata(vertices2n, [], faces2n)
    objects4n = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4n)
    collection.objects.link(objects4n)

    uv_texn = mesh4n.uv_layers.new()
    uv_layern = mesh4n.uv_layers[0].data
    vert_loopsn = {}
    for l in mesh4n.loops:
        vert_loopsn.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2n):
        for li in vert_loopsn[i]:
            uv_layern[li].uv = coord

    mesh4o = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4o.from_pydata(vertices2o, [], faces2o)
    objects4o = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4o)
    collection.objects.link(objects4o)

    uv_texo = mesh4o.uv_layers.new()
    uv_layero = mesh4o.uv_layers[0].data
    vert_loopso = {}
    for l in mesh4o.loops:
        vert_loopso.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2o):
        for li in vert_loopso[i]:
            uv_layero[li].uv = coord

    mesh4p = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4p.from_pydata(vertices2p, [], faces2p)
    objects4p = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4p)
    collection.objects.link(objects4p)

    uv_texp = mesh4p.uv_layers.new()
    uv_layerp = mesh4p.uv_layers[0].data
    vert_loopsp = {}
    for l in mesh4p.loops:
        vert_loopsp.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2p):
        for li in vert_loopsp[i]:
            uv_layerp[li].uv = coord

    mesh4q = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4q.from_pydata(vertices2q, [], faces2q)
    objects4q = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4q)
    collection.objects.link(objects4q)

    uv_texq = mesh4q.uv_layers.new()
    uv_layerq = mesh4q.uv_layers[0].data
    vert_loopsq = {}
    for l in mesh4q.loops:
        vert_loopsq.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2q):
        for li in vert_loopsq[i]:
            uv_layerq[li].uv = coord

    mesh4r = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4r.from_pydata(vertices2r, [], faces2r)
    objects4r = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4r)
    collection.objects.link(objects4r)

    uv_texr = mesh4r.uv_layers.new()
    uv_layerr = mesh4r.uv_layers[0].data
    vert_loopsr = {}
    for l in mesh4r.loops:
        vert_loopsr.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2r):
        for li in vert_loopsr[i]:
            uv_layerr[li].uv = coord

    mesh4s = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4s.from_pydata(vertices2s, [], faces2s)
    objects4s = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4s)
    collection.objects.link(objects4s)

    uv_texs = mesh4s.uv_layers.new()
    uv_layers = mesh4s.uv_layers[0].data
    vert_loopss = {}
    for l in mesh4s.loops:
        vert_loopss.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2s):
        for li in vert_loopss[i]:
            uv_layers[li].uv = coord

    mesh4t = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4t.from_pydata(vertices2t, [], faces2t)
    objects4t = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4t)
    collection.objects.link(objects4t)

    uv_text = mesh4t.uv_layers.new()
    uv_layert = mesh4t.uv_layers[0].data
    vert_loopst = {}
    for l in mesh4t.loops:
        vert_loopst.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2t):
        for li in vert_loopst[i]:
            uv_layert[li].uv = coord

    mesh4u = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4u.from_pydata(vertices2u, [], faces2u)
    objects4u = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4u)
    collection.objects.link(objects4u)

    uv_texu = mesh4u.uv_layers.new()
    uv_layeru = mesh4u.uv_layers[0].data
    vert_loopsu = {}
    for l in mesh4u.loops:
        vert_loopsu.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2u):
        for li in vert_loopsu[i]:
            uv_layeru[li].uv = coord

    mesh4v = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4v.from_pydata(vertices2v, [], faces2v)
    objects4v = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4v)
    collection.objects.link(objects4v)

    uv_texv = mesh4v.uv_layers.new()
    uv_layerv = mesh4v.uv_layers[0].data
    vert_loopsv = {}
    for l in mesh4v.loops:
        vert_loopsv.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2v):
        for li in vert_loopsv[i]:
            uv_layerv[li].uv = coord

    mesh4w = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4w.from_pydata(vertices2w, [], faces2w)
    objects4w = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4w)
    collection.objects.link(objects4w)

    uv_texw = mesh4w.uv_layers.new()
    uv_layerw = mesh4w.uv_layers[0].data
    vert_loopsw = {}
    for l in mesh4w.loops:
        vert_loopsw.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2w):
        for li in vert_loopsw[i]:
            uv_layerw[li].uv = coord

    mesh4x = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4x.from_pydata(vertices2x, [], faces2x)
    objects4x = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4x)
    collection.objects.link(objects4x)

    uv_texx = mesh4x.uv_layers.new()
    uv_layerx = mesh4x.uv_layers[0].data
    vert_loopsx = {}
    for l in mesh4x.loops:
        vert_loopsx.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2x):
        for li in vert_loopsx[i]:
            uv_layerx[li].uv = coord

    mesh4y = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4y.from_pydata(vertices2y, [], faces2y)
    objects4y = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4y)
    collection.objects.link(objects4y)

    uv_texy = mesh4y.uv_layers.new()
    uv_layery = mesh4y.uv_layers[0].data
    vert_loopsy = {}
    for l in mesh4y.loops:
        vert_loopsy.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2y):
        for li in vert_loopsy[i]:
            uv_layery[li].uv = coord

    mesh4z = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4z.from_pydata(vertices2z, [], faces2z)
    objects4z = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4z)
    collection.objects.link(objects4z)

    uv_texz = mesh4z.uv_layers.new()
    uv_layerz = mesh4z.uv_layers[0].data
    vert_loopsz = {}
    for l in mesh4z.loops:
        vert_loopsz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2z):
        for li in vert_loopsz[i]:
            uv_layerz[li].uv = coord

    mesh4zz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zz.from_pydata(vertices2zz, [], faces2zz)
    objects4zz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zz)
    collection.objects.link(objects4zz)

    uv_texzz = mesh4zz.uv_layers.new()
    uv_layerzz = mesh4zz.uv_layers[0].data
    vert_loopszz = {}
    for l in mesh4zz.loops:
        vert_loopszz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zz):
        for li in vert_loopszz[i]:
            uv_layerzz[li].uv = coord

    mesh4zzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzz.from_pydata(vertices2zzz, [], faces2zzz)
    objects4zzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzz)
    collection.objects.link(objects4zzz)

    uv_texzzz = mesh4zzz.uv_layers.new()
    uv_layerzzz = mesh4zzz.uv_layers[0].data
    vert_loopszzz = {}
    for l in mesh4zzz.loops:
        vert_loopszzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzz):
        for li in vert_loopszzz[i]:
            uv_layerzzz[li].uv = coord

    mesh4zzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzz.from_pydata(vertices2zzzz, [], faces2zzzz)
    objects4zzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzz)
    collection.objects.link(objects4zzzz)

    uv_texzzzz = mesh4zzzz.uv_layers.new()
    uv_layerzzzz = mesh4zzzz.uv_layers[0].data
    vert_loopszzzz = {}
    for l in mesh4zzzz.loops:
        vert_loopszzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzz):
        for li in vert_loopszzzz[i]:
            uv_layerzzzz[li].uv = coord


    mesh4zzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzz.from_pydata(vertices2zzzzz, [], faces2zzzzz)
    objects4zzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzz)
    collection.objects.link(objects4zzzzz)

    uv_texzzzzz = mesh4zzzzz.uv_layers.new()
    uv_layerzzzzz = mesh4zzzzz.uv_layers[0].data
    vert_loopszzzzz = {}
    for l in mesh4zzzzz.loops:
        vert_loopszzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzz):
        for li in vert_loopszzzzz[i]:
            uv_layerzzzzz[li].uv = coord

    mesh4zzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzz.from_pydata(vertices2zzzzzz, [], faces2zzzzzz)
    objects4zzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzz)
    collection.objects.link(objects4zzzzzz)

    uv_texzzzzzz = mesh4zzzzzz.uv_layers.new()
    uv_layerzzzzzz = mesh4zzzzzz.uv_layers[0].data
    vert_loopszzzzzz = {}
    for l in mesh4zzzzzz.loops:
        vert_loopszzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzz):
        for li in vert_loopszzzzzz[i]:
            uv_layerzzzzzz[li].uv = coord

    mesh4zzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzz.from_pydata(vertices2zzzzzzz, [], faces2zzzzzzz)
    objects4zzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzz)
    collection.objects.link(objects4zzzzzzz)

    uv_texzzzzzzz = mesh4zzzzzzz.uv_layers.new()
    uv_layerzzzzzzz = mesh4zzzzzzz.uv_layers[0].data
    vert_loopszzzzzzz = {}
    for l in mesh4zzzzzzz.loops:
        vert_loopszzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzz):
        for li in vert_loopszzzzzzz[i]:
            uv_layerzzzzzzz[li].uv = coord

    mesh4zzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzz.from_pydata(vertices2zzzzzzzz, [], faces2zzzzzzzz)
    objects4zzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzz)
    collection.objects.link(objects4zzzzzzzz)

    uv_texzzzzzzzz = mesh4zzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzz = mesh4zzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzz = {}
    for l in mesh4zzzzzzzz.loops:
        vert_loopszzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzz):
        for li in vert_loopszzzzzzzz[i]:
            uv_layerzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzz.from_pydata(vertices2zzzzzzzzz, [], faces2zzzzzzzzz)
    objects4zzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzz)

    uv_texzzzzzzzzz = mesh4zzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzz = mesh4zzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzz = {}
    for l in mesh4zzzzzzzzz.loops:
        vert_loopszzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzz):
        for li in vert_loopszzzzzzzzz[i]:
            uv_layerzzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzzz.from_pydata(vertices2zzzzzzzzzz, [], faces2zzzzzzzzzz)
    objects4zzzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzzz)

    uv_texzzzzzzzzzz = mesh4zzzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzzz = mesh4zzzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzzz = {}
    for l in mesh4zzzzzzzzzz.loops:
        vert_loopszzzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzzz):
        for li in vert_loopszzzzzzzzzz[i]:
            uv_layerzzzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzzzz.from_pydata(vertices2zzzzzzzzzzz, [], faces2zzzzzzzzzzz)
    objects4zzzzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzzzz)

    uv_texzzzzzzzzzzz = mesh4zzzzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzzzz = mesh4zzzzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzzzz = {}
    for l in mesh4zzzzzzzzzzz.loops:
        vert_loopszzzzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzzzz):
        for li in vert_loopszzzzzzzzzzz[i]:
            uv_layerzzzzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzzzzz.from_pydata(vertices2zzzzzzzzzzzz, [], faces2zzzzzzzzzzzz)
    objects4zzzzzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzzzzz)

    uv_texzzzzzzzzzzzz = mesh4zzzzzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzzzzz = mesh4zzzzzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzzzzz = {}
    for l in mesh4zzzzzzzzzzzz.loops:
        vert_loopszzzzzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzzzzz):
        for li in vert_loopszzzzzzzzzzzz[i]:
            uv_layerzzzzzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzzzzzz.from_pydata(vertices2zzzzzzzzzzzzz, [], faces2zzzzzzzzzzzzz)
    objects4zzzzzzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzzzzzz)

    uv_texzzzzzzzzzzzzz = mesh4zzzzzzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzzzzzz = mesh4zzzzzzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzzzzzz = {}
    for l in mesh4zzzzzzzzzzzzz.loops:
        vert_loopszzzzzzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzzzzzz):
        for li in vert_loopszzzzzzzzzzzzz[i]:
            uv_layerzzzzzzzzzzzzz[li].uv = coord

    mesh4zzzzzzzzzzzzzz = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4zzzzzzzzzzzzzz.from_pydata(vertices2zzzzzzzzzzzzzz, [], faces2zzzzzzzzzzzzzz)
    objects4zzzzzzzzzzzzzz = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4zzzzzzzzzzzzzz)
    collection.objects.link(objects4zzzzzzzzzzzzzz)

    uv_texzzzzzzzzzzzzzz = mesh4zzzzzzzzzzzzzz.uv_layers.new()
    uv_layerzzzzzzzzzzzzzz = mesh4zzzzzzzzzzzzzz.uv_layers[0].data
    vert_loopszzzzzzzzzzzzzz = {}
    for l in mesh4zzzzzzzzzzzzzz.loops:
        vert_loopszzzzzzzzzzzzzz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2zzzzzzzzzzzzzz):
        for li in vert_loopszzzzzzzzzzzzzz[i]:
            uv_layerzzzzzzzzzzzzzz[li].uv = coord

    """texture TODO
    
    restore is down here"""

    for fac in mesh4l.polygons:
        fac.use_smooth = True

    for fac in mesh4k.polygons:
        fac.use_smooth = True

    for fac in mesh4j.polygons:
        fac.use_smooth = True
        
    for fac in mesh4i.polygons:
        fac.use_smooth = True

    for fac in mesh4h.polygons:
        fac.use_smooth = True

    for fac in mesh4g.polygons:
        fac.use_smooth = True
        
    for fac in mesh4f.polygons:
        fac.use_smooth = True

    for fac in mesh4e.polygons:
        fac.use_smooth = True

    for fac in mesh4d.polygons:
        fac.use_smooth = True

    for fac in mesh4c.polygons:
        fac.use_smooth = True

    for fac in mesh4b.polygons:
        fac.use_smooth = True

    for fac in mesh4a.polygons:
        fac.use_smooth = True

    for fac in mesh4.polygons:
        fac.use_smooth = True

    objects4.parent = arma
    armamodifier4 = objects4.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier4.object = arma

    vgroups4 = [objects4.vertex_groups.new(name = bone.name) for bone in arma.data.bones]


    obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    bpy.ops.object.shade_smooth()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()
    bpy.ops.view3d.copybuffer()

    for m_o in bpy.data.meshes:
        bpy.data.meshes.remove(m_o)
    for a_o in bpy.data.armatures:
        bpy.data.armatures.remove(a_o)
    for c_o in bpy.data.collections:
        bpy.data.collections.remove(c_o)
    bpy.ops.view3d.pastebuffer()
    
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.shade_smooth()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.mode_set(mode='OBJECT')

    obj_1_1_1_armature = bpy.data.objects["GHG Armature"]
    bpy.context.view_layer.objects.active = obj_1_1_1_armature

    bpy.ops.object.select_all(action='SELECT')
    
    bpy.ops.object.parent_set(type='ARMATURE')
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    obj_a2 = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj_a2
    bpy.ops.object.select_all(action='SELECT')

    #bpy.ops.object.select_all(action='SELECT')

    #if obj and obj.type == 'MESH':
    #mesh = obj.data

    #bpy.ops.object.mode_set(mode='EDIT')
    #bpy.ops.object.mode_set(mode='OBJECT')
    #bpy.ops.object.mode_set(mode='EDIT')
    #bpy.ops.mesh.select_mode(type="VERT")

    
                        

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
                fa1 = bm.verts.new([+vx1,+vz1,+vy1])
                                
                        
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    for fac in bm.faces:
        fac.normal_flip()

    for fac in mesh.polygons:
        fac.use_smooth = True
                

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
                bm.verts.new([+vx1,+vz1,+vy1])
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    for fac in mesh.polygons:
        fac.use_smooth = True

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
                bm.verts.new([+vx1,+vz1,+vy1])
                    
            
                
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    for fac in bm.faces:
        fac.normal_flip()

    for fac in mesh.polygons:
        fac.use_smooth = True

def select3rdUVnoloop(f, uvs=[]):

    f.seek(0)
    uvfirstread = f.read()
    uvfirstfind = uvfirstread.find(b"\x04\x02\x00\x01\x03\x80")
    if uvfirstread != 0:
        f.seek(uvfirstfind, 0)
        f.seek(6, 1)
        uvcount = unpack("B", f.read(1))[0] // 2
        flag1a = unpack("B", f.read(1))[0]
        if flag1a == 0x6C:
            
            for i in range(uvcount):
                f.seek(16,1)
                ux = unpack("<f", f.read(4))[0]
                uy = unpack("<f", f.read(4))[0]
                f.seek(8, 1)
                uvs.append([+ux,-uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

def select3rdUVloop(f, uvs=[]):

    f.seek(0)
    uvfirstread = f.read()
    f.seek(0)
    while f.tell() < len(uvfirstread):
        uvfirstfind = f.read(4)
        if uvfirstfind == b"\x04\x02\x00\x01":
            f.seek(2,1)
            uvcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6C:
                
                for i in range(uvcount):
                    f.seek(16,1)
                    ux = unpack("<f", f.read(4))[0]
                    uy = unpack("<f", f.read(4))[0]
                    f.seek(8, 1)
                    uvs.append([+ux,-uy])
    obdata = bpy.context.object.data
    uv_tex = obdata.uv_layers.new()
    uv_layer = obdata.uv_layers[0].data
    vert_loops = {}
    for l in obdata.loops:
        vert_loops.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs):
        for li in vert_loops[i]:
            uv_layer[li].uv = coord

def select2ndUVnoloop(f, uvs=[]):

    f.seek(0)
    uvfirstread = f.read()
    uvfirstfind = uvfirstread.find(b"\x03\x02\x00\x01\x03\x80")
    if uvfirstread != 0:
        f.seek(uvfirstfind, 0)
        f.seek(6, 1)
        uvcount = unpack("B", f.read(1))[0] // 2
        flag1a = unpack("B", f.read(1))[0]
        if flag1a == 0x6D:
            
            for i in range(uvcount):
                f.seek(8,1)
                ux = unpack("<h", f.read(2))[0]/4096
                uy = unpack("<h", f.read(2))[0]/4096
                f.seek(4, 1)
                uvs.append([+ux,-uy])
            obdata = bpy.context.object.data
            uv_tex = obdata.uv_layers.new()
            uv_layer = obdata.uv_layers[0].data
            vert_loops = {}
            for l in obdata.loops:
                vert_loops.setdefault(l.vertex_index, []).append(l.index)
            for i, coord in enumerate(uvs):
                for li in vert_loops[i]:
                    uv_layer[li].uv = coord

def select2ndUVloop(f, uvs=[]):

    f.seek(0)
    uvfirstread = f.read()
    f.seek(0)
    while f.tell() < len(uvfirstread):
        uvfirstfind = f.read(4)
        if uvfirstfind == b"\x03\x02\x00\x01":
            f.seek(2,1)
            uvcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                
                for i in range(uvcount):
                    f.seek(8,1)
                    ux = unpack("<h", f.read(2))[0]/4096
                    uy = unpack("<h", f.read(2))[0]/4096
                    f.seek(4, 1)
                    uvs.append([+ux,-uy])
    obdata = bpy.context.object.data
    uv_tex = obdata.uv_layers.new()
    uv_layer = obdata.uv_layers[0].data
    vert_loops = {}
    for l in obdata.loops:
        vert_loops.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs):
        for li in vert_loops[i]:
            uv_layer[li].uv = coord


    
def ghgmesh2nouvdatanonormalsnoweightsTri(f, filepath):
    verts=[]
    faces=[]
    f.seek(0)
    meshsecondread = f.read()
    f.seek(0)
    while f.tell() < len(meshsecondread):
        meshsecond = f.read(4)
        if meshsecond == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                if vertexcount == 3:
                    for i in range(vertexcount):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        f.seek(10,1)
                        verts.append([vx,vz,vy])
                    faces.append([0,1,2])

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new("3")
    mesh.from_pydata(verts, [], faces)
    objects = bpy.data.objects.new("3", mesh)
    collection.objects.link(objects)

def ghgmesh2nouvdatanonormalsnoweights4th(f, filepath):
    verts=[]
    faces=[]
    f.seek(0)
    meshsecondread = f.read()
    f.seek(0)

    fa=-4
    fb=-3
    fc=-2
    fd=-1
    
    while f.tell() < len(meshsecondread):
        meshsecond = f.read(4)
        if meshsecond == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                if vertexcount == 4:
                    for i in range(vertexcount):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        f.seek(10,1)
                        verts.append([vx,vz,vy])
                    f.seek(82,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag01 = unpack("B", f.read(1))[0]
                    id1 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6E:
                        if facecount == 2:
                            fa=unpack("B", f.read(1))[0]&0x0F
                            fb=unpack("B", f.read(1))[0]&0x0F
                            fc=unpack("B", f.read(1))[0]&0x0F
                            fd=unpack("B", f.read(1))[0]&0x0F

                            fa//=3
                            fb//=3
                            fc//=3
                            fd//=3

                            fa-=4
                            fb-=4
                            fc-=4
                            fd-=4

                            fa+=1*len(verts)
                            fb+=1*len(verts)
                            fc+=1*len(verts)
                            fd+=1*len(verts)

                            faces.append([fa,fb,fc])
                            faces.append([fb,fc,fd])

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new("4")
    mesh.from_pydata(verts, [], faces)
    objects = bpy.data.objects.new("4", mesh)
    collection.objects.link(objects)

def ghgmesh2nouvdatanonormalsnoweights5th(f, filepath):
    verts=[]
    faces=[]
    f.seek(0)
    meshsecondread = f.read()
    f.seek(0)

    fa=-5
    fb=-4
    fc=-3
    fd=-2
    fe=-1

    
    while f.tell() < len(meshsecondread):
        meshsecond = f.read(4)
        if meshsecond == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                if vertexcount == 5:
                    for i in range(vertexcount):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        f.seek(10,1)
                        verts.append([vx,vz,vy])
                    f.seek(86,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag01 = unpack("B", f.read(1))[0]
                    id1 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6E:
                        if facecount == 2:
                            fa=unpack("B", f.read(1))[0]&0x0F
                            fb=unpack("B", f.read(1))[0]&0x0F
                            fc=unpack("B", f.read(1))[0]&0x0F
                            fd=unpack("B", f.read(1))[0]&0x0F
                            fe=unpack("B", f.read(1))[0]&0x0F

                            fa//=3
                            fb//=3
                            fc//=3
                            fd//=3
                            fe//=3

                            fa-=5
                            fb-=5
                            fc-=5
                            fd-=5
                            fe-=5

                            fa+=1*len(verts)
                            fb+=1*len(verts)
                            fc+=1*len(verts)
                            fd+=1*len(verts)
                            fe+=1*len(verts)

                            faces.append([fa,fb,fc])
                            faces.append([fb,fc,fd])
                            faces.append([fc,fd,fe])

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new("5")
    mesh.from_pydata(verts, [], faces)
    objects = bpy.data.objects.new("5", mesh)
    collection.objects.link(objects)

def ghgmesh2nouvdatanonormalsnoweights6th(f, filepath):
    verts=[]
    faces=[]
    f.seek(0)
    meshsecondread = f.read()
    f.seek(0)

    fa=-6
    fb=-5
    fc=-4
    fd=-3
    fe=-2
    ff=-1

    
    while f.tell() < len(meshsecondread):
        meshsecond = f.read(4)
        if meshsecond == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                if vertexcount == 6:
                    for i in range(vertexcount):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        f.seek(10,1)
                        verts.append([vx,vz,vy])
                    f.seek(90,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag01 = unpack("B", f.read(1))[0]
                    id1 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6E:
                        if facecount == 2:
                            fa=unpack("B", f.read(1))[0]&0x0F
                            fb=unpack("B", f.read(1))[0]&0x0F
                            fc=unpack("B", f.read(1))[0]&0x0F
                            fd=unpack("B", f.read(1))[0]&0x0F
                            fe=unpack("B", f.read(1))[0]&0x0F
                            ff=unpack("B", f.read(1))[0]&0x0F

                            fa//=3
                            fb//=3
                            fc//=3
                            fd//=3
                            fe//=3
                            ff//=3

                            fa-=6
                            fb-=6
                            fc-=6
                            fd-=6
                            fe-=6
                            ff-=6

                            fa+=1*len(verts)
                            fb+=1*len(verts)
                            fc+=1*len(verts)
                            fd+=1*len(verts)
                            fe+=1*len(verts)
                            ff+=1*len(verts)

                            faces.append([fa,fb,fc])
                            faces.append([fb,fc,fd])
                            faces.append([fc,fd,fe])
                            faces.append([fd,fe,ff])

                            
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new("6")
    mesh.from_pydata(verts, [], faces)
    objects = bpy.data.objects.new("6", mesh)
    collection.objects.link(objects)

def ghgmesh2nouvdatanonormalsnoweights7th(f, filepath):
    verts=[]
    faces=[]
    f.seek(0)
    meshsecondread = f.read()
    f.seek(0)

    fa=-7
    fb=-6
    fc=-5
    fd=-4
    fe=-3
    ff=-2
    fg=-1

    
    while f.tell() < len(meshsecondread):
        meshsecond = f.read(4)
        if meshsecond == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0] // 2
            flag1a = unpack("B", f.read(1))[0]
            if flag1a == 0x6D:
                if vertexcount == 7:
                    for i in range(vertexcount):
                        vx = unpack("<h", f.read(2))[0]/4096
                        vy = unpack("<h", f.read(2))[0]/4096
                        vz = unpack("<h", f.read(2))[0]/4096
                        f.seek(10,1)
                        verts.append([vx,vz,vy])
                    f.seek(94,1)
                    facecount = unpack("B", f.read(1))[0]
                    flag01 = unpack("B", f.read(1))[0]
                    id1 = unpack("B", f.read(1))[0]
                    if flag01 == 0x6E:
                        if facecount == 2:
                            fa=unpack("B", f.read(1))[0]&0x1f
                            fb=unpack("B", f.read(1))[0]&0x1f
                            fc=unpack("B", f.read(1))[0]&0x1f
                            fd=unpack("B", f.read(1))[0]&0x1f
                            fe=unpack("B", f.read(1))[0]&0x1f
                            ff=unpack("B", f.read(1))[0]&0x1f
                            fg=unpack("B", f.read(1))[0]&0x1f

                            fa//=3
                            fb//=3
                            fc//=3
                            fd//=3
                            fe//=3
                            ff//=3
                            fg//=3

                            fa-=7
                            fb-=7
                            fc-=7
                            fd-=7
                            fe-=7
                            ff-=7
                            fg-=7

                            fa+=1*len(verts)
                            fb+=1*len(verts)
                            fc+=1*len(verts)
                            fd+=1*len(verts)
                            fe+=1*len(verts)
                            ff+=1*len(verts)
                            fg+=1*len(verts)

                            faces.append([fa,fb,fc])
                            faces.append([fb,fc,fd])
                            faces.append([fc,fd,fe])
                            faces.append([fd,fe,ff])
                            faces.append([fe,ff,fg])

                            
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new("7")
    mesh.from_pydata(verts, [], faces)
    objects = bpy.data.objects.new("7", mesh)
    collection.objects.link(objects)
                    
    
        

    
            

def ghg_open(filepath, offset_on_off=False, bsa_on_off=False, uv3rdnoloop=False, uv3rdloop=False,uv2ndnoloop=False, uv2ndloop=False, me2s3h=False, me2s4h=False, me2s5h=False, me2s6h=False, me2s7h=False):
    with open(filepath, "rb") as f:
        if offset_on_off:
            GHG_mesh(f, filepath)
            #GHG_mesha(f, filepath)

        if bsa_on_off:
            GHG_Blend_Object(f, filepath)

        if uv3rdnoloop:
            select3rdUVnoloop(f, uvs=[])

        if uv3rdloop:
            select3rdUVloop(f, uvs=[])

        if uv2ndnoloop:
            select2ndUVnoloop(f, uvs=[])

        if uv2ndloop:
            select2ndUVloop(f, uvs=[])

        if me2s3h:
            ghgmesh2nouvdatanonormalsnoweightsTri(f, filepath)

        if me2s4h:
            ghgmesh2nouvdatanonormalsnoweights4th(f, filepath)

        if me2s5h:
            ghgmesh2nouvdatanonormalsnoweights5th(f, filepath)

        if me2s6h:
            ghgmesh2nouvdatanonormalsnoweights6th(f, filepath)

        if me2s7h:
            ghgmesh2nouvdatanonormalsnoweights7th(f, filepath)
            
