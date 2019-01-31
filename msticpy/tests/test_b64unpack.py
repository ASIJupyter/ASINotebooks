# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Base64unpack test class."""
import unittest
import pandas as pd
from .. sectools import base64unpack as b64


class TestB64Unpack(unittest.TestCase):

    def test_archive_string(self):
        try:
            input_txt = None
            FILE_NAME = 'msticpy/tests/testdata/b64text_inzip.txt'
            with open(FILE_NAME, 'r') as f_handle:
                input_txt = f_handle.read()

            self.assertIsNotNone(input_txt)

            result_str, result_df = b64.unpack_items(input_string=input_txt, trace=True)
            print(result_str)
            #assert result_df.shape == (2, 12)
            self.assertIsNotNone(result_str)
            self.assertIsNotNone(result_df)

        except FileNotFoundError as ex:
            self.fail(msg='Exception {}'.format(str(ex)))

    def test_nested_archive(self):
        try:
            input_txt = None
            FILE_NAME = 'msticpy/tests/testdata/base64msg.txt'
            with open(FILE_NAME, 'r') as f_handle:
                input_txt = f_handle.read()

            self.assertIsNotNone(input_txt)

            result_str, result_df = b64.unpack_items(input_string=input_txt, trace=True)
            assert result_df.shape == (8, 12)
            self.assertIsNotNone(result_str)
            self.assertIsNotNone(result_df)

        except FileNotFoundError as ex:
            self.fail(msg='Exception {}'.format(str(ex)))

    def test_nested_archive_df(self):
        try:
            input_txt = None
            FILE_NAME = 'msticpy/tests/testdata/base64msg.txt'
            with open(FILE_NAME, 'r') as f_handle:
                input_txt = f_handle.read()

            self.assertIsNotNone(input_txt)
            # create datframe for input with 2 rows and add same data to both
            input_df = pd.DataFrame(data=['a', 'b'], columns=['input'], index=[0, 1])
            input_df['input'] = input_txt
            result_df = b64.unpack_items(data=input_df, column='input', trace=True)
            # we should get 2x the rows as the previous test (since data is duplicated)
            # plus 2 added columns
            assert result_df.shape == (16, 14)
            self.assertIsNotNone(result_df)

        except FileNotFoundError as ex:
            self.fail(msg='Exception {}'.format(str(ex)))

if __name__ == '__main__':
    unittest.main()
    print('bye')
