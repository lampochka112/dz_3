number = int(input("введите номер дня недели:"))
match number:
    case 1 :
        print("понидельник")
    case 2:
        print("вторник")
    case 3:
        print("среда") 
    case 4:
        print("четверг")
    case 5:
        print("пятница")
    case 6:
        print("суббота")
    case 7:
        print("воскресенье")
    case _:
        print("такого дня не существует")
        

