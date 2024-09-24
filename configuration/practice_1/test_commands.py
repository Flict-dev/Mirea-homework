import pytest
from zipfile import ZipFile
from io import BytesIO
from commands import LSCommand, CDCommand, ExitCommand, WhoamiCommand, ClearCommand, FindCommand
@pytest.fixture
def vfs():
    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, 'w') as zf:
        zf.writestr('folder1/file1.txt', '')
        zf.writestr('folder1/file2.txt', '')
        zf.writestr('folder2/file3.txt', '')
    zip_buffer.seek(0)
    return ZipFile(zip_buffer, 'r')

def test_ls_lists_files_in_current_directory(vfs):
    result = LSCommand.run(vfs, '/folder1/')
    assert 'file1.txt' in result
    assert 'file2.txt' in result
    assert 'file3.txt' not in result

def test_ls_empty_directory(vfs):
    result = LSCommand.run(vfs, '/empty_folder/')
    assert result == ''

def test_ls_root_directory(vfs):
    result = LSCommand.run(vfs, '/')
    assert 'folder1' in result
    assert 'folder2' in result

def test_cd_to_subdirectory(vfs):
    result = CDCommand.run(vfs, '/', 'folder1')
    assert result == '/folder1/'

def test_cd_to_parent_directory(vfs):
    result = CDCommand.run(vfs, '/folder1/', '..')
    assert result == '/'

def test_cd_non_existent_directory(vfs):
    result = CDCommand.run(vfs, '/', 'non_existent_folder')
    assert result == 'Error: path not found'

    def test_exit_command(vfs):
        result = ExitCommand.run(vfs, '/')
        assert result == 'exit'

def test_exit_command_with_args(vfs):
    result = ExitCommand.run(vfs, '/', 'some_arg')
    assert result == 'exit'

def test_exit_does_not_affect_state(vfs):
    initial_path = '/'
    result = ExitCommand.run(vfs, initial_path)
    assert result == 'exit'
    assert initial_path == '/'


def test_whoami_command(vfs):
    result = WhoamiCommand.run(vfs, '/')
    assert result == 'root'

def test_whoami_with_args(vfs):
    result = WhoamiCommand.run(vfs, '/', 'extra_arg')
    assert result == 'root'

def test_whoami_in_different_directory(vfs):
    result = WhoamiCommand.run(vfs, '/folder1/')
    assert result == 'root'


def test_find_file_in_vfs(vfs):
    result = FindCommand.run(vfs, '/', 'file1.txt')
    assert 'file1.txt' in result

def test_find_file_not_found(vfs):
    result = FindCommand.run(vfs, '/', 'nonexistent_file.txt')
    assert result == 'Error: path not found'

def test_find_without_arguments(vfs):
    result = FindCommand.run(vfs, '/')
    assert result == 'Error: not enough arguments'


def test_clear_command(vfs):
    result = ClearCommand.run(vfs, '/')
    assert result == 'clear'

def test_clear_with_args(vfs):
    result = ClearCommand.run(vfs, '/', 'extra_arg')
    assert result == 'clear'

def test_clear_in_different_directory(vfs):
    result = ClearCommand.run(vfs, '/folder1/')
    assert result == 'clear'
