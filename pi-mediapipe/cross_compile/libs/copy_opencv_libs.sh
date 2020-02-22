# https://github.com/google/mediapipe/tree/master/mediapipe/examples/coral
export DEST=/dest/arm-linux-gnueabihf
export SRC=/usr/local/lib

mkdir -p $DEST
cd $SRC
cp libopencv_core.so $DEST
cp libopencv_calib3d.so $DEST
cp libopencv_features2d.so $DEST
cp libopencv_highgui.so $DEST
cp libopencv_imgcodecs.so $DEST
cp libopencv_imgproc.so $DEST
cp libopencv_video.so $DEST
cp libopencv_videoio.so $DEST

