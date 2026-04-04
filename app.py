def home():
    return "Bot is Running 🚀"

async def start_bot():
    import asyncio
    import logging

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    from main import app as bot_client
    from start import register_start_handlers
    from status import register_status_handlers
    from us import register_us_handlers
    from video import register_video_handlers
    from cancel import register_cancel_handlers
    from getid import register_getid_handlers

    logger = logging.getLogger(__name__)

    register_start_handlers(bot_client)
    register_status_handlers(bot_client)
    register_us_handlers(bot_client)
    register_video_handlers(bot_client)
    register_cancel_handlers(bot_client)
    register_getid_handlers(bot_client)

    logger.info("Starting bot...")

    await bot_client.start()
    await asyncio.Event().wait()


def run_bot():
    import asyncio

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(start_bot())
    except Exception as e:
        print(f"Bot Error: {e}")
