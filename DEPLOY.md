# デプロイ手順

## 事前準備

1. PyPIアカウントの設定
   - [PyPI](https://pypi.org)でアカウントを作成（まだの場合）
   - Account Settings → API tokens で新しいトークンを生成
   - トークンをGitHubリポジトリのSecretsに追加
     - GitHubリポジトリの Settings → Secrets → New repository secret
     - 名前: `PYPI_API_TOKEN`
     - 値: PyPIで生成したトークン

2. パッケージ情報の更新
   - `setup.py`の以下の項目を確認・更新
     - `version`: 新しいバージョン番号（セマンティックバージョニング推奨）
     - `author`: 作者名
     - `author_email`: 連絡先メールアドレス
     - `url`: GitHubリポジトリのURL
     - `description`: パッケージの説明
   - `README.md`の更新（必要に応じて）
   - ドキュメントの更新（必要に応じて）

## デプロイ方法

1. 変更をコミット
   ```bash
   git add .
   git commit -m "Update package information and documentation"
   git push origin main
   ```

2. 新しいバージョンのタグを作成してプッシュ
   ```bash
   git tag v1.1.39  # バージョン番号を適切に設定
   git push origin v1.1.39
   ```

3. GitHub Actionsの実行
   - タグがプッシュされると、自動的にGitHub Actionsが実行されます
   - Actionsタブでデプロイの進行状況を確認できます
   - 成功すると、新しいバージョンがPyPIに公開されます
   - ドキュメントがGitHub Pagesに自動的にデプロイされます

## 注意事項

- バージョン番号は必ず更新してください（同じバージョンでの再デプロイはできません）
- PyPIトークンは安全に管理し、GitHub Secretsとして保存してください
- デプロイ前に`setup.py`と`README.md`の内容が正しいことを確認してください
- テストを実行して、パッケージが正しく動作することを確認してください
- ドキュメントの更新が必要な場合は、`docs/`ディレクトリ内のファイルを編集してください 