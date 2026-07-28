ComfyUI-3D-Pack integration added.

- To use: run comfyui_integration/fetch_upstream.sh to clone the upstream project into comfyui_3d_pack
- Start ComfyUI and follow that project's README to install nodes/workflows
- Export a workflow (API format) and place it at comfyui_integration/workflow.json (or upload via Modly)
- Run the Modly model with workflow_json pointing to that file, or let generator.py find it in the repo

I did not copy upstream code — you must fetch it via the script so you have the latest version and comply with upstream licensing.
