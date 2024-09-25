A simple video to image converter utilizing OpenCV Python.

This code was used to extract frames from h264 video obtained for Bacterial Resistance Susceptibility Testing from Goh Lab at the University of Toronto.

## Directions

The python files are under the folder *src*

Change the following to collect every *frame_interval* frame (i.e., 1 would mean storing every possible frame)
```
frame_interval = 1
```

Change the following to specify the path of the video

```
base_name = "INPUT VIDEO NAME"  
```

*filesave_all_at_once.py* allows processing the entire videos within a folder
