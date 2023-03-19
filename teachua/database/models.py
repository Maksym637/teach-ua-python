from sqlalchemy import (
    Column, ForeignKey, Integer, BigInteger, Double, VARCHAR, Text, Date, Boolean
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))

    def __repr__(self):
        return f"Role(id={self.id}, name={self.name})"


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    email = Column(VARCHAR(255))
    first_name = Column(VARCHAR(255))
    last_name = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    phone = Column(VARCHAR(255))
    provider = Column(VARCHAR(255))
    provider_id = Column(VARCHAR(255))
    status = Column(Boolean)
    url_logo = Column(VARCHAR(255))
    verification_code = Column(VARCHAR(255))
    role_id = Column(Integer, ForeignKey(Role.id, ondelete="CASCADE"))

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, first_name={self.first_name})"


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(BigInteger, primary_key=True)
    description = Column(VARCHAR(30000))
    is_active = Column(Boolean)
    name = Column(VARCHAR(255))
    picture = Column(VARCHAR(255))
    registration_link = Column(VARCHAR(255))
    sort_number = Column(BigInteger)
    title = Column(VARCHAR(255))
    user_id = Column(BigInteger, ForeignKey(User.id, ondelete="CASCADE"))

    def __repr__(self):
        return f"Challenge(id={self.id}, name={self.name}, title={self.title})"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True)
    description = Column(VARCHAR(10000))
    name = Column(VARCHAR(255))
    picture = Column(VARCHAR(255))
    start_date = Column(Date)
    challenge_id = Column(BigInteger, ForeignKey(Challenge.id, ondelete="CASCADE"))
    header_text = Column(VARCHAR(10000))

    def __repr__(self):
        return f"Task(id={self.id}, name={self.name}, header_text={self.header_text})"


class Center(Base):
    __tablename__ = "centers"

    id = Column(BigInteger, primary_key=True)
    center_external_id = Column(BigInteger)
    contacts = Column(VARCHAR(3000))
    description = Column(Text)
    name = Column(VARCHAR(255))
    url_background_picture = Column(VARCHAR(255))
    url_logo = Column(VARCHAR(255))
    url_web = Column(VARCHAR(255))
    user_id = Column(BigInteger, ForeignKey(User.id, ondelete="CASCADE"))
    club_count = Column(BigInteger)
    rating = Column(Double)

    def __repr__(self):
        return f"Center(id={self.id}, name={self.name}, rating={self.rating})"


class Club(Base):
    __tablename__ = "clubs"

    id = Column(BigInteger, primary_key=True)
    age_from = Column(Integer)
    age_to = Column(Integer)
    center_external_id = Column(BigInteger)
    club_external_id = Column(BigInteger)
    contacts = Column(VARCHAR(3000))
    description = Column(Text)
    is_approved = Column(Boolean)
    is_online = Column(Boolean)
    name = Column(VARCHAR(255))
    rating = Column(Double)
    url_background = Column(VARCHAR(255))
    url_logo = Column(VARCHAR(255))
    url_web = Column(VARCHAR(255))
    work_time = Column(VARCHAR(255))
    center_id = Column(BigInteger, ForeignKey(Center.id, ondelete="CASCADE"))
    user_id = Column(BigInteger, ForeignKey(User.id, ondelete="CASCADE"))
    feedback_count = Column(BigInteger)

    def __repr__(self):
        return (f"Club(id={self.id}, name={self.name}, rating={self.rating})")
