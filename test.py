import importlib.util
import os
import unittest


class IncomeTaxCalculatorTest(unittest.TestCase):
    def setUp(self):
        # Specify the submissions directory
        submissions_dir = "submissions"

        # Get a list of all student folders in the submissions directory
        self.student_folders = [folder for folder in os.listdir(submissions_dir) if
                                os.path.isdir(os.path.join(submissions_dir, folder)) and '_' in folder]
        self.student_scores = dict()
        for student in self.student_folders:
            if student not in self.student_scores:
                self.student_scores[student] = 0

        self.flag = ""

    def run_test_for_student(self, student_folder):
        # Specify the submissions directory
        submissions_dir = "submissions"

        # Load the student's code dynamically
        spec = importlib.util.spec_from_file_location("income_tax",
                                                      os.path.join(submissions_dir, student_folder, "income_tax.py"))
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)

        # Run tests for the income tax calculator class
        self.flag = "c"
        self.comprehensive_tests(student_module.compute_tax, student_folder)
        self.flag = "r"
        self.robustness_tests(student_module.compute_tax, student_folder)

    def comprehensive_tests(self, compute_tax_function, student_folder):
        # Comprehensive tests for the compute_tax function
        print("***** Comprehensive Start *****")
        # Test with various income values
        test_cases = [
            (2000, 1743.85),
            (5000, 4117.0),
            # Add more comprehensive test cases
        ]

        for i, (income, expected_output) in enumerate(test_cases, start=1):
            try:
                actual_output = compute_tax_function(income)
                self.assertAlmostEqual(actual_output, expected_output, places=2)
                self.student_scores[student_folder] += 1
                print(f"{student_folder} passed test {i}")
            except:
                print(f"{student_folder} failed test {i}")
        print("***** Comprehensive Done *****\n")

    def robustness_tests(self, compute_tax_function, student_folder):
        # Robustness tests for the compute_tax function
        print("Robustness Start -------------------------------")
        # Test with edge cases and invalid inputs
        test_cases = [
            (0, 0.0),
            (-5000, 0.0),  # Invalid input, should return 0.0
            # Add more robustness test cases
        ]

        for i, (income, expected_output) in enumerate(test_cases, start=1):
            try:
                actual_output = compute_tax_function(income)
                self.assertAlmostEqual(actual_output, expected_output, places=2)
                self.student_scores[student_folder] += 1
                print(f"{student_folder} passed test {i}")
            except:
                print(f"{student_folder} failed test {i}")
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
