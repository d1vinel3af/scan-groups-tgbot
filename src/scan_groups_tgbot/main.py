from telethon import TelegramClient
from telethon import events
from core import settings

client = TelegramClient(
        'bot_session', 
        settings.api_id, 
        settings.api_hash
    ).start(
        bot_token=settings.api_bot_token
    )

@client.on(events.NewMessage(pattern='/members'))
async def get_usernames_only(event):
    try:
        chat = await event.get_chat()
        
        print("\n" + "=" * 50)
        print(f"USERNAME УЧАСТНИКОВ ЧАТА: {chat.title}")
        print("=" * 50)
        
        usernames = []
        total_members = 0
        
        async for user in client.iter_participants(chat):
            total_members += 1
            if user.username:
                usernames.append(user.username)
        
        # Выводим все username
        for i, username in enumerate(usernames, 1):
            print(f"{i}. @{username}")
        
        print(f"\n📊 Статистика:")
        print(f"Всего участников: {total_members}")
        print(f"С username: {len(usernames)}")
        print(f"Без username: {total_members - len(usernames)}")
        
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

print("🤖 Бот запущен! Отправьте /members в чате")
client.start()
