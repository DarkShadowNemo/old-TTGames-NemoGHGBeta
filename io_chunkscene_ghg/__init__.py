bl_info = {
        'name'			: 'Finding Nemo GHG Character Non Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 8, 6),
	'blender'		: (4, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import GHG mesh chunk',
	'category'		: 'Non-Chunk-Importer and Exporter',
}
import os
import bpy
import importlib
import time
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import GHG_importer,GHG_export 

class ImportNonChunkGHG(bpy.types.Operator, ImportHelper):
        bl_idname  = 'import_non_chunk.ghg'
        bl_label   = 'Import Non Chunk GHG'
        bl_options = {'UNDO'}
        filename_ext = '.ghg'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the GHG file without chunks.',
                type	    = bpy.types.OperatorFileListElement
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ghg', options = {'HIDDEN'})

        offset_on_off : BoolProperty(name="offset on or off", description="turn on or turn off offset") 

        #################################################

        bsa_on_off : BoolProperty(name="Blend Shapes", description="bsa on to true and bsa off to false")

        uv3rdnoloop : BoolProperty(name="uv 0x04020001 0", description="imports uvs on 0x04020001 with no loop, only once with 1 splited chunk file")

        uv3rdloop : BoolProperty(name="uv 0x04020001 -1", description="imports uvs on 0x04020001 with loop")

        uv2ndnoloop : BoolProperty(name="uv 0x03020001 0", description="imports uvs on 0x03020001 with no loop, only once with 1 splited chunk file")

        uv2ndloop : BoolProperty(name="uv 0x03020001 -1", description="imports uvs on 0x03020001 with loop")

        me2s3h: BoolProperty(name ="0x03020001 Tri", description = "imports by 0x03020001 with tri")

        me2s4h: BoolProperty(name ="0x03020001 Strip 4", description = "imports by 0x03020001 with 4th strips")

        me2s5h: BoolProperty(name ="0x03020001 Strip 5", description = "imports by 0x03020001 with 5th strips")

        me2s6h: BoolProperty(name ="0x03020001 Strip 6", description = "imports by 0x03020001 with 6th strips")

        me2s7h: BoolProperty(name ="0x03020001 Strip 7", description = "imports by 0x03020001 with 7th strips")
        
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(GHG_importer)
                for path in paths: GHG_importer.ghg_open(path)
                return {'FINISHED'}

class ExportNonChunkGHG(bpy.types.Operator, ExportHelper):
        bl_idname = "export_non_chunk.ghg"
        bl_label = "Export Non Chunk GHG"
        bl_options = {"UNDO"}
        filename_ext = ".ghg"
        files: CollectionProperty(
                name = "File path",
                description = 'File path used for finding the GHG file without chunks.',
                type	    = bpy.types.OperatorFileListElement
        )
        Shadow_0x04020001 : BoolProperty(
                name = "0x04020001 no Strip List Info",
                description = "Exports by 0x03010001 data, may cause flickering and bit buggy"
        )
        StripListInfo_0x04020001 : BoolProperty(
                name = "0x04020001 Strip List Info"
        )
        StripListInfo_0x04020001uv : BoolProperty(
                name = "0x04020001 Strip List Info uv"
        )
        StripListInfo_0x04020001imgOne : BoolProperty(
                name = "0x04020001 Strip List Info image"
        )
        StripListInfo_0x03020001 : BoolProperty(
                name = "0x03020001 Strip List Info"
        )

        Strip_0x030100010380XX6C: BoolProperty(
                name = "0x030100010380XX6C",
                description = "Exports by 0x03010001 data"
        )
        










        
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ghg', options = {'HIDDEN'})
        def execute(self, context):
            importlib.reload(GHG_export)
            GHG_export.ghg_save(self.filepath, StripListInfo_0x04020001=self.StripListInfo_0x04020001,StripListInfo_0x03020001=self.StripListInfo_0x03020001)
            return {"FINISHED"}
                

        
        

        
	
def menu_func_import(self, context):
        self.layout.operator(ImportNonChunkGHG.bl_idname, text='GHG Non Chunk Importer (.ghg)')
def menu_func_export(self, context):
        self.layout.operator(ExportNonChunkGHG.bl_idname, text='GHG Non Chunk Exporter (.ghg)')
def register():
        bpy.utils.register_class(ImportNonChunkGHG)
        bpy.utils.register_class(ExportNonChunkGHG)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
        bpy.utils.unregister_class(ImportNonChunkGHG)
        bpy.utils.unregister_class(ExportNonChunkGHG)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == '__main__': register()
