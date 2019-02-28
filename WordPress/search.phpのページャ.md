## search.phpの2ページめはどこ？
http://○○○/?s=testの場合2ページ目のurlは
http://○○○/page/2/?s=testになる

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

### paginate links()
記事一覧のページ番号付きリンクを取得する
引数には配列を渡す

### 配列の中のオプション
