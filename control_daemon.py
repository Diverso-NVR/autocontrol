import time

import schedule

from cameras_control import call_default_preset
from models import Room, Session


class AutoControlApp:
    rooms = None

    def __init__(self):
        schedule.every(2).minutes.do(self.call_default_presets)

    def call_default_presets(self):
        session = Session()
        self.rooms = session.query(Room).all()
        session.close()

        for room in self.rooms:
            if room.auto_control:
                for source in room.sources:
                    call_default_preset(source.ip, source.port)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


auto_control_app = AutoControlApp()
auto_control_app.run()
