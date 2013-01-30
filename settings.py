#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

import sae
import sae.const
import web

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


from web.contrib.template import render_jinja

# jinja2模板
app_root = os.path.dirname(__file__)
templates_path = os.path.join(app_root, 'templates\global').replace('\\', '/')

global_render = render_jinja(
        templates_path,   	# 设置模板路径.
        encoding = 'utf-8', # 编码.
    )

admin_render = render_jinja(
        os.path.join(app_root, 'templates\manage').replace('\\', '/'),     # 设置模板路径.
        encoding = 'utf-8', # 编码.
    )



# sqlalchemy
# create_engine(数据库://用户名:密码(没有密码则为空)@主机名:端口/数据库名',echo =True)
MYSQL_DB = sae.const.MYSQL_DB
MYSQL_USER = sae.const.MYSQL_USER
MYSQL_PASS = sae.const.MYSQL_PASS
MYSQL_HOST_M = sae.const.MYSQL_HOST
MYSQL_HOST_S = sae.const.MYSQL_HOST_S
MYSQL_PORT = int(sae.const.MYSQL_PORT)

mysql_engine = create_engine(
    'mysql://%s:%s@%s:%s/app_chouyangbox?charset=utf8' %
    (MYSQL_USER, MYSQL_PASS, MYSQL_HOST_M, MYSQL_PORT),
    encoding='utf8',
    echo=False,
    pool_recycle=5,
)

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=mysql_engine))
    try:
        return handler()
    except web.HTTPError:
       web.ctx.orm.commit()
       raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()




#Session in mysql
db = web.database(
                    dbn  = 'mysql',
                    user = MYSQL_USER,
                    pw   = MYSQL_PASS, 
                    host = MYSQL_HOST_M,
                    port = MYSQL_PORT, 
                    db   = MYSQL_DB
                )
store = web.session.DBStore(db, 'sessions')




