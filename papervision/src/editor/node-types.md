# Node Types

The power of **PaperVision** lies in its organized and color-coded system for building computer vision pipelines. To help you quickly find the specific block of functionality you need, every node is assigned to a distinct **category**, visually identifiable by its **title bar color**. Understanding these categories will make building, debugging, and expanding your visual program much faster and more intuitive.

| Category Name              | Node Color | Purpose                                                                                     | Examples                                                                          |
| -------------------------- | ---------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Pipeline Flow              | Cyan       | Defines the structural beginning and end of your visual program.                            | Handling the camera input and outputting the final result.                        |
| Image Processing           | Orange     | The fundamental tools for modifying, enhancing, and preparing an image.                     | Applying a Threshold, Blur filter, or converting color spaces.                    |
| Feature Detection          | Indigo     | Analyzing the image to find objects, shapes, or points of interest.                         | Finding the biggest Contour, detecting Blobs, or identifying Bounding Rectangles. |
| Classification & Filtering | Yellow     | Organizing and refining detected objects based on specific criteria.                        | Filtering contours by area or aspect ratio, or exporting targets.                 |
| Drawing & Overlay          | Teal       | Drawing elements (like shapes or lines) back onto the image for visualization and feedback. | Drawing Contours or Rectangles onto the final output.                             |

### Understanding Node Pins and Data Flow

While nodes perform the work, the pins on their edges manage the flow of information. Understanding pin types is essential for building a valid pipeline:

* **Inputs (Left Side)**: These pins accept data from other nodes. A node may have multiple inputs for different types of data (e.g., one for the image, one for a number).
* **Outputs (Right Side)**: These pins release the result of the node's function.
* **Data Typing**: Every pin is _**strongly typed**_ and color-coded.&#x20;

> [!NOTE]
> The editor strictly enforces compatibility behind the scenes. An Image output pin, for instance, cannot be wired into a numeric expected input pin, even by accident.

If you attempt to draw a wire between two pins that carry incompatible data types, the connection will simply not be created. This automatic validation guarantees that your data flow is fundamentally sound, helping you prevent execution errors in your visual program.
