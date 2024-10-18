import os
from git import Repo
from collections import Counter


def get_most_frequently_changed_files(repo_path, num_files=10):
    # Открываем репозиторий
    repo = Repo(repo_path)

    # Получаем все коммиты
    commits = list(repo.iter_commits('main'))

    # Счетчик для файлов
    file_changes = Counter()

    # Проходим по всем коммитам и подсчитываем изменения файлов
    for commit in commits:
        for file in commit.stats.files:
            file_changes[file] += 1

    # Возвращаем наиболее часто изменяемые файлы
    return file_changes.most_common(num_files)


if __name__ == "__main__":
    # Путь к вашему локальному репозиторию
    repo_path = "../"  # Текущая директория, измените при необходимости

    # Получаем 10 наиболее часто изменяемых файлов
    most_changed = get_most_frequently_changed_files(repo_path)

    print("Наиболее часто изменяемые файлы:")
    for file, count in most_changed:
        print(f"{file}: {count} изменений")