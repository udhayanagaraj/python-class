

def is_valid_aadhar(aadhar_no):
    n = len(aadhar_no)

    if n != 12:
        return "Invalid Aadhar number"
    
    return "Valid Aadhar number"


def check():
    print("just checking")