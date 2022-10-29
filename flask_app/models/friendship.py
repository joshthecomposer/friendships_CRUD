from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import Flask

class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_friendship(cls, data):
        check_query_1 = """
        SELECT users1.id AS UserID, users2.id AS FriendID, 
        CONCAT(users1.first_name," ",users1.last_name) AS userName, 
        CONCAT(users2.first_name," ",users2.last_name) AS friendName FROM friendships
        JOIN users AS users1 ON friendships.user_id = users1.id
        JOIN users AS users2 ON friendships.friend_id = users2.id
        WHERE users1.id = %(user_id)s AND users2.id = %(friend_id)s;
        """
        check_query_2 = """
        SELECT users1.id AS UserID, users2.id AS FriendID, 
        CONCAT(users1.first_name," ",users1.last_name) AS userName, 
        CONCAT(users2.first_name," ",users2.last_name) AS friendName FROM friendships
        JOIN users AS users1 ON friendships.user_id = users1.id
        JOIN users AS users2 ON friendships.friend_id = users2.id
        WHERE users1.id = %(friend_id)s AND users2.id = %(user_id)s;
        """
        
        result = connectToMySQL('friendships_schema').query_db(check_query_1, data)
        result_2 = connectToMySQL('friendships_schema').query_db(check_query_2, data)
        print(result)
        if result or result_2:
            return False
        else:
            query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
            return connectToMySQL('friendships_schema').query_db(query, data)
    
    @classmethod
    def get_all_friendships(cls):
        query = """
        SELECT users1.id AS UserID, users2.id AS FriendID, 
        CONCAT(users1.first_name," ",users1.last_name) AS userName, 
        CONCAT(users2.first_name," ",users2.last_name) AS friendName FROM friendships
        JOIN users AS users1 ON friendships.user_id = users1.id
        JOIN users AS users2 ON friendships.friend_id = users2.id
        """
        return connectToMySQL('friendships_schema').query_db(query)
