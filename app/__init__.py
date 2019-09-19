import os

from dotenv import load_dotenv
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

load_dotenv()
vk_bot_id = os.getenv("VK_BOT_ID")
vk_bot_api_token = os.getenv("VK_BOT_API_TOKEN")

vk_session = VkApi(token=vk_bot_api_token)
vk_longpoll = VkBotLongPoll(vk_session, vk_bot_id)


def run():
    for event in vk_longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
