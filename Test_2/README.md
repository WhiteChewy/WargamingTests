#Циклический буффер FIFO

---

В рамках 2ого тестового задания требовалось написать минимум по 2 класса реализовывающих циклический буффер FIFO (Firs In
First Out) и объяснить плюсы и минусы каждой реализации. Было реализовано 2 хороших решения (*list_usage.py* и *deque_usage.py*)
и для примера 1 "плохое" решение (*list_inherited.py*)

##list_inherited.py

Не самое удачное решение поскольку используется наследование от стандартного типа list. Это плохо по двум причинам:
1. Undefined Behaviour при миграции версий
2. Плохая читаемость кода

Из наиболее ярких минусов наблюдаются следующие:
1. При создании объекта такого класса self является самим списком и это не позволяет нам "нормально" использовать например изменение через срезы и реализовывать 
дополнительный метод shift() который возвращает сдвинутый массив, вместо того чтобы просто использовать следующую конструкцию
   ```python
   self.buffer = self.buffer[1:]
   ```
что коссвенно влияет на пункт 2 указанный выше

2. Приходится использовать конструкции вида:
   ```python
   super(CycledBuffer, self).pop()
   ```
   для того чтобы использовать методы родительского класса.

Все выше перечисленное противоречит Дзену Пайтона. Из плюсов пожалуй только если то, что код работает и реализованы полезные
вспомогательные инструменты ввиде методов *getEmptySlots*, *getMaxLen* и *isEmpty*

##list_usage

Пример того чтобы сделал не самый плохой программист с идеей в основе реализации *list_inherited.py*. Рабочий и вполне неплохой bruteforce.

####+
1. Читаемость кода
2. Возбуждение изсключения *IndexError* при попытки изъятия объекта из пустого буфера.
3. Добавлены методы *getEmptySlots*, *getMaxLen* и *isEmpty* которые являются полезным инструментом, но не требовались в рамках задания

####-
1. Так как используется стандартный тип list, а его поведение не очень подходит для Cycled Buffer (FIFO), то некоторые действия
с буфером приходится самому придумывать реализацию некоторых функций


##deque_usage
На мой взгял самое лучшее решение которое можно предоставить в рамках текущей задачи. Если понять смысл работы циклического
буффера FIFO и вспомнить о таком полезном модуле *collections* можно понять что по функционалу они (буффер и deque) очень похожи
а значит все что требуется это "красиво обернуть" deque в рамках задания.

####+
1. Читаемость кода
2. Возбуждение изсключения *IndexError* при попытки изъятия объекта из пустого буфера.
3. Добавлены методы *getEmptySlots*, *getMaxLen* и *isEmpty* которые являются полезным инструментом, но не требовались в рамках задания
4. Не требуется с нуля расписывать большинство инструментария для работы с буфером, а значит вероятность ошибки сведена к минимуму

####-

Не обнаружил. В рамках задачи считаю реализацию лучшим решением