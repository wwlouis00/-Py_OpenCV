import py_compile
from pathlib import Path

SRC_DIR = Path(".")
OUT_DIR = Path("pyc")
OUT_DIR.mkdir(exist_ok=True)

for py_file in SRC_DIR.glob("*.py"):
    if py_file.name == Path(__file__).name:
        continue

    out_file = OUT_DIR / (py_file.stem + ".pyc")
    py_compile.compile(
        file=str(py_file),
        cfile=str(out_file),
        optimize=2
    )

    print(f"Compiled {py_file.name} -> {out_file}")
