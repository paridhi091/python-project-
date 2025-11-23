print("Unit Converter")
print("===============")
# ==== Main Menu ====
unit_change = {
    1: "Length",
    2: "Mass"
}
for key, value in unit_change.items():
    print(f"{key}. {value}")

change = int(input("\nWhich type of conversion you want to do (1/2): "))
# ======================= LENGTH =============================
if change == 1:
    print("\n>>> You chose Length\n")
    
    length_dict = {
        1: "Centimeter to Meter",
        2: "Meter to Centimeter",
        3: "Centimeter to Inch",
        4: "Inch to Centimeter",
        5: "Centimeter to Kilometer",
        6: "Kilometer to Centimeter"
    }

    for k, v in length_dict.items():
        print(f"{k}. {v}")

    value = float(input("\nEnter value to convert: "))
    opt = int(input("Choose conversion (1–6): "))

    if opt == 1:
        print(f"{value} cm = {value/100} m")
    elif opt == 2:
        print(f"{value} m = {value*100} cm")
    elif opt == 3:
        print(f"{value} cm = {value/2.54} inch")
    elif opt == 4:
        print(f"{value} inch = {value*2.54} cm")
    elif opt == 5:
        print(f"{value} cm = {value/100000} km")
    elif opt == 6:
        print(f"{value} km = {value*100000} cm")
    else:
        print("Invalid option.")
# ======================== MASS ==============================
elif change == 2:
    print("\n>>> You chose Mass\n")

    mass_dict = {
        1: "Gram to Kilogram",
        2: "Kilogram to Gram",
        3: "Milligram to Gram",
        4: "Gram to Milligram",
        5: "Kilogram to Pound",
        6: "Pound to Kilogram"
    }

    for k, v in mass_dict.items():
        print(f"{k}. {v}")

    value = int(input("\nEnter value to convert: "))
    opt = int(input("Choose conversion (1–6): "))

    if opt == 1:
        print(f"{value} g = {value/1000} kg")
    elif opt == 2:
        print(f"{value} kg = {value*1000} g")
    elif opt == 3:
        print(f"{value} mg = {value/1000} g")
    elif opt == 4:
        print(f"{value} g = {value*1000} mg")
    elif opt == 5:
        print(f"{value} kg = {value*2.20462} lb")
    elif opt == 6:
        print(f"{value} lb = {value/2.20462} kg")
    else:
        print("Invalid option.")
else:
    print("Please select only 1 or 2.")