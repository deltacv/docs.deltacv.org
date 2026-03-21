# Creating and Running a VisionProcessor

We'll start off with a familiar example; the most simple processing that can be done in OpenCV is changing an image's color space to another one. The following VisionProcessor simply takes the input frame and changes its color space to grayscale:

<pre class="language-java"><code class="lang-java">import android.graphics.Canvas;

import org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration;
import org.firstinspires.ftc.vision.VisionProcessor;

import org.opencv.core.Mat;
<strong>import org.opencv.imgproc.Imgproc;
</strong><strong>
</strong><strong>public class GrayProcessor implements VisionProcessor {
</strong>
    @Override
    public void init(int width, int height, CameraCalibration calibration) {
        // Not useful in this case, but we do need to implement it either way
    }
    
    @Override
    public Object processFrame(Mat frame, long captureTimeNanos) {
        Imgproc.cvtColor(frame, frame, Imgproc.COLOR_RGB2GRAY);
        return null; // No context object
    }
    
    @Override
    public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext) {
        // Not useful either
    }
    
}
</code></pre>

The key difference from OpenCvPipeline is in the way we display the gray image - instead of returning a Mat, any change made to the `frame` object will be displayed on the screen accordingly. Although it is advisable to use `onDrawFrame` instead, this will serve well for our example purposes.

Note that we return _null_ from `processFrame`, which means that the `userContext` in `onDrawFrame`will have that corresponding value. Anything returned from `processFrame`will be respectively passed into `onDrawFrame` as `userContext`.

## Adding processors to EOCV-Sim

There are two ways for adding your own processors:

* [Workspaces](../../workspaces/what-are-workspaces.md), which are the fastest and most flexible method of using the sim, since the code is built on-the-fly and changes are applied immediately.
* [Building from source](../../other/building-from-source.md), which allows the use of other JVM languages such as Kotlin, but it is slower since you have to recompile and wait for the sim to open every time you make changes in your code.

Workspaces are the recommended method for development if you use Java. You can use any IDE or text editor for them.

## Executing a processor

Once you have added a processor using any of the methods mentioned before, executing it is very simple. Your processor should appear in the "Pipelines" list once it's part of a workspace or added to EOCV-Sim's source code:

![We will select the GrayProcessor we made earlier](<../../assets/image (5) (1).png>)

You can simply select the processor in this list, and it will begin execution right away.

![GrayProcessor running live in EOCV-Sim](<../../assets/image (3) (1).png>)

