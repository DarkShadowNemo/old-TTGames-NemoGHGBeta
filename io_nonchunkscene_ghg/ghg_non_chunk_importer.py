from struct import pack, unpack
import os
import bpy

"""def HavenCalloftheKing(f, vertices=[]):
    f.seek(0)
    NonChunk = unpack("<I", f.read(4))[0]
    if NonChunk == 340294:
        f.seek(0x2Ef9C, 1)
        f.seek(6,1)
        vertexCount = unpack("B", f.read(1))[0]
        clump = unpack("B", f.read(4))[0]
        for i in range(int(vertexCount/2)):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vxn = unpack("<f", f.read(4))[0]
            vyn = unpack("<f", f.read(4))[0]
            vzn = unpack("<f", f.read(4))[0]
            nzx = unpack("<f", f.read(4))[0]7
    elif NonChunk ==
            vertices.append([vx,vy,vz])"""
    

            
            
        

def get_1stobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[]):
    f.seek(0)
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexCount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
        for i in range(vertexCount-2):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
            
                
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

def get_2ndobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[]):
    f.seek(0)
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x02\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(int(vertexCount/2)):
            vx = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
            vy = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
            vz = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
            f.seek(10,1)
            vertices.append([vx,vy,vz])
        for i in range(int(vertexCount/2-2)):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
            
                
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

def get_3rdobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[]):
    f.seek(0)
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x04\x02\x00\x01")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(int(vertexCount/2)):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vxn = unpack("<f", f.read(4))[0]
            vyn = unpack("<f", f.read(4))[0]
            vzn = unpack("<f", f.read(4))[0]
            nzx = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
        for i in range(int(vertexCount/2-2)):
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
                
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True
   

def wholeGHGMesh1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    while 1:
        NonChunk = f.read(4)
        if NonChunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("b", f.read(1))[0]
            clump = unpack("b", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif NonChunk == b"\x03\x03\x00\x01":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def wholeGHGMesh2(f, vertices=[], faces=[], fa=-1,fb=0,fc=1):
    f.seek(0)
    while 1:
        NonChunk = f.read(4)
        if NonChunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("b", f.read(1))[0]
            decimal = unpack("b", f.read(1))[0]
            for i in range(int(vertexCount/2)):
                vx = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                vy = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                vz = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                f.seek(10,1)
                vertices.append([vx,vy,vz])
            for i in range(int(vertexCount/2-2)):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif NonChunk == b"\x03\x03\x00\x01":
            print(f.tell())
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def writeFixwholeGHGMesh2(f):
    f.write(b"\x03\x03\x00\x01")

def wholeGHGMesh3(f, vertices=[], faces=[], fa=-1,fb=0,fc=1):
    f.seek(0)
    while 1:
        NonChunk = f.read(4)
        if NonChunk == b"\x04\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("b", f.read(1))[0]
            clump = unpack("b", f.read(1))[0]
            for i in range(int(vertexCount/2)):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vxn = unpack("<f", f.read(4))[0]
                vyn = unpack("<f", f.read(4))[0]
                vzn = unpack("<f", f.read(4))[0]
                nzx = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
            for i in range(int(vertexCount/2-2)):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
        elif NonChunk == b"\x03\x03\x00\x01":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def NonParseGHG(filepath, OFFSET1=False, OFFSET2=False, OFFSET3=False, writeaccesstoghg=False, OFFSETWHOLEEntireGHG1=False, OFFSETWHOLEEntireGHG2=False, OFFSETWHOLEEntireGHG3=False):
    f = open(filepath, "rb")
    if OFFSET1:
        get_1stobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[])
        #wholeGHGMesh1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
    if OFFSETWHOLEEntireGHG1:
        wholeGHGMesh1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
    if OFFSET2:
        get_2ndobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[])
        #wholeGHGMesh2(f, vertices=[], faces=[], fa=-1,fb=0,fc=1)
    if OFFSETWHOLEEntireGHG2:
        wholeGHGMesh2(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
    if OFFSET3:
        get_3rdobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[])
        #wholeGHGMesh3(f, vertices=[], faces=[], fa=-1,fb=0,fc=1)
    if OFFSETWHOLEEntireGHG3:
        wholeGHGMesh3(f, vertices=[], faces=[], fa=-1,fb=0,fc=1)
    if writeaccesstoghg:
        f = open(filepath, "ab")
        writeFixwholeGHGMesh2(f)
        f.close()
    f.close()
    
