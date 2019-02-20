## その前に
node.jsがインストールされているか確認
```sh
$node -v
```
npmがインストールされているか確認
```sh
$npm -v
```
yarnがインストールされているか確認
```sh
$yarn -v
```

## watchman をインストール
```sh
$brew install watchman
```
### watchman とは
https://mag.osdn.jp/13/06/05/075200
> 米Facebookによって開発されたファイルの変更監視ツール。
> ビルド作業を高速化するために同社内で開発されたツールで、ビルドの効率化を行える。
> 指定したディレクトリ下にあるファイルの変更をモニタリングする。
> 変更されたファイルの記録やあらかじめ指定しておいたアクションの実行などが可能で、自動ビルド、特定のファイルへの変更を通知する機能なども備える。

いわゆるタスクランナー。gulpやGruntなど

## expo-cli をインストール
```sh
$yarn global add expo-cli
```

## expoを動かす
任意のディレクトリでプロジェクトを作成
```sh
$expo init tommy-app
```
その後ディレクトリに移動し起動
```sh
$yarn start
```

## iOS simulator をインストール
- ブラウザに表示されたexpoの画面の「Run　on　iOS simulator」をクリック
- Xcodeを開きiOS simulatorをインストール（Xcodeを開かないといつまでたってもダウンロードが完了しないため)

## 参考
https://qiita.com/tommy96/items/448c87fd6950ec2b6265
