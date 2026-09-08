# Simulations-in-physics-projects.
# Scientific Computing & Physics Simulation Portfolio

Welcome to my portfolio repository. This repository contains a collection of computational physics models, data analysis scripts, and biophysical simulations developed during my graduate studies, as well as independent research projects.

The projects showcase my work in **medical physics, radiation transport, radiobiological modeling, and data visualization**.

---

## Skills & Technologies

- **Programming & Analysis:** Python (`NumPy`, `SciPy`, `Matplotlib`, `Pandas`)
- **Monte Carlo Simulations:** MCNP (Radiation transport and dose scoring)
- **Biophysical Modeling:** Radiobiological model fitting (Linear-Quadratic model, RBE/LET calculations)
- **Documentation & Publishing:** LaTeX, Jupyter Notebooks, Markdown
- **Version Control & Environments:** Git, GitHub, Linux (Fedora CLI)

---

## Repository Structure & Projects

### 1. Artificial Intelligence for Experimental and Applied Physics
* **Directory:** `AI simulations in physics/`
* **Description:** Machine learning-based prediction model for gallstone disease using bioimpedance and laboratory data.
* **Key Features:**
  *  Random Forest, Gradient Boosting, XGBoost, and CatBoost.
* **Notebooks:**
  * [Early prediction of gallstone disease](AI%20simulations%20in%20physics/Proyecto_final.ipynb) 
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/camilacostav01-oss/AI-in-physics-projects./blob/main/AI%20simulations%20in%20physics/Proyecto_final.ipynb)

---

### 2. Radiation Transport & Monte Carlo Simulations
* **Directory:** `mcnp-simulations/`
* **Description:** Configuration of Monte Carlo radiation transport simulations.
* **Key Features:**
  * Creation of a geometry and visualization of MCNP tally outputs (fluence, absorbed dose, and secondary particle spectra)
* **Notebooks / Scripts:**
  * [MCNP geometry and Tally](mcnp-simulations/radiation-soft-tissue)

---

### 3. Radiobiology & Biophysical Modeling
* **Directory:** `Thesis-BIANCA-simulations/`
* **Description:** Implementation and analysis of biophysical models for radiotherapy and hadrontherapy applications.
* **Key Features:**
  * Curve fitting for experimental signal decay and characterization of physical properties.
  * Quantitative analysis with uncertainty propagation and error estimation.
  * Estimation of absorbed dose with different calculation methods for the Isoeffective dose
* **Notebooks:**
  * [Survival function](Thesis-BIANCA-simulations/surv_function.py)
  * [Radiobiological parameters estimator](Thesis-BIANCA-simulations/analyzer.py)
  * [Isoeffective Dose Calculations](Thesis-BIANCA-simulations/Diso_vs_Dphys.ipynb)
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/camilacostav01-oss/AI-in-physics-projects./blob/main/Thesis-BIANCA-simulations/Diso_vs_Dphys_5.ipynb)

---

## How to Run the Projects

### Running in Google Colab (Recommended)
You can directly open and execute any Jupyter Notebook in Google Colab by clicking the **"Open in Colab"** badges above next to each project.

### Running Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
