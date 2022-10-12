from operator import concat
import os
from pydoc import render_doc
import pandas as pd
from flask import (
    Flask,
    jsonify,
    json,
    Response,

)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete

from flask_restx import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
search_api = api.namespace('search',path='/wanted', description='조회 API')

app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


## MODEL 
class WantedCompany(db.Model):
    __tablename__ = "wantedcompany"

    id = db.Column(db.Integer, primary_key=True)
    company_ko = db.Column(db.Text)
    company_en = db.Column(db.Text)
    company_ja = db.Column(db.Text)
    tag_ko = db.Column(db.Text)
    tag_en = db.Column(db.Text)
    tag_ja = db.Column(db.Text)

   
@search_api.route("/companylist", methods=['GET'])
class CompanyList(Resource):
    @search_api.doc(responses={200: 'Success'})
    @search_api.doc(responses={404: 'Not found'})
    def get(self):
        WantedCompany_all = WantedCompany.query.all()
        results = []

        for company in WantedCompany_all:
            obj = {
                'id' : company.company_ko,
                'company_ko' : company.company_ko,
                'company_en' : company.company_en,
                'company_ja' : company.company_ja,
                'tag_ko' : company.tag_ko,
                'tag_en' : company.tag_en,
                'tag_ja' : company.tag_ja
            
            }
            results.append(obj)

        return jsonify(results,200)
    
    
@search_api.route("/search/name/<string:name_type>/<string:value>", methods=['GET'])
class CompnayNameSearch(Resource):
    @staticmethod    
    @search_api.doc(responses={200: 'Success'})
    @search_api.doc(responses={201: 'Create'})
    @search_api.doc(responses={204: 'Delete'})
    @search_api.doc(responses={404: 'Not found'})
    @search_api.doc(responses={405: 'Not allowed'})
    @search_api.doc(responses={400: 'Bad request'})
    
    
    def get(name_type,value):
        
        if name_type=='company_ko':
            value = "%{}%".format(value)
            search_query = WantedCompany.query.filter(WantedCompany.company_ko.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_ko' : company.company_ko,
               
            
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)
            
        elif name_type=='company_en':
            value = "%{}%".format(value)
            search_query = WantedCompany.query.filter(WantedCompany.company_en.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_en' : company.company_en,
               
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)
            
        elif name_type=='company_ja':
            search_query = WantedCompany.query.filter(WantedCompany.company_ja.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_ja' : company.company_ja,
               
            
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)
        
@search_api.route("/search/tag/<string:tag_type>/<string:value>", methods=['GET','DELETE'])
class CompanyTagSearch(Resource):
    @staticmethod    
    @search_api.doc(responses={200: 'Success'})
    @search_api.doc(responses={201: 'Create'})
    @search_api.doc(responses={204: 'Delete'})
    @search_api.doc(responses={404: 'Not found'})
    @search_api.doc(responses={405: 'Not allowed'})
    @search_api.doc(responses={400: 'Bad request'})
    
    
    def get(tag_type,value):
        
        if tag_type=='tag_ko':
            value = "%{}%".format(value)
            search_query = WantedCompany.query.filter(WantedCompany.tag_ko.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_ko' : company.company_ko,
                'company_en' : company.company_en,
                'company_ja' : company.company_ja,
                'tag_ko' : company.tag_ko,
                'tag_en' : company.tag_en,
                'tag_ja' : company.tag_ja
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)
            
        elif tag_type=='tag_en':
            value = "%{}%".format(value)
            search_query = WantedCompany.query.filter(WantedCompany.tag_en.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_ko' : company.company_ko,
                'company_en' : company.company_en,
                'company_ja' : company.company_ja,
                'tag_ko' : company.tag_ko,
                'tag_en' : company.tag_en,
                'tag_ja' : company.tag_ja
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)
            
        elif tag_type=='tag_ja':
            value = "%{}%".format(value)
            search_query = WantedCompany.query.filter(WantedCompany.tag_ja.like(value))
            results = []
            for company in search_query:
                obj = {
                'company_ko' : company.company_ko,
                'company_en' : company.company_en,
                'company_ja' : company.company_ja,
                'tag_ko' : company.tag_ko,
                'tag_en' : company.tag_en,
                'tag_ja' : company.tag_ja
            }
                results.append(obj)
            print(results)
            return jsonify(results,200)

@search_api.route("/tag/delete/<string:tag_type>/<string:value>", methods=['DELETE'])
class TagDelete(Resource):
    @staticmethod    
    @search_api.doc(responses={204: 'Delete'})
    @search_api.doc(responses={404: 'Not found'})
    @search_api.doc(responses={405: 'Not allowed'})
    @search_api.doc(responses={400: 'Bad request'})
     
    def delete(tag_type,value):
        if tag_type=='tag_ko':
    
            search_query = WantedCompany.query.filter(WantedCompany.tag_ko == value).update(dict(tag_ko=""))
          
            db.session.commit() # 데이터에 반영
            
            return Response('Delete Success',204)

  
        elif tag_type=='tag_en':
            search_query = WantedCompany.query.filter(WantedCompany.tag_en == value).update(dict(tag_en=""))
          
            db.session.commit() # 데이터에 반영
  
            return Response('Delete Success',204)
        
        elif tag_type=='tag_ja':
            search_query = WantedCompany.query.filter(WantedCompany.tag_ja == value).update(dict(tag_ja=""))
          
            db.session.commit() # 데이터에 반영
  
            return Response('Delete Success',204)

  

@search_api.route("/tag/put/<string:tag_type>/<string:tag_value>/<string:update_value>", methods=['PUT'])
class TagUpdate(Resource):
    @staticmethod    
    @search_api.doc(responses={200: 'Update'})
    @search_api.doc(responses={404: 'Not found'})
    @search_api.doc(responses={405: 'Not allowed'})
    @search_api.doc(responses={400: 'Bad request'})

    def put(tag_type,tag_value,update_value):
        if tag_type=='tag_ko':

            search_query = WantedCompany.query.filter(WantedCompany.tag_ko == tag_value).update(dict(tag_ko=update_value))
          
            db.session.commit() # 데이터에 반영
            
            return Response('Update Success',200)

  
        elif tag_type=='tag_en':
            search_query = WantedCompany.query.filter(WantedCompany.tag_en == tag_value).update(dict(tag_en=update_value))
          
            db.session.commit() # 데이터에 반영
  
            return Response('Update Success',200)
        elif tag_type=='tag_ja':
            search_query = WantedCompany.query.filter(WantedCompany.tag_ja == tag_value).update(dict(tag_ja=update_value))
          
            db.session.commit() # 데이터에 반영
  
            return Response('Update Success',200)
