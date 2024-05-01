bl_info = {
        'name'			: 'Finding Nemo GHG Character Non Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 2, 6),
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

from.import GHG_import, GHG_export

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

        offsets : StringProperty(name="offsets", description="all offsets may contain issues on most models but may work on custom only")

        input_on_off : BoolProperty(name="input on or off", description="turn on or off input names")

        input_name : StringProperty(name="Input name", description="must be the exact name as the folder by its file")

        #################################################

        bsa_on_off : BoolProperty(name="Blend Shapes", description="bsa on to true and bsa off to false")

        ghg_tex_utility : BoolProperty(name="GHG Tex On or off", description="turn on or off textures")

        seek_pallete : IntProperty(name="seek texture", description="seek where is the pallete")

        pallete_offsets : IntProperty(name="pallete offset", description="choose a pallete offset")
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(GHG_import)
                for path in paths: GHG_import.ghg_open(path, offset_on_off = self.offset_on_off, offsets = self.offsets, input_on_off = self.input_on_off, input_name = self.input_name, bsa_on_off = self.bsa_on_off, ghg_tex_utility = self.ghg_tex_utility, pallete_offsets = self.pallete_offsets, seek_pallete = self.seek_pallete)
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
        STRIP_SMOOTHS: BoolProperty(
                name = "SMOOTH STRIPS ONLY",
                description = "turns smooth in one material only multiply by 3 by flag 96",
        )
        offset_0x030100010380XX6C : IntProperty(
                name = "0x030100010380XX6C",
                description = "1 on 0x03010001"
        )
        offset_0x030200010380XX6D : IntProperty(
                name = "0x030200010380XX6D",
                description = "2 on 0x03020001"
        )
        offset_0x040200010380XX6C : IntProperty(
                name = "0x040200010380XX6C",
                description = "3 on 0x04020001"
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ghg', options = {'HIDDEN'})
        def execute(self, context):
            importlib.reload(GHG_export)
            GHG_export.ghg_save(self.filepath, STRIP_SMOOTHS = self.STRIP_SMOOTHS, offset_0x030100010380XX6C = self.offset_0x030100010380XX6C, offset_0x030200010380XX6D = self.offset_0x030200010380XX6D, offset_0x040200010380XX6C = self.offset_0x040200010380XX6C)
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
