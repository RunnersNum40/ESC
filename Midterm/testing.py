
import unittest
from midterm import *
import random

class TestMidterm(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_cubes(1), 1)
        self.assertEqual(sum_cubes(2), 9)
        self.assertEqual(sum_cubes(3), 36)
        self.assertEqual(sum_cubes(4), 100)

    def test_2(self):
        self.assertEqual(sum_cubes_num_terms(-999), 1)
        self.assertEqual(sum_cubes_num_terms(-1), 1)
        self.assertEqual(sum_cubes_num_terms(0), 1)
        self.assertEqual(sum_cubes_num_terms(1), 1)
        self.assertEqual(sum_cubes_num_terms(2), 2)
        self.assertEqual(sum_cubes_num_terms(9), 2)
        self.assertEqual(sum_cubes_num_terms(8.99), 2)
        self.assertEqual(sum_cubes_num_terms(9.01), 3)
        self.assertEqual(sum_cubes_num_terms(10), 3)
        self.assertEqual(sum_cubes_num_terms(35), 3)
        self.assertEqual(sum_cubes_num_terms(36), 3)
        self.assertEqual(sum_cubes_num_terms(37), 4)

    def test_3(self):
        test_case_sample = [10.4, 1.6, 2, 0.2, 0, 0, 5.2, 0, 0, 0, 0, 0, 3.8, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 2.0, 0, 0, 0, 8.4, 2.2, 5.0]

        self.assertEqual(len(moving_average(test_case_sample)),28)
        self.assertEqual(moving_average([0,0,0]),[0])
        self.assertAlmostEqual(moving_average([0.1,0.1,0.1])[0],0.1)
        self.assertAlmostEqual(moving_average([0,0,33])[0],11)

        test_case_sol = [4.66666667,1.26666667,0.733333333,0.0666666667,1.73333333,1.73333333,1.73333333,0,0,0,1.26666667,1.26666667,1.26666667,0,0,0,0,0,0,0,0,0.666666667,0.666666667,0.666666667,0,2.8,3.53333333,5.2]

        for i in range(len(test_case_sol)):
            self.assertAlmostEqual(moving_average(test_case_sample)[i],test_case_sol[i])

        test_case_sample = [0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(sum(moving_average(test_case_sample)),0)

        test_case_sample = [random.randint(0,10) for i in range(1000)]
        self.assertAlmostEqual(
            sum(moving_average(test_case_sample)),
                (3*sum(test_case_sample)-
                2*test_case_sample[0]-2*test_case_sample[-1]-
                test_case_sample[1]-test_case_sample[-2])/3
            )

    def test_4(self):
        self.assertEqual(match("a","a"),True)
        self.assertEqual(match("abc","abc"),True)
        self.assertEqual(match("abc","ab"),True)
        self.assertEqual(match("abc","bc"),True)
        self.assertEqual(match("abc","ca"),True)
        self.assertEqual(match("abc","cab"),True)
        self.assertEqual(match("abc","bca"),True)
        self.assertEqual(match("abc","bca"),True)
        self.assertEqual(match("zabcz","abc"),True)
        self.assertEqual(match("zabcz","abcz"),True)
        self.assertEqual(match("zabcz","bczza"),True)
        self.assertEqual(match("zabcz","bczza"),True)
        self.assertEqual(match("zabcz","abcza"),False)
        self.assertEqual(match("zabcz","cba"),False)
        self.assertEqual(match("zabcz","zzc"),False)
        self.assertEqual(match("zabcz","czy"),False)
        self.assertEqual(match("aaaaaa","aaaaaa"),True)
        self.assertEqual(match("aaaaaaa","aaaaaa"),True)
        self.assertEqual(match("aaaAaaa","aaaaaa"),True)
        self.assertEqual(match("aaaaaaA","aaaaaa"),True)
        self.assertEqual(match("aaaaaA","aaAaaa"),True)
        self.assertEqual(match("AaaaaA","aaAaaa"),False)
        self.assertEqual(match("aaaa","b"),False)
        self.assertEqual(match("12345","4512"),True)
        self.assertEqual(match("12345","4523"),False)

    def test_5(self):

        T1 = [[1, 2, 3],
            [1, 5, 1],
            [1, 2, 2]]

        T2 = [[3, 1, 0],
            [1, 1, 2],
            [2, 1, 0]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[1, 2, 3],
              [1, 5, 1],
              [1, 2, 2]]

        T2 = [[3, 1, 2],
              [1, 1, 5],
              [2, 1, 2]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[1],
              [1],
              [1]]
        T2 = [[1],
              [1],
              [1]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[1],
              [2],
              [3]]
        T2 = [[1],
              [1],
              [1]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[1,0],
              [2,0],
              [3,0]]
        T2 = [[1,0],
              [1,0],
              [1,0]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[1,0],
              [2,0],
              [3,0]]
        T2 = [[1,0],
              [1,0],
              [1,1]]
        self.assertEqual(share_n1(T1,T2),False)
        self.assertEqual(share_n1(T2,T1),False)

        T1 = [[0]]
        T2 = [[0]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[0]]
        T2 = [[1]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[0,1]]
        T2 = [[1,2]]
        self.assertEqual(share_n1(T1,T2),True)

        T1 = [[0,1]]
        T2 = [[2,3]]
        self.assertEqual(share_n1(T1,T2),False)

        T1 = [[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]]
        T2 = [[1,2,3,4,5,6,7,8,9,10,11],[0,1,2,3,4,5,6,7,8,9,10]]
        self.assertEqual(share_n1(T1,T2),False)

        T1 = [[0,1,6],
              [3,4,5],
              [8,9,10],
              [8,3,4]]
        T2 = [[4,1,0],
              [6,4,3],
              [5,3,8],
              [10,9,8]]
        self.assertEqual(share_n1(T1,T2),False)


        T1 = [[0,1,6],
              [3,4,5],
              [8,9,10],
              [8,3,4]]
        T2 = [[6,1,0],
              [5,4,3],
              [10,3,8],
              [4,9,8]]
        self.assertEqual(share_n1(T1,T2),True)

if __name__ == '__main__':
    unittest.main()