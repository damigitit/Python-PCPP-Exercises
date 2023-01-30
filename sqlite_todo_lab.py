"""
Author: Damian Archer
Date: 1/14/2023
File: sqlite_todo_lab.py
Purpose: PCPP Exercises - sqlite
"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    
    def add_task(self):
        while True:
            try:
                name = input('Enter task name: ')
                if (name != '' and name.strip() != ''):
                        priority = int(input('Enter priority: '))
                        if priority > 0:
                            self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
                            self.conn.commit()
                            break
                        else:
                            raise ValueError('Priority must be a postive integer')
                else:
                    raise ValueError('Enter a valid task name (not empty or only spaces)')
            
            except ValueError as e:
                print(e)
                print('Try again')
            
        

    def find_task(self, name:str) -> list:
        if name != '' and isinstance(name, str):
            self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,))
            return self.c.fetchall()
        else:
            return None

    def show_tasks(self):
        print('\nTasks:')
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)


    def change_priority(self):
        while True:
            try:
                record_id = int(input("please enter id as integer:"))
                new_priority_value = int(input("Please enter new priority as integer:"))
                
                if (record_id >= 1) and (new_priority_value >= 1):
                    self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?',
                                   (new_priority_value, record_id))
                    self.conn.commit()
                    break
                else:
                    raise ValueError
                    
            except ValueError as e:
                print("\nplease enter valid, positive integer values only\n")

            except KeyboardInterrupt as e:
                print("quitting...")
                break
        

    def delete_task(self):
        try:
            record_id = int(input("please enter record id (as integer) to delete: "))
            if (record_id >= 1):
                self.c.execute("DELETE FROM tasks WHERE id = ?", (record_id,))
                print('\ndeleted record: ', record_id)
                self.conn.commit()
            else:
                print("invalid record id")
        except ValueError as e:
            print("\nplease enter valid, positive integer values only\n")

        except KeyboardInterrupt as e:
            print("quitting...")



def main():
    app = Todo()
    options = { 1: "Show Tasks",
                2: "Add Task",
                3: "Change Priority",
                4: "Delete Task",
                5: "Exit"}
    while True:
        print()
        for k, v in options.items(): # show menu 
            print(f"{k}. {v}")
            
        try:    # get user input            
            user_in = int(input('\nEnter an Option: '))

            
            if options[user_in] == "Show Tasks":
                app.show_tasks()
            elif options[user_in] == "Add Task":
                app.add_task()
            elif options[user_in] == "Change Priority":
                app.change_priority()
            elif options[user_in] == "Delete Task":
                app.delete_task()
            elif options[user_in] == "Exit":
                quit()
            else:
                raise ValueError
                
        except ValueError as e:
            print("\nplease enter valid option (as integer)\n")

        except KeyboardInterrupt as e:
            print("quitting...")
            quit()
    

main()

