Общие сведения
==============

"Внутренняя" часть проекта, ядро поисковика. 

Структура
---------

Работа закрытой части поисковой системы организована четырмя отдельными службами:

1. **Pudge**
  обеспечивает получение содержимого html-страниц и всех ссылок на этих страницах. 

#. **Patchwerk**
  проводит анализ полученных html-страниц, вычленяя значимые части. Формирует словарь данных, которые используются в кеше выдачи на фротенде и словарь значимых блоков текста, используемых для подсчета релевантности слов.

#. **Whisp**
  проводит подсчет релевантности слов во всех значимых блоках текста с учетом коэффициента важности.

#. **Nox**
  следит за временем. За временем "годности" полученных данных, временем выполнения тех или иных периодических задач. Ведет статистику, которая позволяет правильно распределить время. Составляет список задач для остальных служб.


Принцип работы
--------------

Принцип работы

Зависимости
-----------

* Python 2.7
* PostgreSQL
* REDIS
* Git