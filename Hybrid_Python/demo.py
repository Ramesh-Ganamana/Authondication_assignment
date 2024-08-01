
import pytest

def test_example(setup):
    # Use the 'setup' fixture
    driver = setup
    driver.get("https://www.google.com")