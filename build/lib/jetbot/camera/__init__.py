import os

#DEFAULT_CAMERA = os.environ.get('JETBOT_DEFAULT_CAMERA', 'opencv_gst_camera')
#DEFAULT_CAMERA = os.environ.get('JETBOT_DEFAULT_CAMERA', 'opencv_usb_camera')
DEFAULT_CAMERA = 'opencv_usb_camera'

print(DEFAULT_CAMERA)

if DEFAULT_CAMERA == 'zmq_camera':
    from .zmq_camera import ZmqCamera
    Camera = ZmqCamera
elif DEFAULT_CAMERA == 'opencv_gst_camera':
    #from .opencv_gst_camera import OpenCvGstCamera
    #Camera = OpenCvGstCamera
else:
    from .opencv_usb_camera import OpenCvUsbCamera
    Camera = OpenCvUsbCamera
    
