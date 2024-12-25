# telegram_utils.py

from telethon import TelegramClient
from telethon.tl.types import PeerChannel
from typing import List
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_latest_channel_message(client: TelegramClient, channel_id: str) -> str:
    """
    Получает последнее сообщение из указанного канала.

    :param client: экземпляр TelegramClient
    :param channel_id: ID или username канала
    :return: текст последнего сообщения канала
    """
    try:
        channel = await client.get_entity(channel_id)
        async for message in client.iter_messages(channel, limit=1):
            return message.message  # Эмодзи будут частью текста
    except Exception as e:
        logger.error(f"Ошибка при получении сообщения: {e}")
    return ""

async def send_message_to_selected_chats(client: TelegramClient, message: str, chat_ids: List[str]):
    """
    Отправляет сообщение в указанные чаты.

    :param client: экземпляр TelegramClient
    :param message: текст сообщения для отправки
    :param chat_ids: список идентификаторов чатов
    """
    for chat_id in chat_ids:
        try:
            entity = await client.get_entity(chat_id)
            await client.send_message(entity, message)
            logger.info(f"Сообщение отправлено в чат: {chat_id}")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения в чат {chat_id}: {e}")

def load_chat_ids(file_path: str) -> List[str]:
    """
    Загружает идентификаторы чатов из файла.

    :param file_path: Путь к файлу с идентификаторами
    :return: Список chat_ids
    """
    with open(file_path, 'r') as file:
        chat_ids = [line.strip() for line in file.readlines()]
    return chat_ids
