from struct import pack, unpack
import os
import bpy

def wholeGHGMesh1(f, vertices=[]):
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
        elif NonChunk == b"\x03\x02\x00\x01":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], [])
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def wholeGHGMesh2(f, vertices=[]):
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
        elif NonChunk == b"\x80\x7F\x80\x3F":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], [])
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def wholeGHGMesh3(f, vertices=[]):
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
        elif NonChunk == b"\x05\x80\x01\x60":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], [])
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def NonParseGHG(filepath, OFFSET1=False, OFFSET2=False, OFFSET3=False):
    f = open(filepath, "rb")
    if OFFSET1:
        wholeGHGMesh1(f, vertices=[])
    if OFFSET2:
        wholeGHGMesh2(f, vertices=[])
    if OFFSET3:
        wholeGHGMesh3(f, vertices=[])
    f.close()
    
