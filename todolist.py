from datetime import datetime
import sqlite3

class Sql():
    def __init__(self):
        pass
    
    def create_todo_table(cur):
        cur.execute("""CREATE TABLE IF NOT EXISTS todolist 
                    (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT NOT NULL, 
                    todo TEXT NOT NULL, 
                    details TEXT, 
                    priority INTEGER NOT NULL, 
                    status INTEGER NOT NULL)
                    """)
        
    def add_todo(cur, conn, todo):
        cur.execute('INSERT INTO todolist VALUES (?, ?, ?, ?, ?, ?)', (todo.id, todo.time, todo.todo, todo.details, todo.priority, todo.status))
        conn.commit()
    
    def read_todo(cur):
        cur.execute('SELECT * FROM todolist')
        return cur.fetchall()

    def update_todo(cur, conn, todo):
        cur.execute('UPDATE todolist SET todo = ?, details = ?, priority = ?, status = ? WHERE id = ?', (todo.todo, todo.details, todo.priority, todo.status, todo.id))
        conn.commit()

    def delete_todo(cur, conn, todo):
        cur.execute('DELETE FROM todolist WHERE id = ?', (todo.id,))
        conn.commit()

class Todo():

    def __init__(self, id, time, todo, details, priority, status):
        self.id = id
        self.time = time
        self.todo = todo
        self.details = details
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"Todo(id={self.id}, time={self.time}, todo={self.todo}, details={self.details}, priority={self.priority}, status={self.status})"
    
    def commit(self, conn, cur):
        Sql.add_todo(cur, conn, self)

    def read(self, cur):
        return Sql.read_todo(cur)
    
    def update(self, conn):
        Sql.update_todo(conn, self)

    def delete(self, conn):
        Sql.delete_todo(conn, self)

    def cancel(self, conn):
        self.status = 2
        Sql.update_todo(conn, self)
    
    def done(self, conn):
        self.status = 1
        Sql.update_todo(conn, self)

    def undone(self, conn):
        self.status = 0
        Sql.update_todo(conn, self)

    def set_priority(self, conn):
        Sql.update_todo(conn, self)

    def add_table(self, cur):
        Sql.create_todo_table(cur)
    

class App():
    def __init__(self):
        pass

def main():
    conn = sqlite3.connect('todolist.db')
    cur = conn.cursor()

    todo = Todo(1, datetime.now(), 'test', 'test', 1, 0)

    # todo.add_table(cur)
    # todo.commit(conn, cur)
    print(todo.read(cur))



if __name__ == '__main__':
    main()


