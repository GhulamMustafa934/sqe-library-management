import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import fine_tier


@pytest.mark.parametrize('days,expected', [
    (0, 'None'),
    (4, 'Low'),
    (10, 'Medium'),
    (20, 'High'),
    (45, 'Severe'),
])
def test_fine_tier_valid_classes(days, expected):
    """Test valid equivalence classes for fine_tier."""
    assert fine_tier(days) == expected


def test_fine_tier_negative_days_raises():
    """Test that negative days raise ValueError."""
    with pytest.raises(ValueError):
        fine_tier(-3)