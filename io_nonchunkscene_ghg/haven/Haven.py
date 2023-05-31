from struct import unpack
import bpy
import bmesh

def WholeMeshGHGHavenOne(f, vertices=[], faces=[], uvs=[],fa=-1,fb=0,fc=1):
    chunkSize = 0
    QT = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(QT)):
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
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                #ea = unpack("B", f.read(1))[0]
                #eb = unpack("B", f.read(1))[0] // 2 - 1
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
            if len(vertices) == 2737:
                #Haven
                #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
                if faces.remove([231,232,233]):
                    pass
                elif faces.remove([230,231,232]):
                    pass
                elif faces.remove([352,353,354]):
                    pass
                elif faces.remove([353,354,355]):
                    pass
                elif faces.remove([358,359,360]):
                    pass
                elif faces.remove([353,354,355]):
                    pass
                elif faces.remove([357,358,359]):
                    pass
                elif faces.remove([371,372,373]):
                    pass
                elif faces.remove([357,358,359]):
                    pass
                elif faces.remove([91,92,93]):
                    pass
                elif faces.remove([357,358,359]):
                    pass
                elif faces.remove([119,120,121]):
                    pass
                elif faces.remove([120,121,122]):
                    pass
                elif faces.remove([370,371,372]):
                    pass
                elif faces.remove([366,367,368]):
                    pass
                elif faces.remove([367,368,369]):
                    pass
                elif faces.remove([366,367,368]):
                    pass
                elif faces.remove([92,93,94]):
                    pass
                elif faces.remove([382,383,384]):
                    pass
                elif faces.remove([383,384,385]):
                    pass
                elif faces.remove([382,383,384]):
                    pass
                elif faces.remove([813,814,815]):
                    pass
                elif faces.remove([814,815,816]):
                    pass
                elif faces.remove([2109,2110,2111]):
                    pass
                elif faces.remove([2099,2100,2101]):
                    pass
                elif faces.remove([2098,2099,2100]):
                    pass
                elif faces.append([948,21,950]):
                    pass
                elif faces.append([948,21,23]):
                    pass
                elif faces.remove([1103,1104,1105]):
                    pass
                elif faces.remove([1102,1103,1104]):
                    pass
                elif faces.remove([977,978,979]):
                    pass
                elif faces.remove([978,979,980]):
                    pass
                
                
                
                
            
    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
