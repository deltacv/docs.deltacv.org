# Crosshair

The **Crosshair Node** (found in the Classification & Filtering category) is a powerful, multi-purpose tool that brings together visualization and target selection in one block.

It is designed to take the stream of filtered objects (Contours) from your detection pipeline and **classify** them based on their relationship to a central, adjustable $$+$$ crosshair drawn on the image.

The node's dual function allows you to:

1. **Visually Align** your robot or camera using the drawn crosshair as a focal point.
2. **Filter Targets** to instantly select the object(s) nearest to, or surrounding, that crosshair.

This allows your code to easily identify and lock onto the intended target from a cluttered list of detected objects.

### Inputs and Parameters

The Crosshair node requires the following inputs to function:

| Pin Name         | Description                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Overlay Input    | The image stream (usually the original camera feed) onto which the crosshair will be drawn.                                                                                                      |
| Contours         | The list of detected objects (e.g., from a contour finder or filter) that you want to filter or select from.                                                                                     |
| Scale            | An integer that controls the size (length) of the crosshair lines. This value is automatically scaled relative to the image size to ensure visibility.                                           |
| Crosshair Offset | A vector ($$\Delta x, \Delta y$$) used to shift the crosshair away from the exact center of the image. This is useful for camera calibrations or if your target isn't centrally located.         |
| Crosshair Line   | Defines the style of the crosshair. You can connect an external Line Parameters Node or use the internal editor to set the color and thickness. If unlinked, the color defaults to bright green. |

### Selection Modes (Classification)

The core function of this node is to classify and filter your objects based on the crosshair's position. This logic is controlled by the Detection Mode setting:

#### 1. Mode: Inside

In Inside mode, the node acts as a containment filter.

* **Logic**: It checks every object to see if its Bounding Rectangle fully contains the crosshair's center point.
* Result: The output list (`Crosshair` pin) will contain **all the objects** whose bounding boxes overlap or enclose the crosshair.

#### 2. Mode: Nearest

In Nearest mode, the node acts as a single-target selector.

* **Logic**: It calculates the distance between the crosshair's center point and the center of every object.
* **Result**: The output list (`Crosshair` pin) will contain only the **single object** that is closest to the crosshair.

### Crosshair in Action

![Crosshair with the "Into the Deep" Samples](<../assets/crosshair .gif>)

