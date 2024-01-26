from struct import unpack, pack
import os
import bmesh
import math
import bpy
import mathutils
from io import BytesIO as bio

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

def GHG_whole_entire_bones(f, filepath):

    boneIndex = -1

    bones_=[]

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
        f.seek(11,1)
        ntbl_buffer.seek(name_offset-1,1)
            
    f.seek(0)
    f.seek(36,1)
    f.seek(RotBoneEntrySize-36,1)
    for i in range(BoneCount):
        ScaleX = unpack("<f", f.read(4))[0]
        rotationz = unpack("<f", f.read(4))[0]
        rotationy = unpack("<f", f.read(4))[0]
        null1 = unpack("<f", f.read(4))[0]
        nrotationz = unpack("<f", f.read(4))[0]
        ScaleY = unpack("<f", f.read(4))[0]
        rotationx = unpack("<f", f.read(4))[0]
        nrotationy = unpack("<f", f.read(4))[0]
        null2 = unpack("<f", f.read(4))[0]
        nrotationx = unpack("<f", f.read(4))[0]
        ScaleZ = unpack("<f", f.read(4))[0]
        null3 = unpack("<f", f.read(4))[0]
        posx = unpack("<f", f.read(4))[0]
        posy = unpack("<f", f.read(4))[0]
        posz = unpack("<f", f.read(4))[0]
        ScaleW = unpack("<f", f.read(4))[0]

        matrix = mathutils.Matrix([[ScaleX,rotationz,rotationy,null1],[nrotationz,ScaleY,rotationx,nrotationy],[null2,nrotationx,ScaleZ,null3],[posx,posy,posz,ScaleW]]).inverted().to_3x3().transposed()

        bone_name = fetch_cstr(ntbl_buffer).decode('ascii')

        bone = skel.edit_bones.new(bone_name)
        
        bone.tail = mathutils.Vector([0,0,-0.03])
        
        bone.head = ([
            posx,
            posy,
            posz,
        ])
        
        bone.length = 0.03
        
        bone.transform(matrix)
    for bone_id, bone_parent in enumerate(bone_parentlist):
        if bone_parent < 0: continue # root bone is set to -1
        skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
    bpy.ops.object.mode_set(mode = 'OBJECT')


