import pandas as pd

# --------------------------------------------------------------------------------------------------
# Python Script: N₂O Emissions from Biomass Burning (VM0042 v2.1 Equations 33 & 59)
# --------------------------------------------------------------------------------------------------

area_ha = 30000  # ha

# ----------------------------
# BASELINE INPUTS
# ----------------------------

# >> Example default: 5.5 t DM/ha for agricultural residues (IPCC 2006 GL Vol 4, Ch 2, Table 2.4).
MB_bsl = 9.814168716/0.45  # t DM/ha

# >> Typical IPCC default for residues: 0.9.
CF = 0.755  # unitless  average between early/mid/late season burns in savannah grasslands

# >> From IPCC 2006 GL Vol 4, Ch 2, Table 2.5 (Andreae & Merlet, 2001).
EF_N2O = 0.00021  # kg/kg DM

# >> IPCC AR6 WGI Table 7.15: 100‑yr GWP including climate-carbon feedbacks.
# >> See: https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7 (#Table7.15)
GWP_N2O = 273  # unitless

# Convert N₂O emissions to t CO2e per ha
n2o_co2e_bsl_per_ha = (GWP_N2O * MB_bsl * CF * EF_N2O)


# ----------------------------
# PROJECT INPUTS
# ----------------------------

# >> Example default: 5.5 t DM/ha for agricultural residues (IPCC 2006 GL Vol 4, Ch 2, Table 2.4).
MB_prj = 8.654190883/0.45  # t DM/ha

# >> Typical IPCC default for residues: 0.9.
CF = 0.755  # unitless  average between early/mid/late season burns in savannah grasslands

# >> From IPCC 2006 GL Vol 4, Ch 2, Table 2.5 (Andreae & Merlet, 2001).
EF_N2O = 0.00021  # kg/kg DM

# >> IPCC AR6 WGI Table 7.15: 100‑yr GWP including climate-carbon feedbacks.
# >> See: https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7 (#Table7.15)
GWP_N2O = 273  # unitless

# Convert N₂O emissions to t CO2e per ha
n2o_co2e_prj_per_ha = (GWP_N2O * MB_prj * CF * EF_N2O)


# ----------------------------
# TOTALS
# ----------------------------

# Total baseline emissions
total_n2o_co2e_baseline = n2o_co2e_bsl_per_ha * area_ha

# Total project emissions
total_n2o_co2e_project = n2o_co2e_prj_per_ha * area_ha

# Emission reduction achieved
total_n2o_reduction = total_n2o_co2e_baseline - total_n2o_co2e_project

print(f"Total N2O emissions (baseline) = {total_n2o_co2e_baseline:.8f}")

print(f"Total N2O emissions (project) = {total_n2o_co2e_project:.8f}")


