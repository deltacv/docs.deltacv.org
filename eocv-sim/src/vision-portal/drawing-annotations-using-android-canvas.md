# Drawing annotations using Android Canvas

### onDrawFrame() basics

Java classes implementing the VisionProcessor interface inherit 3 very useful methods; we have extensively covered the uses of `init`and `processFrame` earlier in this documentation.&#x20;

However there's still one more method we haven't explained, yet it holds great usefulness as well:

```java
@Override
public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext)
```

`onDrawFrame()` comes in handy for better visualization of your vision processing algorithm, although with a steep learning curve, since it introduces a new way to draw shapes and colors on top of our image processing results, which is often really useful to indicate the results of our pipelines, such as highlighting which elements are currently being detected, draw a multicolored 3d cube on top of signaled AprilTags, annotate text to describe detected objects, etcetera.

Since this drawing step is executed in another _Thread_ (which means that it runs in parallel, at different pace than the rest of your vision processing), and is oftenly GPU accelerated to produce high quality rendering, it is needed to introduce this functionality as part of a separate method (step).

### Android Canvas object

In Android, the Canvas object acts as a virtual drawing surface. You can use it to create a graphical context for drawing shapes, images, color, and text on the screen. The `Canvas` is, well, your _canvas_, and you can paint on it to visually enrich your VisionProcessor. EOCV-Sim is prepared to handle most Android Canvas use-cases and appropiately mocks this interface to use it in your desktop OS just as you would in an Android device within the FTC SDK.

1. **Canvas Drawing Methods:** The Canvas provides various drawing methods to create different types of graphical elements. Some common methods include `drawRect()`, `drawCircle()`, `drawLine()`, `drawText()`, and many more. These methods allow you to draw shapes and text on the Canvas.
2. **Coordinate System:** The Canvas uses a 2D Cartesian coordinate system, with the origin (0,0) at the top-left corner of the Canvas. Positive X values extend to the right, and positive Y values extend downward.
3. **Color and Style:** You can set various attributes for your drawings using the Paint object. This includes attributes like stroke color, fill color, stroke width, and text size. You configure the Paint object and then use it in conjunction with Canvas drawing methods.

<pre class="language-java"><code class="lang-java">// Create a Paint object to set drawing attributes
Paint paint = new Paint();
paint.setColor(Color.RED); // Set the color to red

<strong>// Draw a red rectangle on the Canvas
</strong>canvas.drawRect(50, 50, 200, 200, paint);
</code></pre>

### Understanding the Paint object

The Android Paint object is used to define how graphical elements are drawn on the Canvas. It allows you to set multiple attributes such as color, style, stroke width, text size, and more. Understanding how to configure the Paint object is key for creating the desired visual effects when working with the Canvas. You can think of the `Paint` object as the combination of your _bucket_ containing paint of a defined color, and its _brush with a_ specific _size_ and _style_, which you will later use to draw shapes using the methods of a _Canvas._

1. **Color:** The Paint object can set the color of lines, shapes, and text. You can use the `setColor()` method to specify the desired color. For example, `paint.setColor(Color.RED)` sets the paint color to red.
2. **Style:** Paint can determine the style for drawing shapes and lines, such as `FILL` for filled shapes, `STROKE` for outlines, and `FILL_AND_STROKE` for both. Use `setStyle()` to configure the style.
3. **Stroke Width:** You can specify the width of the stroke when drawing lines and shapes using the `setStrokeWidth()` method.
4. **Text Size:** When drawing text, you can control the text size with `setTextSize()`. This is especially useful when annotating images or creating custom text labels.
5. **Typeface:** The Paint object also allows you to set the typeface for text using `setTypeface()`, which can be used to customize the font style.

```java
Paint paint = new Paint();
paint.setColor(Color.BLUE); // Set the color to blue
paint.setStyle(Paint.Style.FILL); // Fill the shape
```

Most of the methods from `Canvas` take a `Paint` object as an argument, which gives an easy way to draw multiple shapes and lines with the same color and parameters.

```java
// Draw a blue filled circle on the Canvas
canvas.drawCircle(150, 150, 100, paint);
```

### Handling context objects in a VisionProcessor

In the context of a VisionProcessor, handling a _context object_ is a fundamental practice that involves managing and passing additional information and state data between `processFrame` and `onDrawFrame`. This mechanism is essential for efficient coordination and communication between these two components.&#x20;

Let's review a few key concepts to make sure we're on track:

1. **VisionProcessor Interface**: Defines methods for initializing, processing frames, and rendering visual data.
2. **Initialization**: The `init` method sets up the processor with frame dimensions and calibration data.
3. **Processing Step**: In `processFrame`, analyze frames, perform object detection, and store results in the context object.
4. **Context Object**: Stores and passes information between `processFrame` and `onDrawFrame` methods.
5. **Context Object as UserContext**: The context object from `processFrame` is returned as `userContext` for `onDrawFrame`.
6. **Rendering Step**: `onDrawFrame` uses `userContext` to render visual annotations on the canvas.
7. **Data Flow**: Context objects enable efficient data flow from processing to rendering.

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

For the purposes of this example, we won't write the implementation details of `detectRects`, but this should give a barebones demonstration of how the `userContext` works.

Note how we pass a context object from processFrame, by returning it through this method;

```java
// Process the frame, detect shapes, and store them in the context object
List<Rect> detectedRects = detectRects(frame);

// Return the context object as userContext
return detectedShapes;
```

Now let's see how we handle this userContext in `onDrawFrame`, where we need to perform [type casting](https://www.w3schools.com/java/java\_type\_casting.asp) to ensure we are actually getting the expected object that was created in `processFrame`:

```java
(List<Rect>) userContext
```

### OpenCV to Android Canvas Position transformations

Due to the differences in size and aspect ratio between the Android _Canvas_ and the image coming from _OpenCV_, we do need to perform a few simple transformations to display our shapes in the adequate positions. For example, we can implement a utility method that converts an OpenCV rectangle into _Canvas_ positions:

```java
private android.graphics.Rect makeGraphicsRect(Rect rect, float scaleBmpPxToCanvasPx) {
     int left = Math.round(rect.x * scaleBmpPxToCanvasPx);
     int top = Math.round(rect.y * scaleBmpPxToCanvasPx);
     int right = left + Math.round(rect.width * scaleBmpPxToCanvasPx);
     int bottom = top + Math.round(rect.height * scaleBmpPxToCanvasPx);
     
     return new android.graphics.Rect(left, top, right, bottom);
}
```

Note that the parameter `scaleBmpPxToCanvasPx` is a pretty useful scale factor that easily allows you to correctly place shapes on the Android Canvas, it is calculated under the hood and provided to your code through the onDrawFrame method; take the following code as an example of how to use this utility

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
