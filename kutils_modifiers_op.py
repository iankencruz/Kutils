import bpy

from bpy.types import Operator


class Mirror(bpy.types.Operator):
    """Creates a Mirror modifier on active object"""
    bl_idname = "object.mirror_operator"
    bl_label = "Mirror Modifier Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}


class Array(bpy.types.Operator):
    """Creates an Array modifier on active object"""
    bl_idname = "object.array_operator"
    bl_label = "Simple Array Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}

class Solidify(bpy.types.Operator):
    """Creates a Solidify modifier on active object"""
    bl_idname = "object.solidify_operator"
    bl_label = "Simple Solidify Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}

class Boolean(bpy.types.Operator):
    """Creates a Boolean modifier on active object"""
    bl_idname = "object.boolean_operator"
    bl_label = "Simple Boolean Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}

class Lattice(bpy.types.Operator):
    """Creates a Lattice modifier on active object"""
    bl_idname = "object.lattice_operator"
    bl_label = "Simple Lattice Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='LATTICE')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}

class Subsurf(bpy.types.Operator):
    """Creates a Subsurf modifier on active object"""
    bl_idname = "object.subsurf_operator"
    bl_label = "Simple Subsurf Operator"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.space_data.context = 'PROPERTIES'
        return {'FINISHED'}