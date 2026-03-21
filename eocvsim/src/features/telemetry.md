# Telemetry

It's sometimes useful to log data from your vision code to know the result in real time. To do this, we partially implement the basic Telemetry interface that is present in the FTC SDK (e.g methods like `Telemetry#talk`are not implemented) to follow the main idea of EOCV-Sim of "easily copy-pasting into an FTC SDK project".

### Telemetry in VisionProcessor

To use telemetry in a proccessor, you need to have a constructor which takes a Telemetry parameter, and save it into an instance variable within your code. This is demostrated in the following snippet:

```java
import android.graphics.Canvas;

import org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration;
import org.firstinspires.ftc.vision.VisionProcessor;

import org.opencv.core.Mat;
import org.opencv.imgproc.Imgproc;

import org.firstinspires.ftc.robotcore.external.Telemetry;

public class TelemetryProcessor implements VisionProcessor {

    Telemetry telemetry;

    public TelemetryProcessor(Telemetry telemetry) {
        this.telemetry = telemetry;
    }
    
    @Override
    public void init(int width, int height, CameraCalibration calibration) {
        // Not useful in this case, but we do need to implement it either way
    }

    @Override
    public Object processFrame(Mat input) {
        telemetry.addData("[Hello]", "World!");
        telemetry.update();
        
        return null; // No need for a context object
    }
    
    @Override
    public void onDrawFrame(Canvas canvas, int onscreenWidth, int onscreenHeight, float scaleBmpPxToCanvasPx, float scaleCanvasDensity, Object userContext) {
        // Not useful either
    }

}
```

![The telemetry output from the code above](../assets/eocvsim\_usage\_telemetry.png)

The basic idea of telemetry is to send data using the `Telemetry#addData` or `Telemetry#addLine` methods. Once you finish adding data, you call `Telemetry#update` in the end, to display the data and clear the past state of the telemetry so the messages that were sent in a previous call to update will not be displayed.

### Telemetry in OpenCvPipeline

We'll replicate the example from earlier as an OpenCvPipeline. The core concept remains the same, but the code structure changes a little from using a different interface;

```java
import org.opencv.core.Mat;
import org.openftc.easyopencv.OpenCvPipeline;

import org.firstinspires.ftc.robotcore.external.Telemetry;

public class TelemetryPipeline extends OpenCvPipeline {

    Telemetry telemetry;

    public TelemetryPipeline(Telemetry telemetry) {
        this.telemetry = telemetry;
    }

    @Override
    public Mat processFrame(Mat input) {
        telemetry.addData("[Hello]", "World!");
        telemetry.update();
        return input; // Return the input mat
    }

}
```
