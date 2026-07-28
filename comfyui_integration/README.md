# ComfyUI-3D-Pack Integration for Modly

This folder contains helper scripts and instructions to integrate the ComfyUI-3D-Pack (or other ComfyUI 3D workflows) with this Modly extension repository.

Goal
- Provide a ready path to use the community ComfyUI-3D-Pack workflows (text+image → 3D), export their API-format workflow JSON, and run them from Modly using generator.py.

Important upstream repo (you should review license and README before use)
- MrForExample/ComfyUI-3D-Pack: https://github.com/MrForExample/ComfyUI-3D-Pack

What this integration provides
- fetch_upstream.sh: helper to clone the upstream ComfyUI-3D-Pack into ./comfyui_3d_pack
- workflow_example.json: a tiny example placeholder (replace with an exported API-format workflow from ComfyUI)
- blender_edit.py: example Blender script to decimate, smooth, recenter origin, and save .blend
- README with step-by-step instructions

How this is intended to be used
1. Run the fetch script locally (or on the Modly host) to download the ComfyUI-3D-Pack nodes/workflows:
   ./comfyui_integration/fetch_upstream.sh

2. Start ComfyUI and load the ComfyUI-3D-Pack nodes or workflows per that project's README.

3. In ComfyUI, open a workflow (for example a Trellis2 or Hunyuan3D workflow) and export it using "Save (API Format)".
   Save the exported JSON into this repo at: comfyui_integration/workflow.json (or upload it via Modly when installing the model).

4. In Modly, install this repository (https://github.com/Niivan16/Modly). When running the model, pass the `workflow_json` input pointing to the exported workflow file or include `workflow.json` in the repo.

Notes
- This repo DOES NOT bundle the full ComfyUI-3D-Pack content. You must fetch the upstream package using the script because that project is maintained separately and may have large files or submodules.
- If Modly runs in an environment without git/network access, clone the upstream repo manually on the host or copy the exported workflow.json into the repo.

License & upstream
- Please review the ComfyUI-3D-Pack repo license and the licenses of any AI models you use. Use these projects in accordance with their licenses.
