class VehicleState:
    def __init__(self):
        # Flight state
        self.armed = False
        self.mode = "UNKNOWN"

        # Position
        self.latitude = None
        self.longitude = None
        self.altitude = None

        # Motion
        self.ground_speed = None

        # Attitude
        self.roll = None
        self.pitch = None
        self.yaw = None

        # Battery
        self.battery_voltage = None
        self.battery_remaining = None

    def __repr__(self):
        return (
            f"VehicleState("
            f"mode={self.mode}, "
            f"armed={self.armed}, "
            f"altitude={self.altitude}, "
            f"ground_speed={self.ground_speed})"
        )
