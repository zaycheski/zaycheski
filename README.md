# Зайчески <3

Привет, моя Варюшка!!!

Я наконец-то решил сделать обновление zaycheski в честь празднования Нового Года! (кчау). Кстати с Наступающим тебя!!!

![Kchauuu](./img/kiss.jpg)

Я решил немного переписать zaycheski, чтобы сделать его более изменяемым и легко устанавливаемым, а также, чтобы можно было делать регулярные обновления (кчау).


## Инструкция по установке zaycheski

- Первым делом открой терминал и перейди в любую папку на твоем компьютере, в которую не жалко временно склонировать этот репозиторий (репозиторий == папка).
- Теперь нужно склонировать этот репозиторий к себе в папку. Для этого просто вбей команду "git clone https://github.com/maximshuklin/zaycheski.git" в свой терминал.
- Сейчас в папке, в который ты находишься должна была появится папка "zaycheski". Перейди в нее "cd zaycheski"!
- А теперь запусти установитель зайческого. Для этого выполни команду "python3 zaycheski-setup.py" и следуй инструкциям этой программы!
- Отлично! У тебя получилось установить zaycheski! Можешь спокойно удалить директорию "zaycheski" со своего компьютера и zaycheski будет работать!

Если че-то не работает, то вбей команду "pip install -r requirements.txt" - она установит модули, которые использует zaycheski и которых у тебя нет. А заодно и лишней фигни может установит - но ничего страшного! После этого запусти установителя зайческого еще разок!

В случае проблем отбращаться к зайческому.

## А что если хочется добавить новых фотографий?

Это можно сделать! К тому же, ты имеешь полный доступ к этому репозиторию на github, поэтому твои изменения смогу увидеть и я. Так как же добавить новую фотографию? Есть два варианта:

1) Если у тебя уже есть фотография, переведенная в ASCII-символы в формате .txt (то есть #, $, ., ; и т.д.), то можешь поступить следующим образом:
    - Склонировать этот репозиторий себе "git clone https://github.com/maximshuklin/zaycheski.git"
    - Добавить .txt файл в папку ascii_images в формате **i_love_varya_1234**, где вместо 1234 может быть любое еще не занятое число
    - Залить эти изменения на github: 
      - git add .
      - git commit -m "Я залила фоточку"
      - git push

    P.S. можешь воспользоваться онлайн-сервисом для перевода картинок в ASCII таблицу - [www.ascii-art-generator.org](https://www.ascii-art-generator.org/)
2) Если ты хочешь добавить фотографию, но она не переведена ASCII, то можешь поступить следующим образом:
      - Склонировать этот репозиторий себе "git clone https://github.com/maximshuklin/zaycheski.git"
      - Запустить файл "python3 adder.py" и следовать инструкциям (нужно будет указать путь до фотографии).
      - Adder.py выведет перевод в ASCII-символы и предложит добавить эту фоточку в репозиторий. Если тебе перевод понравился, то нажми клавишу "y" и фотка добавиться в ascii_images.
      - Далее нужно залить эти изменения на github:
        - git add .
        - git commit -m "Я залила фоточку"
        - git push
    
    P.S. Пока что adder.py работает не очень хорошо - часто ASCII перевод выглядит не очень :(
 3) Скинуть фотографию своему любимому зайке (только любимому) и попросить его залить новую фоточку в zaycheski. Он это обязательно сделает.

После того, как новая фотография добавлена, нужно будет заново склонировать репозиторий и запустить "python3 zaycheski-setup.py" (по сути заново пройти инструкцию по установке).
