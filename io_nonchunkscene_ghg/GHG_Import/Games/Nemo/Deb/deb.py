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
                elif faces.remove([385,386,387]):
                    pass
                elif faces.remove([277,278,279]):
                    pass
                elif faces.remove([275,276,277]):
                    pass
                elif faces.remove([265,266,267]):
                    pass
                elif faces.remove([374,375,376]):
                    pass
                elif faces.remove([267,268,269]):
                    pass
                elif faces.remove([268,269,270]):
                    pass
                elif faces.remove([375,376,377]):
                    pass
                elif faces.remove([266,267,268]):
                    pass
                elif faces.remove([283,284,285]):
                    pass
                elif faces.remove([282,283,284]):
                    pass
                elif faces.remove([284,285,286]):
                    pass
                elif faces.remove([285,286,287]):
                    pass
                elif faces.remove([940,941,942]):
                    pass
                elif faces.remove([939,940,941]):
                    pass
                elif faces.remove([938,939,940]):
                    pass
                elif faces.remove([936,937,938]):
                    pass
                elif faces.remove([934,935,936]):
                    pass
                elif faces.remove([935,936,937]):
                    pass
                elif faces.remove([691,692,693]):
                    pass
                elif faces.remove([927,928,929]):
                    pass
                elif faces.append([927,929,928]):
                    pass
                elif faces.remove([1013,1014,1015]):
                    pass
                elif faces.remove([1012,1013,1014]):
                    pass
                elif faces.remove([1010,1011,1012]):
                    pass
                elif faces.remove([629,630,631]):
                    pass
                elif faces.remove([969,970,971]):
                    pass
                elif faces.remove([260,261,262]):
                    pass
                elif faces.remove([1008,1009,1010]):
                    pass
                elif faces.remove([1006,1007,1008]):
                    pass
                elif faces.append([1008,1029,1009]):
                    pass
                elif faces.remove([405,406,407]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([23,24,25]):
                    pass
                elif faces.remove([16,17,18]):
                    pass
                elif faces.remove([1,2,3]):
                    pass
                elif faces.remove([0,1,2]):
                    pass
                elif faces.remove([15,16,17]):
                    pass
                elif faces.remove([14,15,16]):
                    pass
                elif faces.remove([7,8,9]):
                    pass
                elif faces.remove([22,23,24]):
                    pass
                elif faces.remove([8,9,10]):
                    pass
                elif faces.remove([37,38,39]):
                    pass
                elif faces.remove([17,18,19]):
                    pass
                elif faces.remove([38,39,40]):
                    pass
                elif faces.remove([21,22,23]):
                    pass
                elif faces.remove([9,10,11]):
                    pass
                elif faces.remove([10,11,12]):
                    pass
                elif faces.remove([11,12,13]):
                    pass
                elif faces.remove([12,13,14]):
                    pass
                elif faces.remove([13,14,15]):
                    pass
                elif faces.remove([791,792,793]):
                    pass
                elif faces.remove([652,653,654]):
                    pass
                elif faces.remove([65,66,67]):
                    pass
                elif faces.remove([35,36,37]):
                    pass
                elif faces.remove([34,35,36]):
                    pass
                elif faces.remove([33,34,35]):
                    pass
                elif faces.remove([91,92,93]):
                    pass
                elif faces.remove([90,91,92]):
                    pass
                elif faces.remove([87,88,89]):
                    pass
                elif faces.remove([86,87,88]):
                    pass
                elif faces.remove([77,78,79]):
                    pass
                elif faces.remove([287,288,289]):
                    pass
                elif faces.remove([288,289,290]):
                    pass
                elif faces.remove([289,290,291]):
                    pass
                elif faces.remove([658,659,660]):
                    pass
                elif faces.remove([81,82,83]):
                    pass
                elif faces.append([81,83,82]):
                    pass
                elif faces.remove([89,90,91]):
                    pass
                elif faces.remove([88,89,90]):
                    pass
                elif faces.append([88,90,89]):
                    pass
                elif faces.append([81,82,65]):
                    pass
                elif faces.remove([64,65,66]):
                    pass
                elif faces.append([64,66,65]):
                    pass
                elif faces.append([84,86,90]):
                    pass
                elif faces.append([76,88,90]):
                    pass
                elif faces.remove([933,934,935]):
                    pass
                elif faces.remove([626,627,628]):
                    pass
                elif faces.remove([627,628,629]):
                    pass
                elif faces.remove([786,787,788]):
                    pass
                elif faces.remove([790,791,792]):
                    pass
                elif faces.remove([624,625,626]):
                    pass
                elif faces.remove([785,786,787]):
                    pass
                elif faces.remove([625,626,627]):
                    pass
                elif faces.remove([623,624,625]):
                    pass
                elif faces.remove([622,623,624]):
                    pass
                elif faces.remove([444,445,446]):
                    pass
                elif faces.remove([441,442,443]):
                    pass
                elif faces.remove([555,556,557]):
                    pass
                elif faces.remove([554,555,556]):
                    pass
                elif faces.remove([463,464,465]):
                    pass
                elif faces.remove([442,443,444]):
                    pass
                elif faces.remove([545,546,547]):
                    pass
                elif faces.remove([440,441,442]):
                    pass
                elif faces.remove([459,460,461]):
                    pass
                elif faces.remove([458,459,460]):
                    pass
                elif faces.remove([457,458,459]):
                    pass
                elif faces.remove([456,457,458]):
                    pass
                elif faces.remove([143,144,145]):
                    pass
                elif faces.remove([142,143,144]):
                    pass
                elif faces.remove([160,161,162]):
                    pass
                elif faces.remove([877,878,879]):
                    pass
                elif faces.remove([878,879,880]):
                    pass
                elif faces.remove([504,505,506]):
                    pass
                elif faces.remove([876,877,878]):
                    pass
                elif faces.remove([875,876,877]):
                    pass
                elif faces.remove([434,435,436]):
                    pass
                elif faces.remove([435,436,437]):
                    pass
                elif faces.remove([430,431,432]):
                    pass
                elif faces.remove([431,432,433]):
                    pass
                elif faces.remove([634,635,636]):
                    pass
                elif faces.remove([633,634,635]):
                    pass
                elif faces.remove([898,899,900]):
                    pass
                elif faces.remove([899,900,901]):
                    pass
                elif faces.remove([900,901,902]):
                    pass
                elif faces.remove([376,377,378]):
                    pass
                elif faces.remove([369,370,371]):
                    pass
                elif faces.remove([616,617,618]):
                    pass
                elif faces.remove([869,870,871]):
                    pass
                elif faces.remove([868,869,870]):
                    pass
                elif faces.remove([862,863,864]):
                    pass
                elif faces.remove([347,348,349]):
                    pass
                elif faces.remove([348,349,350]):
                    pass
                elif faces.remove([756,757,758]):
                    pass
                elif faces.remove([755,756,757]):
                    pass
                elif faces.remove([725,726,727]):
                    pass
                elif faces.remove([726,727,728]):
                    pass
                elif faces.remove([723,724,725]):
                    pass
                elif faces.remove([722,723,724]):
                    pass
                elif faces.remove([746,747,748]):
                    pass
                elif faces.remove([745,746,747]):
                    pass
                elif faces.remove([350,351,352]):
                    pass
                elif faces.remove([358,359,360]):
                    pass
                elif faces.remove([349,350,351]):
                    pass
                elif faces.remove([747,748,749]):
                    pass
                elif faces.remove([698,699,700]):
                    pass
                elif faces.remove([697,698,699]):
                    pass
                elif faces.remove([696,697,698]):
                    pass
                elif faces.remove([676,677,678]):
                    pass
                elif faces.remove([677,678,679]):
                    pass
                elif faces.remove([678,679,680]):
                    pass
                elif faces.remove([310,311,312]):
                    pass
                elif faces.remove([228,229,230]):
                    pass
                elif faces.remove([211,212,213]):
                    pass
                elif faces.remove([193,194,195]):
                    pass
                elif faces.remove([439,440,441]):
                    pass
                elif faces.remove([890,891,892]):
                    pass
                elif faces.remove([901,902,903]):
                    pass
                elif faces.remove([885,886,887]):
                    pass
                elif faces.remove([886,887,888]):
                    pass
                elif faces.remove([870,871,872]):
                    pass
                elif faces.remove([871,872,873]):
                    pass
                elif faces.remove([872,873,874]):
                    pass
                elif faces.remove([278,279,280]):
                    pass
                elif faces.remove([279,280,281]):
                    pass
                elif faces.remove([286,287,288]):
                    pass
                elif faces.remove([553,554,555]):
                    pass
                elif faces.remove([551,552,553]):
                    pass
                elif faces.remove([548,549,550]):
                    pass
                elif faces.remove([546,547,548]):
                    pass
                elif faces.remove([547,548,549]):
                    pass
                elif faces.remove([450,451,452]):
                    pass
                elif faces.remove([452,453,454]):
                    pass
                elif faces.remove([453,454,455]):
                    pass
                elif faces.remove([632,633,634]):
                    pass
                elif faces.remove([448,449,450]):
                    pass
                elif faces.remove([449,450,451]):
                    pass
                elif faces.remove([757,758,759]):
                    pass
                elif faces.remove([684,685,686]):
                    pass
                elif faces.remove([683,684,685]):
                    pass
                elif faces.remove([340,341,342]):
                    pass
                elif faces.remove([361,362,363]):
                    pass
                elif faces.remove([362,363,364]):
                    pass
                elif faces.remove([290,291,292]):
                    pass
                elif faces.remove([274,275,276]):
                    pass
                elif faces.remove([386,387,388]):
                    pass
                elif faces.remove([272,273,274]):
                    pass
                elif faces.remove([404,405,406]):
                    pass
                elif faces.remove([422,423,424]):
                    pass
                elif faces.remove([420,421,422]):
                    pass
                elif faces.remove([421,422,423]):
                    pass
                elif faces.remove([325,326,327]):
                    pass
                elif faces.remove([324,325,326]):
                    pass
                elif faces.remove([30,31,32]):
                    pass
                elif faces.remove([29,30,31]):
                    pass
                elif faces.remove([6,7,8]):
                    pass
                elif faces.remove([5,6,7]):
                    pass
                elif faces.remove([36,37,38]):
                    pass
                elif faces.remove([377,378,379]):
                    pass
                elif faces.remove([345,346,347]):
                    pass
                elif faces.remove([718,719,720]):
                    pass
                elif faces.remove([276,277,278]):
                    pass
                elif faces.remove([384,385,386]):
                    pass
                elif faces.remove([802,803,804]):
                    pass
                elif faces.remove([803,804,805]):
                    pass
                elif faces.remove([424,425,426]):
                    pass
                elif faces.remove([810,811,812]):
                    pass
                elif faces.remove([796,797,798]):
                    pass
                elif faces.remove([831,832,833]):
                    pass
                elif faces.remove([832,833,834]):
                    pass
                elif faces.remove([808,809,810]):
                    pass
                elif faces.remove([809,810,811]):
                    pass
                elif faces.remove([814,815,816]):
                    pass
                elif faces.remove([813,814,815]):
                    pass
                elif faces.remove([423,424,425]):
                    pass
                elif faces.remove([830,831,832]):
                    pass
                elif faces.remove([851,852,853]):
                    pass
                elif faces.remove([817,818,819]):
                    pass
                elif faces.remove([717,718,719]):
                    pass
                elif faces.remove([341,342,343]):
                    pass
                elif faces.remove([346,347,348]):
                    pass
                elif faces.remove([666,667,668]):
                    pass
                elif faces.remove([192,193,194]):
                    pass
                elif faces.remove([231,232,233]):
                    pass
                elif faces.remove([464,465,466]):
                    pass
                elif faces.remove([208,209,210]):
                    pass
                elif faces.remove([230,231,232]):
                    pass
                elif faces.remove([229,230,231]):
                    pass
                elif faces.remove([474,475,476]):
                    pass
                elif faces.remove([257,258,259]):
                    pass
                elif faces.remove([256,257,258]):
                    pass
                elif faces.remove([250,251,252]):
                    pass
                elif faces.remove([255,256,257]):
                    pass
                elif faces.remove([447,448,449]):
                    pass
                elif faces.remove([451,452,453]):
                    pass
                elif faces.remove([874,875,876]):
                    pass
                elif faces.remove([503,504,505]):
                    pass
                elif faces.remove([855,856,857]):
                    pass
                elif faces.remove([850,851,852]):
                    pass
                elif faces.remove([856,857,858]):
                    pass
                elif faces.remove([849,850,851]):
                    pass
                elif faces.remove([845,846,847]):
                    pass
                elif faces.remove([846,847,848]):
                    pass
                elif faces.remove([847,848,849]):
                    pass
                elif faces.remove([854,855,856]):
                    pass
                elif faces.remove([853,854,855]):
                    pass
                elif faces.remove([852,853,854]):
                    pass
                elif faces.remove([812,813,814]):
                    pass
                elif faces.remove([419,420,421]):
                    pass
                elif faces.remove([570,571,572]):
                    pass
                elif faces.remove([589,590,591]):
                    pass
                elif faces.remove([590,591,592]):
                    pass
                elif faces.remove([592,593,594]):
                    pass
                elif faces.remove([491,492,493]):
                    pass
                elif faces.remove([492,493,494]):
                    pass
                elif faces.remove([493,494,495]):
                    pass
                elif faces.remove([594,595,596]):
                    pass
                elif faces.remove([446,447,448]):
                    pass
                elif faces.remove([433,434,435]):
                    pass
                elif faces.remove([541,542,543]):
                    pass
                elif faces.remove([540,541,542]):
                    pass
                elif faces.remove([413,414,415]):
                    pass
                elif faces.remove([417,418,419]):
                    pass
                elif faces.remove([416,417,418]):
                    pass
                elif faces.remove([418,419,420]):
                    pass
                elif faces.remove([414,415,416]):
                    pass
                elif faces.remove([523,524,525]):
                    pass
                elif faces.remove([522,523,524]):
                    pass
                elif faces.remove([521,522,523]):
                    pass
                elif faces.remove([328,329,330]):
                    pass
                elif faces.remove([327,328,329]):
                    pass
                elif faces.remove([326,327,328]):
                    pass
                elif faces.remove([432,433,434]):
                    pass
                elif faces.remove([538,539,540]):
                    pass
                elif faces.remove([584,585,586]):
                    pass
                elif faces.remove([585,586,587]):
                    pass
                elif faces.remove([738,739,740]):
                    pass
                elif faces.remove([771,772,773]):
                    pass
                elif faces.remove([744,745,746]):
                    pass
                elif faces.remove([768,769,770]):
                    pass
                elif faces.remove([769,770,771]):
                    pass
                elif faces.remove([770,771,772]):
                    pass
                elif faces.remove([739,740,741]):
                    pass
                elif faces.remove([730,731,732]):
                    pass
                elif faces.remove([743,744,745]):
                    pass
                elif faces.remove([767,768,769]):
                    pass
                elif faces.remove([699,700,701]):
                    pass
                elif faces.remove([68,69,70]):
                    pass
                elif faces.remove([69,70,71]):
                    pass
                elif faces.remove([71,72,73]):
                    pass
                elif faces.remove([321,322,323]):
                    pass
                elif faces.remove([322,323,324]):
                    pass
                elif faces.remove([323,324,325]):
                    pass
                elif faces.remove([50,51,52]):
                    pass
                elif faces.remove([59,60,61]):
                    pass
                elif faces.remove([58,59,60]):
                    pass
                elif faces.remove([61,62,63]):
                    pass
                elif faces.remove([552,553,554]):
                    pass
                elif faces.remove([100,101,102]):
                    pass
                elif faces.remove([104,105,106]):
                    pass
                elif faces.remove([106,107,108]):
                    pass
                elif faces.remove([105,106,107]):
                    pass
                elif faces.remove([99,100,101]):
                    pass
                elif faces.remove([98,99,100]):
                    pass
                elif faces.remove([101,102,103]):
                    pass
                elif faces.remove([95,96,97]):
                    pass
                elif faces.remove([94,95,96]):
                    pass
                elif faces.remove([103,104,105]):
                    pass
                elif faces.remove([102,103,104]):
                    pass
                elif faces.remove([96,97,98]):
                    pass
                elif faces.remove([97,98,99]):
                    pass
                elif faces.remove([991,992,993]):
                    pass
                elif faces.remove([992,993,994]):
                    pass
                elif faces.remove([1001,1002,1003]):
                    pass
                elif faces.remove([1002,1003,1004]):
                    pass
                elif faces.remove([995,996,997]):
                    pass
                elif faces.remove([994,995,996]):
                    pass
                elif faces.remove([380,381,382]):
                    pass
                elif faces.remove([732,733,734]):
                    pass
                elif faces.remove([764,765,766]):
                    pass
                elif faces.remove([765,766,767]):
                    pass
                elif faces.remove([766,767,768]):
                    pass
                elif faces.remove([731,732,733]):
                    pass
                elif faces.remove([54,55,56]):
                    pass
                elif faces.remove([53,54,55]):
                    pass
                elif faces.remove([51,52,53]):
                    pass
                elif faces.remove([46,47,48]):
                    pass
                elif faces.remove([1000,1001,1002]):
                    pass
                elif faces.remove([967,968,969]):
                    pass
                elif faces.remove([109,110,111]):
                    pass
                elif faces.remove([475,476,477]):
                    pass
                elif faces.remove([483,484,485]):
                    pass
                elif faces.remove([482,483,484]):
                    pass
                elif faces.remove([896,897,898]):
                    pass
                elif faces.remove([897,898,899]):
                    pass
                elif faces.remove([815,816,817]):
                    pass
                elif faces.remove([887,888,889]):
                    pass
                elif faces.remove([888,889,890]):
                    pass
                elif faces.remove([618,619,620]):
                    pass
                elif faces.remove([818,819,820]):
                    pass
                elif faces.remove([571,572,573]):
                    pass
                elif faces.remove([821,822,823]):
                    pass
                elif faces.remove([574,575,576]):
                    pass
                elif faces.remove([398,399,400]):
                    pass
                elif faces.remove([344,345,346]):
                    pass
                elif faces.remove([338,339,340]):
                    pass
                elif faces.remove([686,687,688]):
                    pass
                elif faces.remove([337,338,339]):
                    pass
                elif faces.remove([687,688,689]):
                    pass
                elif faces.remove([688,689,690]):
                    pass
                elif faces.remove([822,823,824]):
                    pass
                elif faces.remove([539,540,541]):
                    pass
                elif faces.remove([816,817,818]):
                    pass
                elif faces.remove([189,190,191]):
                    pass
                elif faces.remove([161,162,163]):
                    pass
                elif faces.remove([188,189,190]):
                    pass
                elif faces.remove([209,210,211]):
                    pass
                elif faces.remove([210,211,212]):
                    pass
                elif faces.remove([187,188,189]):
                    pass
                elif faces.remove([166,167,168]):
                    pass
                elif faces.remove([168,169,170]):
                    pass
                elif faces.remove([167,168,169]):
                    pass
                elif faces.remove([176,177,178]):
                    pass
                elif faces.remove([252,253,254]):
                    pass
                elif faces.remove([251,252,253]):
                    pass
                elif faces.remove([254,255,256]):
                    pass
                elif faces.remove([253,254,255]):
                    pass
                elif faces.remove([184,185,186]):
                    pass
                elif faces.remove([185,186,187]):
                    pass
                elif faces.remove([180,181,182]):
                    pass
                elif faces.remove([181,182,183]):
                    pass
                elif faces.remove([748,749,750]):
                    pass
                elif faces.remove([719,720,721]):
                    pass
                elif faces.remove([715,716,717]):
                    pass
                elif faces.remove([714,715,716]):
                    pass
                elif faces.remove([681,682,683]):
                    pass
                elif faces.remove([383,384,385]):
                    pass
                elif faces.remove([382,383,384]):
                    pass
                elif faces.remove([381,382,383]):
                    pass
                elif faces.remove([701,702,703]):
                    pass
                elif faces.remove([695,696,697]):
                    pass
                elif faces.remove([700,701,702]):
                    pass
                elif faces.remove([273,274,275]):
                    pass
                elif faces.remove([988,989,990]):
                    pass
                elif faces.remove([777,778,779]):
                    pass
                elif faces.remove([565,566,567]):
                    pass
                elif faces.remove([505,506,507]):
                    pass
                elif faces.remove([393,394,395]):
                    pass
                elif faces.remove([563,564,565]):
                    pass
                elif faces.remove([28,29,30]):
                    pass
                elif faces.remove([27,28,29]):
                    pass
                elif faces.remove([25,26,27]):
                    pass
                elif faces.remove([24,25,26]):
                    pass
                elif faces.remove([18,19,20]):
                    pass
                elif faces.remove([32,33,34]):
                    pass
                elif faces.remove([4,5,6]):
                    pass
                elif faces.remove([2,3,4]):
                    pass
                elif faces.remove([31,32,33]):
                    pass
                elif faces.remove([753,754,755]):
                    pass
                elif faces.remove([751,752,753]):
                    pass
                elif faces.remove([749,750,751]):
                    pass
                elif faces.remove([343,344,345]):
                    pass
                elif faces.remove([487,488,489]):
                    pass
                elif faces.remove([562,563,564]):
                    pass
                elif faces.remove([561,562,563]):
                    pass
                elif faces.remove([892,893,894]):
                    pass
                #appending
                elif faces.append([565,567,566]):
                    pass
                elif faces.append([563,567,565]):
                    pass
                elif faces.append([393,395,394]):
                    pass
                elif faces.append([563,565,564]):
                    pass
                elif faces.append([27,29,28]):
                    pass
                elif faces.append([25,27,26]):
                    pass
                elif faces.append([20,27,25]):
                    pass
                elif faces.append([18,20,19]):
                    pass
                elif faces.append([19,20,32]):
                    pass
                elif faces.append([19,29,27]):
                    pass
                elif faces.append([4,6,5]):
                    pass
                elif faces.append([2,4,3]):
                    pass
                elif faces.append([31,33,32]):
                    pass
                elif faces.append([563,567,565]):
                    pass
                elif faces.append([753,755,754]):
                    pass
                elif faces.append([751,753,752]):
                    pass
                elif faces.append([749,751,750]):
                    pass
                elif faces.append([343,345,344]):
                    pass
                elif faces.append([487,489,488]):
                    pass
                elif faces.append([562,599,601]):
                    pass
                elif faces.append([561,563,562]):
                    pass
                elif faces.append([926,893,927]):
                    pass
                elif faces.append([926,892,893]):
                    pass
                

    if os.path.basename(filepath) == r"deb.ghg":
        

        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)

        for fac in mesh.polygons:
            fac.use_smooth = True
