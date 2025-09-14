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

def GHG_Texture_Utility_0x81_only(f, filepath, seek_=0):
    #32x32 width and height
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A
                
                
            
    for i in range(compression_width):
        for k in range(compression_height):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            a = unpack("B", f.read(1))[0]/127
            drawPixel(i,k,r,g,b,a)

def GHG_Texture_Utility_0x83_only(f, filepath, seek_=0):
    #64x64 width and height without alpha
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3]
                
                
            
    for i in range(compression_width):
        for k in range(compression_height):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            drawPixel(i,k,r,g,b)

def GHG_Texture_Utility_0x84_only(f, filepath, seek_=0):
    #64x64 width and height
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A
                
                
            
    for i in range(compression_width):
        for k in range(compression_height):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            a = unpack("B", f.read(1))[0]/127
            drawPixel(i,k,r,g,b,a)

def GHG_Texture_Utility_0x90_only(f, filepath, seek_=0):
    #256x64 width floor division by 4 and height multiply by 4
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]//4
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]*4
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A
                
                
            
    for i in range(compression_width//4):
        for k in range(compression_height*4):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            a = unpack("B", f.read(1))[0]/127
            drawPixel(i,k,r,g,b,a)

def GHG_Texture_Utility_0xA0_only(f, filepath, seek_=0):
    #256 divide 2 and 128 multiply
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]//2
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]*2
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A
                
                
            
    for i in range(compression_width//2):
        for k in range(compression_height*2):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            a = unpack("B", f.read(1))[0]/127
            drawPixel(i,k,r,g,b,a)

def GHG_Texture_Utility_0xC0_only(f, filepath, seek_=0):
    #found on the xbox
    #256x256 width and height only
    f.seek(seek_,1)
    w = unpack("<H", f.read(2))[0]
    f.seek(2,1)
    h = unpack("<H", f.read(2))[0]
    f.seek(26,1)
    size = unpack("<I", f.read(4))[0]
    f.seek(size,1)
    f.seek(48,1)
    compression_width = unpack("<I", f.read(4))[0]
    compression_height = unpack("<I", f.read(4))[0]
    f.seek(24,1)
    pallete_offsetss = unpack("<H", f.read(2))[0]
    f.seek(14,1)
    image_test = bpy.data.images.new(name="GHG Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
            


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A
                
                
            
    for i in range(compression_width):
        for k in range(compression_height):
            r = unpack("B", f.read(1))[0]/255
            g = unpack("B", f.read(1))[0]/255
            b = unpack("B", f.read(1))[0]/255
            a = unpack("B", f.read(1))[0]/127
            drawPixel(i,k,r,g,b,a)

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
    f.seek(0)

    fad7_=-1
    fbd7_=0
    fcd7_=1
    fdd7_=2
    fed7_=3
    ffd7_=4
    fgd7_=4

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

    fa2 = -1
    fb2 = 0
    fc2 = 1


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

    #blend_vertices=[]

    #blend shape offset 0x13380001

    blendshapeinfos = {} # you don't have to use dictionarys if you want to it does work with lists
    skininfos = {}

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
    if TextureCount != 0:
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
                if type3 == 0:
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
                        image_test = bpy.data.images.new(name="GHG Image", width=width1, height=height1, alpha=True)
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

                                texttures.append([r,g,b,a])

                                if idxA_== 0:
                                    drawPixel(y,x,r1,g1,b1,a1)

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
                            if idxOffset == 0x8400:
                                idxA_+=1
                                for xi in range(comprWa):
                                    for yi in range(comprHa):
                                        iidx = unpack("B", f.read(1))[0]
                                        iidx2 = iidx
                                        if idxA_ == 1:
                                            if iidx == 1:
                                                iidx2+=254
                                            drawPixel(yi,xi,iidx2/255,iidx2/255,iidx2/255,1)
                                            
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

                            if idxOffset == 0x8400:
                                idxA_+=1
                    elif palleteOffset == 0x8008:
                        pass
                elif type3 != 0:
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
                    pass

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
                            for i in range(1):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                
                                vx1 = unpack("<h", f.read(2))[0] / 4096
                                vy1 = unpack("<h", f.read(2))[0] / 4096
                                vz1 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)

                                vx2 = unpack("<h", f.read(2))[0] / 4096
                                vy2 = unpack("<h", f.read(2))[0] / 4096
                                vz2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)

                                vx3 = unpack("<h", f.read(2))[0] / 4096
                                vy3 = unpack("<h", f.read(2))[0] / 4096
                                vz3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)

                                vx4 = unpack("<h", f.read(2))[0] / 4096
                                vy4 = unpack("<h", f.read(2))[0] / 4096
                                vz4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)

                                vx5 = unpack("<h", f.read(2))[0] / 4096
                                vy5 = unpack("<h", f.read(2))[0] / 4096
                                vz5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)

                                vx6 = unpack("<h", f.read(2))[0] / 4096
                                vy6 = unpack("<h", f.read(2))[0] / 4096
                                vz6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx5 = unpack("<h", f.read(2))[0] / 4096
                                uvy5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                
                                vertices2d.append([vx,vz,vy])
                                vertices2d.append([vx1,vz1,vy1])
                                vertices2d.append([vx2,vz2,vy2])
                                vertices2d.append([vx3,vz3,vy3])
                                vertices2d.append([vx4,vz4,vy4])
                                vertices2d.append([vx5,vz5,vy5])
                                vertices2d.append([vx6,vz6,vy6])
                            f.seek(94,1)
                            facecount1 = unpack("B", f.read(1))[0]
                            flagsD = unpack("B", f.read(1))[0]
                            if flagsD == 0x6E:
                                if facecount1 == 3:
                                    id1 = unpack("B", f.read(1))[0]
                                    fad7 = unpack("B", f.read(1))[0]
                                    fbd7 = unpack("B", f.read(1))[0]
                                    fcd7 = unpack("B", f.read(1))[0]
                                    fdd7 = unpack("B", f.read(1))[0]
                                    fed7 = unpack("B", f.read(1))[0]
                                    ffd7 = unpack("B", f.read(1))[0]
                                    fgd7 = unpack("B", f.read(1))[0]
                                    if id1 == 21 and fad7 == 146 and fbd7 == 128 and fcd7 == 3 and fdd7 == 6 and fed7 == 137 and ffd7 == 140 and fgd7 == 15:
                                        f.seek(-8,1)
                                        id1 = unpack("B", f.read(1))[0]
                                        fad7_ = unpack("B", f.read(1))[0] & 0x10
                                        fbd7_ = unpack("B", f.read(1))[0] & 0x0F
                                        fcd7_ = unpack("B", f.read(1))[0] & 0x0F
                                        fdd7_ = unpack("B", f.read(1))[0] & 0x0F
                                        fed7_ = unpack("B", f.read(1))[0] & 0x0F
                                        ffd7_ = unpack("B", f.read(1))[0] & 0x0F
                                        fgd7_ = unpack("B", f.read(1))[0] & 0x0F

                                        fad7_//=3+1
                                        fbd7_//=3
                                        fcd7_//=3
                                        fdd7_//=3
                                        fed7_//=3
                                        ffd7_//=3
                                        fgd7_//=3

                                        fad7_+=1*len(vertices2d)-7
                                        fbd7_+=1*len(vertices2d)-7
                                        fcd7_+=1*len(vertices2d)-7
                                        fdd7_+=1*len(vertices2d)-7
                                        fed7_+=1*len(vertices2d)-7
                                        ffd7_+=1*len(vertices2d)-7
                                        fgd7_+=1*len(vertices2d)-7

                                        faces2d.append([fad7_,fbd7_,fcd7_])
                                        faces2d.append([fdd7_,fed7_,ffd7_])
                        

                        """elif vertexCount == 8:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx6 = unpack("<h", f.read(2))[0] / 4096
                                uvy6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2e.append([vx,vz,vy])
                                uvs2e.append([uvx6,-uvy6])
                            for i in range(vertexCount-7):
                                fad15+=1*8
                                fbd15+=1*8
                                fcd15+=1*8
                                fad16+=1*8
                                fbd16+=1*8
                                fcd16+=1*8
                                fad17+=1*8
                                fbd17+=1*8
                                fcd17+=1*8
                                fad18+=1*8
                                fbd18+=1*8
                                fcd18+=1*8
                                fad19+=1*8
                                fbd19+=1*8
                                fcd19+=1*8
                                fad20+=1*8
                                fbd20+=1*8
                                fcd20+=1*8
                                faces2e.append([fad15,fbd15,fcd15])
                                faces2e.append([fad16,fbd16,fcd16])
                                faces2e.append([fad17,fbd17,fcd17])
                                faces2e.append([fad18,fbd18,fcd18])
                                faces2e.append([fad19,fbd19,fcd19])
                                faces2e.append([fad20,fbd20,fcd20])

                        elif vertexCount == 9:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx7 = unpack("<h", f.read(2))[0] / 4096
                                uvy7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2f.append([vx,vz,vy])
                                uvs2f.append([uvx7,-uvy7])
                            for i in range(vertexCount-8):
                                fad21+=1*9
                                fbd21+=1*9
                                fcd21+=1*9
                                fad22+=1*9
                                fbd22+=1*9
                                fcd22+=1*9
                                fad23+=1*9
                                fbd23+=1*9
                                fcd23+=1*9
                                fad24+=1*9
                                fbd24+=1*9
                                fcd24+=1*9
                                fad25+=1*9
                                fbd25+=1*9
                                fcd25+=1*9
                                fad26+=1*9
                                fbd26+=1*9
                                fcd26+=1*9
                                fad27+=1*9
                                fbd27+=1*9
                                fcd27+=1*9
                                faces2f.append([fad21,fbd21,fcd21])
                                faces2f.append([fad22,fbd22,fcd22])
                                faces2f.append([fad23,fbd23,fcd23])
                                faces2f.append([fad24,fbd24,fcd24])
                                faces2f.append([fad25,fbd25,fcd25])
                                faces2f.append([fad26,fbd26,fcd26])
                                faces2f.append([fad27,fbd27,fcd27])

                        elif vertexCount == 10:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx8 = unpack("<h", f.read(2))[0] / 4096
                                uvy8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2g.append([vx,vz,vy])
                                uvs2g.append([uvx8,-uvy8])
                            for i in range(vertexCount-9):
                                fad28+=1*10
                                fbd28+=1*10
                                fcd28+=1*10
                                fad29+=1*10
                                fbd29+=1*10
                                fcd29+=1*10
                                fad30+=1*10
                                fbd30+=1*10
                                fcd30+=1*10
                                fad31+=1*10
                                fbd31+=1*10
                                fcd31+=1*10
                                fad32+=1*10
                                fbd32+=1*10
                                fcd32+=1*10
                                fad33+=1*10
                                fbd33+=1*10
                                fcd33+=1*10
                                fad34+=1*10
                                fbd34+=1*10
                                fcd34+=1*10
                                fad35+=1*10
                                fbd35+=1*10
                                fcd35+=1*10
                                faces2g.append([fad28,fbd28,fcd28])
                                faces2g.append([fad29,fbd29,fcd29])
                                faces2g.append([fad30,fbd30,fcd30])
                                faces2g.append([fad31,fbd31,fcd31])
                                faces2g.append([fad32,fbd32,fcd32])
                                faces2g.append([fad33,fbd33,fcd33])
                                faces2g.append([fad34,fbd34,fcd34])
                                faces2g.append([fad35,fbd35,fcd35])

                        elif vertexCount == 11:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx9 = unpack("<h", f.read(2))[0] / 4096
                                uvy9 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2h.append([vx,vz,vy])
                                uvs2h.append([uvx9,-uvy9])
                            for i in range(vertexCount-10):
                                fad36+=1*11
                                fbd36+=1*11
                                fcd36+=1*11
                                fad37+=1*11
                                fbd37+=1*11
                                fcd37+=1*11
                                fad38+=1*11
                                fbd38+=1*11
                                fcd38+=1*11
                                fad39+=1*11
                                fbd39+=1*11
                                fcd39+=1*11
                                fad40+=1*11
                                fbd40+=1*11
                                fcd40+=1*11
                                fad41+=1*11
                                fbd41+=1*11
                                fcd41+=1*11
                                fad42+=1*11
                                fbd42+=1*11
                                fcd42+=1*11
                                fad43+=1*11
                                fbd43+=1*11
                                fcd43+=1*11
                                fad44+=1*11
                                fbd44+=1*11
                                fcd44+=1*11
                                faces2h.append([fad36,fbd36,fcd36])
                                faces2h.append([fad37,fbd37,fcd37])
                                faces2h.append([fad38,fbd38,fcd38])
                                faces2h.append([fad39,fbd39,fcd39])
                                faces2h.append([fad40,fbd40,fcd40])
                                faces2h.append([fad41,fbd41,fcd41])
                                faces2h.append([fad42,fbd42,fcd42])
                                faces2h.append([fad43,fbd43,fcd43])
                                faces2h.append([fad44,fbd44,fcd44])

                        elif vertexCount == 12:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx10 = unpack("<h", f.read(2))[0] / 4096
                                uvy10 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2i.append([vx,vz,vy])
                                uvs2i.append([uvx10,-uvy10])
                            for i in range(vertexCount-11):
                                fad45+=1*12
                                fbd45+=1*12
                                fcd45+=1*12
                                fad46+=1*12
                                fbd46+=1*12
                                fcd46+=1*12
                                fad47+=1*12
                                fbd47+=1*12
                                fcd47+=1*12
                                fad48+=1*12
                                fbd48+=1*12
                                fcd48+=1*12
                                fad49+=1*12
                                fbd49+=1*12
                                fcd49+=1*12
                                fad50+=1*12
                                fbd50+=1*12
                                fcd50+=1*12
                                fad51+=1*12
                                fbd51+=1*12
                                fcd51+=1*12
                                fad52+=1*12
                                fbd52+=1*12
                                fcd52+=1*12
                                fad53+=1*12
                                fbd53+=1*12
                                fcd53+=1*12
                                fad54+=1*12
                                fbd54+=1*12
                                fcd54+=1*12
                                faces2i.append([fad45,fbd45,fcd45])
                                faces2i.append([fad46,fbd46,fcd46])
                                faces2i.append([fad47,fbd47,fcd47])
                                faces2i.append([fad48,fbd48,fcd48])
                                faces2i.append([fad49,fbd49,fcd49])
                                faces2i.append([fad50,fbd50,fcd50])
                                faces2i.append([fad51,fbd51,fcd51])
                                faces2i.append([fad52,fbd52,fcd52])
                                faces2i.append([fad53,fbd53,fcd53])
                                faces2i.append([fad54,fbd54,fcd54])

                        elif vertexCount == 13:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx11 = unpack("<h", f.read(2))[0] / 4096
                                uvy11 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2j.append([vx,vz,vy])
                                uvs2j.append([uvx11,-uvy11])
                            for i in range(vertexCount-12):
                                fad55+=1*13
                                fbd55+=1*13
                                fcd55+=1*13
                                fad56+=1*13
                                fbd56+=1*13
                                fcd56+=1*13
                                fad57+=1*13
                                fbd57+=1*13
                                fcd57+=1*13
                                fad58+=1*13
                                fbd58+=1*13
                                fcd58+=1*13
                                fad59+=1*13
                                fbd59+=1*13
                                fcd59+=1*13
                                fad60+=1*13
                                fbd60+=1*13
                                fcd60+=1*13
                                fad61+=1*13
                                fbd61+=1*13
                                fcd61+=1*13
                                fad62+=1*13
                                fbd62+=1*13
                                fcd62+=1*13
                                fad63+=1*13
                                fbd63+=1*13
                                fcd63+=1*13
                                fad64+=1*13
                                fbd64+=1*13
                                fcd64+=1*13
                                fad65+=1*13
                                fbd65+=1*13
                                fcd65+=1*13
                                faces2j.append([fad55,fbd55,fcd55])
                                faces2j.append([fad56,fbd56,fcd56])
                                faces2j.append([fad57,fbd57,fcd57])
                                faces2j.append([fad58,fbd58,fcd58])
                                faces2j.append([fad59,fbd59,fcd59])
                                faces2j.append([fad60,fbd60,fcd60])
                                faces2j.append([fad61,fbd61,fcd61])
                                faces2j.append([fad62,fbd62,fcd62])
                                faces2j.append([fad63,fbd63,fcd63])
                                faces2j.append([fad64,fbd64,fcd64])
                                faces2j.append([fad65,fbd65,fcd65])

                        elif vertexCount == 14:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx12 = unpack("<h", f.read(2))[0] / 4096
                                uvy12 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2k.append([vx,vz,vy])
                                uvs2k.append([uvx12,-uvy12])
                            for i in range(vertexCount-13):
                                fad66+=1*14
                                fbd66+=1*14
                                fcd66+=1*14
                                fad67+=1*14
                                fbd67+=1*14
                                fcd67+=1*14
                                fad68+=1*14
                                fbd68+=1*14
                                fcd68+=1*14
                                fad69+=1*14
                                fbd69+=1*14
                                fcd69+=1*14
                                fad70+=1*14
                                fbd70+=1*14
                                fcd70+=1*14
                                fad71+=1*14
                                fbd71+=1*14
                                fcd71+=1*14
                                fad72+=1*14
                                fbd72+=1*14
                                fcd72+=1*14
                                fad73+=1*14
                                fbd73+=1*14
                                fcd73+=1*14
                                fad74+=1*14
                                fbd74+=1*14
                                fcd74+=1*14
                                fad75+=1*14
                                fbd75+=1*14
                                fcd75+=1*14
                                fad76+=1*14
                                fbd76+=1*14
                                fcd76+=1*14
                                fad77+=1*14
                                fbd77+=1*14
                                fcd77+=1*14
                                faces2k.append([fad66,fbd66,fcd66])
                                faces2k.append([fad67,fbd67,fcd67])
                                faces2k.append([fad68,fbd68,fcd68])
                                faces2k.append([fad69,fbd69,fcd69])
                                faces2k.append([fad70,fbd70,fcd70])
                                faces2k.append([fad71,fbd71,fcd71])
                                faces2k.append([fad72,fbd72,fcd72])
                                faces2k.append([fad73,fbd73,fcd73])
                                faces2k.append([fad74,fbd74,fcd74])
                                faces2k.append([fad75,fbd75,fcd75])
                                faces2k.append([fad76,fbd76,fcd76])
                                faces2k.append([fad77,fbd77,fcd77])

                        elif vertexCount == 15:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx13 = unpack("<h", f.read(2))[0] / 4096
                                uvy13 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2l.append([vx,vz,vy])
                                uvs2l.append([uvx13,-uvy13])
                            for i in range(vertexCount-14):
                                fad78+=1*15
                                fbd78+=1*15
                                fcd78+=1*15
                                fad79+=1*15
                                fbd79+=1*15
                                fcd79+=1*15
                                fad80+=1*15
                                fbd80+=1*15
                                fcd80+=1*15
                                fad81+=1*15
                                fbd81+=1*15
                                fcd81+=1*15
                                fad82+=1*15
                                fbd82+=1*15
                                fcd82+=1*15
                                fad83+=1*15
                                fbd83+=1*15
                                fcd83+=1*15
                                fad84+=1*15
                                fbd84+=1*15
                                fcd84+=1*15
                                fad85+=1*15
                                fbd85+=1*15
                                fcd85+=1*15
                                fad86+=1*15
                                fbd86+=1*15
                                fcd86+=1*15
                                fad87+=1*15
                                fbd87+=1*15
                                fcd87+=1*15
                                fad88+=1*15
                                fbd88+=1*15
                                fcd88+=1*15
                                fad89+=1*15
                                fbd89+=1*15
                                fcd89+=1*15
                                fad90+=1*15
                                fbd90+=1*15
                                fcd90+=1*15
                                faces2l.append([fad78,fbd78,fcd78])
                                faces2l.append([fad79,fbd79,fcd79])
                                faces2l.append([fad80,fbd80,fcd80])
                                faces2l.append([fad81,fbd81,fcd81])
                                faces2l.append([fad82,fbd82,fcd82])
                                faces2l.append([fad83,fbd83,fcd83])
                                faces2l.append([fad84,fbd84,fcd84])
                                faces2l.append([fad85,fbd85,fcd85])
                                faces2l.append([fad86,fbd86,fcd86])
                                faces2l.append([fad87,fbd87,fcd87])
                                faces2l.append([fad88,fbd88,fcd88])
                                faces2l.append([fad89,fbd89,fcd89])
                                faces2l.append([fad90,fbd90,fcd90])

                        elif vertexCount == 16:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx14 = unpack("<h", f.read(2))[0] / 4096
                                uvy14 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2m.append([vx,vz,vy])
                                uvs2m.append([uvx14,-uvy14])
                            for i in range(vertexCount-15):
                                fad91+=1*16
                                fbd91+=1*16
                                fcd91+=1*16
                                fad92+=1*16
                                fbd92+=1*16
                                fcd92+=1*16
                                fad93+=1*16
                                fbd93+=1*16
                                fcd93+=1*16
                                fad94+=1*16
                                fbd94+=1*16
                                fcd94+=1*16
                                fad95+=1*16
                                fbd95+=1*16
                                fcd95+=1*16
                                fad96+=1*16
                                fbd96+=1*16
                                fcd96+=1*16
                                fad97+=1*16
                                fbd97+=1*16
                                fcd97+=1*16
                                fad98+=1*16
                                fbd98+=1*16
                                fcd98+=1*16
                                fad99+=1*16
                                fbd99+=1*16
                                fcd99+=1*16
                                fad100+=1*16
                                fbd100+=1*16
                                fcd100+=1*16
                                fad101+=1*16
                                fbd101+=1*16
                                fcd101+=1*16
                                fad102+=1*16
                                fbd102+=1*16
                                fcd102+=1*16
                                fad103+=1*16
                                fbd103+=1*16
                                fcd103+=1*16
                                fad104+=1*16
                                fbd104+=1*16
                                fcd104+=1*16
                                faces2m.append([fad91,fbd91,fcd91])
                                faces2m.append([fad92,fbd92,fcd92])
                                faces2m.append([fad93,fbd93,fcd93])
                                faces2m.append([fad94,fbd94,fcd94])
                                faces2m.append([fad95,fbd95,fcd95])
                                faces2m.append([fad96,fbd96,fcd96])
                                faces2m.append([fad97,fbd97,fcd97])
                                faces2m.append([fad98,fbd98,fcd98])
                                faces2m.append([fad99,fbd99,fcd99])
                                faces2m.append([fad100,fbd100,fcd100])
                                faces2m.append([fad101,fbd101,fcd101])
                                faces2m.append([fad102,fbd102,fcd102])
                                faces2m.append([fad103,fbd103,fcd103])
                                faces2m.append([fad104,fbd104,fcd104])

                        elif vertexCount == 17:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx15 = unpack("<h", f.read(2))[0] / 4096
                                uvy15 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2n.append([vx,vz,vy])
                                uvs2n.append([uvx15,-uvy15])
                            for i in range(vertexCount-16):
                                fad105+=1*17
                                fbd105+=1*17
                                fcd105+=1*17
                                fad106+=1*17
                                fbd106+=1*17
                                fcd106+=1*17
                                fad107+=1*17
                                fbd107+=1*17
                                fcd107+=1*17
                                fad108+=1*17
                                fbd108+=1*17
                                fcd108+=1*17
                                fad109+=1*17
                                fbd109+=1*17
                                fcd109+=1*17
                                fad110+=1*17
                                fbd110+=1*17
                                fcd110+=1*17
                                fad111+=1*17
                                fbd111+=1*17
                                fcd111+=1*17
                                fad112+=1*17
                                fbd112+=1*17
                                fcd112+=1*17
                                fad113+=1*17
                                fbd113+=1*17
                                fcd113+=1*17
                                fad114+=1*17
                                fbd114+=1*17
                                fcd114+=1*17
                                fad115+=1*17
                                fbd115+=1*17
                                fcd115+=1*17
                                fad116+=1*17
                                fbd116+=1*17
                                fcd116+=1*17
                                fad117+=1*17
                                fbd117+=1*17
                                fcd117+=1*17
                                fad118+=1*17
                                fbd118+=1*17
                                fcd118+=1*17
                                fad119+=1*17
                                fbd119+=1*17
                                fcd119+=1*17
                                faces2n.append([fad105,fbd105,fcd105])
                                faces2n.append([fad106,fbd106,fcd106])
                                faces2n.append([fad107,fbd107,fcd107])
                                faces2n.append([fad108,fbd108,fcd108])
                                faces2n.append([fad109,fbd109,fcd109])
                                faces2n.append([fad110,fbd110,fcd110])
                                faces2n.append([fad111,fbd111,fcd111])
                                faces2n.append([fad112,fbd112,fcd112])
                                faces2n.append([fad113,fbd113,fcd113])
                                faces2n.append([fad114,fbd114,fcd114])
                                faces2n.append([fad115,fbd115,fcd115])
                                faces2n.append([fad116,fbd116,fcd116])
                                faces2n.append([fad117,fbd117,fcd117])
                                faces2n.append([fad118,fbd118,fcd118])
                                faces2n.append([fad119,fbd119,fcd119])

                        elif vertexCount == 18:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx16 = unpack("<h", f.read(2))[0] / 4096
                                uvy16 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2o.append([vx,vz,vy])
                                uvs2o.append([uvx16,-uvy16])
                            for i in range(vertexCount-17):
                                fad120+=1*18
                                fbd120+=1*18
                                fcd120+=1*18
                                fad121+=1*18
                                fbd121+=1*18
                                fcd121+=1*18
                                fad122+=1*18
                                fbd122+=1*18
                                fcd122+=1*18
                                fad123+=1*18
                                fbd123+=1*18
                                fcd123+=1*18
                                fad124+=1*18
                                fbd124+=1*18
                                fcd124+=1*18
                                fad125+=1*18
                                fbd125+=1*18
                                fcd125+=1*18
                                fad126+=1*18
                                fbd126+=1*18
                                fcd126+=1*18
                                fad127+=1*18
                                fbd127+=1*18
                                fcd127+=1*18
                                fad128+=1*18
                                fbd128+=1*18
                                fcd128+=1*18
                                fad129+=1*18
                                fbd129+=1*18
                                fcd129+=1*18
                                fad130+=1*18
                                fbd130+=1*18
                                fcd130+=1*18
                                fad131+=1*18
                                fbd131+=1*18
                                fcd131+=1*18
                                fad132+=1*18
                                fbd132+=1*18
                                fcd132+=1*18
                                fad133+=1*18
                                fbd133+=1*18
                                fcd133+=1*18
                                fad134+=1*18
                                fbd134+=1*18
                                fcd134+=1*18
                                fad135+=1*18
                                fbd135+=1*18
                                fcd135+=1*18
                                faces2o.append([fad120,fbd120,fcd120])
                                faces2o.append([fad121,fbd121,fcd121])
                                faces2o.append([fad122,fbd122,fcd122])
                                faces2o.append([fad123,fbd123,fcd123])
                                faces2o.append([fad124,fbd124,fcd124])
                                faces2o.append([fad125,fbd125,fcd125])
                                faces2o.append([fad126,fbd126,fcd126])
                                faces2o.append([fad127,fbd127,fcd127])
                                faces2o.append([fad128,fbd128,fcd128])
                                faces2o.append([fad129,fbd129,fcd129])
                                faces2o.append([fad130,fbd130,fcd130])
                                faces2o.append([fad131,fbd131,fcd131])
                                faces2o.append([fad132,fbd132,fcd132])
                                faces2o.append([fad133,fbd133,fcd133])
                                faces2o.append([fad134,fbd134,fcd134])
                                faces2o.append([fad135,fbd135,fcd135])

                        elif vertexCount == 19:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx17 = unpack("<h", f.read(2))[0] / 4096
                                uvy17 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2p.append([vx,vz,vy])
                                uvs2p.append([uvx17,-uvy17])
                            for i in range(vertexCount-18):
                                fad136+=1*19
                                fbd136+=1*19
                                fcd136+=1*19
                                fad137+=1*19
                                fbd137+=1*19
                                fcd137+=1*19
                                fad138+=1*19
                                fbd138+=1*19
                                fcd138+=1*19
                                fad139+=1*19
                                fbd139+=1*19
                                fcd139+=1*19
                                fad140+=1*19
                                fbd140+=1*19
                                fcd140+=1*19
                                fad141+=1*19
                                fbd141+=1*19
                                fcd141+=1*19
                                fad142+=1*19
                                fbd142+=1*19
                                fcd142+=1*19
                                fad143+=1*19
                                fbd143+=1*19
                                fcd143+=1*19
                                fad144+=1*19
                                fbd144+=1*19
                                fcd144+=1*19
                                fad145+=1*19
                                fbd145+=1*19
                                fcd145+=1*19
                                fad146+=1*19
                                fbd146+=1*19
                                fcd146+=1*19
                                fad147+=1*19
                                fbd147+=1*19
                                fcd147+=1*19
                                fad148+=1*19
                                fbd148+=1*19
                                fcd148+=1*19
                                fad149+=1*19
                                fbd149+=1*19
                                fcd149+=1*19
                                fad150+=1*19
                                fbd150+=1*19
                                fcd150+=1*19
                                fad151+=1*19
                                fbd151+=1*19
                                fcd151+=1*19
                                fad152+=1*19
                                fbd152+=1*19
                                fcd152+=1*19
                                faces2p.append([fad136,fbd136,fcd136])
                                faces2p.append([fad137,fbd137,fcd137])
                                faces2p.append([fad138,fbd138,fcd138])
                                faces2p.append([fad139,fbd139,fcd139])
                                faces2p.append([fad140,fbd140,fcd140])
                                faces2p.append([fad141,fbd141,fcd141])
                                faces2p.append([fad142,fbd142,fcd142])
                                faces2p.append([fad143,fbd143,fcd143])
                                faces2p.append([fad144,fbd144,fcd144])
                                faces2p.append([fad145,fbd145,fcd145])
                                faces2p.append([fad146,fbd146,fcd146])
                                faces2p.append([fad147,fbd147,fcd147])
                                faces2p.append([fad148,fbd148,fcd148])
                                faces2p.append([fad149,fbd149,fcd139])
                                faces2p.append([fad150,fbd150,fcd150])
                                faces2p.append([fad151,fbd151,fcd151])
                                faces2p.append([fad152,fbd152,fcd152])

                        elif vertexCount == 20:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx18 = unpack("<h", f.read(2))[0] / 4096
                                uvy18 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2q.append([vx,vz,vy])
                                uvs2q.append([uvx18,-uvy18])
                            for i in range(vertexCount-19):
                                fad153+=1*20
                                fbd153+=1*20
                                fcd153+=1*20
                                fad154+=1*20
                                fbd154+=1*20
                                fcd154+=1*20
                                fad155+=1*20
                                fbd155+=1*20
                                fcd155+=1*20
                                fad156+=1*20
                                fbd156+=1*20
                                fcd156+=1*20
                                fad157+=1*20
                                fbd157+=1*20
                                fcd157+=1*20
                                fad158+=1*20
                                fbd158+=1*20
                                fcd158+=1*20
                                fad159+=1*20
                                fbd159+=1*20
                                fcd159+=1*20
                                fad160+=1*20
                                fbd160+=1*20
                                fcd160+=1*20
                                fad161+=1*20
                                fbd161+=1*20
                                fcd161+=1*20
                                fad162+=1*20
                                fbd162+=1*20
                                fcd162+=1*20
                                fad163+=1*20
                                fbd163+=1*20
                                fcd163+=1*20
                                fad164+=1*20
                                fbd164+=1*20
                                fcd164+=1*20
                                fad165+=1*20
                                fbd165+=1*20
                                fcd165+=1*20
                                fad166+=1*20
                                fbd166+=1*20
                                fcd166+=1*20
                                fad167+=1*20
                                fbd167+=1*20
                                fcd167+=1*20
                                fad168+=1*20
                                fbd168+=1*20
                                fcd168+=1*20
                                fad169+=1*20
                                fbd169+=1*20
                                fcd169+=1*20
                                fad170+=1*20
                                fbd170+=1*20
                                fcd170+=1*20
                                faces2q.append([fad153,fbd153,fcd153])
                                faces2q.append([fad154,fbd154,fcd154])
                                faces2q.append([fad155,fbd155,fcd155])
                                faces2q.append([fad156,fbd156,fcd156])
                                faces2q.append([fad157,fbd157,fcd157])
                                faces2q.append([fad158,fbd158,fcd158])
                                faces2q.append([fad159,fbd159,fcd159])
                                faces2q.append([fad160,fbd160,fcd160])
                                faces2q.append([fad161,fbd161,fcd161])
                                faces2q.append([fad162,fbd162,fcd162])
                                faces2q.append([fad163,fbd163,fcd163])
                                faces2q.append([fad164,fbd164,fcd164])
                                faces2q.append([fad165,fbd165,fcd165])
                                faces2q.append([fad166,fbd166,fcd166])
                                faces2q.append([fad167,fbd167,fcd167])
                                faces2q.append([fad168,fbd168,fcd168])
                                faces2q.append([fad169,fbd169,fcd169])
                                faces2q.append([fad170,fbd170,fcd170])

                        elif vertexCount == 21:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx19 = unpack("<h", f.read(2))[0] / 4096
                                uvy19 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2r.append([vx,vz,vy])
                                uvs2r.append([uvx19,-uvy19])
                            for i in range(vertexCount-20):
                                fad171+=1*21
                                fbd171+=1*21
                                fcd171+=1*21
                                fad172+=1*21
                                fbd172+=1*21
                                fcd172+=1*21
                                fad173+=1*21
                                fbd173+=1*21
                                fcd173+=1*21
                                fad174+=1*21
                                fbd174+=1*21
                                fcd174+=1*21
                                fad175+=1*21
                                fbd175+=1*21
                                fcd175+=1*21
                                fad176+=1*21
                                fbd176+=1*21
                                fcd176+=1*21
                                fad177+=1*21
                                fbd177+=1*21
                                fcd177+=1*21
                                fad178+=1*21
                                fbd178+=1*21
                                fcd178+=1*21
                                fad179+=1*21
                                fbd179+=1*21
                                fcd179+=1*21
                                fad180+=1*21
                                fbd180+=1*21
                                fcd180+=1*21
                                fad181+=1*21
                                fbd181+=1*21
                                fcd181+=1*21
                                fad182+=1*21
                                fbd182+=1*21
                                fcd182+=1*21
                                fad183+=1*21
                                fbd183+=1*21
                                fcd183+=1*21
                                fad184+=1*21
                                fbd184+=1*21
                                fcd184+=1*21
                                fad185+=1*21
                                fbd185+=1*21
                                fcd185+=1*21
                                fad186+=1*21
                                fbd186+=1*21
                                fcd186+=1*21
                                fad187+=1*21
                                fbd187+=1*21
                                fcd187+=1*21
                                fad188+=1*21
                                fbd188+=1*21
                                fcd188+=1*21
                                fad189+=1*21
                                fbd189+=1*21
                                fcd189+=1*21
                                faces2r.append([fad171,fbd171,fcd171])
                                faces2r.append([fad172,fbd172,fcd172])
                                faces2r.append([fad173,fbd173,fcd173])
                                faces2r.append([fad174,fbd174,fcd174])
                                faces2r.append([fad175,fbd175,fcd175])
                                faces2r.append([fad176,fbd176,fcd176])
                                faces2r.append([fad177,fbd177,fcd177])
                                faces2r.append([fad178,fbd178,fcd178])
                                faces2r.append([fad179,fbd179,fcd179])
                                faces2r.append([fad180,fbd180,fcd180])
                                faces2r.append([fad181,fbd181,fcd181])
                                faces2r.append([fad182,fbd182,fcd182])
                                faces2r.append([fad183,fbd183,fcd183])
                                faces2r.append([fad184,fbd184,fcd184])
                                faces2r.append([fad185,fbd185,fcd185])
                                faces2r.append([fad186,fbd186,fcd186])
                                faces2r.append([fad187,fbd187,fcd187])
                                faces2r.append([fad188,fbd188,fcd188])
                                faces2r.append([fad189,fbd189,fcd189])

                        elif vertexCount == 22:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx20 = unpack("<h", f.read(2))[0] / 4096
                                uvy20 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2s.append([vx,vz,vy])
                                uvs2s.append([uvx20,-uvy20])
                            for i in range(vertexCount-21):
                                fad190+=1*22
                                fbd190+=1*22
                                fcd190+=1*22
                                fad191+=1*22
                                fbd191+=1*22
                                fcd191+=1*22
                                fad192+=1*22
                                fbd192+=1*22
                                fcd192+=1*22
                                fad193+=1*22
                                fbd193+=1*22
                                fcd193+=1*22
                                fad194+=1*22
                                fbd194+=1*22
                                fcd194+=1*22
                                fad195+=1*22
                                fbd195+=1*22
                                fcd195+=1*22
                                fad196+=1*22
                                fbd196+=1*22
                                fcd196+=1*22
                                fad197+=1*22
                                fbd197+=1*22
                                fcd197+=1*22
                                fad198+=1*22
                                fbd198+=1*22
                                fcd198+=1*22
                                fad199+=1*22
                                fbd199+=1*22
                                fcd199+=1*22
                                fad200+=1*22
                                fbd200+=1*22
                                fcd200+=1*22
                                fad201+=1*22
                                fbd201+=1*22
                                fcd201+=1*22
                                fad202+=1*22
                                fbd202+=1*22
                                fcd202+=1*22
                                fad203+=1*22
                                fbd203+=1*22
                                fcd203+=1*22
                                fad204+=1*22
                                fbd204+=1*22
                                fcd204+=1*22
                                fad205+=1*22
                                fbd205+=1*22
                                fcd205+=1*22
                                fad206+=1*22
                                fbd206+=1*22
                                fcd206+=1*22
                                fad207+=1*22
                                fbd207+=1*22
                                fcd207+=1*22
                                fad208+=1*22
                                fbd208+=1*22
                                fcd208+=1*22
                                fad209+=1*22
                                fbd209+=1*22
                                fcd209+=1*22
                                faces2s.append([fad190,fbd190,fcd190])
                                faces2s.append([fad191,fbd191,fcd191])
                                faces2s.append([fad192,fbd192,fcd192])
                                faces2s.append([fad193,fbd193,fcd193])
                                faces2s.append([fad194,fbd194,fcd194])
                                faces2s.append([fad195,fbd195,fcd195])
                                faces2s.append([fad196,fbd196,fcd196])
                                faces2s.append([fad197,fbd197,fcd197])
                                faces2s.append([fad198,fbd198,fcd198])
                                faces2s.append([fad199,fbd199,fcd199])
                                faces2s.append([fad200,fbd200,fcd200])
                                faces2s.append([fad201,fbd201,fcd201])
                                faces2s.append([fad202,fbd202,fcd202])
                                faces2s.append([fad203,fbd203,fcd203])
                                faces2s.append([fad204,fbd204,fcd204])
                                faces2s.append([fad205,fbd205,fcd205])
                                faces2s.append([fad206,fbd206,fcd206])
                                faces2s.append([fad207,fbd207,fcd207])
                                faces2s.append([fad208,fbd208,fcd208])
                                faces2s.append([fad209,fbd209,fcd209])

                        elif vertexCount == 23:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx21 = unpack("<h", f.read(2))[0] / 4096
                                uvy21 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2t.append([vx,vz,vy])
                                uvs2t.append([uvx21,-uvy21])
                            for i in range(vertexCount-22):
                                fad210+=1*23
                                fbd210+=1*23
                                fcd210+=1*23
                                fad211+=1*23
                                fbd211+=1*23
                                fcd211+=1*23
                                fad212+=1*23
                                fbd212+=1*23
                                fcd212+=1*23
                                fad213+=1*23
                                fbd213+=1*23
                                fcd213+=1*23
                                fad214+=1*23
                                fbd214+=1*23
                                fcd214+=1*23
                                fad215+=1*23
                                fbd215+=1*23
                                fcd215+=1*23
                                fad216+=1*23
                                fbd216+=1*23
                                fcd216+=1*23
                                fad217+=1*23
                                fbd217+=1*23
                                fcd217+=1*23
                                fad218+=1*23
                                fbd218+=1*23
                                fcd218+=1*23
                                fad219+=1*23
                                fbd219+=1*23
                                fcd219+=1*23
                                fad220+=1*23
                                fbd220+=1*23
                                fcd220+=1*23
                                fad221+=1*23
                                fbd221+=1*23
                                fcd221+=1*23
                                fad222+=1*23
                                fbd222+=1*23
                                fcd222+=1*23
                                fad223+=1*23
                                fbd223+=1*23
                                fcd223+=1*23
                                fad224+=1*23
                                fbd224+=1*23
                                fcd224+=1*23
                                fad225+=1*23
                                fbd225+=1*23
                                fcd225+=1*23
                                fad226+=1*23
                                fbd226+=1*23
                                fcd226+=1*23
                                fad227+=1*23
                                fbd227+=1*23
                                fcd227+=1*23
                                fad228+=1*23
                                fbd228+=1*23
                                fcd228+=1*23
                                fad229+=1*23
                                fbd229+=1*23
                                fcd229+=1*23
                                fad230+=1*23
                                fbd230+=1*23
                                fcd230+=1*23
                                faces2t.append([fad210,fbd210,fcd210])
                                faces2t.append([fad211,fbd211,fcd211])
                                faces2t.append([fad212,fbd212,fcd212])
                                faces2t.append([fad213,fbd213,fcd213])
                                faces2t.append([fad214,fbd214,fcd214])
                                faces2t.append([fad215,fbd215,fcd215])
                                faces2t.append([fad216,fbd216,fcd216])
                                faces2t.append([fad217,fbd217,fcd217])
                                faces2t.append([fad218,fbd218,fcd218])
                                faces2t.append([fad219,fbd219,fcd219])
                                faces2t.append([fad220,fbd220,fcd220])
                                faces2t.append([fad221,fbd221,fcd221])
                                faces2t.append([fad222,fbd222,fcd222])
                                faces2t.append([fad223,fbd223,fcd223])
                                faces2t.append([fad224,fbd224,fcd224])
                                faces2t.append([fad225,fbd225,fcd225])
                                faces2t.append([fad226,fbd226,fcd226])
                                faces2t.append([fad227,fbd227,fcd227])
                                faces2t.append([fad228,fbd228,fcd228])
                                faces2t.append([fad229,fbd229,fcd229])
                                faces2t.append([fad230,fbd230,fcd230])

                        elif vertexCount == 24:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx22 = unpack("<h", f.read(2))[0] / 4096
                                uvy22 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2u.append([vx,vz,vy])
                                uvs2u.append([uvx22,-uvy22])
                            for i in range(vertexCount-23):
                                fad231+=1*24
                                fbd231+=1*24
                                fcd231+=1*24
                                fad232+=1*24
                                fbd232+=1*24
                                fcd232+=1*24
                                fad233+=1*24
                                fbd233+=1*24
                                fcd233+=1*24
                                fad234+=1*24
                                fbd234+=1*24
                                fcd234+=1*24
                                fad235+=1*24
                                fbd235+=1*24
                                fcd235+=1*24
                                fad236+=1*24
                                fbd236+=1*24
                                fcd236+=1*24
                                fad237+=1*24
                                fbd237+=1*24
                                fcd237+=1*24
                                fad238+=1*24
                                fbd238+=1*24
                                fcd238+=1*24
                                fad239+=1*24
                                fbd239+=1*24
                                fcd239+=1*24
                                fad240+=1*24
                                fbd240+=1*24
                                fcd240+=1*24
                                fad241+=1*24
                                fbd241+=1*24
                                fcd241+=1*24
                                fad242+=1*24
                                fbd242+=1*24
                                fcd242+=1*24
                                fad243+=1*24
                                fbd243+=1*24
                                fcd243+=1*24
                                fad244+=1*24
                                fbd244+=1*24
                                fcd244+=1*24
                                fad245+=1*24
                                fbd245+=1*24
                                fcd245+=1*24
                                fad246+=1*24
                                fbd246+=1*24
                                fcd246+=1*24
                                fad247+=1*24
                                fbd247+=1*24
                                fcd247+=1*24
                                fad248+=1*24
                                fbd248+=1*24
                                fcd248+=1*24
                                fad249+=1*24
                                fbd249+=1*24
                                fcd249+=1*24
                                fad250+=1*24
                                fbd250+=1*24
                                fcd250+=1*24
                                fad251+=1*24
                                fbd251+=1*24
                                fcd251+=1*24
                                fad252+=1*24
                                fbd252+=1*24
                                fcd252+=1*24
                                faces2u.append([fad231,fbd231,fcd231])
                                faces2u.append([fad232,fbd232,fcd232])
                                faces2u.append([fad233,fbd233,fcd233])
                                faces2u.append([fad234,fbd234,fcd234])
                                faces2u.append([fad235,fbd235,fcd235])
                                faces2u.append([fad236,fbd236,fcd236])
                                faces2u.append([fad237,fbd237,fcd237])
                                faces2u.append([fad238,fbd238,fcd238])
                                faces2u.append([fad239,fbd239,fcd239])
                                faces2u.append([fad240,fbd240,fcd240])
                                faces2u.append([fad241,fbd241,fcd241])
                                faces2u.append([fad242,fbd242,fcd242])
                                faces2u.append([fad243,fbd243,fcd243])
                                faces2u.append([fad244,fbd244,fcd244])
                                faces2u.append([fad245,fbd245,fcd245])
                                faces2u.append([fad246,fbd246,fcd246])
                                faces2u.append([fad247,fbd247,fcd247])
                                faces2u.append([fad248,fbd248,fcd248])
                                faces2u.append([fad249,fbd249,fcd249])
                                faces2u.append([fad250,fbd250,fcd250])
                                faces2u.append([fad251,fbd251,fcd251])
                                faces2u.append([fad252,fbd252,fcd252])

                        elif vertexCount == 25:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx23 = unpack("<h", f.read(2))[0] / 4096
                                uvy23 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2v.append([vx,vz,vy])
                                uvs2v.append([uvx23,-uvy23])
                            for i in range(vertexCount-24):
                                fad253+=1*25
                                fbd253+=1*25
                                fcd253+=1*25
                                fad254+=1*25
                                fbd254+=1*25
                                fcd254+=1*25
                                fad255+=1*25
                                fbd255+=1*25
                                fcd255+=1*25
                                fad256+=1*25
                                fbd256+=1*25
                                fcd256+=1*25
                                fad257+=1*25
                                fbd257+=1*25
                                fcd257+=1*25
                                fad258+=1*25
                                fbd258+=1*25
                                fcd258+=1*25
                                fad259+=1*25
                                fbd259+=1*25
                                fcd259+=1*25
                                fad260+=1*25
                                fbd260+=1*25
                                fcd260+=1*25
                                fad261+=1*25
                                fbd261+=1*25
                                fcd261+=1*25
                                fad262+=1*25
                                fbd262+=1*25
                                fcd262+=1*25
                                fad263+=1*25
                                fbd263+=1*25
                                fcd263+=1*25
                                fad264+=1*25
                                fbd264+=1*25
                                fcd264+=1*25
                                fad265+=1*25
                                fbd265+=1*25
                                fcd265+=1*25
                                fad266+=1*25
                                fbd266+=1*25
                                fcd266+=1*25
                                fad267+=1*25
                                fbd267+=1*25
                                fcd267+=1*25
                                fad268+=1*25
                                fbd268+=1*25
                                fcd268+=1*25
                                fad269+=1*25
                                fbd269+=1*25
                                fcd269+=1*25
                                fad270+=1*25
                                fbd270+=1*25
                                fcd270+=1*25
                                fad271+=1*25
                                fbd271+=1*25
                                fcd271+=1*25
                                fad272+=1*25
                                fbd272+=1*25
                                fcd272+=1*25
                                fad273+=1*25
                                fbd273+=1*25
                                fcd273+=1*25
                                fad274+=1*25
                                fbd274+=1*25
                                fcd274+=1*25
                                fad275+=1*25
                                fbd275+=1*25
                                fcd275+=1*25
                                faces2v.append([fad253,fbd253,fcd253])
                                faces2v.append([fad254,fbd254,fcd254])
                                faces2v.append([fad255,fbd255,fcd255])
                                faces2v.append([fad256,fbd256,fcd256])
                                faces2v.append([fad257,fbd257,fcd257])
                                faces2v.append([fad258,fbd258,fcd258])
                                faces2v.append([fad259,fbd259,fcd259])
                                faces2v.append([fad260,fbd260,fcd260])
                                faces2v.append([fad261,fbd261,fcd261])
                                faces2v.append([fad262,fbd262,fcd262])
                                faces2v.append([fad263,fbd263,fcd263])
                                faces2v.append([fad264,fbd264,fcd264])
                                faces2v.append([fad265,fbd265,fcd265])
                                faces2v.append([fad266,fbd266,fcd266])
                                faces2v.append([fad267,fbd267,fcd267])
                                faces2v.append([fad268,fbd268,fcd268])
                                faces2v.append([fad269,fbd269,fcd269])
                                faces2v.append([fad270,fbd270,fcd270])
                                faces2v.append([fad271,fbd271,fcd271])
                                faces2v.append([fad272,fbd272,fcd272])
                                faces2v.append([fad273,fbd273,fcd273])
                                faces2v.append([fad274,fbd274,fcd274])
                                faces2v.append([fad275,fbd275,fcd275])
                        elif vertexCount == 26:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx24 = unpack("<h", f.read(2))[0] / 4096
                                uvy24 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2w.append([vx,vz,vy])
                                uvs2w.append([uvx24,-uvy24])
                            for i in range(vertexCount-25):
                                fad276+=1*26
                                fbd276+=1*26
                                fcd276+=1*26
                                fad277+=1*26
                                fbd277+=1*26
                                fcd277+=1*26
                                fad278+=1*26
                                fbd278+=1*26
                                fcd278+=1*26
                                fad279+=1*26
                                fbd279+=1*26
                                fcd279+=1*26
                                fad280+=1*26
                                fbd280+=1*26
                                fcd280+=1*26
                                fad281+=1*26
                                fbd281+=1*26
                                fcd281+=1*26
                                fad282+=1*26
                                fbd282+=1*26
                                fcd282+=1*26
                                fad283+=1*26
                                fbd283+=1*26
                                fcd283+=1*26
                                fad284+=1*26
                                fbd284+=1*26
                                fcd284+=1*26
                                fad285+=1*26
                                fbd285+=1*26
                                fcd285+=1*26
                                fad286+=1*26
                                fbd286+=1*26
                                fcd286+=1*26
                                fad287+=1*26
                                fbd287+=1*26
                                fcd287+=1*26
                                fad288+=1*26
                                fbd288+=1*26
                                fcd288+=1*26
                                fad289+=1*26
                                fbd289+=1*26
                                fcd289+=1*26
                                fad290+=1*26
                                fbd290+=1*26
                                fcd290+=1*26
                                fad291+=1*26
                                fbd291+=1*26
                                fcd291+=1*26
                                fad292+=1*26
                                fbd292+=1*26
                                fcd292+=1*26
                                fad293+=1*26
                                fbd293+=1*26
                                fcd293+=1*26
                                fad294+=1*26
                                fbd294+=1*26
                                fcd294+=1*26
                                fad295+=1*26
                                fbd295+=1*26
                                fcd295+=1*26
                                fad296+=1*26
                                fbd296+=1*26
                                fcd296+=1*26
                                fad297+=1*26
                                fbd297+=1*26
                                fcd297+=1*26
                                fad298+=1*26
                                fbd298+=1*26
                                fcd298+=1*26
                                fad299+=1*26
                                fbd299+=1*26
                                fcd299+=1*26
                                faces2w.append([fad276,fbd276,fcd276])
                                faces2w.append([fad277,fbd277,fcd277])
                                faces2w.append([fad278,fbd278,fcd278])
                                faces2w.append([fad279,fbd279,fcd279])
                                faces2w.append([fad280,fbd280,fcd280])
                                faces2w.append([fad281,fbd281,fcd281])
                                faces2w.append([fad282,fbd282,fcd282])
                                faces2w.append([fad283,fbd283,fcd283])
                                faces2w.append([fad284,fbd284,fcd284])
                                faces2w.append([fad285,fbd285,fcd285])
                                faces2w.append([fad286,fbd286,fcd286])
                                faces2w.append([fad287,fbd287,fcd287])
                                faces2w.append([fad288,fbd288,fcd288])
                                faces2w.append([fad289,fbd289,fcd289])
                                faces2w.append([fad290,fbd290,fcd290])
                                faces2w.append([fad291,fbd291,fcd291])
                                faces2w.append([fad292,fbd292,fcd292])
                                faces2w.append([fad293,fbd293,fcd293])
                                faces2w.append([fad294,fbd294,fcd294])
                                faces2w.append([fad295,fbd295,fcd295])
                                faces2w.append([fad296,fbd296,fcd296])
                                faces2w.append([fad297,fbd297,fcd297])
                                faces2w.append([fad298,fbd298,fcd298])
                                faces2w.append([fad299,fbd299,fcd299])
                        elif vertexCount == 27:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx25 = unpack("<h", f.read(2))[0] / 4096
                                uvy25 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2x.append([vx,vz,vy])
                                uvs2x.append([uvx25,-uvy25])
                            for i in range(vertexCount-26):
                                fad300+=1*27
                                fbd300+=1*27
                                fcd300+=1*27
                                fad301+=1*27
                                fbd301+=1*27
                                fcd301+=1*27
                                fad302+=1*27
                                fbd302+=1*27
                                fcd302+=1*27
                                fad303+=1*27
                                fbd303+=1*27
                                fcd303+=1*27
                                fad304+=1*27
                                fbd304+=1*27
                                fcd304+=1*27
                                fad305+=1*27
                                fbd305+=1*27
                                fcd305+=1*27
                                fad306+=1*27
                                fbd306+=1*27
                                fcd306+=1*27
                                fad307+=1*27
                                fbd307+=1*27
                                fcd307+=1*27
                                fad308+=1*27
                                fbd308+=1*27
                                fcd308+=1*27
                                fad309+=1*27
                                fbd309+=1*27
                                fcd309+=1*27
                                fad310+=1*27
                                fbd310+=1*27
                                fcd310+=1*27
                                fad311+=1*27
                                fbd311+=1*27
                                fcd311+=1*27
                                fad312+=1*27
                                fbd312+=1*27
                                fcd312+=1*27
                                fad313+=1*27
                                fbd313+=1*27
                                fcd313+=1*27
                                fad314+=1*27
                                fbd314+=1*27
                                fcd314+=1*27
                                fad315+=1*27
                                fbd315+=1*27
                                fcd315+=1*27
                                fad316+=1*27
                                fbd316+=1*27
                                fcd316+=1*27
                                fad317+=1*27
                                fbd317+=1*27
                                fcd317+=1*27
                                fad318+=1*27
                                fbd318+=1*27
                                fcd318+=1*27
                                fad319+=1*27
                                fbd319+=1*27
                                fcd319+=1*27
                                fad320+=1*27
                                fbd320+=1*27
                                fcd320+=1*27
                                fad321+=1*27
                                fbd321+=1*27
                                fcd321+=1*27
                                fad322+=1*27
                                fbd322+=1*27
                                fcd322+=1*27
                                fad323+=1*27
                                fbd323+=1*27
                                fcd323+=1*27
                                fad324+=1*27
                                fbd324+=1*27
                                fcd324+=1*27
                                faces2x.append([fad300,fbd300,fcd300])
                                faces2x.append([fad301,fbd301,fcd301])
                                faces2x.append([fad302,fbd302,fcd302])
                                faces2x.append([fad303,fbd303,fcd303])
                                faces2x.append([fad304,fbd304,fcd304])
                                faces2x.append([fad305,fbd305,fcd305])
                                faces2x.append([fad306,fbd306,fcd306])
                                faces2x.append([fad307,fbd307,fcd307])
                                faces2x.append([fad308,fbd308,fcd308])
                                faces2x.append([fad309,fbd309,fcd309])
                                faces2x.append([fad310,fbd310,fcd310])
                                faces2x.append([fad311,fbd311,fcd311])
                                faces2x.append([fad312,fbd312,fcd312])
                                faces2x.append([fad313,fbd313,fcd313])
                                faces2x.append([fad314,fbd314,fcd314])
                                faces2x.append([fad315,fbd315,fcd315])
                                faces2x.append([fad316,fbd316,fcd316])
                                faces2x.append([fad317,fbd317,fcd317])
                                faces2x.append([fad318,fbd318,fcd318])
                                faces2x.append([fad319,fbd319,fcd319])
                                faces2x.append([fad320,fbd320,fcd320])
                                faces2x.append([fad321,fbd321,fcd321])
                                faces2x.append([fad322,fbd322,fcd322])
                                faces2x.append([fad323,fbd323,fcd323])
                                faces2x.append([fad324,fbd324,fcd324])
                        elif vertexCount == 28:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx26 = unpack("<h", f.read(2))[0] / 4096
                                uvy26 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2y.append([vx,vz,vy])
                                uvs2y.append([uvx26,-uvy26])
                            for i in range(vertexCount-27):
                                fad325+=1*28
                                fbd325+=1*28
                                fcd325+=1*28
                                fad326+=1*28
                                fbd326+=1*28
                                fcd326+=1*28
                                fad327+=1*28
                                fbd327+=1*28
                                fcd327+=1*28
                                fad328+=1*28
                                fbd328+=1*28
                                fcd328+=1*28
                                fad329+=1*28
                                fbd329+=1*28
                                fcd329+=1*28
                                fad330+=1*28
                                fbd330+=1*28
                                fcd330+=1*28
                                fad331+=1*28
                                fbd331+=1*28
                                fcd331+=1*28
                                fad332+=1*28
                                fbd332+=1*28
                                fcd332+=1*28
                                fad333+=1*28
                                fbd333+=1*28
                                fcd333+=1*28
                                fad334+=1*28
                                fbd334+=1*28
                                fcd334+=1*28
                                fad335+=1*28
                                fbd335+=1*28
                                fcd335+=1*28
                                fad336+=1*28
                                fbd336+=1*28
                                fcd336+=1*28
                                fad337+=1*28
                                fbd337+=1*28
                                fcd337+=1*28
                                fad338+=1*28
                                fbd338+=1*28
                                fcd338+=1*28
                                fad339+=1*28
                                fbd339+=1*28
                                fcd339+=1*28
                                fad340+=1*28
                                fbd340+=1*28
                                fcd340+=1*28
                                fad341+=1*28
                                fbd341+=1*28
                                fcd341+=1*28
                                fad342+=1*28
                                fbd342+=1*28
                                fcd342+=1*28
                                fad343+=1*28
                                fbd343+=1*28
                                fcd343+=1*28
                                fad344+=1*28
                                fbd344+=1*28
                                fcd344+=1*28
                                fad345+=1*28
                                fbd345+=1*28
                                fcd345+=1*28
                                fad346+=1*28
                                fbd346+=1*28
                                fcd346+=1*28
                                fad347+=1*28
                                fbd347+=1*28
                                fcd347+=1*28
                                fad348+=1*28
                                fbd348+=1*28
                                fcd348+=1*28
                                fad349+=1*28
                                fbd349+=1*28
                                fcd349+=1*28
                                fad350+=1*28
                                fbd350+=1*28
                                fcd350+=1*28
                                faces2y.append([fad325,fbd325,fcd325])
                                faces2y.append([fad326,fbd326,fcd326])
                                faces2y.append([fad327,fbd327,fcd327])
                                faces2y.append([fad328,fbd328,fcd328])
                                faces2y.append([fad329,fbd329,fcd329])
                                faces2y.append([fad330,fbd330,fcd330])
                                faces2y.append([fad331,fbd331,fcd331])
                                faces2y.append([fad332,fbd332,fcd332])
                                faces2y.append([fad333,fbd333,fcd333])
                                faces2y.append([fad334,fbd334,fcd334])
                                faces2y.append([fad335,fbd335,fcd335])
                                faces2y.append([fad336,fbd336,fcd336])
                                faces2y.append([fad337,fbd337,fcd337])
                                faces2y.append([fad338,fbd338,fcd338])
                                faces2y.append([fad339,fbd339,fcd339])
                                faces2y.append([fad340,fbd340,fcd340])
                                faces2y.append([fad341,fbd341,fcd341])
                                faces2y.append([fad342,fbd342,fcd342])
                                faces2y.append([fad343,fbd343,fcd343])
                                faces2y.append([fad344,fbd344,fcd344])
                                faces2y.append([fad345,fbd345,fcd345])
                                faces2y.append([fad346,fbd346,fcd346])
                                faces2y.append([fad347,fbd347,fcd347])
                                faces2y.append([fad348,fbd348,fcd348])
                                faces2y.append([fad349,fbd349,fcd349])
                                faces2y.append([fad350,fbd350,fcd350])
                        elif vertexCount == 29:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx27 = unpack("<h", f.read(2))[0] / 4096
                                uvy27 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2z.append([vx,vz,vy])
                                uvs2z.append([uvx27,-uvy27])
                            for i in range(vertexCount-28):
                                fad351+=1*29
                                fbd351+=1*29
                                fcd351+=1*29
                                fad352+=1*29
                                fbd352+=1*29
                                fcd352+=1*29
                                fad353+=1*29
                                fbd353+=1*29
                                fcd353+=1*29
                                fad354+=1*29
                                fbd354+=1*29
                                fcd354+=1*29
                                fad355+=1*29
                                fbd355+=1*29
                                fcd355+=1*29
                                fad356+=1*29
                                fbd356+=1*29
                                fcd356+=1*29
                                fad357+=1*29
                                fbd357+=1*29
                                fcd357+=1*29
                                fad358+=1*29
                                fbd358+=1*29
                                fcd358+=1*29
                                fad359+=1*29
                                fbd359+=1*29
                                fcd359+=1*29
                                fad360+=1*29
                                fbd360+=1*29
                                fcd360+=1*29
                                fad361+=1*29
                                fbd361+=1*29
                                fcd361+=1*29
                                fad362+=1*29
                                fbd362+=1*29
                                fcd362+=1*29
                                fad363+=1*29
                                fbd363+=1*29
                                fcd363+=1*29
                                fad364+=1*29
                                fbd364+=1*29
                                fcd364+=1*29
                                fad365+=1*29
                                fbd365+=1*29
                                fcd365+=1*29
                                fad366+=1*29
                                fbd366+=1*29
                                fcd366+=1*29
                                fad367+=1*29
                                fbd367+=1*29
                                fcd367+=1*29
                                fad368+=1*29
                                fbd368+=1*29
                                fcd368+=1*29
                                fad369+=1*29
                                fbd369+=1*29
                                fcd369+=1*29
                                fad370+=1*29
                                fbd370+=1*29
                                fcd370+=1*29
                                fad371+=1*29
                                fbd371+=1*29
                                fcd371+=1*29
                                fad372+=1*29
                                fbd372+=1*29
                                fcd372+=1*29
                                fad373+=1*29
                                fbd373+=1*29
                                fcd373+=1*29
                                fad374+=1*29
                                fbd374+=1*29
                                fcd374+=1*29
                                fad375+=1*29
                                fbd375+=1*29
                                fcd375+=1*29
                                fad376+=1*29
                                fbd376+=1*29
                                fcd376+=1*29
                                fad377+=1*29
                                fbd377+=1*29
                                fcd377+=1*29
                                faces2z.append([fad351,fbd351,fcd351])
                                faces2z.append([fad352,fbd352,fcd352])
                                faces2z.append([fad353,fbd353,fcd353])
                                faces2z.append([fad354,fbd354,fcd354])
                                faces2z.append([fad355,fbd355,fcd355])
                                faces2z.append([fad356,fbd356,fcd356])
                                faces2z.append([fad357,fbd357,fcd357])
                                faces2z.append([fad358,fbd358,fcd358])
                                faces2z.append([fad359,fbd359,fcd359])
                                faces2z.append([fad360,fbd360,fcd360])
                                faces2z.append([fad361,fbd361,fcd361])
                                faces2z.append([fad362,fbd362,fcd362])
                                faces2z.append([fad363,fbd363,fcd363])
                                faces2z.append([fad364,fbd364,fcd364])
                                faces2z.append([fad365,fbd365,fcd365])
                                faces2z.append([fad366,fbd366,fcd366])
                                faces2z.append([fad367,fbd367,fcd367])
                                faces2z.append([fad368,fbd368,fcd368])
                                faces2z.append([fad369,fbd369,fcd369])
                                faces2z.append([fad370,fbd370,fcd370])
                                faces2z.append([fad371,fbd371,fcd371])
                                faces2z.append([fad372,fbd372,fcd372])
                                faces2z.append([fad373,fbd373,fcd373])
                                faces2z.append([fad374,fbd374,fcd374])
                                faces2z.append([fad375,fbd375,fcd375])
                                faces2z.append([fad376,fbd376,fcd376])
                                faces2z.append([fad377,fbd377,fcd377])
                        elif vertexCount == 30:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx28 = unpack("<h", f.read(2))[0] / 4096
                                uvy28 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zz.append([vx,vz,vy])
                                uvs2zz.append([uvx28,-uvy28])
                            for i in range(vertexCount-29):
                                fad378+=1*30
                                fbd378+=1*30
                                fcd378+=1*30
                                fad379+=1*30
                                fbd379+=1*30
                                fcd379+=1*30
                                fad380+=1*30
                                fbd380+=1*30
                                fcd380+=1*30
                                fad381+=1*30
                                fbd381+=1*30
                                fcd381+=1*30
                                fad382+=1*30
                                fbd382+=1*30
                                fcd382+=1*30
                                fad383+=1*30
                                fbd383+=1*30
                                fcd383+=1*30
                                fad384+=1*30
                                fbd384+=1*30
                                fcd384+=1*30
                                fad385+=1*30
                                fbd385+=1*30
                                fcd385+=1*30
                                fad386+=1*30
                                fbd386+=1*30
                                fcd386+=1*30
                                fad387+=1*30
                                fbd387+=1*30
                                fcd387+=1*30
                                fad388+=1*30
                                fbd388+=1*30
                                fcd388+=1*30
                                fad389+=1*30
                                fbd389+=1*30
                                fcd389+=1*30
                                fad390+=1*30
                                fbd390+=1*30
                                fcd390+=1*30
                                fad391+=1*30
                                fbd391+=1*30
                                fcd391+=1*30
                                fad392+=1*30
                                fbd392+=1*30
                                fcd392+=1*30
                                fad393+=1*30
                                fbd393+=1*30
                                fcd393+=1*30
                                fad394+=1*30
                                fbd394+=1*30
                                fcd394+=1*30
                                fad395+=1*30
                                fbd395+=1*30
                                fcd395+=1*30
                                fad396+=1*30
                                fbd396+=1*30
                                fcd396+=1*30
                                fad397+=1*30
                                fbd397+=1*30
                                fcd397+=1*30
                                fad398+=1*30
                                fbd398+=1*30
                                fcd398+=1*30
                                fad399+=1*30
                                fbd399+=1*30
                                fcd399+=1*30
                                fad400+=1*30
                                fbd400+=1*30
                                fcd400+=1*30
                                fad401+=1*30
                                fbd401+=1*30
                                fcd401+=1*30
                                fad402+=1*30
                                fbd402+=1*30
                                fcd402+=1*30
                                fad403+=1*30
                                fbd403+=1*30
                                fcd403+=1*30
                                fad404+=1*30
                                fbd404+=1*30
                                fcd404+=1*30
                                fad405+=1*30
                                fbd405+=1*30
                                fcd405+=1*30
                                faces2zz.append([fad378,fbd378,fcd378])
                                faces2zz.append([fad379,fbd379,fcd379])
                                faces2zz.append([fad380,fbd380,fcd380])
                                faces2zz.append([fad381,fbd381,fcd381])
                                faces2zz.append([fad382,fbd382,fcd382])
                                faces2zz.append([fad383,fbd383,fcd383])
                                faces2zz.append([fad384,fbd384,fcd384])
                                faces2zz.append([fad385,fbd385,fcd385])
                                faces2zz.append([fad386,fbd386,fcd386])
                                faces2zz.append([fad387,fbd387,fcd387])
                                faces2zz.append([fad388,fbd388,fcd388])
                                faces2zz.append([fad389,fbd389,fcd389])
                                faces2zz.append([fad390,fbd390,fcd390])
                                faces2zz.append([fad391,fbd391,fcd391])
                                faces2zz.append([fad392,fbd392,fcd392])
                                faces2zz.append([fad393,fbd393,fcd393])
                                faces2zz.append([fad394,fbd394,fcd394])
                                faces2zz.append([fad395,fbd395,fcd395])
                                faces2zz.append([fad396,fbd396,fcd396])
                                faces2zz.append([fad397,fbd397,fcd397])
                                faces2zz.append([fad398,fbd398,fcd398])
                                faces2zz.append([fad399,fbd399,fcd399])
                                faces2zz.append([fad400,fbd400,fcd400])
                                faces2zz.append([fad401,fbd401,fcd401])
                                faces2zz.append([fad402,fbd402,fcd402])
                                faces2zz.append([fad403,fbd403,fcd403])
                                faces2zz.append([fad404,fbd404,fcd404])
                                faces2zz.append([fad405,fbd405,fcd405])
                        elif vertexCount == 31:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx29 = unpack("<h", f.read(2))[0] / 4096
                                uvy29 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzz.append([vx,vz,vy])
                                uvs2zzz.append([uvx29,-uvy29])
                            for i in range(vertexCount-30):
                                fad406+=1*31
                                fbd406+=1*31
                                fcd406+=1*31
                                fad407+=1*31
                                fbd407+=1*31
                                fcd407+=1*31
                                fad408+=1*31
                                fbd408+=1*31
                                fcd408+=1*31
                                fad409+=1*31
                                fbd409+=1*31
                                fcd409+=1*31
                                fad410+=1*31
                                fbd410+=1*31
                                fcd410+=1*31
                                fad411+=1*31
                                fbd411+=1*31
                                fcd411+=1*31
                                fad412+=1*31
                                fbd412+=1*31
                                fcd412+=1*31
                                fad413+=1*31
                                fbd413+=1*31
                                fcd413+=1*31
                                fad414+=1*31
                                fbd414+=1*31
                                fcd414+=1*31
                                fad415+=1*31
                                fbd415+=1*31
                                fcd415+=1*31
                                fad416+=1*31
                                fbd416+=1*31
                                fcd416+=1*31
                                fad417+=1*31
                                fbd417+=1*31
                                fcd417+=1*31
                                fad418+=1*31
                                fbd418+=1*31
                                fcd418+=1*31
                                fad419+=1*31
                                fbd419+=1*31
                                fcd419+=1*31
                                fad420+=1*31
                                fbd420+=1*31
                                fcd420+=1*31
                                fad421+=1*31
                                fbd421+=1*31
                                fcd421+=1*31
                                fad422+=1*31
                                fbd422+=1*31
                                fcd422+=1*31
                                fad423+=1*31
                                fbd423+=1*31
                                fcd423+=1*31
                                fad424+=1*31
                                fbd424+=1*31
                                fcd424+=1*31
                                fad425+=1*31
                                fbd425+=1*31
                                fcd425+=1*31
                                fad426+=1*31
                                fbd426+=1*31
                                fcd426+=1*31
                                fad427+=1*31
                                fbd427+=1*31
                                fcd427+=1*31
                                fad428+=1*31
                                fbd428+=1*31
                                fcd428+=1*31
                                fad429+=1*31
                                fbd429+=1*31
                                fcd429+=1*31
                                fad430+=1*31
                                fbd430+=1*31
                                fcd430+=1*31
                                fad431+=1*31
                                fbd431+=1*31
                                fcd431+=1*31
                                fad432+=1*31
                                fbd432+=1*31
                                fcd432+=1*31
                                fad433+=1*31
                                fbd433+=1*31
                                fcd433+=1*31
                                fad434+=1*31
                                fbd434+=1*31
                                fcd434+=1*31
                                faces2zzz.append([fad406,fbd406,fcd406])
                                faces2zzz.append([fad407,fbd407,fcd407])
                                faces2zzz.append([fad408,fbd408,fcd408])
                                faces2zzz.append([fad409,fbd409,fcd409])
                                faces2zzz.append([fad410,fbd410,fcd410])
                                faces2zzz.append([fad411,fbd411,fcd411])
                                faces2zzz.append([fad412,fbd412,fcd412])
                                faces2zzz.append([fad413,fbd413,fcd413])
                                faces2zzz.append([fad414,fbd414,fcd414])
                                faces2zzz.append([fad415,fbd415,fcd415])
                                faces2zzz.append([fad416,fbd416,fcd416])
                                faces2zzz.append([fad417,fbd417,fcd417])
                                faces2zzz.append([fad418,fbd418,fcd418])
                                faces2zzz.append([fad419,fbd419,fcd419])
                                faces2zzz.append([fad420,fbd420,fcd420])
                                faces2zzz.append([fad421,fbd421,fcd421])
                                faces2zzz.append([fad422,fbd422,fcd422])
                                faces2zzz.append([fad423,fbd423,fcd423])
                                faces2zzz.append([fad424,fbd424,fcd424])
                                faces2zzz.append([fad425,fbd425,fcd425])
                                faces2zzz.append([fad426,fbd426,fcd426])
                                faces2zzz.append([fad427,fbd427,fcd427])
                                faces2zzz.append([fad428,fbd428,fcd428])
                                faces2zzz.append([fad429,fbd429,fcd429])
                                faces2zzz.append([fad430,fbd430,fcd430])
                                faces2zzz.append([fad431,fbd431,fcd431])
                                faces2zzz.append([fad432,fbd432,fcd432])
                                faces2zzz.append([fad433,fbd433,fcd433])
                                faces2zzz.append([fad434,fbd434,fcd434])
                        elif vertexCount == 32:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx30 = unpack("<h", f.read(2))[0] / 4096
                                uvy30 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzz.append([vx,vz,vy])
                                uvs2zzzz.append([uvx30,-uvy30])
                            for i in range(vertexCount-31):
                                fad435+=1*32
                                fbd435+=1*32
                                fcd435+=1*32
                                fad436+=1*32
                                fbd436+=1*32
                                fcd436+=1*32
                                fad437+=1*32
                                fbd437+=1*32
                                fcd437+=1*32
                                fad438+=1*32
                                fbd438+=1*32
                                fcd438+=1*32
                                fad439+=1*32
                                fbd439+=1*32
                                fcd439+=1*32
                                fad440+=1*32
                                fbd440+=1*32
                                fcd440+=1*32
                                fad441+=1*32
                                fbd441+=1*32
                                fcd441+=1*32
                                fad442+=1*32
                                fbd442+=1*32
                                fcd442+=1*32
                                fad443+=1*32
                                fbd443+=1*32
                                fcd443+=1*32
                                fad444+=1*32
                                fbd444+=1*32
                                fcd444+=1*32
                                fad445+=1*32
                                fbd445+=1*32
                                fcd445+=1*32
                                fad446+=1*32
                                fbd446+=1*32
                                fcd446+=1*32
                                fad447+=1*32
                                fbd447+=1*32
                                fcd447+=1*32
                                fad448+=1*32
                                fbd448+=1*32
                                fcd448+=1*32
                                fad449+=1*32
                                fbd449+=1*32
                                fcd449+=1*32
                                fad450+=1*32
                                fbd450+=1*32
                                fcd450+=1*32
                                fad451+=1*32
                                fbd451+=1*32
                                fcd451+=1*32
                                fad452+=1*32
                                fbd452+=1*32
                                fcd452+=1*32
                                fad453+=1*32
                                fbd453+=1*32
                                fcd453+=1*32
                                fad454+=1*32
                                fbd454+=1*32
                                fcd454+=1*32
                                fad455+=1*32
                                fbd455+=1*32
                                fcd455+=1*32
                                fad456+=1*32
                                fbd456+=1*32
                                fcd456+=1*32
                                fad457+=1*32
                                fbd457+=1*32
                                fcd457+=1*32
                                fad458+=1*32
                                fbd458+=1*32
                                fcd458+=1*32
                                fad459+=1*32
                                fbd459+=1*32
                                fcd459+=1*32
                                fad460+=1*32
                                fbd460+=1*32
                                fcd460+=1*32
                                fad461+=1*32
                                fbd461+=1*32
                                fcd461+=1*32
                                fad462+=1*32
                                fbd462+=1*32
                                fcd462+=1*32
                                fad463+=1*32
                                fbd463+=1*32
                                fcd463+=1*32
                                fad464+=1*32
                                fbd464+=1*32
                                fcd464+=1*32
                                faces2zzzz.append([fad435,fbd435,fcd435])
                                faces2zzzz.append([fad436,fbd436,fcd436])
                                faces2zzzz.append([fad437,fbd437,fcd437])
                                faces2zzzz.append([fad438,fbd438,fcd438])
                                faces2zzzz.append([fad439,fbd439,fcd439])
                                faces2zzzz.append([fad440,fbd440,fcd440])
                                faces2zzzz.append([fad441,fbd441,fcd441])
                                faces2zzzz.append([fad442,fbd442,fcd442])
                                faces2zzzz.append([fad443,fbd443,fcd443])
                                faces2zzzz.append([fad444,fbd444,fcd444])
                                faces2zzzz.append([fad445,fbd445,fcd445])
                                faces2zzzz.append([fad446,fbd446,fcd446])
                                faces2zzzz.append([fad447,fbd447,fcd447])
                                faces2zzzz.append([fad448,fbd448,fcd448])
                                faces2zzzz.append([fad449,fbd449,fcd449])
                                faces2zzzz.append([fad450,fbd450,fcd450])
                                faces2zzzz.append([fad451,fbd451,fcd451])
                                faces2zzzz.append([fad452,fbd452,fcd452])
                                faces2zzzz.append([fad453,fbd453,fcd453])
                                faces2zzzz.append([fad454,fbd454,fcd454])
                                faces2zzzz.append([fad455,fbd455,fcd455])
                                faces2zzzz.append([fad456,fbd456,fcd456])
                                faces2zzzz.append([fad457,fbd457,fcd457])
                                faces2zzzz.append([fad458,fbd458,fcd458])
                                faces2zzzz.append([fad459,fbd459,fcd459])
                                faces2zzzz.append([fad460,fbd460,fcd460])
                                faces2zzzz.append([fad461,fbd461,fcd461])
                                faces2zzzz.append([fad462,fbd462,fcd462])
                                faces2zzzz.append([fad463,fbd463,fcd463])
                                faces2zzzz.append([fad464,fbd464,fcd464])

                        elif vertexCount == 33:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx31 = unpack("<h", f.read(2))[0] / 4096
                                uvy31 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzz.append([vx,vz,vy])
                                uvs2zzzzz.append([uvx31,-uvy31])
                            for i in range(vertexCount-32):
                                fad465+=1*33
                                fbd465+=1*33
                                fcd465+=1*33
                                fad466+=1*33
                                fbd466+=1*33
                                fcd466+=1*33
                                fad467+=1*33
                                fbd467+=1*33
                                fcd467+=1*33
                                fad468+=1*33
                                fbd468+=1*33
                                fcd468+=1*33
                                fad469+=1*33
                                fbd469+=1*33
                                fcd469+=1*33
                                fad470+=1*33
                                fbd470+=1*33
                                fcd470+=1*33
                                fad471+=1*33
                                fbd471+=1*33
                                fcd471+=1*33
                                fad472+=1*33
                                fbd472+=1*33
                                fcd472+=1*33
                                fad473+=1*33
                                fbd473+=1*33
                                fcd473+=1*33
                                fad474+=1*33
                                fbd474+=1*33
                                fcd474+=1*33
                                fad475+=1*33
                                fbd475+=1*33
                                fcd475+=1*33
                                fad476+=1*33
                                fbd476+=1*33
                                fcd476+=1*33
                                fad477+=1*33
                                fbd477+=1*33
                                fcd477+=1*33
                                fad478+=1*33
                                fbd478+=1*33
                                fcd478+=1*33
                                fad479+=1*33
                                fbd479+=1*33
                                fcd479+=1*33
                                fad480+=1*33
                                fbd480+=1*33
                                fcd480+=1*33
                                fad481+=1*33
                                fbd481+=1*33
                                fcd481+=1*33
                                fad482+=1*33
                                fbd482+=1*33
                                fcd482+=1*33
                                fad483+=1*33
                                fbd483+=1*33
                                fcd483+=1*33
                                fad484+=1*33
                                fbd484+=1*33
                                fcd484+=1*33
                                fad485+=1*33
                                fbd485+=1*33
                                fcd485+=1*33
                                fad486+=1*33
                                fbd486+=1*33
                                fcd486+=1*33
                                fad487+=1*33
                                fbd487+=1*33
                                fcd487+=1*33
                                fad488+=1*33
                                fbd488+=1*33
                                fcd488+=1*33
                                fad489+=1*33
                                fbd489+=1*33
                                fcd489+=1*33
                                fad490+=1*33
                                fbd490+=1*33
                                fcd490+=1*33
                                fad491+=1*33
                                fbd491+=1*33
                                fcd491+=1*33
                                fad492+=1*33
                                fbd492+=1*33
                                fcd492+=1*33
                                fad493+=1*33
                                fbd493+=1*33
                                fcd493+=1*33
                                fad494+=1*33
                                fbd494+=1*33
                                fcd494+=1*33
                                fad495+=1*33
                                fbd495+=1*33
                                fcd495+=1*33
                                faces2zzzzz.append([fad465,fbd465,fcd465])
                                faces2zzzzz.append([fad466,fbd466,fcd466])
                                faces2zzzzz.append([fad467,fbd467,fcd467])
                                faces2zzzzz.append([fad468,fbd468,fcd468])
                                faces2zzzzz.append([fad469,fbd469,fcd469])
                                faces2zzzzz.append([fad470,fbd470,fcd470])
                                faces2zzzzz.append([fad471,fbd471,fcd471])
                                faces2zzzzz.append([fad472,fbd472,fcd472])
                                faces2zzzzz.append([fad473,fbd473,fcd473])
                                faces2zzzzz.append([fad474,fbd474,fcd474])
                                faces2zzzzz.append([fad475,fbd475,fcd475])
                                faces2zzzzz.append([fad476,fbd476,fcd476])
                                faces2zzzzz.append([fad477,fbd477,fcd477])
                                faces2zzzzz.append([fad478,fbd478,fcd478])
                                faces2zzzzz.append([fad479,fbd479,fcd479])
                                faces2zzzzz.append([fad480,fbd480,fcd480])
                                faces2zzzzz.append([fad481,fbd481,fcd481])
                                faces2zzzzz.append([fad482,fbd482,fcd482])
                                faces2zzzzz.append([fad483,fbd483,fcd483])
                                faces2zzzzz.append([fad484,fbd484,fcd484])
                                faces2zzzzz.append([fad485,fbd485,fcd485])
                                faces2zzzzz.append([fad486,fbd486,fcd486])
                                faces2zzzzz.append([fad487,fbd487,fcd487])
                                faces2zzzzz.append([fad488,fbd488,fcd488])
                                faces2zzzzz.append([fad489,fbd489,fcd489])
                                faces2zzzzz.append([fad490,fbd490,fcd490])
                                faces2zzzzz.append([fad491,fbd491,fcd491])
                                faces2zzzzz.append([fad492,fbd492,fcd492])
                                faces2zzzzz.append([fad493,fbd493,fcd493])
                                faces2zzzzz.append([fad494,fbd494,fcd494])
                                faces2zzzzz.append([fad495,fbd495,fcd495])

                        elif vertexCount == 34:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx32 = unpack("<h", f.read(2))[0] / 4096
                                uvy32 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzz.append([vx,vz,vy])
                                uvs2zzzzzz.append([uvx32,-uvy32])
                            for i in range(vertexCount-33):
                                fad496+=1*34
                                fbd496+=1*34
                                fcd496+=1*34
                                fad497+=1*34
                                fbd497+=1*34
                                fcd497+=1*34
                                fad498+=1*34
                                fbd498+=1*34
                                fcd498+=1*34
                                fad499+=1*34
                                fbd499+=1*34
                                fcd499+=1*34
                                fad500+=1*34
                                fbd500+=1*34
                                fcd500+=1*34
                                fad501+=1*34
                                fbd501+=1*34
                                fcd501+=1*34
                                fad502+=1*34
                                fbd502+=1*34
                                fcd502+=1*34
                                fad503+=1*34
                                fbd503+=1*34
                                fcd503+=1*34
                                fad504+=1*34
                                fbd504+=1*34
                                fcd504+=1*34
                                fad505+=1*34
                                fbd505+=1*34
                                fcd505+=1*34
                                fad506+=1*34
                                fbd506+=1*34
                                fcd506+=1*34
                                fad507+=1*34
                                fbd507+=1*34
                                fcd507+=1*34
                                fad508+=1*34
                                fbd508+=1*34
                                fcd508+=1*34
                                fad509+=1*34
                                fbd509+=1*34
                                fcd509+=1*34
                                fad510+=1*34
                                fbd510+=1*34
                                fcd510+=1*34
                                fad511+=1*34
                                fbd511+=1*34
                                fcd511+=1*34
                                fad512+=1*34
                                fbd512+=1*34
                                fcd512+=1*34
                                fad513+=1*34
                                fbd513+=1*34
                                fcd513+=1*34
                                fad514+=1*34
                                fbd514+=1*34
                                fcd514+=1*34
                                fad515+=1*34
                                fbd515+=1*34
                                fcd515+=1*34
                                fad516+=1*34
                                fbd516+=1*34
                                fcd516+=1*34
                                fad517+=1*34
                                fbd517+=1*34
                                fcd517+=1*34
                                fad518+=1*34
                                fbd518+=1*34
                                fcd518+=1*34
                                fad519+=1*34
                                fbd519+=1*34
                                fcd519+=1*34
                                fad520+=1*34
                                fbd520+=1*34
                                fcd520+=1*34
                                fad521+=1*34
                                fbd521+=1*34
                                fcd521+=1*34
                                fad522+=1*34
                                fbd522+=1*34
                                fcd522+=1*34
                                fad523+=1*34
                                fbd523+=1*34
                                fcd523+=1*34
                                fad524+=1*34
                                fbd524+=1*34
                                fcd524+=1*34
                                fad525+=1*34
                                fbd525+=1*34
                                fcd525+=1*34
                                fad526+=1*34
                                fbd526+=1*34
                                fcd526+=1*34
                                fad527+=1*34
                                fbd527+=1*34
                                fcd527+=1*34
                                faces2zzzzzz.append([fad496,fbd496,fcd496])
                                faces2zzzzzz.append([fad497,fbd497,fcd497])
                                faces2zzzzzz.append([fad498,fbd498,fcd498])
                                faces2zzzzzz.append([fad499,fbd499,fcd499])
                                faces2zzzzzz.append([fad500,fbd500,fcd500])
                                faces2zzzzzz.append([fad501,fbd501,fcd501])
                                faces2zzzzzz.append([fad502,fbd502,fcd502])
                                faces2zzzzzz.append([fad503,fbd503,fcd503])
                                faces2zzzzzz.append([fad504,fbd504,fcd504])
                                faces2zzzzzz.append([fad505,fbd505,fcd505])
                                faces2zzzzzz.append([fad506,fbd506,fcd506])
                                faces2zzzzzz.append([fad507,fbd507,fcd507])
                                faces2zzzzzz.append([fad508,fbd508,fcd508])
                                faces2zzzzzz.append([fad509,fbd509,fcd509])
                                faces2zzzzzz.append([fad510,fbd510,fcd510])
                                faces2zzzzzz.append([fad511,fbd511,fcd511])
                                faces2zzzzzz.append([fad512,fbd512,fcd512])
                                faces2zzzzzz.append([fad513,fbd513,fcd513])
                                faces2zzzzzz.append([fad514,fbd514,fcd514])
                                faces2zzzzzz.append([fad515,fbd515,fcd515])
                                faces2zzzzzz.append([fad516,fbd516,fcd516])
                                faces2zzzzzz.append([fad517,fbd517,fcd517])
                                faces2zzzzzz.append([fad518,fbd518,fcd518])
                                faces2zzzzzz.append([fad519,fbd519,fcd519])
                                faces2zzzzzz.append([fad520,fbd520,fcd520])
                                faces2zzzzzz.append([fad521,fbd521,fcd521])
                                faces2zzzzzz.append([fad522,fbd522,fcd522])
                                faces2zzzzzz.append([fad523,fbd523,fcd523])
                                faces2zzzzzz.append([fad524,fbd524,fcd524])
                                faces2zzzzzz.append([fad525,fbd525,fcd525])
                                faces2zzzzzz.append([fad526,fbd526,fcd526])
                                faces2zzzzzz.append([fad527,fbd527,fcd527])

                        elif vertexCount == 35:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx33 = unpack("<h", f.read(2))[0] / 4096
                                uvy33 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzz.append([uvx33,-uvy33])
                            for i in range(vertexCount-34):
                                fad528+=1*35
                                fbd528+=1*35
                                fcd528+=1*35
                                fad529+=1*35
                                fbd529+=1*35
                                fcd529+=1*35
                                fad530+=1*35
                                fbd530+=1*35
                                fcd530+=1*35
                                fad531+=1*35
                                fbd531+=1*35
                                fcd531+=1*35
                                fad532+=1*35
                                fbd532+=1*35
                                fcd532+=1*35
                                fad533+=1*35
                                fbd533+=1*35
                                fcd533+=1*35
                                fad534+=1*35
                                fbd534+=1*35
                                fcd534+=1*35
                                fad535+=1*35
                                fbd535+=1*35
                                fcd535+=1*35
                                fad536+=1*35
                                fbd536+=1*35
                                fcd536+=1*35
                                fad537+=1*35
                                fbd537+=1*35
                                fcd537+=1*35
                                fad538+=1*35
                                fbd538+=1*35
                                fcd538+=1*35
                                fad539+=1*35
                                fbd539+=1*35
                                fcd539+=1*35
                                fad540+=1*35
                                fbd540+=1*35
                                fcd540+=1*35
                                fad541+=1*35
                                fbd541+=1*35
                                fcd541+=1*35
                                fad542+=1*35
                                fbd542+=1*35
                                fcd542+=1*35
                                fad543+=1*35
                                fbd543+=1*35
                                fcd543+=1*35
                                fad544+=1*35
                                fbd544+=1*35
                                fcd544+=1*35
                                fad545+=1*35
                                fbd545+=1*35
                                fcd545+=1*35
                                fad546+=1*35
                                fbd546+=1*35
                                fcd546+=1*35
                                fad547+=1*35
                                fbd547+=1*35
                                fcd547+=1*35
                                fad548+=1*35
                                fbd548+=1*35
                                fcd548+=1*35
                                fad549+=1*35
                                fbd549+=1*35
                                fcd549+=1*35
                                fad550+=1*35
                                fbd550+=1*35
                                fcd550+=1*35
                                fad551+=1*35
                                fbd551+=1*35
                                fcd551+=1*35
                                fad552+=1*35
                                fbd552+=1*35
                                fcd552+=1*35
                                fad553+=1*35
                                fbd553+=1*35
                                fcd553+=1*35
                                fad554+=1*35
                                fbd554+=1*35
                                fcd554+=1*35
                                fad555+=1*35
                                fbd555+=1*35
                                fcd555+=1*35
                                fad556+=1*35
                                fbd556+=1*35
                                fcd556+=1*35
                                fad557+=1*35
                                fbd557+=1*35
                                fcd557+=1*35
                                fad558+=1*35
                                fbd558+=1*35
                                fcd558+=1*35
                                fad559+=1*35
                                fbd559+=1*35
                                fcd559+=1*35
                                fad560+=1*35
                                fbd560+=1*35
                                fcd560+=1*35
                                faces2zzzzzzz.append([fad528,fbd528,fcd528])
                                faces2zzzzzzz.append([fad529,fbd529,fcd529])
                                faces2zzzzzzz.append([fad530,fbd530,fcd530])
                                faces2zzzzzzz.append([fad531,fbd531,fcd531])
                                faces2zzzzzzz.append([fad532,fbd532,fcd532])
                                faces2zzzzzzz.append([fad533,fbd533,fcd533])
                                faces2zzzzzzz.append([fad534,fbd534,fcd534])
                                faces2zzzzzzz.append([fad535,fbd535,fcd535])
                                faces2zzzzzzz.append([fad536,fbd536,fcd536])
                                faces2zzzzzzz.append([fad537,fbd537,fcd537])
                                faces2zzzzzzz.append([fad538,fbd538,fcd538])
                                faces2zzzzzzz.append([fad539,fbd539,fcd539])
                                faces2zzzzzzz.append([fad540,fbd540,fcd540])
                                faces2zzzzzzz.append([fad541,fbd541,fcd541])
                                faces2zzzzzzz.append([fad542,fbd542,fcd542])
                                faces2zzzzzzz.append([fad543,fbd543,fcd543])
                                faces2zzzzzzz.append([fad544,fbd544,fcd544])
                                faces2zzzzzzz.append([fad545,fbd545,fcd545])
                                faces2zzzzzzz.append([fad546,fbd546,fcd546])
                                faces2zzzzzzz.append([fad547,fbd547,fcd547])
                                faces2zzzzzzz.append([fad548,fbd548,fcd548])
                                faces2zzzzzzz.append([fad549,fbd549,fcd549])
                                faces2zzzzzzz.append([fad550,fbd550,fcd550])
                                faces2zzzzzzz.append([fad551,fbd551,fcd551])
                                faces2zzzzzzz.append([fad552,fbd552,fcd552])
                                faces2zzzzzzz.append([fad553,fbd553,fcd553])
                                faces2zzzzzzz.append([fad554,fbd554,fcd554])
                                faces2zzzzzzz.append([fad555,fbd555,fcd555])
                                faces2zzzzzzz.append([fad556,fbd556,fcd556])
                                faces2zzzzzzz.append([fad557,fbd557,fcd557])
                                faces2zzzzzzz.append([fad558,fbd558,fcd558])
                                faces2zzzzzzz.append([fad559,fbd559,fcd559])
                                faces2zzzzzzz.append([fad560,fbd560,fcd560])

                        elif vertexCount == 36:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx34 = unpack("<h", f.read(2))[0] / 4096
                                uvy34 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzz.append([uvx34,-uvy34])
                            for i in range(vertexCount-35):
                                fad561+=1*36
                                fbd561+=1*36
                                fcd561+=1*36
                                fad562+=1*36
                                fbd562+=1*36
                                fcd562+=1*36
                                fad563+=1*36
                                fbd563+=1*36
                                fcd563+=1*36
                                fad564+=1*36
                                fbd564+=1*36
                                fcd564+=1*36
                                fad565+=1*36
                                fbd565+=1*36
                                fcd565+=1*36
                                fad566+=1*36
                                fbd566+=1*36
                                fcd566+=1*36
                                fad567+=1*36
                                fbd567+=1*36
                                fcd567+=1*36
                                fad568+=1*36
                                fbd568+=1*36
                                fcd568+=1*36
                                fad569+=1*36
                                fbd569+=1*36
                                fcd569+=1*36
                                fad570+=1*36
                                fbd570+=1*36
                                fcd570+=1*36
                                fad571+=1*36
                                fbd571+=1*36
                                fcd571+=1*36
                                fad572+=1*36
                                fbd572+=1*36
                                fcd572+=1*36
                                fad573+=1*36
                                fbd573+=1*36
                                fcd573+=1*36
                                fad574+=1*36
                                fbd574+=1*36
                                fcd574+=1*36
                                fad575+=1*36
                                fbd575+=1*36
                                fcd575+=1*36
                                fad576+=1*36
                                fbd576+=1*36
                                fcd576+=1*36
                                fad577+=1*36
                                fbd577+=1*36
                                fcd577+=1*36
                                fad578+=1*36
                                fbd578+=1*36
                                fcd578+=1*36
                                fad579+=1*36
                                fbd579+=1*36
                                fcd579+=1*36
                                fad580+=1*36
                                fbd580+=1*36
                                fcd580+=1*36
                                fad581+=1*36
                                fbd581+=1*36
                                fcd581+=1*36
                                fad582+=1*36
                                fbd582+=1*36
                                fcd582+=1*36
                                fad583+=1*36
                                fbd583+=1*36
                                fcd583+=1*36
                                fad584+=1*36
                                fbd584+=1*36
                                fcd584+=1*36
                                fad585+=1*36
                                fbd585+=1*36
                                fcd585+=1*36
                                fad586+=1*36
                                fbd586+=1*36
                                fcd586+=1*36
                                fad587+=1*36
                                fbd587+=1*36
                                fcd587+=1*36
                                fad588+=1*36
                                fbd588+=1*36
                                fcd588+=1*36
                                fad589+=1*36
                                fbd589+=1*36
                                fcd589+=1*36
                                fad590+=1*36
                                fbd590+=1*36
                                fcd590+=1*36
                                fad591+=1*36
                                fbd591+=1*36
                                fcd591+=1*36
                                fad592+=1*36
                                fbd592+=1*36
                                fcd592+=1*36
                                fad593+=1*36
                                fbd593+=1*36
                                fcd593+=1*36
                                fad594+=1*36
                                fbd594+=1*36
                                fcd594+=1*36
                                faces2zzzzzzzz.append([fad561,fbd561,fcd561])
                                faces2zzzzzzzz.append([fad562,fbd562,fcd562])
                                faces2zzzzzzzz.append([fad563,fbd563,fcd563])
                                faces2zzzzzzzz.append([fad564,fbd564,fcd564])
                                faces2zzzzzzzz.append([fad565,fbd565,fcd565])
                                faces2zzzzzzzz.append([fad566,fbd566,fcd566])
                                faces2zzzzzzzz.append([fad567,fbd567,fcd567])
                                faces2zzzzzzzz.append([fad568,fbd568,fcd568])
                                faces2zzzzzzzz.append([fad569,fbd569,fcd569])
                                faces2zzzzzzzz.append([fad570,fbd570,fcd570])
                                faces2zzzzzzzz.append([fad571,fbd571,fcd571])
                                faces2zzzzzzzz.append([fad572,fbd572,fcd572])
                                faces2zzzzzzzz.append([fad573,fbd573,fcd573])
                                faces2zzzzzzzz.append([fad574,fbd574,fcd574])
                                faces2zzzzzzzz.append([fad575,fbd575,fcd575])
                                faces2zzzzzzzz.append([fad576,fbd576,fcd576])
                                faces2zzzzzzzz.append([fad577,fbd577,fcd577])
                                faces2zzzzzzzz.append([fad578,fbd578,fcd578])
                                faces2zzzzzzzz.append([fad579,fbd579,fcd579])
                                faces2zzzzzzzz.append([fad580,fbd580,fcd580])
                                faces2zzzzzzzz.append([fad581,fbd581,fcd581])
                                faces2zzzzzzzz.append([fad582,fbd582,fcd582])
                                faces2zzzzzzzz.append([fad583,fbd583,fcd583])
                                faces2zzzzzzzz.append([fad584,fbd584,fcd584])
                                faces2zzzzzzzz.append([fad585,fbd585,fcd585])
                                faces2zzzzzzzz.append([fad586,fbd586,fcd586])
                                faces2zzzzzzzz.append([fad587,fbd587,fcd587])
                                faces2zzzzzzzz.append([fad588,fbd588,fcd588])
                                faces2zzzzzzzz.append([fad589,fbd589,fcd589])
                                faces2zzzzzzzz.append([fad590,fbd590,fcd590])
                                faces2zzzzzzzz.append([fad591,fbd591,fcd591])
                                faces2zzzzzzzz.append([fad592,fbd592,fcd592])
                                faces2zzzzzzzz.append([fad593,fbd593,fcd593])
                                faces2zzzzzzzz.append([fad594,fbd594,fcd594])

                        elif vertexCount == 37:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx35 = unpack("<h", f.read(2))[0] / 4096
                                uvy35 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzz.append([uvx35,-uvy35])
                            for i in range(vertexCount-36):
                                fad595+=1*37
                                fbd595+=1*37
                                fcd595+=1*37
                                fad596+=1*37
                                fbd596+=1*37
                                fcd596+=1*37
                                fad597+=1*37
                                fbd597+=1*37
                                fcd597+=1*37
                                fad598+=1*37
                                fbd598+=1*37
                                fcd598+=1*37
                                fad599+=1*37
                                fbd599+=1*37
                                fcd599+=1*37
                                fad600+=1*37
                                fbd600+=1*37
                                fcd600+=1*37
                                fad601+=1*37
                                fbd601+=1*37
                                fcd601+=1*37
                                fad602+=1*37
                                fbd602+=1*37
                                fcd602+=1*37
                                fad603+=1*37
                                fbd603+=1*37
                                fcd603+=1*37
                                fad604+=1*37
                                fbd604+=1*37
                                fcd604+=1*37
                                fad605+=1*37
                                fbd605+=1*37
                                fcd605+=1*37
                                fad606+=1*37
                                fbd606+=1*37
                                fcd606+=1*37
                                fad607+=1*37
                                fbd607+=1*37
                                fcd607+=1*37
                                fad608+=1*37
                                fbd608+=1*37
                                fcd608+=1*37
                                fad609+=1*37
                                fbd609+=1*37
                                fcd609+=1*37
                                fad610+=1*37
                                fbd610+=1*37
                                fcd610+=1*37
                                fad611+=1*37
                                fbd611+=1*37
                                fcd611+=1*37
                                fad612+=1*37
                                fbd612+=1*37
                                fcd612+=1*37
                                fad613+=1*37
                                fbd613+=1*37
                                fcd613+=1*37
                                fad614+=1*37
                                fbd614+=1*37
                                fcd614+=1*37
                                fad615+=1*37
                                fbd615+=1*37
                                fcd615+=1*37
                                fad616+=1*37
                                fbd616+=1*37
                                fcd616+=1*37
                                fad617+=1*37
                                fbd617+=1*37
                                fcd617+=1*37
                                fad618+=1*37
                                fbd618+=1*37
                                fcd618+=1*37
                                fad619+=1*37
                                fbd619+=1*37
                                fcd619+=1*37
                                fad620+=1*37
                                fbd620+=1*37
                                fcd620+=1*37
                                fad621+=1*37
                                fbd621+=1*37
                                fcd621+=1*37
                                fad622+=1*37
                                fbd622+=1*37
                                fcd622+=1*37
                                fad623+=1*37
                                fbd623+=1*37
                                fcd623+=1*37
                                fad624+=1*37
                                fbd624+=1*37
                                fcd624+=1*37
                                fad625+=1*37
                                fbd625+=1*37
                                fcd625+=1*37
                                fad626+=1*37
                                fbd626+=1*37
                                fcd626+=1*37
                                fad627+=1*37
                                fbd627+=1*37
                                fcd627+=1*37
                                fad628+=1*37
                                fbd628+=1*37
                                fcd628+=1*37
                                fad629+=1*37
                                fbd629+=1*37
                                fcd629+=1*37
                                faces2zzzzzzzzz.append([fad595,fbd595,fcd595])
                                faces2zzzzzzzzz.append([fad596,fbd596,fcd596])
                                faces2zzzzzzzzz.append([fad597,fbd597,fcd597])
                                faces2zzzzzzzzz.append([fad598,fbd598,fcd598])
                                faces2zzzzzzzzz.append([fad599,fbd599,fcd599])
                                faces2zzzzzzzzz.append([fad600,fbd600,fcd600])
                                faces2zzzzzzzzz.append([fad601,fbd601,fcd601])
                                faces2zzzzzzzzz.append([fad602,fbd602,fcd602])
                                faces2zzzzzzzzz.append([fad603,fbd603,fcd603])
                                faces2zzzzzzzzz.append([fad604,fbd604,fcd604])
                                faces2zzzzzzzzz.append([fad605,fbd605,fcd605])
                                faces2zzzzzzzzz.append([fad606,fbd606,fcd606])
                                faces2zzzzzzzzz.append([fad607,fbd607,fcd607])
                                faces2zzzzzzzzz.append([fad608,fbd608,fcd608])
                                faces2zzzzzzzzz.append([fad609,fbd609,fcd609])
                                faces2zzzzzzzzz.append([fad610,fbd610,fcd610])
                                faces2zzzzzzzzz.append([fad611,fbd611,fcd611])
                                faces2zzzzzzzzz.append([fad612,fbd612,fcd612])
                                faces2zzzzzzzzz.append([fad613,fbd613,fcd613])
                                faces2zzzzzzzzz.append([fad614,fbd614,fcd614])
                                faces2zzzzzzzzz.append([fad615,fbd615,fcd615])
                                faces2zzzzzzzzz.append([fad616,fbd616,fcd616])
                                faces2zzzzzzzzz.append([fad617,fbd617,fcd617])
                                faces2zzzzzzzzz.append([fad618,fbd618,fcd618])
                                faces2zzzzzzzzz.append([fad619,fbd619,fcd619])
                                faces2zzzzzzzzz.append([fad620,fbd620,fcd620])
                                faces2zzzzzzzzz.append([fad621,fbd621,fcd621])
                                faces2zzzzzzzzz.append([fad622,fbd622,fcd622])
                                faces2zzzzzzzzz.append([fad623,fbd623,fcd623])
                                faces2zzzzzzzzz.append([fad624,fbd624,fcd624])
                                faces2zzzzzzzzz.append([fad625,fbd625,fcd625])
                                faces2zzzzzzzzz.append([fad626,fbd626,fcd626])
                                faces2zzzzzzzzz.append([fad627,fbd627,fcd627])
                                faces2zzzzzzzzz.append([fad628,fbd628,fcd628])
                                faces2zzzzzzzzz.append([fad629,fbd629,fcd629])

                        elif vertexCount == 38:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx36 = unpack("<h", f.read(2))[0] / 4096
                                uvy36 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzzz.append([uvx36,-uvy36])
                            for i in range(vertexCount-37):
                                fad630+=1*38
                                fbd630+=1*38
                                fcd630+=1*38
                                fad631+=1*38
                                fbd631+=1*38
                                fcd631+=1*38
                                fad632+=1*38
                                fbd632+=1*38
                                fcd632+=1*38
                                fad633+=1*38
                                fbd633+=1*38
                                fcd633+=1*38
                                fad634+=1*38
                                fbd634+=1*38
                                fcd634+=1*38
                                fad635+=1*38
                                fbd635+=1*38
                                fcd635+=1*38
                                fad636+=1*38
                                fbd636+=1*38
                                fcd636+=1*38
                                fad637+=1*38
                                fbd637+=1*38
                                fcd637+=1*38
                                fad638+=1*38
                                fbd638+=1*38
                                fcd638+=1*38
                                fad639+=1*38
                                fbd639+=1*38
                                fcd639+=1*38
                                fad640+=1*38
                                fbd640+=1*38
                                fcd640+=1*38
                                fad641+=1*38
                                fbd641+=1*38
                                fcd641+=1*38
                                fad642+=1*38
                                fbd642+=1*38
                                fcd642+=1*38
                                fad643+=1*38
                                fbd643+=1*38
                                fcd643+=1*38
                                fad644+=1*38
                                fbd644+=1*38
                                fcd644+=1*38
                                fad645+=1*38
                                fbd645+=1*38
                                fcd645+=1*38
                                fad646+=1*38
                                fbd646+=1*38
                                fcd646+=1*38
                                fad647+=1*38
                                fbd647+=1*38
                                fcd647+=1*38
                                fad648+=1*38
                                fbd648+=1*38
                                fcd648+=1*38
                                fad649+=1*38
                                fbd649+=1*38
                                fcd649+=1*38
                                fad650+=1*38
                                fbd650+=1*38
                                fcd650+=1*38
                                fad651+=1*38
                                fbd651+=1*38
                                fcd651+=1*38
                                fad652+=1*38
                                fbd652+=1*38
                                fcd652+=1*38
                                fad653+=1*38
                                fbd653+=1*38
                                fcd653+=1*38
                                fad654+=1*38
                                fbd654+=1*38
                                fcd654+=1*38
                                fad655+=1*38
                                fbd655+=1*38
                                fcd655+=1*38
                                fad656+=1*38
                                fbd656+=1*38
                                fcd656+=1*38
                                fad657+=1*38
                                fbd657+=1*38
                                fcd657+=1*38
                                fad658+=1*38
                                fbd658+=1*38
                                fcd658+=1*38
                                fad659+=1*38
                                fbd659+=1*38
                                fcd659+=1*38
                                fad660+=1*38
                                fbd660+=1*38
                                fcd660+=1*38
                                fad661+=1*38
                                fbd661+=1*38
                                fcd661+=1*38
                                fad662+=1*38
                                fbd662+=1*38
                                fcd662+=1*38
                                fad663+=1*38
                                fbd663+=1*38
                                fcd663+=1*38
                                fad664+=1*38
                                fbd664+=1*38
                                fcd664+=1*38
                                fad665+=1*38
                                fbd665+=1*38
                                fcd665+=1*38
                                faces2zzzzzzzzzz.append([fad630,fbd630,fcd630])
                                faces2zzzzzzzzzz.append([fad631,fbd631,fcd631])
                                faces2zzzzzzzzzz.append([fad632,fbd632,fcd632])
                                faces2zzzzzzzzzz.append([fad633,fbd633,fcd633])
                                faces2zzzzzzzzzz.append([fad634,fbd634,fcd634])
                                faces2zzzzzzzzzz.append([fad635,fbd635,fcd635])
                                faces2zzzzzzzzzz.append([fad636,fbd636,fcd636])
                                faces2zzzzzzzzzz.append([fad637,fbd637,fcd637])
                                faces2zzzzzzzzzz.append([fad638,fbd638,fcd638])
                                faces2zzzzzzzzzz.append([fad639,fbd639,fcd639])
                                faces2zzzzzzzzzz.append([fad640,fbd640,fcd640])
                                faces2zzzzzzzzzz.append([fad641,fbd641,fcd641])
                                faces2zzzzzzzzzz.append([fad642,fbd642,fcd642])
                                faces2zzzzzzzzzz.append([fad643,fbd643,fcd643])
                                faces2zzzzzzzzzz.append([fad644,fbd644,fcd644])
                                faces2zzzzzzzzzz.append([fad645,fbd645,fcd645])
                                faces2zzzzzzzzzz.append([fad646,fbd646,fcd646])
                                faces2zzzzzzzzzz.append([fad647,fbd647,fcd647])
                                faces2zzzzzzzzzz.append([fad648,fbd648,fcd648])
                                faces2zzzzzzzzzz.append([fad649,fbd649,fcd649])
                                faces2zzzzzzzzzz.append([fad650,fbd650,fcd650])
                                faces2zzzzzzzzzz.append([fad651,fbd651,fcd651])
                                faces2zzzzzzzzzz.append([fad652,fbd652,fcd652])
                                faces2zzzzzzzzzz.append([fad653,fbd653,fcd653])
                                faces2zzzzzzzzzz.append([fad654,fbd654,fcd654])
                                faces2zzzzzzzzzz.append([fad655,fbd655,fcd655])
                                faces2zzzzzzzzzz.append([fad656,fbd656,fcd656])
                                faces2zzzzzzzzzz.append([fad657,fbd657,fcd657])
                                faces2zzzzzzzzzz.append([fad658,fbd658,fcd658])
                                faces2zzzzzzzzzz.append([fad659,fbd659,fcd659])
                                faces2zzzzzzzzzz.append([fad660,fbd660,fcd660])
                                faces2zzzzzzzzzz.append([fad661,fbd661,fcd661])
                                faces2zzzzzzzzzz.append([fad662,fbd662,fcd662])
                                faces2zzzzzzzzzz.append([fad663,fbd663,fcd663])
                                faces2zzzzzzzzzz.append([fad664,fbd664,fcd664])
                                faces2zzzzzzzzzz.append([fad665,fbd665,fcd665])
                        elif vertexCount == 39:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx37 = unpack("<h", f.read(2))[0] / 4096
                                uvy37 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzzzz.append([uvx37,-uvy37])
                            for i in range(vertexCount-38):
                                fad666+=1*39
                                fbd666+=1*39
                                fcd666+=1*39
                                fad667+=1*39
                                fbd667+=1*39
                                fcd667+=1*39
                                fad668+=1*39
                                fbd668+=1*39
                                fcd668+=1*39
                                fad669+=1*39
                                fbd669+=1*39
                                fcd669+=1*39
                                fad670+=1*39
                                fbd670+=1*39
                                fcd670+=1*39
                                fad671+=1*39
                                fbd671+=1*39
                                fcd671+=1*39
                                fad672+=1*39
                                fbd672+=1*39
                                fcd672+=1*39
                                fad673+=1*39
                                fbd673+=1*39
                                fcd673+=1*39
                                fad674+=1*39
                                fbd674+=1*39
                                fcd674+=1*39
                                fad675+=1*39
                                fbd675+=1*39
                                fcd675+=1*39
                                fad676+=1*39
                                fbd676+=1*39
                                fcd676+=1*39
                                fad677+=1*39
                                fbd677+=1*39
                                fcd677+=1*39
                                fad678+=1*39
                                fbd678+=1*39
                                fcd678+=1*39
                                fad679+=1*39
                                fbd679+=1*39
                                fcd679+=1*39
                                fad680+=1*39
                                fbd680+=1*39
                                fcd680+=1*39
                                fad681+=1*39
                                fbd681+=1*39
                                fcd681+=1*39
                                fad682+=1*39
                                fbd682+=1*39
                                fcd682+=1*39
                                fad683+=1*39
                                fbd683+=1*39
                                fcd683+=1*39
                                fad684+=1*39
                                fbd684+=1*39
                                fcd684+=1*39
                                fad685+=1*39
                                fbd685+=1*39
                                fcd685+=1*39
                                fad686+=1*39
                                fbd686+=1*39
                                fcd686+=1*39
                                fad687+=1*39
                                fbd687+=1*39
                                fcd687+=1*39
                                fad688+=1*39
                                fbd688+=1*39
                                fcd688+=1*39
                                fad689+=1*39
                                fbd689+=1*39
                                fcd689+=1*39
                                fad690+=1*39
                                fbd690+=1*39
                                fcd690+=1*39
                                fad691+=1*39
                                fbd691+=1*39
                                fcd691+=1*39
                                fad692+=1*39
                                fbd692+=1*39
                                fcd692+=1*39
                                fad693+=1*39
                                fbd693+=1*39
                                fcd693+=1*39
                                fad694+=1*39
                                fbd694+=1*39
                                fcd694+=1*39
                                fad695+=1*39
                                fbd695+=1*39
                                fcd695+=1*39
                                fad696+=1*39
                                fbd696+=1*39
                                fcd696+=1*39
                                fad697+=1*39
                                fbd697+=1*39
                                fcd697+=1*39
                                fad698+=1*39
                                fbd698+=1*39
                                fcd698+=1*39
                                fad699+=1*39
                                fbd699+=1*39
                                fcd699+=1*39
                                fad700+=1*39
                                fbd700+=1*39
                                fcd700+=1*39
                                fad701+=1*39
                                fbd701+=1*39
                                fcd701+=1*39
                                fad702+=1*39
                                fbd702+=1*39
                                fcd702+=1*39
                                faces2zzzzzzzzzzz.append([fad666,fbd666,fcd666])
                                faces2zzzzzzzzzzz.append([fad667,fbd667,fcd667])
                                faces2zzzzzzzzzzz.append([fad668,fbd668,fcd668])
                                faces2zzzzzzzzzzz.append([fad669,fbd669,fcd669])
                                faces2zzzzzzzzzzz.append([fad670,fbd670,fcd670])
                                faces2zzzzzzzzzzz.append([fad671,fbd671,fcd671])
                                faces2zzzzzzzzzzz.append([fad672,fbd672,fcd672])
                                faces2zzzzzzzzzzz.append([fad673,fbd673,fcd673])
                                faces2zzzzzzzzzzz.append([fad674,fbd674,fcd674])
                                faces2zzzzzzzzzzz.append([fad675,fbd675,fcd675])
                                faces2zzzzzzzzzzz.append([fad676,fbd676,fcd676])
                                faces2zzzzzzzzzzz.append([fad677,fbd677,fcd677])
                                faces2zzzzzzzzzzz.append([fad678,fbd678,fcd678])
                                faces2zzzzzzzzzzz.append([fad679,fbd679,fcd679])
                                faces2zzzzzzzzzzz.append([fad680,fbd680,fcd680])
                                faces2zzzzzzzzzzz.append([fad681,fbd681,fcd681])
                                faces2zzzzzzzzzzz.append([fad682,fbd682,fcd682])
                                faces2zzzzzzzzzzz.append([fad683,fbd683,fcd683])
                                faces2zzzzzzzzzzz.append([fad684,fbd684,fcd684])
                                faces2zzzzzzzzzzz.append([fad685,fbd685,fcd685])
                                faces2zzzzzzzzzzz.append([fad686,fbd686,fcd686])
                                faces2zzzzzzzzzzz.append([fad687,fbd687,fcd687])
                                faces2zzzzzzzzzzz.append([fad688,fbd688,fcd688])
                                faces2zzzzzzzzzzz.append([fad689,fbd689,fcd689])
                                faces2zzzzzzzzzzz.append([fad690,fbd690,fcd690])
                                faces2zzzzzzzzzzz.append([fad691,fbd691,fcd691])
                                faces2zzzzzzzzzzz.append([fad692,fbd692,fcd692])
                                faces2zzzzzzzzzzz.append([fad693,fbd693,fcd693])
                                faces2zzzzzzzzzzz.append([fad694,fbd694,fcd694])
                                faces2zzzzzzzzzzz.append([fad695,fbd695,fcd695])
                                faces2zzzzzzzzzzz.append([fad696,fbd696,fcd696])
                                faces2zzzzzzzzzzz.append([fad697,fbd697,fcd697])
                                faces2zzzzzzzzzzz.append([fad698,fbd698,fcd698])
                                faces2zzzzzzzzzzz.append([fad699,fbd699,fcd699])
                                faces2zzzzzzzzzzz.append([fad700,fbd700,fcd700])
                                faces2zzzzzzzzzzz.append([fad701,fbd701,fcd701])
                                faces2zzzzzzzzzzz.append([fad702,fbd702,fcd702])
                        elif vertexCount == 40:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx38 = unpack("<h", f.read(2))[0] / 4096
                                uvy38 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzzzzz.append([uvx38,-uvy38])
                            for i in range(vertexCount-39):
                                fad703+=1*40
                                fbd703+=1*40
                                fcd703+=1*40
                                fad704+=1*40
                                fbd704+=1*40
                                fcd704+=1*40
                                fad705+=1*40
                                fbd705+=1*40
                                fcd705+=1*40
                                fad706+=1*40
                                fbd706+=1*40
                                fcd706+=1*40
                                fad707+=1*40
                                fbd707+=1*40
                                fcd707+=1*40
                                fad708+=1*40
                                fbd708+=1*40
                                fcd708+=1*40
                                fad709+=1*40
                                fbd709+=1*40
                                fcd709+=1*40
                                fad710+=1*40
                                fbd710+=1*40
                                fcd710+=1*40
                                fad711+=1*40
                                fbd711+=1*40
                                fcd711+=1*40
                                fad712+=1*40
                                fbd712+=1*40
                                fcd712+=1*40
                                fad713+=1*40
                                fbd713+=1*40
                                fcd713+=1*40
                                fad714+=1*40
                                fbd714+=1*40
                                fcd714+=1*40
                                fad715+=1*40
                                fbd715+=1*40
                                fcd715+=1*40
                                fad716+=1*40
                                fbd716+=1*40
                                fcd716+=1*40
                                fad717+=1*40
                                fbd717+=1*40
                                fcd717+=1*40
                                fad718+=1*40
                                fbd718+=1*40
                                fcd718+=1*40
                                fad719+=1*40
                                fbd719+=1*40
                                fcd719+=1*40
                                fad720+=1*40
                                fbd720+=1*40
                                fcd720+=1*40
                                fad721+=1*40
                                fbd721+=1*40
                                fcd721+=1*40
                                fad722+=1*40
                                fbd722+=1*40
                                fcd722+=1*40
                                fad723+=1*40
                                fbd723+=1*40
                                fcd723+=1*40
                                fad724+=1*40
                                fbd724+=1*40
                                fcd724+=1*40
                                fad725+=1*40
                                fbd725+=1*40
                                fcd725+=1*40
                                fad726+=1*40
                                fbd726+=1*40
                                fcd726+=1*40
                                fad727+=1*40
                                fbd727+=1*40
                                fcd727+=1*40
                                fad728+=1*40
                                fbd728+=1*40
                                fcd728+=1*40
                                fad729+=1*40
                                fbd729+=1*40
                                fcd729+=1*40
                                fad730+=1*40
                                fbd730+=1*40
                                fcd730+=1*40
                                fad731+=1*40
                                fbd731+=1*40
                                fcd731+=1*40
                                fad732+=1*40
                                fbd732+=1*40
                                fcd732+=1*40
                                fad733+=1*40
                                fbd733+=1*40
                                fcd733+=1*40
                                fad734+=1*40
                                fbd734+=1*40
                                fcd734+=1*40
                                fad735+=1*40
                                fbd735+=1*40
                                fcd735+=1*40
                                fad736+=1*40
                                fbd736+=1*40
                                fcd736+=1*40
                                fad737+=1*40
                                fbd737+=1*40
                                fcd737+=1*40
                                fad738+=1*40
                                fbd738+=1*40
                                fcd738+=1*40
                                fad739+=1*40
                                fbd739+=1*40
                                fcd739+=1*40
                                fad740+=1*40
                                fbd740+=1*40
                                fcd740+=1*40
                                faces2zzzzzzzzzzzz.append([fad703,fbd703,fcd703])
                                faces2zzzzzzzzzzzz.append([fad704,fbd704,fcd704])
                                faces2zzzzzzzzzzzz.append([fad705,fbd705,fcd705])
                                faces2zzzzzzzzzzzz.append([fad706,fbd706,fcd706])
                                faces2zzzzzzzzzzzz.append([fad707,fbd707,fcd707])
                                faces2zzzzzzzzzzzz.append([fad708,fbd708,fcd708])
                                faces2zzzzzzzzzzzz.append([fad709,fbd709,fcd709])
                                faces2zzzzzzzzzzzz.append([fad710,fbd710,fcd710])
                                faces2zzzzzzzzzzzz.append([fad711,fbd711,fcd711])
                                faces2zzzzzzzzzzzz.append([fad712,fbd712,fcd712])
                                faces2zzzzzzzzzzzz.append([fad713,fbd713,fcd713])
                                faces2zzzzzzzzzzzz.append([fad714,fbd714,fcd714])
                                faces2zzzzzzzzzzzz.append([fad715,fbd715,fcd715])
                                faces2zzzzzzzzzzzz.append([fad716,fbd716,fcd716])
                                faces2zzzzzzzzzzzz.append([fad717,fbd717,fcd717])
                                faces2zzzzzzzzzzzz.append([fad718,fbd718,fcd718])
                                faces2zzzzzzzzzzzz.append([fad719,fbd719,fcd719])
                                faces2zzzzzzzzzzzz.append([fad720,fbd720,fcd720])
                                faces2zzzzzzzzzzzz.append([fad721,fbd721,fcd721])
                                faces2zzzzzzzzzzzz.append([fad722,fbd722,fcd722])
                                faces2zzzzzzzzzzzz.append([fad723,fbd723,fcd723])
                                faces2zzzzzzzzzzzz.append([fad724,fbd724,fcd724])
                                faces2zzzzzzzzzzzz.append([fad725,fbd725,fcd725])
                                faces2zzzzzzzzzzzz.append([fad726,fbd726,fcd726])
                                faces2zzzzzzzzzzzz.append([fad727,fbd727,fcd727])
                                faces2zzzzzzzzzzzz.append([fad728,fbd728,fcd728])
                                faces2zzzzzzzzzzzz.append([fad729,fbd729,fcd729])
                                faces2zzzzzzzzzzzz.append([fad730,fbd730,fcd730])
                                faces2zzzzzzzzzzzz.append([fad731,fbd731,fcd731])
                                faces2zzzzzzzzzzzz.append([fad732,fbd732,fcd732])
                                faces2zzzzzzzzzzzz.append([fad733,fbd733,fcd733])
                                faces2zzzzzzzzzzzz.append([fad734,fbd734,fcd734])
                                faces2zzzzzzzzzzzz.append([fad735,fbd735,fcd735])
                                faces2zzzzzzzzzzzz.append([fad736,fbd736,fcd736])
                                faces2zzzzzzzzzzzz.append([fad737,fbd737,fcd737])
                                faces2zzzzzzzzzzzz.append([fad738,fbd738,fcd738])
                                faces2zzzzzzzzzzzz.append([fad739,fbd739,fcd739])
                                faces2zzzzzzzzzzzz.append([fad740,fbd740,fcd740])

                        elif vertexCount == 41:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx39 = unpack("<h", f.read(2))[0] / 4096
                                uvy39 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzzzzzz.append([uvx39,-uvy39])
                            for i in range(vertexCount-40):
                                fad741+=1*41
                                fbd741+=1*41
                                fcd741+=1*41
                                fad742+=1*41
                                fbd742+=1*41
                                fcd742+=1*41
                                fad743+=1*41
                                fbd743+=1*41
                                fcd743+=1*41
                                fad744+=1*41
                                fbd744+=1*41
                                fcd744+=1*41
                                fad745+=1*41
                                fbd745+=1*41
                                fcd745+=1*41
                                fad746+=1*41
                                fbd746+=1*41
                                fcd746+=1*41
                                fad747+=1*41
                                fbd747+=1*41
                                fcd747+=1*41
                                fad748+=1*41
                                fbd748+=1*41
                                fcd748+=1*41
                                fad749+=1*41
                                fbd749+=1*41
                                fcd749+=1*41
                                fad750+=1*41
                                fbd750+=1*41
                                fcd750+=1*41
                                fad751+=1*41
                                fbd751+=1*41
                                fcd751+=1*41
                                fad752+=1*41
                                fbd752+=1*41
                                fcd752+=1*41
                                fad753+=1*41
                                fbd753+=1*41
                                fcd753+=1*41
                                fad754+=1*41
                                fbd754+=1*41
                                fcd754+=1*41
                                fad755+=1*41
                                fbd755+=1*41
                                fcd755+=1*41
                                fad756+=1*41
                                fbd756+=1*41
                                fcd756+=1*41
                                fad757+=1*41
                                fbd757+=1*41
                                fcd757+=1*41
                                fad758+=1*41
                                fbd758+=1*41
                                fcd758+=1*41
                                fad759+=1*41
                                fbd759+=1*41
                                fcd759+=1*41
                                fad760+=1*41
                                fbd760+=1*41
                                fcd760+=1*41
                                fad761+=1*41
                                fbd761+=1*41
                                fcd761+=1*41
                                fad762+=1*41
                                fbd762+=1*41
                                fcd762+=1*41
                                fad763+=1*41
                                fbd763+=1*41
                                fcd763+=1*41
                                fad764+=1*41
                                fbd764+=1*41
                                fcd764+=1*41
                                fad765+=1*41
                                fbd765+=1*41
                                fcd765+=1*41
                                fad766+=1*41
                                fbd766+=1*41
                                fcd766+=1*41
                                fad767+=1*41
                                fbd767+=1*41
                                fcd767+=1*41
                                fad768+=1*41
                                fbd768+=1*41
                                fcd768+=1*41
                                fad769+=1*41
                                fbd769+=1*41
                                fcd769+=1*41
                                fad770+=1*41
                                fbd770+=1*41
                                fcd770+=1*41
                                fad771+=1*41
                                fbd771+=1*41
                                fcd771+=1*41
                                fad772+=1*41
                                fbd772+=1*41
                                fcd772+=1*41
                                fad773+=1*41
                                fbd773+=1*41
                                fcd773+=1*41
                                fad774+=1*41
                                fbd774+=1*41
                                fcd774+=1*41
                                fad775+=1*41
                                fbd775+=1*41
                                fcd775+=1*41
                                fad776+=1*41
                                fbd776+=1*41
                                fcd776+=1*41
                                fad777+=1*41
                                fbd777+=1*41
                                fcd777+=1*41
                                fad778+=1*41
                                fbd778+=1*41
                                fcd778+=1*41
                                fad779+=1*41
                                fbd779+=1*41
                                fcd779+=1*41
                                faces2zzzzzzzzzzzzz.append([fad741,fbd741,fcd741])
                                faces2zzzzzzzzzzzzz.append([fad742,fbd742,fcd742])
                                faces2zzzzzzzzzzzzz.append([fad743,fbd743,fcd743])
                                faces2zzzzzzzzzzzzz.append([fad744,fbd744,fcd744])
                                faces2zzzzzzzzzzzzz.append([fad745,fbd745,fcd745])
                                faces2zzzzzzzzzzzzz.append([fad746,fbd746,fcd746])
                                faces2zzzzzzzzzzzzz.append([fad747,fbd747,fcd747])
                                faces2zzzzzzzzzzzzz.append([fad748,fbd748,fcd748])
                                faces2zzzzzzzzzzzzz.append([fad749,fbd749,fcd749])
                                faces2zzzzzzzzzzzzz.append([fad750,fbd750,fcd750])
                                faces2zzzzzzzzzzzzz.append([fad751,fbd751,fcd751])
                                faces2zzzzzzzzzzzzz.append([fad752,fbd752,fcd752])
                                faces2zzzzzzzzzzzzz.append([fad753,fbd753,fcd753])
                                faces2zzzzzzzzzzzzz.append([fad754,fbd754,fcd754])
                                faces2zzzzzzzzzzzzz.append([fad755,fbd755,fcd755])
                                faces2zzzzzzzzzzzzz.append([fad756,fbd756,fcd756])
                                faces2zzzzzzzzzzzzz.append([fad757,fbd757,fcd757])
                                faces2zzzzzzzzzzzzz.append([fad758,fbd758,fcd758])
                                faces2zzzzzzzzzzzzz.append([fad759,fbd759,fcd759])
                                faces2zzzzzzzzzzzzz.append([fad760,fbd760,fcd760])
                                faces2zzzzzzzzzzzzz.append([fad761,fbd761,fcd761])
                                faces2zzzzzzzzzzzzz.append([fad762,fbd762,fcd762])
                                faces2zzzzzzzzzzzzz.append([fad763,fbd763,fcd763])
                                faces2zzzzzzzzzzzzz.append([fad764,fbd764,fcd764])
                                faces2zzzzzzzzzzzzz.append([fad765,fbd765,fcd765])
                                faces2zzzzzzzzzzzzz.append([fad766,fbd766,fcd766])
                                faces2zzzzzzzzzzzzz.append([fad767,fbd767,fcd767])
                                faces2zzzzzzzzzzzzz.append([fad768,fbd768,fcd768])
                                faces2zzzzzzzzzzzzz.append([fad769,fbd769,fcd769])
                                faces2zzzzzzzzzzzzz.append([fad770,fbd770,fcd770])
                                faces2zzzzzzzzzzzzz.append([fad771,fbd771,fcd771])
                                faces2zzzzzzzzzzzzz.append([fad772,fbd772,fcd772])
                                faces2zzzzzzzzzzzzz.append([fad773,fbd773,fcd773])
                                faces2zzzzzzzzzzzzz.append([fad774,fbd774,fcd774])
                                faces2zzzzzzzzzzzzz.append([fad775,fbd775,fcd775])
                                faces2zzzzzzzzzzzzz.append([fad776,fbd776,fcd776])
                                faces2zzzzzzzzzzzzz.append([fad777,fbd777,fcd777])
                                faces2zzzzzzzzzzzzz.append([fad778,fbd778,fcd778])
                                faces2zzzzzzzzzzzzz.append([fad779,fbd779,fcd779])

                        elif vertexCount == 42:
                            for i in range(vertexCount):
                                vx = unpack("<h", f.read(2))[0] / 4096
                                vy = unpack("<h", f.read(2))[0] / 4096
                                vz = unpack("<h", f.read(2))[0] / 4096
                                f.seek(2,1)
                                uvx40 = unpack("<h", f.read(2))[0] / 4096
                                uvy40 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                vertices2zzzzzzzzzzzzzz.append([vx,vz,vy])
                                uvs2zzzzzzzzzzzzzz.append([uvx40,-uvy40])
                            for i in range(vertexCount-41):
                                fad780+=1*42
                                fbd780+=1*42
                                fcd780+=1*42
                                fad781+=1*42
                                fbd781+=1*42
                                fcd781+=1*42
                                fad782+=1*42
                                fbd782+=1*42
                                fcd782+=1*42
                                fad783+=1*42
                                fbd783+=1*42
                                fcd783+=1*42
                                fad784+=1*42
                                fbd784+=1*42
                                fcd784+=1*42
                                fad785+=1*42
                                fbd785+=1*42
                                fcd785+=1*42
                                fad786+=1*42
                                fbd786+=1*42
                                fcd786+=1*42
                                fad787+=1*42
                                fbd787+=1*42
                                fcd787+=1*42
                                fad788+=1*42
                                fbd788+=1*42
                                fcd788+=1*42
                                fad789+=1*42
                                fbd789+=1*42
                                fcd789+=1*42
                                fad790+=1*42
                                fbd790+=1*42
                                fcd790+=1*42
                                fad791+=1*42
                                fbd791+=1*42
                                fcd791+=1*42
                                fad792+=1*42
                                fbd792+=1*42
                                fcd792+=1*42
                                fad793+=1*42
                                fbd793+=1*42
                                fcd793+=1*42
                                fad794+=1*42
                                fbd794+=1*42
                                fcd794+=1*42
                                fad795+=1*42
                                fbd795+=1*42
                                fcd795+=1*42
                                fad796+=1*42
                                fbd796+=1*42
                                fcd796+=1*42
                                fad797+=1*42
                                fbd797+=1*42
                                fcd797+=1*42
                                fad798+=1*42
                                fbd798+=1*42
                                fcd798+=1*42
                                fad799+=1*42
                                fbd799+=1*42
                                fcd799+=1*42
                                fad800+=1*42
                                fbd800+=1*42
                                fcd800+=1*42
                                fad801+=1*42
                                fbd801+=1*42
                                fcd801+=1*42
                                fad802+=1*42
                                fbd802+=1*42
                                fcd802+=1*42
                                fad803+=1*42
                                fbd803+=1*42
                                fcd803+=1*42
                                fad804+=1*42
                                fbd804+=1*42
                                fcd804+=1*42
                                fad805+=1*42
                                fbd805+=1*42
                                fcd805+=1*42
                                fad806+=1*42
                                fbd806+=1*42
                                fcd806+=1*42
                                fad807+=1*42
                                fbd807+=1*42
                                fcd807+=1*42
                                fad808+=1*42
                                fbd808+=1*42
                                fcd808+=1*42
                                fad809+=1*42
                                fbd809+=1*42
                                fcd809+=1*42
                                fad810+=1*42
                                fbd810+=1*42
                                fcd810+=1*42
                                fad811+=1*42
                                fbd811+=1*42
                                fcd811+=1*42
                                fad812+=1*42
                                fbd812+=1*42
                                fcd812+=1*42
                                fad813+=1*42
                                fbd813+=1*42
                                fcd813+=1*42
                                fad814+=1*42
                                fbd814+=1*42
                                fcd814+=1*42
                                fad815+=1*42
                                fbd815+=1*42
                                fcd815+=1*42
                                fad816+=1*42
                                fbd816+=1*42
                                fcd816+=1*42
                                fad817+=1*42
                                fbd817+=1*42
                                fcd817+=1*42
                                fad818+=1*42
                                fbd818+=1*42
                                fcd818+=1*42
                                fad819+=1*42
                                fbd819+=1*42
                                fcd819+=1*42
                                faces2zzzzzzzzzzzzzz.append([fad780,fbd780,fcd780])
                                faces2zzzzzzzzzzzzzz.append([fad781,fbd781,fcd781])
                                faces2zzzzzzzzzzzzzz.append([fad782,fbd782,fcd782])
                                faces2zzzzzzzzzzzzzz.append([fad783,fbd783,fcd783])
                                faces2zzzzzzzzzzzzzz.append([fad784,fbd784,fcd784])
                                faces2zzzzzzzzzzzzzz.append([fad785,fbd785,fcd785])
                                faces2zzzzzzzzzzzzzz.append([fad786,fbd786,fcd786])
                                faces2zzzzzzzzzzzzzz.append([fad787,fbd787,fcd787])
                                faces2zzzzzzzzzzzzzz.append([fad788,fbd788,fcd788])
                                faces2zzzzzzzzzzzzzz.append([fad789,fbd789,fcd789])
                                faces2zzzzzzzzzzzzzz.append([fad790,fbd790,fcd790])
                                faces2zzzzzzzzzzzzzz.append([fad791,fbd791,fcd791])
                                faces2zzzzzzzzzzzzzz.append([fad792,fbd792,fcd792])
                                faces2zzzzzzzzzzzzzz.append([fad793,fbd793,fcd793])
                                faces2zzzzzzzzzzzzzz.append([fad794,fbd794,fcd794])
                                faces2zzzzzzzzzzzzzz.append([fad795,fbd795,fcd795])
                                faces2zzzzzzzzzzzzzz.append([fad796,fbd796,fcd796])
                                faces2zzzzzzzzzzzzzz.append([fad797,fbd797,fcd797])
                                faces2zzzzzzzzzzzzzz.append([fad798,fbd798,fcd798])
                                faces2zzzzzzzzzzzzzz.append([fad799,fbd799,fcd799])
                                faces2zzzzzzzzzzzzzz.append([fad800,fbd800,fcd800])
                                faces2zzzzzzzzzzzzzz.append([fad801,fbd801,fcd801])
                                faces2zzzzzzzzzzzzzz.append([fad802,fbd802,fcd802])
                                faces2zzzzzzzzzzzzzz.append([fad803,fbd803,fcd803])
                                faces2zzzzzzzzzzzzzz.append([fad804,fbd804,fcd804])
                                faces2zzzzzzzzzzzzzz.append([fad805,fbd805,fcd805])
                                faces2zzzzzzzzzzzzzz.append([fad806,fbd806,fcd806])
                                faces2zzzzzzzzzzzzzz.append([fad807,fbd807,fcd807])
                                faces2zzzzzzzzzzzzzz.append([fad808,fbd808,fcd808])
                                faces2zzzzzzzzzzzzzz.append([fad809,fbd809,fcd809])
                                faces2zzzzzzzzzzzzzz.append([fad810,fbd810,fcd810])
                                faces2zzzzzzzzzzzzzz.append([fad811,fbd811,fcd811])
                                faces2zzzzzzzzzzzzzz.append([fad812,fbd812,fcd812])
                                faces2zzzzzzzzzzzzzz.append([fad813,fbd813,fcd813])
                                faces2zzzzzzzzzzzzzz.append([fad814,fbd814,fcd814])
                                faces2zzzzzzzzzzzzzz.append([fad815,fbd815,fcd815])
                                faces2zzzzzzzzzzzzzz.append([fad816,fbd816,fcd816])
                                faces2zzzzzzzzzzzzzz.append([fad817,fbd817,fcd817])
                                faces2zzzzzzzzzzzzzz.append([fad818,fbd818,fcd818])
                                faces2zzzzzzzzzzzzzz.append([fad819,fbd819,fcd819])"""
                            
                            
                            
                            
                            
                                        
                            
                        
                """elif Chunks == b"\x04\x02\x00\x01":
                    f.seek(1,1)
                    value1 = unpack("B", f.read(1))[0]
                    vertexCount = unpack("B", f.read(1))[0] // 2
                    flag2 = unpack("B", f.read(1))[0]
                    if flag2 == 0x6C:
                        if vertexCount:
                            for j in range(vertexCount):
                                
                                vx0001__ = unpack("<f", f.read(4))[0]
                                vy0001__ = unpack("<f", f.read(4))[0]
                                vz0001__ = unpack("<f", f.read(4))[0]
                                brightness1__ = unpack("<f", f.read(4))[0]
                                uvx0001__ = unpack("<f", f.read(4))[0]
                                uvy0001__ = unpack("<f", f.read(4))[0]
                                f.seek(4,1)
                                type4 = unpack("B", f.read(1))[0]==0
                                f.seek(3,1)
                                vertices3.append([vx0001__,vz0001__,vy0001__])
                                fa2+=1
                                fb2+=1
                                fc2+=1
                                if type4 > 0:
                                    faces3.append([j+j+type4-type4-1+fa2-j-j-1,j-j+type4-type4+1+fb2-2-1,j+type4-type4+fc2-j+2-4])"""

    
    
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

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

    mesh3EE = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3EE.from_pydata(vertices3EE, [], faces3EE)
    objects3EE = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3EE)
    collection.objects.link(objects3EE)

    uv_tex3EE = mesh3EE.uv_layers.new()
    uv_layer3EE = mesh3EE.uv_layers[0].data
    vert_loops3EE = {}
    for l in mesh3EE.loops:
        vert_loops3EE.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3EE):
        for li in vert_loops3EE[i]:
            uv_layer3EE[li].uv = coord

    mesh3DD = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3DD.from_pydata(vertices3DD, [], faces3DD)
    objects3DD = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3DD)
    collection.objects.link(objects3DD)

    uv_tex3DD = mesh3DD.uv_layers.new()
    uv_layer3DD = mesh3DD.uv_layers[0].data
    vert_loops3DD = {}
    for l in mesh3DD.loops:
        vert_loops3DD.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3DD):
        for li in vert_loops3DD[i]:
            uv_layer3DD[li].uv = coord

    mesh3CC = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3CC.from_pydata(vertices3CC, [], faces3CC)
    objects3CC = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3CC)
    collection.objects.link(objects3CC)

    uv_tex3CC = mesh3CC.uv_layers.new()
    uv_layer3CC = mesh3CC.uv_layers[0].data
    vert_loops3CC = {}
    for l in mesh3CC.loops:
        vert_loops3CC.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3CC):
        for li in vert_loops3CC[i]:
            uv_layer3CC[li].uv = coord

    mesh3BB = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3BB.from_pydata(vertices3BB, [], faces3BB)
    objects3BB = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3BB)
    collection.objects.link(objects3BB)

    uv_tex3BB = mesh3BB.uv_layers.new()
    uv_layer3BB = mesh3BB.uv_layers[0].data
    vert_loops3BB = {}
    for l in mesh3BB.loops:
        vert_loops3BB.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3BB):
        for li in vert_loops3BB[i]:
            uv_layer3BB[li].uv = coord

    mesh3BBd = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3BBd.from_pydata(vertices3BBd, [], faces3BBd)
    objects3BBd = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3BBd)
    collection.objects.link(objects3BBd)

    uv_tex3BBd = mesh3BBd.uv_layers.new()
    uv_layer3BBd = mesh3BBd.uv_layers[0].data
    vert_loops3BBd = {}
    for l in mesh3BBd.loops:
        vert_loops3BBd.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3BBd):
        for li in vert_loops3BBd[i]:
            uv_layer3BBd[li].uv = coord

    mesh3AAx = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3AAx.from_pydata(vertices3AAx, [], faces3AAx)
    objects3AAx = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3AAx)
    collection.objects.link(objects3AAx)

    mesh3AA = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3AA.from_pydata(vertices3AA, [], faces3AA)
    objects3AA = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3AA)
    collection.objects.link(objects3AA)

    #brightt2

    bpy.context.view_layer.objects.active = objects3AA

    colname4 = "GHG_Brightess_strip"

    colattr4 = objects3AA.data.color_attributes.new(
        name=colname4,
        type='FLOAT_COLOR',
        domain='POINT',
    )

    for v_index in range(len(objects3AA.data.vertices)):
        colattr4.data[v_index].color = brightt2[v_index]

    uv_tex3AA = mesh3AA.uv_layers.new()
    uv_layer3AA = mesh3AA.uv_layers[0].data
    vert_loops3AA = {}
    for l in mesh3AA.loops:
        vert_loops3AA.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3AA):
        for li in vert_loops3AA[i]:
            uv_layer3AA[li].uv = coord

    mesh3AApt2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3AApt2.from_pydata(vertices3AApt2, [], faces3AApt2)
    objects3AApt2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3AApt2)
    collection.objects.link(objects3AApt2)

    uv_tex3AApt2 = mesh3AApt2.uv_layers.new()
    uv_layer3AApt2 = mesh3AApt2.uv_layers[0].data
    vert_loops3AApt2 = {}
    for l in mesh3AApt2.loops:
        vert_loops3AApt2.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3AApt2):
        for li in vert_loops3AApt2[i]:
            uv_layer3AApt2[li].uv = coord

    mesh3AApt3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3AApt3.from_pydata(vertices3AApt3, [], faces3AApt3)
    objects3AApt3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3AApt3)
    collection.objects.link(objects3AApt3)

    uv_tex3AApt3 = mesh3AApt3.uv_layers.new()
    uv_layer3AApt3 = mesh3AApt3.uv_layers[0].data
    vert_loops3AApt3 = {}
    for l in mesh3AApt3.loops:
        vert_loops3AApt3.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs3AApt3):
        for li in vert_loops3AApt3[i]:
            uv_layer3AApt3[li].uv = coord


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


    objects3.parent = arma
    armamodifier3 = objects3.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3.object = arma

    vgroups3 = [objects3.vertex_groups.new(name = bone.name) for bone in arma.data.bones]

    mesh4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh4.from_pydata(vertices2, [], faces2)
    objects4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4)
    collection.objects.link(objects4)

    uv_tex_ = mesh4.uv_layers.new()
    uv_layer_ = mesh4.uv_layers[0].data
    vert_loops_ = {}
    for l in mesh4.loops:
        vert_loops_.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs2):
        for li in vert_loops_[i]:
            uv_layer_[li].uv = coord

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

    bpy.ops.mesh.separate(type='LOOSE')

    bpy.ops.object.mode_set(mode='OBJECT')

    
                        

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
    

    
        

    
            

