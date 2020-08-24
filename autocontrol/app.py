import time
import schedule

from core.cameras_control import goto_home_position
from core.db.models import Room, Session


class AutoControlApp:
    rooms = None

    def __init__(self):
        schedule.every(2).minutes.do(self.call_default_presets)
        schedule.every().day.at("00:00").do(self.set_autocontrol_true)

    def call_default_presets(self):
        session = Session()
        self.rooms = session.query(Room).all()
        session.close()

        for room in self.rooms:
            if not room.auto_control:
                continue

            for source in room.sources:
                try:
                    goto_home_position(source.ip, source.port)
                except Exception as e:
                    print(
                        f"Error while moving {source.ip} to home position:", e)

    def set_autocontrol_true(self):
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
    auto_control_app.run()
