'''
Author: MB 790220273@qq.com
Date: 2024-02-04 17:30:26
LastEditors: MB 790220273@qq.com
LastEditTime: 2024-02-04 18:15:49
FilePath: \awesome-python3-webapp\www\static\orm.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging
    
import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

# 创建连接池
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        maxsize = kw.get("maxsize", 10),
        minsize = kw.get('minsize', 1),
        loop=loop
    )
    
# Select
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', "%s"), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs
        
# Insert Update Delete
async def execute(ql, args):
    

             
    