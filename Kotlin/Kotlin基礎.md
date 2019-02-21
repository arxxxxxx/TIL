## 基底はObjectクラスではなくAnyクラス
Kotlinのクラスは全て「Any」というクラスを継承しており、AnyのさらにスーパークラスとしてNull許容型であるAny?型が存在するという関係になります。

## 基本的な継承の書き方
extendsではなくコロン:で継承元クラスを指定。

kotlinのクラスはデフォルトではJavaでのfinal classになっており、クラスを拡張することはできません。
継承を想定したクラスを作成する場合はclassの宣言の前にopenを付ける必要があります。

#### 継承元がセカンドリコンストラクタだけの場合
「super」キーワードを使って基底クラスのコンストラクタを呼ぶ

## メソッドのオーバーライド
メソッドをオーバーライドする場合は継承元の「fun」の前に「open」を書き
継承したメソッドの「fun」の前に「override」を書く

## 参考
Android Studioで始めるKotlin入門（5)
https://www.atmarkit.co.jp/ait/articles/1804/24/news008.html
