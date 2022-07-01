# UGC
Сервис Notification. 
Ссылка на репозиторий для ревью.  
https://github.com/Neoduss/notifications_sprint_1


Комманды для запуска проекта
-

**make build_up**
- Поднимает все контейнеры
 
**make destroy**
- Убивает все контейнеры
- Чистит вольюмы

**Все комманды make**
- make help

Инфрастуктура
-

API доступен по адресу http://127.0.0.1/  
- Эндпоинт для отправки уведомлений http://127.0.0.1/app/v1/notification/send  
- Метод POST  
- Принимает уведомления от внешних сервисов
- Принимает уведомления от шедулера
- Документация достуна по адресу http://127.0.0.1/app/openapi  

Django admin доступен по адресу http://127.0.0.1/admin  
- Админ-панель для отправки уведомлений группам пользователей
- Создания групп рассылки

Worker_send_email  
- Собирает чанки
- Собирает письмо из данных для отправки
- Запрашивает недоставющие данные для отправки сообщения через API
- Отправляет письма пользователям

Worker_chunk
- Забирает из групповой очереди
- Разбивает групповые рассылки на чанки и отправляет в очередь сообщений

Настройки всех приложений объеденены в один [.env](/.env.example) файл

Архитектурные схемы
-
![Альтернативный текст](/diagram/diagram.png "Архитектура сервисов")
![Альтернативный текст](/diagram/rabbitmq.jpg "Архитектура RebbitMQ")

Схема сообщений
-
[message.json](/schemas/message.json)
```json
[
    {
      "type_send": "new_series",
      "template_id": "3507b67d-de18-420c-b410-3a48aa035698",
      "context": {
        "users_id": [
          "3507b67d-de18-420c-b410-3a48aa035698"
        ],
        "group_id": "85afd5db-5387-451d-bac0-929e65bb3163",
        "payload": {
          "films_data": [
            {
              "film_id": "88b95f93-dc50-4a2b-ab56-171f53496326",
              "film_name": "Film 1"
            },
            {
              "film_id": "e1d23244-6680-441c-8c07-98dc57b02ed0",
              "film_name": "Film 2"
            },
            {
              "film_id": "3fa0c771-53a4-4698-8aef-285f9cd4c5ba",
              "film_name": "Film 3"
            },
            {
              "film_id": "3b09f631-efa5-4be5-8f77-0f4bd60aa5b6",
              "film_name": "Film 4"
            },
            {
              "film_id": "045753cc-9d83-4ed9-a868-6e775132fb9c",
              "film_name": "Film 5"
            },
            {
              "film_id": "e56f8aa1-ad05-467a-87f3-4f9f0f13e072",
              "film_name": "Film 6"
            },
            {
              "film_id": "0b2ab939-8136-496f-b225-dfea222e99b9",
              "film_name": "Film 7"
            }
          ]
        },
        "link": "http://cinoteatr.ru/user/3507b67d-de18-420c-b410-3a48aa035698/data/"
      }
    }
  ]


```
