from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s)"
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL('friendships_schema').query_db(query)