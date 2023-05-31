from struct import pack, unpack
import os
import bpy
import mathutils
import bmesh

def WholeMeshGHGAnemoneOne(f, vertices=[], faces=[], uvs=[],fa=-1,fb=0,fc=1,fa_=-3,fb_=-2,fc_=-1):
    chunkSize = 0
    QT = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(QT)):
        Chunk = f.read(4)
        if Chunk == b"\x04\x02\x00\x01":
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
            if len(vertices) == 595:
                #Anemone
                #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
                if faces.remove([173,174,175]):
                    pass
                elif faces.remove([174,175,176]):
                    pass
                elif faces.remove([244,245,246]):
                    pass
                elif faces.remove([243,244,245]):
                    pass
                elif faces.remove([208,209,210]):
                    pass
                elif faces.remove([209,210,211]):
                    pass
                elif faces.remove([278,279,280]):
                    pass
                elif faces.remove([279,280,281]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                #elif faces.remove([103,104,105]):
                    #pass
                elif faces.remove([104,105,106]):
                    pass
                elif faces.remove([138,139,140]):
                    pass
                elif faces.remove([139,140,141]):
                    pass
                elif faces.remove([383,384,385]):
                    pass
                elif faces.remove([384,385,386]):
                    pass
                elif faces.remove([313,314,315]):
                    pass
                elif faces.remove([314,315,316]):
                    pass
                elif faces.remove([349,350,351]):
                    pass
                elif faces.remove([348,349,350]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.remove([33,34,35]):
                    pass
                elif faces.remove([68,69,70]):
                    pass
                elif faces.remove([69,70,71]):
                    pass
                elif faces.append([571,575,576]):
                    pass
                elif faces.append([569,571,576]):
                    pass
                
            
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
                
        
                
        
        
        
