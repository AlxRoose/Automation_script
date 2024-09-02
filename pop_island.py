# -*- encoding=utf8 -*-
__author__ = "帅伦"

from airtest.core.api import *
import os
from abc import ABC, abstractmethod
import logging

os.environ['AIRTEST_USE_MINICAP'] = '1'
auto_setup(__file__)


def initialize_device():
    init_device()
    device_info = device().display_info
    return device_info['width'], device_info['height']


width, height = initialize_device()


class ImageRecognizer(ABC):
    @abstractmethod
    def wait_for_image(self, image, timeout=10):
        pass


class AirtestImageRecognizer(ImageRecognizer):
    @staticmethod
    def wait_for_image(image, timeout=10):
        start_time = time.time()
        while True:
            if exists(image):
                sleep(2)
                return True
            if time.time() - start_time > timeout:
                return False


class DeviceOperator(ABC):
    @abstractmethod
    def touch(self, target):
        pass

    @abstractmethod
    def swipe(self, start, end):
        pass

    @abstractmethod
    def input_text(self, text):
        pass


class AirtestDeviceOperator(DeviceOperator):
    @staticmethod
    def touch(target):
        touch(target)

    @staticmethod
    def swipe(start, end):
        swipe(v1=start, v2=end)

    @staticmethod
    def input_text(text_content):
        # 使用 text 函数输入文本
        text(text_content, enter=False)


class TemplateManager:
    def __init__(self):
        self.templates = {}

    def add_template(self, name, path, record_pos, threshold=0.8):
        self.templates[name] = Template(path, record_pos=record_pos, resolution=(width, height), threshold=threshold)

    def get_template(self, name):
        return self.templates.get(name)


class Level(ABC):
    def __init__(self, tester):
        self.tester = tester

    @abstractmethod
    def execute(self):
        pass


class Level1(Level):
    def execute(self):
        self.tester.device_operator.touch(self.tester.template_manager.get_template('level_button'))
        if self.tester.image_recognizer.wait_for_image(self.tester.template_manager.get_template('tips_level_1_1')):
            self.tester.device_operator.swipe((0.606, 0.51), (0.503, 0.515))
        sleep(2)
        self.tester.input_command(1)
        self.tester.end_level()
        sleep(2)
        self.tester.transition()




class Level2(Level):
    def execute(self):
        self.tester.start_level()
        if self.tester.image_recognizer.wait_for_image(self.tester.template_manager.get_template('tips_leval_2_1')):
            self.tester.device_operator.touch((0.406, 0.804))
        sleep(2)
        self.tester.end_level(3)
        self.tester.level_connect('normal_button_3')


class Level3(Level):
    def execute(self):
        self.tester.generate_level('level_3', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.616, 0.515), 'v2': (0.606, 0.457)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.606, 0.457), 'v2': (0.502, 0.457)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.183, 0.465), 'v2': (0.289, 0.457)},
            {'type': 'sleep', 'duration': 2}
        ], 3)
        self.tester.level_connect('normal_button_4')


class Level4(Level):
    def execute(self):
        self.tester.generate_level('level_4', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.5, 0.56), 'v2': (0.5, 0.51)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'touch', 'v': (0.5, 0.51)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.185, 0.56), 'v2': (0.291, 0.56)},
            {'type': 'sleep', 'duration': 2}
        ], 3)
        self.tester.level_connect('normal_button_4')
        self.tester.level_bouns()


class Level5(Level):
    def execute(self):
        self.tester.generate_level('level_5', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.66, 0.371), 'v2': (0.76, 0.371)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.766, 0.418), 'v2': (0.766, 0.371)},
            {'type': 'sleep', 'duration': 2}
        ], 2)


class Level6(Level):
    def execute(self):
        self.tester.generate_level('level_6', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.714, 0.561), 'v2': (0.714, 0.511)},
            {'type': 'sleep', 'duration': 2},
            {'type': 'swipe', 'v1': (0.714, 0.511), 'v2': (0.714, 0.461)},
            {'type': 'sleep', 'duration': 5},
            {'type': 'touch', 'v': (0.714, 0.561)}
        ], 2)


