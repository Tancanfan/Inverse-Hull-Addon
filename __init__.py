bl_info = {
    "name": "Auto Cartoon Outline",
    "description": "Automatically add a cartoon-style outline to selected objects.",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Auto Cartoon",
    "warning": "",
    "category": "Mesh",
}

if "bpy" in locals():
    import importlib
    if "auto_cartoon" in locals():
        importlib.reload(auto_cartoon)

import bpy
from . import auto_cartoon


def register():
    auto_cartoon.register()


def unregister():
    auto_cartoon.unregister()


if __name__ == "__main__":
    register()
