# Flask Account Generator

Flask Account Generator - это веб-приложение, созданное для генерации случайных учетных записей. Приложение разработано с использованием микрофреймворка Flask и упаковано в Docker-контейнер для удобства развертывания и изоляции зависимостей.

## Стек технологий
- **Flask**: Микрофреймворк для создания веб-приложений на Python.
- **SQLAlchemy**: ORM для работы с базами данных в Python.
- **PostgreSQL**: Выбрана в качестве системы управления базами данных.
- **Docker**: Используется для создания контейнеризованных приложений, обеспечивая легкость развертывания и совместимость.

## Установка и запуск

### Предварительные требования
Убедитесь, что на вашем компьютере установлен Docker

### Клонирование репозитория
```bash
git clone https://github.com/artyoma2000/docker-test.git
cd docker-test
```

### Сборка и запуск контейнера
```bash
docker-compose up --build
```

После выполнения этих команд приложение будет доступно по адресу `http://localhost:5000/`.

## Использование
Приложение предоставляет две основные функции:
- **Генерация учетных записей**: Нажмите кнопку "Generate and Save" на главной странице для создания новой учетной записи.
- **Просмотр учетных записей**: Нажмите кнопку "Show Accounts" для отображения всех сгенерированных учетных записей.

## Контакты
Если у вас возникли вопросы по проекту, пожалуйста, создайте issue в репозитории GitHub или свяжитесь с разработчиком напрямую.

---

Это описание предназначено для файла README.md вашего проекта на GitHub. Оно содержит краткое введение, описание используемого стека технологий и инструкции по установке и использованию приложения.
