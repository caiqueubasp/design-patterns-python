import sqlite3

def _execute(query):
    db_path = './geek_university'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result = None
    
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f'Error Query: {e}')
        connection.rollback()
        raise e 

    connection.close()
    
    return result