class Level7(Level):
    def execute(self):
        self.tester.generate_level('level_7', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'touch', 'v': (0.479, 0.825)}
        ], 6)
        self.tester.pause(v=(0.479, 0.825), seconds=5)


class Level8(Level):
    def execute(self):
        self.tester.level_8()


class Level9(Level):
    def execute(self):
        self.tester.generate_level('level_9', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'touch', 'v': (0.177, 0.584)}
        ], 5)
        self.tester.pause(v=(0.177, 0.584))


class Level10(Level):
    def execute(self):
        self.tester.generate_level('level_10', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'touch', 'v': (0.106, 0.963)},
            {'type': 'sleep', 'duration': 3},
            {'type': 'touch', 'v': (0.499, 0.419)},
            {'type': 'sleep', 'duration': 3}
        ], 2)


class Level11(Level):
    def execute(self):
        self.tester.generate_level('level_11', [{'type': 'sleep', 'duration': 2}], 5)
        self.tester.pause(v=(0.106, 0.963))


class Level12(Level):
    def execute(self):
        self.tester.generate_level('level_12', [
            {'type': 'sleep', 'duration': 2},
            {'type': 'touch', 'v': (0.277, 0.94)},
            {'type': 'sleep', 'duration': 3},
            {'type': 'touch', 'v': (0.5, 0.399)},
            {'type': 'sleep', 'duration': 3}
        ], 3)



