## 基底はObjectクラスではなくAnyクラス
Kotlinのクラスは全て「Any」というクラスを継承しており、AnyのさらにスーパークラスとしてNull許容型であるAny?型が存在するという関係になります。

## 基本的な継承の書き方
extendsではなくコロン:で継承元クラスを指定。
```kt
// 基底クラスSpam
open class Spam{}
// Spamを継承したSpam2クラス。「extends」ではなく「:」で基底クラスを指定する
class Cat: Spam2(){}
```
kotlinのクラスはデフォルトではJavaでのfinal classになっており、クラスを拡張することはできません。
継承を想定したクラスを作成する場合はclassの宣言の前にopenを付ける必要があります。

## 基底クラスのコンストラクタ呼び出し
```kt
// 基底クラス
open class Hoge(val fuga: String,val piyo: String = ""){....}

// 継承クラス。継承元のコンストラクタを指定
class Hoge2(fuga: String,piyo: String = "",val age: Int) : Hoge (fuga,piyo){....}
```
#### 継承元がセカンドリコンストラクタだけの場合
「super」キーワードを使って基底クラスのコンストラクタを呼ぶ
```kt
// プライマリコンストラクタのないクラス
class SecondB : Second {
  // セカンダリコンストラクタはsuperキーワードで直接基底クラスのコンストラクタを呼び出す
  constructor(a:Any) : super(a){
  }
  // 同上
  constructor(a: Any,b: Any) : supper(a,b){
  }
}
```

## 参考
Android Studioで始めるKotlin入門（5)
https://www.atmarkit.co.jp/ait/articles/1804/24/news008.html
