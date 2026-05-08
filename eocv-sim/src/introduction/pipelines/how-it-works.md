# Creating and Running a Pipeline

## Lifecycle

`OpenCvPipeline`s are the main executable unit in EOCV-Sim, and they can be created [as explained here](./). The lifecycle is automatically managed by the sim, which calls:

* `init` before the first `processFrame`
* `processFrame` every time a new frame is dispatched from an [Input Source](../../features/input-sources.md)
* `onViewportTapped` when the image displayed on the UI is clicked with the mouse (or tapped if running the pipeline on a phone)

```java
import org.opencv.core.Mat;
import org.openftc.easyopencv.OpenCvPipeline;

public class SamplePipeline extends OpenCvPipeline {

    @Override
    public void init(Mat input) {
        // Executed before the first call to processFrame
    }

    @Override
    public Mat processFrame(Mat input) {
        // Executed every time a new frame is dispatched

        return input; // Return the image that will be displayed in the viewport
                      // (In this case the input mat directly)
    }

    @Override
    public void onViewportTapped() {
        // Executed when the image display is clicked by the mouse or tapped
        // This method is executed from the UI thread, so be careful to not
        // perform any sort heavy processing here! Your app might hang otherwise
    }

}
```

You can learn more about pipelines in [their dedicated section](./).

## Adding pipelines to EOCV-Sim

There are two ways to add your own pipelines:

* [Workspaces](../../workspaces/what-are-workspaces.md), which are the fastest and most flexible option — pipelines are built on-the-fly and changes are applied immediately.
* [Building from source](../../other/building-from-source.md), which allows the use of other JVM languages such as Kotlin, but is slower since you have to rebuild and reopen the sim every time you make changes to your pipelines.

Workspaces are the recommended method for development if you use Java. You can use any IDE or text editor for them. We officially support [Android Studio](../../workspaces/android-studio.md) (partially), [VS Code, and IntelliJ IDEA](../../workspaces/vscode-and-intellij.md).

## Executing a pipeline

Once you've added a pipeline using either of the methods above, running it is straightforward. Your pipeline should appear in the "Pipelines" list on the right side of the UI:

![In this case we will use the SamplePipeline shown before](<../../assets/image (1) (2).png>)

Click on a pipeline to select it, and [the lifecycle described above](how-it-works.md#lifecycle) will start running in your code.

The gears icon on SamplePipeline indicates it was added via the [Workspaces](../../workspaces/what-are-workspaces.md) method. The hammer and wrench icon on DefaultPipeline indicates it was added via [Build from Source](../../other/building-from-source.md).
