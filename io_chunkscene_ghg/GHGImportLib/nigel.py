from struct import unpack, pack
import os
import math
import bpy
import mathutils
from io import BytesIO as bio

def global_nigel_():

    global vertices3
    global faces3
    global vertices3pt6a
    global faces3pt6a
    global vertices3pt5a
    global faces3pt5a
    global vertices3pt4a
    global faces3pt4a
    global vertices3pt3a
    global faces3pt3a
    global vertices3pt2a
    global faces3pt2a
    global vertices3pt2
    global faces3pt2
    global vertices3pt7a
    global faces3pt7a
    global vertices3pt8a
    global faces3pt8a
    global vertices3pt9a
    global faces3pt9a

    global fa3
    global fb3
    global fc3
    global fa3a
    global fb3a
    global fc3a
    global fd3a
    global fa3b
    global fb3b
    global fc3b
    global fd3b
    global fe3b
    global fa3c
    global fb3c
    global fc3c
    global fd3c
    global fa4c
    global fb4c
    global fc4c
    

    fa3=-3
    fb3=-2
    fc3=-1

    fa3a=-4
    fb3a=-3
    fc3a=-2
    fd3a=-1

    fa3b=-5
    fb3b=-4
    fc3b=-3
    fd3b=-2
    fe3b=-1

    fa3c=-4
    fb3c=-3
    fc3c=-2
    fd3c=-1

    fa4c=-3
    fb4c=-2
    fc4c=-1
    
    vertices3=[]
    faces3=[]

    vertices3pt9a=[]
    faces3pt9a=[]
    
    vertices3pt8a=[]
    faces3pt8a=[]
    
    vertices3pt7a=[]
    faces3pt7a=[]

    vertices3pt6a=[]
    faces3pt6a=[]

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

