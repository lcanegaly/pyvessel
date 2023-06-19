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
    def mole(self, total_molar_quantity: float):
        """Sets molar volume by changing moles per volume. Solves for pressure.
        """
        self.state.moles = total_molar_quantity
        self.state.pressure = ideal_gas.pressure(self.state.volume,
                                                 self.state.moles,
                                                 self.state.temperature)

    def transfer(self, volume_m3: float):
        """Transfers gas by volume into or out of vessel. Solves for pressure.
        """
        moles_transfered = ideal_gas.moles(self.pressure, volume_m3,
                                           self.temperature)
        self.mole += moles_transfered

    def __repr__(self):
        return textwrap.dedent('''\
                <Vessel Pressure Pa:{} | Volume_m3:{} | Temperature_c:{}'''\
                ''' | moles:{}>'''.format(
                    self.pressure - ideal_gas.BARO_PRESSURE,
                    self.volume,
                    ideal_gas.kelvin_to_celcius(self.temperature),
                    self.mole))


def test():
    #create a test vessel of 1m3 at 0C and check for correct outputs
    v = Vessel(1.0, 0.0)
    volume = v.volume
    temperature = v.temperature
    pressure = v.pressure
    moles = v.mole
    assert volume == 1.0
    assert temperature == 273.15
    assert moles == 44.61503340547032
    assert pressure == 101325.0
    print(v)

if __name__ == '__main__':
    test()
