from struct import unpack, pack
import bpy
import os
import mathutils
import math
import bmesh

def GHG_whole_beta_Anemone(f, filepath):
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
        if Chunk == b"\x04\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]//2
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                nz1 = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                vertices.append([vx1,vz1,vy1])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            if len(vertices) == 595:
                if faces.remove([1,2,3]):
                    pass
                elif faces.remove([208,209,210]):
                    pass
                elif faces.remove([209,210,211]):
                    pass
                elif faces.remove([278,279,280]):
                    pass
                elif faces.remove([279,280,281]):
                    pass
                elif faces.remove([174,175,176]):
                    pass
                elif faces.remove([173,174,175]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                elif faces.remove([104,105,106]):
                    pass
                elif faces.remove([68,69,70]):
                    pass
                elif faces.remove([69,70,71]):
                    pass
                elif faces.remove([33,34,35]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.remove([243,244,245]):
                    pass
                elif faces.remove([244,245,246]):
                    pass
                elif faces.remove([138,139,140]):
                    pass
                elif faces.remove([139,140,141]):
                    pass
                elif faces.remove([313,314,315]):
                    pass
                elif faces.remove([314,315,316]):
                    pass
                elif faces.remove([348,349,350]):
                    pass
                elif faces.remove([349,350,351]):
                    pass
                elif faces.remove([383,384,385]):
                    pass
                elif faces.remove([384,385,386]):
                    pass
                elif faces.remove([188,189,190]):
                    pass
                elif faces.append([188,190,189]):
                    pass
                elif faces.remove([187,188,189]):
                    pass
                elif faces.remove([181,182,183]):
                    pass
                elif faces.append([181,183,182]):
                    pass
                elif faces.remove([180,181,182]):
                    pass
                elif faces.remove([177,178,179]):
                    pass
                elif faces.append([177,179,178]):
                    pass
                elif faces.remove([179,180,181]):
                    pass
                elif faces.remove([193,194,195]):
                    pass
                elif faces.append([193,195,194]):
                    pass
                elif faces.append([175,176,177]):
                    pass
                elif faces.append([175,177,176]):
                    pass
                elif faces.remove([189,190,191]):
                    pass
                elif faces.append([189,190,192]):
                    pass

    if os.path.basename(filepath) == r"anemone.ghg":
        

        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)

        for fac in mesh.polygons:
            fac.use_smooth = True
