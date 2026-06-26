
class Patient:
    def __init__(self, patient_id, name, insurance_number):
        self.patient_id         = patient_id
        self.name               = name
        self.__medical_history  = []
        self.__insurance_number = insurance_number

    def add_medical_record(self, medical_history):
        if medical_history in self.__medical_history:
            raise ValueError("Record already added")
        self.__medical_history.append(medical_history)
        print("Medical record(s) added successfully")

    def view_medical_history(self):
        return self.__medical_history.copy()

    def get_insurance_number(self):
        return self.__insurance_number

    def display_patient(self):
        return f"Patient ID: {self.patient_id} and Name: {self.name}"
    
patient = Patient(1,"Rahul", "INS001")
patient.add_medical_record("Knee Fracture")
patient.add_medical_record("Fever")
patient.add_medical_record("Fever")
print(patient.view_medical_history())
print(patient.get_insurance_number())
print(patient.display_patient())