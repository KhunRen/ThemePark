import bpy

def set_HDRI(path):
    C = bpy.context
    scn = C.scene

    node_tree = scn.world.node_tree
    tree_nodes = node_tree.nodes

    tree_nodes.clear()

    node_background = tree_nodes.new(type='ShaderNodeBackground')

    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
    node_environment.image = bpy.data.images.load(path)
    node_environment.location = -300,0

    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
    node_output.location = 200,0

    links = node_tree.links
    link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
    link = links.new(node_background.outputs["Background"], node_output.inputs["Surface"])
    

def set_viewport_shading_material(scene_light = False, scene_world=False, rotation=0, strength=1, world_opacity=0, blur=0.5):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'MATERIAL'
                    space.shading.use_scene_lights=scene_light
                    space.shading.use_scene_world=scene_world
                    if scene_world == False:
                        space.shading.studiolight_rotate_z = rotation
                        space.shading.studiolight_intensity = strength
                        space.shading.studiolight_background_alpha = world_opacity
                        space.shading.studiolight_background_blur = blur
                    break

def eevee_sampling(render=64,viewport=16, viewport_denoise=True):
    bpy.context.scene.eevee.taa_render_samples = render
    bpy.context.scene.eevee.taa_samples = viewport
    bpy.context.scene.eevee.use_taa_reprojection = viewport_denoise
    
def eevee_ambient_occlusion(distance=0.2,factor=1,trace_precision=0.250,bend_normal=True, bounce_approximation=True):
    bpy.context.scene.eevee.use_gtao = True
    bpy.context.scene.eevee.gtao_distance = distance
    bpy.context.scene.eevee.gtao_factor = factor
    bpy.context.scene.eevee.gtao_quality = trace_precision
    bpy.context.scene.eevee.use_gtao_bent_normals = bend_normal
    bpy.context.scene.eevee.use_gtao_bounce = bounce_approximation
    
def eevee_bloom(threshold=0.800,knee=0.500,radius=6.500, color=(1,1,1),intensity=0.05,clamp=0):
    bpy.context.scene.eevee.use_bloom = True
    bpy.context.scene.eevee.bloom_threshold = threshold
    bpy.context.scene.eevee.bloom_knee = knee
    bpy.context.scene.eevee.bloom_radius = radius
    bpy.context.scene.eevee.bloom_color = color
    bpy.context.scene.eevee.bloom_intensity = intensity
    bpy.context.scene.eevee.bloom_clamp = clamp
    
def eevee_screen_space_reflections(refraction=False, half_res_trace=True,trace_precision=0.250,max_roughness=0.5,thickness=0.2,edge_fading=0.075, clamp=10.000):
    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_ssr_refraction= refraction
    bpy.context.scene.eevee.use_ssr_halfres = half_res_trace
    bpy.context.scene.eevee.ssr_quality = trace_precision
    bpy.context.scene.eevee.ssr_max_roughness = max_roughness
    bpy.context.scene.eevee.ssr_thickness = thickness
    bpy.context.scene.eevee.ssr_border_fade = edge_fading
    bpy.context.scene.eevee.ssr_max_roughness = clamp
    
def color_management(display_device="sRGB",view_transform="Standard",look="None",exposure=0.0,gamma=1.0,sequencer="sRGB"):
    bpy.context.scene.display_settings.display_device = display_device
    bpy.context.scene.view_settings.view_transform = view_transform
    bpy.context.scene.view_settings.look = look
    bpy.context.scene.view_settings.exposure = exposure
    bpy.context.scene.view_settings.gamma = gamma
    bpy.context.scene.sequencer_colorspace_settings.name = sequencer
    
def hide_hdri(hdri_path):
    
    C = bpy.context
    scn = C.scene

    node_tree = scn.world.node_tree
    tree_nodes = node_tree.nodes
    links = node_tree.links
    for node in tree_nodes:
        tree_nodes.remove(node)

    node_background = tree_nodes.new(type='ShaderNodeBackground')

    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
    node_environment.image = bpy.data.images.load(hdri_path)
    node_environment.location = -300,0

    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
    node_output.location = 200,0

    links = node_tree.links
    link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
    
    node_mix = tree_nodes.new(type='ShaderNodeMixShader')
    node_mix.location = 0, 200

    node_light_path = tree_nodes.new(type='ShaderNodeLightPath')
    node_light_path.location = -300, 200
    
    black = tree_nodes.new(type='ShaderNodeBackground')
    black.inputs['Color'].default_value = (0,0,0,1)


    link = links.new(node_light_path.outputs['Is Camera Ray'], node_mix.inputs['Fac'])
    link = links.new(node_background.outputs['Background'], node_mix.inputs[1])
    link = links.new(black.outputs['Background'], node_mix.inputs[2])
    link = links.new(node_mix.outputs['Shader'], node_output.inputs['Surface'])