import bpy

class AutoCartoonOutline(bpy.types.Operator):
    bl_idname = "mesh.auto_cartoon_outline"
    bl_label = "Insert Outline"
    bl_options = {'REGISTER', 'UNDO'}
    
    thickness: bpy.props.FloatProperty(
        name="Thickness",
        default=0.01,
        min=0.0,
        max=0.1,
        precision=4,
        subtype='DISTANCE',
        unit='LENGTH'
    )
    
    even_thickness: bpy.props.BoolProperty(
        name="Even Thickness",
        default=False
    )

    offset: bpy.props.FloatProperty(
        name="Offset",
        default=0.01,
        min=0.0,
        max=0.1,
        precision=4,
        subtype='DISTANCE',
        unit='LENGTH'
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'OBJECT'

    def execute(self, context):
        obj = context.active_object
        
        # Check if the solidify modifier already exists
        solidify_modifier = None
        for modifier in obj.modifiers:
            if modifier.name == "Auto Cartoon Outline Solidify":
                solidify_modifier = modifier
                break
        
        # Create a new material slot for the outline material
        mat_count = len(obj.material_slots)
        obj.active_material_index = mat_count
        bpy.ops.object.material_slot_add()
        material_offset = mat_count
        
        # Create a new material for the outline
        outline_material = bpy.data.materials.new(name="Auto Cartoon Outline")
        outline_material.use_backface_culling = True
        outline_material.blend_method = 'CLIP'
        outline_material.shadow_method = 'NONE'
        
        # Set material to emission
        outline_material.use_nodes = True
        nodes = outline_material.node_tree.nodes
        links = outline_material.node_tree.links
        for node in nodes:
            nodes.remove(node)
        emission = nodes.new(type='ShaderNodeEmission')
        emission.inputs['Color'].default_value = (0.0, 0.0, 0.0, 1.0)
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        links.new(emission.outputs['Emission'], material_output.inputs['Surface'])
        
        # Assign the material to the new material slot
        obj.material_slots[material_offset].material = outline_material
        
        # Set the solidify modifier settings
        if solidify_modifier is None:
            solidify_modifier = obj.modifiers.new(name="Auto Cartoon Outline Solidify", type='SOLIDIFY')
            solidify_modifier.material_offset = material_offset
        solidify_modifier.thickness = self.thickness
        solidify_modifier.use_even_offset = self.even_thickness
        solidify_modifier.offset = self.offset
        
        # Flip the normals of the solidify modifier
        solidify_modifier.use_flip_normals = True
        
        return {'FINISHED'}

    bl_idname = "mesh.auto_cartoon_outline"
    bl_label = "Insert Outline"
    bl_options = {'REGISTER', 'UNDO'}
    
    thickness: bpy.props.FloatProperty(
        name = "Thickness",
        default = 0.01,
        min = 0.0,
        max = 0.1,
        precision = 4,
        subtype = 'DISTANCE',
        unit = 'LENGTH'
    )
    
    even_thickness: bpy.props.BoolProperty(
        name = "Even Thickness",
        default = False
    )

    offset: bpy.props.FloatProperty(
        name = "Offset",
        default = 0.01,
        min = 0.0,
        max = 0.1,
        precision = 4,
        subtype = 'DISTANCE',
        unit = 'LENGTH'
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'OBJECT'

    def execute(self, context):
        obj = context.active_object
        
        # Count the number of materials
        mat_count = len(obj.material_slots)
        
        # Create a new material slot for the outline material
        obj.active_material_index = mat_count
        bpy.ops.object.material_slot_add()
        
        # Set the outline material offset to the new material slot
        material_offset = mat_count
                
        # Create a new material for the outline
        outline_material = bpy.data.materials.new(name="Auto Cartoon Outline")
        
        # Set the material settings
        outline_material.use_backface_culling = True
        outline_material.blend_method = 'CLIP'
        outline_material.shadow_method = 'NONE'

        # Set material to emission
        outline_material.use_nodes = True
        nodes = outline_material.node_tree.nodes
        links = outline_material.node_tree.links
        for node in nodes:
            nodes.remove(node)
        emission = nodes.new(type='ShaderNodeEmission')
        emission.inputs['Color'].default_value = (0.0, 0.0, 0.0, 1.0)
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        links.new(emission.outputs['Emission'], material_output.inputs['Surface'])
        
        # Assign the material to the new material slot
        obj.material_slots[material_offset].material = outline_material
        
        # Create a solidify modifier for the outline
        solidify_modifier = obj.modifiers.new(name="Auto Cartoon Outline Solidify", type='SOLIDIFY')
        
        # Set the solidify modifier settings
        solidify_modifier.thickness = self.thickness
        solidify_modifier.use_even_offset = self.even_thickness
        solidify_modifier.offset = self.offset
        solidify_modifier.material_offset = material_offset
        
        # Flip the normals of the solidify modifier
        solidify_modifier.use_flip_normals = True
        
        return {'FINISHED'}


class AutoCartoonOutlinePanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_auto_cartoon_outline_panel"
    bl_label = "Auto Cartoon Outline"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto Cartoon"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("mesh.auto_cartoon_outline", text="Insert Outline")
        col.prop(context.scene.auto_cartoon, "outline_thickness", text="Thickness")
        col.prop(context.scene.auto_cartoon, "outline_even_thickness", text="Even Thickness")
        col.prop(context.scene.auto_cartoon, "outline_offset", text="Offset")

class AutoCartoonSettings(bpy.types.PropertyGroup):
    outline_thickness: bpy.props.FloatProperty(
        name="Outline Thickness",
        default=1.0,
        min=-1.0,
        max=1.0,
        precision=4,
        subtype='DISTANCE',
        unit='LENGTH'
    )

    outline_even_thickness: bpy.props.BoolProperty(
        name="Even Thickness",
        default=False
    )

    outline_offset: bpy.props.FloatProperty(
        name="Offset",
        default=1.0,
        min=-1.0,
        max=1.0,
        precision=4,
        subtype='DISTANCE',
        unit='LENGTH'
    )


def register():
    bpy.utils.register_class(AutoCartoonSettings)
    bpy.utils.register_class(AutoCartoonOutline)
    bpy.utils.register_class(AutoCartoonOutlinePanel)
    bpy.types.Scene.auto_cartoon = bpy.props.PointerProperty(type=AutoCartoonSettings)


def unregister():
    bpy.utils.unregister_class(AutoCartoonOutline)
    bpy.utils.unregister_class(AutoCartoonOutlinePanel)
    bpy.utils.unregister_class(AutoCartoonSettings)
    del bpy.types.Scene.auto_cartoon
    

if __name__ == "__main__":
    register()