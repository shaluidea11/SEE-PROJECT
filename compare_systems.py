"""
Solar Water Heater vs Electric Geyser comparison
Run: python compare_systems.py Solar_vs_Electric_Geyser_Dataset.xlsx
Requires: pandas, openpyxl
NOTE: The supplied workbook contains illustrative synthetic data. Replace it with measured hostel data.
"""
import sys
import pandas as pd

CP_KJ_PER_KG_C = 4.186
GEYSER_EFFICIENCY = 0.90
TARIFF_INR_PER_KWH = 8.0
GRID_KG_CO2_PER_KWH = 0.716

def main(path):
    df = pd.read_excel(path, sheet_name="Cleaned_Data")
    df["temp_rise_C"] = df["Water temp after (°C)"] - df["Water temp before (°C)"]
    df["thermal_kWh"] = (
        df["Water volume (L)"] * df["temp_rise_C"] * CP_KJ_PER_KG_C / 3600
    )
    # Electrical energy required by an electric geyser to supply the same heat.
    df["equivalent_electricity_kWh"] = df["thermal_kWh"] / GEYSER_EFFICIENCY

    daily = df.pivot(index="Date", columns="System",
                     values="equivalent_electricity_kWh")
    # Solar heat displaces geyser electricity only where solar delivered less
    # equivalent heat than the geyser's delivered heat on that date.
    daily["electricity_saved_kWh"] = (
        daily["Electric geyser"] - daily["Solar"]
    ).clip(lower=0)

    saved = daily["electricity_saved_kWh"].sum()
    print(f"Equivalent electricity saved: {saved:.2f} kWh")
    print(f"Estimated cost saved: ₹{saved*TARIFF_INR_PER_KWH:.2f}")
    print(f"Estimated CO2 avoided: {saved*GRID_KG_CO2_PER_KWH:.2f} kg")
    daily.to_csv("daily_comparison_output.csv")
    print("Wrote daily_comparison_output.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python compare_systems.py <workbook.xlsx>")
    main(sys.argv[1])
