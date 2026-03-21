# Overlaying

Overlaying is the final step in a visual pipeline that takes the data you've found (like contours, rectangles, or key points) and draws it back onto the image. This process doesn't change the underlying image or the data you found; it simply creates a visual representation of your detection logic so you can see exactly what the computer is seeing.

The Overlay nodes are found in the Drawing & Overlay category (Teal colored) and are critical for debugging and providing clear feedback during robot operation.

### How Overlay Nodes Work

Overlay nodes have a very specific structure and flow:

1. **Input**: The main `Input` pin receives the image you want to draw _on_. This is typically your original, full-color camera stream.
2. **Parameters (What to Draw)**: You connect the specific data you want to visualize—such as the list of Rectangles found by a `BoundingRotatedRectsNode` or the Contours found by a contour finder.
3. **Drawing Parameters (How to Draw)**: You connect a Line Parameters Node to define the appearance of the drawing. This node specifies the color and thickness of the lines that will be drawn on the image.
4. **Output**: The node outputs the image with the overlay elements now drawn on top

| Node                    | Purpose                                                        | Data Required                |
| ----------------------- | -------------------------------------------------------------- | ---------------------------- |
| Draw Rectangles         | Draws axis-aligned bounding boxes around detected objects.     | List of `Rectangles`         |
| Draw Rotated Rectangles | Draws the snug-fitting, rotated boxes around detected objects. | List of `Rotated Rectangles` |
| Draw Contours           | Draws the precise, raw boundary lines of the detected shapes.  | List of `Contours`           |
| Draw Key Points         | Marks specific points found by feature detection algorithms.   | List of `Key Points`         |

![](<../assets/image (15).png>)

### Line Parameters Node

The Line Parameters Node is a utility node found in the Overlay category whose sole purpose is to define _how_ an overlay element should look when drawn onto the image.

Drawing nodes like `Draw Rectangles` or `Draw Contours` don't contain any styling information themselves. Instead, they require the output of a Line Parameters Node to fill their `Parameters` input pin.

> [!NOTE]
> You can easily create a "Line Parameters" node by clicking the pencil button that is available on any of the nodes that have such a parameter, instead of having to add it manually!

![](<../assets/line parameters.gif>)

This node gives you control over two key visual properties:

#### 1. Line Color

This defines the color of the drawing using standard RGB (Red, Green, Blue) values.

* You can set the $$R$$, $$G$$, and $$B$$ values on a scale from $$0$$ to $$255$$.
* For example, setting $$R=255$$, $$G=255$$, and $$B=0$$ will produce a bright Yellow line.

#### 2. Line Thickness

This defines how many pixels wide the drawn line will be.

* A thickness of $$1$$ results in a very thin line.
* Increasing the number (e.g., $$3$$ or $$5$$) will create a thicker, more visible outline.

> [!NOTE]
> Another advantage of using "Line Parameters" is being able to share a single instance among different overlay nodes

![](<../assets/image (14).png>)

### Default Line Color (Unlinked Parameters)

The Drawing Nodes (like `Draw Rectangles`) are designed for quick visual feedback. When you look at the Parameters pin, you'll see a pencil icon next to it, which you can click to automatically link a new Line Parameters node.

If you leave the Parameters pin unlinked to an external Line Parameters Node, the node uses its own default values. These are set to: $$Red=0$$, $$Blue=0$$, and $$Green=255$$.

