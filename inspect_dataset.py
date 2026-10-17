import json
from pathlib import Path 

# Find the dataset inside our project
dataset_path = Path("data/LiquidFormulationsDataset_2023.json")

# Open and read the JSON file
with open(dataset_path, "r") as file:
    formulations = json.load(file)

# Display basic information
print("Dataset loaded successfully!")
print("Number of formulations:", len(formulations))
print("First formulation ID:", formulations[0]["ID"])
print("Available fields:", list(formulations[0].keys()))

# Count formulations with and without testing data
tested = sum(
    1 for formulation in formulations
    if formulation["Stability_Test"] is True 
)

not_tested = len(formulations) - tested

print("\n--- Experimental Data Availability ---")
print("Formulations with testing data:", tested)
print("Formulations without testing data:", not_tested)
print("Percentage tested:", round(tested / len(formulations) * 100, 1), "%")

# Check whether tested formulations have turbidity measurements
tested_formulations = [
    f for f in formulations
    if f["Stability_Test"] is True
]

missing_turbidity = [
    f for f in tested_formulations
    if f["Turbidity_NTU"] in ("NA", "", None)
]

print("\n--- Measurement Validation ---")
print("Tested formulations:", len(tested_formulations))
print("Tested formulations missing turbidity:", len(missing_turbidity))

# Check completeness of other experimental fields
measurement_fields = [
    "Turbidity_NTU",
    "Turbidity_Error",
    "Viscosity",
    "Rheology_Type",
    "Rheology_Data"
]

print("\n--- Measurement Completeness ---")

for field in measurement_fields:
    missing = sum(
        1 for f in tested_formulations
        if f[field] in ("NA", "", None)
    )

    print(f"{field}: {missing} missing out of {len(tested_formulations)}")

print("\n--- Example Experimental Record ---")

example = tested_formulations[0]

for field in [
    "ID",
    "Stability_Test",
    "Turbidity_NTU",
    "Turbidity_Error",
    "Viscosity",
    "Rheology_Type",
    "Rheology_Data"
]:
    print(f"{field}: {example[field]}")