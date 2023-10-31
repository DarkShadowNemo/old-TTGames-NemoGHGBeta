from struct import unpack, pack
import bpy
import os
import mathutils
import math
import bmesh

def GHG_whole_beta_Key(f, filepath):
    bm = bmesh.new()
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    meshes={}
    vertices=[]
    faces=[]
    fa=-1
    fb=0
    fc=1
    os.system("cls")
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                nz1 = unpack("<f", f.read(4))[0]
                vertices.append([vx1,vz1,vy1])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            if len(vertices) == 124:
                if faces.remove([28,29,30]):
                    pass
                elif faces.append([28,30,29]):
                    pass
                elif faces.remove([30,31,32]):
                    pass
                elif faces.append([30,32,31]):
                    pass
                elif faces.remove([32,33,34]):
                    pass
                elif faces.append([32,34,33]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.append([34,36,35]):
                    pass
                elif faces.remove([36,37,38]):
                    pass
                elif faces.append([36,38,37]):
                    pass
                elif faces.remove([26,27,28]):
                    pass
                elif faces.append([26,28,27]):
                    pass
                elif faces.remove([100,101,102]):
                    pass
                elif faces.append([100,102,101]):
                    pass
                elif faces.remove([25,26,27]):
                    pass
                elif faces.remove([99,100,101]):
                    pass
                elif faces.remove([98,99,100]):
                    pass
                elif faces.remove([24,25,26]):
                    pass
                elif faces.remove([46,47,48]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([73,74,75]):
                    pass
                elif faces.remove([42,43,44]):
                    pass
                elif faces.remove([43,44,45]):
                    pass
                elif faces.remove([47,48,49]):
                    pass
                elif faces.remove([38,39,40]):
                    pass
                elif faces.remove([92,93,94]):
                    pass
                elif faces.remove([93,94,95]):
                    pass
                elif faces.remove([19,20,21]):
                    pass
                elif faces.remove([18,19,20]):
                    pass
                elif faces.remove([16,17,18]):
                    pass
                elif faces.append([16,18,17]):
                    pass
                elif faces.remove([0,1,2]):
                    pass
                elif faces.append([0,2,1]):
                    pass
                elif faces.remove([66,67,68]):
                    pass
                elif faces.remove([67,68,69]):
                    pass
                elif faces.remove([64,65,66]):
                    pass
                elif faces.append([64,66,65]):
                    pass
                elif faces.remove([48,49,50]):
                    pass
                elif faces.append([48,50,49]):
                    pass
                elif faces.remove([14,15,16]):
                    pass
                elif faces.append([14,16,15]):
                    pass
                elif faces.remove([12,13,14]):
                    pass
                elif faces.append([12,14,13]):
                    pass
                elif faces.remove([10,11,12]):
                    pass
                elif faces.append([10,12,11]):
                    pass
                elif faces.remove([8,9,10]):
                    pass
                elif faces.append([8,10,9]):
                    pass
                elif faces.remove([6,7,8]):
                    pass
                elif faces.append([6,8,7]):
                    pass
                elif faces.remove([4,5,6]):
                    pass
                elif faces.append([4,6,5]):
                    pass
                elif faces.remove([2,3,4]):
                    pass
                elif faces.append([2,4,3]):
                    pass
                elif faces.remove([20,21,22]):
                    pass
                elif faces.append([20,22,21]):
                    pass
                elif faces.remove([22,23,24]):
                    pass
                elif faces.append([22,24,23]):
                    pass
                elif faces.remove([112,113,114]):
                    pass
                elif faces.remove([113,114,115]):
                    pass
                elif faces.remove([115,116,117]):
                    pass
                elif faces.remove([110,111,112]):
                    pass
                elif faces.remove([111,112,113]):
                    pass
                elif faces.remove([106,107,108]):
                    pass
                elif faces.remove([107,108,109]):
                    pass
                elif faces.remove([114,115,116]):
                    pass
                elif faces.remove([108,109,110]):
                    pass
                elif faces.remove([102,103,104]):
                    pass
                elif faces.append([102,104,103]):
                    pass
                elif faces.remove([104,105,106]):
                    pass
                elif faces.append([104,106,105]):
                    pass
                elif faces.remove([44,45,46]):
                    pass
                elif faces.append([44,46,45]):
                    pass
                elif faces.remove([70,71,72]):
                    pass
                elif faces.append([70,72,71]):
                    pass
                elif faces.remove([96,97,98]):
                    pass
                elif faces.append([96,98,97]):
                    pass
                elif faces.remove([94,95,96]):
                    pass
                elif faces.append([94,96,95]):
                    pass
                elif faces.remove([68,69,70]):
                    pass
                elif faces.append([68,70,69]):
                    pass
                elif faces.remove([60,61,62]):
                    pass
                elif faces.append([60,62,61]):
                    pass
                elif faces.remove([62,63,64]):
                    pass
                elif faces.append([62,64,63]):
                    pass
                elif faces.remove([50,51,52]):
                    pass
                elif faces.append([50,52,51]):
                    pass
                elif faces.remove([52,53,54]):
                    pass
                elif faces.append([52,54,53]):
                    pass
                elif faces.remove([54,55,56]):
                    pass
                elif faces.append([54,56,55]):
                    pass
                elif faces.remove([56,57,58]):
                    pass
                elif faces.append([56,58,57]):
                    pass
                elif faces.remove([58,59,60]):
                    pass
                elif faces.append([58,60,59]):
                    pass
                elif faces.remove([40,41,42]):
                    pass
                elif faces.append([40,42,41]):
                    pass
                elif faces.remove([90,91,92]):
                    pass
                elif faces.append([90,92,91]):
                    pass
                elif faces.remove([74,75,76]):
                    pass
                elif faces.append([74,76,75]):
                    pass
                elif faces.remove([76,77,78]):
                    pass
                elif faces.append([76,78,77]):
                    pass
                elif faces.remove([78,79,80]):
                    pass
                elif faces.append([78,80,79]):
                    pass
                elif faces.remove([80,81,82]):
                    pass
                elif faces.append([80,82,81]):
                    pass
                elif faces.remove([82,83,84]):
                    pass
                elif faces.append([82,84,83]):
                    pass
                elif faces.remove([84,85,86]):
                    pass
                elif faces.append([84,86,85]):
                    pass
                elif faces.remove([86,87,88]):
                    pass
                elif faces.append([86,88,87]):
                    pass
                elif faces.remove([88,89,90]):
                    pass
                elif faces.append([88,90,89]):
                    pass
                elif faces.append([23,25,104]):
                    pass
                elif faces.append([25,106,104]):
                    pass
                elif faces.append([45,47,106]):
                    pass
                elif faces.append([47,107,106]):
                    pass
                elif faces.append([70,107,72]):
                    pass
                elif faces.append([70,105,107]):
                    pass
                elif faces.remove([109,110,111]):
                    pass
                elif faces.append([39,66,40]):
                    pass

    if os.path.basename(filepath) == r"key.ghg":
        

        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)

        for fac in mesh.polygons:
            fac.use_smooth = True
