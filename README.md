# Python Notepad

Простой блокнот на Python с графическим интерфейсом Tkinter.<br>
<strong>Проект свободен для использования любым желающим.</strong>

---

## Описание

Проект представляет собой текстовый редактор с основными функциями:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Создание новых вкладок и закрытие текущей или последней вкладки<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Открытие и сохранение файлов (`Save`, `Save As`, `Save all`)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Вырезание, копирование, вставка и удаление текста<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Поиск, переход к следующему/предыдущему совпадению, замена текста<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Выделение всего текста и вставка текущей даты/времени<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Изменение шрифта и размера текста<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Изменение масштаба текста (Zoom in, Zoom out, Restore default zoom)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Горячие клавиши для быстрого доступа ко всем функциям

---

## Установка

1.&nbsp;&nbsp;Склонируйте репозиторий:<br>
```
bash
git clone https://github.com/DanVolov/Блокнот.git
```

2.&nbsp;&nbsp;Установите зависимости:<br>
```
pip install -r requirements.txt
```

---

## Использование

Через Python:<br>
Запуск блокнота:<br>
```
python Notepad.py
```

Через скомпилированный файл:<br>
&nbsp;&nbsp;&nbsp;&nbsp;В папке dist есть готовый .exe файл:<br>
&nbsp;&nbsp;&nbsp;&nbsp;dist/Notepad.exe<br>
&nbsp;&nbsp;&nbsp;&nbsp;Просто запустите его двойным кликом.

---

## Структура проекта

Блокнот/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── Notepad.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Главный файл проекта<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── requirements.txt &nbsp;&nbsp;# Зависимости проекта<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── icon.ico &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Иконка приложения<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Этот файл<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── build/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Папка с файлами сборки PyInstaller<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── Notebook.spec &nbsp;&nbsp;&nbsp;# Файл сборки PyInstaller<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── dist/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Notepad.exe &nbsp;&nbsp;&nbsp;&nbsp;# Скомпилированный исполняемый файл<br>

---

## Горячие клавиши

File<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + N — новая вкладка<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + O — открыть файл<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + S — сохранить<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + Shift + S — сохранить как<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + Alt + S — сохранить все<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + W — закрыть вкладку<br>

Edit<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + Z — отмена<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + X — вырезать<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + C — копировать<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + V — вставить<br>
&nbsp;&nbsp;&nbsp;&nbsp;Delete — удалить<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + F — найти<br>
&nbsp;&nbsp;&nbsp;&nbsp;F3 — найти далее<br>
&nbsp;&nbsp;&nbsp;&nbsp;Shift + F3 — найти ранее<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + H — заменить<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + G — перейти к строке<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + A — выделить всё<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + T — вставить текущие дату и время<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + F — изменить шрифт<br>

View<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + + — увеличить текст<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + - — уменьшить текст<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ctrl + 0 — восстановить масштаб<br>

---

## Вклад

Если хотите помочь:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Форкните репозиторий<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Создайте ветку для фичи (git checkout -b feature/имя-фичи)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Сделайте коммит (git commit -m "Добавил новую функцию")<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Отправьте изменения (git push origin feature/имя-фичи)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Создайте Pull Request<br>
