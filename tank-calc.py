
#This scrip takes 4 paramaters describing an open top cylindrical tank, it dose a bit of math and tell you how much 
# force would be exurted on the very bottom bolt or rivet that is holding seam in the tank together, the shearing strength
# of the fastener would need to be about 3 times the shear force exurted on it to be cosiderd safe as a peachy printer tank 
# as it will have repeated loadings put on it. 


def centimetersFromInches(inches):
    return(inches*2.54)



# change these variables:

centimetersPerFastener = 1.3 # use cm This is the distance between the center hole of each fastener in your seam of your tank in the hight direction. 

cercumference = centimetersFromInches(90.0) # use cm, the final cercumference of your tank ( after over laps of seams)

height = centimetersFromInches(96.0) # use cm, this is the Highes levle you will fill your tank to 

densityOfSatruatedSaltWater = 1.202 # use g/ml  or g/cubic-cm , this is for NaCl 

dollarsPerGramOfSalt =  5.0 / (20.0 * 1000.0) # use cad per gram .... ie  5 dolars / 20k grams 


import math





def diameterFromCercumference(cercumference):
    return(cercumference/math.pi)

def radiusFromDiameter(diameter):
    return(diameter/2)

def ariaFromRadius(radius):
    return(math.pi * radius *radius)

def volumeFromRadiusAndHeight(radius, height):
    return(math.pi * radius * radius * height)

def weightFromVolumeAndDensity(volume,density):  #needs units
    return(volume * density)

def hoopAriaPerFastenerFromDiameterAndCentimetersPerFastener(diameter,centimetersPerFastener):
    return(diameter * centimetersPerFastener)

def volumeAboveHoopAriaPerFastenerFromHoopAriaPerFastenerAndHeight(hoopAriaPerFastener, height):
    return(hoopAriaPerFastener * height)
    

def wieghtOnHoopAriaFromVolumeAboveHoopAriaPerFastenerAndDensity(volumeAboveHoopAriaPerFastener, density):
    return(volumeAboveHoopAriaPerFastener* density)

def shearForceFromWeightOnHoopAria(weightOnHoopAria):
    return(weightOnHoopAria/2)

def poundsFromGrams(grams):
    return(grams*.00220462)

def massOfSalt(weight):
    return(weight*.26)

def costOfSalt(massOfSalt, dollarsPerGramOfSalt):
    return(massOfSalt * dollarsPerGramOfSalt)



diameter = diameterFromCercumference(cercumference) # cm

radius = radiusFromDiameter(diameter) #cm

hoopAriaPerFastener = hoopAriaPerFastenerFromDiameterAndCentimetersPerFastener(diameter,centimetersPerFastener) #cm

aria = ariaFromRadius(radius) # cm squar

volume = volumeFromRadiusAndHeight(radius, height) # cm cubed == ml 

weight = weightFromVolumeAndDensity(volume, densityOfSatruatedSaltWater) # 1ml of water is 1 gram of weight

volumeAboveHoopAriaPerFastener = volumeAboveHoopAriaPerFastenerFromHoopAriaPerFastenerAndHeight(hoopAriaPerFastener, height) # cm qubed

weightOnHoopAria = wieghtOnHoopAriaFromVolumeAboveHoopAriaPerFastenerAndDensity(volumeAboveHoopAriaPerFastener, densityOfSatruatedSaltWater)  # retruns in grams 

shearForce = shearForceFromWeightOnHoopAria(weightOnHoopAria)  # return in grams

massOfSalt = massOfSalt(weight)

costOfSalt = costOfSalt(massOfSalt, dollarsPerGramOfSalt)

print cercumference, ' cercumference in cm'
print height, ' height in cm'
print densityOfSatruatedSaltWater, ' densityOfSatruatedSaltWater in g/ml or g/cubic-cm'
print diameter, ' diameter in cm'
print radius, ' radius in cm'
print aria, ' aria in cm square'
print volume, ' volume in ml or cubic cm'
print weight, ' weight or mass in grams'
print hoopAriaPerFastener, ' hoopAriaPerFastener in cm square'
print volumeAboveHoopAriaPerFastener, ' volumeAboveHoopAriaPerFastener in cm qubed'
print weightOnHoopAria, ' weightOnHoopAria in grams'
print shearForce, ' shearForce in grams'
print poundsFromGrams(shearForce), ' shear force in pounds'
print shearForce/1000, ' shear force in kg'
print massOfSalt, ' massOfSalt in grams'
print costOfSalt, ' cost of total salt needed to saturate full tank in dollars'



# some extra notes:

# ugg why int this open...  http://steelfinder.outokumpu.com/v3/StorageTank.aspx

#goals are shear per height 
#psi at at bottom 
#volume of water
#amout of salt needed. 

# http://moodlearn.ariel.ac.il/pluginfile.php/456055/mod_resource/content/0/pressure_vessels_1_.pdf
#http://en.wikipedia.org/wiki/Brine

# http://www.homedepot.ca/product/20-kg-crystal-plus-water-softener-salt/966409


