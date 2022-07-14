import threading
import time


def CN268():
    from CN268.main import CN268
    CN_268 = CN268()
    CN_268.header_function()


def CN274():
    from CN274.main import CN274
    CN_274 = CN274()
    CN_274.full_function()


def CN299():
    from CN299.main import CN299
    CN_299 = CN299()
    CN_299.maximize_voltage()


def CN300():
    from CN300.main import CN300
    CN_300 = CN300()
    CN_300.full_function()


def EU096():
    from EU096.main import EU096
    EU_096 = EU096()
    EU_096.full_function()


def CN243():
    from CN243.main import CN243
    CN_243 = CN243()
    CN_243.connected_rgb_function()


def JP167():
    from JP167.main import JP167
    JP_167 = JP167()
    JP_167.power_line_communication()


def CN118():
    from CN118.main import CN118
    CN_118 = CN118()
    CN_118.mini_power_monitor_function()


def EU065():
    from EU065.main import EU065
    EU = EU065()
    EU.light_control_function()


def CN157():
    from CN157.main import CN157
    CN_157 = CN157()
    CN_157.manual_testing()


def EU036():
    from EU036.main import EU036
    EU_036 = EU036()
    EU_036.slider_function()


def EU045():
    from EU045.main import EU045
    EU_045 = EU045()
    EU_045.alcohol_gas_function()


def EU084():
    from EU084.main import EU084
    EU_084 = EU084()
    EU_084.auto_mode()


def RZ_A2M():
    from RZ_A2M.main import RZ_A2M
    RZ_A2M = RZ_A2M()
    RZ_A2M.face_detection_function()


def AS104():
    from AS104.main import AS104
    AS_104 = AS104()
    AS_104.config_function()


def EU065_2nd():
    from EU065.main import EU065
    EU = EU065()
    EU.RGB_control_function()


def CN157_2nd():
    from CN157.main import CN157
    CN_157 = CN157()
    CN_157.auto_testing()


def EU036_2nd():
    from EU036.main import EU036
    EU_036 = EU036()
    EU_036.temperature_control_function()


def EU045_2nd():
    from EU045.main import EU045
    EU_045 = EU045()
    EU_045.humidity_shot_function()


def EU084_2nd():
    from EU084.main import EU084
    EU_084 = EU084()
    EU_084.auto_mode()


def RZ_A2M_2nd():
    from RZ_A2M.main import RZ_A2M
    RZ_A2M = RZ_A2M()
    RZ_A2M.barcode_scanner_function()


if __name__ == "__main__":
    # ////////////////////////////////////////////////////////////////////
    test1 = threading.Thread(target=CN268)
    # test2 = threading.Thread(target=CN274)
    # test3 = threading.Thread(target=CN299)
    # test4 = threading.Thread(target=CN300)
    # test5 = threading.Thread(target=EU096)
    # test6 = threading.Thread(target=CN243)
    # test7 = threading.Thread(target=JP167)
    # test8 = threading.Thread(target=CN118)

    # RUN 1ST FUNCTION---------------------
    # test9 = threading.Thread(target=EU065)
    # test10 = threading.Thread(target=CN157)
    # test11 = threading.Thread(target=EU036)
    # test12 = threading.Thread(target=EU045)
    # test13 = threading.Thread(target=EU084)
    # test14 = threading.Thread(target=RZ_A2M)
    # test15 = threading.Thread(target=AS104)

    # RUN 2ND FUNCTION-----------------------
    # test9_2nd = threading.Thread(target=EU065_2nd)
    # test10_2nd = threading.Thread(target=CN157_2nd)
    # test11_2nd = threading.Thread(target=EU036_2nd)
    # test12_2nd = threading.Thread(target=EU045_2nd)
    # test13_2nd = threading.Thread(target=EU084_2nd)
    # test14_2nd = threading.Thread(target=RZ_A2M_2nd)

    # //////////////////////////////////////////////////////////////////////
    # test1.start()
    # time.sleep(3)
    #
    # test2.start()
    # time.sleep(3)
    #
    # test3.start()
    # time.sleep(3)
    #
    # test4.start()
    # time.sleep(3)
    #
    # test5.start()
    # time.sleep(3)

    # test6.start()
    # time.sleep(3)
    #
    # test7.start()
    # time.sleep(3)

    # test8.start()
    # time.sleep(3)

    # 1ST FUNCTION--------------

    # test9.start()
    # time.sleep(3)
    #
    # test10.start()
    # time.sleep(3)
    #
    # test11.start()
    # time.sleep(3)
    #
    # test12.start()
    # time.sleep(3)
    #
    # test13.start()
    # time.sleep(3)
    #
    # test14.start()
    # time.sleep(3)
    # #
    # test15.start()
    # time.sleep(3)

    # 2ND FUNCTION

    # test9_2nd.start()
    # time.sleep(3)
    #
    # test10_2nd.start()
    # time.sleep(3)

    # test11_2nd.start()
    # time.sleep(3)
    #
    # test12_2nd.start()
    # time.sleep(3)
    #
    # test13_2nd.start()
    # time.sleep(3)
    #
    # test14_2nd.start()
    # time.sleep(3)

    # ///////////////////////////////////////////////////////////////
    # test1.join()
    # time.sleep(3)
    #
    # test2.join()
    # time.sleep(3)
    #
    # test3.join()
    # time.sleep(3)
    #
    # test4.join()
    # time.sleep(3)
    #
    # test5.join()
    # time.sleep(3)

    # test6.join()
    # time.sleep(3)
    #
    # test7.join()
    # time.sleep(3)

    # test8.join()
    # time.sleep(3)

    # 1ST FUNCTION------------------------------------------------------

    # test9.join()
    # time.sleep(3)
    #
    # test10.join()
    # time.sleep(3)
    #
    # test11.join()
    # time.sleep(3)
    #
    # test12.join()
    # time.sleep(3)
    #
    # test13.join()
    # time.sleep(3)
    #
    # test14.join()
    # time.sleep(3)
    #
    # test15.join()
    # time.sleep(3)

    # 2ND FUNCTION------------------------------------------------------

    # test9_2nd.join()
    # time.sleep(3)
    #
    # test10_2nd.join()
    # time.sleep(3)

    # test11_2nd.join()
    # time.sleep(3)
    #
    # test12_2nd.join()
    # time.sleep(3)
    #
    # test13_2nd.join()
    # time.sleep(3)
    #
    # test14_2nd.join()
    # time.sleep(3)
