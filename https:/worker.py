from pyrogram import Client, enums
import asyncio

# بيانات حساباتك الـ 10
API_ID = 123456 # الـ API ID الخاص بك
API_HASH = "hash_here" # الـ API Hash الخاص بك

# البروكسي الدوار من صورتك
PROXY = {
    "scheme": "http",
    "hostname": "107.173.128.95",
    "port": 7549,
    "username": "wqgarwtp",
    "password": "0gw21xt85dpu"
}

# أسماء جلسات الحسابات (يجب أن تكون ملفات .session موجودة)
SESSIONS = ["acc1", "acc2", "acc3", "acc4", "acc5", "acc6", "acc7", "acc8", "acc9", "acc10"]

async def start_reporting(target_link, platform):
    async def task(session_name):
        try:
            async with Client(f"sessions/{session_name}", api_id=API_ID, api_hash=API_HASH, proxy=PROXY) as app:
                # هنا يتم تنفيذ البلاغ
                await app.report_peer(target_link, reason=enums.ReportReason.SPAM)
                print(f"Done: {session_name}")
        except Exception as e:
            print(f"Error {session_name}: {e}")

    jobs = [task(s) for s in SESSIONS]
    await asyncio.gather(*jobs)
