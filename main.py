# main.py

import asyncio
from telegram_utils import get_latest_channel_message, send_message_to_selected_chats, load_chat_ids
from config import API_ID, API_HASH, PHONE_NUMBER, CHANNEL_ID

async def main():
    # Создаем экземпляр клиента
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        # Авторизация
        await client.start(PHONE_NUMBER)
        
        # Загружаем список идентификаторов чатов из файла
        chat_ids = load_chat_ids('chat_ids.txt')  # Укажите путь к вашему файлу

        # Получаем последнее сообщение из канала
        latest_message = await get_latest_channel_message(client, CHANNEL_ID)

        if latest_message:
            # Отправляем сообщение в указанные чаты
            await send_message_to_selected_chats(client, latest_message, chat_ids)
        else:
            print("Нет доступных сообщений для отправки.")

# Запуск главной функции
if __name__ == "__main__":
    asyncio.run(main())
