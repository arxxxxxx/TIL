function に static 修飾子を使うことでオブジェクトを生成しなくても使えるようになる
```php
class Hoge{
  public static function utilMethod(){
    // 処理
  }
}
// クラス名::staticメソッド名 で使用できる
Hoge::utilMethod();
```
