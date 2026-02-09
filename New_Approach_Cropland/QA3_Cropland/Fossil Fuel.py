# ====================================================================================================
# Python Script: VM0042 v2.1 - Fossil Fuel Emission Reductions (Equations 7, 8, 52)
# Project Context: Wa Region, Ghana | Tractor Use: Massey Ferguson (slightly used)
#
# Description:
# This script calculates CO₂ emissions from diesel-powered tractors using Equations (7), (8), and (52)
# from the Verra VM0042 v2.1 methodology. It distinguishes between clustered ("blog") and remote farms,
# and applies IPCC 2019 emission factors for off-road agricultural diesel.
#
# ----------------------------------------------------------------------------------------------------
#  Key Equations:
# - Equation (8): EFF = FFC × EF_CO2
# - Equation (7): CO2_mean = EFF / Area
# - Equation (52): ΔCO2 = (CO2_mean_bsl - CO2_mean_prj) × Area
#
#  Emission Factor Source:
# IPCC 2019 Refinement to the 2006 Guidelines
# Volume 2, Chapter 3, Table 3.2.1 (Diesel – Off-road/Agriculture)
# EF = 72,850.77 kg CO2/TJ × 0.036 TJ/liter = 2.623 kg CO2/l = 0.002623 t CO2/l
# Source: https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/2_Volume2/19R_V2_3_Ch03_Mobile_Combustion.pdf
# ====================================================================================================

# ===============================
#  INPUT PARAMETERS
# ===============================

# Constants
EF_DIESEL = 0.002623  # tCO2e per liter (IPCC 2019)

# Tractor operating assumptions
TRACTORS_BLOG = 7  # Tractors operating in blog (clustered) areas
TRACTORS_REMOTE = 7  # Tractors operating in remote areas

DAYS_PER_WEEK = 5  # Workdays
WEEKS_PER_YEAR = 52
DAYS_PER_YEAR = DAYS_PER_WEEK * WEEKS_PER_YEAR  # 260 days/year

# Area covered per tractor per day (based on your data)
HECTARES_PER_DAY_BLOG = 6.1
HECTARES_PER_DAY_REMOTE = 5.0

# Fuel use per hectare
FUEL_PER_HA_BSL_BLOG = 28.07  # Baseline fuel use (L/ha) - blog
FUEL_PER_HA_PRJ_BLOG = 20.00  # Project scenario (L/ha)

FUEL_PER_HA_BSL_REMOTE = 30.88  # Baseline fuel use (L/ha) - remote farms
FUEL_PER_HA_PRJ_REMOTE = 22.00  # Project scenario (L/ha)

# -------------------------------
#  Derived inputs
# -------------------------------

# Area worked per field type
area_blog = TRACTORS_BLOG * HECTARES_PER_DAY_BLOG * DAYS_PER_YEAR
area_remote = TRACTORS_REMOTE * HECTARES_PER_DAY_REMOTE * DAYS_PER_YEAR

# Total area worked by tractors (this is not full project area, only what's worked mechanically)
area_total = area_blog + area_remote

# ===============================
#  CALCULATION FUNCTIONS
# ===============================

def emissions_per_hectare(fuel_per_ha: float) -> float:
    """Calculate emissions per hectare (tCO2e/ha) using Equation 8."""
    return fuel_per_ha * EF_DIESEL

def total_emissions(mean_emissions_per_ha: float, area_ha: float) -> float:
    """Calculate total emissions over an area using Equation 7."""
    return mean_emissions_per_ha * area_ha

def emission_reduction(mean_bsl: float, mean_prj: float, area_ha: float) -> float:
    """Calculate total emission reductions using Equation 52."""
    return (mean_bsl - mean_prj) * area_ha

# ===============================
#  EMISSIONS CALCULATIONS
# ===============================

# Emissions per hectare
mean_bsl_blog = emissions_per_hectare(FUEL_PER_HA_BSL_BLOG)
mean_prj_blog = emissions_per_hectare(FUEL_PER_HA_PRJ_BLOG)

mean_bsl_remote = emissions_per_hectare(FUEL_PER_HA_BSL_REMOTE)
mean_prj_remote = emissions_per_hectare(FUEL_PER_HA_PRJ_REMOTE)

# Total emissions
total_bsl_blog = total_emissions(mean_bsl_blog, area_blog)
total_prj_blog = total_emissions(mean_prj_blog, area_blog)

total_bsl_remote = total_emissions(mean_bsl_remote, area_remote)
total_prj_remote = total_emissions(mean_prj_remote, area_remote)

# Emission reductions (Equation 52)
reduction_blog = emission_reduction(mean_bsl_blog, mean_prj_blog, area_blog)
reduction_remote = emission_reduction(mean_bsl_remote, mean_prj_remote, area_remote)

total_reduction = reduction_blog + reduction_remote

# ===============================
#  OUTPUT
# ===============================
output = {
    "Total area (ha) worked by tractors": area_total,
    "Baseline emissions (tCO2e)": total_bsl_blog + total_bsl_remote,
    "Project emissions (tCO2e)": total_prj_blog + total_prj_remote,
    "Emission reductions (tCO2e/year)": round(total_reduction, 2)
}

import pprint
pprint.pprint(output)
