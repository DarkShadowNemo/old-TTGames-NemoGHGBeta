bl_info = {
        'name'			: 'Finding Nemo GHG Character Non Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 3, 1),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import GHG mesh chunk',
	'category'		: 'Non-Chunk-Importer and Exporter',
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import ghg_non_chunk_importer, ghg_non_chunk_exporter

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

        offset_1 : BoolProperty(name="offset 0x03010001", description="0x030100010380XX6C")

        seek_ : IntProperty(name="seek 1", description="targets to seek 0x030100010380")

        seek__ : IntProperty(name="seek 2", description="targets to seek 0x030200010380")

        seek___ : IntProperty(name="seek 3", description="targets to seek 0x040200010380")
        
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(ghg_non_chunk_importer)
                for path in paths: ghg_non_chunk_importer.NonParseGHG(path, offset_1 = self.offset_1, seek_ = self.seek_)
                return {'FINISHED'}

class ExportNonChunkGHG(bpy.types.Operator, ExportHelper):
        bl_idname  = 'export_non_chunk.ghg'
        bl_label   = 'Export Non Chunk GHG'
        bl_options = {'UNDO'}
        filename_ext = '.ghg'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the GHG file without chunks.',
                type	    = bpy.types.OperatorFileListElement
        )

        appendGHG : BoolProperty(name="append 0x030100010380")

        noappendGHG : BoolProperty(name="no append 0x030100010380")

        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ghg', options = {'HIDDEN'})

        def execute(self, context):
            importlib.reload(ghg_non_chunk_exporter)
            ghg_non_chunk_exporter.WritingEditGHG(self.filepath, appendGHG = self.appendGHG, noappendGHG = self.noappendGHG)
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
