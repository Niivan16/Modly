# Modly (ComfyUI extension) - Blender-ready

This repo contains a Modly extension that routes image/text prompts and optional existing 3D files
into a ComfyUI workflow and tries to produce a .blend file (when Blender is available).

Files:
- manifest.json — metadata Modly uses to list & run the model
- requirements.txt — Python deps to install
- generator.py — the main script Modly will call (accepts text/image/existing file inputs)

Important notes
- To export .blend files this generator calls the `blender` CLI. You must have Blender installed
  (the full application, not a pip package) and accessible in PATH in the environment where Modly
  runs this generator.

- ComfyUI output formats and API responses vary with versions. For reliable operation:
  1. Export your ComfyUI workflow using "Save (API Format)" and add it to this repo as `workflow.json`,
     or upload it to Modly when installing the model.
  2. If your ComfyUI returns mesh URLs in a specific response structure, paste a sample response here
     or open an issue and I will adapt generator.py to parse and download the actual output files.

How to install in Modly
1. Open Modly → Models → Install from GitHub
2. Paste: https://github.com/Niivan16/Modly

Testing locally
- Ensure Blender is installed and `blender` is on PATH if you want .blend output.
- Example:

python generator.py --image path/to/test.png --out test_out --workflow path/to/workflow.json --text "a stylized statue"

If Blender is available and an OBJ/GLTF is produced, the script will attempt to save test_out/generated_model.blend

Next steps I can do for you
- Add your exported ComfyUI `workflow.json` to this repo and wire the payload parsing to download real outputs.
- Add a Blender edit script so the generator can apply deterministic edits to an existing .blend file (you can
  provide the script or describe the edit and I will write it).
