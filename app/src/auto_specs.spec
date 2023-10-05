# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ui.py'],
    pathex=['./', './app/src/modules'],
    binaries=[],
    datas=[],
    hiddenimports = ['app.src.modules.functions_ui', 'app.src.modules.delete_files', 'app.src.modules.rewrite_docx', 'app.src.modules.fix_mistakes', 'app.src.modules.hocr_parser', 'app.src.modules.run_tesseract', 'app.src.modules.rotate_and_split_image', 'app.src.modules.doublepage_img_rename', 'app.src.modules.singlepage_img_rename', 'app.src.modules.verify_folders', 'app.src.modules.setup_functions', 'app.src.modules.is_image', 'app.src.modules.logger_mod'],
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
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
