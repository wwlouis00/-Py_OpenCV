
# OpenCV Image Grid Viewer with Python Bytecode Compilation

This project provides:

1. A Python script that displays multiple images in a single OpenCV window using a grid layout.
2. A utility script to compile Python source files (`.py`) into Python bytecode files (`.pyc`) for distribution.

The project is designed to be executed as standard `.py` scripts (not Jupyter Notebook).



## Features

### Image Grid Viewer
- Display multiple images in **one OpenCV window**
- Automatic **grid layout** (rows × columns)
- All images are **resized to a uniform size**
- Each image is **labeled with a title**
- Supports **grayscale and color images**
- Uses **pure OpenCV** (suitable for `.py` execution)

### Python Bytecode Compilation
- Compile `.py` files into `.pyc`
- Output compiled files into a dedicated `pyc/` directory
- Excludes the compiler script itself
- Uses optimization level `-O2` (removes docstrings and asserts)
- Useful for **source code protection** and **controlled deployment**


## Project Structure

```

project/
├── Photos/
│   ├── ROI_image.png
│   ├── result_well.png
│   ├── ROI_image_new.png
│   └── merge_finish.png
│
├── main.py               # Image grid display script
├── py_compile.py         # Python bytecode compiler
├── pyc/                  # Output directory for .pyc files
└── README.md

````


## Requirements

- Python 3.8 or newer (recommended to keep compile/run versions identical)
- OpenCV (GUI version)

Install dependencies:
```bash
pip install opencv-python numpy
````

⚠️ Do **NOT** use `opencv-python-headless`, as GUI windows are required.


## Image Grid Viewer Usage

### Description

The image viewer loads four images and displays them in a **2×2 grid**:

* Well Image
* Original ROI (grayscale)
* New ROI
* Merged Result

Each image is resized and labeled for easy comparison.


### Run the Viewer

```bash
python main.py
```

### Behavior

* A single OpenCV window will appear
* Images are displayed in a grid
* Press **any key** to close the window


## Python Bytecode Compilation

### Why Compile to `.pyc`?

* Faster startup (bytecode is precompiled)
* Basic source code protection
* Prevents accidental modification of source files
* Common in internal tools and production environments

⚠️ `.pyc` files are **Python-version dependent**.


### Run the Compiler

```bash
python py_compile.py
```

### Output Example

```
Compiled  py_compile.py -> pyc/image_grid_viewer.pyc
```

Compiled files will be placed in:

```
pyc/
└── image_grid_viewer.pyc
```

## Using the Compiled `.pyc` Files

### Run Directly

```bash
python pyc/image_grid_viewer.pyc
```

### Or Import as a Module

```python
import sys
sys.path.append("pyc")

import image_grid_viewer
image_grid_viewer.main()
```

⚠️ If both `.py` and `.pyc` exist, Python will always prefer `.py`.

## Important Notes

* Compile and run using the **same Python version**
* `.pyc` files are **not encrypted**, only obfuscated
* Remove `.py` files if you want to enforce `.pyc` usage
* Ensure OpenCV GUI support is available on the target system

