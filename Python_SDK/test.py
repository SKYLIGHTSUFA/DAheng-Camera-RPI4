import gxipy as gx
from PIL import Image
import datetime

"""
Author:NoamaNelson
Date:2019-11-21
Discription:Secondary development of pythonsdk of Daheng camera.
"""


def main():
    Width_set = 640  # Установить ширину разрешения
    Height_set = 480  # Установить высокое разрешение
    framerate_set = 80  # Установить частоту кадров
    num = 500  # Время частоты кадров получения (для целей отладки вы можете установить последующее получение изображения как цикл while для получения неограниченного цикла)

    # Распечатать
    print("")
    print("###############################################################")
    print("Постоянно получать цветные изображенияи отображать полученные изображения")
    print("###############################################################")
    print("")
    print("Инициализация камеры ...")
    print("")

    # Создать устройство
    device_manager = gx.DeviceManager()  # Создать объект устройства
    dev_num, dev_info_list = device_manager.update_device_list()  # Enumerate devices, то есть перечислить все доступные устройства
    if dev_num is 0:
        print("Number of enumerated devices is 0")
        return
    else:
        print("")
        print("**********************************************************")
        print("Устройство было успешно создано, номер устройства: % d»" % dev_num)

        # Открыть устройство по серийному номеру устройства
        cam = device_manager.open_device_by_sn(dev_info_list[0].get("sn"))

        # Если это черно-белая камера
        if cam.PixelColorFilter.is_implemented() is False:  # is_implemented Определить, был ли реализован параметр перечисляемого атрибута
            print("Этот пример неподдерживает черно - белые камеры")
            cam.close_device()
            return
        else:
            print("")
            print("**********************************************************")
            print("Цветная камера успешно открыта, серийный номер:% s" % dev_info_list[0].get("sn"))

        # Установить ширину и высоту
        cam.Width.set(Width_set)
        cam.Height.set(Height_set)

        # Настроить непрерывный сбор
        # cam.TriggerMode.set (gx.GxSwitchEntry.OFF) # Установить режим триггера
        cam.AcquisitionFrameRateMode.set(gx.GxSwitchEntry.ON)

        # Установить частоту кадров
        cam.AcquisitionFrameRate.set(framerate_set)
        print("")
        print("**********************************************************")
        print("Частота кадров, установленная пользователем:% d fps" % framerate_set)
        framerate_get = cam.CurrentAcquisitionFrameRate.get()  # Получить частоту кадров текущего приобретения
        print("Частота кадров текущего захвата:% d кадров в секунду" % framerate_get)

        # Начать сбор данных
        print("")
        print("**********************************************************")
        print("Начат сбор данных")
        print("")
        cam.stream_on()

        # Capture image
        for i in range(num):
            raw_image = cam.data_stream[0].get_image()  # Открыть поток данных 0-го канала
            if raw_image is None:
                print("Неудалось получить цветное исходное изображение")
                continue

            rgb_image = raw_image.convert("RGB")  # Получить изображение RGB из цветного исходного изображения
            if rgb_image is None:
                continue

            # rgb_image.image_improvement (color_correction_param, Contrast_lut, gamma_lut) # реализовать улучшение изображения

            numpy_image = rgb_image.get_numpy_array()  # Создать массив numpy из данных изображения RGB
            if numpy_image is None:
                continue

            img = Image.fromarray(numpy_image, 'RGB')  # Показать полученное изображение
            # img.show()
            mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')

            img.save(r"D:\image\\" + str(i) + str("-") + mtime + ".jpg")  # Сохранить картинку локально

            print("Frame ID: %d   Height: %d   Width: %d   framerate_set:%dfps   framerate_get:%dfps"
                  % (raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width(), framerate_set,
                     framerate_get))  # Распечатать высоту, ширину, идентификатор кадра захваченного изображения, частоту кадров, установленную пользователем, и текущую частоту кадров

        # Прекратить собирать
        print("")
        print("**********************************************************")
        print("Камера перестала снимать")
        cam.stream_off()

        # Закрыть устройство
        print("")
        print("**********************************************************")
        print("Система подсказывает: устройство выключено!")
        cam.close_device()

    if __name__ == "__main__":
        main()