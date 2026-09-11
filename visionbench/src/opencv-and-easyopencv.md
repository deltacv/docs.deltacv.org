# OpenCV and EasyOpenCV

## What is OpenCV?

OpenCV is known as a library containing multiple programming functions that are aimed at real-time computer vision.

The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms.

These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality, and more.

![OpenCV used for detecting the 2019-2020 season's stones and skystones](assets/imagen\_2021-09-08\_083505.png)

## So... How do I integrate it to FTC?

The folks from OpenFTC built a library to handle exactly this, wrapping the underlying complexities behind a clean API.

[EasyOpenCV](https://github.com/OpenFTC/EasyOpenCV) integrates OpenCV into the FTC SDK in a straightforward way, bundling the full OpenCV Java library alongside interfaces for accessing internal phone cameras or external webcams and feeding their images into your pipeline.

The EasyOpenCV repo includes examples for both [internal camera](https://github.com/OpenFTC/EasyOpenCV/blob/master/examples/src/main/java/org/openftc/easyopencv/examples/InternalCamera2Example.java) and [webcam](https://github.com/OpenFTC/EasyOpenCV/blob/master/examples/src/main/java/org/openftc/easyopencv/examples/WebcamExample.java) usage.
