"""
Dependency inversion: add an abstraction
Liskov sub: added a contract
Cannot interchange which alarm goes with which sensor
"""
import unittest
from unittest.mock import Mock, patch
from tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):
    def setUp(self) -> None:
        self._mock_sensor = Mock()
        self._alarm = Alarm(self._mock_sensor)

    def tearDown(self) -> None:
        del self._mock_sensor
        del self._alarm

    def test_alarm_is_off_by_default(self):
        self.assertEqual(self._alarm.is_alarm_on, False)

    def test_value(self):
        self._mock_sensor.pop_next_pressure_psi_value.return_value = 19
        self._alarm.check()
        self.assertEqual(self._alarm.is_alarm_on, False)

        self._mock_sensor.pop_next_pressure_psi_value.return_value = 16
        self._alarm.check()
        self.assertEqual(self._alarm.is_alarm_on, True)

        self._mock_sensor.pop_next_pressure_psi_value.return_value = 19
        self._alarm.check()
        self.assertEqual(self._alarm.is_alarm_on, False)

        self._mock_sensor.pop_next_pressure_psi_value.return_value = 25
        self._alarm.check()
        self.assertEqual(self._alarm.is_alarm_on, True)

        self._mock_sensor.pop_next_pressure_psi_value.return_value = 19
        self._alarm.check()
        self.assertEqual(self._alarm.is_alarm_on, False)

    def test_no_arg(self):
        with patch("tire_pressure_monitoring.Sensor") as mock_sensor:
            mock_sensor.return_value = 5
            temp_alarm = Alarm()
            self.assertEqual(temp_alarm._sensor, 5)
