# modly-comfyui-extension

A beginner-friendly Modly extension template that routes an input image to a local ComfyUI instance and returns a 3D mesh.

Files:
- manifest.json — metadata Modly uses to list & run the model
- requirements.txt — Python deps to install
- generator.py — the main script Modly will call

Quick start
1. This repository contains the files Modly needs to install the model.
2. In Modly: Models page → Install from GitHub → paste the repo HTTPS URL: https://github.com/Niivan16/Modly

Testing locally
Run generator.py directly to test without Modly:

python generator.py --image path/to/test.png --out test_out --workflow path/to/workflow.json

Next steps
- Export your ComfyUI workflow in "API format" and either add it to the repo or upload it to Modly when running the model.
- If you provide a sample ComfyUI queue/history response, I can adapt generator.py to download the actual mesh outputs.
