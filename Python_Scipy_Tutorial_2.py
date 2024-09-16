# Constants in scipy: scipy is more focused on scientific impelementions, it provides many built in scientific constants: helpful in data science.
# printing the constant value of PI:
from scipy import constants
print(constants.pi)  # 3.141592653589793

# Constants Units: # Constants unit:  all list of unit under the constant can be seen with dir

from scipy import constants
print(dir(constants))   

# Unit Categories: Metric, Binary, Mass, Angle, Time, Length, Pressure, Volume, Speed, Temprature, Energy, Power, Force.

# Metric (SI) Prefixes: 
from scipy import constants

print(constants.yotta) # 1e+24
print(constants.zetta) # 1e+21
print(constants.exa) # 1e+18
print(constants.peta) # 1000000000000000.0
print(constants.tera) # 10000000000000.0
print(constants.giga) # 1000000000.0
print(constants.mega) # 1000000.0
print(constants.kilo) # 1000.0
print(constants.hecto) # 100.0
print(constants.deka) # 10.0
print(constants.deci) # 0.1
print(constants.centi) # 0.01
print(constants.milli) # 0.001
print(constants.micro) # 1e-06
print(constants.nano) # 1e-09
print(constants.pico) # 1e-12
print(constants.femto) # 1e-15
print(constants.atto) # 1e-18
print(constants.zepto) # 1e-21

# Binary Prefixes: 
from scipy import constants
print(constants.kibi) # 1024
print(constants.mebi) # 1048576
print(constants.gibi) # 1073741824
print(constants.tebi) # 1099511627776
print(constants.pebi) # 1125899906842624
print(constants.exbi) # 1152921504606846976
print(constants.zebi) # 1180591620717411303424
print(constants.yobi) # 1208925819614629174706176


# MASS: 
from scipy import constants
print(constants.gram) # 0.001
print(constants.metric_ton) # 1000.0
print(constants.grain) # 6.479891e-05
print(constants.lb) # 0.45359236999999997
print(constants.pound) # 0.45359236999999997
print(constants.oz) # 0.028349523124999998
print(constants.ounce) # 0.028349523124999998
print(constants.stone) # 6.3502931799999995
print(constants.long_ton) # 1016.0469088
print(constants.short_ton) # 907.1847399999999
print(constants.troy_ounce) # 0.031103476799999998
print(constants.troy_pound) # 0.37324172159999996
print(constants.carat) # 0.0002
print(constants.atomic_mass) # 1.6605390666e-27
print(constants.m_u) # 1.6605390666e-27
print(constants.u) # 1.6605390666e-27


# Angle:
from scipy import constants
print(constants.degree) # 0.0174
print(constants.arcmin)
print(constants.arcminute) # 0.0002
print(constants.arcsec)
print(constants.arcsecond)

# Time:
from scipy import constants
print(constants.minute) # 60.0
print(constants.hour) # 3600
print(constants.day) 
print(constants.week)
print(constants.year)
print(constants.Julian_year)

# length
from scipy import constants
print(constants.inch) # 0.0254
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.mil)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.micron)
print(constants.au)
print(constants.astronomical_unit)
print(constants.light_year)
print(constants.parsec)

# Pressure: pascals
from scipy import constants
print(constants.atm)
print(constants.atmosphere)
print(constants.bar)
print(constants.torr)
print(constants.mmHg) 
print(constants.psi)

# Volume: cubic meter
from scipy import constants
print(constants.liter) # 0.001
print(constants.litre) # 0.001
print(constants.gallon)
print(constants.gallon_US)
print(constants.gallon_imp)
print(constants.fluid_ounce)
print(constants.fluid_ounce_US)
print(constants.fluid_ounce_imp)
print(constants.barrel)
print(constants.bbl)

# speed: meter per sec
from scipy import constants
print(constants.kmh) # 0.27777777
print(constants.mph)
print(constants.mach) # 340.5
print(constants.speed_of_sound) # 340.5
print(constants.knot)

# Temprature: kelvin
from scipy import constants
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)

# Energy: joules
from scipy import constants
print(constants.eV)
print(constants.electron_volt)
print(constants.calorie) # 4.184
print(constants.calorie_th) # 4.184
print(constants.calorie_IT)
print(constants.erg) # 07
print(constants.Btu)
print(constants.Btu_IT)
print(constants.Btu_th)
print(constants.ton_TNT)
# Power : newton
from scipy import constants
print(constants.dyn)
print(constants.dyne)
print(constants.lbf)
print(constants.pound_force)
print(constants.kgf)
print(constants.kilogram_force)

