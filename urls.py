#!/usr/bin/env python
#-*- coding: utf-8 -*-

urls = (
    '/' 			,	'Index',
    '/index/(\d+)/(.+)'	,	'ClassIndex',
    '/page/(.+)'   ,   'Page',
    '/article/(.+)'	,	'Content',
    '/add'			,	'Add_article',
    '/edit/(.+)'	,	'Edit_article',
    '/manage'		,	'Manage',
    '/delete/(.+)'	,	'Delete_article',
    '/login'		,	'Login',
    '/addclass'    ,   'ClassesTool'
    
   # '/.*?'			,	'notfound',
)