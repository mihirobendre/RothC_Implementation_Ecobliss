import pandas as pd

# --------------------------------------------------------------------------------------------------
# Python Script: N₂O Emissions from Biomass Burning (VM0042 v2.1 Equations 33 & 59)
# --------------------------------------------------------------------------------------------------

# >> Example default: 5.5 t DM/ha for agricultural residues (IPCC 2006 GL Vol 4, Ch 2, Table 2.4).
additional_C_in = 1.416 # Amount that's left after burning
MB_bsl = additional_C_in / 0.95 / 0.45   # t DM/ha

# >> percent of biomass burned - already taken into account, in Excel.
CF = 1

# >> From IPCC 2006 GL Vol 4, Ch 2, Table 2.5 (Andreae & Merlet, 2001).
EF_N2O = 0.00021  # kg/kg DM

# >> IPCC AR6 WGI Table 7.15: 100‑yr GWP including climate-carbon feedbacks.
# >> See: https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7 (#Table7.15)
GWP_N2O = 273  # unitless

# Convert N₂O emissions to t CO2e per ha
n2o_co2e_bsl_per_ha = (GWP_N2O * MB_bsl * CF * EF_N2O)


# TOTALS

print('N2O ERs (tCO2e/ha)')

print(f"Per-ha N2O emissions (prj - bsl) = {n2o_co2e_bsl_per_ha:.8f}")

