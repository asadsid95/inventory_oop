import sqlite3

class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.config = config
        pass

    def __enter__(self):
        self.conn = sqlite3.connect(**self.config)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cur.close()    
        self.conn.close()        

