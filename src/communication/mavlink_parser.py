from pymavlink import mavutil
from src.vehicle.state import VehicleState


class MAVLinkParser:
    def __init__(self, connection):
        self.connection = connection
        self.state = VehicleState()

    def update(self):
        message = self.connection.recv_msg()

        if message is None:
            return False

        self.parse_message(message)
        return True

    def parse_message(self, message):
        message_type = message.get_type()

        if message_type == "HEARTBEAT":
            self._parse_heartbeat(message)

        elif message_type == "GLOBAL_POSITION_INT":
            self._parse_position(message)

        elif message_type == "ATTITUDE":
            self._parse_attitude(message)

        elif message_type == "VFR_HUD":
            self._parse_vfr_hud(message)

        elif message_type == "SYS_STATUS":
            self._parse_system_status(message)

    def _parse_heartbeat(self, message):
        self.state.armed = bool(
            message.base_mode
            & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
        )

        self.state.mode = mavutil.mode_string_v10(message)

    def _parse_position(self, message):
        self.state.latitude = message.lat / 1e7
        self.state.longitude = message.lon / 1e7
        self.state.altitude = message.relative_alt / 1000.0

    def _parse_attitude(self, message):
        self.state.roll = message.roll
        self.state.pitch = message.pitch
        self.state.yaw = message.yaw

    def _parse_vfr_hud(self, message):
        self.state.ground_speed = message.groundspeed

    def _parse_system_status(self, message):
        self.state.battery_voltage = (
            message.voltage_battery / 1000.0
        )
        self.state.battery_remaining = message.battery_remaining
