import hashlib

import asyncpg
import bcrypt


async def registeruser(username, password):
    conn = await asyncpg.connect(user='postgres', password='',
                                 database='', host='127.0.0.1')
    passw = hashlib.md5(password.encode('utf-8'))
    password = passw.hexdigest()
    permissions = 0
    await conn.execute('''INSERT INTO users(username, password, permissions) VALUES($1, $2, $3)''', username, password,
                       permissions)


async def get_password(username):
    conn = await asyncpg.connect(user='postgres', password='',
                                 database='', host='127.0.0.1')
    r = await conn.fetch('SELECT password FROM users WHERE username = $1', username)
    r = str(r).replace('[<Record password="', '').replace('">]', "")
    return r


async def check_user(username):
    conn = await asyncpg.connect(user='postgres', password='',
                                 database='', host='127.0.0.1')
    r = await conn.fetch('SELECT username FROM users WHERE username = $1', username)
    r = str(r).replace('[<Record username="', '').replace('">]', "")
    return r
