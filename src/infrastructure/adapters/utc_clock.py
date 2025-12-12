from datetime import datetime, timezone
from src.application.ports.clock import Clock


class UTCClock(Clock):
    def now(self) -> datetime:
        return datetime.now(timezone.utc)