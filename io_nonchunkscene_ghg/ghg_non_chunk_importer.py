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
    pass
def GHG_whole_entire_uv3(f):
    pass

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
        ntbl_buffer.seek(name_offset)
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

def GHG_whole_beta_1(f, filepath):
    vertices=[]
    faces=[]
    normals=[]
    material_ID = os.path.basename(os.path.splitext(filepath)[0])
    mat = bpy.data.materials.new(name=material_ID)
    bpy.data.materials.get(os.path.basename(os.path.splitext(filepath)[0]))
    ob = bpy.context.object
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    fa = -1
    fb = 0
    fc = 1
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
                normals.append([0,0,nz])
            for i, mat in enumerate(bpy.data.materials):
                mat.use_nodes = True
                mat.blend_method = "HASHED"
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    

def GHG_whole_beta_2(f, filepath):
    vertices=[]
    normals=[]
    faces = []
    material_ID = os.path.basename(os.path.splitext(filepath)[0])
    mat = bpy.data.materials.new(name=material_ID)
    bpy.data.materials.get(os.path.basename(os.path.splitext(filepath)[0]))
    ob = bpy.context.object
    #######################
    #another extra
    fa = -1
    fb = 0
    fc = 1
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x03\x02\x00\x01":
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
                normals.append([0,0,1])
            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
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

def GHG_whole_beta_3(f, filepath):
    vertices=[]
    vertices2=[]
    vertices2_pt2=[]
    vertices3=[]
    vertices3_pt2=[]
    faces=[]
    faces2=[]
    faces2_pt2=[]
    faces3=[]
    faces3_pt2=[]
    normals=[]
    normals2=[]
    normals2_pt2=[]
    normals3=[]
    normals3_pt2=[]
    material_ID = os.path.basename(os.path.splitext(filepath)[0])
    mat = bpy.data.materials.new(name=material_ID)
    bpy.data.materials.get(os.path.basename(os.path.splitext(filepath)[0]))
    ob = bpy.context.object
    #######################
    #another extra
    f.seek(0)
    ChunkRead = f.read()
    f.seek(0)
    fa = -3
    fb = -2
    fc = -1

    fa_ = -3
    fb_ = -2
    fc_ = -1

    fa_pt2 = -3
    fb_pt2 = -2
    fc_pt2 = -1

    fa__ = -3
    fb__ = -2
    fc__ = -1

    fa__pt2 = -3
    fb__pt2 = -2
    fc__pt2 = -1
    for i in range(len(ChunkRead)):
        Chunk = f.read(4)
        if Chunk == b"\x04\x02\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            f.seek(1,1)
            if vertexCount == 3:
                for i in range(vertexCount):
                    
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices.append([vx,vy,vz])
                    normals.append([0,0,1])
                for i in range(vertexCount-2):
                    fa+=1*3
                    fb+=1*3
                    fc+=1*3
                    faces.append([fa,fb,fc])
            elif vertexCount == 4:
                for i in range(vertexCount-1):
                    
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices2.append([vx,vy,vz])
                    normals2.append([0,0,1])
                for i in range(vertexCount-1):
                    f.seek(-16,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(16,1)
                for i in range(vertexCount-1):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices2_pt2.append([vx,vy,vz])
                    normals2_pt2.append([0,0,1])
                for i in range(vertexCount-3):
                    fa_+=1*3
                    fb_+=1*3
                    fc_+=1*3
                    faces2.append([fa_,fb_,fc_])
                for i in range(vertexCount-3):
                    fa_pt2+=1*3
                    fb_pt2+=1*3
                    fc_pt2+=1*3
                    faces2_pt2.append([fa_pt2,fb_pt2,fc_pt2])
            elif vertexCount == 5:
                for i in range(vertexCount-2):
                    
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vertices3.append([vx,vy,vz])
                    normals3.append([0,0,1])
                for i in range(vertexCount-4):
                    fa__+=1*3
                    fb__+=1*3
                    fc__+=1*3
                    faces3.append([fa__,fb__,fc__])
                for i in range(vertexCount-1):
                    f.seek(-16,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                    f.seek(-4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(4,1)
                f.seek(16,1)
                
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

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices2, [], faces2)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices2_pt2, [], faces2_pt2)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices3, [], faces3)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices3_pt2, [], faces3_pt2)
    object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials[os.path.basename(os.path.splitext(filepath)[0])].use_backface_culling = True
    objs = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = objs
    objs.data.materials.append(mat)

    



def NonParseGHG(filepath, GHG_Meshes=1, GHG_Bones=1):
    with open(filepath, "rb") as f:
        if GHG_Meshes == 1:
            GHG_whole_beta_1(f, filepath)
        if GHG_Meshes == 2:
            GHG_whole_beta_2(f, filepath)
        if GHG_Meshes == 3:
            GHG_whole_beta_3(f, filepath)
        if GHG_Bones == 1:
            GHG_whole_entire_bones(f, bone_parentlist=[],bones_=[])
        if GHG_Bones == 2:
            GHG_whole_entire_bones_(f, bone_parentlist=[],bones_=[])
                
        
                
        
        
        
