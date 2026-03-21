# Android Studio

If you want to use EOCV-Sim with `OpenCvPipeline`s that are already in Android Studio, that's easily possible using the workspaces feature.

To achieve this, you need to isolate your pipeline's source files into their own package. Since EOCV-Sim only implements a very small part of the FTC SDK, if you try to compile a class that references stuff like `DcMotor`, it will fail since those classes don't exist in EOCV-Sim.

The only classes from the FTC SDK and EasyOpenCV that have been implemented are...

| Package                                           | Classes                                                                                                  |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| org.firstinspires.ftc.robotcore.external          | <p>Telemetry (partially)</p><p>Func</p>                                                                  |
| org.firstinspires.ftc.robotcore.external.function | Consumer                                                                                                 |
| org.firstinspires.ftc.vision                      | \* (everything)                                                                                          |
| com.qualcomm.robotcore.eventloop.opmode           | <p>OpMode<br>LinearOpMode</p>                                                                            |
| com.qualcomm.robotcore.util                       | <p>ElapsedTime</p><p>MovingStatistics</p><p>Range</p><p>Statistics</p>                                   |
| org.openftc.easyopencv                            | <p>OpenCvPipeline</p><p>OpenCvTracker</p><p>OpenCvTrackerApiPipeline</p><p>TimestampedOpenCvPipeline</p> |
| org.opencv                                        | \* (everything)                                                                                          |

This also means that, outside of `OpMode`s, you **do not need to use the`OpenCvCamera`related stuff in EOCV-Sim**, inputs are simulated using [Input Sources](../features/input-sources.md).

For example, you can have the following package structure in your Android Studio project to isolate `OpenCvPipeline`s and load them into EOCV-Sim:

![](../assets/eocv-sim-folder-structure.png)

The `VisionTestOpMode`class can freely use any of the FTC SDK or EasyOpenCV classes, while the classes under the `vision`package should only use the ones specified in the table before, including the whole OpenCV library of course.

Now, you will select the `vision` package as a workspace in EOCV-Sim. To select a workspace you can go to `Workspace -> Select workspace`, like in the gif shown below (both options showcased do the same thing):

![](../assets/eocvsim_usage_workspace_select.gif)

To find the vision folder in the project, first locate the root folder of your FTC SDK project in the file selector, something that looks like this:

![](../assets/root-sdk-folder.png)

Then, navigate through the folders`TeamCode/src/main/java/org/firstinspires/ftc/teamcode` and you will find the following:

![](../assets/select-vision-package.png)

Select the `vision` folder and click on "Open". The pipelines inside will be compiled in a few instants, and you will have them on the pipeline selector once it finishes successfully:

![The pipelines that are in the vision package, in the first screenshot of this page](../assets/selected-vision-package.png)

And now you are done! You will now be able to modify your pipelines from Android Studio and see the changes live. Refer to [the features section](../features/input-sources.md) to learn more about the additional features of EOCV-Sim
