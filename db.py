import sqlite3


conn = sqlite3.connect("politics.db")
if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")
cur = conn.cursor()


cur.execute('''CREATE TABLE states (User_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    States VARCHAR(50) NOT NULL, 
                    Zones VARCHAR(50) NOT NULL)''')
"""
South West, South South, South East, North West, North Central

"""
North_Central=['Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau States', 'Federal Capital Territory']
North_East = ['Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe']
North_West = ['Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara']
South_East = ['Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo']
South_South = ['Akwa Ibom', 'Bayelsa', 'Cross River', 'Delta', 'Edo', 'Rivers']
South_West = ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo']

zones = ['North Central', 'North East', 'North West', 'South East', 'South South', 'South West']
states = ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Akwa Ibom', 'Bayelsa', 'Cross River', 'Delta', 'Edo', 'Rivers', 'Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo', 'Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau States', 'Federal Capital Territory', 'Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara' ]

for state in states:
    if state in North_Central:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[0]))
    if state in North_East:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[1]))
    if state in North_West:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[2]))
    if state in South_East:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[3]))
    if state in South_South:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[4]))
    if state in South_West:
        cur.execute('''INSERT INTO states(States, Zones) VALUES (?, ?)''', (state, zones[5]))

which = input("What state: ")
out = cur.execute('''SELECT Zones from states WHERE States=?''', (which,)).fetchone()[0]
print(out)

conn.commit()
conn.close()