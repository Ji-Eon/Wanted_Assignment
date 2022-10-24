from operator import concat
import os
from pydoc import render_doc
from telnetlib import WILL

import pandas as pd
from flask import (
    Flask,
    jsonify,
    json,
    Response,

)
from decimal import *

from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, flash, redirect, url_for

from flask_restx import Api, Resource, reqparse
from flask_paginate import Pagination, get_page_args

import psycopg2

app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
search_api = api.namespace('search',path='/wanted', description='조회 API')



def get_db_connection():
    db = psycopg2.connect(
            host="49.50.167.136",
            database="synthea_1000",
            user='walker101',
            password='forcebewithyou')

    # Open a cursor to perform database operations
    cur = db.cursor()
    return cur

def concept_drug(column_name,concept_id):
    cur  = get_db_connection()
    offset=0
    per_page=10
    
    query = f"SELECT drug_exposure_id ,person_id ,drug_concept_id from de.drug_exposure where {column_name} = {concept_id};" 
    cur.execute(query)
       
    rows = cur.fetchall()
    
    dicts = {}
    reuslt = []
    for row in rows :
        
        dicts = {"drug_exposure_id":row[0],"person_id":row[1],"drug_concept_id":row[2]}
        reuslt.append(dicts)
   
  
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = len(reuslt)
    pagination_users  = reuslt[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return pagination_users, page,per_page,pagination
    

def concept(column_name,concept_id):
    cur  = get_db_connection()
    offset=0
    per_page=10
    
    query = f"SELECT concept_id ,concept_name ,domain_id,vocabulary_id,concept_code from de.concept where {column_name} = {concept_id};" 
    cur.execute(query)
       
    rows = cur.fetchall()
    
    dicts = {}
    reuslt = []
    for row in rows :
        
        dicts = {"concept_id":row[0],"concept_name":row[1],"domain_id":row[2],"vocabulary_id":row[3],"concept_code":row[4]}
        reuslt.append(dicts)
   
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = len(reuslt)
    pagination_users  = reuslt[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return pagination_users, page,per_page,pagination

def death(column_name,concept_id):
    cur  = get_db_connection()
    offset=0
    per_page=10
    
    query = f"SELECT person_id,death_date,death_datetime,cause_concept_id,death_type_concept_id from de.death where {column_name} = {concept_id};" 
    cur.execute(query)
       
    rows = cur.fetchall()
    
    dicts = {}
    reuslt = []
    for row in rows :
        
        dicts = {"person_id":row[0],"death_date":row[1],"death_datetime":row[2],"cause_concept_id":row[3],"death_type_concept_id":row[4]}
        reuslt.append(dicts)
   
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = len(reuslt)
    pagination_users  = reuslt[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return pagination_users, page,per_page,pagination
    
def visit_concept(column_name,concept_id):
    cur  = get_db_connection()
    offset=0
    per_page=10
    
    query = f"SELECT visit_occurrence_id,person_id,visit_concept_id from de.visit_occurrence vo where {column_name} = {concept_id};" 
    cur.execute(query)
       
    rows = cur.fetchall()
    
    dicts = {}
    reuslt = []
    for row in rows :
        
        dicts = {"visit_occurrence_id":row[0],"person_id":row[1],"visit_concept_id":row[2]}
        reuslt.append(dicts)
   
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = len(reuslt)
    pagination_users  = reuslt[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return pagination_users, page,per_page,pagination

def condition_occurence(column_name,concept_id):
    cur  = get_db_connection()
    offset=0
    per_page=10
    
    query = f"SELECT condition_occurrence_id, person_id ,condition_concept_id ,condition_source_value ,condition_source_concept_id  from de.condition_occurrence co  where {column_name} = {concept_id};" 
    cur.execute(query)
       
    rows = cur.fetchall()
    
    dicts = {}
    reuslt = []
    for row in rows :
        
        dicts = {"condition_occurrence_id":row[0],"person_id":row[1],"condition_concept_id":row[2],"condition_source_value":row[3],"condition_source_concept_id":row[4]}
        reuslt.append(dicts)
   
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    
    total = len(reuslt)
    pagination_users  = reuslt[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return pagination_users, page,per_page,pagination
    
    

# Person Stastics
@app.route('/statistics/person', methods=['GET'])
def statistics_person():
    if request.method == 'GET':
        print('row')
        
        cur  = get_db_connection()
        
        cur.execute("""
                    SELECT count(person_id), count(case when gender_concept_id = 8532 then 8532 end) , count(case when gender_concept_id = 8507 then 8507 end),
                    count(case when race_concept_id = 8515 then 8515 end) , count(case when race_concept_id = 8527 then 8527 end), count(case when race_concept_id = 8516 then 8516 end), count(case when race_concept_id = 0 then 0 end) , (select count(person_id)from de.death d) as Death  from de.person ;

                    """)
       
        rows = cur.fetchall()
        
        
        dicts = {}
        
        for row in rows :
            dicts = {"person":row[0],"female":row[1],"male":row[2],"8515":row[3],"8527":row[4],"8516":row[5],"0":row[6],"death":row[7]}
        
        return jsonify(dicts)


# Visit Stastics
@app.route('/statistics/visit', methods=['GET'])
def statistics_visit():
    if request.method == 'GET':
        
        cur  = get_db_connection()
        
        cur.execute("""
                    SELECT count(case when gender_concept_id  = 8532 then 8532 end),count(case when gender_concept_id  = 8507 then 8507 end), 
                    count(case when race_concept_id  = 8515 then 8515 end),  count(case when race_concept_id = 8527 then 8527 end), count(case when race_concept_id  = 8516 then 8516 end),count(case when race_concept_id  = 0 then 0 end),
                    count(case when visit_concept_id  = 9201 then 9201 end) as Inpatient , count(case when visit_concept_id  = 9202 then 9202 end) as Outpatient , count(case when visit_concept_id  = 9203 then 9203 end) as Emergency
                    FROM de.visit_occurrence, de.person where de.visit_occurrence .person_id  = de.person .person_id ;
                    """)
       
        rows = cur.fetchall()
        
        
        
        dicts = {}
        
        for row in rows :
            dicts = {"female":row[0],"male":row[1],"8515":row[2],"8527":row[3],"8516":row[4],"0":row[5],"Inpatient":row[6],"Outpatient":row[7],"Emergency":row[8]}
        
        return jsonify(dicts)



# Visit Stastics
@app.route('/search/<table_name>/<column_name>/<concept_id>', methods=['GET'])
def search_concept(table_name,column_name,concept_id):
    if request.method == 'GET':
        
        concept_id = int(concept_id)
      
        
        if  table_name == 'concept':
            pagination_users, page,per_page,pagination = concept(column_name,concept_id)
            
            return render_template('concept.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )            
        elif table_name == 'drug_exposure':
            pagination_users, page,per_page,pagination = concept_drug(column_name,concept_id)
            
            return render_template('drug_index.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
            
        elif table_name == 'visit_occurrence':
            pagination_users, page,per_page,pagination = visit_concept(column_name,concept_id)
            
            return render_template('visit_occurrence.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
        elif table_name == 'condition_occurrence':
            pagination_users, page,per_page,pagination = condition_occurence(column_name,concept_id)
            
            return render_template('condition_occurrence.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
            
        elif table_name == 'death':
            pagination_users, page,per_page,pagination = death(column_name,concept_id)
            
            return render_template('death.html',
                           results=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
        