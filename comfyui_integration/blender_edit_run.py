#!/usr/bin/env python3
"""
blender_edit.py
Run inside Blender: blender --background --python blender_edit.py -- <input_mesh> <output_blend> [decimate_ratio]
"""
import sys
import bpy

def main():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    if len(argv) < 2:
        print("Usage: blender --background --python blender_edit.py -- <input_mesh> <output_blend> [decimate_ratio]")
        return
    in_path = argv[0]
    out_path = argv[1]
    decimate_ratio = float(argv[2]) if len(argv) > 2 else None

    bpy.ops.wm.read_factory_settings(use_empty=True)

    if in_path.lower().endswith('.obj'):
        bpy.ops.import_scene.obj(filepath=in_path)
    elif in_path.lower().endswith('.gltf') or in_path.lower().endswith('.glb'):
        bpy.ops.import_scene.gltf(filepath=in_path)
    else:
        print('Unsupported format for import:', in_path)

    for ob in list(bpy.context.scene.objects):
        if ob.type == 'MESH':
            bpy.context.view_layer.objects.active = ob
            if decimate_ratio is not None:
                mod = ob.modifiers.new(name='DecimateMod', type='DECIMATE')
                mod.ratio = decimate_ratio
                bpy.ops.object.modifier_apply(modifier=mod.name)
            bpy.ops.object.shade_smooth()
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    bpy.ops.wm.save_mainfile(filepath=out_path)
    print('Saved .blend to', out_path)

if __name__ == '__main__':
    main()