def nigel_(f):
    global_nigel_()
    global vertices3
    global faces3
    global vertices3pt6a
    global faces3pt6a
    global vertices3pt5a
    global faces3pt5a
    global vertices3pt4a
    global faces3pt4a
    global vertices3pt3a
    global faces3pt3a
    global vertices3pt2a
    global faces3pt2a
    global vertices3pt2
    global faces3pt2
    global vertices3pt7a
    global faces3pt7a
    global vertices3pt8a
    global faces3pt8a
    global vertices3pt9a
    global faces3pt9a

    global fa3
    global fb3
    global fc3
    global fa3a
    global fb3a
    global fc3a
    global fd3a
    global fa3b
    global fb3b
    global fc3b
    global fd3b
    global fe3b
    global fa3c
    global fb3c
    global fc3c
    global fd3c
    global fa4c
    global fb4c
    global fc4c
    f.seek(0)
    NigelChunks = f.read()
    f.seek(0)
    while f.tell() < len(NigelChunks):#
        NigelChunk = f.read(4)
        if NigelChunk == b"\x04\x02\x00\x01":
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
                                    vertices3.append([vx1_,vz1_,vy1_]);vertices3.append([vx2_,vz2_,vy2_]);vertices3.append([vx3_,vz3_,vy3_]);fa3+=1*3;fb3+=1*3;fc3+=1*3;faces3.append([fa3,fb3,fc3])
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
                        vx4_a_a_a = unpack("<f", f.read(4))[0];vy4_a_a_a = unpack("<f", f.read(4))[0];vz4_a_a_a = unpack("<f", f.read(4))[0];brightness4_a_a_a = unpack("<f", f.read(4))[0];uvx4_a_a_a = unpack("<f", f.read(4))[0];uvy4_a_a_a = unpack("<f", f.read(4))[0];unk4_a_a_a = unpack("<f", f.read(4))[0];faceon4_a_a_a = unpack("B", f.read(1))[0];valueon4_a_a_a = unpack("B", f.read(1))[0];nz4_a_a_ = unpack("<h", f.read(2))[0];vx5_a_a_a = unpack("<f", f.read(4))[0];vy5_a_a_a = unpack("<f", f.read(4))[0];vz5_a_a_a = unpack("<f", f.read(4))[0];brightness5_a_a_a = unpack("<f", f.read(4))[0];uvx5_a_a_a = unpack("<f", f.read(4))[0];uvy5_a_a_a = unpack("<f", f.read(4))[0];unk5_a_a_a = unpack("<f", f.read(4))[0];faceon5_a_a_a = unpack("B", f.read(1))[0];valueon5_a_a_a = unpack("B", f.read(1))[0];nz5_a_a_a = unpack("<h", f.read(2))[0];vx6_a_a_a = unpack("<f", f.read(4))[0];vy6_a_a_a = unpack("<f", f.read(4))[0];vz6_a_a_a = unpack("<f", f.read(4))[0];brightness6_a_a_a = unpack("<f", f.read(4))[0];uvx6_a_a_a = unpack("<f", f.read(4))[0];uvy6_a_a_a = unpack("<f", f.read(4))[0];unk6_a_a_a = unpack("<f", f.read(4))[0];faceon6_a_a_a = unpack("B", f.read(1))[0];valueon6_a_a_a = unpack("B", f.read(1))[0];nz6_a_a_a = unpack("<h", f.read(2))[0];vx7_a_a_a = unpack("<f", f.read(4))[0];vy7_a_a_a = unpack("<f", f.read(4))[0];vz7_a_a_a = unpack("<f", f.read(4))[0];brightness7_a_a_a = unpack("<f", f.read(4))[0];uvx7_a_a_a = unpack("<f", f.read(4))[0];uvy7_a_a_a = unpack("<f", f.read(4))[0];faceon7_a_a_a = unpack("B", f.read(1))[0];valueon7_a_a_a = unpack("B", f.read(1))[0];nz7_a_a_a = unpack("<h", f.read(2))[0]
                    offset2 = unpack("<I", f.read(4))[0]
                    f.seek(-4,1)
                    offset3 = unpack("<I", f.read(4))[0]
                    f.seek(-4,1)
                    offset4 = unpack("<I", f.read(4))[0]
                    if offset4 != 1627553811:
                       offset4a_ = unpack("<I", f.read(4))[0]
                       if offset4a_ == 1627553811:
                           offset3aa = unpack("<I", f.read(4))[0]
                           if offset3aa == 65539:
                               f.seek(2,1)
                               himCount1 = unpack("B", f.read(1))[0]//2
                               himFlag1 = unpack("B", f.read(1))[0]
                               if himFlag1 == 0x6C:
                                   if himCount1 == 17:
                                       for i in range(1):
                                           himvx1 = unpack("<f", f.read(4))[0];himvy1 = unpack("<f", f.read(4))[0];himvz1 = unpack("<f", f.read(4))[0];himfaceoff1 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx1 = unpack("<f", f.read(4))[0];himuvy1 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx2 = unpack("<f", f.read(4))[0];himvy2 = unpack("<f", f.read(4))[0];himvz2 = unpack("<f", f.read(4))[0];himfaceoff2 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx2 = unpack("<f", f.read(4))[0];himuvy2 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx3 = unpack("<f", f.read(4))[0];himvy3 = unpack("<f", f.read(4))[0];himvz3 = unpack("<f", f.read(4))[0];himfaceoff3 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx3 = unpack("<f", f.read(4))[0];himuvy3 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx4 = unpack("<f", f.read(4))[0];himvy4 = unpack("<f", f.read(4))[0];himvz4 = unpack("<f", f.read(4))[0];himfaceoff4 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx4 = unpack("<f", f.read(4))[0];himuvy4 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx5 = unpack("<f", f.read(4))[0];himvy5 = unpack("<f", f.read(4))[0];himvz5 = unpack("<f", f.read(4))[0];himfaceoff5 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx5 = unpack("<f", f.read(4))[0];himuvy5 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx6 = unpack("<f", f.read(4))[0];himvy6 = unpack("<f", f.read(4))[0];himvz6 = unpack("<f", f.read(4))[0];himfaceoff6 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx6 = unpack("<f", f.read(4))[0];himuvy6 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx7 = unpack("<f", f.read(4))[0];himvy7 = unpack("<f", f.read(4))[0];himvz7 = unpack("<f", f.read(4))[0];himfaceoff7 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx7 = unpack("<f", f.read(4))[0];himuvy7 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx8 = unpack("<f", f.read(4))[0];himvy8 = unpack("<f", f.read(4))[0];himvz8 = unpack("<f", f.read(4))[0];himfaceoff8 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx8 = unpack("<f", f.read(4))[0];himuvy8 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx9 = unpack("<f", f.read(4))[0];himvy9 = unpack("<f", f.read(4))[0];himvz9 = unpack("<f", f.read(4))[0];himfaceoff9 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx9 = unpack("<f", f.read(4))[0];himuvy9 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx10 = unpack("<f", f.read(4))[0];himvy10 = unpack("<f", f.read(4))[0];himvz10 = unpack("<f", f.read(4))[0];himfaceoff10 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx10 = unpack("<f", f.read(4))[0];himuvy10 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx11 = unpack("<f", f.read(4))[0];himvy11 = unpack("<f", f.read(4))[0];himvz11 = unpack("<f", f.read(4))[0];himfaceoff11 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx11 = unpack("<f", f.read(4))[0];himuvy11 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx12 = unpack("<f", f.read(4))[0];himvy12 = unpack("<f", f.read(4))[0];himvz12 = unpack("<f", f.read(4))[0];himfaceoff12 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx12 = unpack("<f", f.read(4))[0];himuvy12 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx13 = unpack("<f", f.read(4))[0];himvy13 = unpack("<f", f.read(4))[0];himvz13 = unpack("<f", f.read(4))[0];himfaceoff13 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx13 = unpack("<f", f.read(4))[0];himuvy13 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx14 = unpack("<f", f.read(4))[0];himvy14 = unpack("<f", f.read(4))[0];himvz14 = unpack("<f", f.read(4))[0];himfaceoff14 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx14 = unpack("<f", f.read(4))[0];himuvy14 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx15 = unpack("<f", f.read(4))[0];himvy15 = unpack("<f", f.read(4))[0];himvz15 = unpack("<f", f.read(4))[0];himfaceoff15 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx15 = unpack("<f", f.read(4))[0];himuvy15 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx16 = unpack("<f", f.read(4))[0];himvy16 = unpack("<f", f.read(4))[0];himvz16 = unpack("<f", f.read(4))[0];himfaceoff16 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx16 = unpack("<f", f.read(4))[0];himuvy16 = unpack("<f", f.read(4))[0];f.seek(8,1);himvx17 = unpack("<f", f.read(4))[0];himvy17 = unpack("<f", f.read(4))[0];himvz17 = unpack("<f", f.read(4))[0];himfaceoff17 = unpack("B", f.read(1))[0];f.seek(3,1);himuvx17 = unpack("<f", f.read(4))[0];himuvy17 = unpack("<f", f.read(4))[0];f.seek(8,1)
                                       
                                       himOffset1 = unpack("<I", f.read(4))[0]
                                       if himOffset1 == 1627553883:
                                           himC = unpack("<I", f.read(4))[0]
                                           if himC == 12:
                                               himOffset2 = unpack("<I", f.read(4))[0]
                                               if himOffset2 == 1627553887:
                                                   himE = unpack("<I", f.read(4))[0]
                                                   if himE == 14:
                                                       himOffset3 = unpack("<I", f.read(4))[0]
                                                       if himOffset3 == 16777473:
                                                           if faceon4_a_a_a == 1:
                                                               if faceon5_a_a_a == 1:
                                                                   if faceon6_a_a_a == 0:
                                                                       if faceon6_a_a_a == 0:
                                                                           if himfaceoff1 == 0:
                                                                               if himfaceoff2 == 0:
                                                                                   if himfaceoff3 == 0:
                                                                                       if himfaceoff4 == 0:
                                                                                           if himfaceoff5 == 0:
                                                                                               if himfaceoff6 == 0:
                                                                                                   if himfaceoff7 == 0:
                                                                                                       if himfaceoff8 == 0:
                                                                                                           if himfaceoff9 == 0:
                                                                                                               if himfaceoff10 == 0:
                                                                                                                   if himfaceoff11 == 0:
                                                                                                                       if himfaceoff12 == 0:
                                                                                                                           if himfaceoff13 == 0:
                                                                                                                               if himfaceoff14 == 0:
                                                                                                                                   if himfaceoff15 == 0:
                                                                                                                                       if himfaceoff16 == 0:
                                                                                                                                           if himfaceoff17 == 0:
                                                                                                                                               vertices3pt6a.append([vx4_a_a_a,vz4_a_a_a,vy4_a_a_a])
                                                                                                                                               vertices3pt6a.append([vx5_a_a_a,vz5_a_a_a,vy5_a_a_a])
                                                                                                                                               vertices3pt6a.append([vx6_a_a_a,vz6_a_a_a,vy6_a_a_a])
                                                                                                                                               vertices3pt6a.append([vx7_a_a_a,vz7_a_a_a,vy7_a_a_a])
                                                                                                                                               vertices3pt6a.append([himvx1,himvz1,himvy1])
                                                                                                                                               vertices3pt6a.append([himvx2,himvz2,himvy2])
                                                                                                                                               vertices3pt6a.append([himvx3,himvz3,himvy3])
                                                                                                                                               vertices3pt6a.append([himvx4,himvz4,himvy4])
                                                                                                                                               vertices3pt6a.append([himvx5,himvz5,himvy5])
                                                                                                                                               vertices3pt6a.append([himvx6,himvz6,himvy6])
                                                                                                                                               vertices3pt6a.append([himvx7,himvz7,himvy7])
                                                                                                                                               vertices3pt6a.append([himvx8,himvz8,himvy8])
                                                                                                                                               vertices3pt6a.append([himvx9,himvz9,himvy9])
                                                                                                                                               vertices3pt6a.append([himvx10,himvz10,himvy10])
                                                                                                                                               vertices3pt6a.append([himvx11,himvz11,himvy11])
                                                                                                                                               vertices3pt6a.append([himvx12,himvz12,himvy12])
                                                                                                                                               vertices3pt6a.append([himvx13,himvz13,himvy13])
                                                                                                                                               vertices3pt6a.append([himvx14,himvz14,himvy14])
                                                                                                                                               vertices3pt6a.append([himvx15,himvz15,himvy15])
                                                                                                                                               vertices3pt6a.append([himvx16,himvz16,himvy16])
                                                                                                                                               vertices3pt6a.append([himvx17,himvz17,himvy17])

                                                                                                                                               faces3pt6a.append([0,1,2])
                                                                                                                                               faces3pt6a.append([1,2,3])
                                                                                                                                               faces3pt6a.append([4,6,2])
                                                                                                                                               faces3pt6a.append([0,6,2])
                                                                                                                                               faces3pt6a.append([4,6,10])
                                                                                                                                               faces3pt6a.append([6,10,9])
                                                                                                                                               faces3pt6a.append([9,10,3])
                                                                                                                                               faces3pt6a.append([9,3,1])
                                                                                                                                               faces3pt6a.append([0,27,31])
                                                                                                                                               faces3pt6a.append([25,27,31])
                                                                                                                                               faces3pt6a.append([25,31,40])
                                                                                                                                               faces3pt6a.append([25,40,39])
                                                                                                                                               faces3pt6a.append([0,31,24])
                                                                                                                                               faces3pt6a.append([24,0,22])
                                                                                                                                               faces3pt6a.append([31,40,35])
                                                                                                                                               faces3pt6a.append([24,31,35])
                                                                                                                                               faces3pt6a.append([27,25,23])
                                                                                                                                               faces3pt6a.append([27,21,23])
                                                                                                                                               faces3pt6a.append([25,23,37])
                                                                                                                                               faces3pt6a.append([37,25,39])
                                                                                                                                               faces3pt6a.append([23,24,35])
                                                                                                                                               faces3pt6a.append([23,35,37])
                                                                                                                                               faces3pt6a.append([21,22,24])
                                                                                                                                               faces3pt6a.append([21,24,23])
                                                                                                                                               faces3pt6a.append([31,40,2])
                                                                                                                                               faces3pt6a.append([2,40,16])
                                                                                                                                               faces3pt6a.append([18,16,4])
                                                                                                                                               faces3pt6a.append([4,2,16])
                                                                                                                                               faces3pt6a.append([16,20,2])
                                                                                                                                               faces3pt6a.append([2,3,20])
                                                                                                                                               faces3pt6a.append([4,18,19])
                                                                                                                                               faces3pt6a.append([4,19,10])
                                                                                                                                               faces3pt6a.append([10,19,20])
                                                                                                                                               faces3pt6a.append([10,20,3])
                                                                                                                                               faces3pt6a.append([0,2,31])
                                                                                                                                               
                                                                                                                                               
                    if offset3 != 1627553811:
                        f.seek(-4,1)
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

                elif stripcount == 5:
                    for i in range(1):
                        vx9_ = unpack("<f", f.read(4))[0];vy9_ = unpack("<f", f.read(4))[0];vz9_ = unpack("<f", f.read(4))[0];brightness9_ = unpack("<f", f.read(4))[0];uvx9_ = unpack("<f", f.read(4))[0];uvy9_ = unpack("<f", f.read(4))[0];unk9_ = unpack("<f", f.read(4))[0];faceon9_ = unpack("B", f.read(1))[0];valueon9_ = unpack("B", f.read(1))[0];nz9_ = unpack("<h", f.read(2))[0];vx10_ = unpack("<f", f.read(4))[0];vy10_ = unpack("<f", f.read(4))[0];vz10_ = unpack("<f", f.read(4))[0];brightness10_ = unpack("<f", f.read(4))[0];uvx10_ = unpack("<f", f.read(4))[0];uvy10_ = unpack("<f", f.read(4))[0];unk10_ = unpack("<f", f.read(4))[0];faceon10_ = unpack("B", f.read(1))[0];valueon10_ = unpack("B", f.read(1))[0];nz10_ = unpack("<h", f.read(2))[0];vx11_ = unpack("<f", f.read(4))[0];vy11_ = unpack("<f", f.read(4))[0];vz11_ = unpack("<f", f.read(4))[0];brightness11_ = unpack("<f", f.read(4))[0];uvx11_ = unpack("<f", f.read(4))[0];uvy11_ = unpack("<f", f.read(4))[0];unk11_ = unpack("<f", f.read(4))[0];faceon11_ = unpack("B", f.read(1))[0];valueon11_ = unpack("B", f.read(1))[0];nz11_ = unpack("<h", f.read(2))[0];vx12_ = unpack("<f", f.read(4))[0];vy12_ = unpack("<f", f.read(4))[0];vz12_ = unpack("<f", f.read(4))[0];brightness12_ = unpack("<f", f.read(4))[0];uvx12_ = unpack("<f", f.read(4))[0];uvy12_ = unpack("<f", f.read(4))[0];unk12_ = unpack("<f", f.read(4))[0];faceon12_ = unpack("B", f.read(1))[0];valueon12_ = unpack("B", f.read(1))[0];nz12_ = unpack("<h", f.read(2))[0];vx13_ = unpack("<f", f.read(4))[0];vy13_ = unpack("<f", f.read(4))[0];vz13_ = unpack("<f", f.read(4))[0];brightness13_ = unpack("<f", f.read(4))[0];uvx13_ = unpack("<f", f.read(4))[0];uvy13_ = unpack("<f", f.read(4))[0];unk13_ = unpack("<f", f.read(4))[0];faceon13_ = unpack("B", f.read(1))[0];valueon13_ = unpack("B", f.read(1))[0];nz13_ = unpack("<h", f.read(2))[0]
                    for i in range(1):
                        f.seek(-160,1)
                    for i in range(1):
                        vx9_a = unpack("<f", f.read(4))[0];vy9_a = unpack("<f", f.read(4))[0];vz9_a = unpack("<f", f.read(4))[0];brightness9_a = unpack("<f", f.read(4))[0];uvx9_a = unpack("<f", f.read(4))[0];uvy9_a = unpack("<f", f.read(4))[0];unk9_a = unpack("<f", f.read(4))[0];faceon9_a = unpack("B", f.read(1))[0];valueon9_a = unpack("B", f.read(1))[0];nz9_a = unpack("<h", f.read(2))[0];vx10_a = unpack("<f", f.read(4))[0];vy10_a = unpack("<f", f.read(4))[0];vz10_a = unpack("<f", f.read(4))[0];brightness10_a = unpack("<f", f.read(4))[0];uvx10_a = unpack("<f", f.read(4))[0];uvy10_a = unpack("<f", f.read(4))[0];unk10_a = unpack("<f", f.read(4))[0];faceon10_a = unpack("B", f.read(1))[0];valueon10_a = unpack("B", f.read(1))[0];nz10_a = unpack("<h", f.read(2))[0];vx11_a = unpack("<f", f.read(4))[0];vy11_a = unpack("<f", f.read(4))[0];vz11_a = unpack("<f", f.read(4))[0];brightness11_a = unpack("<f", f.read(4))[0];uvx11_a = unpack("<f", f.read(4))[0];uvy11_a = unpack("<f", f.read(4))[0];unk11_a = unpack("<f", f.read(4))[0];faceon11_a = unpack("B", f.read(1))[0];valueon11_a = unpack("B", f.read(1))[0];nz11_a = unpack("<h", f.read(2))[0];vx12_a = unpack("<f", f.read(4))[0];vy12_a = unpack("<f", f.read(4))[0];vz12_a = unpack("<f", f.read(4))[0];brightness12_a = unpack("<f", f.read(4))[0];uvx12_a = unpack("<f", f.read(4))[0];uvy12_a = unpack("<f", f.read(4))[0];unk12_a = unpack("<f", f.read(4))[0];faceon12_a = unpack("B", f.read(1))[0];valueon12_a = unpack("B", f.read(1))[0];nz12_a = unpack("<h", f.read(2))[0];vx13_a = unpack("<f", f.read(4))[0];vy13_a = unpack("<f", f.read(4))[0];vz13_a = unpack("<f", f.read(4))[0];brightness13_a = unpack("<f", f.read(4))[0];uvx13_a = unpack("<f", f.read(4))[0];uvy13_a = unpack("<f", f.read(4))[0];unk13_a = unpack("<f", f.read(4))[0];faceon13_a = unpack("B", f.read(1))[0];valueon13_a = unpack("B", f.read(1))[0];nz13_a = unpack("<h", f.read(2))[0]
                    offset6 = unpack("<I", f.read(4))[0]
                    f.seek(-4,1)
                    offset5 = unpack("<I", f.read(4))[0]
                    if offset6 == 1627553815:
                        offset6_ = unpack("<I", f.read(4))[0]
                        if offset6_ == 65540:
                            SamuraiJackoffset1_ = unpack("<I", f.read(4))[0]
                            if SamuraiJackoffset1_ == 1627553819:
                                SamuraiJackcount1_ = unpack("<I", f.read(4))[0]
                                if SamuraiJackcount1_ == 2:
                                    SamuraiJackEndoffset1_ = unpack("<I", f.read(4))[0]
                                    if SamuraiJackEndoffset1_ == 16777473:
                                        if faceon9_a == 1:
                                            if faceon10_a == 1:
                                                if faceon11_a == 0:
                                                    if faceon12_a == 0:
                                                        if faceon13_a == 1:
                                                            vertices3pt8a.append([vx9_a,vz9_a,vy9_a])
                                                            vertices3pt8a.append([vx10_a,vz10_a,vy10_a])
                                                            vertices3pt8a.append([vx11_a,vz11_a,vy11_a])
                                                            vertices3pt8a.append([vx12_a,vz12_a,vy12_a])
                                                            vertices3pt8a.append([vx13_a,vz13_a,vy13_a])
                                                            faces3pt8a.append([0,1,2])
                                                            faces3pt8a.append([1,2,3])
                                                            faces3pt8a.append([1,3,4])
                            elif SamuraiJackoffset1_ != 1627553819:
                                f.seek(-4,1)
                    if offset5 == 16777473:
                        if faceon9_ == 1:
                            if faceon10_ == 1:
                                if faceon11_ == 0:
                                    if faceon12_ == 0:
                                        if faceon13_ == 0:
                                            vertices3pt7a.append([vx9_,vz9_,vy9_])
                                            vertices3pt7a.append([vx10_,vz10_,vy10_])
                                            vertices3pt7a.append([vx11_,vz11_,vy11_])
                                            vertices3pt7a.append([vx12_,vz12_,vy12_])
                                            vertices3pt7a.append([vx13_,vz13_,vy13_])
                                            fa3b+=1*5
                                            fb3b+=1*5
                                            fc3b+=1*5
                                            fd3b+=1*5
                                            fe3b+=1*5
                                            faces3pt7a.append([fa3b,fb3b,fc3b])
                                            faces3pt7a.append([fb3b,fc3b,fd3b])
                                            faces3pt7a.append([fc3b,fd3b,fe3b])

    collection = bpy.data.collections.new("Nigel")
    bpy.context.scene.collection.children.link(collection)

    mesh3 = bpy.data.meshes.new("nigel")
    mesh3.from_pydata(vertices3, [], faces3)
    object3 = bpy.data.objects.new("nigel", mesh3)
    collection.objects.link(object3)

    mesh3pt2 = bpy.data.meshes.new("nigel")
    mesh3pt2.from_pydata(vertices3pt2a, [], faces3pt2a)
    object3pt2 = bpy.data.objects.new("nigel", mesh3pt2)
    collection.objects.link(object3pt2)

    mesh3pt3 = bpy.data.meshes.new("nigel")
    mesh3pt3.from_pydata(vertices3pt3a, [], faces3pt3a)
    object3pt3 = bpy.data.objects.new("nigel", mesh3pt3)
    collection.objects.link(object3pt3)

    mesh3pt4 = bpy.data.meshes.new("nigel")
    mesh3pt4.from_pydata(vertices3pt4a, [], faces3pt4a)
    object3pt4 = bpy.data.objects.new("nigel", mesh3pt4)
    collection.objects.link(object3pt4)

    mesh3pt5 = bpy.data.meshes.new("nigel")
    mesh3pt5.from_pydata(vertices3pt5a, [], faces3pt5a)
    object3pt5 = bpy.data.objects.new("nigel", mesh3pt5)
    collection.objects.link(object3pt5)

    mesh3pt6 = bpy.data.meshes.new("nigel")
    mesh3pt6.from_pydata(vertices3pt6a, [], faces3pt6a)
    object3pt6 = bpy.data.objects.new("nigel", mesh3pt6)
    collection.objects.link(object3pt6)

    mesh3pt2a = bpy.data.meshes.new("nigel")
    mesh3pt2a.from_pydata(vertices3pt2, [], faces3pt2)
    object3pt2a = bpy.data.objects.new("nigel", mesh3pt2a)
    collection.objects.link(object3pt2a)

    mesh3pt7 = bpy.data.meshes.new("nigel")
    mesh3pt7.from_pydata(vertices3pt7a, [], faces3pt7a)
    object3pt7 = bpy.data.objects.new("nigel", mesh3pt7)
    collection.objects.link(object3pt7)

    mesh3pt8 = bpy.data.meshes.new("nigel")
    mesh3pt8.from_pydata(vertices3pt8a, [], faces3pt8a)
    object3pt8 = bpy.data.objects.new("nigel", mesh3pt8)
    collection.objects.link(object3pt8)

    mesh3pt9 = bpy.data.meshes.new("nigel")
    mesh3pt9.from_pydata(vertices3pt9a, [], faces3pt9a)
    object3pt9 = bpy.data.objects.new("nigel", mesh3pt9)
    collection.objects.link(object3pt9)
