#!/usr/bin/env python
#-*- coding: utf-8 -*-

urls = (
    '/' 			,	'Index',
    '/article/(.+)'	,	'Content',
    '/add'			,	'Add_article',
    '/edit/(.+)'	,	'Edit_article',
    '/manage'		,	'Manage',
    '/delete/(.+)'	,	'Delete_article',
    '/login'		,	'Login',
   # '/.*?'			,	'notfound',
)