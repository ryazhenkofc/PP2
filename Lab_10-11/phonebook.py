import psycopg2, csv

def connect_to_db():
    return psycopg2.connect(dbname='Lab_10', user='postgres', password='1234', host='localhost')

def search_contact(current, n):
    sql="""
        SELECT * FROM phonebook WHERE person_name LIKE %s OR person_number LIKE %s;
    """
    current.execute(sql, (n, n))
    results = current.fetchall()
    print(results)

def add_or_update_contact(current, name, phone):
    sql="""
        DELETE FROM phonebook WHERE person_name = %s;
    """
    current.execute(sql, (name,))
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    current.execute(sql, (name, phone))

def add_many_contacts(current, contact):
    cont = []
    for tup in contact.split('), ('):
        tup = tup.replace(')','').replace('(','')
        cont.append(tuple(tup.split(',')))
    print(cont)
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    for i in range(len(cont)):
        current.execute(sql, (cont[i][0], cont[i][1]))

def see_first_n_contacts(current, x):
    sql = """
        SELECT * FROM phonebook;
    """
    current.execute(sql)
    results = current.fetchmany(int(x))
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))

def delete_contact(current, delete):
    sql="""
        DELETE FROM phonebook WHERE person_name = %s;
    """
    current.execute(sql, (delete,))
    sql="""
        DELETE FROM phonebook WHERE person_number = %s;
    """
    current.execute(sql, (delete,))
    print("Contact", delete, "has been deleted")

def add_contacts_from_csv(current):
    sql="""
        INSERT INTO phonebook VALUES(%s, %s) returning *;
    """
    result=[]
    with open(r'/home/dmitriy/Documents/Code/PP2/Lab_10/phonebook1.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            current.execute(sql, row)
            result.append(current.fetchone())
        print(result, "has been added to the phonebook")

def change_contact_info(current, w, x, y):
    if w == 'name':
        sql = """
            UPDATE phonebook SET person_name = %s WHERE person_number = %s;
        """
    elif w == 'phone':
        sql = """
            UPDATE phonebook SET person_number = %s WHERE person_name = %s;
        """
    current.execute(sql, (y, x))
    print("Data has been updated")

def see_all_names(current):
    sql = """
        SELECT person_name FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])

def see_all_phones(current):
    sql = """
        SELECT person_number FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])

def see_whole_table(current):
    sql = """
        SELECT * FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))    

def main():
    db = connect_to_db()
    current = db.cursor()

    print('''What do you want?

    Print "1" if you want to search contact by name or phone
    Print "2" if you want to add a new contact or update existing 
    Print "3" if you want to add many contacts by list
    Print "4" if you want to see first N contacts
    Print "5" if you want to delete contact by name or phone
    Print "6" if you want to add contacts from .csv file
    Print "7" if you want to change name or phone of contact
    Print "8" if you want to see all names of contacts
    Print "9" if you want to see all phones of contacts
    Print "0" if you want to see the whole table contacts 
    ''')
    req = input("Enter the number of request:")

    if req == '1':
        n = input("Enter name or phone:")
        search_contact(current, n)
    elif req == '2':
        name = input("Enter name:")
        phone = input("Enter phone:")
        add_or_update_contact(current, name, phone)
    elif req == '3':
        contact = input("Enter the list of contacts:")
        add_many_contacts(current, contact)
    elif req == '4':
        x = input("Enter the number of contacts:") 
        see_first_n_contacts(current, x)
    elif req == '5':
        delete = input("Enter the name or phone:")
        delete_contact(current, delete)
    elif req == '6':
        add_contacts_from_csv(current)
    elif req == '7':
        w = input("Do you want to update name or phone:")
        x = input("Enter the person_number: " if w == 'name' else "Enter the name: ")
        y = input("Enter the new name: " if w == 'name' else "Enter the new person_number: ")
        change_contact_info(current, w, x, y)
    elif req == '8':
        see_all_names(current)
    elif req == '9':
        see_all_phones(current)
    elif req == '0':
        see_whole_table(current)
    else:
        print("Request is unidentified")

    current.close()
    db.commit()
    db.close()

if __name__ == "__main__":
    main()
