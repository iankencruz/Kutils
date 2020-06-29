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
    "version" : (0, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Interface"
}


import bpy
from . kutils_modifiers_op import *




class Kutils(bpy.types.Panel):
    """Creates a Utility Panel for all common used tools"""
    bl_label = "Kutilies"
    bl_idname = "KUTILS_PT_utils"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kutils"



    """ Polls for Active Object """
    @classmethod
    def poll(cls, context):
        return (context.object is not None)





    def draw(self, context):
        layout = self.layout    

        ###################################
        #           File Manager           #

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



        ###################################
        #           Globals                #



        row = layout.row()  
        row.label(text="Global", icon='WORLD_DATA')
        
        # Gizmos Section
        view = context.space_data       
                
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
        
        row = layout.row(align=True)
        row.prop(overlay, "show_face_orientation",icon='ORIENTATION_NORMAL')
        row.operator('mesh.flip_normals', text="Flip Normals", icon='ARROW_LEFTRIGHT')

        # ClearCust
        row = layout.column()
        row.operator('mesh.customdata_custom_splitnormals_clear', text='Clear Custom Split Normals', icon = 'X')


        col = layout.column(align=True)
        col.operator('object.make_single_user', text="Make Single User", icon="SNAP_VOLUME").obdata=True
        row = col.split(align=True)
        objType = getattr(context.object, 'type', '')
        if objType  in ['CURVE']:
            row.operator('object.convert', text="Convert To Mesh", icon="MESH_CYLINDER").target='MESH'
        elif objType  in ['MESH']:
            row.operator('object.convert', text="Convert To Curve", icon="OUTLINER_DATA_CURVE").target='CURVE'

        # Auto Smoothing Test
        obj = context.object
        mesh = obj.data

        split = layout.split()

        col = split.row()
        col.prop(mesh, "use_auto_smooth")
        sub = col.row()
        sub.active = mesh.use_auto_smooth and not mesh.has_custom_normals
        sub.prop(mesh, "auto_smooth_angle", text="Angle")

        layout.separator()








        ###################################
        #           MODIFIERS                #
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
        
        if context.active_object.mode == 'OBJECT':
            row = layout.row()           
            row.label(text="Object mode", icon='SNAP_VOLUME')     

            # Shading
            split = layout.split(align=True)
            col = split.column(align=True)      
            col.operator('object.shade_smooth', text="Smooth", icon='SHADING_TEXTURE')  
            col.operator('object.origin_set', text='Cursor', icon='GIZMO').type = "ORIGIN_CURSOR"          
        
            # Origin
            col = split.column(align=True)
            col.operator('object.shade_flat', text="Flat", icon='SHADING_SOLID')  
            col.operator('object.origin_set', text='Geometry', icon='GIZMO').type = "ORIGIN_GEOMETRY"

            
            



        
        ###################################
        #           Edit                #
        
        if context.active_object.mode == 'EDIT':

            row = layout.row(align=True)
            row.label(text="Edit mode", icon='MOD_SOLIDIFY')

            # Align First and Last together
            col = layout.column(align=True)
            row = col.row(align=True)         
            for k in ['FIRST','CENTER','LAST']:                
                try:
                    row.operator("mesh.merge", text=k.title(), icon="GROUP_VERTEX").type = k
                except TypeError:
                    row.enabled = False
            #Align Big button "Distance" with first and last
            row = col.row(align=True)
            split = row.split(align=True)
            row.operator('mesh.remove_doubles', text='Distance', icon='DRIVER_DISTANCE').threshold = 0.01            
            col.operator('mesh.separate', text="Separate Selected", icon='FACESEL').type='SELECTED'            

            row = layout.row(align=True)
            row.operator('mesh.bridge_edge_loops', text='Bridge', icon='NOCURVE')
            row.operator('mesh.fill_grid', text='Grid Fill', icon='MESH_GRID')

            split = layout.split(align=True)
            col = split.column(align=True)
            col.operator('mesh.mark_seam', text='Mark Seam', icon='STICKY_UVS_VERT').clear=False
            col.operator('mesh.mark_seam', text='Clear Seam', icon='STICKY_UVS_DISABLE').clear=True    
              
            col = split.column(align=True) 
            col.operator('mesh.mark_sharp', text='Mark Sharp', icon='CUBE')     
            col.operator('mesh.mark_sharp', text='Clear Sharp',icon='MESH_CUBE').clear=True

            row = layout.row(align=True)
            row.operator("uv.unwrap", icon='UV')
            row.operator("uv.smart_project", icon='MOD_UVPROJECT')
            uv_projection = row.operator("uv.project_from_view", icon='UV_DATA')
            # Projection properties
            uv_projection.scale_to_bounds=False
            uv_projection.correct_aspect=True
            uv_projection.camera_bounds=False


            


classes = (Kutils, Mirror, Array, Solidify, Boolean, Lattice, Subsurf)


register, unregister = bpy.utils.register_classes_factory(classes)