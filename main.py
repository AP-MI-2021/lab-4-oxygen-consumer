def print_menu():
    menu = """
i. Citire lista
l. Afisare lista
m. Afisare meniu
x. Iesite
"""
    print(menu)


def input_list():
    lst = []
    raw_input = input("Introduceti lista de elemente separate prin spatii: ")
    return raw_input.split()

def main():
    print_menu()
    lst = []

    while True:
        option = input("Introduceti optiunea: ")

        if option == "i":
            lst = input_list()
        elif option == "x":
            break
        elif option == "l":
            print(lst)
        elif option == "m":
            print_menu()


if __name__ == "__main__":
    main()
