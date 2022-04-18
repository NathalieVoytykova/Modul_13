tickets = int(input("Введите количество билетов: "))
cost = list ()
while True:
    if tickets >0:
        print(" Номер билета: ", tickets)
        age = int(input("Введите возраст посетителя: "))
        price = 0
        if age < 18:
            price += 0
            cost.append(price)
            print("Стоимость билета: ", price)
        elif 18 <= age < 25:
            price += 990
            cost.append(price)
            print("Стоимость билета: ", price)
        else:
            price += 1390
            cost.append(price)
            print("Стоимость билета: ", price)
            for elements in cost:
                sum_of_elements = sum(cost)
            print("Стоимость Вашего заказа: ", sum_of_elements)

            if tickets <= 3:
                discont_0 = 0
                print("Ваша скидка: ", discont_0)
                print("Сумма Вашего заказа с учетом скидки:", sum_of_elements)
            else:
                discont = sum_of_elements * 0.1
                new_cost = sum_of_elements * 0.9
                print("Ваша скидка: ", discont)
                print("Сумма Вашего заказа с учетом скидки:", new_cost)

        tickets -= 1
        break














