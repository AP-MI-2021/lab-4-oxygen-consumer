def get_multiples(lst):
    lst.sort()
    multiples = []

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            if len(multiples) == 0 or multiples[len(multiples) - 1] != lst[i]:
                multiples.append(lst[i])

    return multiples


def run_get_multiples(lst):
    multiples = get_multiples(lst)
    if multiples == []:
        print("UNIC")
    else:
        print(multiples)


def test_get_multiples():
    assert get_multiples(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa']
    assert get_multiples([]) == []


def get_if_its_present(lst, elem) -> bool:
    for i in lst:
        if elem == i:
            return True
    return False


def run_get_if_its_present(lst):
    elem = input("Introduceti un element: ")
    if get_if_its_present(lst, elem) == True:
        print("DA")
    else:
        print("NU")


def test_get_if_its_present():
    assert get_if_its_present(["abcd"], "abcd") == True
    assert get_if_its_present([], "a") == False


def print_menu():
    menu = """
i. Citire lista
l. Afisare lista
m. Afisare meniu
x. Iesite

1. Verificare daca un element dat este in lista
2. Afisarea tuturor elementelor ce apar de cel putin 2 ori in lista
"""
    print(menu)


def run_tests():
    test_get_if_its_present()
    test_get_multiples()


def input_list():
    lst = []
    raw_input = input("Introduceti lista de elemente separate prin spatii: ")
    return raw_input.split()


def main():
    print_menu()
    run_tests()
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

        elif option == "1":
            run_get_if_its_present(lst)
        elif option == "2":
            run_get_multiples(lst)

        else:
            print("Optiune inexistenta!")
            


if __name__ == "__main__":
    main()