def ghg_open(filepath, offset_on_off=False, offsets="", input_on_off=False, input_name="", bsa_on_off=False, ghg_tex_utility=False,seek_pallete=0,pallete_offsets=0):
    with open(filepath, "r+b") as f:
        if offset_on_off:
            GHG_mesh(f, filepath)
            #GHG_mesha(f, filepath)

        if bsa_on_off:
            GHG_Blend_Object(f, filepath)

        if input_on_off:
            if input_name=="eel":
                ghg_read_Eel(f, filepath)

        if ghg_tex_utility:
            if pallete_offsets == 33792:
                GHG_Texture_Utility_0x84_only(f, filepath, seek_=seek_pallete)
            if pallete_offsets == 49152:
                GHG_Texture_Utility_0xC0_only(f, filepath, seek_=seek_pallete)
            if pallete_offsets == 33536:
                GHG_Texture_Utility_0x83_only(f, filepath, seek_=seek_pallete)
            if pallete_offsets == 40960:
                GHG_Texture_Utility_0xA0_only(f, filepath, seek_=seek_pallete)
            if pallete_offsets == 33024:
                GHG_Texture_Utility_0x81_only(f, filepath, seek_=seek_pallete)
            if pallete_offsets == 36864:
                GHG_Texture_Utility_0x90_only(f, filepath, seek_=seek_pallete)
            
            
                
            
    
