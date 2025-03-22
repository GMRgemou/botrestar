from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.log import logger
import os
import sys
import subprocess
#这里可以换成自己的密钥
restart = on_command("re", rule=to_me(), permission=SUPERUSER, priority=5)

@restart.handle()
async def handle_restart(bot: Bot, event: MessageEvent):
    await restart.send("正在重启，稍等喵")
    python = sys.executable
    script = os.path.abspath(sys.argv[0])

    try:
        subprocess.Popen([python, script])
        sys.exit(0)
    except Exception as e:
        logger.error(f"重启失败：{e}")
        await restart.finish("重启失败了")