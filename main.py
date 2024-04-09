import random
import functools

# Question 1
def randomized_array(size):
    """Génère une liste contenant des nombres entiers aléatoires variant de 1 à 10

    Args:
        size (int): taille (nbr d'éléments) de la liste à générer
    Returns:
        (list): liste contenant des nombres aléatoires de 1 à 10
    """
    return list(
        map(
            lambda _: random.randint(1, 10),
            [0] * size # devrait utiliser range(size)
        )
    )


# Question 2
def remove_special_chars_from_array(array):
    """Retire les éléments qui contiennent d'autres charactères que des lettres dans une liste

    Args:
        array (list[str]): liste à nettoyer
    Returns:
        (list): liste sans éléments à charactères spéciaux
    """
    return list(
        filter(
            lambda text: text.isalpha(),
            array
        )
    )


def test_remove_special_chars_from_array():
    assert remove_special_chars_from_array(['', ' ']) == []
    assert remove_special_chars_from_array(['la vie est belle']) == []
    assert remove_special_chars_from_array(['a', '1', '#', 'I']) == ['a', 'I']
    assert remove_special_chars_from_array(['abcdefg', 'a$%?&*g']) == ['abcdefg']
    assert remove_special_chars_from_array(['a', ' ', '', '$ab^2', 'allo']) == ['a', 'allo']

# Question 3
def remove_odd_numbers_from_array(array):
    """Retire les nombres impaires d'une liste d'entier

    Args:
        array (list[int]): liste à nettoyer
    Returns:
        (list): liste avec que des nombres pairs
    """
    return list(
        filter(
            lambda num: num % 2 == 0,
            array
        )
    )


def test_remove_odd_numbers_from_array():
    assert remove_odd_numbers_from_array([]) == []
    assert remove_odd_numbers_from_array([1]) == []
    assert remove_odd_numbers_from_array([2]) == [2]
    assert remove_odd_numbers_from_array([3647, 4684]) == [4684]
    assert remove_odd_numbers_from_array([0, 1, 2, 3, 4, 5, 6]) == [0, 2, 4, 6]

# Question 4
def geometric_serie_from_array(array):
    """Calcule la somme de tous les éléments entiers qui sont exposants
    de 2. C'est-à-dire qu'on calcule Σ 2^i pour tout i ∈ array.

    Args:
        array (list[int]): liste d'entiers à calculer la somme
    Returns:
        int: résultat de la somme (Σ 2^i pour tout i ∈ array)
    """
    return functools.reduce(
        lambda x, y: x + y,
        map(
            lambda num: 2 ** num,
            array
        )
    )


def test_geometric_serie_from_array():
    assert geometric_serie_from_array([1]) == 2
    assert geometric_serie_from_array([5]) == 32
    assert geometric_serie_from_array([1, 5]) == 34
    assert geometric_serie_from_array([3, 7, 2]) == 140
    assert geometric_serie_from_array([4, 10, 21, 42]) == 4_398_048_609_296


# Question 5.a
def run_unit_tests():
    """Execute tous les tests unitaires"""
    test_remove_special_chars_from_array()
    test_remove_odd_numbers_from_array()
    test_geometric_serie_from_array()


# Question 5
def main():
    run_unit_tests()

    # Affichage des résultats demandés
    print(randomized_array(10))
    print(remove_odd_numbers_from_array(randomized_array(10)))
    print(geometric_serie_from_array(remove_odd_numbers_from_array(randomized_array(10))))


if __name__ == '__main__':
    main()
