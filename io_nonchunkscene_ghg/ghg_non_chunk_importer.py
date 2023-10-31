from struct import pack, unpack
from io import BytesIO as bio
import os
import bpy
import mathutils
import math
import bmesh
from. GHG_Import.Games.Nemo.Bubble.bubble import *
from. GHG_Import.Games.Nemo.Anemone.anemone import *
from. GHG_Import.Games.Nemo.Key.key import *

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

def GHG_entire_weights(f):
    pass

def GHG_vertex_entire_vc1(f):
    pass

def GHG_whole_entire_uv1(f, uvs=[]):
    obdata = bpy.context.object.data
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    for i in range(len(Chunk)):
        Chunk_ = f.read(4)
        if Chunk_ == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexcountskip = unpack("B", f.read(1))[0] # skip vertex data
            f.seek(1,1)
            for i in range(vertexcountskip):
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
            f.seek(6,1)
            uvCount1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(uvCount1):
                uvx = unpack("<h", f.read(2))[0] / 4096.0
                uvy = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(4,1)
                uvs.append([uvx,uvy])
            uv_tex = obdata.uv_layers.new()
            uv_layer = obdata.uv_layers[0].data
            vert_loops = {}
            for l in obdata.loops:
                vert_loops.setdefault(l.vertex_index, []).append(l.index)
            for i, coord in enumerate(uvs):
                for li in vert_loops[i]:
                    uv_layer[li].uv = coord
def GHG_whole_entire_uv2(f):
    obdata = bpy.context.object.data
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    uvs=[]
    for i in range(len(Chunk)):
        Chunk_ = f.read(4)
        if Chunk_ == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexcountskip = unpack("B", f.read(1))[0] // 2 # skip vertex data
            f.seek(1,1)
            for i in range(vertexcountskip):
                f.seek(2,1)
                f.seek(2,1)
                f.seek(2,1)
                f.seek(2,1)
                f.seek(8,1)
            f.seek(30,1)
            vertexColor1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexColor1):
                f.seek(1,1)
                f.seek(1,1)
                f.seek(1,1)
                f.seek(1,1)
            f.seek(34,1)
            uvCount1 = unpack("B", f.read(1))[0]*2
            f.seek(1,1)
            for i in range(uvCount1):
                uvx = unpack("B", f.read(1))[0] / 255.0
                uvy = unpack("B", f.read(1))[0] / 255.0
                uvs.append([uvx,uvy])
            uv_tex = obdata.uv_layers.new()
            uv_layer = obdata.uv_layers[0].data
            vert_loops = {}
            for l in obdata.loops:
                vert_loops.setdefault(l.vertex_index, []).append(l.index)
            for i, coord in enumerate(uvs):
                for li in vert_loops[i]:
                    uv_layer[li].uv = coord
def GHG_whole_entire_uv3(f):
    pass
                    

def GHG_whole_entire_bones(f, filepath):

    boneIndex = -1

    Coordinates=[]

    bone_parentlist=[]
        
    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')
    f.seek(0)
    FileSize = unpack("<I", f.read(4))[0]
    unk = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    Texture_EntrySize = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    Material_EntrySize = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    SclBoneEntrySize = unpack("<I", f.read(4))[0]
    PosBoneEntrySize = unpack("<I", f.read(4))[0]
    RotBoneEntrySize = unpack("<I", f.read(4))[0]
    Unk_ = unpack("<I", f.read(4))[0]
    Unk__ = unpack("<I", f.read(4))[0]
    EndMaterialEntrySize = unpack("<I", f.read(4))[0]
    NamedtableEntrySize,=unpack("<I", f.read(4))
    f.seek(EndMaterialEntrySize-56,1)
    ntbl_buffer = bio(f.read(NamedtableEntrySize))
    name_i = 0
    while 1:
        name = fetch_cstr(ntbl_buffer).decode('ascii')
        if not name: break
        name_i +=1
    f.seek(0)
    f.seek(32,1)
    f.seek(SclBoneEntrySize-32,1)

    for i in range(BoneCount):
        f.seek(64,1)
        bdiv4_v00 = unpack("<f", f.read(4))[0]
        bdiv4_v04 = unpack("<f", f.read(4))[0]
        bdiv4_v08 = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        bone_parent,=unpack("b", f.read(1))
        bone_parentlist.append(bone_parent)
        #ntbl_buffer.seek(name_offset - 1) or ntbl_buffer.seek(name_offset)
        #bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
        name_offset,=unpack("<L", f.read(4)) # WHAT doesnt work
        ntbl_buffer.seek(name_offset-1)
        f.seek(11,1)
            
    f.seek(0)
    f.seek(36,1)
    f.seek(RotBoneEntrySize-36,1)
    for i in range(BoneCount):
        ScaleX = unpack("<f", f.read(4))[0]
        RotZ = unpack("<f", f.read(4))[0]
        RotY = unpack("<f", f.read(4))[0]
        unk1 = unpack("<f", f.read(4))[0]
        _RotZ = unpack("<f", f.read(4))[0]
        ScaleY = unpack("<f", f.read(4))[0]
        RotX = unpack("<f", f.read(4))[0]
        _RotY = unpack("<f", f.read(4))[0]
        unk2 = unpack("<f", f.read(4))[0]
        _RotX = unpack("<f", f.read(4))[0]
        ScaleZ = unpack("<f", f.read(4))[0]
        unk3 = unpack("<f", f.read(4))[0]
        posx = unpack("<f", f.read(4))[0]
        posy = unpack("<f", f.read(4))[0]
        posz = unpack("<f", f.read(4))[0]
        unk4 = unpack("<f", f.read(4))[0]
        Coordinates.append([1, RotZ, RotY, unk1, _RotZ, 1, RotX, _RotY, unk2, _RotX, 1, unk3, posx,posy,posz,unk4])

        bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
        bone = skel.edit_bones.new(bone_name)

        bone.head = (
            +posx,
            +posz,
            +posy,
	)
        bone.tail = (
            bone.head[0],
            bone.head[1],
            bone.head[2] + 0.03,
        )
    #bone.roll = RotZ
    for bone_id, bone_parent in enumerate(bone_parentlist):
        if bone_parent < 0: continue # root bone is set to -1
        skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
    bpy.ops.object.mode_set(mode = 'OBJECT')



