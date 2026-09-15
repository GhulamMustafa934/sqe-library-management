import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import fine_tier


# ---------------------------------------------------------------
# BVA Test Suite for fine_tier(days_overdue)
# Boundaries: 0 (edge), 0/1, 7/8, 14/15, 30/31
# ---------------------------------------------------------------

@pytest.mark.parametrize('days,expected', [
    # --- Domain edge (invalid -> valid) ---
    (0, 'None'),       # Boundary: 0 days -> None
    (1, 'Low'),        # Boundary +1: 1 day -> Low

    # --- Boundary 0/1 (None -> Low) ---
    (0, 'None'),       # value-1: 0 -> None
    (1, 'Low'),        # value: 1 -> Low
    (2, 'Low'),        # value+1: 2 -> Low

    # --- Boundary 7/8 (Low -> Medium) ---
    (7, 'Low'),        # value-1: 7 -> Low
    (8, 'Medium'),     # value: 8 -> Medium
    (9, 'Medium'),     # value+1: 9 -> Medium

    # --- Boundary 14/15 (Medium -> High) ---
    (14, 'Medium'),    # value-1: 14 -> Medium
    (15, 'High'),      # value: 15 -> High
    (16, 'High'),      # value+1: 16 -> High

    # --- Boundary 30/31 (High -> Severe) ---
    (30, 'High'),      # value-1: 30 -> High
    (31, 'Severe'),    # value: 31 -> Severe
    (32, 'Severe'),    # value+1: 32 -> Severe
])
def test_fine_tier_boundaries(days, expected):
    """BVA tests for fine_tier across all boundaries."""
    assert fine_tier(days) == expected


def test_fine_tier_negative_raises():
    """Test that negative days raise ValueError (domain edge)."""
    with pytest.raises(ValueError):
        fine_tier(-1)