# Задача 4. Вариант 2.
#Напишите программу, которая выводит имя, под которым скрывается Михаил Евграфович Салтыков. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Andzhukaev E.S.
#12.03.2017

Name = "Николай Щедрин"
print ("Михайл Евграфович Салтыков более известен, как", Name)
Interests = "писатель, журналист,вице-губернатор."
print ("\nОбласть интересов: ", Interests)
PlaceOfBirth = "село Спас-Угол, Калязинский уезд, Тверская губерния"
print ("\nМесто рождения: ", PlaceOfBirth)
DateOfBirth = ("1826")
DateOfBirth = int(DateOfBirth)
print ("\nГод рождения: ", DateOfBirth)
DateOfDeath = ("1889")
DateOfDeath = int(DateOfDeath)
print ("\nГод смерти: ", DateOfDeath)
Age = (DateOfDeath - DateOfBirth)
print ("\nНиколай Щедрин умер в возрасте" , Age, " лет.")
input ('\n\nНажмите Enter для выхода.')