# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/mathsolver/main.py'],
    pathex=[],
    binaries=[],
    datas=[('src/mathsolver/ui/main_window.ui', 'mathsolver/ui'), ('src/mathsolver/ui/style/main_window.qss', 'mathsolver/ui/style'), ('src/mathsolver/about/about.json', 'mathsolver/about'), ('src/mathsolver/assets/icons/icon.ico', 'mathsolver/assets/icons'), ('src/mathsolver/assets/icons/icon.icns', 'mathsolver/assets/icons'), ('src/mathsolver/assets/icons/icon.png', 'mathsolver/assets/icons')],
    hiddenimports=[],
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
    name='MathSolver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src/mathsolver/assets/icons/icon.ico'],
)