def GHG_mesh_1(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm = bmesh.new()
    bm2 = bmesh.new()
    bm3 = bmesh.new()
    bm4 = bmesh.new()
    bm5 = bmesh.new()
    bm6 = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x03\x01\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            if vertexCount == 3:
                
                for i in range(vertexCount//3):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa = bm.verts.new([vx1,vz1,vy1])
                    fb = bm.verts.new([vx2,vz2,vy2])
                    fc = bm.verts.new([vx3,vz3,vy3])
                    bm.faces.new([fa,fb,fc])
            elif vertexCount == 4:
                for i in range(vertexCount//4):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    faceon4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa1 = bm2.verts.new([vx1,vz1,vy1])
                    fb1 = bm2.verts.new([vx2,vz2,vy2])
                    fc1 = bm2.verts.new([vx3,vz3,vy3])
                    fd1 = bm2.verts.new([vx4,vz4,vy4])
                    bm2.faces.new([fa1,fb1,fc1])
                    bm2.faces.new([fc1,fb1,fd1])
            elif vertexCount == 5:
                for i in range(vertexCount//5):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    faceon4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    faceon5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa1 = bm3.verts.new([vx1,vz1,vy1])
                    fb1 = bm3.verts.new([vx2,vz2,vy2])
                    fc1 = bm3.verts.new([vx3,vz3,vy3])
                    fd1 = bm3.verts.new([vx4,vz4,vy4])
                    fe1 = bm3.verts.new([vx5,vz5,vy5])
                    bm3.faces.new([fa1,fb1,fc1])
                    bm3.faces.new([fc1,fb1,fd1])
            elif vertexCount == 6:
                for i in range(vertexCount//6):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    faceon4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    faceon5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    faceon6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa1 = bm4.verts.new([vx1,vz1,vy1])
                    fb1 = bm4.verts.new([vx2,vz2,vy2])
                    fc1 = bm4.verts.new([vx3,vz3,vy3])
                    fd1 = bm4.verts.new([vx4,vz4,vy4])
                    fe1 = bm4.verts.new([vx5,vz5,vy5])
                    ff1 = bm4.verts.new([vx6,vz6,vy6])
                    bm4.faces.new([fa1,fb1,fc1])
                    bm4.faces.new([fc1,fb1,fd1])
            elif vertexCount == 7:
                for i in range(vertexCount//7):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    faceon4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    faceon5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    faceon6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    faceon7 = unpack("B", f.read(1))[0]
                    value7 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa1 = bm5.verts.new([vx1,vz1,vy1])
                    fb1 = bm5.verts.new([vx2,vz2,vy2])
                    fc1 = bm5.verts.new([vx3,vz3,vy3])
                    fd1 = bm5.verts.new([vx4,vz4,vy4])
                    fe1 = bm5.verts.new([vx5,vz5,vy5])
                    ff1 = bm5.verts.new([vx6,vz6,vy6])
                    fg1 = bm5.verts.new([vx7,vz7,vy7])
                    bm5.faces.new([fa1,fb1,fc1])
                    bm5.faces.new([fc1,fb1,fd1])
            elif vertexCount == 8:
                for i in range(vertexCount//8):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    faceon1 = unpack("B", f.read(1))[0]
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    faceon2 = unpack("B", f.read(1))[0]
                    value2 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    faceon3 = unpack("B", f.read(1))[0]
                    value3 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    faceon4 = unpack("B", f.read(1))[0]
                    value4 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    faceon5 = unpack("B", f.read(1))[0]
                    value5 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    faceon6 = unpack("B", f.read(1))[0]
                    value6 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    faceon7 = unpack("B", f.read(1))[0]
                    value7 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vx8 = unpack("<f", f.read(4))[0]
                    vy8 = unpack("<f", f.read(4))[0]
                    vz8 = unpack("<f", f.read(4))[0]
                    faceon8 = unpack("B", f.read(1))[0]
                    value8 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    fa1 = bm6.verts.new([vx1,vz1,vy1])
                    fb1 = bm6.verts.new([vx2,vz2,vy2])
                    fc1 = bm6.verts.new([vx3,vz3,vy3])
                    fd1 = bm6.verts.new([vx4,vz4,vy4])
                    fe1 = bm6.verts.new([vx5,vz5,vy5])
                    ff1 = bm6.verts.new([vx6,vz6,vy6])
                    fg1 = bm6.verts.new([vx7,vz7,vy7])
                    fh1 = bm6.verts.new([vx8,vz8,vy8])
                    bm6.faces.new([fa1,fb1,fc1])
                    bm6.faces.new([fc1,fb1,fd1])
                                    
                                
                        
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    for fac in bm.faces:
        fac.normal_flip()
    bm.to_mesh(mesh)

    for fac in mesh.polygons:
        fac.use_smooth = True

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm2.from_mesh(mesh2)
    objects2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(objects2)
    bmesh.ops.remove_doubles(bm2, verts = bm2.verts, dist = 0.0001)
    for fac in bm2.faces:
        fac.normal_flip()
    bm2.to_mesh(mesh2)

    for fac in mesh2.polygons:
        fac.use_smooth = True

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm3.from_mesh(mesh3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)
    bmesh.ops.remove_doubles(bm3, verts = bm3.verts, dist = 0.0001)
    for fac in bm3.faces:
        fac.normal_flip()
    bm3.to_mesh(mesh3)

    for fac in mesh3.polygons:
        fac.use_smooth = True

    mesh4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm4.from_mesh(mesh4)
    objects4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4)
    collection.objects.link(objects4)
    bmesh.ops.remove_doubles(bm4, verts = bm4.verts, dist = 0.0001)
    for fac in bm4.faces:
        fac.normal_flip()
    bm4.to_mesh(mesh4)

    for fac in mesh4.polygons:
        fac.use_smooth = True

    mesh5 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm5.from_mesh(mesh5)
    objects5 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh5)
    collection.objects.link(objects5)
    bmesh.ops.remove_doubles(bm5, verts = bm5.verts, dist = 0.0001)
    for fac in bm5.faces:
        fac.normal_flip()
    bm5.to_mesh(mesh5)

    for fac in mesh5.polygons:
        fac.use_smooth = True

    mesh6 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm6.from_mesh(mesh6)
    objects6 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh6)
    collection.objects.link(objects6)
    bmesh.ops.remove_doubles(bm6, verts = bm6.verts, dist = 0.0001)
    for fac in bm6.faces:
        fac.normal_flip()
    bm6.to_mesh(mesh6)

    for fac in mesh6.polygons:
        fac.use_smooth = True
                

def GHG_mesh_2(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x03\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0]//2
            flag2 = unpack("B", f.read(1))[0]
            for i in range(vertexCount):
                vx1 = unpack("<h", f.read(2))[0] / 4096
                vy1 = unpack("<h", f.read(2))[0] / 4096
                vz1 = unpack("<h", f.read(2))[0] / 4096
                vw1 = unpack("<h", f.read(2))[0] / 4096
                f.seek(8,1)
                bm.verts.new([vx1,vz1,vy1])
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    for fac in mesh.polygons:
        fac.use_smooth = True

def GHG_mesh_3(f, filepath):
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    bm = bmesh.new()
    bm2 = bmesh.new()
    bm3 = bmesh.new()
    bm4 = bmesh.new()
    bm5 = bmesh.new()
    bm6 = bmesh.new()
    for i in range(len(Chunk)):
        Chunks = f.read(4)
        if Chunks == b"\x04\x02\x00\x01":
            flag1 = unpack("B", f.read(1))[0]
            f.seek(1,1)
            vertexCount = unpack("B", f.read(1))[0] // 2
            flag2 = unpack("B", f.read(1))[0]
            if vertexCount == 3:
                
                for i in range(vertexCount//3):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm.verts.new([vx1,vz1,vy1])
                    fb = bm.verts.new([vx2,vz2,vy2])
                    fc = bm.verts.new([vx3,vz3,vy3])
                    bm.edges.new([fa,fb])
            elif vertexCount == 4:
                
                for i in range(vertexCount//4):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    vw4 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm2.verts.new([vx1,vz1,vy1])
                    fb = bm2.verts.new([vx2,vz2,vy2])
                    fc = bm2.verts.new([vx3,vz3,vy3])
                    fd = bm2.verts.new([vx4,vz4,vy4])
                    bm2.edges.new([fa,fb])
            elif vertexCount == 5:
                
                for i in range(vertexCount//5):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    vw4 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    vw5 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm3.verts.new([vx1,vz1,vy1])
                    fb = bm3.verts.new([vx2,vz2,vy2])
                    fc = bm3.verts.new([vx3,vz3,vy3])
                    fd = bm3.verts.new([vx4,vz4,vy4])
                    fe = bm3.verts.new([vx5,vz5,vy5])
                    bm3.edges.new([fa,fb])

            elif vertexCount == 6:
                
                for i in range(vertexCount//6):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    vw4 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    vw5 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    vw6 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm4.verts.new([vx1,vz1,vy1])
                    fb = bm4.verts.new([vx2,vz2,vy2])
                    fc = bm4.verts.new([vx3,vz3,vy3])
                    fd = bm4.verts.new([vx4,vz4,vy4])
                    fe = bm4.verts.new([vx5,vz5,vy5])
                    ff = bm4.verts.new([vx6,vz6,vy6])
                    bm4.edges.new([fa,fb])
            elif vertexCount == 7:
                
                for i in range(vertexCount//7):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    vw4 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    vw5 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    vw6 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    vw7 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm5.verts.new([vx1,vz1,vy1])
                    fb = bm5.verts.new([vx2,vz2,vy2])
                    fc = bm5.verts.new([vx3,vz3,vy3])
                    fd = bm5.verts.new([vx4,vz4,vy4])
                    fe = bm5.verts.new([vx5,vz5,vy5])
                    ff = bm5.verts.new([vx6,vz6,vy6])
                    fg = bm5.verts.new([vx7,vz7,vy7])
                    bm5.edges.new([fa,fb])
            elif vertexCount == 8:
                
                for i in range(vertexCount//8):
                    vx1 = unpack("<f", f.read(4))[0]
                    vy1 = unpack("<f", f.read(4))[0]
                    vz1 = unpack("<f", f.read(4))[0]
                    vw1 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx2 = unpack("<f", f.read(4))[0]
                    vy2 = unpack("<f", f.read(4))[0]
                    vz2 = unpack("<f", f.read(4))[0]
                    vw2 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx3 = unpack("<f", f.read(4))[0]
                    vy3 = unpack("<f", f.read(4))[0]
                    vz3 = unpack("<f", f.read(4))[0]
                    vw3 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx4 = unpack("<f", f.read(4))[0]
                    vy4 = unpack("<f", f.read(4))[0]
                    vz4 = unpack("<f", f.read(4))[0]
                    vw4 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx5 = unpack("<f", f.read(4))[0]
                    vy5 = unpack("<f", f.read(4))[0]
                    vz5 = unpack("<f", f.read(4))[0]
                    vw5 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx6 = unpack("<f", f.read(4))[0]
                    vy6 = unpack("<f", f.read(4))[0]
                    vz6 = unpack("<f", f.read(4))[0]
                    vw6 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx7 = unpack("<f", f.read(4))[0]
                    vy7 = unpack("<f", f.read(4))[0]
                    vz7 = unpack("<f", f.read(4))[0]
                    vw7 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    vx8 = unpack("<f", f.read(4))[0]
                    vy8 = unpack("<f", f.read(4))[0]
                    vz8 = unpack("<f", f.read(4))[0]
                    vw8 = unpack("<f", f.read(4))[0]
                    f.seek(16,1)
                    fa = bm6.verts.new([vx1,vz1,vy1])
                    fb = bm6.verts.new([vx2,vz2,vy2])
                    fc = bm6.verts.new([vx3,vz3,vy3])
                    fd = bm6.verts.new([vx4,vz4,vy4])
                    fe = bm6.verts.new([vx5,vz5,vy5])
                    ff = bm6.verts.new([vx6,vz6,vy6])
                    fg = bm6.verts.new([vx7,vz7,vy7])
                    fh = bm6.verts.new([vx8,vz8,vy8])
                    bm6.edges.new([fa,fb])
                        
    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm.from_mesh(mesh)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)
    bmesh.ops.remove_doubles(bm, verts = bm.verts, dist = 0.0001)
    bm.to_mesh(mesh)

    for fac in mesh.polygons:
        fac.use_smooth = True

    mesh2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm2.from_mesh(mesh2)
    objects2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh2)
    collection.objects.link(objects2)
    bmesh.ops.remove_doubles(bm2, verts = bm2.verts, dist = 0.0001)
    bm2.to_mesh(mesh2)

    for fac in mesh2.polygons:
        fac.use_smooth = True

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm3.from_mesh(mesh3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)
    bmesh.ops.remove_doubles(bm3, verts = bm3.verts, dist = 0.0001)
    bm3.to_mesh(mesh3)

    for fac in mesh3.polygons:
        fac.use_smooth = True

    mesh4 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm4.from_mesh(mesh4)
    objects4 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh4)
    collection.objects.link(objects4)
    bmesh.ops.remove_doubles(bm4, verts = bm4.verts, dist = 0.0001)
    bm4.to_mesh(mesh4)

    for fac in mesh4.polygons:
        fac.use_smooth = True

    mesh5 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm5.from_mesh(mesh5)
    objects5 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh5)
    collection.objects.link(objects5)
    bmesh.ops.remove_doubles(bm5, verts = bm5.verts, dist = 0.0001)
    bm5.to_mesh(mesh5)

    for fac in mesh5.polygons:
        fac.use_smooth = True

    mesh6 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    bm6.from_mesh(mesh6)
    objects6 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh6)
    collection.objects.link(objects6)
    bmesh.ops.remove_doubles(bm6, verts = bm6.verts, dist = 0.0001)
    bm6.to_mesh(mesh6)

    for fac in mesh6.polygons:
        fac.use_smooth = True

def ghg_open(filepath, offset_on_off=False, offsets="", skeleton_on_or_off=False):
    with open(filepath, "rb") as f:
        if skeleton_on_or_off:
            GHG_whole_entire_bones(f, filepath)
        if offset_on_off:
            if offsets == "0x030100010380XX6C":
                GHG_mesh_1(f, filepath)
            if offsets == "0x030200010380XX6D":
                GHG_mesh_2(f, filepath)
            if offsets == "0x040200010380XX6C":
                GHG_mesh_3(f, filepath)
            
            
                
            
    
