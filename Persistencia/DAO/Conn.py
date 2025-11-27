import pymysql as sql

class Connection:
    def __init__(self, host, user, password, db) -> None:
        self.db = sql.connect(
            host=host, user=user,password=password, db=db
        )
        self.cursor = self.db.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor

    def disconnect(self) -> None:
        self.db.close()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()


