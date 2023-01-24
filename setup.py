import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"], "include_files": ['Imagens/',
                                                           'TemaDefault/',
                                                           'DLLs/python3.dll',
                                                           'DLLs/python310.dll']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Consultor",
    version="0.1",
    description="Cotação, conversão e muito mais!",
    options={"build_exe": build_exe_options},
    executables=[Executable("consultor.py", base=base, icon='Imagens/Ico_Princ.ico')]
)
