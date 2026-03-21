# Countours and Filtering

After you have used Thresholding and Masking to isolate your object of interest, the next logical step is to mathematically define its shape using Contours. This process allows the computer to understand the object's boundaries, which is essential for accurate measurement and location.

### What is a Contour?

A Contour is simply a curve joining all the continuous points along the boundary of a shape that have the same color or intensity.

Once an object's boundary is defined as a contour, you can use that list of coordinates to perform various operations, like calculating area, finding the center, or drawing a bounding box.

### 1. Image Preparation (Creating the Binary Mask)

Contour detection works best, and often exclusively, on a **binary image** (_a black-and-white image where pixels are either 0 or 255_). This step ensures the algorithm only sees two things: **the object** and the **background**.

You first use a process like "[Thresholding](thresholding.md)" to convert your original image (which may be color, or grayscale) into a binary mask. This isolates the area of interest (which should be white) from the background (which should be black).

![](<../assets/image (2) (1).png>)

### 2. Contour Detection

Once the image is a clean binary mask, the contour-finding algorithm can be applied.

The algorithm systematically scans the image, looking for a transition from a black pixel (background) to a white pixel (object). When it finds this transition, it begins to "trace" the continuous line of white pixels around the shape until it returns to the starting point.

The output of this process is not an image; it is a mathematical list of (x, y) coordinates for every point along the boundary of the detected shape.

![](<../assets/image (3) (1).png>)

### 3. Post-Detection (Filtering and Analysis)

After detection, the list of contours is passed to the rest of your pipeline. Since the detection process often finds many small, noisy, or irrelevant shapes, the next steps involve turning the raw contours into actionable data:

* **Filtering**: You apply Filtering to eliminate unwanted contours based on criteria like area (to remove noise), aspect ratio (to identify specific shapes), or the number of vertices.
* **Analysis**: The remaining, filtered contours are then used for analysis, such as calculating the object's area, finding its centroid (center point), or drawing a simple Bounding Box or Bounding Rotated Rectangle around it.

![](<../assets/image (4) (1).png>)

### 4. Final Result

![](<../assets/image (5) (1).png>)

> [!NOTE]
> We will learn how to draw shape outlines, such as this example, in the "[Overlaying](overlaying.md)" chapter.
