# Team10のバックエンド用リポジトリ

## 起動

--buildは初回起動時とかライブラリに変更があった場合にのみつける

```(bash)
docker-compose up -d --build
```

## コンテナ内に入る

```(bash)Cancel changes
docker-compose exec <サービス名> /bin/bash
```

## マイグレーション

```(bash)
docker-compose exec api /bin/bash

# コンテナ内で
python3 -m alembic upgrade head
python3 -m seed.py
```
