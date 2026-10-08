# ==================================================
# FITCHECK - SIZE RECOMMENDATION MINI APP
# ==================================================

fitcheck_data = [
    {
        "id": "FC001",
        "name": "Amanda",
        "gender": "Female",
        "height": 160,
        "weight": 52,
        "fit": "Regular",
        "size": "M"
    },
    {
        "id": "FC002",
        "name": "Adzhani",
        "gender": "Female",
        "height": 155,
        "weight": 47,
        "fit": "Slim",
        "size": "S"
    }
]


# ==================================================
# FORMAT CUSTOMER ID
# ==================================================

def format_id(customer_id):

    customer_id = customer_id.upper()

    if customer_id.startswith("FC"):
        return customer_id

    else:
        return "FC" + customer_id.zfill(3)


# ==================================================
# SIZE RECOMMENDATION
# ==================================================

def recommend_size(weight):

    if weight < 50:
        return "S"

    elif weight < 60:
        return "M"

    elif weight < 70:
        return "L"

    else:
        return "XL"


# ==================================================
# FIND CUSTOMER
# ==================================================

def find_customer(customer_id):

    customer_id = format_id(customer_id)

    for customer in fitcheck_data:

        if customer["id"] == customer_id:
            return customer

    return None


# ==================================================
# CREATE
# ==================================================

def create_data():

    print("\n===== ADD FITCHECK =====")

    customer_id = format_id(
        input("Customer ID: ")
    )

    # Check duplicate ID
    if find_customer(customer_id):
        print("Customer ID already exists.")
        return

    name = input("Name: ").title()

    if name == "":
        print("Name cannot be empty.")
        return

    gender = input(
        "Gender (Male/Female): "
    ).title()

    if gender not in ["Male", "Female"]:
        print("Invalid gender.")
        return

    height = int(
        input("Height (cm): ")
    )

    weight = int(
        input("Weight (kg): ")
    )

    if height <= 0 or weight <= 0:
        print("Height and weight must be greater than 0.")
        return

    print("""
Fit Preference:

1. Slim
2. Regular
3. Oversized
""")

    fit_choice = input("Choose fit: ")

    if fit_choice == "1":
        fit = "Slim"

    elif fit_choice == "2":
        fit = "Regular"

    elif fit_choice == "3":
        fit = "Oversized"

    else:
        print("Invalid fit preference.")
        return

    size = recommend_size(weight)

    print("\nRecommended Size:", size)

    confirm = input(
        "Save data? (Y/N): "
    ).upper()

    if confirm == "Y":

        new_customer = {
            "id": customer_id,
            "name": name,
            "gender": gender,
            "height": height,
            "weight": weight,
            "fit": fit,
            "size": size
        }

        fitcheck_data.append(new_customer)

        print("\nData successfully saved.")

    else:

        print("\nData was not saved.")


# ==================================================
# READ
# ==================================================

def read_data():

    while True:

        print("""
===== VIEW FITCHECK =====

1. View All Customers
2. Search Customer by ID
3. Filter by Size
4. Size Summary
5. Back
""")

        choice = input("Choose menu: ")


        # ==========================================
        # VIEW ALL
        # ==========================================

        if choice == "1":

            if len(fitcheck_data) == 0:

                print("\nNo customer data.")

            else:

                print("\n===== ALL FITCHECK DATA =====")

                for customer in fitcheck_data:

                    print(
                        customer["id"],
                        "|",
                        customer["name"],
                        "|",
                        customer["gender"],
                        "|",
                        customer["height"],
                        "cm |",
                        customer["weight"],
                        "kg |",
                        customer["fit"],
                        "| Size:",
                        customer["size"]
                    )


        # ==========================================
        # SEARCH BY ID
        # ==========================================

        elif choice == "2":

            customer_id = format_id(
                input("\nEnter Customer ID: ")
            )

            customer = find_customer(customer_id)

            if customer:

                print("\n===== CUSTOMER FOUND =====")

                print(
                    "ID              :",
                    customer["id"]
                )

                print(
                    "Name            :",
                    customer["name"]
                )

                print(
                    "Gender          :",
                    customer["gender"]
                )

                print(
                    "Height          :",
                    customer["height"],
                    "cm"
                )

                print(
                    "Weight          :",
                    customer["weight"],
                    "kg"
                )

                print(
                    "Fit Preference  :",
                    customer["fit"]
                )

                print(
                    "Recommended Size:",
                    customer["size"]
                )

            else:

                print("\nCustomer not found.")


        # ==========================================
        # FILTER BY SIZE
        # ==========================================

        elif choice == "3":

            size = input(
                "\nEnter Size (S/M/L/XL): "
            ).upper()

            found = False

            print("\n===== FILTER RESULT =====")

            for customer in fitcheck_data:

                if customer["size"] == size:

                    print(
                        customer["id"],
                        "|",
                        customer["name"],
                        "| Size:",
                        customer["size"]
                    )

                    found = True

            if found == False:

                print(
                    "No customer found with this size."
                )


        # ==========================================
        # SIZE SUMMARY
        # ==========================================

        elif choice == "4":

            size_s = 0
            size_m = 0
            size_l = 0
            size_xl = 0

            for customer in fitcheck_data:

                if customer["size"] == "S":

                    size_s += 1

                elif customer["size"] == "M":

                    size_m += 1

                elif customer["size"] == "L":

                    size_l += 1

                elif customer["size"] == "XL":

                    size_xl += 1

            print("\n===== SIZE SUMMARY =====")

            print("Size S  :", size_s)
            print("Size M  :", size_m)
            print("Size L  :", size_l)
            print("Size XL :", size_xl)


        elif choice == "5":

            break


        else:

            print("\nInvalid menu.")


