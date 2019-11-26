# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Kutils",
    "author" : "ikruz",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}


import bpy
from . kutils_modifiers_op import *






class KFile_Manager(bpy.types.Panel):
    """Creates a Utility Panel for all common used tools"""
    bl_label = "File Manager"
    bl_idname = "KFM_PT_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kutils"



    @classmethod
    def poll(cls, context):
        return (context.object is not None)


    def draw(self, context):
        layout = self.layout
        row = layout.row()

        

        
        row.label(text="Files", icon='FILEBROWSER')

        split = layout.split(align=True)
        col = split.column(align=True)
        col.operator('wm.read_homefile', text='New', icon='FILE_NEW')
        col.operator('wm.link', icon='LINK_BLEND')
        col.operator('import_scene.fbx', icon='IMPORT')

        col = split.column(align=True)
        col.operator('wm.open_mainfile', text='Open')        
        col.operator('wm.append', icon='APPEND_BLEND')        
        col.operator('export_scene.fbx', icon='EXPORT')


        col = layout.column(align=True)
        col.operator('wm.search_menu', text="Search", icon='VIEWZOOM')
        
        




class Kutils(bpy.types.Panel):
    """Creates a Utility Panel for all common used tools"""
    bl_label = "Kutilies"
    bl_idname = "KUTILS_PT_utils"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kutils"




    @classmethod
    def poll(cls, context):
        return (context.object is not None)





    def draw(self, context):
        layout = self.layout    


        ###################################
        #           Globals                #



        row = layout.row()  
        row.label(text="Global Controls", icon='WORLD_DATA')
        
        # Gizmos Section
        scene = context.scene
        view = context.space_data       

        row = layout.row()
        row.label(text="Object Gizmo")
        
        row = layout.row(align=True)        
        row.prop(view, "show_gizmo_object_translate", text="Move", icon='OUTLINER_DATA_EMPTY')
        row.prop(view, "show_gizmo_object_rotate", text="Rotate",icon='ORIENTATION_GIMBAL')
        row.prop(view, "show_gizmo_object_scale", text="Scale", icon='ORIENTATION_LOCAL')

        
        # Wireframe and orientation code
        view = context.space_data
        overlay = view.overlay
        display_all = overlay.show_overlays
        is_wireframes = view.shading.type == 'WIREFRAME'

        col = layout.column()
        col.active = display_all

        row = col.row(align=True)
        #If Not Active
        if not is_wireframes:
            row.prop(overlay, "show_wireframes", text="", icon='MOD_WIREFRAME')
        sub = row.row()
        sub.active = overlay.show_wireframes or is_wireframes
        sub.prop(overlay, "wireframe_threshold", text="Wireframe")

        col = layout.column(align=True)
        col.active = display_all
        
        col.prop(overlay, "show_face_orientation",icon='ORIENTATION_NORMAL')

        layout.separator()






        ###################################
        #           MODIFIERS                #
        
        obj = context.active_object
        row = layout.row()           
        row.label(text="Modifiers", icon='MODIFIER')     

        split = layout.split(align=True)
        col = split.column(align=True)
        col.operator('object.array_operator',text='Array', icon='MOD_ARRAY')
        col.operator('object.mirror_operator', text='Mirror', icon='MOD_MIRROR')
        col.operator('object.solidify_operator', text='Solidify', icon='MOD_SOLIDIFY')
        col = split.column(align=True)
        col.operator('object.boolean_operator', text='Boolean', icon='MOD_BOOLEAN')
        col.operator('object.lattice_operator', text='Lattice', icon='MOD_LATTICE')
        col.operator('object.subsurf_operator', text='Subsurf', icon='MOD_SUBSURF')


        ###################################
        #           OBJECT                #
        
        row = layout.row()           
        row.label(text="Object mode", icon='SNAP_VOLUME')     

        # Shading
        split = layout.split(align=True)
        col = split.column(align=True)      
        col.operator('object.shade_smooth', icon='SHADING_TEXTURE')  
        col.operator('object.origin_set', text='Cursor', icon='GIZMO').type = "ORIGIN_CURSOR"
          
    
        # Origin
        col = split.column(align=True)
        col.operator('object.shade_flat', icon='SHADING_SOLID')  
        col.operator('object.origin_set', text='Geometry', icon='GIZMO').type = "ORIGIN_GEOMETRY"



    
        
        
        ###################################
        #           Edit                #
        
        if context.active_object.mode == 'EDIT':

            row = layout.row()
            row.label(text="Edit mode", icon='MOD_SOLIDIFY')

            
            row = layout.row(align=False) 
            row.operator('mesh.separate', text="Separate Selected", icon='FACESEL').type='SELECTED'

            
            # Create new row var to section off operators 
            row = layout.row(align=True)                  
            row.operator('mesh.remove_doubles', text='Distance', icon='DRIVER_DISTANCE').threshold = 0.1              
            row.operator('mesh.merge', text='Cursor', icon='PIVOT_CURSOR').type='CURSOR'


            split = layout.split(align=True)
            col = split.column(align=True)
            col.operator('mesh.mark_seam', text='Mark Seam', icon='STICKY_UVS_VERT').clear=False
            col.operator('mesh.mark_sharp', text='Mark Sharp', icon='CUBE')   
            col = split.column(align=True) 
            col.operator('mesh.mark_seam', text='Clear Seam', icon='STICKY_UVS_DISABLE').clear=True        
            col.operator('mesh.mark_sharp', text='Clear Sharp',icon='MESH_CUBE').clear=True

            row = layout.row()
            row.operator("uv.unwrap", icon='UV_VERTEXSEL')

            




def register():    
    bpy.utils.register_class(KFile_Manager)
    bpy.utils.register_class(Kutils)

    #modifiers
    bpy.utils.register_class(Mirror)
    bpy.utils.register_class(Array)
    bpy.utils.register_class(Solidify)
    bpy.utils.register_class(Boolean)
    bpy.utils.register_class(Lattice)
    bpy.utils.register_class(Subsurf)

def unregister():
    bpy.utils.unregister_class(KFile_Manager)
    bpy.utils.unregister_class(Kutils)

    #modifiers
    bpy.utils.unregister_class(Mirror)
    bpy.utils.unregister_class(Array)
    bpy.utils.unregister_class(Solidify)
    bpy.utils.unregister_class(Boolean)
    bpy.utils.unregister_class(Lattice)
    bpy.utils.unregister_class(Subsurf)