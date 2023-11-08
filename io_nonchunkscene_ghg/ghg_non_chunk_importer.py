from struct import pack, unpack
from io import BytesIO as bio
import os
import bpy
import mathutils
import math
import bmesh

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



def GHG_whole_beta_1(f, filepath):
    if os.path.basename(filepath) == r"key.ghg":
        f.seek(0)
        ChunkRead = f.read()
        f.seek(0)
        meshes={}
        normals=[]
        rgba=[]
        uvs=[]

        fa=-1
        fb=0
        fc=1

        faces=[]
        vertices=[]

        os.system("cls")

        face_index_search = 0

        f.seek(0)
        Chunk = f.read()
        f.seek(0)
        for i in range(len(Chunk)):
            Chunks = f.read(4)
            if Chunk == b"\x03\x01\x00\x01":
                f.seek(2,1)
                vertexCount = unpack("B", f.read(1))[0]
                flag = unpack("B", f.read(1))[0]
                for i in range(vertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    magicFaceExponents = unpack("<Q", f.read(8))[0]
                    f.seek(-8,1)
                    f.seek(4,1)
                    vertices.append([vx,vz,vy])
                    normals.append([0,0, 1])
                    for i in range(1):
                        if magicFaceExponents == 4441297034452369409:
                            for i in range(122):
                                
                                faces.append([i - i % 2 + 1,i + i % 2,i + 2])
                            if faces.remove([43, 44, 45]):
                                pass
                            
                            elif faces.remove([43, 42, 44]):
                                pass
                            elif faces.remove([19, 18,20]):
                                pass
                            elif faces.remove([19,20, 21]):
                                pass
                            elif faces.remove([67, 66,68]):
                                pass
                            
                            elif faces.remove([67,68,69]):
                                pass
                            
                            
                            
                            elif faces.remove([47,46,48]):
                                pass
                            elif faces.remove([73,72,74]):
                                pass
                            elif faces.remove([73,74,75]):
                                pass
                            elif faces.remove([47,48,49]):
                                pass
                            elif faces.remove([93,92,94]):
                                pass
                            elif faces.remove([93,94,95]):
                                pass
                            elif faces.remove([99,100,101]):
                                pass
                            elif faces.remove([99,98,100]):
                                pass
                            elif faces.remove([25,24,26]):
                                pass
                            elif faces.remove([25,26,27]):
                                pass
                            elif faces.remove([111,112,113]):
                                pass
                            elif faces.remove([115,116,117]):
                                pass
                            elif faces.remove([115,114,116]):
                                pass
                            elif faces.remove([111,110,112]):
                                pass
                            elif faces.remove([119,120,121]):
                                pass
                            elif faces.remove([119,118,120]):
                                pass
                            elif faces.remove([107,108,109]):
                                pass
                            elif faces.remove([107,106,108]):
                                pass
                                
                            break
                        elif magicFaceExponents == 13617892458184736769:
                            faceA = magicFaceExponents**0-1
                            faceB = magicFaceExponents**0
                            faceC = magicFaceExponents**0+1
                        
                            faces.append([faceA,faceB,faceC])
                f.seek(2,1)
                uvcount = unpack("B", f.read(1))[0]
                f.seek(1,1)
                for i in range(uvcount):
                    uvx = unpack("<h", f.read(2))[0] / 4096.0
                    uvy = unpack("<h", f.read(2))[0] / 4096.0
                    f.seek(4,1) #not sure
                    uvs.append([uvx,uvy])
                        
                f.seek(2,1)
                vertexcolorCount = unpack("B", f.read(1))[0]
                flag = unpack("B", f.read(1))[0]
                for i in range(vertexcolorCount):
                    r = unpack("B", f.read(1))[0] / 127.0
                    g = unpack("B", f.read(1))[0] / 127.0
                    b = unpack("B", f.read(1))[0] / 127.0
                    a = unpack("B", f.read(1))[0] / 127.0
                    rgba.append([r,g,b,a])
        f.seek(0)
        MaterialChunkReach = f.read(16)
        MaterialCount = unpack("<I", f.read(4))[0]
        MaterialEntrySize1 = unpack("<I", f.read(4))[0]
        f.seek(MaterialEntrySize1-24,1)
        for i in range(MaterialCount):
            matByte1 = unpack("B", f.read(1))[0]
            matByte2 = unpack("B", f.read(1))[0]
            matByte3 = unpack("B", f.read(1))[0]
            matByte4 = unpack("B", f.read(1))[0]
            matByte5 = unpack("B", f.read(1))[0]
            matByte6 = unpack("B", f.read(1))[0]
            matByte7 = unpack("B", f.read(1))[0]
            matByte8 = unpack("B", f.read(1))[0]
            matByte9 = unpack("B", f.read(1))[0]
            matByte10 = unpack("B", f.read(1))[0]
            matByte11 = unpack("B", f.read(1))[0]
            matByte12 = unpack("B", f.read(1))[0]
            matByte13 = unpack("B", f.read(1))[0]
            matByte14 = unpack("B", f.read(1))[0]
            matByte15 = unpack("B", f.read(1))[0]
            matByte16 = unpack("B", f.read(1))[0]
            matByte17 = unpack("B", f.read(1))[0]
            matByte18 = unpack("B", f.read(1))[0]
            matByte19 = unpack("B", f.read(1))[0]
            matByte20 = unpack("B", f.read(1))[0]
            matByte21 = unpack("B", f.read(1))[0]
            matByte22 = unpack("B", f.read(1))[0]
            matByte23 = unpack("B", f.read(1))[0]
            matByte24 = unpack("B", f.read(1))[0]
            matByte25 = unpack("B", f.read(1))[0]
            matByte26 = unpack("B", f.read(1))[0]
            matByte27 = unpack("B", f.read(1))[0]
            matByte28 = unpack("B", f.read(1))[0]
            matByte29 = unpack("B", f.read(1))[0]
            matByte30 = unpack("B", f.read(1))[0]
            matByte31 = unpack("B", f.read(1))[0]
            matByte32 = unpack("B", f.read(1))[0]
            matByte33 = unpack("B", f.read(1))[0]
            matByte34 = unpack("B", f.read(1))[0]
            matByte35 = unpack("B", f.read(1))[0]
            matByte36 = unpack("B", f.read(1))[0]
            matByte37 = unpack("B", f.read(1))[0]
            matByte38 = unpack("B", f.read(1))[0]
            matByte39 = unpack("B", f.read(1))[0]
            matByte40 = unpack("B", f.read(1))[0]
            matByte41 = unpack("B", f.read(1))[0]
            matByte42 = unpack("B", f.read(1))[0]
            matByte43 = unpack("B", f.read(1))[0]
            matByte44 = unpack("B", f.read(1))[0]
            matByte45 = unpack("B", f.read(1))[0]
            matByte46 = unpack("B", f.read(1))[0]
            matByte47 = unpack("B", f.read(1))[0]
            matByte48 = unpack("B", f.read(1))[0]
            matByte49 = unpack("B", f.read(1))[0]
            matByte50 = unpack("B", f.read(1))[0]
            matByte51 = unpack("B", f.read(1))[0]
            matByte52 = unpack("B", f.read(1))[0]
            matByte53 = unpack("B", f.read(1))[0]
            matByte54 = unpack("B", f.read(1))[0]
            matByte55 = unpack("B", f.read(1))[0]
            matByte56 = unpack("B", f.read(1))[0]
            matByte57 = unpack("B", f.read(1))[0]
            matByte58 = unpack("B", f.read(1))[0]
            matByte59 = unpack("B", f.read(1))[0]
            matByte60 = unpack("B", f.read(1))[0]
            matByte61 = unpack("B", f.read(1))[0]
            matByte62 = unpack("B", f.read(1))[0]
            matByte63 = unpack("B", f.read(1))[0]
            matByte64 = unpack("B", f.read(1))[0]
            matByte65 = unpack("B", f.read(1))[0]
            matByte66 = unpack("B", f.read(1))[0]
            matByte67 = unpack("B", f.read(1))[0]
            matByte68 = unpack("B", f.read(1))[0]
            matByte69 = unpack("B", f.read(1))[0]
            matByte70 = unpack("B", f.read(1))[0]
            matByte71 = unpack("B", f.read(1))[0]
            matByte72 = unpack("B", f.read(1))[0]
            matByte73 = unpack("B", f.read(1))[0]
            matByte74 = unpack("B", f.read(1))[0]
            matByte75 = unpack("B", f.read(1))[0]
            matByte76 = unpack("B", f.read(1))[0]
            matByte77 = unpack("B", f.read(1))[0]
            matByte78 = unpack("B", f.read(1))[0]
            matByte79 = unpack("B", f.read(1))[0]
            matByte80 = unpack("B", f.read(1))[0]
            matByte81 = unpack("B", f.read(1))[0]
            matByte82 = unpack("B", f.read(1))[0]
            matByte83 = unpack("B", f.read(1))[0]
            matByte84 = unpack("B", f.read(1))[0]
            matByte85 = unpack("B", f.read(1))[0]
            matByte86 = unpack("B", f.read(1))[0]
            matByte87 = unpack("B", f.read(1))[0]
            matByte88 = unpack("B", f.read(1))[0]
            matByte89 = unpack("B", f.read(1))[0]
            matByte90 = unpack("B", f.read(1))[0]
            matByte91 = unpack("B", f.read(1))[0]
            matByte92 = unpack("B", f.read(1))[0]
            matByte93 = unpack("B", f.read(1))[0]
            matByte94 = unpack("B", f.read(1))[0]
            matByte95 = unpack("B", f.read(1))[0]
            matByte96 = unpack("B", f.read(1))[0]
            matByte97 = unpack("B", f.read(1))[0]
            matByte98 = unpack("B", f.read(1))[0]
            matByte99 = unpack("B", f.read(1))[0]
            matByte100 = unpack("B", f.read(1))[0]
            matByte101 = unpack("B", f.read(1))[0]
            matByte102 = unpack("B", f.read(1))[0]
            matByte103 = unpack("B", f.read(1))[0]
            matByte104 = unpack("B", f.read(1))[0]
            matByte105 = unpack("B", f.read(1))[0]
            matByte106 = unpack("B", f.read(1))[0]
            matByte107 = unpack("B", f.read(1))[0]
            matByte108 = unpack("B", f.read(1))[0]
            matByte109 = unpack("B", f.read(1))[0]
            matByte110 = unpack("B", f.read(1))[0]
            matByte111 = unpack("B", f.read(1))[0]
            matByte112 = unpack("B", f.read(1))[0]
            matByte113 = unpack("B", f.read(1))[0]
            matByte114 = unpack("B", f.read(1))[0]
            matByte115 = unpack("B", f.read(1))[0]
            matByte116 = unpack("B", f.read(1))[0]
            matByte117 = unpack("B", f.read(1))[0]
            matByte118 = unpack("B", f.read(1))[0]
            matByte119 = unpack("B", f.read(1))[0]
            matByte120 = unpack("B", f.read(1))[0]
            matByte121 = unpack("B", f.read(1))[0]
            matByte122 = unpack("B", f.read(1))[0]
            matByte123 = unpack("B", f.read(1))[0]
            matByte124 = unpack("B", f.read(1))[0]
            matByte125 = unpack("B", f.read(1))[0]
            matByte126 = unpack("B", f.read(1))[0]
            matByte127 = unpack("B", f.read(1))[0]
            matByte128 = unpack("B", f.read(1))[0]
            matByte129 = unpack("B", f.read(1))[0]
            matByte130 = unpack("B", f.read(1))[0]
            matByte131 = unpack("B", f.read(1))[0]
            matByte132 = unpack("B", f.read(1))[0]
            matByte133 = unpack("B", f.read(1))[0]
            matByte134 = unpack("B", f.read(1))[0]
            matByte135 = unpack("B", f.read(1))[0]
            matByte136 = unpack("B", f.read(1))[0]
            matByte137 = unpack("B", f.read(1))[0]
            matByte138 = unpack("B", f.read(1))[0]
            matByte139 = unpack("B", f.read(1))[0]
            matByte140 = unpack("B", f.read(1))[0]
            matByte141 = unpack("B", f.read(1))[0]
            matByte142 = unpack("B", f.read(1))[0]
            matByte143 = unpack("B", f.read(1))[0]
            matByte144 = unpack("B", f.read(1))[0]
            matByte145 = unpack("B", f.read(1))[0]
            matByte146 = unpack("B", f.read(1))[0]
            matByte147 = unpack("B", f.read(1))[0]
            matByte148 = unpack("B", f.read(1))[0]
            matByte149 = unpack("B", f.read(1))[0]
            matByte150 = unpack("B", f.read(1))[0]
            subSurfaceColorCount = unpack("B", f.read(1))[0]
            flag_ = unpack("B", f.read(1))[0]
            for i in range(subSurfaceColorCount+1):
                subSurfaceColorCountRed     = unpack("<f", f.read(4))[0]
                subSurfaceColorCountGreen   = unpack("<f", f.read(4))[0]
                subSurfaceColorCountBlue    = unpack("<f", f.read(4))[0]
                subSurfaceColorCountAlpha   = unpack("<f", f.read(4))[0]
            ramMaterialStuff = f.read(284) # only appears in ram only
            MaterialFlag = unpack("<I", f.read(4))[0]
            if MaterialFlag == 29:
                f.seek(32,1) # skip this don't need this, since trace it in ram
                red1    = unpack("<I", f.read(4))[0] / 4294967295
                green1  = unpack("<I", f.read(4))[0] / 4294967295
                blue1   = unpack("<I", f.read(4))[0] / 4294967295

        BSDF = "Principled BSDF"
        vmesh = "dragonjanCol"
        meshID = len(bpy.data.objects)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        mesh.normals_split_custom_set_from_vertices(normals)
        bpy.context.collection.objects.link(object)
        mesh.vertex_colors.new(name=vmesh)

        for fac in mesh.polygons:
            fac.use_smooth = True

        vindex = 0
        for vertex in mesh.vertices:
            vertex.normal = normals[vindex]
            vindex += 1
            
        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
                
        index=0
        for vcol in mesh.vertex_colors[0].data:
            vcol.color = rgba[i]
            index+=i

        NU_MIX_MODE = 'ShaderNodeMixRGB'
        NU_RGBA_VERT = 'ShaderNodeVertexColor'
        MaterialName = "dragonjan Material"

        name=0

        obj = bpy.data.objects[name]
        mats = bpy.data.materials.new("dragonjan Material")
        obj.data.materials.append(mats)

        previous_mix = None
        previous_rgba = None

        for i, mat in enumerate(bpy.data.materials):
            mat.use_nodes = True
            bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
            bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
            #bpy.data.node.add_search(use_transform=True, node_item=items)
            mat.blend_method = "HASHED"
            mix = mat.node_tree.nodes.new(NU_MIX_MODE)
            rgbaV = mat.node_tree.nodes.new(NU_RGBA_VERT)
            mat.node_tree.nodes["Mix"].blend_type = 'MULTIPLY'
            mat.node_tree.nodes["Mix"].inputs[0].default_value = 1
            bpy.data.materials[MaterialName].node_tree.nodes["Vertex Color"].layer_name = vmesh
            nodes = mat.node_tree.nodes
            links = mat.node_tree.links
            principled = nodes.get('Principled BSDF')
            mixer = nodes.get("ShaderNodeVertexColor")
            for i in range(1):
                mix.location.x = -300
                if previous_mix:
                    links.new(previous_mix.outputs[0], mix.inputs[0])
            previous_mix = mix
            links.new(mix.outputs[0], principled.inputs[0])
            for i in range(1):
                rgbaV.location.x = -300
                rgbaV.location.y = -300
                if previous_rgba:
                    links.new(previous_rgba.outputs[0], rgbaV.inputs[0])
            previous_rgba = rgbaV
        links.new(rgbaV.outputs[1], principled.inputs[21])
        links.new(rgbaV.outputs[0], mix.inputs[1])

def GHG_whole_beta_2(f, filepath):
    pass
    """bm = bmesh.new()
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    meshes = {}
    fa=-1
    fb=0
    fc=1
    faces=[]
    vertices=[]
    os.system("cls")
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag = unpack("B", f.read(1))[0]
            for i in range(vertexCount//6):
                vx1 = unpack("<h", f.read(2))[0] / 4096.0
                vy1 = unpack("<h", f.read(2))[0] / 4096.0
                vz1 = unpack("<h", f.read(2))[0] / 4096.0
                vw1 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vx2 = unpack("<h", f.read(2))[0] / 4096.0
                vy2 = unpack("<h", f.read(2))[0] / 4096.0
                vz2 = unpack("<h", f.read(2))[0] / 4096.0
                vw2 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vx3 = unpack("<h", f.read(2))[0] / 4096.0
                vy3 = unpack("<h", f.read(2))[0] / 4096.0
                vz3 = unpack("<h", f.read(2))[0] / 4096.0
                vw3 = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)

                verts1 = bm.verts.new([vx1, vz1, vy1])
                verts2 = bm.verts.new([vx2, vz2, vy2])
                verts3 = bm.verts.new([vx3, vz3, vy3])

                bm.faces.new([verts1, verts2, verts3])

    bpy.context.view_layer.objects.active

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.to_mesh(mesh)
    
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    for face in mesh.polygons:
        face.use_smooth = True
    for mesh in meshes:
        bm.from_mesh(mesh)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)

        modifier = mesh.modifiers.new(name="GHG Edge Split", type='EDGE_SPLIT')
        modifier.split_angle = 0
        modifier.use_edge_angle = True
        

        bm.to_mesh(mesh)"""

def GHG_whole_beta_3(f, filepath):
    pass
    """bm = bmesh.new()
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
            for i in range(vertexCount//8):
                vx1 = unpack("<f", f.read(4))[0]
                vy1 = unpack("<f", f.read(4))[0]
                vz1 = unpack("<f", f.read(4))[0]
                vw1 = unpack("<f", f.read(4))[0]
                f.seek(-4,1)
                byte1__ = unpack("B", f.read(1))[0]
                byte2 = unpack("B", f.read(1))[0]
                byte3 = unpack("<Q", f.read(8))[0]
                f.seek(-6,1)
                f.seek(16,1)
                if byte1__ == 1:
                    pass
                vx2 = unpack("<f", f.read(4))[0]
                vy2 = unpack("<f", f.read(4))[0]
                vz2 = unpack("<f", f.read(4))[0]
                vw2 = unpack("<f", f.read(4))[0]
                f.seek(-4,1)
                byte1_ = unpack("B", f.read(1))[0]
                byte2_ = unpack("B", f.read(1))[0]
                byte3_ = unpack("<Q", f.read(8))[0]
                f.seek(-6,1)
                f.seek(16,1)
                if byte1_ == 1:
                    pass
                vx3 = unpack("<f", f.read(4))[0]
                vy3 = unpack("<f", f.read(4))[0]
                vz3 = unpack("<f", f.read(4))[0]
                vw3 = unpack("<f", f.read(4))[0]
                f.seek(-4,1)
                byte1 = unpack("B", f.read(1))[0]
                byte2 = unpack("B", f.read(1))[0]
                byte3 = unpack("<Q", f.read(8))[0]
                f.seek(-6,1)
                f.seek(16,1)
                if byte1 == 1:
                    pass
                elif byte1 == 0:
                    verts1 = bm.verts.new([vx1, vz1, vy1])
                    verts2 = bm.verts.new([vx2, vz2, vy2])
                    verts3 = bm.verts.new([vx3, vz3, vy3])

                    bm.faces.new([verts1, verts2, verts3])

    bpy.context.view_layer.objects.active

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.to_mesh(mesh)
    
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    for face in mesh.polygons:
        face.use_smooth = True
    for mesh in meshes:
        bm.from_mesh(mesh)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)

        modifier = mesh.modifiers.new(name="GHG Edge Split", type='EDGE_SPLIT')
        modifier.split_angle = 0
        modifier.use_edge_angle = True
        

        bm.to_mesh(mesh)"""


    
            
    

def NonParseGHG(filepath, GHG_Bones=1, GHG_Name=""):
    with open(filepath, "rb") as f:
        """if GHG_Name == "any_1":
            GHG_whole_beta_1(f, filepath)
        if GHG_Name == "any_2":
            GHG_whole_beta_2(f, filepath)
        if GHG_Name == "any_3":
            GHG_whole_beta_3(f, filepath)
        if GHG_Bones == 1:
            GHG_whole_entire_bones(f, filepath)"""
        pass
                
        
                
        
        
        
