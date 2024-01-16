import unittest
import os
import importlib.util


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        # Specify the submissions directory
        submissions_dir = "submissions"

        # Get a list of all student folders in the submissions directory
        self.student_folders = [folder for folder in os.listdir(submissions_dir) if
                                os.path.isdir(os.path.join(submissions_dir, folder)) and '_' in folder]
        self.student_scores = dict()
        for student in self.student_folders:
            if student not in self.student_scores:
                self.student_scores[student] = 10

        self.flag = ""

    def run_test_for_student(self, student_folder):
        # Specify the submissions directory
        submissions_dir = "submissions"

        # Load the student's code dynamically
        spec = importlib.util.spec_from_file_location("calc", os.path.join(submissions_dir, student_folder, "calc.py"))
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)

        # Run tests for the Calculator class by criteria
        calculator = student_module.Calculator()
        self.flag = "s"
        self.sanity_basic_tests(calculator, student_folder)
        self.flag = "c"
        self.comprehensive_tests(calculator, student_folder)
        self.flag = "r"
        self.robustness_tests(calculator, student_folder)

    def sanity_basic_tests(self, calculator, student_folder):
        # Test addition
        print("Sanity Start -------------------------------")
        nums_x = [2, -2]
        nums_y = [3, 3]
        output = [5, 1]
        for i in range(2):
            try:
                self.assertEqual(calculator.add(nums_x[i], nums_y[i]), output[i])
                print(f"{student_folder} passed test {i + 1}")
            except:
                self.student_scores[student_folder] -= 0.5
                print(f"{student_folder} failed test {i + 1}")
        print("Sanity Done -------------------------------\n")

    def comprehensive_tests(self, calculator, student_folder):
        # # Test subtraction
        # self.assertEqual(calculator.subtract(5, 3), 2)
        # self.assertEqual(calculator.subtract(0, 0), 0)
        # # ... Add more comprehensive tests
        #
        # # Test multiplication
        # self.assertEqual(calculator.multiply(2, 4), 8)
        # self.assertEqual(calculator.multiply(3, 0), 0)
        # # ... Add more comprehensive tests

        # Test division
        print("Comprehensive Start -------------------------------")
        nums_x = [6, 5]
        nums_y = [2, 0]
        output = [3, "Cannot divide by zero."]
        for i in range(2):
            try:
                self.assertEqual(calculator.divide(nums_x[i], nums_y[i]), output[i])
                print(f"{student_folder} passed test {i + 1}")
            except:
                self.student_scores[student_folder] -= -0.5
                print(f"{student_folder} failed test {i + 1}")
        print("Comprehensive Done -------------------------------\n")

    def robustness_tests(self, calculator, student_folder):
        # Test edge cases
        print("Robustness Start -------------------------------")
        nums_x = [0, 1]
        nums_y = [0, 1]
        output = [0, 1]
        for i in range(len(output)):
            try:
                self.assertEqual(calculator.divide(nums_x[i], nums_y[i]), output[i])
                print(f"{student_folder} passed test {i + 1}")
            except:
                self.student_scores[student_folder] -= 1
                print(f"{student_folder} failed test {i + 1}")
        print("Robustness Done -------------------------------\n")

    def test_all_students(self):
        for student_folder in self.student_folders:
            with self.subTest(student=student_folder):
                print(f"----------------------- {student_folder} Running ----------------------")
                self.run_test_for_student(student_folder)
                print(f"----------------------- {student_folder} Done ----------------------\n\n")

    def tearDown(self):
        print(self.student_scores)


if __name__ == '__main__':
    unittest.main()
