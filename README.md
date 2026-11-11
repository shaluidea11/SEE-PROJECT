# Solar Water Heater vs Electric Geyser Comparator

## Purpose
Compare the useful heat delivered by a hostel solar water heater and an electric geyser over 14 days. Convert the measured temperature rise into thermal energy, estimate equivalent electrical energy, and estimate electricity-cost and CO2 savings.

## Important data note
The attached workbook is populated with **synthetic illustrative data**, not measurements from a real hostel. Replace the rows in `Raw_Data` with actual observations before making claims about savings. `Cleaned_Data` demonstrates duplicate removal, missing-temperature imputation, and invalid-duration correction.

## Workbook
- `Raw_Data`: unmodified example observations plus intentionally introduced data-quality issues.
- `Cleaned_Data`: cleaned 14-day paired observations with derived heat/energy columns.
- `Assumptions`: editable water volume, geyser efficiency, tariff and grid emission factor.
- `Summary`: example aggregate results.

## Calculation
For water volume `m` (kg; approximately litres), specific heat `cp = 4.186 kJ/kg°C`, and temperature rise `ΔT`:

`Thermal energy (kWh) = m × cp × ΔT / 3600`

`Equivalent electricity (kWh) = thermal energy / geyser efficiency`

Daily displaced electricity is estimated as the electric-geyser equivalent energy minus the solar equivalent energy, floored at zero. Cost and CO2 savings are displaced kWh multiplied by the assumed tariff and grid emission factor.

## Run
Install dependencies:
```bash
pip install pandas openpyxl
```
Run:
```bash
python compare_systems.py Solar_vs_Electric_Geyser_Dataset.xlsx
```
The script writes `daily_comparison_output.csv`.

## Assumptions and limitations
- Example volume: 100 L/day for each system.
- Example electric-geyser efficiency: 90%.
- Example tariff: ₹8/kWh.
- Example grid factor: 0.716 kg CO2/kWh. Replace with the factor required by your course/institution or a current official factor.
- Temperature measurements alone do not capture tank heat losses, draw-off volume, solar pump electricity, standby losses, or different hot-water demand. For a fair field study, measure actual volume consumed and compare equivalent delivered hot-water service.
