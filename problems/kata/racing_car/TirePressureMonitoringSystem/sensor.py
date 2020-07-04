import random
from typing import Union

from abc import ABC, abstractmethod


class AbstractSensor(ABC):
    @abstractmethod
    def pop_next_pressure_psi_value(self):
        pass


class Sensor(AbstractSensor):
    # The reading of the pressure value from the sensor is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET = 16

    def pop_next_pressure_psi_value(self) -> Union[int, float]:
        pressure_telemetry_value = self.sample_pressure()
        return self._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_pressure() -> Union[int, float]:
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value
