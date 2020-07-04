from sensor import Sensor, AbstractSensor


class Alarm:
    def __init__(
            self, sensor: AbstractSensor = None
            , low_threshold: float = 17.0, high_threshold: float = 21.0
    ):
        self._low_pressure_threshold = low_threshold
        self._high_pressure_threshold = high_threshold
        if sensor is None:
            self._sensor = Sensor()
        else:
            self._sensor = sensor
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        if self._high_pressure_threshold < psi_pressure_value \
                or psi_pressure_value < self._low_pressure_threshold:
            self._is_alarm_on = True
        else:
            self._is_alarm_on = False

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
