"""Ideal gas law constants and formulas"""

GAS_CONSTANT = 8.31446261815324
BARO_PRESSURE = 101325.0
LITER_PER_MOLE = 22.413969545014
MOLE_PER_M3 = 1000/LITER_PER_MOLE

def celsius_to_kelvin(c: float) -> float:
    return c + 273.15

def pressure(cubic_meter_volume: float,
             total_moles: float, temperature_kelvin: float) -> float:
    #p = nRT/V
    nrt = total_moles * GAS_CONSTANT * temperature_kelvin
    v = cubic_meter_volume
    return nrt/v

def temperature(pressure_pascal: float, cubic_meter_volume: float,
                total_moles: float) -> float:
    #T = pV/nR
    pv = pressure_pascal * cubic_meter_volume
    nr = total_moles * GAS_CONSTANT
    return pv/nr

def moles(pressure_pascal: float, cubic_meter_volume: float,
          temperature_kelvin: float) -> float:
    #n = pV/RT
    pv = pressure_pascal * cubic_meter_volume
    rt = GAS_CONSTANT * temperature_kelvin
    return pv/rt

def test():
    v = 1.0
    t = celsius_to_kelvin(0)
    m = MOLE_PER_M3
    p = BARO_PRESSURE
    print(f'inputs: {v=}, {t=}, {m=}, {p=}')
    print('pressure pa: ', pressure(v, m, t))
    print('temperature k: ', temperature(p, v, m))
    print('moles: ', moles(p, v, t))

if __name__ == '__main__':
    test()




