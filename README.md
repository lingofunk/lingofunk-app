# Infrastructure 

Каталог демок и вебморда к ним.

```bash
.
├── docker-compose.yml
├── README.md
├── webapp                  # веб-приложение с мордой
│   ├── Dockerfile          
│   ├── main.py             # само приложение
│   ├── requirements.txt    # питоновые пакеты исключительно для фласка
│   └── templates
│       ├── index.html      # шаблон для главной, здесь размещать ссылку на демки
│       └── worker_demo.html # шаблон для странички с конкретной демкой, одна демка == один шаблон 
└── worker_one              # пример демки, одна демка == одна папка
    ├── Dockerfile          # докерфайл надо будет переписать под свои нужды
    ├── main.py             # веб-приложение с одной ручкой, должно грузить модель и отвечать на эту ручку
    └── requirements.txt    # питоновые пакеты для этой демки
```


## Описание

С помощью docker-compose поднимается несколько сервисов:

* flask-приложение с каталогом и вебмордами
* flask-приложение с демо-демкой


## Пререквизиты

Поставить [docker](https://docs.docker.com/install/) и [docker-compose](https://docs.docker.com/compose/install/).



## Инструкция по локальному развёртыванию 


Стащить последнюю версию репозитория и в корне проекта запустить docker-compose 
```bash
git pull
docker-compose up
```



## Разные (возможно, полезные) команды
  * Почистить результаты неудачной сборки:

    ```
    sudo docker rmi test_docker --force
    sudo docker rmi $(sudo docker images -f "dangling=true" -q)
    ```

  * Посмотреть историю образа (есть и информация про размер по памяти):

    `
    sudo docker history test_docker
    `

  * Экспортировать образ и заархивировать его:

    `
    sudo docker save test_docker > test_docker.tar
    zip docker_archive  test_docker.tar
    `