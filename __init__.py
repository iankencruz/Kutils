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






class Kutils(bpy.types.Panel):
    """Creates a Utility Panel for all common used tools"""
    bl_label = "Kutilies"
    bl_idname = "KUTILS_PT_create"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kutils"




    @classmethod
    def poll(cls, context):
        return (context.object is not None)





    def draw(self, context):
        layout = self.layout    

        row = layout.row()  
        row.label(text="GLOBALS", icon='WORLD_DATA')

        
        # Gizmos Section
        scene = context.scene
        view = context.space_data       

        row = layout.row()
        row.label(text="Object Gizmo")
        
        row = layout.row(align=False)        
        row.prop(view, "show_gizmo_object_translate", text="M")
        row.prop(view, "show_gizmo_object_rotate", text="R")
        row.prop(view, "show_gizmo_object_scale", text="S")

        
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
            row.prop(overlay, "show_wireframes", text="")
        sub = row.row()
        sub.active = overlay.show_wireframes or is_wireframes
        sub.prop(overlay, "wireframe_threshold", text="Wireframe")

        col = layout.column(align=True)
        col.active = display_all
        
        col.prop(overlay, "show_face_orientation",)

        layout.separator()


        ###################################
        #           OBJECT                #
        
        row = layout.row()           
        # Change operator based on context is OBJECT mode    
        row.label(text="Object mode", icon='SNAP_VOLUME')     

        # Shading
        row = layout.row(align=True)        
        row.operator('object.shade_smooth')  
        row.operator('object.shade_flat')    
    
        # Origin
        row = layout.row(align=True)
        row.operator('object.origin_set', text='Set To Cursor').type = "ORIGIN_CURSOR"
        row.operator('object.origin_set', text='Set To Geo').type = "ORIGIN_GEOMETRY"

       

        
        
        
        # Change operator based on context is EDIT mode    t
        if context.active_object.mode == 'EDIT':

            obj = context.object
            col = layout.column()
            col.label(text="Edit mode", icon='MOD_SOLIDIFY')


            
            row = layout.row(align=False) 
            row.operator('mesh.separate').type='SELECTED'

            
            # Create new row var to section off operators 
            row = layout.row(align=True)                  
            row.operator('mesh.remove_doubles', text='Distance').threshold = 0.1              
            row.operator('mesh.merge', text='First').type='FIRST'
            row.operator('mesh.merge', text='Last').type='LAST'





def register():
    bpy.utils.register_class(Kutils)

def unregister():
    bpy.utils.unregister_class(Kutils)


