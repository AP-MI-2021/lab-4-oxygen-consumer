def print_menu():
    menu = """
i. Citire lista
l. Afisare lista
x. Iesite
"""


def input_list():
    lst = []
    raw_input = input("Introduceti lista de elemente separate prin spatii: ")
    return raw_input.split()

def main():
    print_menu()

    option = input("Introduceti optiunea: ")

    if option == "i":
        input_list()

