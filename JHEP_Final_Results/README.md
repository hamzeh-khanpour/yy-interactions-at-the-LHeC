# Photon Luminosity Spectrum and tau-tau Production Cross-Section Calculation at the LHeC
# AGH University of Krakow

## Overview

This repository contains Python scripts for calculating the **elastic/inelastic photon-photon luminosity spectrum** ($S_{\gamma\gamma}$) and 
the **tau-tau production cross-section** for the process $ep \rightarrow e (\gamma\gamma \rightarrow \tau^+\tau^-) p^{(*)}$. 

## Features

- **Photon-Photon Luminosity Spectrum Calculation** ($S_{\gamma\gamma}$):
  - Computes $S_{\gamma\gamma}$ for a range of center-of-mass energies `W`.
  - Allows flexibility for analyzing dimuon or Higgsinos production cross-sections as well. 
  
- **Tau-Tau Production Cross-Section Calculation**:
  - Calculates the production cross-section for tau pairs at specified W values using the interpolated $S_{\gamma\gamma}$.
  - Integrates cross-section values from a user-specified threshold `W_0` up to the center-of-mass energy.
  - Includes options for visualizing results with Matplotlib.

## File Structure

### Key Files

- **`flux_el_yy_atW(W, eEbeam, pEbeam)`**  
  - Computes the $S_{\gamma\gamma}$ values for inelastic photon-photon interactions.
  - Includes options for saving and plotting results, with customized parameters for MN, \( Q^2 \) max values, and W range.

- **`cs_tautau_w(W)`**  
  - Calculates and integrates the tau-tau production cross-section using $S_{\gamma\gamma}$ data from a precomputed file.
  - Provides options to skip integration for W values where $S_{\gamma\gamma}$ is zero, improving performance and accuracy.

- **`Integrated_elastic_tau_tau_cross_section_final_version_using_vegas.py`** and **`Integrated_inelastic_tau_tau_cross_section_final_version_using_vegas.py`**
  - Compares $S_{\gamma\gamma}$ values between a simple approximation and the corrected inelastic model.
  - Computes and plots the relative difference between the two models for a comprehensive comparison.

- **Data Files**:  
  - **`Inelastic_Photon_Luminosity_Spectrum_MNmax_<value>_q2emax_<value>_q2pmax_<value>_using_vegas.txt`**  
    - Precomputed $S_{\gamma\gamma}$ values for inelastic photon-photon interactions, generated using the phthon script.

## Dependencies

- `numpy`
- `scipy`
- `matplotlib`
- `vegas`

Install dependencies via:
```bash
pip install numpy 
pip install scipy
pip install matplotlib
pip install vegas
```

## Usage

### 1. Generate Photon-Photon Luminosity Spectrum ($S_{\gamma\gamma}$ and cross-sections calculations) - elastic case

Run `Integrated_elastic_tau_tau_cross_section_final_version_using_vegas.py` to compute $S_{\gamma\gamma}$ and integrated tau-tau production cross-section for elastic interactions. 
Customize parameters such as the beam energies, \( Q^2 \) maximum values, and MN upper limit before running the script.

```bash
python Integrated_elastic_tau_tau_cross_section_final_version_using_vegas.py
```

Results are saved in `Inelastic_Photon_Luminosity_Spectrum_MNmax_<value>_q2emax_<value>_q2pmax_<value>_using_vegas.txt`.

### 2. Generate Photon-Photon Luminosity Spectrum ($S_{\gamma\gamma}$ and cross-sections calculations)  - inelastic case

Using `Integrated_inelastic_tau_tau_cross_section_final_version_using_vegas.py`, calculate the iSyy and integrated tau-tau production cross-section. 
This script reads $S_{\gamma\gamma}$ data, interpolates it, and performs integration to compute the cross-section at each threshold energy `W0`.

```bash
python Integrated_inelastic_tau_tau_cross_section_final_version_using_vegas.py
```

The script outputs the integrated tau-tau cross-section and saves the result plot.

## 3. Results and Visualization

Each script outputs results in both text and graphical formats:
- $S_{\gamma\gamma}$ and cross-section data are saved in `.txt` files.
- Plots are generated for the luminosity spectrum, tau-tau cross-section, and model comparisons. Files are saved as `.pdf` and `.jpg`.
- 

To emphasize the use of **Vegas integration** in the project, here’s a detailed description you can add at the end of your `README.md` file:

---

## 4. Vegas Monte Carlo Integration

This project extensively leverages the **Vegas Monte Carlo Integration** method to accurately compute elastic/inelastic photon-photon luminosity ($S_{\gamma\gamma}$) and 
tau-tau production cross-sections over a complex multi-dimensional parameter space. 

### Why Vegas?

The Vegas integration method is particularly powerful for high-dimensional and complex integrals where traditional 
numerical methods become impractical. 
By adapting the sampling density to focus on regions of high importance within the integration domain, 
Vegas improves convergence rates and computational efficiency. 
In this project, we use Vegas to handle integrations over multiple variables, 
including photon virtualities and kinematic parameters, for more precise `S_yy` and cross-section values.

### Vegas Library in Python

The implementation in this repository utilizes the [Vegas Python library](https://pypi.org/project/vegas/), 
a popular library for Monte Carlo integration that follows the adaptive importance-sampling strategy of the original Fortran and C implementations. 
Some key features of Vegas integration as applied here include:

- **Adaptive Sampling**: Vegas adapts its sampling strategy over multiple iterations (`nitn`), enhancing accuracy in high-contribution regions.
- **Multi-dimensional Integration**: By performing multi-dimensional integration in an efficient, parallelized manner, Vegas enables us to accurately model high-energy physics scenarios like tau-tau production.
- **Precision Control**: Parameters such as `nitn` (number of iterations) and `neval` (number of evaluations per iteration) are optimized to control the balance between computational time and precision.

### Vegas Integration Parameters

In our calculations, we set the following parameters for Vegas:

- **Training Phase**: The initial phase with a lower `nitn` and `neval` allows Vegas to learn the structure of the integrand and improve sampling efficiency.
- **Final Evaluation**: In the final evaluation phase, we use a higher `nitn` and `neval` to converge on a precise result.

You can adjust these values in the code to balance speed and precision based on available computational resources. Here’s an example configuration used in this project:

```python
# Example Vegas parameters for integrator setup
integrator = vegas.Integrator([[0, 1], [0, 1], [0, 1], [0, 1]])

# Training phase
integrator(vegas_integrand, nitn=10, neval=10000)

# Final evaluation phase
result = integrator(vegas_integrand, nitn=20, neval=100000)
```

For further details on the Vegas library, please refer to the [official Vegas documentation](https://pypi.org/project/vegas/). This repository leverages Vegas's adaptive multi-dimensional integration capabilities to produce precise and reliable results for complex high-energy physics calculations.


## 5. Contacts
For additional information or questions, contact us using the email adresses below:
- Hamzeh Khanpour (Hamzeh.Khanpour@cern.ch)
- Laurent Forthomme (Laurent.Forthomme@cern.ch)
- Krzysztof Piotrzkowski (Krzysztof.Piotrzkowski@cern.ch)
  
