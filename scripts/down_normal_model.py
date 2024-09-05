import subprocess

subprocess.run(["cd", "submodules/omnidata", "&&", "sh", "tools/download_surface_normal_models.sh"])
