import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("resources/DrillingData.csv")

fig, axs = plt.subplots(ncols = 1, nrows = 9, figsize = (10, 20), layout = "constrained")

data.plot(x="Depth", y="Flow In Rate (galUS/min)", ax = axs[0])
data.plot(x="Depth", y="Pump Pressure (psi)", ax = axs[1])
data.plot(x="Depth", y="Diff Press (psi)", ax = axs[2])
data.plot(x="Depth", y="Top Drive RPM (RPM)", ax = axs[3])
data.plot(x="Depth", y="ROP - Average (ft/hr)", ax = axs[4])
data.plot(x="Depth", y="Bit Weight (klb)", ax = axs[5])
data.plot(x="Depth", y="Top Drive Torque (ft·lbf)", ax = axs[6])
data.plot(x="Depth", y="Block Height (ft)", ax = axs[7])
data.plot(x="Depth", y="Hook Load (klb)", ax = axs[8])

