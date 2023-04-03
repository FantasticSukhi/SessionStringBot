import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("𝔄𝔟𝔢 𝔟𝔬𝔱 𝔨𝔬 𝔰𝔱𝔞𝔯𝔱 𝔨𝔞𝔯 𝔯𝔥𝔞 𝔥𝔲...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("𝔗𝔢𝔯𝔦 API_ID/API_HASH 𝔖𝔞𝔥𝔦 𝔫𝔞𝔥𝔦 𝔥𝔞𝔦.")
    except AccessTokenInvalid:
        raise Exception("𝔗𝔢𝔯𝔦 BOT_TOKEN 𝔖𝔞𝔥𝔦 𝔫𝔞𝔥𝔦 𝔥𝔞𝔦.")
    uname = app.get_me().username
    print(f"@{uname} 𝔖𝔱𝔞𝔯𝔱 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 !")
    idle()
    app.stop()
    print("𝔅𝔬𝔱 𝔖𝔱𝔬𝔭𝔭𝔢𝔡.......... !")
