### @extends('layout')でエラー
```bash
View [layout] not found. (View: /vagrant/code/sampleapp/resources/views/Posts/index.blade.php)
```
#### 出てきた答え
>resources
>  ↳views
>    ↳pages
>      ↳layouts
>         app.blade.php
resources/viewsディレクトリを基準にしてブレードテンプレートを参照する必要があります。
正しくは
```php
@extends('pages.layout')
```
となる
