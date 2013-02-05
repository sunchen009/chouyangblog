#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sae
import web

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , Text , DateTime


Base = declarative_base()

class Article(Base):
	__tablename__ = 'articles'
	
	aid          	= Column(Integer ,primary_key = True)
	title       	= Column(String(100))
	content			= Column(Text)
	posttime		= Column(DateTime)
	classid		 	= Column(Integer)
	classname		= Column(String(20))
	pv				= Column(Integer)
	tags		 	= Column(String(50))
	commentnumber 	= Column(Integer)
	summary			= Column(Text)

#	def __init__(self,title,content):
#		self.title = title
#		self.content = content
		

#	def __repr__(self):
#		return "<Arcticle('%d','%s','%s','%s','%d','%s','%d')>"
#		%(self.id , self.title , self.content , self.posttime , self.classid , self.tags , self.commentnumber)


class Comment(Base):	
	__tablename__ = 'comments'	
	cid 	= Column(Integer ,primary_key = True)
	aid		= Column(Integer)
	posttime= Column(DateTime)
	content	= Column(Text)
	email	= Column(String(50))
	username= Column(String(20))
	
#	def __init__(self, aid, posttime , content , email , username):
#		self.aid		= 	aid
#		self.posttime	=	posttime
#		self.content	=	content	
#		self.email		=	email
#		self.username	=	username

#	def __repr__(self):
#		return "Comment<'%s' , '%s' , '%s'>" 	/
#		%(self.posttime , self.content , self.username)


class Classes(Base):	
	__tablename__	= 'classes'	
	
	classid		= Column(Integer , primary_key = True )
	classname 	= Column(String(20))

#	def __init__(self, classname):
#		self.classname	=	classname

#	def __repr__(self):
#		return "Classes<'%s','%s'>" /
#		%(self.classid , self.classname)
#	

class Admins(Base):
	__tablename__ = 'admins'

	uid = Column(Integer , primary_key = True )
	username = Column(String(20))
	userpass = Column(String(100))