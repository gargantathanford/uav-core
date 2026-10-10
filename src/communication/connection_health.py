import time


class ConnectionHealth:
    def __init__(self, heartbeat_timeout=3.0):
        self.heartbeat_timeout = heartbeat_timeout
        self.last_heartbeat = None

    def record_heartbeat(self):
        self.last_heartbeat = time.monotonic()

    @property
    def connected(self):
        if self.last_heartbeat is None:
            return False

        elapsed = time.monotonic() - self.last_heartbeat
        return elapsed < self.heartbeat_timeout

    @property
    def seconds_since_heartbeat(self):
        if self.last_heartbeat is None:
            return None

        return time.monotonic() - self.last_heartbeat
