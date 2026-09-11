# Introduction to VisionPortal

New for the 2023-2024 season is the **VisionPortal** interface. A new technology that implements **OpenCV** vision right into the **FTC SDK**, making computer vision more accessible and easier to code for _FIRST Tech Challenge_ than ever before. Creating a camera stream with VisionPortal is as easy as writting just a few, concise lines of code;

```java
VisionPortal myVisionPortal;

// Create a VisionPortal, with the specified camera, and assign it to a variable.
myVisionPortal = VisionPortal.easyCreateWithDefaults(hardwareMap.get(WebcamName.class, "Webcam 1"), ...);
```

Going into more technical details, VisionPortal is a thin API built on top of **EasyOpenCV**. So, not only is it easier to use, but it also takes advantage of the proven reliability of EasyOpenCV, used by hundreds (or even thousands!) of teams ever since 2019.

We won't go further in depth on the functionality of VisionPortal for the purposes of this documentation, but it's highly advised check out [ftc-docs](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision\_portal/visionportal\_overview/visionportal-overview.html) for more information about the usage of this API.

### VisionProcessor

The **VisionProcessor** interface was introduced along VisionPortal to mimic the usage of OpenCvPipeline to this new API. If we take a look into the interface, we can notice it is pretty similar in concept:

```java
import android.graphics.Canvas;

import org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration;
import org.firstinspires.ftc.vision.VisionProcessor;

import org.opencv.core.Mat;

public class SampleProcessor implements VisionProcessor {

    @Override
    public void init(int width, int height, CameraCalibration calibration) {
        // Code executed on the first frame dispatched into this VisionProcessor
    }
    
    @Override
    public Object processFrame(Mat frame, long captureTimeNanos) {
        // Actual computer vision magic will happen here
    }
    
    @Override
    public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext) {
        // Cool feature: This method is used for drawing annotations onto
        // the displayed image, e.g outlining and indicating which objects
        // are being detected on the screen, using a GPU and high quality 
        // graphics Canvas which allow for crisp quality shapes.
    }
    
}
```

We can attach this processor into a VisionPortal to start dispatching camera frames into our custom computer vision algorithms;

```java
VisionPortal myVisionPortal;
SampleProcessor sampleProcessor = new SampleProcessor();

// Create a VisionPortal, with the specified camera and the 
// SampleProcessor we created earlier, and assign it to a variable.
myVisionPortal = VisionPortal.easyCreateWithDefaults(hardwareMap.get(WebcamName.class, "Webcam 1"), sampleProcessor);
```
