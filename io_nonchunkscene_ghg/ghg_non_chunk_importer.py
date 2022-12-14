from struct import pack, unpack
import os
import bpy

"""def RND_decompress(f):
    f.seek(0)
    ChunkSize = unpack("<I", f.read(4))[0]
    Unknown01 = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    HeaderSize = unpack("<I", f.read(4))[0]
    f.seek(HeaderSize-16,1)
    
    bpy.data.images.new(name=os.path.basename(filepath), alpha=True)"""

def NonParseGHG(filepath):
    with open(filepath, "r+b") as f:
        vertices=[]
        faces=[]
        uvs=[]
        colors=[]
        fa = -1
        fb = 0
        fc = 1
        ChunkSize = f.read()
        f.seek(-4,1)
        ChunkOne = f.write(b"SST0")
        f.seek(0)
        while 1:
            Chunk = f.read(4)
            if Chunk == b"\x03\x01\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]
                clump = unpack("B", f.read(1))[0]
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
            elif Chunk == b"\x03\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0] // 2
                decmimal = unpack("B", f.read(1))[0]
                for i in range(vertexCount):
                    vx = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                    vy = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                    vz = unpack("<h", f.read(2))[0] / 10000.0 * 2.2
                    f.seek(10,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa += 1
                    fb += 1
                    fc += 1
                    faces.append([fa,fb,fc])
            elif Chunk == b"\x04\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0] // 2
                clump = unpack("B", f.read(1))[0]
                for i in range(vertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    vxn = unpack("<f", f.read(4))[0]
                    vyn = unpack("<f", f.read(4))[0]
                    vzn = unpack("<f", f.read(4))[0]
                    nzx = unpack("<f", f.read(4))[0]
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa += 1
                    fb += 1
                    fc += 1
                    faces.append([fa,fb,fc])
            elif Chunk == b"SST0":
                print(f.tell())
                break

        mesh = bpy.data.meshes.new(os.path.basename(filepath))
        object = bpy.data.objects.new(os.path.basename(filepath), mesh)
        mesh.from_pydata(vertices, [], faces)
        bpy.context.collection.objects.link(object)
        
        
        
