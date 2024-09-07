from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://healapp_admin:healapp_adminbnm@db-healapp-dev-inst.czgwgssk653p.us-east-2.rds.amazonaws.com:5432/db_healapp_dev"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)