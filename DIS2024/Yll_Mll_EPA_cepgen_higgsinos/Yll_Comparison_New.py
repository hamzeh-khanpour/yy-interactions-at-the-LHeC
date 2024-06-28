

import ROOT
import numpy as np
import matplotlib.pyplot as plt


# Import data from the custom module
from dSigmadY_10_100_100_higgsinos_MN100 import wvalues, elas, inel


# Matplotlib configuration for publication-quality plots
plt.rcParams["axes.linewidth"] = 1.8
plt.rcParams["xtick.major.width"] = 1.8
plt.rcParams["xtick.minor.width"] = 1.8
plt.rcParams["ytick.major.width"] = 1.8
plt.rcParams["ytick.minor.width"] = 1.8
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["legend.fontsize"] = 15
plt.rcParams['legend.title_fontsize'] = 'x-large'


# Constants
integrated_cross_section_value_E = 1.01516903e-03  # pb
integrated_cross_section_value_QE = 9.35686193e-04  # pb
bin_width_correction = 10.0


def compare_distributions(filename):
    """
    Compare the distributions of Yll from two different TTrees in a ROOT file.

    Args:
        filename (str): The path to the ROOT file.
    """
    # Open the ROOT file
    file = ROOT.TFile(filename)
    if file.IsZombie():
        print("Error: Could not open file", filename)
        return

    # Get the TTree objects
    tree_E = file.Get("LHeC_E")
    tree_QE = file.Get("LHeC_QE")
    if not tree_E or not tree_QE:
        print("Error: Could not retrieve TTrees from the file")
        file.Close()
        return


    # Create arrays to hold Yll values
    Yll_E = []
    Yll_QE = []


    # Fill arrays with Yll values
    for event in tree_E:
        Yll_E.append(event.Yll)
    for event in tree_QE:
        Yll_QE.append(event.Yll)


    # Close the ROOT file
    file.Close()

    # Create histograms using numpy
    bins = np.linspace(0, 10, 101)
    hist_Yll_E, _ = np.histogram(Yll_E, bins=bins, weights=[bin_width_correction * integrated_cross_section_value_E / len(Yll_E)] * len(Yll_E))
    hist_Yll_QE, _ = np.histogram(Yll_QE, bins=bins, weights=[bin_width_correction * integrated_cross_section_value_QE / len(Yll_QE)] * len(Yll_QE))
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    DX = abs(bins[:-1] - bins[1:])



    # Load Yll data from Matplotlib
    Yll_MPL = wvalues[3][:303]
    elas_MPL = elas[3][:303]
    inel_MPL = inel[3][:303]



    # Plotting with Matplotlib
    fig, ax = plt.subplots(figsize=(9.0, 8.0))
    ax.set_xlim(0.0, 5.0)
    ax.set_ylim(1.e-6, 1.e-3)



    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    # Plot graphs from Matplotlib data
    ax.plot(Yll_MPL, elas_MPL, linestyle='solid', linewidth=2, color='blue', label='elastic (EPA)')
    ax.plot(Yll_MPL, inel_MPL, linestyle='dashed', linewidth=2, color='red', label='inelastic (EPA)')

    # Plot histograms
    ax.plot(bin_centers, hist_Yll_E, marker='.', linestyle='None', linewidth=2, color='magenta', label='elastic (cepgen)')
    ax.plot(bin_centers, hist_Yll_QE, marker='.', linestyle='None', linewidth=2, color='green', label='inelastic (cepgen)')



    # Set labels and title
    font2 = {'family':'serif', 'color':'black', 'size':24}
    ax.set_xlabel(r'$Y_{higgsinos}$', fontdict=font2)
    ax.set_ylabel(r'$d\sigma/dY_{higgsinos} \, [pb]$', fontdict=font2)



    # Add legend
    inel_label = ('$M_N<$ ${{{:g}}}$ GeV').format(inel[0]) + (' ($Q^2_p<$ ${{{:g}}}$ GeV$^2$)').format(inel[2])
    title_label = ('$Q^2_e<$ ${{{:g}}}^{{{:g}}}$ GeV$^2$').format(10, np.log10(inel[1]))
    ax.legend(title=title_label, loc='upper right', fontsize=15)



    # Add text annotations
    info_text_1 = r"LHeC ($E_{e}=50$ GeV; $E_{p}=7000$ GeV)"
    ax.text(0.05, 0.95, info_text_1, transform=ax.transAxes, fontsize=15, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.0))
    info_text_2 = r"$Q^2_p<10^2$ GeV$^2$; $M_N<10$ GeV"
    ax.text(0.05, 0.88, info_text_2, transform=ax.transAxes, fontsize=15, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.0))
    info_text_3 = r"$M_{higgsino}$ = 100 GeV"
    ax.text(0.05, 0.78, info_text_3, transform=ax.transAxes, fontsize=15, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.0))


# $Q^2_e<10^2$ GeV$^2$;

    # Save the plot as a PDF and JPG file
    plt.savefig("Yll_Comparison_higgsinos_DIS2024_New.pdf")
#    plt.savefig("Yll_Comparison_higgsinos_DIS2024_New.jpg")


    # Show the plot
    plt.show()

    # Calculate area under the curve for each distribution
    area_Yll_E = np.sum(hist_Yll_E) / bin_width_correction
    area_Yll_QE = np.sum(hist_Yll_QE) / bin_width_correction
    area_Yll_MPL_elastic = np.trapz(elas_MPL, Yll_MPL)
    area_Yll_MPL_inelastic = np.trapz(inel_MPL, Yll_MPL)



    print("Area under the curve for Yll (elastic (cepgen)):", area_Yll_E)
    print("Area under the curve for Yll (inelastic (cepgen)):", area_Yll_QE)
    print("Area under the curve for Yll (elastic (EPA)):", area_Yll_MPL_elastic)
    print("Area under the curve for Yll (inelastic (EPA)):", area_Yll_MPL_inelastic)


# Call the function with the filename of the ROOT file
compare_distributions("LHeC_higgsino_Compare.root")


