#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import datetime

import sae
import web

import md5

from urls import urls       
from settings import global_render , admin_render
from settings import load_sqla ,store
from web import form
from models	import Article , Comment , Classes , Admins



class Index(object):
	def GET(self):
		article_list = web.ctx.orm.query(Article).order_by( Article.posttime.desc()).all()
		return global_render.index(article_list=article_list)
	

class Content(object):
	def GET(self,id):
		article=web.ctx.orm.query(Article).filter_by(aid=int(id)).all()[0]
		comments = web.ctx.orm.query(Comment).filter_by(aid=int(id)).all()
		return global_render.content(comments=comments,article=article)
	def POST(self,id):
		i=web.input()
		article=web.ctx.orm.query(Article).filter_by(aid=int(id)).all()[0]
		article.commentnumber = article.commentnumber+1
		comment=Comment()
		comment.aid=int(id)
		comment.posttime = datetime.datetime.now()
		comment.username = i.comment_username
		comment.email	 = i.comment_email
		comment.content  = i.comment_content
		web.ctx.orm.add(comment)
		web.ctx.orm.commit()
		raise web.seeother('/')
	
class Add_article(object):
	def GET(self):
		if session.loggin == True:		
			article = Article()
			return admin_render.edit(article=article)	
		else:
			raise web.seeother('/login')
	def POST(self):
		if session.loggin == True:		
			i = web.input()
			a = Article()
			a.title = i.title
			a.content = i.content
			a.posttime =  datetime.datetime.now()  
			web.ctx.orm.add(a)
			raise web.seeother('/')
		else:
			raise web.seeother('/login')
		

class Edit_article(object):
	def GET(self,id):
		if session.loggin == True:		
			article=web.ctx.orm.query(Article).filter_by(aid=int(id)).all()[0]
			return admin_render.edit(article=article)	
		else:
			raise web.seeother('/login')
		
	def POST(self,id):
		if session.loggin == True:		
			i = web.input()
			a = web.ctx.orm.query(Article).filter_by(aid=int(id)).all()[0]
			a.title = i.title
			a.content = i.content
			a.posttime =  datetime.datetime.now() 
			web.ctx.orm.commit()
			raise web.seeother('/manage')
		else:
			raise web.seeother('/login')
		

class Delete_article(object):
	def GET(self,id):
		if session.loggin == True:
			a = web.ctx.orm.query(Article).filter_by(aid=int(id)).all()[0]
			web.ctx.orm.delete(a)
			raise web.seeother('/manage')	
		else:
			raise web.seeother('/login')

class Manage(object):
	def GET(self):
		if session.loggin == True:		
			article_list = web.ctx.orm.query(Article).order_by( Article.posttime.desc()).all()
			return admin_render.manage(items=article_list)
		else:
			raise web.seeother('/login')

	def POST(self):
		if session.loggin == True:		
			i = web.input()
			a = Article()
			a.title = i.title
			a.content = i.content
			a.posttime =  datetime.datetime.now()  
			web.ctx.orm.add(a)
			raise web.seeother('/manage')
		else:
			raise web.seeother('/login')
		
	
class Login(object):
	def GET(self):
		return admin_render.login()
	
	def POST(self):
		i=web.input()
		username = i.username.strip()
		password = i.password.strip()
		user = web.ctx.orm.query(Admins).filter_by(username=username).all()[0]
		if md5.new(password).hexdigest() == user.userpass :
			session.loggin = True
			session.username = username
			raise web.seeother('/manage')
		else:
			raise web.seeother('/login')



def notfound():
    return  web.notfound(global_render.page404())

def internalerror():
    return web.internalerror(global_render.page500())


app = web.application(urls, globals())
app.add_processor(load_sqla)
#app.notfound = notfound
#app.internalerror = internalerror


#use session in debug modal
if web.config.get('_session') is None:
    session = web.session.Session(app, store)
    web.config._session = session
else:
    session = web.config._session

application = sae.create_wsgi_app(app.wsgifunc())

web.config.debug = True



