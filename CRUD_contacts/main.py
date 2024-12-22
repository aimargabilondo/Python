import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL
)
''')
conn.commit()

def create_contact(name, email, phone):
    try:
        cursor.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        conn.commit()
        print("Contacto creado con éxito.")
    except sqlite3.IntegrityError as e:
        print("Error:", e)

def read_contacts():
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"ID: {contact[0]}, Nombre: {contact[1]}, Email: {contact[2]}, Teléfono: {contact[3]}")

def update_contact(contact_id, name=None, email=None, phone=None):
    query = 'UPDATE contacts SET '
    updates = []
    values = []
    if name:
        updates.append("name = ?")
        values.append(name)
    if email:
        updates.append("email = ?")
        values.append(email)
    if phone:
        updates.append("phone = ?")
        values.append(phone)
    query += ", ".join(updates) + " WHERE id = ?"
    values.append(contact_id)
    cursor.execute(query, values)
    conn.commit()
    print("Contacto actualizado con éxito.")

def delete_contact(contact_id):
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    print("Contacto eliminado con éxito.")

def menu():
    while True:
        print("\nSistema de Gestión de Contactos")
        print("1. Crear contacto")
        print("2. Leer contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        choice = input("Elige una opción: ")
        if choice == '1':
            name = input("Nombre: ")
            email = input("Email: ")
            phone = input("Teléfono: ")
            create_contact(name, email, phone)
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            contact_id = int(input("ID del contacto a actualizar: "))
            name = input("Nuevo nombre (dejar vacío para no cambiar): ")
            email = input("Nuevo email (dejar vacío para no cambiar): ")
            phone = input("Nuevo teléfono (dejar vacío para no cambiar): ")
            update_contact(contact_id, name or None, email or None, phone or None)
        elif choice == '4':
            contact_id = int(input("ID del contacto a eliminar: "))
            delete_contact(contact_id)
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

menu()
conn.close()
