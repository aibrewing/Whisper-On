"""
Whisper On — .exe builder
Run this script on Windows inside the whisper-on folder:
    python build_exe.py

Requirements (install once):
    pip install pyinstaller

Output: dist/WhisperOn.exe  (~60-80 MB, standalone, no Python needed)
"""
import subprocess, sys, os

spec = """
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['transcriber.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('index.html', '.'),
    ],
    hiddenimports=[
        'pystray._win32',
        'PIL._imagingtk',
        'pyaudio',
        'flask',
        'flask_cors',
        'keyboard',
        'pyperclip',
        'pynput.keyboard._win32',
        'pynput.mouse._win32',
        'requests',
    ],
    hookspath=[],
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
    name='WhisperOn',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # no terminal window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='icon.ico',      # uncomment and add icon.ico to use a custom icon
)
"""

# Write spec file
with open('WhisperOn.spec', 'w') as f:
    f.write(spec)

print("Building WhisperOn.exe...")
print("This may take 3-5 minutes on first run.\n")

result = subprocess.run(
    [sys.executable, '-m', 'PyInstaller', 'WhisperOn.spec', '--clean'],
    capture_output=False,
    text=True,
)

if result.returncode == 0:
    size_mb = os.path.getsize('dist/WhisperOn.exe') / 1024 / 1024
    print(f"\n✅ Build complete: dist/WhisperOn.exe ({size_mb:.0f} MB)")
    print("Copy WhisperOn.exe anywhere and double-click to run.")
    print("config.json and history.json will be created next to the .exe on first run.")
else:
    print("\n❌ Build failed.")
    print("\nTo diagnose, open a terminal in this folder and run:")
    print("  pyinstaller WhisperOn.spec --clean")
    print("\nOr run this for a more detailed log:")
    print("  pyinstaller WhisperOn.spec --clean --log-level DEBUG > build_log.txt 2>&1")
    print("\nCommon causes and fixes:")
    print("  Missing packages  → pip install pyinstaller pystray pillow pyaudio keyboard pyperclip pynput flask flask-cors requests")
    print("  pyaudio error     → pip install pipwin && pipwin install pyaudio")
    print("  Permission error  → run terminal as Administrator")
