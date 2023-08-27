real = float(input("Enter the real part: "))
imaginary = float(input("Enter the imaginary part: "))

complex1 = {"real": real, "imaginary": imaginary}

def add_complex(complex1, complex2):
    real = complex1["real"] + complex2["real"]
    imaginary = complex1["imaginary"] + complex2["imaginary"]
    return {"real": real, "imaginary": imaginary}

def subtract_complex(complex1, complex2):
    real = complex1["real"] - complex2["real"]
    imaginary = complex1["imaginary"] - complex2["imaginary"]
    return {"real": real, "imaginary": imaginary}

real = float(input("Enter the real part of the second complex number: "))
imaginary = float(input("Enter the imaginary part of the second complex number: "))

complex2 = {"real": real, "imaginary": imaginary}

result = add_complex(complex1, complex2)
print(f"The result of addition is {result['real']} + {result['imaginary']}i")

result = subtract_complex(complex1, complex2)
print(f"The result of subtraction is {result['real']} + {result['imaginary']}i")
