# Target Exporting

The Target Exporting step is the last piece of the computer vision pipeline. This is where you package the final, filtered data—the precise location and dimensions of your detected objects—and give it a name so your external program (your robot code) can easily access and use it.

Exporting is done using nodes from the Classification & Filtering category.

![](<../assets/image (19).png>)

### The Exporting Process

After you have used nodes like Bounding Rectangles and Crosshair to find and select your targets, you must use an export node to finalize the data.

1. **Input Targets**: Connect the output list of targets (e.g., the `Rotated Rectangles` from a Bounding Node or the `Crosshair` output) to the export node's Targets pin.
2. **Assign a Label**: Enter a descriptive Label (e.g., `goal_targets`, `shipping_hub`) directly into the node. This label is the name that your robot code will use to retrieve the data.

> [!NOTE]
> You can use multiple export nodes to package different sets of data (e.g., one for Axis-Aligned Rectangles and another for Rotated Rectangles), giving each set a unique label.

### How to Get the Data

Your robot code will interact with the pipeline object to retrieve the targets. The generated methods are designed to handle both single-target and multi-target scenarios:

#### 1. Retrieving a Single Target

The generated code often exports targets with indexed names internally (e.g., `"rects_0"`, `"rects_1"`). There's a method that can retrieve a single target when it might be needed:

<pre class="language-java"><code class="lang-java"><strong>Rect singleTarget = pipeline.getRectTarget("front_box");
</strong></code></pre>

Rotated Rectangles are stored in a separate list:

```java
RotatedRect nearestTarget = pipeline.getRotRectTarget("nearest_target");
```

#### 2. Retrieving All Targets with the Same Label

If your pipeline detects multiple objects and exports them all under the label `"rects"`, you'll use the plural getter:

```java
// Retrieves the full list of Rectangles exported under the label "boxes"
List<Rect> allBoxes = pipeline.getRectTargets("boxes");

// A loop is used to process each detected rectangle
for (Rect box : allBoxes) {
    // Example use: calculate the center X of each box
    int centerX = box.x + (box.width / 2);
    telemetry.addData("Center X", centerX);
}
```

Rotated Rectangles are stored in a separate list:

```java
// Retrieves the list of all Rotated Rectangles (useful for angled targets)
List<RotatedRect> allTiltedTargets = pipeline.getRotRectTargets("rings");

// A loop is used to process the angle of each target
for (RotatedRect ring : allTiltedTargets) {
    // Example use: the angle is essential for alignment
    double angle = ring.angle;
    telemetry.addData("Target Angle", angle);
}
```
