import logging
import time

import schedule

from core.cameras_control import goto_nvr_preset
from core.db.models import Room, Session


class AutoControlApp:
    def __init__(self):
        self.logger = logging.getLogger('autocontrol_logger')
        self.logger.info('Class \"AutoControlApp\" instantiated')

        self.room = None

        schedule.every(2).minutes.do(self.call_default_presets)
        schedule.every().day.at("00:00").do(self.set_autocontrol_true)

    def call_default_presets(self):
        self.logger.info('Setting all cameras to default positions')

        session = Session()
        self.rooms = session.query(Room).all()
        session.close()

        for room in self.rooms:
            if not room.auto_control:
                continue

            for source in room.sources:
                ip = source.ip
                port = source.port
                try:
                    self.logger.info(f'Moving device {ip}:{port}')
                    goto_nvr_preset(ip, port)
                except Exception as err:
                    self.logger.error(f'Error while setting device {ip}:{port}')

    def set_autocontrol_true(self):
        self.logger.info('Setting automatic cameras control on every room')

        session = Session()
        self.rooms = session.query(Room).all()

        for room in self.rooms:
            room.auto_control = True

        session.commit()
        session.close()

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)



if __name__ == "__main__":
    auto_control_app = AutoControlApp()
    auto_control_app.call_default_presets()
    auto_control_app.run()
