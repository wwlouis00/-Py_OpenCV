#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Display multiple images in a single OpenCV window using a grid layout.
Each image is resized to the same size and labeled with a title.

This script is designed to be executed as a .py file (not Jupyter).
"""

from pathlib import Path
import cv2
import numpy as np


# =========================
# Path Configuration
# =========================
PHOTO_DIR = Path("Photos")
ROI_SRC = PHOTO_DIR / "ROI_image.png"
WELL_SRC = PHOTO_DIR / "result_well.png"
ROI_NEW_SRC = PHOTO_DIR / "ROI_image_new.png"
MERGE_SRC = PHOTO_DIR / "merge_finish.png"


# =========================
# Utility Functions
# =========================
def load_image(path: Path, gray: bool = False) -> np.ndarray:
    """
    Load an image from disk.

    Args:
        path (Path): Image file path
        gray (bool): Load as grayscale if True

    Returns:
        np.ndarray: Loaded image

    Raises:
        FileNotFoundError: If the image cannot be loaded
    """
    flag = cv2.IMREAD_GRAYSCALE if gray else cv2.IMREAD_COLOR
    img = cv2.imread(str(path), flag)

    if img is None:
        raise FileNotFoundError(f"Failed to load image: {path}")

    return img


def ensure_bgr(img: np.ndarray) -> np.ndarray:
    """
    Ensure the image is in BGR format.
    Converts grayscale images to BGR for concatenation.

    Args:
        img (np.ndarray): Input image

    Returns:
        np.ndarray: BGR image
    """
    if img.ndim == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def resize_image(img: np.ndarray, size: tuple[int, int]) -> np.ndarray:
    """
    Resize image to a fixed size.

    Args:
        img (np.ndarray): Input image
        size (tuple): (width, height)

    Returns:
        np.ndarray: Resized image
    """
    return cv2.resize(img, size)


def draw_title(img: np.ndarray, title: str) -> np.ndarray:
    """
    Draw a title text on the top-left corner of the image.

    Args:
        img (np.ndarray): Input image
        title (str): Title text

    Returns:
        np.ndarray: Image with title drawn
    """
    output = img.copy()
    cv2.putText(
        output,
        title,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )
    return output


# =========================
# Image Grid Display
# =========================
def show_image_grid(
    images: list[np.ndarray],
    titles: list[str],
    grid_shape: tuple[int, int],
    window_name: str = "Image Overview",
    cell_size: tuple[int, int] = (400, 300)
) -> None:
    """
    Display multiple images in a grid layout within a single OpenCV window.

    Args:
        images (list): List of images
        titles (list): List of titles for each image
        grid_shape (tuple): (rows, cols)
        window_name (str): OpenCV window name
        cell_size (tuple): Size of each grid cell (width, height)
    """
    rows, cols = grid_shape

    assert len(images) == len(titles), "Images and titles count mismatch"
    assert rows * cols >= len(images), "Grid size is too small"

    processed_images = []

    # Prepare images
    for img, title in zip(images, titles):
        img = ensure_bgr(img)
        img = resize_image(img, cell_size)
        img = draw_title(img, title)
        processed_images.append(img)

    # Fill empty cells with black images if necessary
    blank = np.zeros((cell_size[1], cell_size[0], 3), dtype=np.uint8)
    while len(processed_images) < rows * cols:
        processed_images.append(blank)

    # Concatenate images into grid
    grid_rows = []
    for r in range(rows):
        row_images = processed_images[r * cols:(r + 1) * cols]
        grid_rows.append(cv2.hconcat(row_images))

    grid = cv2.vconcat(grid_rows)

    # Show result
    cv2.imshow(window_name, grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =========================
# Main Entry Point
# =========================
def main() -> None:
    """
    Main execution function.
    Loads images and displays them in a single grid window.
    """
    well_img = load_image(WELL_SRC)
    roi_gray = load_image(ROI_SRC, gray=True)
    roi_new = load_image(ROI_NEW_SRC)
    merged_img = load_image(MERGE_SRC)

    images = [
        well_img,
        roi_gray,
        roi_new,
        merged_img
    ]

    titles = [
        "Well Image",
        "Original ROI",
        "New ROI",
        "Merged Result"
    ]

    show_image_grid(
        images=images,
        titles=titles,
        grid_shape=(2, 2),
        window_name="All Images Overview",
        cell_size=(420, 300)
    )


if __name__ == "__main__":
    main()
