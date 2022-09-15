from tkinter import ttk
import tkinter as tk
import sqlite3
import numpy as np

class Database_app:
    def __init__(self, main_window):
        self.main_window = main_window

        main_window.title('DataBase Control')
        main_window.resizable(width=1, height=1)
        main_window.geometry('1000x400')
        main_window.minsize(400,300)

        style = ttk.Style()
        style.theme_use('alt')

        style.map('Treeview',
                  background=[('selected', '#146103')])

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

        self.frame_in_1_2.columnconfigure(0, weight=1)
        frame_in_1_3.columnconfigure(0, weight=1)
        frame_in_1_3.columnconfigure(1, weight=1)
        frame_in_1_3.columnconfigure(2, weight=1)
        frame_in_1_1.grid(row=0, column=0, sticky='nwe')
        self.frame_in_1_2.grid(row=1, column=0, sticky='nswe')
        frame_in_1_3.grid(row=2, column=0, sticky='swe')

        self.colnames = ['Name','sex','age']
        # self.colnames = []

        create = tk.Button(frame_in_1_1, text='Create / Read and Edit',command = self.create_read_window).grid(row=0, column=0, sticky='nw',
                                                                                           pady=3, padx=10)
        self.entres = []
        self.labels = []
        self.data_to_write = []

        # self.create_labels_entres()

        add = tk.Button(frame_in_1_3, text='Add',command = self.add_item).grid(row=0, sticky='sw', column=0, pady=3, padx=10, ipadx=10)
        update = tk.Button(frame_in_1_3, text='Update',command = self.update_data).grid(row=0, sticky='sw', column=1, pady=3, padx=10, ipadx=10)
        delete = tk.Button(frame_in_1_3, text='Delete',command = self.delete_data).grid(row=0, sticky='sw', column=2, pady=3, padx=1, ipadx=10)

        self.treev = ttk.Treeview(self.frame_2, selectmode='browse')
        # self.create_table()
        self.treev.bind('<ButtonRelease-1>', self.selectItem)

    def get_entry(self):
        a = self.entres[0].get()
        print(a)

    def add_item(self):
        list_of_entres = []
        for i in range(len(self.entres)):
            list_of_entres.append((self.entres[i].get()))
        self.treev.insert("", 'end', text="value",
                          values=(list_of_entres))
        self.convertion()
        self.write_to_db()

    def selectItem(self,non):
        curItem = self.treev.focus()
        list_of_values = self.treev.item(curItem)['values']
        for x, val in enumerate(list_of_values):
            self.entres[x].delete(0,tk.END)
            self.entres[x].insert(0,val)

    def delete_data(self,):
        selected_item = self.treev.selection()[0]
        self.treev.delete(selected_item)

    def update_data(self):
        list_of_entres = []
        for i in range(len(self.entres)):
            list_of_entres.append((self.entres[i].get()))
        curItem = self.treev.focus()
        self.treev.item(curItem,text='value',values = (list_of_entres))

    def create_read_window(self):

        self.crw = tk.Toplevel(self.main_window)
        self.crw.title("Create/Read db")
        self.crw.resizable(False, False)
        self.crw.geometry("400x170")
        tk.Grid.columnconfigure(self.crw, 0, weight=1)
        for i in range(6):
            tk.Grid.rowconfigure(self.crw, i, weight=1)


        path_label = tk.Label(self.crw, text='Insert path').grid(row=0, column=0, sticky='nsw', padx=10, pady=3)
        self.path_entry = tk.Entry(self.crw, text='input path')
        pe = self.path_entry
        pe.grid(row=1, column=0, sticky='nsew', padx=10, pady=3)
        read_but = tk.Button(self.crw, text='Read and Edit',command = self.read_db).grid(row=2, column=0, sticky='nsw', padx=10, pady=3,
                                                                   ipadx=20)
        col_label = tk.Label(self.crw, text='Insert column names').grid(row=3, column=0, sticky='nsw', padx=10, pady=3)
        self.col_entry = tk.Entry(self.crw, text='col_names')
        ce = self.col_entry
        ce.grid(row=4, column=0, sticky='nsew', padx=10, pady=3)
        create_but = tk.Button(self.crw, text='Create',command = self.create_db).grid(row=5, column=0, sticky='nsw',  padx=10, pady=3, ipadx=40)

    def create_db(self):
        self.path = self.path_entry.get()
        print(self.path)

        self.colnames = self.col_entry.get().split(',')
        print(self.colnames)

        self.crw.destroy()

        self.cd = tk.Toplevel(self.main_window)
        self.cd.title("Create db")
        self.cd.resizable(False, False)
        self.cd.geometry("400x250")

        tk.Grid.columnconfigure(self.cd, 0, weight=1)
        for i in range(8):
            tk.Grid.rowconfigure(self.cd, i, weight=1)

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

    def read_db(self):
        self.path = self.path_entry.get()
        print(self.path)

        self.crw.destroy()

    def create_database(self):
        print(self.path+'\\'+self.name_entry.get())
        self.variables = self.desc_entry.get().split(',')
        self.table_name = self.table_entry.get()
        sql = "CREATE TABLE " + self.table_name+" ("
        for x,col in enumerate(self.colnames):
            sql = sql+ col + ' '+ self.variables[x].upper() + ','
        sql = sql[:-1]+')'
        print(sql)

        self.db = sqlite3.connect(self.path+'\\'+self.name_entry.get())
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        self.db.commit()
        self.cd.destroy()
        self.create_labels_entres()
        self.treev.destroy()
        self.treev = ttk.Treeview(self.frame_2, selectmode='browse')
        self.create_table()

    def create_labels_entres(self):
        try:
            for i in range(len(self.labels)):
                self.labels[i].destroy()
                self.entres[i].destroy()
        except:
            pass

        self.entres = []
        self.labels = []

        for x,c in enumerate(self.colnames):
            self.labels.append(tk.Label(self.frame_in_1_2, text=c+' '+ self.variables[x].upper()))
            self.entres.append(tk.Entry(self.frame_in_1_2, text=c+'input'))
        cnt = 0
        for i in range(0,len(self.colnames)*2,2):
            self.labels[cnt].grid(row=i, sticky='nw', column=0, pady=3, padx=10)
            self.entres[cnt].grid(row=i+1, sticky='nwe', column=0, pady=3, padx=10)
            cnt+=1

    def create_table(self):
        self.treev.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)
        self.verscrlbar = ttk.Scrollbar(self.main_window,
                                   orient="vertical",
                                   command=self.treev.yview)
        self.treev.configure(xscrollcommand=self.verscrlbar.set)
        self.treev['show'] = 'headings'
        self.treev["columns"] = tuple([str(x) for x in range(1, len(self.colnames) + 1)])
        for x, c in enumerate(self.colnames):
            self.treev.column(x + 1, width = 1, anchor='c')
            self.treev.heading(str(x + 1), text=c)

    def convertion(self):
        self.data_to_write = []
        for x,var in enumerate(self.variables):
            if var.upper() == 'INTEGER':
                self.data_to_write.append(int(self.entres[x].get()))
            elif "VARCHAR" in var.upper():
                self.data_to_write.append(str(self.entres[x].get()))
            elif var.upper() == 'REAL':
                self.data_to_write.append(float(self.entres[x].get()))

    def write_to_db(self):
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
        self.cursor.execute(self.sql_query)
        self.db.commit()

root = tk.Tk()
app = Database_app(root)
root.mainloop()