from struct import unpack, pack
import os
import bmesh
import math
import bpy
import mathutils
from io import BytesIO as bio
from .GHGImportLib.GHG_import import *

def ghg_open(filepath):
    with open(filepath, "rb") as f:
        GHG_mesh(f, filepath)
