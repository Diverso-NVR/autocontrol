import time

import schedule

from cameras_control import goto_home_position
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
                    try:
                        goto_home_position(source.ip, source.port)
                    except Exception as e:
                        print(e)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


auto_control_app = AutoControlApp()
auto_control_app.run()
