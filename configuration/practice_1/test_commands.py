import os
import pytest
from commands import LSCommand, CDCommand, WhoamiCommand, ClearCommand, FindCommand


@pytest.fixture
def create_test_dir():
    test_dir = "test_dir"
    sub_dir = os.path.join(test_dir, "subdir")
    os.makedirs(sub_dir, exist_ok=True)
    with open(os.path.join(test_dir, "file1.txt"), "w") as f:
        f.write("test file")
    with open(os.path.join(sub_dir, "file2.txt"), "w") as f:
        f.write("test file")
    yield test_dir
    # Tear down
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(test_dir)


def test_ls_current_directory(create_test_dir):
    result = LSCommand.run('ls', create_test_dir)
    assert 'file1.txt' in result
    assert 'subdir' in result


def test_ls_nonexistent_directory():
    result = LSCommand.run('ls', "nonexistent_dir")
    assert "Error" in result


def test_ls_empty_directory(create_test_dir):
    empty_dir = os.path.join(create_test_dir, "subdir")
    result = LSCommand.run('ls', empty_dir)
    assert "file2.txt" in result


@pytest.fixture
def create_cd_test_dir():
    test_dir = "test_cd_dir"
    os.makedirs(test_dir, exist_ok=True)
    yield test_dir
    os.rmdir(test_dir)


def test_cd_existing_directory(create_cd_test_dir):
    result = CDCommand.run('cd', os.getcwd(), create_cd_test_dir)
    assert result == os.path.abspath(create_cd_test_dir)


def test_cd_nonexistent_directory():
    result = CDCommand.run('cd', os.getcwd(), "nonexistent_dir")
    assert "Error" in result


def test_cd_to_root():
    result = CDCommand.run('cd', os.getcwd(), '/')
    assert result == os.path.abspath('/')


def test_whoami():
    result = WhoamiCommand.run('whoami')
    assert result == os.getlogin()


@pytest.fixture
def create_find_test_dir():
    test_dir = "test_find_dir"
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, "file1.txt"), "w") as f:
        f.write("test file")
    with open(os.path.join(test_dir, "file2.txt"), "w") as f:
        f.write("test file")
    yield test_dir
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(test_dir)


def test_find_existing_file(create_find_test_dir):
    result = FindCommand.run('find', create_find_test_dir, 'file1.txt')
    assert 'file1.txt' in result


def test_find_nonexistent_file(create_find_test_dir):
    result = FindCommand.run('find', create_find_test_dir, 'nonexistent_file.txt')
    assert "no results" in result


def test_find_in_empty_directory(create_find_test_dir):
    empty_dir = os.path.join(create_find_test_dir, 'empty_dir')
    os.makedirs(empty_dir, exist_ok=True)
    result = FindCommand.run('find', empty_dir, 'file')
    assert "no results" in result
