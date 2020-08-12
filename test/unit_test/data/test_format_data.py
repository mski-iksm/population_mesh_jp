import unittest

import numpy as np

from population_mesh_jp.data.format_data import FormatToArray


class TestFormatToArray(unittest.TestCase):
    def test_run(self):
        data = dict(GET_STATS_DATA=dict(STATISTICAL_DATA=dict(DATA_INF=dict(
            VALUE=[
                {'@cat01': 'T000609001', '@area': '543700041', '@unit': '人', '$': '1'},
                {'@cat01': 'T000609001', '@area': '543700042', '@unit': '人', '$': '2'},
                {'@cat01': 'T000609001', '@area': '543700043', '@unit': '人', '$': '3'},
                {'@cat01': 'T000609001', '@area': '543700044', '@unit': '人', '$': '4'},
                {'@cat01': 'T000609001', '@area': '543700051', '@unit': '人', '$': '5'},
                {'@cat01': 'T000609001', '@area': '543700052', '@unit': '人', '$': '6'},
                {'@cat01': 'T000609001', '@area': '543700053', '@unit': '人', '$': '7'},
            ]

        ))))
        resulted = FormatToArray._make_array(data=data)
        expected = np.ones((8 * 10 * 2, 8 * 10 * 2)) * -9999
        expected[0, 8] = 1
        expected[0, 9] = 2
        expected[0, 10] = 5
        expected[0, 11] = 6
        expected[1, 8] = 3
        expected[1, 9] = 4
        expected[1, 10] = 7
        expected = np.flipud(expected).astype(np.int32)

        np.testing.assert_array_equal(resulted, expected)

    def test_decompose_item(self):
        resulted = FormatToArray._decompose_item(single_data={'@cat01': 'T000609001', '@area': '543700043', '@unit': '人', '$': '3'})
        self.assertEqual(resulted, (1, 8, 3))
