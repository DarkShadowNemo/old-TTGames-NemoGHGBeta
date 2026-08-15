from struct import unpack, pack
import os
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

def GHG_mesh(f, filepath):

    bone_parentlist=[]
    bone_names=[]

    vertices=[]
    faces=[]
    uvs1=[]

    fa=-1
    fb=0
    fc=1

    vertices3a=[]
    faces3a=[]

    
    vertices3=[]
    faces3=[]

    faces3a=[]

    faa=-1
    fba=0
    fca=1

    idx_ = 0

    coll = bpy.context.collection
    skel = bpy.data.armatures.new('GHG Skeleton')
    arma = bpy.data.objects.new('GHG Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')

    f.seek(0)
    FileSize_ = unpack("<I", f.read(4))[0]
    null1_ = unpack("<I", f.read(4))[0]
    TextureCount = unpack("<I", f.read(4))[0]
    TextureEntrySize1 = unpack("<I", f.read(4))[0]
    MaterialCount = unpack("<I", f.read(4))[0]
    f.seek(-4,1)
    MaterialCount2 = unpack("<I", f.read(4))[0]
    MaterialEntrySize1 = unpack("<I", f.read(4))[0]
    BoneCount = unpack("<I", f.read(4))[0]
    RotSclBoneEntrySize1 = unpack("<I", f.read(4))[0]
    SclBoneEntrySize1 = unpack("<I", f.read(4))[0]
    PosBoneEntrySize1 = unpack("<I", f.read(4))[0]
    ObjectCount = unpack("<I", f.read(4))[0]
    ObjectCountEntrySize1 = unpack("<I", f.read(4))[0]
    NamedtableEntrySize1 = unpack("<I", f.read(4))[0]
    NamedtableLength1,=unpack("<I", f.read(4))
    UnkCount1 = unpack("<I", f.read(4))[0]
    UnkCountEntrySize1 = unpack("<I", f.read(4))[0]
    UnkCount2 = unpack("<I", f.read(4))[0]
    UnkCountEntrySize2 = unpack("<I", f.read(4))[0]
    defaultlayercount = unpack("<I", f.read(4))[0]
    defaultlayerEntrySize1 = unpack("<I", f.read(4))[0]
    bsaEntrySize1 = unpack("<I", f.read(4))[0]
    for i in range(11):
        float01 = unpack("<f", f.read(4))[0]
        float01-=float01
    size01 = unpack("<I", f.read(4))[0]
    float02 = unpack("<f", f.read(4))[0]
    type01 = unpack("<I", f.read(4))[0]
    typeSize1 = unpack("<I", f.read(4))[0]
    if TextureCount == 0:
        pass
    elif TextureCount != 0:
        if TextureEntrySize1 == 144 or TextureEntrySize1 == 148 or TextureEntrySize1 == 152:
            f.seek(0)
            f.seek(NamedtableEntrySize1,0)
            ntbl_buffer = bio(f.read(NamedtableEntrySize1))
            name_i = 0
            while 1:
                name = fetch_cstr(ntbl_buffer).decode('ascii')
                if not name: break
                name_i+=1
            f.seek(0)
            f.seek(RotSclBoneEntrySize1,0)
            for i in range(BoneCount):
                mrscl1 = unpack("<f", f.read(4))[0]
                mrscl2 = unpack("<f", f.read(4))[0]
                mrscl3 = unpack("<f", f.read(4))[0]
                mrscl4 = unpack("<f", f.read(4))[0]
                mrscl5 = unpack("<f", f.read(4))[0]
                mrscl6 = unpack("<f", f.read(4))[0]
                mrscl7 = unpack("<f", f.read(4))[0]
                mrscl8 = unpack("<f", f.read(4))[0]
                mrscl9 = unpack("<f", f.read(4))[0]
                mrsc20 = unpack("<f", f.read(4))[0]
                mrsc21 = unpack("<f", f.read(4))[0]
                mrsc22 = unpack("<f", f.read(4))[0]
                f.seek(16,1)
                bdiv4_v00 = unpack("<f", f.read(4))[0]
                bdiv4_v04 = unpack("<f", f.read(4))[0]
                bdiv4_v08 = unpack("<f", f.read(4))[0]
                f.seek(4,1)
                bone_parent,=unpack("b", f.read(1))
                bone_parentlist.append(bone_parent)

                name_offset,=unpack("<L", f.read(4)) # WHAT doesnt work
                f.seek(11,1)
                try:
                    ntbl_buffer.seek(name_offset-1)
                except:
                    ValueError
            f.seek(0)
            f.seek(PosBoneEntrySize1,0)
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
                posx = -unpack("<f", f.read(4))[0]
                posy = -unpack("<f", f.read(4))[0]
                posz = -unpack("<f", f.read(4))[0]
                ScaleW = unpack("<f", f.read(4))[0]
                m1 = ([ScaleX,rotationz,rotationy,null1])
                m2 = ([nrotationz,ScaleY,rotationx,nrotationy])
                m3 = ([null2,nrotationx,ScaleZ,null3])
                m4 = ([posx,posy,posz,ScaleW])

                matrix = mathutils.Matrix([m1,m3,m2,m4]).inverted().to_3x3().transposed()
                bone_name = fetch_cstr(ntbl_buffer).decode('ascii')
                bone_names.append([bone_name])
                

                bone = skel.edit_bones.new(bone_name)
                
                bone.tail = mathutils.Vector([0,0,0.03])
                
                bone.head = ([
                    posx,
                    posy,
                    posz,
                ])
                
                bone.length = -0.03
                
                bone.transform(matrix)
            for bone_id, bone_parent in enumerate(bone_parentlist):
                if bone_parent < 0: continue # root bone is set to -1
                skel.edit_bones[bone_id].parent = skel.edit_bones[bone_parent]
            bpy.ops.object.mode_set(mode = 'OBJECT')
            f.seek(0)
            Chunks = f.read()
            f.seek(0)

            while f.tell() < len(Chunks):
                Chunk = f.read(4)
                if Chunk == b"\x03\x01\x00\x01":
                    f.seek(2,1)
                    vertexCount2 = unpack("B", f.read(1))[0]
                    flag_2 = unpack("B", f.read(1))[0]
                    if flag_2 == 0x6C:
                        if vertexCount2 == 0:
                            pass
                        elif vertexCount2 == 1:
                            pass
                        elif vertexCount2 == 2:
                            pass
                        elif vertexCount2:
                            for j in range(vertexCount2):
                                vx = unpack("<f", f.read(4))[0]
                                vy = unpack("<f", f.read(4))[0]
                                vz = unpack("<f", f.read(4))[0]
                                type4 = unpack("B", f.read(1))[0]==False
                                value1a = unpack("B", f.read(1))[0]
                                normalZ_ = unpack("<h", f.read(2))[0]
                                static_vx = round(vx,3)
                                static_vy = round(vy,3)
                                static_vz = round(vz,3)
                                
                                vertices.append([static_vx,static_vz,static_vy])
                                fa+=1
                                fb+=1
                                fc+=1
                                if type4 > 0:
                                    faces.append([abs(j+j+type4-type4-1+fa-j-j-1+j%2),abs(j-j+type4-type4+1+fb-2-1+j-j-j%2),abs(j+type4-type4+fc-j+2-4)])

                elif Chunk == b"\x04\x02\x00\x01":
                    f.seek(2,1)
                    vertexCount2a = unpack("B", f.read(1))[0]//2
                    flag_2a = unpack("B", f.read(1))[0]
                    if flag_2a == 0x6C:
                        if vertexCount2a == 0:
                            pass
                        elif vertexCount2a == 1:
                            pass
                        elif vertexCount2a == 2:
                            pass
                        elif vertexCount2a:
                            for j in range(vertexCount2a):
                                vxa = unpack("<f", f.read(4))[0]
                                vya = unpack("<f", f.read(4))[0]
                                vza = unpack("<f", f.read(4))[0]
                                brightness = unpack("<f", f.read(4))[0]
                                uvx3a = unpack("<f", f.read(4))[0]
                                uvy3a = unpack("<f", f.read(4))[0]
                                unk3a = unpack("<f", f.read(4))[0]
                                type4a = unpack("B", f.read(1))[0]^1
                                value1aa = unpack("B", f.read(1))[0]
                                normalZa_ = unpack("<h", f.read(2))[0]
                                static_vxa = round(vxa,3)
                                static_vya = round(vya,3)
                                static_vza = round(vza,3)
                                
                                vertices3.append([static_vxa,static_vza,static_vya])
                                faa+=1
                                fba+=1
                                fca+=1
                                if type4a < 1:
                                    faces3.append([abs(j+type4a-type4a+faa-j) % abs(3)])
                                                                                                                                
                                                                                                                    
                                                            
                                                
                                            
                                            
                                            
                                        
                                    
                                                    

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    objects = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objects)

    mesh3 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh3.from_pydata(vertices3, [], faces3)
    objects3 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh3)
    collection.objects.link(objects3)

    objects3.parent = arma
    armamodifier3 = objects3.modifiers.new("GHG Armature Modifier", "ARMATURE")
    armamodifier3.object = arma

    vgroups3 = [objects3.vertex_groups.new(name = bone.name) for bone in arma.data.bones]
