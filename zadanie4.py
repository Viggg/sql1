import sqlite3
#athletes
con = sqlite3.connect("baza.db")



cur = con.cursor()
res = cur.execute("SELECT * FROM athletes")
sport = res.fetchall()
sport_name = sport





for id, name, gender, age, country, sport in sport:
    print(f"Номер: {id}, Имя: {name}, Гендер: {gender}, Возраст: {age},Страна: {country},Вид спорта: {sport} ")

sportname = input("Введите имя:")
for sname in sport_name:
    if sname[1] == sportname:
        selected_name = sname
        break
print(sname) 

name = input("Введите имя:")
gender = input("Введите гендер:")
age = int(input("Введите возраст:"))
country = input("Введите страну:")
sport = input("Введите вид спорта:")



regisregistration = cur.execute('INSERT INTO athletes (name, gender, age, country, sport) VALUES (?, ?, ?, ?, ?)', (name,gender,age,country,sport))


con.commit()
cur.close()
con.close()


