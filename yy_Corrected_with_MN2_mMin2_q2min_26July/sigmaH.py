import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi
wvalue = np.linspace(10, 1000, 300)


def cs_higgs_w(wvalue):
    re = 2.8179403262e-15 * 137.0 / 128.0
    me = 0.510998950e-3
    MH = 125.0
    G  = 4.2e-3
    Gyy = (2.27e-3)*(4.2e-3)
    hbarc2 =  0.389
    alpha2 = (1.0/137.0)*(1.0/137.0)

    # if wvalue > MH:
    cs = (8. * np.pi * np.pi* hbarc2 ) * (Gyy / MH)* (1./ np.pi) * \
         ( (MH *G)/((MH*MH - wvalue*wvalue)*(MH*MH-wvalue*wvalue) + MH*MH*G*G)) * 1e9
    # else:
    #     cs = 0.

    return cs

# Calculate y values using sin function
y = cs_higgs_w(wvalue)

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(wvalue, y)

ax.set_yscale("log")

# Customize the plot
ax.set_xlabel('wvalue')
ax.set_ylabel('cs_higgs_w')
ax.set_title('Plot of cs_higgs_w')

# Save the plot as a PDF file
plt.savefig('cs_higgs_w_plot.pdf')

# Show the plot
plt.show()
