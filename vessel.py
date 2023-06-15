"""A class which represents a pressure vessel."""
from dataclasses import dataclass
import textwrap
import ideal_gas

@dataclass
class State:
    """A state object for Vessel"""
    pressure: float
    volume: float
    temperature: float
    moles: float

class Vessel:
    """Container of gas, to which volume, temp, and pressure can be modified"""
    def __init__(self, volume: float, temperature_c: float):
        self.state = State(0, volume, 0, 0)
        self.state.temperature = ideal_gas.celsius_to_kelvin(temperature_c)
        self.pressure = ideal_gas.BARO_PRESSURE

    @property
    def volume(self):
        return self.state.volume

    @volume.setter
    def volume(self, volume: float):
        """Sets volume of vessel and solves for pressure."""
        self.state.volume = volume
        self.state.pressure = ideal_gas.pressure(self.state.volume,
                                                 self.state.moles,
                                                 self.state.temperature)

    @property
    def pressure(self):
        return self.state.pressure

    @pressure.setter
    def pressure(self, pressure: float):
        """Sets pressure of vessel and solves for moles of gas"""
        self.state.pressure = pressure
        self.state.moles = ideal_gas.moles(self.state.pressure,
                                           self.state.volume,
                                           self.state.temperature)

    @property
    def temperature(self):
        return self.state.temperature

    @temperature.setter
    def temperature(self, temperature_c: float):
        """Sets temperature of vessel and solves for pressure."""
        self.state.temperature = ideal_gas.celsius_to_kelvin(temperature_c)
        self.state.pressure = ideal_gas.pressure(self.state.volume,
                                                 self.state.moles,
                                                 self.state.temperature)

    @property
    def mole(self):
        return self.state.moles

    @mole.setter
    def mole(self, changed_mole_amount: float):
        self.state.moles = changed_mole_amount
        self.state.pressure = ideal_gas.pressure(self.state.volume,
                                                  self.state.moles,
                                                  self.state.temperature)


        
    def __repr__(self):
        return textwrap.dedent('''\
                <Vessel pressure_pa:{}, 
                volume_m3:{}, temperature_k:{}, moles:{}>'''.format(
                    self.state.pressure - ideal_gas.BARO_PRESSURE,
                    self.state.volume,
                    self.state.temperature,
                    self.state.moles))


def test():
    #create a test vessel of 1m3 at 0C and check for correct outputs
    v = Vessel(1.0, 0.0)
    volume = v.state.volume
    temperature = v.state.temperature
    pressure = v.state.pressure
    moles = v.state.moles
    assert volume == 1.0
    assert temperature == 273.15
    assert moles == 44.61503340547032
    assert pressure == 101325.0
    print(v)

def pressurize(step):
    flow_rate = ideal_gas.moles(ideal_gas.BARO_PRESSURE, 0.1,
                                ideal_gas.celsius_to_kelvin(21))
    v = Vessel(100.0, 0.0)
    for i in range(10):
        v.mole = v.mole + flow_rate
        print(v)

if __name__ == '__main__':
    pressurize(10)
