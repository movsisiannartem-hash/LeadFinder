def choose_source():
    print("Выберите источник: ")
    print("1 - Overpass")
    print("2 - 2GIS")
    n = int(input("Ваш выбор: "))




    if n == 1:
        return "Overpass"
    elif n == 2:
        return "2GIS"

    else:
        return None



