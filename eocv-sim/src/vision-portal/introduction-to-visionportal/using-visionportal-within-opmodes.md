# Using VisionPortal within OpModes

We'll start with a pretty basic example that uses VisionPortal to run the the bundled AprilTagProcessor and explain line by line:

<pre class="language-java"><code class="lang-java">import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.vision.VisionPortal;
import org.firstinspires.ftc.vision.apriltag.AprilTagDetection;
import org.firstinspires.ftc.vision.apriltag.AprilTagProcessor;

<strong>@Autonomous(name = "Example VisionPortal OpMode")
</strong>public class ExampleVisionPortalOpMode extends LinearOpMode {

    /**
     * The variable to store our instance of the AprilTag processor.
     */
    private AprilTagProcessor aprilTag;

    /**
     * The variable to store our instance of the vision portal.
     */
    private VisionPortal visionPortal;

    @Override
    public void runOpMode() {
        visionPortal = VisionPortal.easyCreateWithDefaults(
                    hardwareMap.get(WebcamName.class, "Webcam 1"), aprilTag);

        telemetry.addData(">", "Touch Play to start OpMode");
        telemetry.update();

        // Wait for the DS start button to be touched.``
        waitForStart();

        if (opModeIsActive()) {
            // ...
        }

        // Save more CPU resources when camera is no longer needed.
        visionPortal.close();
    }
}

</code></pre>

***

```java
@Autonomous(name = "Example VisionPortal OpMode")
public class ExampleVisionPortalOpMode extends LinearOpMode {
```

Declares our LinearOpMode and annotates it as an autonomous program. LinearOpMode is often more useful when coding autonomous routines due to its inherent structure.

***

```java
    /**
     * The variable to store our instance of the AprilTag processor.
     */
    private AprilTagProcessor aprilTag;

    /**
     * The variable to store our instance of the vision portal.
     */
    private VisionPortal visionPortal;
```

Some convenience variables that will let us store our VisionProcessor and VisionPortal instances that we will be using later on.

***

```java
    @Override
    public void runOpMode() {
```

Inherits the method from LinearOpMode that will be executed when the OpMode is initialized. Any code put in here will be executed as a result.

***

```java
        // Create the AprilTag processor the easy way.
        aprilTag = AprilTagProcessor.easyCreateWithDefaults();
        
        // Create the vision portal the easy way.
        visionPortal = VisionPortal.easyCreateWithDefaults(
                hardwareMap.get(WebcamName.class, "Webcam 1"), aprilTag);
```

This is the key part of our image processing initialization; we'll create our AprilTagProcessor and VisionPortal instances by using `easyCreateWithDefaults()`methods, which allows us to effortlessly initialize things by only passing a few parameters.&#x20;

We'll make a special emphasis on this part;

```java
hardwareMap.get(WebcamName.class, "Webcam 1")
```

This line basically defines what will be the source of our images that are passed onto the attached `VisionProcessor`s, usually a webcam for that matter. "Webcam 1" indicates the _robot configuration name_ of the image capture device we wish to use, as it is commonly the default name automatically assigned by the FTC SDK.

In the case of EOCV-Sim, fortunately we have quite some other options here in order to provide more flexibility when it comes to testing your vision code;

## Using other input sources in your OpModes

<table><thead><tr><th>Type</th><th>WebcamName</th><th data-hidden>WebcamName</th><th data-hidden></th></tr></thead><tbody><tr><td>USB Camera</td><td><ul><li>"Webcam 1" refers to the first USB camera detected by your operating system</li><li>In order to use other cameras, you will need to enter their index number. "0" is the same as "Webcam 1", but you can specify any number that ranges from 0 to (n-1), where n is the number of USB cameras currently plugged.</li></ul></td><td><ul><li>"Webcam 1" automatically refers to the first USB camera detected by your operating system.</li><li>Using other webcams is as simple as specifying their number; "0" is the same as "Webcam 1"</li></ul></td><td></td></tr><tr><td>Image</td><td><ul><li>Images are specified by providing their absolute path as a WebcamName, the simulator automatically determines if it's an image by the file's extension.</li><li>Examples: "C:\Users\pepito\Pictures\OnePixel.png"</li><li>"/Users/PepitoRico/Downloads/OnePixel.png"</li></ul></td><td></td><td></td></tr><tr><td>Video</td><td><ul><li>Videos are pretty much the same as images, as they are specified by providing their absolute path as a WebcamName, the simulator automatically determines if it's an video by the file's extension. Note that mp4 is most likely not supported due to licensing issues.</li><li>Examples: "C:\Users\pepito\Pictures\10PixelsVideo.avi"</li></ul><ul><li>"/Users/PepitoRico/Downloads/10PixelsVideo.mkv"</li></ul></td><td></td><td></td></tr></tbody></table>

## WebcamName code examples

### USB Cameras

```java
hardwareMap.get(WebcamName.class, "Webcam 1");

hardwareMap.get(WebcamName.class, "0"); // Same as "Webcam 1"
hardwareMap.get(WebcamName.class, "1"); // Other webcam
hardwareMap.get(WebcamName.class, "2"); // Other webcam
```

### Images

```java
hardwareMap.get(WebcamName.class, "C:\Users\pepito\Pictures\OnePixel.png");
```

### Videos

```java
hardwareMap.get(WebcamName.class, "/Users/PepitoRico/Downloads/10PixelsVideo.avi");
```
