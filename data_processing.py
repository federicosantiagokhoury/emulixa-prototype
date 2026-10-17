import json
from pathlib import Path

def load_formulations():
    """Load the original formulation dataset."""
    dataset_path = (
        Path(__file__).resolve().parent
        / "data"
        / "LiquidFormulationsDataset_2023.json"
    )

    with open(dataset_path, "r") as file:
        return json.load(file)

def get_tested_formulations(formulations):
    """Return formulations marked as tested."""
    return [
        formulation
        for formulation in formulations
        if formulation["Stability_Test"] is True
    ]

def find_formulation_by_id(formulations, formulation_id):
    """Find a formulation using its unique ID."""
    for formulation in formulations:
        if formulation["ID"] == formulation_id:
            return formulation

    return None

def save_formulations(formulations, output_path):
    with open(output_path, "w") as file:
        json.dump(formulations, file, indent=2)

if __name__ == "__main__":
    formulations = load_formulations()
    tested = get_tested_formulations(formulations)
    output_path = Path(__file__).resolve().parent / "frontend" / "src" / "data" / "formulations.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_formulations(formulations, output_path)

    print("Total formulations:", len(formulations))
    print("Tested formulations:", len(tested))
    selected = find_formulation_by_id(formulations, 7)

    if selected is not None:
        print("\n--- Selected Formulation ---")
        print("ID:", selected["ID"])
        print("Turbidity:", selected["Turbidity_NTU"])
        print("Viscosity:", selected["Viscosity"])
        print("Rheology type:", selected["Rheology_Type"])