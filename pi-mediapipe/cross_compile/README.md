https://github.com/google/mediapipe/tree/master/mediapipe/examples/coral

### Getting arm32 armhf OpenCV libs:

1. Launch Docker container

```
sh launch_docker.sh
```

2. Run copy script from docker container:
```
sh copy_opencv_libs.sh
exit
```

3. libs will be under libs/arm-linux-gnueabihf/:
```
libopencv_calib3d.so     libopencv_highgui.so    libopencv_videoio.so
libopencv_core.so        libopencv_imgcodecs.so  libopencv_video.so
libopencv_features2d.so  libopencv_imgproc.so
```
