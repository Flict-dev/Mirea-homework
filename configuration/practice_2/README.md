# Practice 2
Этот проект предназначен для сбора зависимостей Alpine Linux пакетов и создания графа зависимостей в формате PlantUML.
```
@startuml
left to right direction
"curl" --> "ca-certificates"
"ca-certificates" --> "/bin/sh"
"ca-certificates" --> "libc"
"ca-certificates" --> "libcrypto"
"curl" --> "libc"
"curl" --> "libcurl"
"libcurl" --> "ca-certificates"
"libcurl" --> "libbrotlidec"
"libcurl" --> "libc"
"libcurl" --> "libcrypto"
"libcurl" --> "libnghttp2"
"libcurl" --> "libssl"
"libcurl" --> "libz"
"curl" --> "libz"
@enduml
```
![image](https://github.com/user-attachments/assets/dc8d7af7-769e-4807-8924-e3aced0bf8fa)

## Установка

Этот проект использует Poetry для управления зависимостями. Убедитесь, что Poetry установлен на вашем компьютере. Если нет, следуйте инструкциям на официальном сайте Poetry.

### Шаги установки:

1. Клонирование репозитория:

    
```bash
    git clone <URL_OF_YOUR_REPOSITORY>
    cd <NAME_OF_YOUR_PROJECT_DIRECTORY>
```
 
2. Установка зависимостей:

    В каталоге проекта выполните команду:

    
```bash
    poetry install
```
Это установит все зависимости, указанные в pyproject.toml.

## Запуск тестов

Тесты написаны с использованием pytest. Чтобы запустить тесты, выполните следующую команду:
```
poetry run pytest test_main.py
```
Эта команда активирует виртуальное окружение Poetry и выполнит pytest для тестирования кода.
<img width="1264" alt="image" src="https://github.com/user-attachments/assets/58047753-8177-478c-9e30-6d1462575ddd">

## Использование

1. Настройте файл config.xml для указания имени пакета и пути к jar-файлу PlantUML:
   
    
xml
    <config>
        <package>openssl</package>
        <plantuml_path>/path/to/plantuml.jar</plantuml_path>
    </config>
    
2. Запустите скрипт:
   
    
bash
    poetry run python main.py
    
Это создаст граф зависимостей в формате PlantUML в файле dependencies.puml и откроет его с помощью PlantUML.

## Примечания

- Убедитесь, что Java установлена и доступна в вашей системе, так как она необходима для работы PlantUML.
- В pyproject.toml могут быть дополнительными зависимости тестировщиков и инструментов разработки.
Эти инструкция позволят пользователям легко понять, как установить и использовать ваш проект с помощью Poetry. Замените <URL_OF_YOUR_REPOSITORY> и <NAME_OF_YOUR_PROJECT_DIRECTORY> на фактические URL и директории вашего проекта.
