## search.phpの2ページめはどこ？
http://○○○/?s=test の場合2ページ目のurlは
http://○○○/page/2/?s=test になる

## コード
```php
if ($wp_query->max_num_pages > 1) {
  echo "<div class='pagination'>";
  echo paginate_links(array(
    'base' => site_url() . '%_%' . '/?s',
    'format' => '/page/%#%',
    'current' => max(1, $paged),
    'total' => $wp_query->max_num_pages,
  ));
  echo "</div>";
}
```

### paginate_links()
記事一覧のページ番号付きリンクを取得する
引数には配列を渡す

#### 引数の配列で指定できるオプション
##### base
    ページ番号付きリンクを作る際のベースのURLを指定する '%_%'で特定の文字列を挿入できる
##### format
    baseで指定した場所('%_%')に挿入する文字列を設定
##### current
    現在のページ番号を表示する
##### total
    全体のページを設定する
