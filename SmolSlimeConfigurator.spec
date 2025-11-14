# -*- mode: python ; coding: utf-8 -*-

import sys

import shutil
nrfutil_executable_path = shutil.which("nrfutil")
print("nrfutil executable path:", nrfutil_executable_path)

a = Analysis(
    ['SmolSlimeConfigurator.py'],
    pathex=[],
    binaries=[
        (nrfutil_executable_path, '.')
    ],
    datas=[
        ('icon.ico', '.'),
    ],
    hiddenimports=[
        'nrfutil',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'pyinstaller',
        'altgraph',
        'pefile',
        'macholib',
        'setuptools',
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SmolSlimeConfigurator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
