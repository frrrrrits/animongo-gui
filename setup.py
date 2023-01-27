from __future__ import annotations

import sys
from cx_Freeze import Executable, setup

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    get_qt_plugins_paths = None

include_files = ['icon.ico']

if get_qt_plugins_paths:
    for plugin_name in (
        "wayland-decoration-client",
        "wayland-graphics-integration-client",
        "wayland-shell-integration",
    ):
        include_files += get_qt_plugins_paths("PyQt5", plugin_name)

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

build_exe_options = {
    # exclude packages that are not really needed
    "excludes": ["tkinter", "unittest", "email", "http", "xml", "pydoc", "PyQt6", "PySide6"],
    "include_files": include_files,
    "zip_include_packages": ["PyQt5"],
}

bdist_mac_options = {
    "bundle_name": "animongo_build",
}

bdist_dmg_options = {
    "volume_label": "ANIMONGO_BUILD",
}

executables = [Executable("main.py", base=base, icon="icon.ico")]

setup(
    name = "AnimOngo",
    version = "1.0",
    description = "Animongo GUI version made with Python",
    author = "lxs7499",
    options = {
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
    executables=executables,
)