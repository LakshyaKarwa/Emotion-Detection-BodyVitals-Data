import numpy as np
import pandas as pd
import math

"""

N = 10 (all cases) (10 readings)

ALSC
sumALSC = 0
ALSC = (sum from n = 2 to N) sqrt(1 + pow((r[n] + r[n-1]), 2))

for i in range(1, 10):
   sumALSC = sumALSC + math.sqrt(1 + pow((r[i] + r[i-1]), 2))  


INSC
sumINSC = 0
INSC = (sum from n = 1 to N) magnitude(r[n])

for i in range(0, 10):
    sumINSC = sumINSC + abs(r[n])


APSC
sumAPSC = 0
finalAPSC = 0
APSC = 1/N * (sum from n = 1 to N) math.pow(r[n], 2)

for i in range(0, 10):
    sumAPSC = sumAPSC + math.pow(r[n], 2)

finalAPSC = (1/N)(sumAPSC)

RMSC

finalRMSC = math.sqrt(finalAPSC)
"""

df = pd.read_csv("sample_data.csv")

# Working on Human Resistance instead of actual GSR Values

"""
human_resistance = ((1024 + 2*gsr_average)*10000) / (659  - gsr_average)
"""

# Applying the above transformation on the GSR Values to obtain actual Human Resitance
df['GSR'] = ((1024 + 2*df['GSR'])*10000) /  (659 - df['GSR'])

listResistance = df['GSR'].tolist()


##############################################################################################
"""                                         ALSC                                           """                                            
##############################################################################################
ALSC = 0
# ALSC = (sum from n = 2 to N) sqrt(1 + pow((r[n] + r[n-1]), 2))

for i in range(1, 10):
   ALSC = ALSC + math.sqrt(1 + pow((listResistance[i] + listResistance[i-1]), 2))  
   

##############################################################################################
"""                                         INSC                                           """                                            
##############################################################################################

INSC = 0
# INSC = (sum from n = 1 to N) magnitude(r[n])

for i in range(0, 10):
    INSC = INSC + abs(listResistance[i])


##############################################################################################
"""                                         APSC                                           """                                            
##############################################################################################

sumAPSC = 0
finalAPSC = 0
# APSC = 1/N * (sum from n = 1 to N) math.pow(r[n], 2)

for i in range(0, 10):
    sumAPSC = sumAPSC + math.pow(listResistance[i], 2)

APSC = (1/10)*(sumAPSC)    
    

##############################################################################################
"""                                         RMSC                                           """                                            
##############################################################################################

RMSC = math.sqrt(APSC)


""" FINAL RESULTS """
print(ALSC)
print(APSC)
print(INSC)
print(RMSC)
