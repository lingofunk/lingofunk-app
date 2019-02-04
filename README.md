# Infrastructure 

## Структура

* `handler` — пакет с сервером 

## Описание

С помощью Docker-а поднимается несколько сервисов:

* flask-приложение
* база данных mongoDB


## Инструкция по развёртыванию

1. Собрать docker-образ.
На машине с Ubuntu это можно сделать с помощью команды:

    `
    sudo docker build -t test_docker .
    `

2. Запустить docker-образ.
На машине с Ubuntu это можно сделать с помощью команды:

    `
    sudo docker-compose up
    `

## Разные (возможно, полезные) команды
  * Почистить результаты неудачной сборки:
    `
    sudo docker rmi test_docker --force
    sudo docker rmi $(sudo docker images -f "dangling=true" -q)
    `

  * Посмотреть историю образа (есть и информация про размер по памяти):
    `
    sudo docker history test_docker
    `

  * Экспортировать образ и заархивировать его:

    `
    sudo docker save test_docker > test_docker.tar
    zip docker_archive  test_docker.tar
    `