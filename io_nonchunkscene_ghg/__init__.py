bl_info = {
        'name'			: 'Finding Nemo GHG Character Non Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 2, 1),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import GHG one mesh chunk makes it easier',
	'category'		: 'Non-Chunk-Importer',
        'warning'               : 'Export is missing',
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import ghg_non_chunk_importer

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
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(ghg_non_chunk_importer)
                for path in paths: ghg_non_chunk_importer.NonParseGHG(path)
                return {'FINISHED'}
	
def menu_func_import(self, context):
        self.layout.operator(ImportNonChunkGHG.bl_idname, text='GHG Non Chunk Importer (.ghg)')
def register():
        bpy.utils.register_class(ImportNonChunkGHG)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
def unregister():
        bpy.utils.unregister_class(ImportNonChunkGHG)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
if __name__ == '__main__': register()
