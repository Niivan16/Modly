#!/usr/bin/env bash
set -e

echo "This script clones MrForExample/ComfyUI-3D-Pack into ./comfyui_3d_pack"
if [ -d "comfyui_3d_pack" ]; then
  echo "comfyui_3d_pack already exists — aborting. Remove or rename the directory to fetch again." 
  exit 0
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git not found on PATH. Please install git or clone manually:"
  echo "  git clone https://github.com/MrForExample/ComfyUI-3D-Pack comfyui_3d_pack"
  exit 1
fi

git clone https://github.com/MrForExample/ComfyUI-3D-Pack comfyui_3d_pack

echo "Cloned ComfyUI-3D-Pack into comfyui_3d_pack"

echo "Next steps: follow comfyui_3d_pack/README.md to copy node files into your ComfyUI custom_nodes folder or use workflows in ComfyUI UI. Then export a workflow JSON (API format) and place it at comfyui_integration/workflow.json"
