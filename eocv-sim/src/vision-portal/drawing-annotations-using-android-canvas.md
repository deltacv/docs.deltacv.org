# Drawing annotations using Android Canvas

### onDrawFrame() basics

Java classes implementing the VisionProcessor interface inherit 3 methods: `init`, `processFrame`, and one more that hasn't been covered yet:

```java
@Override
public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext)
```

`onDrawFrame()` lets you draw shapes, text, and colors on top of your image processing results — useful for highlighting detected elements, annotating text, drawing 3D overlays on AprilTags, and so on. Because this drawing step runs on a separate thread (in parallel with your vision processing) and is often GPU-accelerated, it lives in its own method rather than inside `processFrame`.

### Android Canvas object

In Android, the `Canvas` object acts as a virtual drawing surface. You can use it to draw shapes, images, and text on screen. EOCV-Sim mocks this interface so it works on desktop the same way it would inside the FTC SDK on an Android device.

A few things worth knowing about the Canvas:

1. **Drawing methods:** `drawRect()`, `drawCircle()`, `drawLine()`, `drawText()`, and many more.
2. **Coordinate system:** Origin `(0, 0)` is at the top-left corner. Positive X goes right, positive Y goes down.
3. **Color and style:** Controlled through the `Paint` object, which you pass into drawing methods.

```java
// Create a Paint object to set drawing attributes
Paint paint = new Paint();
paint.setColor(Color.RED); // Set the color to red

// Draw a red rectangle on the Canvas
canvas.drawRect(50, 50, 200, 200, paint);
```

### Understanding the Paint object

Think of the `Paint` object as a combination of a paint bucket (defining the color) and a brush (defining the size and style). You configure it once and pass it to Canvas drawing methods.

The most commonly used attributes:

1. **Color:** `setColor()` — e.g. `paint.setColor(Color.RED)`
2. **Style:** `setStyle()` — `FILL`, `STROKE`, or `FILL_AND_STROKE`
3. **Stroke width:** `setStrokeWidth()` — controls line thickness
4. **Text size:** `setTextSize()` — for text annotations and labels
5. **Typeface:** `setTypeface()` — for custom font styles

```java
Paint paint = new Paint();
paint.setColor(Color.BLUE);
paint.setStyle(Paint.Style.FILL);
```

Most Canvas methods take a `Paint` as their last argument, so you can reuse the same object across multiple draw calls to keep consistent styling.

```java
// Draw a blue filled circle on the Canvas
canvas.drawCircle(150, 150, 100, paint);
```

### Handling context objects in a VisionProcessor

The `userContext` parameter in `onDrawFrame` is the key to coordinating between your processing and drawing steps. Whatever object you return from `processFrame` is passed in as `userContext` in the next `onDrawFrame` call — this is how you transfer detection results (like a list of rectangles) from one step to the other without shared mutable state.

```java
public class SimpleVisionProcessor implements VisionProcessor {
    @Override
    public void init(int width, int height, CameraCalibration calibration) {
        // Initialization code, if needed
    }

    @Override
    public Object processFrame(Mat frame, long captureTimeNanos) {
        // Process the frame, detect shapes, and store them in the context object
        List<Rect> detectedRects = detectRects(frame);
        
        // Return the context object as userContext
        return detectedShapes;
    }

    @Override
    public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext) {
        // Render detected shapes using the userContext (which is the context object)
        drawRects(canvas, (List<Rect>) userContext);
    }

    // TODO: Implement detectRects and drawRects...
}
```

Note the [type cast](https://www.w3schools.com/java/java\_type\_casting.asp) in `onDrawFrame` — since `userContext` is typed as `Object`, you need to cast it back to the expected type before using it.

### OpenCV to Android Canvas position transformations

The Canvas and the OpenCV image may differ in size and aspect ratio, so you need to scale coordinates before drawing. The `scaleBmpPxToCanvasPx` parameter provided to `onDrawFrame` handles this. Here's a utility method that converts an OpenCV `Rect` into Android Canvas coordinates:

```java
private android.graphics.Rect makeGraphicsRect(Rect rect, float scaleBmpPxToCanvasPx) {
     int left = Math.round(rect.x * scaleBmpPxToCanvasPx);
     int top = Math.round(rect.y * scaleBmpPxToCanvasPx);
     int right = left + Math.round(rect.width * scaleBmpPxToCanvasPx);
     int bottom = top + Math.round(rect.height * scaleBmpPxToCanvasPx);
     
     return new android.graphics.Rect(left, top, right, bottom);
}
```

And here's how you'd use it in `onDrawFrame`:

```java
@Override
public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext) {
    Rect rect = ...; // OpenCV rectangle
    
    Paint rectPaint = new Paint();
    rectPaint.setColor(Color.RED);
    rectPaint.setStyle(Paint.Style.STROKE);
    rectPaint.setStrokeWidth(scaleCanvasDensity * 4);

    canvas.drawRect(makeGraphicsRect(rect, scaleBmpPxToCanvasPx), rectPaint);
}
```

You can find the [full example code here](https://gist.github.com/serivesmejia/7185b078f2a2a21f41455b2acb80adee) and test it out on EOCV-Sim or even your own robot!
