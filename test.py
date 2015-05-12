# -*- coding: utf-8 -*-
from openerp import models, fields

class author(models.Model):
    _name = 'test.author'
    _rec_name = 'lastname'
    firstname = fields.Char('FirstName', required=True)
    lastname = fields.Char('LastName', required=True)
    cin = fields.Char('cin', required=True)
    book_ids = fields.One2many('test.book','author_id','Books')
    ville_id = fields.Many2one('test.ville' , 'ville')

 
class book(models.Model):
    _name = 'test.book'
    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    author_id = fields.Many2one('test.author','Author',ondelete='cascade')

class ville(models.Model):
    _name = 'test.ville'
    name = fields.Char('ville', required=True)
    
     
