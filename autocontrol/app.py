import logging
import time

import schedule

from core.cameras_control import goto_home_position
from core.db.models import Room, Source


class AutoControlApp:
    logger = logging.getLogger('autocontrol_logger')

    def __init__(self):
        self.logger.info('Class \"AutoControlApp\" instantiated')

        schedule.every(2).minutes.do(self.call_default_presets)
        schedule.every().day.at("00:00").do(self.set_autocontrol_true)

    def call_default_presets(self):
        self.logger.info('Setting all cameras to default positions')

        rooms = [
            Room(name='1', auto_control=True, sources=[
                Source(ip='172.18.130.40', port="544"),
                Source(ip='172.18.130.41', port="544"),
            ]),
            Room(name='2',auto_control=True, sources=[
                Source(ip='172.18.130.30', port="544"),
                Source(ip='172.18.130.31', port="544"),
            ])
        ]

        for room in rooms:
            if not room.auto_control:
                continue

            for source in room.sources:
                try:
                    # goto_home_position(source.ip, source.port)
                    self.logger.info(f'Moving device {source.ip}:{source.port} to home position')
                    time.sleep(1)
                    self.logger.info(f"Successfully moved device {source.ip}:{source.port} to home position")
                except Exception:
                    self.logger.error(f'Error while setting device {source.ip}:{source.port} to home position',
                                      exc_info=True)

    def set_autocontrol_true(self):
        self.logger.info('Setting automatic cameras control on every room')

        # session = Session()
        # rooms = session.query(Room).all()

        # for room in rooms:
        #     room.auto_control = True

        # session.commit()
        # session.close()

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    @staticmethod
    def create_logger(mode='INFO'):
        logs = {'INFO': logging.INFO,
                'DEBUG': logging.DEBUG}

        logger = logging.getLogger('autocontrol_logger')
        logger.setLevel(logs[mode])

        handler = logging.StreamHandler()
        handler.setLevel(logs[mode])

        formatter = logging.Formatter(
            '%(levelname)-8s  %(asctime)s    %(message)s',
            datefmt='%d-%m-%Y %I:%M:%S %p')

        handler.setFormatter(formatter)

        logger.addHandler(handler)


if __name__ == "__main__":
    AutoControlApp.create_logger()

    auto_control_app = AutoControlApp()
    auto_control_app.call_default_presets()
    auto_control_app.run()
