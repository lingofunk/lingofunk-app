# Infrastructure 

## Структура

* `handler` — пакет с сервером 

## Описание

С помощью Docker-а поднимается несколько сервисов:

* flask-приложение
* база данных mongoDB


## Инструкция по развёртыванию

0. Зайти на [сайт](https://repo.continuum.io/miniconda/) с архивами версий Miniconda. Скачать Miniconda3-4.3.31-Linux-x86_64.sh (python 3.6.3)

1. Собрать docker-образ. На Ubuntu — с помощью команды:

    `
    sudo docker build -t test_docker .
    `

2. Запустить docker-образ. На Ubuntu — с помощью команды:

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