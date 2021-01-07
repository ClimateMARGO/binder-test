from os.path import expanduser, join

def setup_plutoserver():
  return {
    "command": ["julia", "--optimize=0", "--project=pluto", "-e", "import Pluto; Pluto.run(host=\"0.0.0.0\", port={port}, require_secret_for_access=false, require_secret_for_open_links=false, launch_browser=false, sysimage=\"notebook_sysimage.so\", project=pwd())"],
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
    },
  }