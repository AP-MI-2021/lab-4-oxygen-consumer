def get_most_frec(lst):
    """
Determina care este cel mai frecvent intalnit caracter si returneaza un tuple format din acesta si frecventa lui.
    """
    all_freq = {}

    for elem in lst:
  
        for i in elem:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1

    ans = "a"
    frec_ans = 0
    for i in all_freq.keys():
        if all_freq[i] > frec_ans:
            ans = i
            frec_ans = all_freq[i]

    return (ans, frec_ans)


def replace_string_with_most_frec(lst):
    """
Inlocuieste elementele care contin cel mai frecvent caracter cu frecventa acestuia.
    """
    tmp = get_most_frec(lst)
    most_frec = tmp[0]
    frec = tmp[1]

    ans = []
    
    for i in lst:
        if most_frec in i:
            ans.append(frec)
        else:
            ans.append(i)

    return ans


def run_replace_string_with_most_frec(lst):
    replaced = replace_string_with_most_frec(lst)
    print(replaced)


def test_replace_string_with_most_frec():
    assert replace_string_with_most_frec([]) == []
    assert replace_string_with_most_frec(['aaa', 'bbab', 'caamtc', 'drd', 'aaa']) == [9, 9, 9, 'drd', 9]


def is_palindrome(n):
    """
Determina daca un nr este palindrom.
    """
    length = len(n)
    ans = True
    for i in range(length // 2):
        if n[i] != n[length - i - 1]:
            ans = False

    return ans


def get_palindromes(lst):
    """
    Returneaza o lista ce contine toate elementele palindrome.
    """
    palindromes = []
    for i in lst:
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes


def run_get_palindromes(lst):
    palindromes = get_palindromes(lst)
    print(palindromes)


def test_get_palindromes():
    assert get_palindromes(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa', 'bbb', 'drd', 'aaa']
    assert get_palindromes([]) == []


def get_multiples(lst):
    """
Returneaza o lista cu toate elemntele ce apar de cel putin 2 ori.
    """
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
    """
Determina daca un element este prezent in lista.
    """
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
3. Afisarea tuturor elementelor care sunt palindrom
4. Afisarea liste obtinute prin inlocuirea elementelor care contin cel mai des intalnit element cu frecventa acestuia
"""
    print(menu)


def run_tests():
    test_get_if_its_present()
    test_get_multiples()
    test_get_palindromes()
    test_replace_string_with_most_frec()


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
        elif option == "3":
            run_get_palindromes(lst)
        elif option == "4":
            run_replace_string_with_most_frec(lst)

        else:
            print("Optiune inexistenta!")
            


if __name__ == "__main__":
    main()
