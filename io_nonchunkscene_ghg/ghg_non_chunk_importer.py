from struct import pack, unpack
import os
import bpy
import mathutils
import bmesh
from .nemo import pearl

def NonParseGHG(filepath, GHG_Meshes=1):
    with open(filepath, "rb") as f:
        #folder id
        if GHG_Meshes == 40:
            #Pearl
            pearl.WholeMeshGHGPearlOne(f, vertices=[], faces=[], uvs=[],normals=[], fa=-1,fb=0,fc=1)
                
        
                
        
        
        
