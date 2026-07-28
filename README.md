# Modly (ComfyUI extension) - Blender-ready

This repo contains a Modly extension that routes image/text prompts and optional existing 3D files
into a ComfyUI workflow and tries to produce a .blend file (when Blender is available).

What I fixed in this commit
- Corrected generator.py to remove variable name typos (comfyurl/comfyui_url vs comfy_url)
- Hardened workflow loading and result parsing
- Added a sample `workflow.json` that includes explicit nodes so Modly/ComfyUI users won't see "nodes missing"
- Added `generator_class` to manifest.json previously; ensure Modly is reinstalled after these changes

Important notes
- The included `workflow.json` is a minimal example. Export your real ComfyUI workflow using "Save (API Format)"
  and replace `workflow.json` with that file for real results.
- Blender CLI: To export .blend files the environment where Modly runs this generator needs Blender installed
  and accessible via the `blender` executable in PATH.

Install into Modly
1. Open Modly → Models → Install from GitHub
2. Paste: https://github.com/Niivan16/Modly

Testing locally
python generator.py --image path/to/test.png --out test_out --workflow workflow.json --text "a stylized statue"

If Modly still reports errors
- Reinstall the model in Modly (uninstall first, then install from GitHub). Modly caches the manifest and generator import.
- If you get an error, copy the full error text here and I will fix it.
