import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os

def get_dependencies(package_name):
    url = f"https://pkgs.alpinelinux.org/package/v3.14/main/x86_64/{package_name}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Ошибка при получении данных для пакета {package_name}: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    dependencies = []
    depends_section = soup.find('summary', string=lambda text: text and 'Depends' in text)
    
    if depends_section:
        ul = depends_section.find_next('ul')
        if ul:
            for li in ul.find_all('li'):
                dep = li.text.strip()
                if dep.startswith("so:"):
                    dep = dep[3:]
                    dep = dep.split('.')[0]
                
                if dep and dep not in dependencies:
                    dependencies.append(dep)

    return dependencies


def create_dependency_graph_plantuml(package_name, output_file):
    visited = set()
    graph_lines = ['@startuml', 'left to right direction']
    
    def _build_graph(pkg):
        if pkg in visited:
            return
        
        visited.add(pkg)
        dependencies = get_dependencies(pkg)
        for dep in dependencies:
            graph_lines.append(f'"{pkg}" --> "{dep}"')
            _build_graph(dep)

    # Построение графа
    _build_graph(package_name)

    # Завершение графа
    graph_lines.append('@enduml')

    # Запись в файл
    with open(f"{output_file}.puml", 'w') as f:
        for line in graph_lines:
            f.write(line + '\n')
    print(f"Граф зависимостей сохранён в {output_file}.puml")
def main():
    # Загрузка конфигурации из XML-файла
    tree = ET.parse('config.xml')
    root = tree.getroot()

    package_name = root.find('package').text
    plantuml_path = root.find('plantuml_path').text

    # Создание графа зависимостей
    create_dependency_graph_plantuml(package_name, 'dependencies')

    # Визуализация графа
    os.system(f'java -jar {plantuml_path} dependencies.puml')

if __name__ == "__main__":
    main()