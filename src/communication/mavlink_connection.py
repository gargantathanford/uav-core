from pymavlink import mavutil

from src.communication.mavlink_parser import MAVLinkParser
from src.communication.connection_health import ConnectionHealth


class MAVLinkConnection:
    def __init__(self, connection_string="udpin:0.0.0.0:14550"):
        self.connection_string = connection_string
        self.connection = None
        self.parser = None
        self.health = ConnectionHealth()

    def connect(self):
        self.connection = mavutil.mavlink_connection(
            self.connection_string
        )

        print("Waiting for heartbeat...")
        heartbeat = self.connection.wait_heartbeat()

        self.health.record_heartbeat()

        print("Connected to vehicle")
        print(f"System ID: {self.connection.target_system}")
        print(f"Component ID: {heartbeat.get_srcComponent()}")

        self.parser = MAVLinkParser(self.connection)
        self.parser.parse_message(heartbeat)

    def update(self):
        if self.parser is None:
            raise RuntimeError(
                "MAVLink connection is not established"
            )

        message = self.connection.recv_msg()

        if message is None:
            return False

        if (
            message.get_type() == "HEARTBEAT"
            and message.get_srcSystem() == self.connection.target_system
            and message.autopilot
            == mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA
        ):
            self.health.record_heartbeat()

        self.parser.parse_message(message)

        return True

    @property
    def state(self):
        if self.parser is None:
            raise RuntimeError(
                "MAVLink connection is not established"
            )

        return self.parser.state
