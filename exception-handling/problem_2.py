def read_file(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: No such file found")
    except PermissionError:
        print("Error: User does not have sufficient permission")
    except Exception as e:
        print(f"Error: {e}")

read_file("Exception Handling/sample.txt")