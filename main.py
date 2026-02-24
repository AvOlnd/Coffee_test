import sqlite3
from tabulate import tabulate

def display_all_coffee():
    try:
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, roast_level, grind_type, 
                   flavor_description, price, package_volume 
            FROM coffee
            ORDER BY id
        ''')
        
        rows = cursor.fetchall()
        
        headers = ["ID", "Название", "Степень обжарки", "Тип", 
                   "Описание вкуса", "Цена (руб)", "Объем (г)"]
        
        print("\n" + "="*100)
        print(" " * 35 + "КАТАЛОГ КОФЕ")
        print("="*100)
        
        print(tabulate(rows, headers=headers, tablefmt="grid", 
                      stralign="left", numalign="right"))
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")

def main():
    try:
        from tabulate import tabulate
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
        from tabulate import tabulate
    
    display_all_coffee()

if __name__ == "__main__":
    main()
