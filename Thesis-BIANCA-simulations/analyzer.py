import numpy as np
from scipy.optimize import curve_fit
import sys

# --- TARGETS FOR U87 (From your papers) ---
# Replace with your actual values and errors  	0.103864 	0.112751 	0.019873 	0.028736
#0.550884 	0.023231 	0.003544 	0.006132
target_alpha = 0.103864
alpha_err    = 0.112751 
target_beta  = 0.019873
beta_err     = 0.028736

def lq_model(D, a, b):
    return np.exp(-a * D - b * D**2)

def analyze():
    try:
        # 1. Use genfromtxt
        # Column 0: Dose
        # Column 14: S(pois) <- This is a common survival metric
        # Column 16: NSENZA <- Based on your file, this is the 17th column
        data = np.genfromtxt('Step_Aberr.dat', 
                            skip_header=1, 
                            usecols=(0, 15), # Changed 14 to 16
                            invalid_raise=False)

        # Now 'data' only has two columns. 
        # Column 0 is Dose, Column 1 is NSENZA
        doses = data[:, 0]
        survival = data[:, 1] # This is now the 2nd column of our filtered data

        # Filter out zeros or NaNs to avoid math errors
        mask = (survival > 0) & (~np.isnan(survival))
        if len(doses[mask]) < 2:
            print("Not enough valid data points for fitting.")
            sys.exit(1)

        # Fit the LQ model
        popt, _ = curve_fit(lq_model, doses[mask], survival[mask], p0=[0.2, 0.05])
        sim_a, sim_b = popt

        error = np.sqrt(((sim_a - target_alpha)/alpha_err)**2 + ((sim_b - target_beta)/beta_err)**2)
        
        print(f"RESULT: a={sim_a:.4f}, b={sim_b:.4f} | Weighted Error={error:.4f}")
        print(f"Doses read: {doses}")
        print(f"Survival read: {survival}")
        if error < 1.0:
            sys.exit(0) 
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    analyze()
    
    
# Results with U87
#Testing CL=1.7 and f=0.010
#RESULT: a=0.0337, b=0.0377 | Weighted Error=0.8788
#Doses read: [0. 1. 2. 3. 4. 5.]
#Survival read: [1.     0.9373 0.8042 0.6374 0.4786 0.3326]
#SUCCESS! Match found.
#U87 Parameters: CL=1.7, f=0.010



