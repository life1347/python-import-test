## Example1

### build docker image

```
cd example1
docker build -t py3env:example1 .
```

### run image

```
docker run --rm -it -p 8888:8888 py3env:example1
```

### 在 container 內執行下列步驟

```
docker exec -it <docker id> sh
$ mv /app/userfunc /           # in container
```

### container 外面 curl 該 container 的 8888 port

```
curl http://127.0.0.1:8888/specialize
```

Console log 出現

```
2017-07-30 17:41:36,997 - ERROR - Exception on /specialize [POST]
Traceback (most recent call last):
  File "/usr/lib/python3.5/site-packages/flask/app.py", line 1988, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3.5/site-packages/flask/app.py", line 1641, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3.5/site-packages/flask/app.py", line 1544, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/lib/python3.5/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "/usr/lib/python3.5/site-packages/flask/app.py", line 1639, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3.5/site-packages/flask/app.py", line 1625, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "server.py", line 20, in load
    userfunc = (imp.load_source('user', codepath)).main
  File "/usr/lib/python3.5/imp.py", line 172, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 693, in _load
  File "<frozen importlib._bootstrap>", line 673, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 665, in exec_module
  File "<frozen importlib._bootstrap>", line 222, in _call_with_frames_removed
  File "/userfunc/user", line 3, in <module>
    import yaml
ImportError: No module named 'yaml'
172.17.0.1 - - [30/Jul/2017 17:41:37] "POST /specialize HTTP/1.1" 500 -
```

表示無法 import yaml 這個 module

## Example2

### build docker image

```
cd example2
docker build -t py3env:example2 .
```

### run image

```
docker run --rm -it -p 8888:8888 py3env:example2
```

### container 外面 curl 該 container 的 8888 port

```
curl http://127.0.0.1:8888/specialize
```

Console log 出現

```
['/app', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-linux', '/usr/lib/python3.5/lib-dynload', '/usr/lib/python3.5/site-packages', '/userfunc']
172.17.0.1 - - [30/Jul/2017 17:37:18] "POST /specialize HTTP/1.1" 200 -
```

## Example3

### build docker image

```
cd example3
docker build -t py3env:example3 .
```

### run image

```
docker run --rm -it -p 8888:8888 -v absolute/path/to/userfunc/:/userfunc py3env:example3
```

### container 外面 curl 該 container 的 8888 port

```
curl http://127.0.0.1:8888/specialize
```

Console log 出現

```
['/app', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-linux', '/usr/lib/python3.5/lib-dynload', '/usr/lib/python3.5/site-packages', '/userfunc']
172.17.0.1 - - [30/Jul/2017 17:37:18] "POST /specialize HTTP/1.1" 200 -
```