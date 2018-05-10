import os
import sys
import numpy as np
import platform
import skimage.io
import skimage.transform

# utilities
sys.path += ['/ncappzoo/apps/ssd-object-detector']
from utils import deserialize_output

print(", ".join(platform.uname()))

import mvnc.mvncapi as mvnc
mvnc.SetGlobalOption(mvnc.GlobalOption.LOG_LEVEL, 0)

TEST_IMAGE = 'assets/coreml_mobilenet.png'
GRAPH = '/ncappzoo/caffe/SSD_MobileNet/graph'
LABELS = '/ncappzoo/caffe/SSD_MobileNet/labels.txt'
MEAN = 127.5
SCALE = 0.00789
CONFIDENCE_THRESHOLD = 0.60

# find the first movidius
ncs_name = mvnc.EnumerateDevices()[0]
movidius = mvnc.Device(ncs_name)

try:
    movidius.OpenDevice()
    print('Hello Movidius: ', ncs_name)

    # load the graph
    print('loading graph: ', GRAPH)
    with open(GRAPH, mode='rb') as f:
        blob = f.read()
    graph = movidius.AllocateGraph(blob)
    print('loaded graph: ', GRAPH)

    # load the labels
    labels = [line.rstrip('\n') for line in open(LABELS) if line != 'classes\n']

    # pre-process the image
    raw_image = skimage.io.imread(TEST_IMAGE)
    input = skimage.transform.resize(raw_image, [300, 300], preserve_range=True)
    input = input[:, :, ::-1] # RGB -> BGR
    input = input.astype(np.float16)
    input = (input - np.float16(MEAN)) * SCALE # subtract mean & scale

    # warm start with a dummy forward pass
    graph.LoadTensor(input, 'user object')
    output, userobj = graph.GetResult()

    # actual timed inference
    graph.LoadTensor(input, 'user object')
    output, userobj = graph.GetResult()
    inference_time = graph.GetGraphOption(mvnc.GraphOption.TIME_TAKEN)

    # deserialize and print output
    output_dict = deserialize_output.ssd(output, CONFIDENCE_THRESHOLD, input.shape)

    print( "Execution time: " + str(np.sum(inference_time)) + "ms" )
    for i in range(0, output_dict['num_detections']):
        print("%3.1f%%\t" % output_dict['detection_scores_' + str(i)]
               + labels[int(output_dict['detection_classes_' + str(i)])]
               + ": Top Left: " + str( output_dict['detection_boxes_' + str(i)][0])
               + " Bottom Right: " + str( output_dict['detection_boxes_' + str(i)][1]))

finally:
    # cleanup
    graph.DeallocateGraph()
    movidius.CloseDevice()
