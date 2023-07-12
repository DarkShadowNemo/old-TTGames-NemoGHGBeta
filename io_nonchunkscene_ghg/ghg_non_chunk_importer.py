from struct import pack, unpack
from io import BytesIO as bio
import os
import bpy
import mathutils
import math

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

def GHG_whole_entire_modelAnakin_Jedi2(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces.append([fa,fb,fc])
                if len(vertices) == 3228:
                    if faces.remove([60,61,62]):
                        pass
                    elif faces.remove([59,60,61]):
                        pass
                    elif faces.remove([80,81,82]):
                        pass
                    elif faces.remove([79,80,81]):
                        pass
                    elif faces.remove([2772,2773,2774]):
                        pass
                    elif faces.remove([2771,2772,2773]):
                        pass
                    elif faces.remove([2393,2394,2395]):
                        pass
                    elif faces.remove([1171,1172,1173]):
                        pass
                    elif faces.remove([2392,2393,2394]):
                        pass
                    elif faces.remove([1170,1171,1172]):
                        pass
                    elif faces.remove([2454,2455,2456]):
                        pass
                    elif faces.remove([1233,1234,1235]):
                        pass
                    elif faces.remove([2455,2456,2457]):
                        pass
                    elif faces.remove([1232,1233,1234]):
                        pass
                    elif faces.remove([2991,2992,2993]):
                        pass
                    elif faces.remove([1638,1639,1640]):
                        pass
                    elif faces.remove([1639,1640,1641]):
                        pass
                    elif faces.remove([1680,1681,1682]):
                        pass
                    elif faces.remove([1681,1682,1683]):
                        pass
                    elif faces.remove([2776,2777,2778]):
                        pass
                    elif faces.remove([2761,2762,2763]):
                        pass
                    elif faces.remove([2778,2779,2780]):
                        pass
                    elif faces.remove([2770,2771,2772]):
                        pass
                    elif faces.remove([2768,2769,2770]):
                        pass
                    elif faces.remove([2779,2780,2781]):
                        pass
                    elif faces.remove([1513,1514,1515]):
                        pass
                    elif faces.remove([1512,1513,1514]):
                        pass
                    elif faces.remove([63,64,65]):
                        pass
                    elif faces.remove([64,65,66]):
                        pass
                    elif faces.remove([2469,2470,2471]):
                        pass
                    elif faces.remove([1269,1270,1271]):
                        pass
                    elif faces.remove([2468,2469,2470]):
                        pass
                    elif faces.remove([1268,1269,1270]):
                        pass
                    elif faces.remove([2762,2763,2764]):
                        pass

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_modelBubbles2(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_modelCRASH(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x04\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces.append([fa,fb,fc])
                if len(vertices) == 2277:
                    if faces.remove([1456,1457,1458]):
                        pass
                    elif faces.remove([1455,1456,1457]):
                        pass
                    elif faces.remove([1715,1716,1717]):
                        pass
                    elif faces.remove([1714,1715,1716]):
                        pass
                    elif faces.remove([1087,1088,1089]):
                        pass
                    elif faces.remove([1088,1089,1090]):
                        pass
                    elif faces.remove([263,264,265]):
                        pass
                    elif faces.remove([273,274,275]):
                        pass
                    elif faces.remove([178,179,180]):
                        pass
                    elif faces.remove([1226,1227,1228]):
                        pass
                    elif faces.remove([1227,1228,1229]):
                        pass
                    elif faces.remove([230,231,232]):
                        pass
                    elif faces.remove([450,451,452]):
                        pass
                    elif faces.remove([449,450,451]):
                        pass
                    elif faces.remove([1240,1241,1242]):
                        pass
                    elif faces.remove([1241,1242,1243]):
                        pass
                    elif faces.remove([143,144,145]):
                        pass
                    elif faces.remove([144,145,146]):
                        pass
                    elif faces.remove([990,991,992]):
                        pass
                    elif faces.remove([991,992,993]):
                        pass
                    elif faces.remove([1141,1142,1143]):
                        pass
                    elif faces.remove([1142,1143,1144]):
                        pass
                    elif faces.remove([655,656,657]):
                        pass
                    elif faces.remove([416,417,418]):
                        pass
                    elif faces.remove([646,647,648]):
                        pass
                    elif faces.remove([415,416,417]):
                        pass
                    elif faces.remove([645,646,647]):
                        pass
                    elif faces.remove([186,187,188]):
                        pass
                    elif faces.remove([195,196,197]):
                        pass
                    elif faces.remove([187,188,189]):
                        pass
                    elif faces.remove([288,289,290]):
                        pass
                    elif faces.remove([179,180,181]):
                        pass
                    elif faces.remove([152,153,154]):
                        pass
                    elif faces.remove([147,148,149]):
                        pass
                    elif faces.remove([165,166,167]):
                        pass
                    elif faces.remove([164,165,166]):
                        pass
                    elif faces.remove([283,284,285]):
                        pass
                    elif faces.remove([284,285,286]):
                        pass
                    elif faces.remove([287,288,289]):
                        pass
                    elif faces.remove([194,195,196]):
                        pass
                    elif faces.remove([151,152,153]):
                        pass
                    elif faces.remove([148,149,150]):
                        pass
                    elif faces.remove([229,230,231]):
                        pass
                    elif faces.remove([272,273,274]):
                        pass
                    elif faces.remove([262,263,264]):
                        pass
                    elif faces.remove([678,679,680]):
                        pass
                    elif faces.remove([975,976,977]):
                        pass
                    elif faces.remove([968,969,970]):
                        pass
                    elif faces.remove([972,973,974]):
                        pass
                    elif faces.remove([971,972,973]):
                        pass
                    elif faces.remove([769,770,771]):
                        pass
                    elif faces.remove([768,769,770]):
                        pass
                    elif faces.remove([976,977,978]):
                        pass
                    elif faces.remove([735,736,737]):
                        pass
                    elif faces.remove([734,735,736]):
                        pass
                    elif faces.remove([656,657,658]):
                        pass
                    elif faces.remove([667,668,669]):
                        pass
                    elif faces.remove([661,662,663]):
                        pass
                    elif faces.remove([662,663,664]):
                        pass
                    elif faces.remove([677,678,679]):
                        pass
                    elif faces.remove([839,840,841]):
                        pass
                    elif faces.remove([836,837,838]):
                        pass
                    elif faces.remove([967,968,969]):
                        pass
                    elif faces.remove([840,841,842]):
                        pass
                    elif faces.remove([820,821,822]):
                        pass
                    elif faces.remove([772,773,774]):
                        pass
                    elif faces.remove([773,774,775]):
                        pass
                    elif faces.remove([660,661,662]):
                        pass
                    elif faces.remove([1013,1014,1015]):
                        pass
                    elif faces.remove([1014,1015,1016]):
                        pass
                    elif faces.remove([510,511,512]):
                        pass
                    elif faces.remove([460,461,462]):
                        pass
                    elif faces.remove([1179,1180,1181]):
                        pass
                    elif faces.remove([1178,1179,1180]):
                        pass
                    elif faces.remove([1210,1211,1212]):
                        pass
                    elif faces.remove([509,510,511]):
                        pass
                    elif faces.remove([919,920,921]):
                        pass
                    elif faces.remove([638,639,640]):
                        pass
                    elif faces.remove([1158,1159,1160]):
                        pass
                    elif faces.remove([751,752,753]):
                        pass
                    elif faces.remove([819,820,821]):
                        pass
                    elif faces.remove([752,753,754]):
                        pass
                    elif faces.remove([835,836,837]):
                        pass
                    elif faces.remove([747,748,749]):
                        pass
                    elif faces.remove([746,747,748]):
                        pass
                    elif faces.remove([742,743,744]):
                        pass
                    elif faces.remove([743,744,745]):
                        pass
                    elif faces.remove([783,784,785]):
                        pass
                    elif faces.remove([782,783,784]):
                        pass
                    elif faces.remove([824,825,826]):
                        pass
                    elif faces.remove([823,824,825]):
                        pass
                    elif faces.remove([827,828,829]):
                        pass
                    elif faces.remove([828,829,830]):
                        pass
                    elif faces.remove([512,513,514]):
                        pass
                    elif faces.remove([513,514,515]):
                        pass
                    elif faces.remove([833,834,835]):
                        pass
                    elif faces.remove([834,835,836]):
                        pass
                    elif faces.remove([795,796,797]):
                        pass
                    elif faces.remove([724,725,726]):
                        pass
                    elif faces.remove([725,726,727]):
                        pass
                    elif faces.remove([291,292,293]):
                        pass
                    elif faces.remove([292,293,294]):
                        pass
                    elif faces.remove([730,731,732]):
                        pass
                    elif faces.remove([729,730,731]):
                        pass
                    elif faces.remove([809,810,811]):
                        pass
                    elif faces.remove([810,811,812]):
                        pass
                    elif faces.remove([796,797,798]):
                        pass
                    elif faces.remove([1632,1633,1634]):
                        pass
                    elif faces.remove([1631,1632,1633]):
                        pass
                    elif faces.remove([1615,1616,1617]):
                        pass
                    elif faces.remove([1616,1617,1618]):
                        pass
                    elif faces.remove([1682,1683,1684]):
                        pass
                    elif faces.remove([1683,1684,1685]):
                        pass
                    elif faces.remove([1476,1477,1478]):
                        pass
                    elif faces.remove([1562,1563,1564]):
                        pass
                    elif faces.remove([1477,1478,1479]):
                        pass

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)
        

def GHG_whole_entire_modelRay2(f, vertices2=[], faces2=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]//2
                f.seek(1,1)
                for i in range(vertexCount):
                    vx = unpack("<h", f.read(2))[0] / 4096.0
                    vy = unpack("<h", f.read(2))[0] / 4096.0
                    vz = unpack("<h", f.read(2))[0] / 4096.0
                    nz = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(8,1)
                    vertices2.append([vx,vy,vz])
                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces2.append([fa,fb,fc])
                if len(vertices2) == 2564:
                    if faces2.remove([1131,1132,1133]):
                        pass
                    elif faces2.remove([1130,1131,1132]):
                        pass
                    elif faces2.remove([1468,1469,1470]):
                        pass
                    elif faces2.remove([1748,1749,1750]):
                        pass
                    elif faces2.remove([1741,1742,1743]):
                        pass
                    elif faces2.remove([1744,1745,1746]):
                        pass
                    elif faces2.remove([1747,1748,1749]):
                        pass
                    elif faces2.remove([1750,1751,1752]):
                        pass
                    elif faces2.remove([1749,1750,1751]):
                        pass
                    elif faces2.remove([313,314,315]):
                        pass
                    elif faces2.remove([1734,1735,1736]):
                        pass
                    elif faces2.remove([728,729,730]):
                        pass
                    elif faces2.remove([729,730,731]):
                        pass
                    elif faces2.remove([785,786,787]):
                        pass
                    elif faces2.remove([114,115,116]):
                        pass
                    elif faces2.remove([1412,1413,1414]):
                        pass
                    elif faces2.remove([692,693,694]):
                        pass
                    elif faces2.remove([689,690,691]):
                        pass
                    elif faces2.remove([581,582,583]):
                        pass
                    elif faces2.remove([577,578,579]):
                        pass
                    elif faces2.remove([576,577,578]):
                        pass
                    elif faces2.remove([573,574,575]):
                        pass
                    elif faces2.remove([574,575,576]):
                        pass
                    elif faces2.remove([580,581,582]):
                        pass
                    elif faces2.remove([578,579,580]):
                        pass
                    elif faces2.remove([575,576,577]):
                        pass
                    elif faces2.remove([572,573,574]):
                        pass
                    elif faces2.remove([711,712,713]):
                        pass
                    elif faces2.remove([112,113,114]):
                        pass
                    elif faces2.remove([778,779,780]):
                        pass
                    elif faces2.remove([777,778,779]):
                        pass
                    elif faces2.remove([776,777,778]):
                        pass
                    elif faces2.remove([1838,1839,1840]):
                        pass
                    elif faces2.remove([715,716,717]):
                        pass
                    elif faces2.remove([712,713,714]):
                        pass
                    elif faces2.remove([716,717,718]):
                        pass
                    elif faces2.remove([368,369,370]):
                        pass
                    elif faces2.remove([367,368,369]):
                        pass
                    elif faces2.remove([349,350,351]):
                        pass
                    elif faces2.remove([61,62,63]):
                        pass
                    elif faces2.remove([883,884,885]):
                        pass

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices2, [], faces2)
    bpy.context.collection.objects.link(object)

def GHG_whole_entire_modelRay1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            if len(faces) == 156:
                if faces.remove([104,105,106]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                elif faces.remove([51,52,53]):
                    pass
                elif faces.remove([50,51,52]):
                    pass
                elif faces.remove([20,21,22]):
                    pass
                elif faces.remove([19,20,21]):
                    pass
                elif faces.remove([135,136,137]):
                    pass
                elif faces.remove([134,135,136]):
                    pass
                elif faces.remove([73,74,75]):
                    pass
                elif faces.remove([114,115,116]):
                    pass
                elif faces.remove([145,146,147]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([113,114,115]):
                    pass
                elif faces.remove([144,145,146]):
                    pass
                elif faces.remove([30,31,32]):
                    pass
                elif faces.remove([29,30,31]):
                    pass
                elif faces.remove([83,84,85]):
                    pass
                elif faces.remove([61,62,63]):
                    pass
                elif faces.remove([60,61,62]):
                    pass
                elif faces.remove([82,83,84]):
                    pass
                elif faces.remove([35,36,37]):
                    pass
                elif faces.remove([36,37,38]):
                    pass
                elif faces.remove([38,39,40]):
                    pass
                elif faces.remove([37,38,39]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.remove([33,34,35]):
                    pass
                elif faces.remove([32,33,34]):
                    pass
                elif faces.remove([31,32,33]):
                    pass
                elif faces.remove([143,144,145]):
                    pass
                elif faces.remove([142,143,144]):
                    pass
                elif faces.remove([44,45,46]):
                    pass
                elif faces.remove([45,46,47]):
                    pass
                elif faces.remove([47,48,49]):
                    pass
                elif faces.remove([46,47,48]):
                    pass
                elif faces.remove([48,49,50]):
                    pass
                elif faces.remove([49,50,51]):
                    pass
                elif faces.remove([115,116,117]):
                    pass
                elif faces.remove([116,117,118]):
                    pass
                elif faces.remove([117,118,119]):
                    pass
                elif faces.remove([118,119,120]):
                    pass
                elif faces.remove([119,120,121]):
                    pass
                elif faces.remove([120,121,122]):
                    pass
                elif faces.remove([121,122,123]):
                    pass
                elif faces.remove([122,123,124]):
                    pass
                elif faces.remove([123,124,125]):
                    pass
                elif faces.remove([124,125,126]):
                    pass
                elif faces.remove([112,113,114]):
                    pass
                elif faces.remove([111,112,113]):
                    pass
                elif faces.remove([110,111,112]):
                    pass
                elif faces.remove([109,110,111]):
                    pass
                elif faces.remove([108,109,110]):
                    pass
                elif faces.remove([107,108,109]):
                    pass
                elif faces.remove([106,107,108]):
                    pass
                elif faces.remove([105,106,107]):
                    pass
                elif faces.remove([133,134,135]):
                    pass
                elif faces.remove([132,133,134]):
                    pass
                elif faces.remove([131,132,133]):
                    pass
                elif faces.remove([130,131,132]):
                    pass
                elif faces.remove([129,130,131]):
                    pass
                elif faces.remove([128,129,130]):
                    pass
                elif faces.remove([127,128,129]):
                    pass
                elif faces.remove([126,127,128]):
                    pass
                elif faces.remove([125,126,127]):
                    pass
                elif faces.remove([92,93,94]):
                    pass
                elif faces.remove([91,92,93]):
                    pass
                elif faces.remove([90,91,92]):
                    pass
                elif faces.remove([89,90,91]):
                    pass
                elif faces.remove([88,89,90]):
                    pass
                elif faces.remove([87,88,89]):
                    pass
                elif faces.remove([86,87,88]):
                    pass
                elif faces.remove([85,86,87]):
                    pass
                elif faces.remove([84,85,86]):
                    pass
                elif faces.remove([93,94,95]):
                    pass
                
            

    mesh = bpy.data.meshes.new("dragonjan")
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.from_pydata(vertices, [], faces)
    bpy.context.collection.objects.link(object)

    



def NonParseGHG(filepath, GHG_Meshes=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes == 1:
            if os.path.basename(filepath) == r"ray.ghg":
                GHG_whole_entire_modelRay1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
        if GHG_Meshes == 2:
            if os.path.basename(filepath) == r"ray.ghg":
                GHG_whole_entire_modelRay2(f, vertices2=[], faces2=[], fa=-1, fb=0, fc=1)

        if GHG_Meshes == 3:
            if os.path.basename(filepath) == r"CRASH_unpack.GHG":
                GHG_whole_entire_modelCRASH(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)

        if GHG_Meshes == 4:
            if os.path.basename(filepath) == r"bubbles.ghg":
                GHG_whole_entire_modelBubbles2(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)

        if GHG_Meshes == 5:
            if os.path.basename(filepath) == r"anakin_jedi.ghg":
                GHG_whole_entire_modelAnakin_Jedi2(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
            
                
        
                
        
        
        
