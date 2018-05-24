import sys, os
sys.path.append(os.getcwd() + '/classes')
import conn

if __name__ == "__main__":
    obj = conn.conn('test')
    db = obj.getDB()
    movie_info = db.movie_info
    movies = movie_info.find({}, {'title':1}).limit(5)
    for row in movies:
        print (row)
    print ()
    movies = movie_info.find({}, {'title':1}).skip(3701)
    for row in movies:
        print (row)
