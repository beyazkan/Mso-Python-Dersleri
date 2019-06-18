from os import system, name

# Komut Satırı Arayüzünü Temizleyen fonksiyon
def clear():
    """
        Bu fonksiyon komut satırı arayüzünü ilk haline getirir.
    """
    # İşletim Sistemi Windows ise
    if name == 'nt':
        _ = system('cls')

    # Windows dışı işletim sistemi ise
    else:
        _ = system('clear')


