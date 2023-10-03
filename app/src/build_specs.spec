# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ui.py'],
    pathex=['./', './modules'],
    binaries=[],
    datas=[],
    hiddenimports = ['modules.functions_ui', 'modules.delete_files', 'modules.rewrite_docx', 'modules.fix_mistakes', 'modules.hocr_parser', 'modules.run_tesseract', 'modules.rotate_and_split_image', 'modules.doublepage_img_rename', 'modules.singlepage_img_rename', 'modules.verify_folders', 'modules.setup_functions', 'modules.is_image'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OCRAutomation',
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
