from kivy_deps import sdl2, glew, gstreamer

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['piano_chordprogression.py'],
             pathex=['C:\\Users\\zichk\\Desktop\\SublimePianoProgression'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PianoChordProgression',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\zichk\\Desktop\\SublimePianoProgression\\pics\\TaylorAcademy.ico')
coll = COLLECT(exe, Tree('C:\\Users\\zichk\\Desktop\\SublimePianoProgression'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PianoChordProgression')
