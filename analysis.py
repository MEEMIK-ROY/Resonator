import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'S22'

#..........................................................................................................

#For Single Peak
#Magnitude-Phase
s1 = pd.read_csv(f"{filename}1PMP.csv", sep=";")
s1.drop(s1.columns[len(s1.columns)-1], axis=1, inplace=True)

#PLot magnitude
fig1=plt.figure(figsize=(10,8))
plt.plot(s1.iloc[:,0], s1.iloc[:,1])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Mag({filename}) dB')
plt.title(f"{filename} Magnitude")
fig1.savefig(f"./plots/{filename}/SinglePeak/{filename}mag.png")

#PLot phase
fig2=plt.figure(figsize=(10,8))
plt.plot(s1.iloc[:,0], s1.iloc[:,2])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Angle({filename})(degrees)')
plt.title(f"{filename} Phase")
fig2.savefig(f"./plots/{filename}/SinglePeak/{filename}phase.png")


#For Real Imaginary
s2 = pd.read_csv(f"{filename}1PRI.csv", sep=";")
s2.drop(s2.columns[len(s2.columns)-1], axis=1, inplace=True)

#PLot Real
fig3=plt.figure(figsize=(10,8))
plt.plot(s2.iloc[:,0], s2.iloc[:,1])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Real({filename}) dB')
plt.title(f"Real {filename}")
fig3.savefig(f"./plots/{filename}/SinglePeak/{filename}real.png")

#PLot Imaginary
fig4=plt.figure(figsize=(10,8))
plt.plot(s2.iloc[:,0], s2.iloc[:,2])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Img({filename}) dB')
plt.title(f"Imaginary {filename}")
fig4.savefig(f"./plots/{filename}/SinglePeak/{filename}img.png")

#.........................................................................................................


#For full range
#Magnitude-Phase
s1_1 = pd.read_csv(f"{filename}2PMP.csv", sep=";")
s1_1.drop(s1_1.columns[len(s1_1.columns)-1], axis=1, inplace=True)

#PLot magnitude
fig1_1=plt.figure(figsize=(10,8))
plt.plot(s1_1.iloc[:,0], s1_1.iloc[:,1])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Mag({filename}) dB')
plt.title(f"{filename} Magnitude")
fig1_1.savefig(f"./plots/{filename}/FullRange/{filename}fullrangemag.png")

#PLot phase
fig2_1=plt.figure(figsize=(10,8))
plt.plot(s1_1.iloc[:,0], s1_1.iloc[:,2])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Angle({filename})(degrees)')
plt.title(f"{filename} Phase")
fig2_1.savefig(f"./plots/{filename}/FullRange/{filename}fullrangephase.png")


#For Real Imaginary
s2_1 = pd.read_csv(f"{filename}2PRI.csv", sep=";")
s2_1.drop(s2_1.columns[len(s2_1.columns)-1], axis=1, inplace=True)

#PLot Real
fig3_1=plt.figure(figsize=(10,8))
plt.plot(s2_1.iloc[:,0], s2_1.iloc[:,1])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Real({filename}) dB')
plt.title(f"Real {filename}")
fig3_1.savefig(f"./plots/{filename}/FullRange/{filename}fullrangereal.png")

#PLot Imaginary
fig4_1=plt.figure(figsize=(10,8))
plt.plot(s2_1.iloc[:,0], s2_1.iloc[:,2])
plt.xlabel("Frequency (GHz)")
plt.ylabel(f'Img({filename}) dB')
plt.title(f"Imaginary {filename}")
fig4_1.savefig(f"./plots/{filename}/FullRange/{filename}fullrangeimg.png")
