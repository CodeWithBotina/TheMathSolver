# run.spec
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['run.py'],
    pathex=['/home/codewithbotina/CodeWithBotina/Dev/Projects/MathSolver/', '/home/codewithbotina/CodeWithBotina/Dev/Projects/MathSolver/src'],  # Add the path to src
    binaries=[],
    datas=[
        ('src/mathsolver/data/about.json', 'data'),
        ('src/mathsolver/ui/main_window.ui', 'mathsolver/ui'),
        ('src/mathsolver/ui/style/main_window.qss', 'mathsolver/ui/style'),
    ],  # Include resource files
    hiddenimports=['mathsolver'],  # Add the module here
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='run',
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