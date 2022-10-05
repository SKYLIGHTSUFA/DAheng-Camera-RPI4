# coding = utf-8
import gxipy as gx
from PIL import Image
import numpy
import cv2
import threading
import sys
import time


class Mer():
    global m_bIsBegin
    m_bIsBegin = False
    m_bContinuous = False;
    def __init__(self,index):
        # --------------------------相机参数相关-------------------------------------------------
        self.IsSnap = False
        self.device_manager = gx.DeviceManager()
        self.index = index
        self.time_now = 0
        self.time_previce = 0
        self.m_old_statue = True
        dev_num, self.dev_info_list = self.device_manager.update_device_list()
        if dev_num is 0:
            print("Number of enumerated devices is 0")
            return
        # ----------------------------------------------------------------------------------------
    def OnClickOpen(self):
        # open the first device
        self.cam = self.device_manager.open_device_by_index(self.index)
        print(self.cam)
        #------------------------ if camera is color----------------------------------------
        if self.cam.PixelColorFilter.is_implemented() is True:
        
            self.cam.BalanceWhiteAuto.set(gx.GxAutoEntry.CONTINUOUS)
            if self.cam.GammaParam.is_readable():
                gamma_value = self.cam.GammaParam.get()
                self.gamma_lut = gx.Utility.get_gamma_lut(gamma_value)
            else:
                self.gamma_lut = None
            if self.cam.ContrastParam.is_readable():
                contrast_value = self.cam.ContrastParam.get()
                self.contrast_lut = gx.Utility.get_contrast_lut(contrast_value)
            else:
                self.contrast_lut = None
            self.color_correction_param = self.cam.ColorCorrectionParam.get()


        #---------------------------------------------------------------------------
        # set continuous acquisition
        self.cam.TriggerMode.set(gx.GxSwitchEntry.OFF)
        #self.cam.TriggerSource.set(gx.GxTriggerSourceEntry.SOFTWARE)
        # set exposure
        self.cam.ExposureTime.set(100000)

        # set gain
        self.cam.Gain.set(10.0)
        self.cam.stream_on()
        

    def OnContinusSnap(self):
        if self.cam.PixelColorFilter.is_implemented() is True:
            t1 = threading.Thread(target=self.acq_color_thread, args=(self.cam,self.index),daemon=True)
        else:
            t1 = threading.Thread(target=self.acq_mono_thread, args=(self.cam,self.index), daemon=True)
        t1.start()
        self.IsSnap = True
        m_bIsBegin = True
        self.m_bContinuous = True; 

    def OnClickStop(self):
        self.IsSnap = False
        self.m_bContinuous = False;
        time.sleep(0.5)
        self.cam.stream_off()
        self.cam.AcquisitionStop.send_command()
        


    def OnClickClose(self):
        self.IsSnap = False
        m_bIsBegin = False
        self.cam.close_device()

    def acq_color_thread(self,device,index):
        cv2.namedWindow("Cam"+str(self.index), 0)
        while(self.m_bContinuous):
            #tic1 = time.time()
            #device.TriggerSoftware.send_command()
            # get raw image
            raw_image = device.data_stream[0].get_image()
            #toc1 = time.time()
            #print("相机%s 第%s次（进去: %s，完成: %s）：  " % (str(self.index),str(i),toc1, tic1))
            if raw_image is None:
                print("Getting image failed.")
                continue

            self.time_now = raw_image.get_timestamp()
            rate = 1000000000/(self.time_now - self.time_previce)
            self.time_previce = raw_image.get_timestamp()
            #print("相机显示帧率为：%s" %rate)
            # get RGB image from raw image
            rgb_image = raw_image.convert("RGB")
            if rgb_image is None:
                continue
            rgb_image.image_improvement(self.color_correction_param, self.contrast_lut, self.gamma_lut)
            # create numpy array with data from raw image

            numpy_image = rgb_image.get_numpy_array()
            if numpy_image is None:
                continue

            # show acquired image
            cv2.imshow('Cam'+str(self.index), numpy_image)
            if cv2.waitKey(30)  == 27:
                break
            # print height, width, and frame ID of the acquisition image
            #print("Cam ID : %d    Frame ID: %d   Height: %d   Width: %d" % (self.index,raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width()))

    def acq_mono_thread(self,device,index):
        cv2.namedWindow('Cam'+str(self.index), 0)
        while(self.m_bContinuous):
            # get raw image
            #tic1 = time.time()
            #time_begin.append(tic1)

            #device.TriggerSoftware.send_command()
            raw_image = device.data_stream[0].get_image()
            '''
            toc1 = time.time()
            time_end.append(toc1)
            print("相机%s 第%s次（进去: %s，完成: %s）：  " % (str(self.index),str(i),tic1, toc1))
            '''
            if raw_image is None:
                print("Getting image failed.")
                continue

            # create numpy array with data from raw image
            numpy_image = raw_image.get_numpy_array()

            if numpy_image is None:
                continue

            # show acquired image

            cv2.imshow('Cam'+str(self.index), numpy_image)
            if cv2.waitKey(30)  == 27:
                break
            # print height, width, and frame ID of the acquisition image
            #print("Cam ID : %d   Frame ID: %d   Height: %d   Width: %d" % (self.index,raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width()))

        



if __name__=="__main__":
    global timer
    device_manager = gx.DeviceManager()
    dev_num, dev_info_list = device_manager.update_device_list()
    if dev_num == 0:
        print('No cam found')
        sys.exit(1)
    cams =[]
    for i in range(dev_num):
        CamTmp = Mer(i+1)
        cams.append(CamTmp)
    #cam1 = Mer(1)
    #cam2 = Mer(2)
    #cam3 = Mer(3)
    #cam4 = Mer(4)

    
    #cams.append(cam2)
    #cams.append(cam3)
    #cams.append(cam4)
    for camera in cams:
        camera.OnClickOpen()
        camera.OnContinusSnap()       
    while True:
        # 判断按键，如果按键为q，退出循环
        a = input("是否退出,退出按q：\n")
        if a == 'q':
            print("主程序退出")
            for camera in cams:
                camera.OnClickStop()
                camera.OnClickClose() 
            sys.exit(0)
            break
