import time

while 1:
    choice = int(input('Run All Boards : \n'
                       '1: Run_ALL_function:\n'
                       '2: Run_1st_function_allBoards:\n'
                       '3: Run_2nd_function_allBoards:\n'
                       '4: Run_3nd_function_allBoards:\n'
                       '5: Run_4nd_function_allBoards:\n'
                       '6: Exit\n'
                       'Option: \n'))

    # FOR ALL FUNCTIONS
    if choice == 1:
        # from CN268.main import CN268
        # CN_268 = CN268()
        # CN_268.header_function()

        from CN274.main import CN274
        CN_274 = CN274()
        CN_274.full_function()

        from CN299.main import CN299
        CN_299 = CN299()
        CN_299.maximize_voltage()

        # from CN300.main import CN300
        # CN_300 = CN300()
        # CN_300.full_function()

        # from EU096.main import EU096
        # EU_096 = EU096()
        # EU_096.full_function()

        # from AS104.main import AS104
        # AS_104 = AS104()
        # AS_104.in_rush()

        exit()

    # FOR 1ST FUNCTIONS
    if choice == 2:
        # from EU065.main import EU065
        # EU = EU065()
        # EU.light_control_function()

        # from CN157.main import CN157
        # CN_157 = CN157()
        # CN_157.manual_testing()

        # from EU036.main import EU036
        # EU_036 = EU036()
        # EU_036.slider_function()

        # from EU045.main import EU045
        # EU_045 = EU045()
        # EU_045.alcohol_gas_function()

        # from EU084.main import EU084
        # EU_084 = EU084()
        # EU_084.auto_mode()

        # from RZ_A2M.main import RZ_A2M
        # RZ_A2M = RZ_A2M()
        # RZ_A2M.face_detection_function()

        # from US101.main import US101
        # US101 = US101()
        # US101.object_detection_function()

        from AS104.main import AS104
        AS_104 = AS104()
        AS_104.config_function()

        exit()

    # FOR 2ND FUNCTIONS
    if choice == 3:
        # from EU065.main import EU065
        # EU = EU065()
        # EU.RGB_control_function()

        # from CN157.main import CN157
        # CN_157 = CN157()
        # CN_157.auto_testing()

        # from EU036.main import EU036
        # EU_036 = EU036()
        # EU_036.temperature_control_function()

        # from EU045.main import EU045
        # EU_045 = EU045()
        # EU_045.humidity_shot_function()
        #
        from EU084.main import EU084
        EU_084 = EU084()
        EU_084.auto_mode()

        # from RZ_A2M.main import RZ_A2M
        # RZ_A2M = RZ_A2M()
        # RZ_A2M.barcode_scanner_function()

        exit()

    if choice == 4:
        from EU045.main import EU045
        EU_045 = EU045()
        EU_045.temperature_function()

    if choice == 5:
        from EU045.main import EU045
        EU_045 = EU045()
        EU_045.clear_air_function()

    if choice == 5:
        print('Thanks for executing me!!!!')
        exit()
