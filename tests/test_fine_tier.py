import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import fine_tier


# ---------------------------------------------------------------
# Boundary tests for fine_tier
# ---------------------------------------------------------------

@pytest.mark.parametrize('days,expected', [
    # Boundary for None → Low
    (0, 'None'),
    (1, 'Low'),

    # Boundary for Low → Medium
    (7, 'Low'),
    (8, 'Medium'),

    # Boundary for Medium → High
    (14, 'Medium'),
    (15, 'High'),

    # Boundary for High → Severe
    (30, 'High'),
    (31, 'Severe'),
])
def test_fine_tier_boundaries(days, expected):
    assert fine_tier(days) == expected


# ---------------------------------------------------------------
# Valid equivalence classes (EP)
# ---------------------------------------------------------------

@pytest.mark.parametrize('days,expected', [
    (0, 'None'),
    (4, 'Low'),
    (10, 'Medium'),
    (20, 'High'),
    (45, 'Severe'),
])
def test_fine_tier_valid_classes(days, expected):
    assert fine_tier(days) == expected


# ---------------------------------------------------------------
# Negative input should raise ValueError
# ---------------------------------------------------------------

@pytest.mark.parametrize('days', [-3, -1])
def test_fine_tier_negative_days_raises(days):
    with pytest.raises(ValueError):
        fine_tier(days)