class AutoTester:
    def __init__(self, package_name):
        self.package_name = package_name
        self.image_recognizer = AirtestImageRecognizer()
        self.device_operator = AirtestDeviceOperator()
        self.template_manager = TemplateManager()
        self.initialize_templates()
        self.levels = self.initialize_levels()

    def initialize_templates(self):
        templates = {
            'old_man': (r"tpl1724123981736.png", (0.0, 0.557)),
            'skip_button': (r"tpl1724124127732.png", (0.378, -1.0)),
            'normal_button': (r"tpl1724124305716.png", (0.043, -0.235)),
            'level_button': (r"tpl1724125875253.png", (-0.249, 0.697)),
            'tips_level_1_1': (r"tpl1724133947551.png", (0.006, -0.499)),
            'arrow': (r"tpl1724145672828.png", (0.225, -0.033)),
            'una': (r"tpl1724142104789.png", (0.231, 0.658)),
            'down_arrow': (r"tpl1725241534265.png", (-0.021, -0.431)),
            'play_button': (r"tpl1724143177910.png", (0.0, 0.375), 0.7),
            'tips_leval_2_1': (r"tpl1724143366851.png", (-0.003, -0.589)),
            'gm_tool': (r"tpl1724639811583.png", (0.45, -0.001)),
            'gm_run_button': (r"tpl1724640029480.png", (0.332, -0.029)),
            'text_label': (r"tpl1724640211171.png", (-0.3, -0.025)),
            'level_bouns_tips' :(r"tpl1724723145871.png",(-0.001, 0.321)),
            'gm_run': (r"tpl1724640466603.png", (0.342, -0.029)),
            'win_button': (r"tpl1724641848434.png", (-0.417, 1.079)),
            'gm_close_button': (r"tpl1724641962421.png", (0.436, -1.006)),
            'update_tips': (r"tpl1724738972155.png", (-0.003, -0.106)),
            'update_skip_button': (r"tpl1724739130220.png", (-0.182, 0.122)),
            'task': (r"tpl1724745207919.png", (-0.167, 0.825)),
            'task_button': (r"tpl1724745344766.png", (-0.167, 0.897)),
            'mark': (r"tpl1724746656502.png", (-0.165, 0.631)),
            'claim_button': (r"tpl1724746747694.png", (-0.165, 0.897)),
            'tips_level_8_1': (r"tpl1724750840396.png", (-0.096, -0.357)),
            'tips_level_8_2': (r"tpl1724750963659.png", (0.003, -0.392)),
            'tips_level_8_3': (r"tpl1724751185857.png", (-0.401, -0.768)),
            'five_star': (r"tpl1724915626005.png", (-0.075, -0.938)),
            'completed': (r"tpl1724912158649.png", (0.243, 0.692)),
            "level_3": (r"tpl1724653934920.png", (0.019, -0.449)), 
            "level_4": (r"tpl1724722376722.png", (-0.029, -0.735)),
            "level_5": (r"tpl1724727296858.png", (0.014, -0.757)),
            "level_6": (r"tpl1724750062114.png", (0.092, -0.265)),
            "level_7": (r"tpl1724750544281.png", (0.004, -0.594)),
            "level_9": (r"tpl1724751361062.png", (-0.003, -0.688)),
            "level_10": (r"tpl1724751570972.png", (-0.007, 0.572)),
            "level_11": (r"tpl1724897796748.png", (-0.215, 0.186)),
            "level_12": (r"tpl1724751852972.png", (-0.006, 0.574)),
            'una_and_oldman':(r"tpl1724723145871.png",(-0.001, 0.321)),
            'area_tips':(r"tpl1724723572367.png",(-0.001, 0.321)),
            'expand_button':(r"tpl1724723625479.png", (0.094, -0.161)),
            'normal_button_2':(r"tpl1725241429125.png", (0.0, -0.032), ),
            'normal_button_3':(r"tpl1725241671200.png", (-0.022, -0.253)),
            'normal_button_4':(r"tpl1725241993753.png", (0.04, -0.233)),
        }
        for name, values in templates.items():
            if len(values) == 2:
                path, pos = values
                threshold = 0.8  # 默认阈值
            elif len(values) == 3:
                path, pos, threshold = values
            else:
                raise ValueError(f"Invalid template data for {name}")

            self.template_manager.add_template(name, path, pos, threshold)

    def initialize_levels(self):
        return [
            Level1(self), Level2(self), Level3(self), Level4(self),
            Level5(self), Level6(self), Level7(self), Level8(self),
            Level9(self), Level10(self), Level11(self), Level12(self)
        ]

    def start(self):
        try:
            stop_app(self.package_name)
            start_app(self.package_name)
            print(f"成功启动！-->{self.package_name}")
        except Exception as e:
            raise Exception(f"检查下包名系咪错嗨左啦7头！Error info: {e}")

    def launch(self):
        if not self.image_recognizer.wait_for_image(self.template_manager.get_template('update_tips'), timeout=40):
            pass
        else:
            self.device_operator.touch(self.template_manager.get_template('update_skip_button'))
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('old_man'), timeout=50):
            self.device_operator.touch(self.template_manager.get_template('skip_button'))
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('arrow'), timeout=20):
                self.device_operator.touch(self.template_manager.get_template('normal_button'))
                sleep(5)
        else:
            raise Exception("Error:未检测到目标图片！")

    def input_command(self, level_num):
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('gm_tool')):
            self.device_operator.touch(self.template_manager.get_template('gm_tool'))
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('gm_run_button')):
                self.device_operator.touch(self.template_manager.get_template('text_label'))
                sleep(6)
                self.device_operator.input_text(f"JumpLevel " + str(level_num))
                sleep(2)
                self.device_operator.touch((0.387, 0.61))
                sleep(2)
                self.device_operator.touch(self.template_manager.get_template('gm_run'))
                sleep(5)  # 等待命令执行
                self.close_gm_tool()  # 关闭GM工具
        else:
            logging.warning("未找到GM工具按钮")

    def close_gm_tool(self):
        max_attempts = 3
        for attempt in range(max_attempts):
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('gm_close_button'), timeout=5):
                self.device_operator.touch(self.template_manager.get_template('gm_close_button'))
                sleep(2)  # 等待关闭动画
                if not self.image_recognizer.wait_for_image(self.template_manager.get_template('gm_tool'), timeout=3):
                    logging.info(f"GM工具已关闭，尝试次数：{attempt + 1}")
                    return
            else:
                logging.warning(f"未找到GM工具关闭按钮，尝试次数：{attempt + 1}")

        logging.error("无法关闭GM工具，请手动检查")

    def end_level(self, seconds=2):
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('win_button')):
            self.device_operator.touch(self.template_manager.get_template('win_button'))
            sleep(2)
            self.device_operator.touch((0.387, 0.61))
            sleep(2)
            self.device_operator.touch((0.387, 0.61))
        sleep(seconds)

    def start_level(self):
        sleep(5)
        self.device_operator.touch((0.248, 0.806))
        sleep(3)
        play_button = self.template_manager.get_template('play_button')
        if play_button is None:
            logging.error("Play button template not found")
            return
        if not self.image_recognizer.wait_for_image(play_button, timeout=20):
            logging.error("Play button not found on screen")
            return
        self.device_operator.touch(play_button)

    def level_connect(self,template_name):
        if self.image_recognizer.wait_for_image(self.template_manager.get_template(template_name)):
            self.device_operator.touch(self.template_manager.get_template(template_name))
            sleep(2)

    def level_bouns(self):
        sleep(2)
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('level_bouns_tips'), timeout=30):
            self.device_operator.touch((0.437, 0.84))
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('una_and_oldman')):
                sleep(5)
                self.device_operator.touch((0.853, 0.058))
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('area_tips')):
                sleep(5)
                self.device_operator.touch(self.template_manager.get_template('expand_button'))
            sleep(5)

    def generate_level(self, level_tips, actions, sleep_time):
        self.start_level()
        if self.image_recognizer.wait_for_image(self.template_manager.get_template(level_tips)):
            for action in actions:
                if action['type'] == 'sleep':
                    sleep(action['duration'])
                elif action['type'] == 'swipe':
                    self.device_operator.swipe(action['v1'], action['v2'])
                elif action['type'] == 'touch':
                    self.device_operator.touch(action['v'])
        self.end_level(sleep_time)
        

    def pause(self, v=None, seconds=2):
        if v:
            self.device_operator.touch(v)
        sleep(seconds)

    def level_8(self):
        self.start_level()
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('tips_level_8_1')):
            self.device_operator.touch((0.25, 0.55))
            sleep(3)
            self.device_operator.touch(self.template_manager.get_template('play_button'))
            sleep(3)

        if self.image_recognizer.wait_for_image(self.template_manager.get_template('tips_level_8_2')):
            self.device_operator.swipe((0.504, 0.462), (0.504, 0.512))
            sleep(5)

        self.end_level()

        sleep(2)
        if self.image_recognizer.wait_for_image(self.template_manager.get_template('tips_level_8_3')):
            self.device_operator.touch(self.template_manager.get_template('tips_level_8_3'))
            sleep(5)
            self.device_operator.touch((0.177, 0.584))
            sleep(5)

    def transition(self):

        if self.image_recognizer.wait_for_image(self.template_manager.get_template('arrow')):
            self.device_operator.touch(self.template_manager.get_template('normal_button_2')) # <-
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('una'), timeout=20):
                self.device_operator.touch(target=(0.853, 0.058))
                if self.image_recognizer.wait_for_image(self.template_manager.get_template('down_arrow'), timeout=20):
                    sleep(2)
                self.device_operator.touch(target=(0.387, 0.61))



    def run_all_levels(self):
        for level in self.levels:
            level.execute()

    def newbie(self):
        self.start()
        self.launch()
        self.run_all_levels()

    def touch_task_button(self):
        found = False
        while not found:
            if self.image_recognizer.wait_for_image(self.template_manager.get_template('five_star')):
                self.device_operator.touch((0.468, 0.813))
                found = True
            elif self.image_recognizer.wait_for_image(self.template_manager.get_template('completed')):
                self.device_operator.touch((0.726, 0.812))
                sleep(3)
                if self.image_recognizer.wait_for_image(self.template_manager.get_template('mark')):
                    self.device_operator.touch(self.template_manager.get_template('claim_button'))
                    sleep(8)
                    self.device_operator.touch((0.766, 0.665))
                else:
                    self.device_operator.touch(self.template_manager.get_template('task_button'))
                    sleep(10)
                    self.device_operator.touch((0.766, 0.665))


if __name__ == '__main__':
    tester = AutoTester(package_name="com.hmbdgames.match")
    tester.newbie()
    tester.touch_task_button()
