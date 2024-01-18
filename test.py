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
        self.flag = "s"
        self.sanity_tests(student_module.compute_tax, student_folder)
        self.flag = "c"
        self.comprehensive_tests(student_module.compute_tax, student_folder)
        self.flag = "r"
        self.robustness_tests(student_module.compute_tax, student_folder)

    def sanity_tests(self, compute_tax_function, student_folder):
        # Sanity tests for the compute_tax function
        print("----------------- SANITY TEST START -----------------")
        # Test with various income values
        test_cases = [
            (2000, 1743.85),
            (600, 585.7),
            (6000, 4867.00),
            (60000, 42868.85)
        ]
        for i, (income, expected_output) in enumerate(test_cases, start=1):
            try:
                actual_output = compute_tax_function(income)
                self.assertAlmostEqual(actual_output, expected_output, places=2)
                self.student_scores[student_folder] += 0.5
                print(f"{student_folder} passed test {i}")
            except:
                print(f"{student_folder} failed test {i}")
        print("----------------- SANITY TEST DONE -----------------")

    def comprehensive_tests(self, compute_tax_function, student_folder):
        # Comprehensive tests for the compute_tax function
        print("----------------- COMPREHENSIVE TEST START -----------------")
        # Test with various income values
        test_cases = [
            (511.5, 506.02),
            (643, 624.33),
            (4004, 3400),
            (23679, 17944.15),
            (73678, 51759.55),
            (12345678.9, 12314547.75),
            (16395.85, 12663.89),
            (29962, 22342.25),
            (50642, 36786.15),
            (99999.99, 68868.84)
        ]

        for i, (income, expected_output) in enumerate(test_cases, start=1):
            try:
                actual_output = compute_tax_function(income)
                self.assertAlmostEqual(actual_output, expected_output, places=2)
                self.student_scores[student_folder] += 0.5
                print(f"{student_folder} passed test {i}")
            except:
                print(f"{student_folder} failed test {i}")
        print("----------------- COMPREHENSIVE TEST DONE -----------------")

    def robustness_tests(self, compute_tax_function, student_folder):
        # Robustness tests for the compute_tax function
        print("----------------- ROBUSTNESS TEST START -----------------")
        # Test with edge cases and invalid inputs
        test_cases = [
            (402, 402),
            (0.01, 0.01),
            (1e12, 999999968868.85)
        ]

        for i, (income, expected_output) in enumerate(test_cases, start=1):
            try:
                actual_output = compute_tax_function(income)
                self.assertAlmostEqual(actual_output, expected_output, places=2)
                self.student_scores[student_folder] += 1
                print(f"{student_folder} passed test {i}")
            except:
                print(f"{student_folder} failed test {i}")
        print("----------------- ROBUSTNESS TEST DONE -----------------\n")

    def test_all_students(self):
        for student_folder in self.student_folders:
            with self.subTest(student=student_folder):
                print(f"##################### {student_folder} Running ########################")
                self.run_test_for_student(student_folder)
                print(f"###################### {student_folder} Done #####################\n\n")

    def tearDown(self):
        print(self.student_scores)


if __name__ == '__main__':
    unittest.main()
