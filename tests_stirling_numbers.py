import codewars_test as test
from solution import stirling_numbers

@test.describe("Basic Tests")
def basic():
    test_cases = [
        (("Test Cases of One Digit", [
            ((0, 0), (1, 1)),
            ((0, 1), (0, 0)),
            ((1, 0), (0, 0)),
            ((5, 2), (50, 15)),
            ((6, 2), (274, 31))
        ])),
        (("Test Cases of Two Digits", [
            ((10, 20), (0, 0)),
            ((42, 41), (861, 861)),
            ((25, 23), (42550, 40250)),
            ((33, 31), (133672, 128216)),
            ((27, 20), (40681506808800, 12246296312250))
        ]))
    ]

    for description, cases in test_cases:
        @test.it(description)
        def test_stirling_numbers():
            for input_data, expected_output in cases:
                test.assert_equals(stirling_numbers(*input_data), expected_output)
                

@test.describe("Random Tests")
def rnd():
    from random import randint
    def stirling_numbers_author(n, k):
        if n == 0 and k == 0:
            return (1, 1)
        elif n == 0 or k == 0 or k > n:
            return (0, 0)
        nkmone = stirling_numbers_author(n - 1, k - 1)
        nmone = stirling_numbers_author(n - 1, k)
        return ((n - 1) * nmone[0] + nkmone[0], k * nmone[1] + nkmone[1])
    
    @test.it("Random Tests (1-20)")
    def test_stirling_numbers_1_20():
        for _ in range(555):
            n1 = randint(1, 20)
            n2 = randint(1, 20)
            expected = stirling_numbers_author(n1, n2)
            test.assert_equals(stirling_numbers(n1, n2), expected)

    @test.it("Random Tests (20-40)")
    def test_stirling_numbers_20_30():
        for _ in range(20):
            n1 = randint(20, 30)
            n2 = randint(1, 3)
            expected = stirling_numbers_author(n1, n1 - n2)
            test.assert_equals(stirling_numbers(n1, n1 - n2), expected)
            
    @test.it("Random Tests (30-100)")
    def test_stirling_numbers_30_70():
        for _ in range(5):
            n1 = randint(40, 70)
            n2 = randint(1, 2)
            expected = stirling_numbers_author(n1, n1 - n2)
            test.assert_equals(stirling_numbers(n1, n1 - n2), expected)
