from math import *

mm    = 1
meter = 1000 * mm
nsec  = 1
um    = 10**-3 * mm
usec  = 1000*nsec
sec   = 1000000000 * nsec
c     = 300 * mm/nsec
MeV   = 1
MeVc2 = MeV / c**2
eV    = 10**-6 * MeV
kg    = 5.6096*10**29  #unit in MeV/c^2

#The apparent issue is that the initial velocity of the electron is high compared to the
#size of the channel thus every next hit will cause an issue.
