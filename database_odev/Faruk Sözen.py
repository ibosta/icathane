import sqlite3

baglanti = sqlite3.connect("galatasaray_kadroliste.db")

cursor = baglanti.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS oyuncular (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    oyuncu_adi TEXT NOT NULL,
    forma_no INTEGER
)
""")

cursor.execute("""
INSERT INTO oyuncular (oyuncu_adi, forma_no)
VALUES ('Osimhen', 45),
    ('Icardi', 9),
    ('Sane', 10),
    ('B.Alper', 53),
    ('Torreira', 34),
    ('Lemina', 99),
    ('Yunus', 11),
    ('Jakobs', 4),
    ('Sallai', 7),
    ('Davinson', 6),
    ('Abdülkerim', 42),
    ('Uğurcan', 1)
""")

baglanti.commit()

print("Veri tabanı başarıyla oluşturuldu ve Oyuncular Eklendi!")

baglanti.close
