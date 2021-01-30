#!/usr/bin/env python3

import io
import unittest
import importlib
ld = importlib.import_module("ldif-decode")


class LdifTestInput(unittest.TestCase):
    expected_output1 = "givenName:: Dörte"
    expected_output2 = "userPassword:: {CRYPT}$6$rounds=2000000$L4hZSOth/ki7L$h1WCQqz9BZEvqDQ5TvhehQN9/pq/ms0FgO2jXG9RPVVu8ITc5X7xMw0BYHck8moxP5KkaVhP9XoAPCAB.xddv0"

    def test_singleline(self):
        file_handle = io.StringIO('givenName:: RMO2cnRl')
        output = ld.main(file_handle)
        self.assertEqual(output.strip(), LdifTestInput.expected_output1)

    def test_twolines(self):
        input = ("userPassword:: e0NSWVBUfSQ2JHJvdW5kcz0yMDAwMDAwJEw0aFpTT3RoL2tpN0wkaDFXQ1Fxejl\n"
                  " CWkV2cURRNVR2aGVoUU45L3BxL21zMEZnTzJqWEc5UlBWVnU4SVRjNVg3eE13MEJZSGNrOG1veFA1\n"
                  " S2thVmhQOVhvQVBDQUIueGRkdjA=\n"
                  "givenName:: RMO2cnRl\n")
        file_handle = io.StringIO(input)
        output = ld.main(file_handle)
        self.assertEqual(output.strip(), f"{LdifTestInput.expected_output2}\n{LdifTestInput.expected_output1}")


class LdifTestFile(unittest.TestCase):
    expected_output1 = "givenName:: Dörte"
    expected_output2 = "userPassword:: {CRYPT}$6$rounds=2000000$L4hZSOth/ki7L$h1WCQqz9BZEvqDQ5TvhehQN9/pq/ms0FgO2jXG9RPVVu8ITc5X7xMw0BYHck8moxP5KkaVhP9XoAPCAB.xddv0"

    def test_01(self):
        count1 = 0
        count2 = 0

        with open("tests/test01.ldif") as test01_file:
            output = ld.main(test01_file)

            for line in output.splitlines():
                if line.strip() == LdifTestFile.expected_output1:
                    count1 += 1
                if line.strip() == LdifTestFile.expected_output2:
                    count2 += 1

        self.assertEqual(count1, 1)
        self.assertEqual(count2, 1)

    def test_02(self):
        count1 = 0
        count2 = 0

        with open("tests/test02.ldif") as test02_file:
            output = ld.main(test02_file)

            for line in output.splitlines():
                if line.strip() == LdifTestFile.expected_output1:
                    count1 += 1
                if line.strip() == LdifTestFile.expected_output2:
                    count2 += 1

        self.assertEqual(count1, 2)
        self.assertEqual(count2, 1)

    def test_03(self):
        count1 = 0
        count2 = 0

        with open("tests/test03.ldif") as test03_file:
            output = ld.main(test03_file)

            for line in output.splitlines():
                if line.strip() == LdifTestFile.expected_output1:
                    count1 += 1
                if line.strip() == LdifTestFile.expected_output2:
                    count2 += 1

        self.assertEqual(count1, 2)
        self.assertEqual(count2, 3)


if __name__ == "__main__":
    unittest.main()
