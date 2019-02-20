
## 基底はObjectクラスではなくAnyクラス
Kotlinのクラスは全て「Any」というクラスを継承しており、AnyのさらにスーパークラスとしてNull許容型であるAny?型が存在するという関係になります。

## 基本的な継承の書き方
extendsではなくコロン:で基底クラスを指定します。
```kt
// 基底クラスAnimal。openを付けないと継承できない
open class Animal{}
// Animalを継承したCatクラス。「extends」ではなく「:」で基底クラスを指定する
class Cat: Animal(){}
```
{% tag_round att 注意 %}
注意
{% endtag_round %}

## 基底クラスのコンストラクタ呼び出し
「Person」クラスのプライマリコンストラクタでは「firstName」「lastName」の２つのプロパティが定義されています。
それを継承したBussinessPersonクラスのコンストラクタでは、firstName、lastNameの2つの引数に加えてageプロパティを定義しています。
firstName、lastName引数については、基底クラスであるPersonクラスのコンストラクタに渡しています。
```kt
// 基底クラス
open class Person(val firstName: String,val lastName: String = ""){....}

// 継承クラス。継承元のコンストラクタを指定
class BussinessPerson(firstName: String,lastName: String = "",val age: Int) : Person (firstName,lastName){....}
```
