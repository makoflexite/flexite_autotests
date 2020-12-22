import datetime

from .base_page import BasePage

# cur_time = ''

class CrossData(BasePage):
    current_time_data = ''
    # CURRENT_TIME_DATA = datetime.datetime.now().strftime("%H:%M")
    # print(CURRENT_TIME_DATA)
    def current_time_function(self):
        # global cur_time
        if self.is_element_present_by_text('Process 1 - Initiate', wait_time=5):
            assert self.is_element_present_by_css("#iframe_content_id_ti1", wait_time=5), "iframe0 is not found!"
            cur_time = datetime.datetime.now().strftime("%H:%M")
            CrossData.current_time_data = cur_time
            print('CrossData.current_time_data', CrossData.current_time_data)
            return cur_time


# def current_time_calculation():
#     global current_time
#     current_time = datetime.datetime.now().strftime("%H:%M")
#     print(current_time)



