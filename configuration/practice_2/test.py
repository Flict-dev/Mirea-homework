import pytest
from unittest.mock import patch, mock_open
from io import StringIO
from main import get_dependencies, create_dependency_graph_plantuml

mock_html_content = """
<html>
<body>
  <summary>Depends</summary>
  <ul>
    <li>lib1</li>
    <li>so:lib2.so.1</li>
  </ul>
</body>
</html>
"""

@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = mock_html_content.encode('utf-8')
        yield mock_get

def test_get_dependencies(mock_requests_get):
    deps = get_dependencies('sample-package')
    assert deps == ['lib1', 'lib2']


def test_create_dependency_graph_plantuml(mock_requests_get):
    with patch('builtins.open', mock_open()) as mock_file:
        create_dependency_graph_plantuml("sample-package", "dependencies")

        # Ожидаем, что open вызывается один раз
        mock_file.assert_called_once_with("dependencies.puml", 'w')

        # Проверка данных, записанных в файл
        handle = mock_file()
        written_data = "".join(call[0][0] for call in handle.write.call_args_list)

        assert '@startuml' in written_data
        assert '"sample-package" --> "lib1"' in written_data
        assert '"sample-package" --> "lib2"' in written_data
        assert '@enduml' in written_data