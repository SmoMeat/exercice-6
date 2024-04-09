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
            range(size)
            #[0] * size
        )
    )


# Question 2
def remove_special_chars_from_array(array):
    """Retire les éléments qui contiennent d'autres charactères que des lettres dans une liste

    Args:
        array (list[str]): taille (nbr d'éléments) de la liste à générer
    Returns:
        (list): liste contenant des nombres aléatoires de 1 à 10
    """
    return list(
        filter(
            lambda text: text.isalpha(),
            array
        )
    )


def test_remove_special_chars_from_array():
    assert True

# Question 3
def remove_odd_numbers_from_array(array):
    return list(
        filter(
            lambda num: num % 2 == 0,
            array
        )
    )


# Question 4
def geometric_serie_from_array(array):
    return functools.reduce(
        lambda x, y: x + y,
        map(
            lambda num: 2 ** num,
            array
        )
    )


# Question 5
def main():
    print(randomized_array(10))

    print(remove_odd_numbers_from_array(randomized_array(10)))

    print(geometric_serie_from_array(remove_odd_numbers_from_array(randomized_array(10))))



if __name__ == '__main__':
    main()

    # print(remove_special_chars_from_array(['allo', 'toi', '', 'l4', 'vie est belle']))

    # print(remove_odd_numbers_from_array([0,1,2,3,4,5,367,4090]))

    # print(geometric_serie_from_array([1, 2, 3, 4]))