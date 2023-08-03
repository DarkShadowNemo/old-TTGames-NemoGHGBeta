from struct import pack, unpack
from io import BytesIO as bio
import os
import bpy
import mathutils
import math
import bmesh

#luxo_list1 = [[201],[202],[203]] # incorrect face data

"del luxo_list1[:]"

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

def GHG_Textures(f, sizing=[]):
    f.seek(0)
    FileSize = unpack("<I", f.read(4))[0]
    unk = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    TextureStartEntrySize = unpack("<I", f.read(4))[0]
    f.seek(TextureStartEntrySize-16,1)
    for i in range(TextureCount):
        size = unpack("<I", f.read(4))[0]
        sizing.append([size])
    for i, siz in enumerate(sizing):
        #the real GHG textures are always in type 1
        f.seek(siz[0])
        W = unpack("<H", f.read(2))[0]
        type = unpack("<H", f.read(2))[0]
        H = unpack("<H", f.read(2))[0]
        unk = unpack("<H", f.read(2))[0]
        size2 = unpack("<H", f.read(2))[0]
        unk2 = unpack("<H", f.read(2))[0]
        f.seek(3,1) # not sure what that is
        flags4 = unpack("B", f.read(1))[0]
        if type == 1:
            size3 = unpack("<I", f.read(4))[0]
            unk3 = unpack("B", f.read(1))[0]
            depth = unpack("B", f.read(1))[0]
            unk4 = unpack("<H", f.read(2))[0]
            type = unpack("<H", f.read(2))[0]
            unk5 = unpack("<H", f.read(2))[0]
            unk6 = unpack("<H", f.read(2))[0]
            unk7 = unpack("<H", f.read(2))[0]
            bpy.data.images.new("GHG Image", width=W, height=H, alpha=True)

def GHG_whole_entire_bones_(f, bone_parentlist=[],bones_=[]):
        
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
    NamedtableEntrySize = unpack("<I", f.read(4))[0]
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
        bone_parent = unpack("b", f.read(1))[0]
        name_offset, = unpack("<L", f.read(4))
        f.seek(11,1)
        bone_parentlist.append(bone_parent)
        ntbl_buffer.seek(name_offset - 1)
        bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
        
    f.seek(0)
    f.seek(36,1)
    f.seek(PosBoneEntrySize-36,1)
    for i in range(BoneCount):
        f.seek(112,1)
        BX = unpack("<f", f.read(4))[0]
        BY = unpack("<f", f.read(4))[0]
        BZ = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        bones_.append([BX,BY,BZ])
        
    

    
            
        bone = skel.edit_bones.new("bone")
        bone.head = (
            +BX,
            +BZ,
            +BY,
        )
        bone.tail = (
            bone.head[0],
            bone.head[1],
            bone.head[2] + 0.03,
        )

        test = mathutils.Vector([BX, BY, BZ+1.0])

        mat_rot = mathutils.Matrix.Rotation(math.radians(90.0), 4, 'X')
        
        mat_trans = mathutils.Matrix.Translation(test)
            
            
        mat = mat_trans @ mat_rot
        mat.inverted()
            
        #mat3 = mat.to_3x3()
            
        bone.transform(mat)

    for bone_id, bone_parent in enumerate(bone_parentlist):
        if bone_parent < 0: continue # root bone is set to -1
        skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
    bpy.ops.object.mode_set(mode = 'OBJECT')

def GHG_whole_entire_bones(f, bone_parentlist=[],bones_=[]):
        
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
    NamedtableEntrySize = unpack("<I", f.read(4))[0]
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
        bone_parent = unpack("b", f.read(1))[0]
        name_offset, = unpack("<L", f.read(4)) # WHAT doesnt work
        f.seek(11,1)
        bone_parentlist.append(bone_parent)
        #ntbl_buffer.seek(name_offset - 1) or ntbl_buffer.seek(name_offset)
        #bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
            
    f.seek(0)
    f.seek(36,1)
    f.seek(PosBoneEntrySize-36,1)
    for i in range(BoneCount):
        f.seek(48,1)
        BX = unpack("<f", f.read(4))[0]
        BY = unpack("<f", f.read(4))[0]
        BZ = unpack("<f", f.read(4))[0]
        f.seek(4,1)
        bones_.append([BX,BY,BZ])

        BZ-=0.5
            
        

        
                
        bone = skel.edit_bones.new("bone")
        bone.head = (
            +BX,
            +BZ,
            +BY,
        )
        bone.tail = (
            bone.head[0],
            bone.head[1],
            bone.head[2] + 0.03,
        )

        test = mathutils.Vector([BX, BY, BZ+1.0])

        mat_rot = mathutils.Matrix.Rotation(math.radians(90.0), 4, 'X')
            
        mat_trans = mathutils.Matrix.Translation(test)
                
                
        mat = mat_trans @ mat_rot
        mat.inverted()
                
        #mat3 = mat.to_3x3()
                
        bone.transform(mat)

    for bone_id, bone_parent in enumerate(bone_parentlist):
        if bone_parent < 0: continue # root bone is set to -1
        skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
    bpy.ops.object.mode_set(mode = 'OBJECT')

def GHG_whole_beta(f, filepath):
    vertices=[]
    faces=[]
    normals=[]
    material_ID = os.path.basename(os.path.splitext(filepath)[0])
    mat = bpy.data.materials.new(name=material_ID)
    bpy.data.materials.get(os.path.basename(os.path.splitext(filepath)[0]))
    ob = bpy.context.object
    #######################
    #another extra 
    fa=-3
    fb=-2
    fc=-1
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
                normals.append([0,0,nz]) # crack down normal z axis to faces
            for i, norm in enumerate(normals):
                if norm[2] == 1.0:
                    for i in range(vertexCount-2):
                        fa+=1*3
                        fb+=1*3
                        fc+=1*3
                        faces.append([fa,fb,fc])
            for i, mat in enumerate(bpy.data.materials):
                mat.use_nodes = True
                mat.blend_method = "HASHED"
        elif Chunk == b"\x03\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                nz = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(8,1)
                vertices.append([vx,vy,vz])
                normals.append([0,0,nz]) # crack down normal z axis to faces
            for i, norm in enumerate(normals):
                if norm[2] == 1.0:
                    for i in range(vertexCount-2):
                        fa+=1*3
                        fb+=1*3
                        fc+=1*3
                        faces.append([fa,fb,fc])
            for i, mat in enumerate(bpy.data.materials):
                mat.use_nodes = True
                mat.blend_method = "HASHED"
        elif Chunk == b"\x04\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                vertices.append([vx,vy,vz])
                normals.append([0,0,nz]) # crack down normal z axis to faces
            for i, norm in enumerate(normals):
                if norm[2] == 1.0:
                    for i in range(vertexCount-2):
                        fa+=1*3
                        fb+=1*3
                        fc+=1*3
                        faces.append([fa,fb,fc])
            for i, mat in enumerate(bpy.data.materials):
                mat.use_nodes = True
                mat.blend_method = "HASHED"

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    



def NonParseGHG(filepath, GHG_Meshes=1, GHG_Bones=1):
    with open(filepath, "rb") as f:
        GHG_whole_beta(f, filepath)
        if GHG_Bones == 1:
            GHG_whole_entire_bones(f, bone_parentlist=[],bones_=[])
        if GHG_Bones == 2:
            GHG_whole_entire_bones_(f, bone_parentlist=[],bones_=[])
                
        
                
        
        
        
