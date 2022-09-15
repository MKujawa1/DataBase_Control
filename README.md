# DataBase_Control
Simple GUI in Python (Tkinter) to create, read and edit databases from sqlite - in progress

**MAIN WINDOW** - place to create, read or edit database
* Create / Read and Edit - button to create or read and edit database from file
* Add - button to add record 
* Update - button to update record
* Delete - button to delete record

![image](https://user-images.githubusercontent.com/99027230/190415189-d1190897-a79a-4626-814b-e4c240e82140.png)

**Create/Read db WINDOW** - place to read or create database
* Insert path - path to read or create db
* Read and Edit - button to read data from selected db
* Insert column names - place to name your new columns (seperate every column with ,)
* Create - button to create new database - after click, the new window is generated

![image](https://user-images.githubusercontent.com/99027230/190418124-19be0eb1-ea52-48a2-ad6c-bad323f89dc4.png)
![image](https://user-images.githubusercontent.com/99027230/190418631-7cc2bd6a-46d4-4959-8874-f3084d55c7d6.png)

**Create db WINDOW** - the last element to create new database
* Database name - name your database
* Table name - name your table
* Define type of variables - define type of variables in passed columns
* Create database - button to create new database

![image](https://user-images.githubusercontent.com/99027230/190420174-ad0843e6-5cc0-4ba3-9751-5393547fa424.png)

After click on **Create database**, in the main window you will see a table and inputs with labels to edit
The table is fully resizable and scrollable.

![image](https://user-images.githubusercontent.com/99027230/190420725-bf972ba4-bae1-4f60-b1b1-62e6c2644266.png)

To add record to database - pass variables to input and then click on Add Button

![image](https://user-images.githubusercontent.com/99027230/190421907-5aeafb43-26ce-4a1e-82fe-b657045bf2fa.png)

After adding some records to database

To update record - click on the line you are interested in. The data from the row is automatically transferred to the inputs. After that, change the selected value, and then click the UPDATE button 

![image](https://user-images.githubusercontent.com/99027230/190424579-393e09cb-3900-4d43-bfc4-b707ab2196c2.png)

After that the current record in updated: 

![image](https://user-images.githubusercontent.com/99027230/190424957-39342123-506f-4647-97de-8bf949e24c94.png)
