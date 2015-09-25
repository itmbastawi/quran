# -*- coding: utf-8 -*-
db.define_table('quranj',
                Field('juza','string'),
                Field('readj','boolean'))
db.define_table('quranh', 
                Field('hizb','string'),
                Field('readh','boolean'))
db.define_table('quranq',
                Field('quarter','string'),
                Field('readr','boolean'))
#الاحصائيات
db.define_table('ehsaa',
                Field('khatma','string'),
                Field('numberkh','integer'),
                Field('datelast','datetime'))
