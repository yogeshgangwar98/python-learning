class ValidationError(Exception):
    pass

class AgeValidationError(ValidationError):
    pass

class SalaryValidationError(ValidationError):
    pass

class EmailValidationError(ValidationError):
    pass

def validate_data(data):
    if data["age"] < 18:
        raise AgeValidationError("AGE_VALIDATION_FAILED")
    if data["salary"] <= 0:
        raise SalaryValidationError("SALARY_VALIDATION_FAILED")
    if '@' not in data["email"]:
        raise EmailValidationError("EMAIL_VALIDATION_FAILED")
    
    return "Validation Successful"

def employee(data):
    try:
        validate = validate_data(data)
    except ValidationError as e:
        print(f"Error: {e}")
    else:
        print(validate)
    finally:
        print("Validation Process Finished")

employee({"age":19, "salary": 300, "email":"abc@gmail.com"})