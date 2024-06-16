## Запуск

Запуск производится внутри докер контейнера:

```
docker build -t get-mtu .
docker run -it --rm get-mtu [host]
```
где host - ip адрес конечного хоста. Внутри себя скрипт перебирает mtu бинарным поиском и пингует хост назначения.
Пример использования (здесь конечный хост - google.com):

```
docker build -t get-mtu .
docker run -it --rm get-mtu 216.58.211.238
```
```
MTU for channel: 1452
```
```
docker run -it --rm mtu 'incorrect_arg'
```
```
Invalid host value
```