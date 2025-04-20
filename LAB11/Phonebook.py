import psycopg2

# Establish connection
conn = psycopg2.connect(
    database="pp",
    user="postgres",
    host="localhost",
    password="3245",
    port=5433
)
cur = conn.cursor()

# Drop old functions/procedures if they exist
cur.execute("DROP FUNCTION IF EXISTS search_by_pattern(VARCHAR);")
cur.execute("DROP PROCEDURE IF EXISTS insert_element(VARCHAR, VARCHAR);")
cur.execute("DROP PROCEDURE IF EXISTS insert_lst(VARCHAR, VARCHAR);")
cur.execute("DROP FUNCTION IF EXISTS querys(INT, INT);")
cur.execute("DROP PROCEDURE IF EXISTS delete_by(VARCHAR, VARCHAR);")

# Create required functions and procedures

cur.execute("""
CREATE OR REPLACE FUNCTION search_by_pattern(search_pattern VARCHAR)
RETURNS TABLE(contact_id INT, contact_name VARCHAR, contact_phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name, phonebook.phone
    FROM phonebook
    WHERE phonebook.name ILIKE '%' || search_pattern || '%'
       OR phonebook.phone ILIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_element(p_name VARCHAR, p_phone VARCHAR) AS
$$
BEGIN
    UPDATE phonebook SET phone = p_phone WHERE phonebook.name = p_name;
    IF NOT FOUND THEN
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_lst(p_name VARCHAR, p_phone VARCHAR) AS
$$
BEGIN
    IF p_phone ~ '^[+][0-9]{10,15}$' THEN
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
    ELSE
        RAISE NOTICE 'Incorrect phone number: %', p_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION querys(p_limit INT, p_offset INT)
RETURNS TABLE(contact_id INT, contact_name VARCHAR, contact_phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE delete_by(p_name VARCHAR, p_phone VARCHAR) AS
$$
BEGIN
    DELETE FROM phonebook WHERE phonebook.name = p_name;
    IF NOT FOUND THEN
        DELETE FROM phonebook WHERE phonebook.phone = p_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

# Create phonebook table
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL
);
""")

# Python functions for working with procedures/functions above

# Search contacts
def search(pattern):
    cur.callproc('search_by_pattern', (pattern,))
    results = cur.fetchall()
    for row in results:
        print(row)

search("Nurasyl")

# Insert or update a contact
def insert(name, phone):
    cur.execute("CALL insert_element(%s, %s)", (name, phone))

insert('Bill Gates', '+1230000002')

# Insert multiple contacts (with phone number validation)
contacts = [
    ["Elon Musk", "+1230000001"],
    ["Bill Gates", "+1230000002"],
    ["Emma Watson", "wrong_phone"]  # This should trigger validation notice
]

for person in contacts:
    cur.execute("CALL insert_lst(%s, %s)", (person[0], person[1]))

# Pagination function
def paginate(limit, offset):
    cur.callproc('querys', (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

paginate(3, 0)

# Delete contact by name or phone
def delete(name=None, phone=None):
    cur.execute("CALL delete_by(%s, %s)", (name, phone))

delete(name="bek")

# Commit and close connection
conn.commit()
cur.close()
conn.close()
