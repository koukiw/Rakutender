from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import env

# mysqlのDBの設定
ENDPOINT = f"mysql+pymysql://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}/{env.DB_NAME}?charset=utf8mb4"
print(ENDPOINT)
engine = create_engine(ENDPOINT)

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
# 予めテーブル定義の継承元クラスにqueryプロパティを仕込んでおく
Base.query = session.query_property()
