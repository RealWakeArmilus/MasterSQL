#######
MasterSQL
#######


.. image:: https://img.shields.io/pypi/l/mastersql.svg?style=flat-square
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License


Документация по использованию SQL-запросов
==========================================

Базовые принципы SQL-запросов
-----------------------------

SQL (Structured Query Language) используется для работы с базами данных. Основные задачи: извлечение, вставка, обновление, удаление данных и управление структурой базы данных. Запросы строятся из ключевых слов (например, SELECT, INSERT), которые определяют действие, и указания условий, например, WHERE или ORDER BY.

Виды запросов
-------------

**1. DDL (Data Definition Language).**

- ``CREATE`` – создание таблицы или базы данных.
  Пример:

  .. code:: sql

    CREATE TABLE {name_table} ({columns and types});

  Создаёт таблицу.

- ``ALTER`` – изменение таблицы. (Переименовать таблицу. Добавьте новый столбец в таблицу).
  Пример:

  .. code:: sql

    ALTER TABLE {name_table} ADD {one_column and type};

  Добавляет новый столбец.

- ``DROP`` – удаление таблицы или базы.
  Пример:

  .. code:: sql

    DROP TABLE {name_table};

  Удаляет таблицу.

**2. DML (Data Manipulation Language).**

- ``SELECT`` – выборка данных из таблицы.
  Пример:

  .. code:: sql

    SELECT {columns} FROM {name_table} WHERE age > 18;
  Выводит имена пользователей старше 18 лет.  

- ``INSERT`` – добавление записей в таблицу.
  Пример:

  .. code:: sql

    INSERT INTO {name_table} ({columns}) VALUES ('Иван', 25);
  Добавляет новую запись.  

- ``UPDATE`` – обновление записей.
  Пример:

  .. code:: sql

    UPDATE {name_table} SET age = 30 WHERE name = 'Иван';
  Изменяет возраст на 30 для пользователя Иван.  

- ``DELETE`` – удаление записей.
  Пример:

  .. code:: sql

    DELETE FROM {name_table} WHERE age < 18;
  Удаляет всех пользователей младше 18 лет.

**3. DCL (Data Control Language).**

- ``GRANT`` – предоставление прав.
  Пример:

  .. code:: sql

    GRANT SELECT ON {name_table} TO 'admin';
  Даёт права на просмотр данных пользователю admin.  

- ``REVOKE`` – удаление прав.
  Пример:

  .. code:: sql

    REVOKE SELECT ON {name_table} FROM 'admin';
  Удаляет права.  

**4. TCL (Transaction Control Language).**

- ``BEGIN`` – начало транзакции.
- ``COMMIT`` – подтверждение изменений.
- ``ROLLBACK`` – отмена изменений.

Применение в конкретных случаях
-------------------------------

1. Создание аналитического отчета. Используем ``SELECT`` с функциями группировки, например, `GROUP BY` и `SUM`.
   Подсчёт выручки по регионам.  

2. Добавление новых записей в CRM-систему.  
   ``INSERT`` используется для записи информации о новых клиентах.

3. Обновление устаревших данных.  
   ``UPDATE`` подходит для массового изменения значений, например, изменения цен в каталоге товаров.

4. Оптимизация базы.  
   ``ALTER`` и ``DROP`` применяются для управления структурой таблиц, удаления ненужных колонок или индексов.


Примеры использования SQL-запросов в реальных сценариях. Ниже приведены запросы с пояснениями, где и как их можно применять.
----------------------------------------------------------------------------------------------------------------------------

**1. SELECT id, name FROM users WHERE status = 'active' AND age = '30' ORDER BY name ASC LIMIT 10**

**Цель:**
Получение отфильтрованного списка пользователей из таблицы `users` на основе заданных условий, 
а именно проверка статуса на 'active' и возраст ранвый 30 лет. А так же фильтрация по алфавиту.

**Примеры использования:**
- **Административные панели:** Отображение списка активных пользователей с пагинацией в интерфейсе администратора.
- **Клиентские интерфейсы:** Вывод пользователей (например, активных клиентов) в веб- или мобильном приложении.
- **Отчёты:** Формирование выборки пользователей для анализа демографических данных или выполнения бизнес-метрик.


**2. INSERT INTO users (name, age, status) VALUES ('John Doe', '30', 'active')**

**Цель:**
Добавление новой записи в таблицу `users`.

**Примеры использования:**
- **Регистрация пользователей:** Сохранение данных нового пользователя после регистрации.
- **Миграция данных:** Импорт данных из внешних источников при интеграции систем.
- **Автоматическое обновление данных:** Динамическое добавление данных в базу в рамках автоматизированных процессов.

**3. UPDATE users SET name = 'Jane Doe' WHERE id = '1'**

**Цель:**
Обновление определённых полей в таблице `users` на основе условия.

**Примеры использования:**
- **Обновление профиля пользователя:** Изменение информации о пользователе через интерфейс управления профилем.
- **Коррекция данных:** Исправление некорректных или неполных записей в базе данных.
- **Синхронизация данных:** Актуализация данных из внешних источников, таких как CRM или ERP-системы.


**4. DELETE FROM users WHERE status = 'inactive'**

**Цель:**
Удаление записей из таблицы `users`, соответствующих заданным критериям.

**Примеры использования:**
- **Очистка базы данных:** Удаление неактивных или устаревших записей для оптимизации производительности.
- **Соответствие законодательству:** Удаление данных пользователей по их запросу (например, в рамках GDPR).
- **Автоматическая очистка:** Периодическое удаление неактивных учётных записей для упрощения структуры базы данных.


**Общие области применения**

**1. Веб-приложения:**
- CRUD-операции для управления данными пользователей (например, регистрация, вход в систему, обновление профиля).
- Динамическая фильтрация, сортировка и пагинация данных в пользовательских интерфейсах.

**2. Административные панели:**
- Углублённая фильтрация и модификация данных для внутренних команд.
- Автоматизация процессов обновления и очистки данных для поддержания их целостности.

**3. CRM/ERP системы:**
- Управление данными клиентов, включая массовое обновление и синхронизацию.
- Интеграция данных между различными системами.

**4. Аналитика и отчёты:**
- Извлечение данных для создания отчётов или передачи в системы бизнес-аналитики (BI).
- Фильтрация данных для анализа демографических и бизнес-метрик.

**5. Мобильные приложения:**
- Работа серверной части, поддерживающей пользовательские операции, такие как управление профилем, поиск пользователей, обновления в реальном времени.


**Краткое описание CRUD операций**

+------------+---------------------------------------------------------+-----------------------------------+
| Операция   | Пример запроса                                          | Цель                              |
+============+=========================================================+===================================+
| **Create** | ``INSERT INTO users (...) VALUES (...)``                | Добавление новых записей.         |
+------------+---------------------------------------------------------+-----------------------------------+
| **Read**   | ``SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...``| Получение и фильтрация данных.    |
+------------+---------------------------------------------------------+-----------------------------------+
| **Update** | ``UPDATE ... SET ... WHERE ...``                        | Изменение существующих данных.    |
+------------+---------------------------------------------------------+-----------------------------------+
| **Delete** | ``DELETE FROM ... WHERE ...``                           | Удаление ненужных записей.        |
+------------+---------------------------------------------------------+-----------------------------------+

Эти SQL-запросы являются основой операций с базами данных и критически важны для построения надёжных и масштабируемых систем. Используйте их как базовые блоки для управления данными в ваших приложениях!