# ==================================================
# UPDATE
# ==================================================

def update_data():

    print("\n===== UPDATE FITCHECK =====")

    customer_id = format_id(
        input("Enter Customer ID: ")
    )

    customer = find_customer(customer_id)

    if customer is None:

        print("Customer not found.")
        return

    print("\n===== CUSTOMER FOUND =====")

    print(
        "ID   :",
        customer["id"]
    )

    print(
        "Name :",
        customer["name"]
    )

    print(
        "Size :",
        customer["size"]
    )

    print("""
Choose Data to Update:

1. Name
2. Gender
3. Height
4. Weight
5. Fit Preference
6. Back
""")

    choice = input("Choose menu: ")


    # ==========================================
    # UPDATE NAME
    # ==========================================

    if choice == "1":

        new_name = input(
            "New Name: "
        ).title()

        if new_name == "":

            print("Name cannot be empty.")
            return

        customer["name"] = new_name


    # ==========================================
    # UPDATE GENDER
    # ==========================================

    elif choice == "2":

        new_gender = input(
            "New Gender (Male/Female): "
        ).title()

        if new_gender not in [
            "Male",
            "Female"
        ]:

            print("Invalid gender.")
            return

        customer["gender"] = new_gender


    # ==========================================
    # UPDATE HEIGHT
    # ==========================================

    elif choice == "3":

        new_height = int(
            input("New Height (cm): ")
        )

        if new_height <= 0:

            print("Invalid height.")
            return

        customer["height"] = new_height


    # ==========================================
    # UPDATE WEIGHT
    # ==========================================

    elif choice == "4":

        new_weight = int(
            input("New Weight (kg): ")
        )

        if new_weight <= 0:

            print("Invalid weight.")
            return

        customer["weight"] = new_weight

        customer["size"] = recommend_size(
            customer["weight"]
        )

        print(
            "\nNew Recommended Size:",
            customer["size"]
        )


    # ==========================================
    # UPDATE FIT PREFERENCE
    # ==========================================

    elif choice == "5":

        print("""
Fit Preference:

1. Slim
2. Regular
3. Oversized
""")

        fit_choice = input(
            "Choose fit: "
        )

        if fit_choice == "1":

            customer["fit"] = "Slim"

        elif fit_choice == "2":

            customer["fit"] = "Regular"

        elif fit_choice == "3":

            customer["fit"] = "Oversized"

        else:

            print("Invalid fit preference.")
            return


    elif choice == "6":

        return


    else:

        print("Invalid menu.")
        return


    print("\nData successfully updated.")


# ==================================================
# DELETE
# ==================================================

def delete_data():

    print("\n===== DELETE FITCHECK =====")

    customer_id = format_id(
        input("Enter Customer ID: ")
    )

    customer = find_customer(customer_id)

    if customer is None:

        print("Customer not found.")
        return


    print("\n===== CUSTOMER DATA =====")

    print(
        "ID              :",
        customer["id"]
    )

    print(
        "Name            :",
        customer["name"]
    )

    print(
        "Gender          :",
        customer["gender"]
    )

    print(
        "Height          :",
        customer["height"],
        "cm"
    )

    print(
        "Weight          :",
        customer["weight"],
        "kg"
    )

    print(
        "Fit Preference  :",
        customer["fit"]
    )

    print(
        "Recommended Size:",
        customer["size"]
    )


    confirm = input(
        "\nDelete this customer? (Y/N): "
    ).upper()


    if confirm == "Y":

        fitcheck_data.remove(customer)

        print(
            "\nData successfully deleted."
        )

    else:

        print(
            "\nDelete cancelled."
        )


# ==================================================
# MAIN MENU
# ==================================================

while True:

    print("""
=================================
          FITCHECK APP
=================================

1. View FitCheck
2. Add FitCheck
3. Update FitCheck
4. Delete FitCheck
5. Exit

=================================
""")

    menu = input(
        "Choose menu: "
    )


    if menu == "1":

        read_data()


    elif menu == "2":

        create_data()


    elif menu == "3":

        update_data()


    elif menu == "4":

        delete_data()


    elif menu == "5":

        print(
            "\nThank you for using FitCheck!"
        )

        break


    else:

        print(
            "\nInvalid menu."
        )