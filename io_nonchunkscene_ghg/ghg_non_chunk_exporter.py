import bpy
from struct import pack
import bmesh

def WriteModdedGHG(f):
    ob = bpy.context.object
    f.write(pack("<I", 0)) # size
    f.write(pack("<I", 0)) # unk
    f.write(pack("<I", 0)) # textures
    f.write(pack("<I", 0)) # 144
    f.write(pack("<I", len(bpy.data.materials)))
    f.write(pack("<I", 0)) # 144
    f.write(pack("<I", len(ob.pose.bones)))
    f.write(pack("<I", 0)) # parent start size
    f.write(pack("<I", 0)) # pos start size
    f.write(pack("<I", 0)) # unk start size
    f.write(pack("<I", 0)) #
    f.write(pack("<I", 0)) #
    f.write(pack("<I", 0)) # namedtable size
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 1)) # maybe object amount
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    for i in range(16):
        f.write(pack("<f", 1))

    f.write(pack("<I", 160))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    for i, mat in enumerate(bpy.data.materials):
        f.write(pack("B", 0x0D))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x10))
        f.write(pack("B", 0x08))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x50))
        f.write(pack("B", 0x07))
        f.write(pack("B", 0x80))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x10))
        f.write(pack("B", 0x0E))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x18))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x1B))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x44))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x42))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x4E))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xDA))
        f.write(pack("B", 0x37))
        f.write(pack("B", 0x05))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x47))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x3F))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xA6))
        f.write(pack("B", 255))
        f.write(pack("B", 255))
        f.write(pack("B", 255))
        f.write(pack("B", 0x14))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 8))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x13))
        f.write(pack("B", 0))
        f.write(pack("B", 3))
        f.write(pack("B", 0x6C))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 128))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
            
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x30))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0x19))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 16384))
        f.write(pack("B", 0x50))
        f.write(pack("B", 0x84))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0x10))
        f.write(pack("B", 0x2C))
        f.write(pack("B", 0x49))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        #this comes up automatically up in game
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0x3D))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0xF8))
        f.write(pack("B", 0x84))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0xF0))
        f.write(pack("B", 0x87))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0x50))
        f.write(pack("B", 0))
        f.write(pack("B", 0x88))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("<f", mat.specular_intensity))
        f.write(pack("B", 19))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<f", mat.diffuse_color[0]))
        f.write(pack("<f", mat.diffuse_color[1]))
        f.write(pack("<f", mat.diffuse_color[2]))
        f.write(pack("<f", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xA0))
        f.write(pack("B", 0x41))
        f.write(pack("<f", mat.roughness))
        f.write(pack("B", 0x91))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0xA6))
        f.write(pack("B", 255))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
    for pbone_ in ob.pose.bones:
        f.write(b"dragonjan_bones")
        f.write(pack("B", 0))
    f.write(b"defaultlayer")
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    nametable_offset = 1
    for pbone in ob.pose.bones: # transpose
        f.write(pack("<f", pbone.length))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))

        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))

        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<I", 0))

        f.write(pack("b", ob.data.bones.find(pbone.parent.name) if pbone.parent is not None else -1))
        f.write(pack("<I", nametable_offset))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        nametable_offset+=1
    for pbone in ob.pose.bones:
        f.write(pack("<f", pbone.length))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", pbone.head.x))
        f.write(pack("<f", pbone.head.y))
        f.write(pack("<f", pbone.head.z))
        f.write(pack("<f", 1))
    for pbone in ob.pose.bones:
        f.write(pack("<f", pbone.length))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        f.write(pack("<f", 1))
        f.write(pack("<f", 0))
        f.write(pack("<f", -pbone.head.x))
        f.write(pack("<f", -pbone.head.y))
        f.write(pack("<f", -pbone.head.z))
        f.write(pack("<f", 1))
        
    f.write(b"defaultlayer")
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    f.write(pack("B", 0))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))

"""import bpy
import bmesh

obj=bpy.context.object
if obj.mode == 'EDIT':
    bm=bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if v.select:
            print(v.co)
else:
    print("Object is not in edit mode.")"""

def WritingEditGHG(filepath):
    with open(filepath, "wb") as f:
        WriteModdedGHG(f)
        
    
    
    
    

