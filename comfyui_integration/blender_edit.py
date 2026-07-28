# Blender edit script for Modly outputs

This Blender Python script is an example of operations you may want to run automatically after generating a mesh.
It is intended to be invoked by the generator using the Blender CLI:

  blender --background --python blender_edit.py -- <input_mesh> <output_blend> <decimate_ratio>

Operations performed:
- Clear default scene
- Import OBJ or GLTF
- Apply a Decimate modifier with the given ratio (0.0-1.0), if provided
- Shade smooth
- Recenter origin to geometry
- Save .blend file

Note: run this from the directory where Blender can access the files.
