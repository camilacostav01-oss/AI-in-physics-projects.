import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from scipy import stats
import pandas as pd
import io

#This program extract dose,  NSENZA (clonogenic SF) and unc_NSENZA (error of clonogenic SF) from a file .dat (you have to write the file name as input).
#This file is mada by a BIANCA simulation
#Then it print dose, NSENZA, unc_NSENZA
#The program uses the LQM to fit the data (using error on survival fraction) and extracting alpha and beta.
#The errors for alpha and beta are extracted from the covariance matrix.
#The reduced chi squadred is calculated
#This program plots survival fraction (with errors) as a function of dose (without error) in a graph using logaritmic scale and draws the fit function on the graph
#TODO: a possible implementation is to save alpha, beta, their errors, reduced chi square and p-value in an output file.

"--------------------Read the file and create a numpy for dose, SF, and SFerror------------"
# 1. Read the file
filename=input ('filename (it should be something similar to Step_AberrP2.dat) = ')
with open(filename, 'r') as file:
    text = file.read()

#2. Substitute the *** with 'NaN' (Not a Number)
new_text = text.replace('********', ' NaN ')

# 3. Use io.StringIO
df = pd.read_csv(io.StringIO(new_text), sep=r'\s+', comment='#', header=None)

# 4. Columns names
df.columns = [

    'Dose', 'DIC', 'unc_DIC', 'CER', 'unc_CER', 'EAF', 'unc_EAF',

    'ALIN', 'unc_ALIN', 'ACER', 'unc_ACER', 'TOT', 'unc_TOT',

    'S_pois', 'unc_S', 'NSENZA', 'unc_NSENZA', 'F', 'G', 'EAF_DIC',

    'H', 'ALIN_DIC', 'cells', 'Scar'

]
Dose_raw = df['Dose'].to_numpy()
NSENZA_raw = df['NSENZA'].to_numpy()
unc_NSENZA_raw = df['unc_NSENZA'].to_numpy()

mask = NSENZA_raw > 0
Dose = Dose_raw[mask]
NSENZA = NSENZA_raw[mask]
unc_NSENZA = unc_NSENZA_raw[mask]
abs_unc_NSENZA = NSENZA*unc_NSENZA

print ('filename = ', filename)
print (type(Dose))
print ("Dose = ",Dose)
print ("NSENZA = " ,NSENZA)
print ("unc_NSENZA = ", unc_NSENZA)

"-------------------Definition of surv_function (with LQM)-----------------"
def surv_function(Dose, alpha, beta):
     SF=np.exp(-(alpha*Dose+beta*Dose*Dose))
     return SF

"----------------- Fit and chi square test-------------------"
optimizedParameters,cov=opt.curve_fit(surv_function,Dose,NSENZA,sigma=unc_NSENZA,absolute_sigma=True)

alpha = optimizedParameters[0]
beta = optimizedParameters[1]

#calculation of alpha_err and beta_err
perr = np.sqrt(np.diag(cov))
alpha_err = perr[0]
beta_err = perr[1]
print ("alpha = ", alpha)
print ("alpha_err = ", alpha_err)
print ("beta = ", beta)
print ("beta_err = ", beta_err)

# 1. Calculate the weighted residuals (the basis of Chi-Square)
# We take the difference between experimental data and the model, divided by the uncertainty
weighted_residuals = (NSENZA - surv_function(Dose, *optimizedParameters)) / unc_NSENZA

# 2. Chi-Square is the sum of the squares of the weighted residuals
chi_sq = np.sum(weighted_residuals**2)

# 3. Degrees of Freedom (DOF) = Number of data points - Number of fitting parameters
dof = len(Dose) - len(optimizedParameters)

# 4. Reduced Chi-Square (indicates a good fit if close to 1)
red_chi_sq = chi_sq / dof

# 5. Calculate the p-value AUTOMATICALLY
# stats.chi2.sf (Survival Function) calculates the probability that the Chi-Square
# value is consistent with the model and statistical fluctuations
p_value = stats.chi2.sf(chi_sq, dof)

print(f"Chi-quadro ridotto: {chi_sq/dof:.4f}")
print(f"P-value: {p_value:.4f}")
"------------------------Draw the data, the fit, the legend----------------"

label_data = "Experimental Data"
plt.ylim(1e-2, 1.1)
label_fit = f"Fit LQM: \nα = {alpha:.4f} ± {alpha_err:.4f} Gy⁻¹\nβ = {beta:.4f} ± {beta_err:.4f} Gy⁻² \nReduced chi-squared: {chi_sq/dof:.4f} \nP-value: {p_value:.4f}"
plt.title("SF vs DOSE for particle " + filename[10:-4] +" keV/μm LET")
plt.xlabel("Dose (Gy)")
plt.ylabel("SF")
plt.yscale('log')
plt.errorbar(Dose, NSENZA, yerr= abs_unc_NSENZA,fmt='.',color ="r", markersize=3, label="Data")
plt.grid(color='tab:gray', linestyle='-', linewidth=0.1)

# Create 100 points between 0 and 3
doseforfit = np.linspace(0, 10, 100)

# Draw the fit line using the 100 points
plt.plot(doseforfit, surv_function(doseforfit, *optimizedParameters), label=label_fit)
plt.legend()
plt.show()
