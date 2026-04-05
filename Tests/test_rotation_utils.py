"""
Program Name: test_rotation_utils
Name: Riddhi Agarwal
Purpose: The purpose of this program is to write test cases in order to 
         verify that the adjust_rotation function works correctly for different inputs.
         This program contains pytest.
Date: 04/05/2026
"""

import pytest

from rotation_utils import adjust_rotation


#Test normal input
def test_positive_input_100() -> None:
    assert adjust_rotation(100) == 100

#Test large inputs
def test_positive_input_460() -> None:
    assert adjust_rotation(460) == 100

def test_positive_input_820() -> None:
    assert adjust_rotation(820) == 100