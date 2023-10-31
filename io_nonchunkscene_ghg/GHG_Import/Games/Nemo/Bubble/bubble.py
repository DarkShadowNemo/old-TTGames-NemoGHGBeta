from struct import unpack, pack
import bpy
import os
import mathutils
import math
import bmesh


def GHG_whole_beta_Bubble(f, filepath):
    bm = bmesh.new()
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    meshes={}

    fa=0
    fb=0
    fc=0

    faces=[]

    os.system("cls")

    
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount//3):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                vw1 = unpack("<f", f.read(4))[0]
                vx2 = unpack("<f", f.read(4))[0]
                vy2 = unpack("<f", f.read(4))[0]
                vz2 = unpack("<f", f.read(4))[0]
                vw2 = unpack("<f", f.read(4))[0]
                vx3 = unpack("<f", f.read(4))[0]
                vy3 = unpack("<f", f.read(4))[0]
                vz3 = unpack("<f", f.read(4))[0]
                vw3 = unpack("<f", f.read(4))[0]
                verts1 = bm.verts.new([vx1,vz1,vy1])
                verts2 = bm.verts.new([vx2,vz2,vy2])
                verts3 = bm.verts.new([vx3,vz3,vy3])

                bm.faces.new([verts1,verts3,verts2])

    if os.path.basename(filepath) == r"bubble.ghg":
        

        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        bm.to_mesh(mesh)
        
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        bpy.context.collection.objects.link(object)
        for face in mesh.polygons:
            face.use_smooth=True
        bm.from_mesh(mesh)

        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
            

        bm.to_mesh(mesh)
