from pyscript import display, document

non_metals = {
    "H": {
        "symbol": "H",
        "name": "Hydrogen",
        "atomic_number": 1,
        "atomic_mass": "1.008",
    },
    "HE": {
        "symbol": "He",
        "name": "Helium",
        "atomic_number": 2,
        "atomic_mass": "4.0026",
    },
    "C": {
        "symbol": "C",
        "name": "Carbon",
        "atomic_number": 6,
        "atomic_mass": "12.011",
    },
    "N": {
        "symbol": "N",
        "name": "Nitrogen",
        "atomic_number": 7,
        "atomic_mass": "14.007",
    },
    "O": {
        "symbol": "O",
        "name": "Oxygen",
        "atomic_number": 8,
        "atomic_mass": "15.999",
    },
    "F": {
        "symbol": "F",
        "name": "Fluorine",
        "atomic_number": 9,
        "atomic_mass": "18.998",
    },
    "NE": {
        "symbol": "Ne",
        "name": "Neon",
        "atomic_number": 10,
        "atomic_mass": "20.180",
    },
    "P": {
        "symbol": "P",
        "name": "Phosphorus",
        "atomic_number": 15,
        "atomic_mass": "30.974",
    },
    "S": {
        "symbol": "S",
        "name": "Sulfur",
        "atomic_number": 16,
        "atomic_mass": "32.06",
    },
    "CL": {
        "symbol": "Cl",
        "name": "Chlorine",
        "atomic_number": 17,
        "atomic_mass": "35.45",
    },
    "AR": {
        "symbol": "Ar",
        "name": "Argon",
        "atomic_number": 18,
        "atomic_mass": "39.948",
    },
    "SE": {
        "symbol": "Se",
        "name": "Selenium",
        "atomic_number": 34,
        "atomic_mass": "78.971",
    },
    "BR": {
        "symbol": "Br",
        "name": "Bromine",
        "atomic_number": 35,
        "atomic_mass": "79.904",
    },
    "KR": {
        "symbol": "Kr",
        "name": "Krypton",
        "atomic_number": 36,
        "atomic_mass": "83.798",
    },
    "I": {
        "symbol": "I",
        "name": "Iodine",
        "atomic_number": 53,
        "atomic_mass": "126.90",
    },
    "XE": {
        "symbol": "Xe",
        "name": "Xenon",
        "atomic_number": 54,
        "atomic_mass": "131.29",
    },
    "RN": {
        "symbol": "Rn",
        "name": "Radon",
        "atomic_number": 86,
        "atomic_mass": "222",
    },
}


def check_details(e):
    input = document.getElementById("symbol").value.strip()
    key = input.upper()

    data = non_metals.get(key)

    display_message = (
            f"The symbol <b>'{input}'</b> does not exist in the non-metals list.",
            f"Symbol: {key}, Name: {non_metals.get(key, {}).get('name')}, Atomic Number: {non_metals.get(key, {}).get('atomic_number')}, Atomic Mass: {non_metals.get(key, {}).get('atomic_mass')}",
        )

    result_html = display_message[bool(data)]

    document.getElementById("display").innerHTML = result_html