"""def GHG_whole_beta_1(f, filepath):
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
            for i in range(vertexCount):
                vx = unpack("<i", f.read(4))[0]
                vy = unpack("<i", f.read(4))[0]
                vz = unpack("<i", f.read(4))[0]
                f.seek(4,1)
                if vx == 1042695906:
                    vertx1 = 0.1623
                    #vertx3 = 0.1623
                if vy == -1103101953:
                    verty1 = 0.2812
                if vz == 1049624575:
                    vertz1 = -0.1874
                elif vx == 1035993088:
                    vertx2 = 0.0937
                elif vy == -1096399135:
                    verty2 = 0.1623
                    verty3 = -0.3247
                elif vz == 1042695904:
                    vertz2 = -0.3247
                elif vz == 1035993085:
                    vertz3 = 0.0937
                elif vx == 1049624576:
                    pass
                elif vz == 1042695903:
                    pass
                new_vertices_bubble=([0.2812,0.1623,-0.1874],[0.1623,0.0937,-0.3247],[0.1623,0.2812,-0.1874],
                                     [vertx1,verty1,vertz1],[0.1623,0.0937,-0.3247],[0.0937,0.1623,-0.3247],
                                     [0.1623,0.2812,-0.1874],[0.0937,0.1623,-0.3247],[0.0000,0.3247,-0.1874],
                                     [0.0000,0.3247,-0.1874],[0.0937, 0.1623, -0.3247],[0.0000,0.1874,-0.3247],
                                     [0.0000,0.3247,-0.1874],[0.0000,0.1874,-0.3247],[-0.1623, 0.2812,-0.1874],
                                     [0.0000,0.1874,-0.3247],[-0.0937,0.1623,-0.3247],[-0.1623, 0.2812,-0.1874],
                                     [-0.1623, 0.2812,-0.1874],[-0.0937,0.1623,-0.3247],[-0.2812,0.1623,-0.1874],
                                     [-0.0937,0.1623,-0.3247],[-0.2812,0.1623,-0.1874],[0.0000,0.0000,0.0000])

                new_faces_bubble=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23]]
            for i in range(vertexCount):
                f.seek(-4,1)
                f.seek(-4,1)
                f.seek(-4,1)
                f.seek(-4,1)
                                            
                            
            for i in range(vertexCount//3):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                vx1 = unpack("<f", f.read(4))[0]
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

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.to_mesh(mesh)
    
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    for face in mesh.polygons:
        face.use_smooth=True
    bm.from_mesh(mesh)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
        

    bm.to_mesh(mesh)

    bpy.data.meshes.remove(mesh)

    if os.path.basename(filepath) == r"bubble.ghg":

        try:
            
        

            new_mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
            new_mesh.from_pydata(new_vertices_bubble, [], new_faces_bubble)
            new_object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), new_mesh)
            bpy.context.collection.objects.link(new_object)

        except:
            pass"""

    

def GHG_whole_beta_2(f, filepath):
    bm = bmesh.new()
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    meshes = {}
    fa = 0
    fb = 0
    fc = 0
    faces=[]
    os.system("cls")
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount//3):
                vx1 = unpack("<h", f.read(2))[0] / 4096.0
                vy1 = unpack("<h", f.read(2))[0] / 4096.0
                vz1 = unpack("<h", f.read(2))[0] / 4096.0
                nz1 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vx2 = unpack("<h", f.read(2))[0] / 4096.0
                vy2 = unpack("<h", f.read(2))[0] / 4096.0
                vz2 = unpack("<h", f.read(2))[0] / 4096.0
                nz2 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vx3 = unpack("<h", f.read(2))[0] / 4096.0
                vy3 = unpack("<h", f.read(2))[0] / 4096.0
                vz3 = unpack("<h", f.read(2))[0] / 4096.0
                nz3 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                verts1 = bm.verts.new([vx1,vz1,vy1])
                verts2 = bm.verts.new([vx2,vz2,vy2])
                verts3 = bm.verts.new([vx3,vz3,vy3])

                bm.faces.new([verts1,verts3,verts2])

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.to_mesh(mesh)
    
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    for face in mesh.polygons:
        face.use_smooth=True
    bm.from_mesh(mesh)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
        

    bm.to_mesh(mesh)

def GHG_whole_beta_3(f, filepath):
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

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

    for fac in mesh.polygons:
        fac.use_smooth = True
    
            
    

def NonParseGHG(filepath, GHG_Bones=1, GHG_Name=""):
    with open(filepath, "rb") as f:
        
        if GHG_Name == "bubble":
            GHG_whole_beta_Bubble(f, filepath)
        if GHG_Name == "anemone":
            GHG_whole_beta_Anemone(f, filepath)
        if GHG_Name == "key":
            GHG_whole_beta_Key(f, filepath)
        
        if GHG_Bones == 1:
            GHG_whole_entire_bones(f, filepath)
                
        
                
        
        
        
