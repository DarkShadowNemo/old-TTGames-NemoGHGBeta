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

    fau = -1
    fbu = 0
    fcu = 1

    #fad1 = -4
    #fbd1 = -3
    #fcd1 = -2
    #fad2 = -3
    #fbd2 = -2
    #fcd2 = -1

    fad = -1
    fbd = 0
    fcd = 1

    fad1abc = -1
    fbd1abc = 0
    fcd1abc = 1
    fdd1abc = 2

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

    #fad2=-3
    #fbd2=-2
    #fcd2=-1

    fad6=-1
    fbd6=0
    fcd6=1
    fdd7=2
    fed7=3
    ffd7=4



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

            if ObjectCount != 0:
                if UnkCount1 == 0 and UnkCount2 == 0:
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
                elif UnkCount1 != 0 and UnkCount2 != 0:
                    f.seek(UnkCountEntrySize2,0)
                    for i in range(UnkCount2):
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
                        objlen = unpack("<I", f.read(4))[0]
                        objid = unpack("<I", f.read(4))[0]
                        f.seek(8,1)
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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

            elif ObjectCount == 0:
                if UnkCount1 != 0 and UnkCount2 != 0:
                    f.seek(UnkCountEntrySize2,0)
                    for i in range(UnkCount2):
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
                        objlen = unpack("<I", f.read(4))[0]
                        objid = unpack("<I", f.read(4))[0]
                        f.seek(8,1)
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
                if UnkCount1 == 0 and UnkCount2 == 0:
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
        if TextureEntrySize1 == 144 or TextureEntrySize1 == 148:
            idxA_=0
            f.seek(TextureEntrySize1,0)
            for i in range(TextureCount):
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
                                cddddpad01 = unpack("B", f.read(1))[0]

                        

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

            if ObjectCount != 0:
                if UnkCount1 == 0 and UnkCount2 == 0:
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
                elif UnkCount1 != 0 and UnkCount2 != 0:
                    f.seek(UnkCountEntrySize2,0)
                    for i in range(UnkCount2):
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
                        objlen = unpack("<I", f.read(4))[0]
                        objid = unpack("<I", f.read(4))[0]
                        f.seek(8,1)
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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

            elif ObjectCount == 0:
                if UnkCount1 != 0 and UnkCount2 != 0:
                    f.seek(UnkCountEntrySize2,0)
                    for i in range(UnkCount2):
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
                        objlen = unpack("<I", f.read(4))[0]
                        objid = unpack("<I", f.read(4))[0]
                        f.seek(8,1)
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                elif vertexCount:
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
                if UnkCount1 == 0 and UnkCount2 == 0:
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
                                        vxaa = unpack("<h", f.read(2))[0] / 4096
                                        vyaa = unpack("<h", f.read(2))[0] / 4096
                                        vzaa = unpack("<h", f.read(2))[0] / 4096
                                        vwaa = unpack("<h", f.read(2))[0] / 4096
                                        uvxaa = unpack("<h", f.read(2))[0] / 4096
                                        uvyaa = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2a.append([vxaa,vzaa,vyaa])
                                    f.seek(82,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fbd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fcd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        fdd1abc = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]
                                        pad03 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 12 and pad02 == 15 and pad03 == 18:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])

                                        elif pad01 == 60 and pad02 == 57 and pad03 == 54:
                                            fad1abc//=3
                                            fbd1abc//=3
                                            fcd1abc//=3
                                            fdd1abc//=3

                                            fad1abc+=1*len(vertices2a)-4
                                            fbd1abc+=1*len(vertices2a)-4
                                            fcd1abc+=1*len(vertices2a)-4
                                            fdd1abc+=1*len(vertices2a)-4

                                            faces2a.append([fad1abc,fbd1abc,fcd1abc])
                                            faces2a.append([fbd1abc,fcd1abc,fdd1abc])
                                        

                                elif vertexCount == 5:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx3 = unpack("<h", f.read(2))[0] / 4096
                                        uvy3 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        vertices2b.append([vx,vz,vy])

                                    f.seek(86,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsB = unpack("B", f.read(1))[0]
                                    if flagsB == 0x6E:
                                        id1 = unpack("B", f.read(1))[0]
                                        fad5 = unpack("B", f.read(1))[0] & 0x0F
                                        fbd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fcd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fdd5 = unpack("B", f.read(1))[0] & 0x0F
                                        fed5 = unpack("B", f.read(1))[0] & 0x0F
                                        pad01 = unpack("B", f.read(1))[0]
                                        pad02 = unpack("B", f.read(1))[0]

                                        if pad01 == 100 and pad02 == 100:
                                            
                                        
                                            fad5//=3
                                            fbd5//=3
                                            fcd5//=3
                                            fdd5//=3
                                            fed5//=3
                                            
                                            fad5+=1*len(vertices2b)-5
                                            fbd5+=1*len(vertices2b)-5
                                            fcd5+=1*len(vertices2b)-5
                                            fdd5+=1*len(vertices2b)-5
                                            fed5+=1*len(vertices2b)-5
                                            
                                            faces2b.append([fad5,fbd5,fcd5])
                                            faces2b.append([fbd5,fcd5,fdd5])
                                            faces2b.append([fcd5,fdd5,fed5])

                                elif vertexCount == 6:
                                    for i in range(1):
                                        vx = unpack("<h", f.read(2))[0]/4096
                                        vy = unpack("<h", f.read(2))[0]/4096
                                        vz = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx1 = unpack("<h", f.read(2))[0]/4096
                                        vy1 = unpack("<h", f.read(2))[0]/4096
                                        vz1 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx2 = unpack("<h", f.read(2))[0]/4096
                                        vy2 = unpack("<h", f.read(2))[0]/4096
                                        vz2 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx3 = unpack("<h", f.read(2))[0]/4096
                                        vy3 = unpack("<h", f.read(2))[0]/4096
                                        vz3 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx4 = unpack("<h", f.read(2))[0]/4096
                                        vy4 = unpack("<h", f.read(2))[0]/4096
                                        vz4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)

                                        vx6 = unpack("<h", f.read(2))[0]/4096
                                        vy6 = unpack("<h", f.read(2))[0]/4096
                                        vz6 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(2,1)
                                        uvx4 = unpack("<h", f.read(2))[0]/4096
                                        uvy4 = unpack("<h", f.read(2))[0]/4096
                                        f.seek(4,1)
                                        vertices2c.append([vx,vz,vy])
                                        vertices2c.append([vx1,vz1,vy1])
                                        vertices2c.append([vx2,vz2,vy2])
                                        vertices2c.append([vx3,vz3,vy3])
                                        vertices2c.append([vx4,vz4,vy4])
                                        vertices2c.append([vx6,vz6,vy6])

                                    f.seek(90,1)
                                    facecount = unpack("B", f.read(1))[0]
                                    flagsC = unpack("B", f.read(1))[0]
                                    if flagsC == 0x6E:
                                        if facecount == 2:
                                            
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6 = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6 = unpack("B", f.read(1))[0] & 0x0F
                                            fed6 = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6 = unpack("B", f.read(1))[0] & 0x0F
                                            pad01 = unpack("B", f.read(1))[0]
                                            if pad01 == 100:
                                                
                                            
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                            elif pad01 == 15:
                                                fad6//=3
                                                fbd6//=3
                                                fcd6//=3
                                                fdd6//=3
                                                fed6//=3
                                                ffd6//=3
                                                
                                                fad6+=1*len(vertices2c)-6
                                                fbd6+=1*len(vertices2c)-6
                                                fcd6+=1*len(vertices2c)-6
                                                fdd6+=1*len(vertices2c)-6
                                                fed6+=1*len(vertices2c)-6
                                                ffd6+=1*len(vertices2c)-6

                                                if math.isclose(vy3,vy4) == True:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fbd6,fcd6,fdd6])
                                                    faces2c.append([fcd6,fdd6,fed6])
                                                    faces2c.append([fdd6,fed6,ffd6])
                                                else:
                                                    faces2c.append([fad6,fbd6,fcd6])
                                                    faces2c.append([fdd6,fed6,ffd6])

                                        elif facecount == 3:
                                            id1 = unpack("B", f.read(1))[0]
                                            fad6a = unpack("B", f.read(1))[0] & 0x0F
                                            fbd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fcd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fdd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fed6a = unpack("B", f.read(1))[0] & 0x0F
                                            ffd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fgd6a = unpack("B", f.read(1))[0] & 0x0F
                                            fhd6a = unpack("B", f.read(1))[0] & 0x0F

                                            pad01 = unpack("B", f.read(1))[0]
                                            pad02 = unpack("B", f.read(1))[0]
                                            pad03 = unpack("B", f.read(1))[0]

                                            if pad01 == 100 and pad02 == 100 and pad03 == 100:
                                                fad6a//=3
                                                fbd6a//=3
                                                fcd6a//=3
                                                fdd6a//=3
                                                fed6a//=3
                                                ffd6a//=3
                                                fgd6a//=3
                                                fhd6a//=3
                                                
                                                fad6a+=1*len(vertices2c)-6
                                                fbd6a+=1*len(vertices2c)-6
                                                fcd6a+=1*len(vertices2c)-6
                                                fdd6a+=1*len(vertices2c)-6
                                                fed6a+=1*len(vertices2c)-6
                                                ffd6a+=1*len(vertices2c)-6
                                                fgd6a+=1*len(vertices2c)-6
                                                fhd6a+=1*len(vertices2c)-6

                                                faces2c.append([fad6a,fbd6a,fcd6a])
                                                faces2c.append([fbd6a,fcd6a,fdd6a])
                                                faces2c.append([fcd6a,fdd6a,fed6a])
                                                faces2c.append([fdd6a,fed6a,ffd6a])
                                                faces2c.append([fed6a,ffd6a,fgd6a])
                                                faces2c.append([ffd6a,fgd6a,fhd6a])

                                elif vertexCount == 7:
                                    for i in range(vertexCount):
                                        vx = unpack("<h", f.read(2))[0] / 4096
                                        vy = unpack("<h", f.read(2))[0] / 4096
                                        vz = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(2,1)
                                        uvx5 = unpack("<h", f.read(2))[0] / 4096
                                        uvy5 = unpack("<h", f.read(2))[0] / 4096
                                        f.seek(4,1)
                                        
                                        vertices2d.append([vx,vz,vy])
                                    
                                    
                                    
                                    
                                    
                                                
                                    
                                
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
                                    for j in range(1):
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
                                    offsettA = unpack("<I", f.read(4))[0]
                                    if offsettA == 1627553807:
                                        offsetB = unpack("<I", f.read(4))[0]
                                        if offsetB == 65538:
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
                                                            if type4G == 0:
                                                                if type4H == 1:
                                                                    if type4I == 0:
                                                                        pass
                                    if offsettA == 16777473:
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
    for l in mesh4a.loops:
        vert_loopsa.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2a):
        for li in vert_loopsa[i]:
            uv_layera[li].uv = coord

    mesh4b = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4b.from_pydata(vertices2b, [], faces2b)
    objects4b = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4b)
    collection.objects.link(objects4b)

    uv_texb = mesh4b.uv_layers.new()
    uv_layerb = mesh4b.uv_layers[0].data
    vert_loopsb = {}
    for l in mesh4b.loops:
        vert_loopsb.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2b):
        for li in vert_loopsb[i]:
            uv_layerb[li].uv = coord

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
                ux = unpack("<h", f.read(2))[0]
                uy = unpack("<h", f.read(2))[0]
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
                    ux = unpack("<h", f.read(2))[0]
                    uy = unpack("<h", f.read(2))[0]
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
    

    
        

    
            

def ghg_open(filepath, offset_on_off=False, bsa_on_off=False, uv3rdnoloop=False, uv3rdloop=False,uv2ndnoloop=False, uv2ndloop=False):
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
