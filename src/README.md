# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

> 🇯🇵 [日本語のドキュメントはこちら](#日本語ドキュメント)

## Features

- View all available extracurricular activities
- Sign up for activities
- Unregister from activities

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/signup?email=student@mergington.edu` | Unregister from an activity                                         |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.

---

## 日本語ドキュメント

# Mergington High School 課外活動 API

生徒が課外活動を閲覧し、参加登録できるシンプルな FastAPI アプリケーションです。

## 機能

- 利用可能な課外活動の一覧表示
- 活動への参加登録
- 活動からの登録解除

## セットアップ

1. 依存パッケージをインストールします:

   ```
   pip install fastapi uvicorn
   ```

2. アプリケーションを起動します:

   ```
   python app.py
   ```

3. ブラウザで以下のURLにアクセスします:
   - APIドキュメント: http://localhost:8000/docs
   - 代替ドキュメント: http://localhost:8000/redoc

## APIエンドポイント

| メソッド | エンドポイント                                                     | 説明                               |
| -------- | ----------------------------------------------------------------- | ---------------------------------- |
| GET      | `/activities`                                                     | すべての活動の詳細と参加者数を取得 |
| POST     | `/activities/{activity_name}/signup?email=student@mergington.edu` | 活動に参加登録する                 |
| DELETE   | `/activities/{activity_name}/signup?email=student@mergington.edu` | 活動の登録を解除する               |

## データモデル

アプリケーションはシンプルなデータモデルを使用しています:

1. **活動 (Activities)** - 活動名を識別子として使用:

   - 説明 (description)
   - スケジュール (schedule)
   - 最大参加人数 (max_participants)
   - 参加中の生徒のメールアドレス一覧 (participants)

2. **生徒 (Students)** - メールアドレスを識別子として使用:
   - 氏名
   - 学年

すべてのデータはメモリ上に保存されます。サーバーを再起動するとデータはリセットされます。

## テスト

テストを実行するには:

```
pip install pytest pytest-asyncio
pytest tests/
```
