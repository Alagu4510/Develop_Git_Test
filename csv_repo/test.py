import pytest
from main import *



def test_fetch_repo_info():
    # Test case 1: Repository exists
    repo_info = fetch_repo_info("existing-repo", "existing-user")
    assert repo_info is not None

    # Test case 2: Repository doesn't exist
    repo_info = fetch_repo_info("non-existing-repo", "existing-user")
    assert repo_info is None

    # Add more test cases as needed
