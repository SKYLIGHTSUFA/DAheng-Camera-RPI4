# version:1.0.1905.9051
import gxipy as gx

from PIL import Image
import numpy
import cv2
import _thread
import threading
import time
from queue import Queue

q = Queue(maxsize=1)
m_gLiveFlag = 1
m_gProcessFlag = 1

##def main():
def live_image( threadName, delay):
    # print the demo information
    print("")
    print("-------------------------------------------------------------")
    print("Sample to show how to acquire mono image continuously and show acquired image.")
    print("-------------------------------------------------------------")
    print("")
    print("Initializing......")
    print("")

    # create a device manager
    device_manager = gx.DeviceManager()
    dev_num, dev_info_list = device_manager.update_device_list()
    if dev_num is 0:
        print("Number of enumerated devices is 0")
        return

    # open the first device
    cam = device_manager.open_device_by_index(1)

    # exit when the camera is a color camera
    if cam.PixelColorFilter.is_implemented() is True:
        print("This sample does not support color camera.")
        cam.close_device()
        return

    # set continuous acquisition
    cam.TriggerMode.set(gx.GxSwitchEntry.OFF)

    # set exposure
    cam.ExposureTime.set(10000.0)

    # set gain
    cam.Gain.set(10.0)

    # set the acq buffer count
    cam.data_stream[0].set_acquisition_buffer_number(1)
    # start data acquisition
    cam.stream_on()

    # acquire image: num is the image number
    #num = 1000
    #for i in range(num):
    while m_gLiveFlag == 1:
        # get raw image
        raw_image = cam.data_stream[0].get_image()
        if raw_image is None:
            print("Getting image failed.")
            continue

        # create numpy array with data from raw image
        numpy_image = raw_image.get_numpy_array()
        if numpy_image is None:
            continue

        # show acquired image
        #img = Image.fromarray(numpy_image, 'L')
	#img.show()

        # display image with opencv
        pimg = cv2.cvtColor(numpy.asarray(numpy_image),cv2.COLOR_GRAY2BGR)
        #put image date to queue
        if q.qsize() ==0:
            q.put(pimg)
        cv2.imshow("OpenCV",pimg)
        cv2.waitKey(10)
        
        # print height, width, and frame ID of the acquisition image
        #print("Frame ID: %d   Height: %d   Width: %d"
              #% (raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width()))

    # stop data acquisition
    cam.stream_off()

    # close device
    cam.close_device()
    cv2.destroyAllWindows() 

#if __name__ == "__main__":
    #main()
def process_image( threadName, delay):
    count = 0
    while m_gProcessFlag ==1:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
        if q.qsize() >0:
          if count <10:
            pimg = q.get()
            cv2.imwrite('test-%d.jpg'%(count),pimg,[int(cv2.IMWRITE_JPEG_QUALITY),70])


def main():
    # print the demo information
    print("")
    print("-------------------------------------------------------------")
    print("Sample to show how to acquire color image continuously and show acquired image.")
    print("-------------------------------------------------------------")
    print("")
    print("Initializing......")
    print("")

# 创建两个线程
    try:
       _thread.start_new_thread( live_image, ("live_image", 5, ) )
       _thread.start_new_thread( process_image, ("process_image", 2, ) )
    except:
       print ("Error: 无法启动线程")


if __name__ == "__main__":
    main()
