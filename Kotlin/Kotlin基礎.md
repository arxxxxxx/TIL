
## 基底はObjectクラスではなくAnyクラス
Kotlinのクラスは全て「Any」というクラスを継承しており、AnyのさらにスーパークラスとしてNull許容型であるAny?型が存在するという関係になります。

## 基本的な継承の書き方
```kt
// 基底クラスAnimal。openを付けないと継承できない
open class Animal{}
// Animalを継承したCatクラス。「extends」ではなく「:」で基底クラスを指定する
class Cat: Animal(){}
```
