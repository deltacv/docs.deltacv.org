# Thresholding

Thresholding is one of the most fundamental and essential techniques in computer vision. In simple terms, it's the process of converting a color image into a purely binary image—meaning every pixel is either black or white.

#### What is a Threshold?

The "threshold" is a specific brightness value (a number) that acts as the cutoff point.

* Pixels Brighter than the threshold value are turned white (255).
* Pixels Darker than the threshold value are turned black (0).

![Example of a binary image](<../assets/image (1) (1).png>)

This action dramatically simplifies an image, eliminating gray areas and leaving only the strongest contrasts.

#### Why Do We Use It?

The primary purpose of thresholding is to isolate objects of interest from the background. By turning the image into a clear binary mask, we make it much easier for the computer vision algorithms to perform the next steps, such as:

1. Detection: Identifying the precise shape and location of an object.
2. Counting: Determining how many distinct objects are present.
3. Measurement: Calculating the area or dimensions of the detected object.

For example, if you are looking for a bright white tennis ball against a dark green court, setting the threshold correctly will instantly make the entire background black and the entire ball white, simplifying the rest of your pipeline.

#### Thresholding in PaperVision

In PaperVision, you use the Color Threshold node (found in the Image Processing category) to apply this technique. This node gives you powerful control:

* Color Space: You can choose to apply the threshold to different color models like RGB or HSV. The HSV color space is often preferred for thresholding because it separates the color information (Hue and Saturation) from the brightness (Value), allowing you to filter by specific colors or light levels more effectively.
* Channels: Unlike a simple grayscale threshold, the node allows you to set independent low and high threshold limits for each color channel (e.g., the Red channel, the Hue channel, etc.). This lets you target a very specific range of colors and brightness simultaneously.

> [!NOTE]
> To gain a grasp of the different color space types, including advantages and disadvantages, **we recommend to go through** [**LearnOpenCV's guide on the topic**](https://learnopencv.com/color-spaces-in-opencv-cpp-python/)

By fine-tuning these ranges, you create a precise binary mask that highlights only the parts of the image you want the rest of your pipeline to analyze.

***
