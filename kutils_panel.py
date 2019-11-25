import bpy


class Kutils(bpy.types.Panel):
    """Creates a Utility Panel for all common used tools"""
    bl_label = "Kutilies"
    bl_idname = "kutils_PT_create"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kutils"

    def draw(self, context):
        layout = self.layout    
        
        row = layout.row()
        

        
        
        
        # Change operator based on context is OBJECT mode    
        if context.active_object.mode == 'OBJECT':
            row.label(text="Object mode", icon='SNAP_VOLUME')
            
            row = layout.column()        
            layout.operator('object.origin_set', text='ORIGIN TO 3D Cursor').type = "ORIGIN_CURSOR"
        
        
        
        # Change operator based on context is EDIT mode    t
        if context.active_object.mode == 'EDIT':
            col = layout.column(align=True)
            col.label(text="Edit mode", icon='MOD_SOLIDIFY')
            
            # Create new row var to section off operators
            row = layout.row()        
            row.operator('mesh.merge', text='To First').type = 'FIRST'
            row.operator('mesh.merge', text='To Last').type = 'LAST'           
            
            row2 = layout.row()   
            row2.operator('mesh.merge', text='ToD First').type = 'FIRST'
            row2.operator('mesh.merge', text='ToD Last').type = 'LAST'                  
               
            layout.operator('mesh.remove_doubles', text='Merge by Distance').threshold = 0.5    



        
        
        

      


def register():
    bpy.utils.register_class(Kutils)


def unregister():
    bpy.utils.unregister_class(Kutils)


if __name__ == "__main__":
    register()
