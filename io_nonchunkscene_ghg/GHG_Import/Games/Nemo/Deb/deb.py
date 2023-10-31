from struct import unpack, pack
import bpy
import os
import mathutils
import math
import bmesh

def GHG_whole_beta_Deb(f, filepath):
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
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<h", f.read(2))[0] / 4096.0
                vy1 = unpack("<h", f.read(2))[0] / 4096.0
                vz1 = unpack("<h", f.read(2))[0] / 4096.0
                nz1 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx1,vz1,vy1])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            if len(vertices) == 1172:
                if faces.remove([124,125,126]):
                    pass
                elif faces.remove([125,126,127]):
                    pass
                elif faces.remove([62,63,64]):
                    pass
                elif faces.remove([63,64,65]):
                    pass
                elif faces.remove([79,80,81]):
                    pass
                elif faces.remove([924,925,926]):
                    pass
                elif faces.remove([906,907,908]):
                    pass
                elif faces.remove([907,908,909]):
                    pass
                elif faces.remove([905,906,907]):
                    pass
                elif faces.remove([904,905,906]):
                    pass
                elif faces.remove([836,837,838]):
                    pass
                elif faces.remove([794,795,796]):
                    pass
                elif faces.remove([646,647,648]):
                    pass
                elif faces.remove([92,93,94]):
                    pass
                elif faces.remove([42,43,44]):
                    pass
                elif faces.remove([41,42,43]):
                    pass
                elif faces.remove([43,44,45]):
                    pass
                elif faces.remove([600,601,602]):
                    pass
                elif faces.remove([506,507,508]):
                    pass
                elif faces.remove([507,508,509]):
                    pass
                elif faces.remove([601,602,603]):
                    pass
                elif faces.remove([583,584,585]):
                    pass
                elif faces.remove([581,582,583]):
                    pass
                elif faces.remove([582,583,584]):
                    pass
                elif faces.remove([664,665,666]):
                    pass
                elif faces.remove([665,666,667]):
                    pass
                elif faces.remove([391,392,393]):
                    pass
                elif faces.remove([602,603,604]):
                    pass
                elif faces.remove([394,395,396]):
                    pass
                elif faces.remove([795,796,797]):
                    pass
                elif faces.remove([615,616,617]):
                    pass
                elif faces.remove([636,637,638]):
                    pass
                elif faces.remove([631,632,633]):
                    pass
                elif faces.remove([775,776,777]):
                    pass
                elif faces.remove([773,774,775]):
                    pass
                elif faces.remove([302,303,304]):
                    pass
                elif faces.remove([373,374,375]):
                    pass
                elif faces.remove([372,373,374]):
                    pass
                elif faces.remove([729,730,731]):
                    pass
                elif faces.remove([776,777,778]):
                    pass
                elif faces.remove([263,264,265]):
                    pass
                elif faces.remove([264,265,266]):
                    pass
                elif faces.remove([262,263,264]):
                    pass
                elif faces.remove([304,305,306]):
                    pass
                elif faces.remove([762,763,764]):
                    pass
                elif faces.remove([842,843,844]):
                    pass
                elif faces.remove([334,335,336]):
                    pass
                elif faces.remove([293,294,295]):
                    pass
                elif faces.remove([294,295,296]):
                    pass
                elif faces.remove([330,331,332]):
                    pass
                elif faces.remove([329,330,331]):
                    pass
                elif faces.remove([307,308,309]):
                    pass
                elif faces.remove([1009,1010,1011]):
                    pass
                elif faces.remove([779,780,781]):
                    pass
                elif faces.remove([305,306,307]):
                    pass
                elif faces.remove([93,94,95]):
                    pass
                elif faces.remove([74,75,76]):
                    pass
                elif faces.remove([66,67,68]):
                    pass
                elif faces.remove([761,762,763]):
                    pass
                elif faces.remove([67,68,69]):
                    pass
                elif faces.remove([781,782,783]):
                    pass
                elif faces.remove([690,691,692]):
                    pass
                elif faces.remove([824,825,826]):
                    pass
                elif faces.remove([859,860,861]):
                    pass
                elif faces.remove([858,859,860]):
                    pass
                elif faces.remove([837,838,839]):
                    pass
                elif faces.remove([630,631,632]):
                    pass
                elif faces.remove([75,76,77]):
                    pass
                elif faces.remove([389,390,391]):
                    pass
                elif faces.remove([388,389,390]):
                    pass
                elif faces.remove([367,368,369]):
                    pass
                elif faces.remove([511,512,513]):
                    pass
                elif faces.remove([308,309,310]):
                    pass
                elif faces.remove([368,369,370]):
                    pass
                elif faces.remove([365,366,367]):
                    pass
                elif faces.remove([366,367,368]):
                    pass
                elif faces.remove([542,543,544]):
                    pass
                elif faces.remove([689,690,691]):
                    pass
                elif faces.remove([543,544,545]):
                    pass
                elif faces.remove([370,371,372]):
                    pass
                elif faces.remove([390,391,392]):
                    pass
                elif faces.remove([535,536,537]):
                    pass
                elif faces.remove([894,895,896]):
                    pass
                elif faces.remove([656,657,658]):
                    pass
                elif faces.remove([661,662,663]):
                    pass
                elif faces.remove([662,663,664]):
                    pass
                elif faces.remove([827,828,829]):
                    pass
                elif faces.remove([728,729,730]):
                    pass
                elif faces.remove([531,532,533]):
                    pass
                elif faces.remove([828,829,830]):
                    pass
                elif faces.remove([533,534,535]):
                    pass
                elif faces.remove([534,535,536]):
                    pass
                elif faces.remove([530,531,532]):
                    pass
                elif faces.remove([529,530,531]):
                    pass
                elif faces.remove([663,664,665]):
                    pass
                elif faces.remove([371,372,373]):
                    pass
                elif faces.remove([891,892,893]):
                    pass
                elif faces.remove([651,652,653]):
                    pass
                elif faces.remove([660,661,662]):
                    pass
                elif faces.remove([655,656,657]):
                    pass
                elif faces.remove([650,651,652]):
                    pass
                elif faces.remove([654,655,656]):
                    pass
                elif faces.remove([653,654,655]):
                    pass
                elif faces.remove([783,784,785]):
                    pass
                elif faces.remove([20,21,22]):
                    pass
                elif faces.remove([19,20,21]):
                    pass
                elif faces.remove([642,643,644]):
                    pass
                elif faces.remove([640,641,642]):
                    pass
                elif faces.remove([639,640,641]):
                    pass
                elif faces.remove([641,642,643]):
                    pass
                elif faces.remove([782,783,784]):
                    pass
                elif faces.remove([784,785,786]):
                    pass
                elif faces.remove([793,794,795]):
                    pass
                elif faces.remove([792,793,794]):
                    pass
                elif faces.remove([443,444,445]):
                    pass
                elif faces.remove([462,463,464]):
                    pass
                elif faces.remove([544,545,546]):
                    pass
                elif faces.remove([460,461,462]):
                    pass
                elif faces.remove([823,824,825]):
                    pass
                elif faces.remove([300,301,302]):
                    pass
                elif faces.remove([301,302,303]):
                    pass
                elif faces.remove([510,511,512]):
                    pass
                elif faces.remove([406,407,408]):
                    pass
                elif faces.remove([527,528,529]):
                    pass
                elif faces.remove([528,529,530]):
                    pass
                elif faces.remove([526,527,528]):
                    pass
                elif faces.remove([408,409,410]):
                    pass
                elif faces.remove([407,408,409]):
                    pass
                elif faces.remove([311,312,313]):
                    pass
                elif faces.remove([312,313,314]):
                    pass
                elif faces.remove([261,262,263]):
                    pass
                elif faces.remove([513,514,515]):
                    pass
                elif faces.remove([895,896,897]):
                    pass
                elif faces.remove([644,645,646]):
                    pass
                elif faces.remove([643,644,645]):
                    pass
                elif faces.remove([621,622,623]):
                    pass
                elif faces.remove([620,621,622]):
                    pass
                elif faces.remove([819,820,821]):
                    pass
                elif faces.remove([820,821,822]):
                    pass
                elif faces.remove([860,861,862]):
                    pass
                elif faces.remove([861,862,863]):
                    pass
                elif faces.remove([532,533,534]):
                    pass
                elif faces.remove([359,360,361]):
                    pass
                elif faces.remove([360,361,362]):
                    pass
                elif faces.remove([363,364,365]):
                    pass
                elif faces.remove([320,321,322]):
                    pass
                elif faces.remove([303,304,305]):
                    pass
                elif faces.remove([319,320,321]):
                    pass
                elif faces.remove([635,636,637]):
                    pass
                elif faces.remove([763,764,765]):
                    pass
                elif faces.remove([758,759,760]):
                    pass
                elif faces.remove([759,760,761]):
                    pass
                elif faces.remove([291,292,293]):
                    pass
                elif faces.remove([727,728,729]):
                    pass
                elif faces.remove([710,711,712]):
                    pass
                elif faces.remove([704,705,706]):
                    pass
                elif faces.remove([364,365,366]):
                    pass
                elif faces.remove([518,519,520]):
                    pass
                elif faces.remove([517,518,519]):
                    pass
                elif faces.remove([516,517,518]):
                    pass
                elif faces.remove([512,513,514]):
                    pass
                elif faces.remove([834,835,836]):
                    pass
                elif faces.remove([514,515,516]):
                    pass
                elif faces.remove([857,858,859]):
                    pass
                elif faces.remove([645,646,647]):
                    pass
                elif faces.remove([843,844,845]):
                    pass
                elif faces.remove([903,904,905]):
                    pass
                elif faces.remove([835,836,837]):
                    pass
                elif faces.remove([519,520,521]):
                    pass
                elif faces.remove([774,775,776]):
                    pass
                elif faces.remove([711,712,713]):
                    pass
                elif faces.remove([298,299,300]):
                    pass
                elif faces.remove([299,300,301]):
                    pass
                elif faces.remove([703,704,705]):
                    pass
                elif faces.remove([693,694,695]):
                    pass
                elif faces.remove([694,695,696]):
                    pass
                elif faces.remove([332,333,334]):
                    pass
                elif faces.remove([333,334,335]):
                    pass
                elif faces.remove([306,307,308]):
                    pass
                elif faces.remove([331,332,333]):
                    pass
                elif faces.remove([296,297,298]):
                    pass
                elif faces.remove([297,298,299]):
                    pass
                elif faces.remove([295,296,297]):
                    pass
                elif faces.remove([292,293,294]):
                    pass
                elif faces.remove([409,410,411]):
                    pass
                elif faces.remove([410,411,412]):
                    pass
                elif faces.remove([525,526,527]):
                    pass
                elif faces.remove([524,525,526]):
                    pass
                elif faces.remove([269,270,271]):
                    pass
                elif faces.remove([270,271,272]):
                    pass
                elif faces.remove([271,272,273]):
                    pass
                elif faces.remove([335,336,337]):
                    pass
                elif faces.remove([78,79,80]):
                    pass
                elif faces.remove([387,388,389]):
                    pass
                elif faces.remove([780,781,782]):
                    pass
                elif faces.remove([778,779,780]):
                    pass
                elif faces.remove([80,81,82]):
                    pass
                elif faces.remove([83,84,85]):
                    pass
                elif faces.remove([85,86,87]):
                    pass
                elif faces.remove([628,629,630]):
                    pass
                elif faces.remove([838,839,840]):
                    pass
                elif faces.remove([647,648,649]):
                    pass
                elif faces.remove([788,789,790]):
                    pass
                elif faces.remove([789,790,791]):
                    pass
                elif faces.remove([925,926,927]):
                    pass
                elif faces.remove([839,840,841]):
                    pass
                elif faces.remove([929,930,931]):
                    pass
                elif faces.remove([963,964,965]):
                    pass
                elif faces.remove([961,962,963]):
                    pass
                elif faces.remove([930,931,932]):
                    pass
                elif faces.remove([931,932,933]):
                    pass
                elif faces.remove([893,894,895]):
                    pass
                elif faces.remove([659,660,661]):
                    pass
                elif faces.remove([840,841,842]):
                    pass
                elif faces.remove([825,826,827]):
                    pass
                elif faces.remove([989,990,991]):
                    pass
                elif faces.remove([657,658,659]):
                    pass
                elif faces.remove([968,969,970]):
                    pass
                elif faces.remove([841,842,843]):
                    pass
                elif faces.remove([928,929,930]):
                    pass

    if os.path.basename(filepath) == r"deb.ghg":
        

        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)

        for fac in mesh.polygons:
            fac.use_smooth = True
