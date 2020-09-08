from aiogram.utils import json
from aiohttp import web
import hashlib

import dbmodule


async def login(request):
    j = await request.json()
    username = j["username"]
    password = j["password"]
    ip = j["ip"]
    api = j["apiKey"]
    hashed = await dbmodule.get_password(username)
    passw = hashlib.md5(password.encode('utf-8'))
    passw = passw.hexdigest()
    print(passw)
    if hashed == passw:
        print(ip)
        print(api)
        resp = json.dumps({"username": username, "permissions": 0})
    else:
        resp = json.dumps({"error": "Неверный логин или пароль"})
    return web.Response(text=(resp))


async def register(request):
    j = json.loads(request)
    username = j['username']
    password = j['password']
    email = j['email']
    r = await dbmodule.check_user(username)
    await dbmodule.registeruser(username, password)
    return web.Response(text="OK")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.post('/login', login)])
    app.add_routes([web.post('/register', register)])
    web.run_app(app, host="0.0.0.0", port=7777)
