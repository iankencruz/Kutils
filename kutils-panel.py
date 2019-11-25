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
        obj = context.object
        
        row = layout.row()
        
        # Change operator based on context is EDIT mode    
        if context.active_object.mode == 'EDIT':
            row.label(text="Hello EDIT!", icon='WORLD_DATA')
                     
            layout.operator('mesh.merge', text='To First').type = 'FIRST'
            layout.operator('mesh.merge', text='To Last').type = 'LAST'           
                     
            layout.operator('mesh.remove_doubles', text='Merge by Distance').threshold = 0.5    
#            layout.operator('mesh.remove_doubles', text='To First').type = 'FIRST'     
           
        # Change operator based on context is OBJECT mode    
        if context.active_object.mode == 'OBJECT':
            row.label(text="Hello OBJECT!", icon='WORLD_DATA')
            
            row = layout.column()        
            layout.operator('object.origin_set', text='ORIGIN TO 3D Cursor').type = "ORIGIN_CURSOR"

        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")
        
        

      


def register():
    bpy.utils.register_class(Kutils)


def unregister():
    bpy.utils.unregister_class(Kutils)


if __name__ == "__main__":
    register()
