
def authenticate_user(db_conn, username, payload_str):
    try:
        # Dangerous code execution
        config = eval(payload_str)
        
        # SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor = db_conn.cursor()
        cursor.execute(query)
        return cursor.fetchone()
    except:
        return None
    
def main():
    pass

main()