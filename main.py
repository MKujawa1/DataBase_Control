from tkinter import ttk
import tkinter as tk
import sqlite3

class Database_app:
    def __init__(self, main_window):
        # Main window configuration
        self.main_window = main_window
        main_window.title('DataBase Control')
        main_window.resizable(width=1, height=1)
        main_window.geometry('1000x400')
        main_window.minsize(400,300)
        main_window.iconbitmap('db_icon.ico')
        # Treeview style configuration
        style = ttk.Style()
        style.theme_use('alt')
        style.map('Treeview',
                  background=[('selected', '#146103')])
        # Layout configuration
        frame_1 = tk.Frame(main_window)
        self.frame_2 = tk.Frame(main_window)
        tk.Grid.columnconfigure(main_window, 0, weight=1)
        tk.Grid.columnconfigure(main_window, 1, weight=32)
        tk.Grid.rowconfigure(main_window, 0, weight=1)
        frame_1.columnconfigure(0, weight=1)
        frame_1.rowconfigure(0, weight=1)
        frame_1.rowconfigure(1, weight=16)
        frame_1.rowconfigure(2, weight=1)
        frame_1.grid(row=0, column=0, sticky='nswe')
        self.frame_2.columnconfigure(0, weight=1)
        self.frame_2.rowconfigure(0, weight=1)
        self.frame_2.grid(row=0, column=1, sticky='nswe')
        frame_in_1_1 = tk.Frame(frame_1)
        self.frame_in_1_2 = tk.Frame(frame_1)
        frame_in_1_3 = tk.Frame(frame_1)
        frame_in_1_1.columnconfigure(0, weight=1)
        frame_in_1_1.grid(row=0, column=0, sticky='nwe')
        self.frame_in_1_2.columnconfigure(0, weight=1)
        self.frame_in_1_2.grid(row=1, column=0, sticky='nswe')
        frame_in_1_3.columnconfigure(0, weight=1)
        frame_in_1_3.columnconfigure(1, weight=1)
        frame_in_1_3.columnconfigure(2, weight=1)
        frame_in_1_3.grid(row=2, column=0, sticky='swe')
        # Activate Treeview
        self.tree = ttk.Treeview(self.frame_2, selectmode='browse')
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        # Create buttons
        create = tk.Button(frame_in_1_1, text='Create / Read and Edit', command=self.create_read_window).grid(row=0,column=0,sticky='nw',pady=3,padx=10)
        add = tk.Button(frame_in_1_3, text='Add',command = self.add_item).grid(row=0, sticky='sw', column=0, pady=3, padx=10, ipadx=10)
        update = tk.Button(frame_in_1_3, text='Update',command = self.update_data).grid(row=0, sticky='sw', column=1, pady=3, padx=10, ipadx=10)
        delete = tk.Button(frame_in_1_3, text='Delete',command = self.delete_data).grid(row=0, sticky='sw', column=2, pady=3, padx=1, ipadx=10)

    def create_read_window(self):
        # Create Read window configuration
        self.crw = tk.Toplevel(self.main_window)
        self.crw.title("Create/Read db")
        self.crw.resizable(False, False)
        self.crw.iconbitmap('db_icon.ico')
        self.crw.geometry("400x170")
        # Layout configuration
        tk.Grid.columnconfigure(self.crw, 0, weight=1)
        for i in range(6):
            tk.Grid.rowconfigure(self.crw, i, weight=1)
        # Create labels, entries and buttons
        path_label = tk.Label(self.crw, text='Insert path').grid(row=0, column=0, sticky='nsw', padx=10, pady=3)
        self.path_entry = tk.Entry(self.crw, text='input path')
        pe = self.path_entry
        pe.grid(row=1, column=0, sticky='nsew', padx=10, pady=3)
        read_but = tk.Button(self.crw, text='Read and Edit',command = self.read_db).grid(row=2, column=0, sticky='nsw', padx=10, pady=3,ipadx=20)
        col_label = tk.Label(self.crw, text='Insert column names').grid(row=3, column=0, sticky='nsw', padx=10, pady=3)
        self.col_entry = tk.Entry(self.crw, text='col_names')
        ce = self.col_entry
        ce.grid(row=4, column=0, sticky='nsew', padx=10, pady=3)
        create_but = tk.Button(self.crw, text='Create',command = self.create_db_window).grid(row=5, column=0, sticky='nsw',  padx=10, pady=3, ipadx=40)

    def create_db_window(self):
        # Get path and colnames
        self.path = self.path_entry.get()
        self.colnames = self.col_entry.get().split(',')
        # Close crw and Create cd window
        self.crw.destroy()
        self.cd = tk.Toplevel(self.main_window)
        self.cd.title("Create db")
        self.cd.iconbitmap('db_icon.ico')
        self.cd.resizable(False, False)
        self.cd.geometry("400x250")
        # Layout configuration
        tk.Grid.columnconfigure(self.cd, 0, weight=1)
        for i in range(8):
            tk.Grid.rowconfigure(self.cd, i, weight=1)
        # Create labels, entries and buttons
        name_label = tk.Label(self.cd, text='Database name').grid(row=0, column=0, sticky='nsw', padx=10, pady=3)
        self.name_entry = tk.Entry(self.cd, text='input name')
        ne = self.name_entry
        ne.grid(row=1, column=0, sticky='nsew', padx=10, pady=3)
        table_label = tk.Label(self.cd, text='Table name').grid(row=2, column=0, sticky='nsw', padx=10, pady=3)
        self.table_entry = tk.Entry(self.cd, text='Table name')
        te = self.table_entry
        te.grid(row=3, column=0, sticky='nsew', padx=10, pady=3)
        type_label = tk.Label(self.cd, text='Define type of variables: integer, varchar(x),real').grid(row=4, column=0, sticky='nsw', padx=10, pady=3)
        desc_label = tk.Label(self.cd, text=self.colnames).grid(row=5, column=0, sticky='nsw', padx=10, pady=3)
        self.desc_entry = tk.Entry(self.cd, text='desc entry')
        de = self.desc_entry
        de.grid(row=6, column=0, sticky='nsew', padx=10, pady=3)
        create_but = tk.Button(self.cd, text = 'Create database',command = self.create_database).grid(row=7, column=0, sticky='nsw', padx=10, pady=3)

    def add_item(self):
        '''
        Add one record to database and Treeview.
        '''
        # Conversion of values according to their types
        self.convertion()
        # Insert values to Treeview
        self.tree.insert("", 'end', text="value",
                         values=(self.data_to_write))
        # Write values into database
        self.write_to_db()

    def delete_data(self,):
        '''
        Delete one record from database and Treeview.
        '''
        # Select values to delete
        selected_item = self.tree.selection()[0]
        # Delete values from Treeview
        self.tree.delete(selected_item)
        # Delete values from database
        self.delete_from_db()

    def update_data(self):
        '''
        Update record in database and Treeview
        '''
        # Get values from Treeview
        item = self.tree.focus()
        self.list_of_values = self.tree.item(item)['values']
        # Get new values from entries
        self.new_values = []
        for i in range(len(self.entries)):
            self.new_values.append((self.entries[i].get()))
        # Update values in Treeview
        item = self.tree.focus()
        self.tree.item(item,text='value',values = (self.new_values))
        # Update values in database
        self.update_db_record()

    def selectItem(self,non):
        '''
        Autofill entries with selected record
        '''
        # Get list of values from record
        item = self.tree.focus()
        self.list_of_values = self.tree.item(item)['values']
        # Insert values into entries
        for x, val in enumerate(self.list_of_values):
            self.entries[x].delete(0,tk.END)
            self.entries[x].insert(0,val)

    def read_db(self):
        '''
        Read data from database. Create tables and entries in main_window.
        '''
        # Get path, connection to db and cursor creating.
        self.path = self.path_entry.get()
        self.db = sqlite3.connect(self.path)
        self.cursor = self.db.cursor()
        # Get table name from db
        sql_table_name = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'"
        self.cursor.execute(sql_table_name)
        for x in self.cursor:
            self.table_name = x
        self.table_name = self.table_name[0]
        # Get column names from db
        sql_column_names = f"PRAGMA table_info({self.table_name})"
        self.cursor.execute(sql_column_names)
        self.colnames = []
        self.variables = []
        for x in self.cursor:
            self.colnames.append(x[1])
            self.variables.append(x[2])
        # Create labels, entries, treeview and table
        self.create_labels_entries()
        self.tree.destroy()
        self.tree = ttk.Treeview(self.frame_2, selectmode='browse')
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.create_table()
        # Read values from table
        sql_data_from_table = "SELECT * FROM " + self.table_name
        self.cursor.execute(sql_data_from_table)
        # Insert values into treeview
        for x in self.cursor:
            self.tree.insert("", 'end', text="value",values=(x))
        # Close crw window
        self.crw.destroy()

    def create_database(self):
        '''
        Create new database.
        '''
        # Get variables types and table name
        self.variables = self.desc_entry.get().split(',')
        self.table_name = self.table_entry.get()
        # Create query
        sql = "CREATE TABLE " + self.table_name+" ("
        for x,col in enumerate(self.colnames):
            sql = sql+ col + ' '+ self.variables[x].upper() + ','
        sql = sql[:-1]+')'
        # Get connection and create cursor
        self.db = sqlite3.connect(self.path+'\\'+self.name_entry.get())
        self.cursor = self.db.cursor()
        # Execute SQL query and commit in db
        self.cursor.execute(sql)
        self.db.commit()
        # Create labels, entries, table and init treeview
        self.create_labels_entries()
        self.tree.destroy()
        self.tree = ttk.Treeview(self.frame_2, selectmode='browse')
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.create_table()
        # Close cd window
        self.cd.destroy()

    def create_labels_entries(self):
        '''
        Create labels and entries based on column names
        '''
        # If exist, destroy all labels and entries in main window
        try:
            for i in range(len(self.labels)):
                self.labels[i].destroy()
                self.entries[i].destroy()
        except:
            pass
        # Create entries and labels
        self.entries = []
        self.labels = []
        for x,c in enumerate(self.colnames):
            self.labels.append(tk.Label(self.frame_in_1_2, text=c+' '+ self.variables[x].upper()))
            self.entries.append(tk.Entry(self.frame_in_1_2, text=c+'input'))
        # Layout configuration
        cnt = 0
        for i in range(0,len(self.colnames)*2,2):
            self.labels[cnt].grid(row=i, sticky='nw', column=0, pady=3, padx=10)
            self.entries[cnt].grid(row=i+1, sticky='nwe', column=0, pady=3, padx=10)
            cnt+=1

    def create_table(self):
        '''
        Create empty table in main_window with column names
        '''
        # Treeview configuration
        self.tree.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)
        self.verscrlbar = ttk.Scrollbar(self.main_window,
                                   orient="vertical",
                                   command=self.tree.yview)
        self.tree.configure(xscrollcommand=self.verscrlbar.set)
        self.tree['show'] = 'headings'
        self.tree["columns"] = tuple([str(x) for x in range(1, len(self.colnames) + 1)])
        # Add column names to Treeview.
        for x, c in enumerate(self.colnames):
            self.tree.column(x + 1, width = 1, anchor='c')
            self.tree.heading(str(x + 1), text=c)

    def convertion(self):
        '''
        Conversion of values according to their types.
        '''
        # Append converted values to list
        self.data_to_write = []
        for x,var in enumerate(self.variables):
            if var.upper() == 'INTEGER':
                self.data_to_write.append(int(self.entries[x].get()))
            elif "VARCHAR" in var.upper():
                self.data_to_write.append(str(self.entries[x].get()))
            elif var.upper() == 'REAL':
                self.data_to_write.append(float(self.entries[x].get()))

    def write_to_db(self):
        '''
        Write record into database.
        '''
        # Create SQL query
        self.sql_query = ''
        self.sql_query = "INSERT INTO "+self.table_name +' ('
        for col in self.colnames:
            self.sql_query = self.sql_query+col+','
        self.sql_query = self.sql_query[:-1]
        self.sql_query = self.sql_query + ') VALUES ('
        for val in self.data_to_write:
            if type(val) == str:
                self.sql_query = self.sql_query + "'"+str(val) +"'"+ ','
            else:
                self.sql_query = self.sql_query + str(val) + ','
        self.sql_query = self.sql_query[:-1]
        self.sql_query = self.sql_query + ')'
        # Execute and commit
        self.cursor.execute(self.sql_query)
        self.db.commit()

    def delete_from_db(self):
        '''
        Delete record from database.
        '''
        # Create SQL query
        self.sql_query_del = ''
        self.sql_query_del = "DELETE FROM "+ self.table_name + ' WHERE '
        for x,c in enumerate(self.colnames):
            if "VARCHAR" in self.variables[x].upper():
                self.sql_query_del = self.sql_query_del + c + ' = ' + "'"+self.entries[x].get()+ "'" + ' AND '
            else:
                self.sql_query_del = self.sql_query_del + c + ' = ' + self.entries[x].get() + ' AND '
        self.sql_query_del = self.sql_query_del[:-5]
        # Execute and commit
        self.cursor.execute(self.sql_query_del)
        self.db.commit()

    def update_db_record(self):
        '''
        Update record in database.
        '''
        # Create SQL query
        self.sql_query_update = ''
        self.sql_query_update = "UPDATE " + self.table_name + ' SET '
        for x,c in enumerate(self.colnames):
            if "VARCHAR" in self.variables[x].upper():
                self.sql_query_update = self.sql_query_update + c + ' = ' +"'"+self.new_values[x]+"'"+','
            else:
                self.sql_query_update = self.sql_query_update + c + ' = ' + str(self.new_values[x]) + ','
        self.sql_query_update = self.sql_query_update[:-1]
        self.sql_query_update = self.sql_query_update + ' WHERE '
        for x,c in enumerate(self.colnames):
            if "VARCHAR" in self.variables[x].upper():
                self.sql_query_update = self.sql_query_update + c + ' = ' +"'"+self.list_of_values[x]+"'"+' AND '
            else:
                self.sql_query_update = self.sql_query_update + c + ' = ' + str(self.list_of_values[x]) + ' AND '
        self.sql_query_update = self.sql_query_update[:-5]
        # Execute and commit
        self.cursor.execute(self.sql_query_update)
        self.db.commit()

root = tk.Tk()
app = Database_app(root)
root.mainloop()