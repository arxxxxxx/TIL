### 2002エラー
プロジェクトファイルの.env
```yml
DB_HOST = mysql
DB_PORT = docker-composeで指定されているポート番号
```
mysqlコンテナに入る
```bash
docker exec -it laradock_mysql_1 /bash/bin
```
DB_DATABASEはmysqlに入って確認する
```yml
DB_DATABASE=default
DB_USERNAME=default
DB_PASSWORD=default
```

### 2054エラー
ユーザーの認証方式のエラーらしい...
```sql
mysql> SELECT user, host, plugin FROM mysql.user;
+------------------+-----------+-----------------------+
| user             | host      | plugin                |
+------------------+-----------+-----------------------+
| default          | %         | caching_sha2_password |
| root             | %         | caching_sha2_password |
| mysql.infoschema | localhost | caching_sha2_password |
| mysql.session    | localhost | caching_sha2_password |
| mysql.sys        | localhost | caching_sha2_password |
| root             | localhost | caching_sha2_password |
+------------------+-----------+-----------------------+
6 rows in set (0.00 sec)
```
pluginの　caching_sha2_password　を　mysql_native_password　に変更する
その後laradock/mysql/my.confで
```cnf
default_authentication_plugin= mysql_native_password
```
を追加する

以上で終了
とんでもなく時間がかかった
