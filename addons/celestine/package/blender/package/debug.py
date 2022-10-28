# <pep8-80 compliant>
"""Print the length of all Blender data types."""
import bpy  # pylint: disable=import-error

print(len(bpy.data.actions), "actions")
print(len(bpy.data.armatures), "armatures")
print(len(bpy.data.brushes), "brushes")
print(len(bpy.data.cache_files), "cache_files")
print(len(bpy.data.cameras), "cameras")
print(len(bpy.data.collections), "collections")
print(len(bpy.data.curves), "curves")
print(len(bpy.data.filepath), "filepath")
print(len(bpy.data.fonts), "fonts")
print(len(bpy.data.grease_pencils), "grease_pencils")
print(len(bpy.data.images), "images")
print(len(bpy.data.lattices), "lattices")
print(len(bpy.data.libraries), "libraries")
print(len(bpy.data.lightprobes), "lightprobes")
print(len(bpy.data.lights), "lights")
print(len(bpy.data.linestyles), "linestyles")
print(len(bpy.data.masks), "masks")
print(len(bpy.data.materials), "materials")
print(len(bpy.data.meshes), "meshes")
print(len(bpy.data.metaballs), "metaballs")
print(len(bpy.data.movieclips), "movieclips")
print(len(bpy.data.node_groups), "node_groups")
print(len(bpy.data.objects), "objects")
print(len(bpy.data.paint_curves), "paint_curves")
print(len(bpy.data.palettes), "palettes")
print(len(bpy.data.particles), "particles")
print(len(bpy.data.scenes), "scenes")
print(len(bpy.data.screens), "screens")
print(len(bpy.data.shape_keys), "shape_keys")
print(len(bpy.data.sounds), "sounds")
print(len(bpy.data.speakers), "speakers")
print(len(bpy.data.texts), "texts")
print(len(bpy.data.textures), "textures")
print(len(bpy.data.version), "version")
print(len(bpy.data.volumes), "volumes")
print(len(bpy.data.window_managers), "window_managers")
print(len(bpy.data.workspaces), "workspaces")
print(len(bpy.data.worlds), "worlds")

# {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}