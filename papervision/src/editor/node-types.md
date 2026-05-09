# Node Types

Every node in **PaperVision** is a specialized tool designed for a specific stage of computer vision. To build an effective pipeline, it's important to understand not just what nodes do, but how they communicate through the data type system.

## Node Categories

Nodes are organized into categories. This classification helps you quickly locate the tools you need for each stage of your processing.

| Category Name              | Purpose                                                                                     | Examples                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Pipeline Flow**          | Structural nodes that handle external data entry and exit points.                           | Pipeline Input, Pipeline Output, Export Data.                                     |
| **Image Processing**       | Fundamental algorithms for modifying, filtering, and enhancing images.                      | Color Threshold, Blur, Grayscale, Bitwise Mask.                                   |
| **Feature Detection**      | Analyzing processed images to extract mathematical shapes or points.                        | Find Contours, Bounding Rect, Blob Detection.                                     |
| **Classification**         | Refining and filtering detected features based on logical criteria.                         | Filter Contours (by area/ratio), Sort Objects.                                    |
| **Drawing & Overlay**      | Rendering feedback onto the image for debugging and visualization.                          | Draw Contours, Draw Rectangles, Text Overlay.                                     |

## The Data Type System

PaperVision uses a **strongly-typed** system to ensure your pipeline is logically sound. You can only connect pins that share the same data type. Each pin features a distinct **icon** that represents the data it carries:

*   **Image**: Represented by a picture frame icon. This is the core stream of visual data used by most processing nodes.
*   **Number**: Represented by a numeric or hash icon. Used for parameters like coordinates, area, or threshold levels.
*   **Boolean**: Represented by a toggle or checkbox icon. Used for simple True/False values or conditional logic.
*   **List / Geometry**: Represented by a points or grouping icon. Used for complex data like groups of points, contours, or detected shapes.

> [!TIP]
> The editor strictly enforces compatibility. If you cannot create a link between two pins, it is likely because their data types (and icons) do not match.

## Anatomy of a Node

While the "Basics" guide explains how to link nodes, most nodes also feature **Inline Controls** located directly on the node body.

1.  **Title Bar**: Displays the node's name and category designation.
2.  **Input Pins (Left)**: Ports for receiving data from upstream nodes.
3.  **Property Fields**: Interactive UI elements (sliders, text boxes, or dropdowns) for adjusting parameters without needing external nodes.
4.  **Output Pins (Right)**: Ports for sending processed data to downstream nodes.
5.  **Pre-visualization (Eye)**: A toggle button available on most image output pins to quickly view the result of that specific node in the preview window.

### Pin Promotion
Many nodes allow you to choose between using an **Inline Control** or an **Input Pin**. For example, a Color Threshold node has sliders for R, G, and B. If you need to change these values dynamically based on another part of your algorithm, you can "link" them to external numeric outputs, which overrides the manual slider values.

