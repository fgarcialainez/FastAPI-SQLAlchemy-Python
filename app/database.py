"""This module holds the SQLAlchemy DB connection logic"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create the DB connection url
SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

# Create the engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Get a reference to the base model
Base = declarative_base()
