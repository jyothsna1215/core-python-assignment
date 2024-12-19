def add_patient(patients):
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    disease = input("Enter patient's disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
    print(f"Patient {name} added successfully.")
def search_patients_by_disease(patients, disease):
    result = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return result
def main():
    patients = []
    while True:
        action = input("Do you want to (a)dd a patient or (s)earch for patients by disease? (type 'done' to exit): ").lower()
        if action == 'done':
            break
        elif action == 'a':
            add_patient(patients)
        elif action == 's':
            search_disease = input("Enter disease to search for: ")
            found_patients = search_patients_by_disease(patients, search_disease)
            if found_patients:
                print(f"Patients with {search_disease}: {found_patients}")
            else:
                print(f"No patients found with the disease '{search_disease}'.")
        else:
            print("Invalid option. Please try again.")
    print("\nFinal list of patients:")
    for patient in patients:
        print(patient)
main()
