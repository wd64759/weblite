from sqlalchemy import Column, String, Float, Integer, Date, DateTime
from weblite.db.basemodel import BaseModel


class Staff(BaseModel):
    __tablename__ = 'staffs'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(50))
    on_boarding_dt = Column(Date)
    soe_id = Column(String(8))
    ge_id = Column(Integer)
    red_id = Column(String(15))
    gender = Column(String(1))
    team = Column(String(50))
    phone = Column(String(20))
    c_level = Column(Integer)
    status = Column(Integer)
    comment = Column(String(100))
    techset = Column(String(50))
    last_upd = Column(DateTime)

    def get_update_fields(self):
        return ['soe_id', 'on_boarding_dt', 'phone', 'c_level', 'status', 'team', 'comment', 'techset']

    def get_date_fields(self):
        return ['on_boarding_dt']

    def __repr__(self):
        return 'id={},name={},last_upd={}'.format(self.id, self.name, self.last_upd)


class Event(BaseModel):
    __tablename__ = 'events'
    id = Column('id', Integer, primary_key=True)
    soe_id = Column(String(8))
    event_desc = Column(String(200))
    event_type = Column(String(50))
    event_date = Column(Date)
    last_upd = Column(DateTime)


class Feedback(BaseModel):
    __tablename__ = 'feedbacks'
    id = Column('id', Integer, primary_key=True)
    soe_id = Column(String(8))
    provider = Column(String(20))
    comments = Column(String(200))
    catetory = Column(String(50))
    positive_score = Column(Integer)


class BCEHist(BaseModel):
    __tablename__ = 'performance'
    id = Column('bce_id', Integer, primary_key=True)
    dev_id = Column(String(20))
    bce_val = Column(Float)
    bce_date = Column(Date)
    bce_category = Column(String(20))


class CodingHist(BaseModel):
    __tablename__ = 'performance_details'
    id = Column('cid', Integer, primary_key=True)
    dev_id = Column(String(20))
    chg_lines = Column(Integer)
    chg_dt = Column(Date)


class PAHist(BaseModel):
    __tablename__ = 'salaries'
    id = Column('pa_id', Integer, primary_key=True)
    name = Column(String(50))
    salary_old = Column(Float)
    salary_new = Column(Float)
    promoted = Column(String(1))
    effected_lv = Column(String(3))
    effected_dt = Column(DateTime)

    def __init__(self, name, salary_old, salary_new, promoted, effected_lv, effected_dt):
        self.name = name
        self.salary_old = salary_old
        self.salary_new = salary_new
        self.promoted = promoted
        self.effected_lv = effected_lv
        self.effected_dt = effected_dt

    def to_json(self):
        return dict(id=self.id, name=self.name,
                    salary_old=self.salary_old, salary_new=self.salary_new,
                    promoted=self.promoted, effected_lv=self.effected_lv,
                    effected_dt=self.effected_dt)


class ReleaseHist(BaseModel):
    __tablename__ = 'sprints'
    id = Column('rid', Integer, primary_key=True)
    project = Column


class Features(BaseModel):
    __tablename__ = 'features'
    id = Column('fid', Integer, primary_key=True)
    fname = Column(String(50))
    soe_id = Column(String(8))
    bizcxt = Column(String(200))
    storypoint = Column(Integer)
    project = Column(String(30))
    module = Column(String(20))
    release_id = Column(Integer)
    status = Column(String(10))
    tag = Column(String(30))
    last_upd = Column(DateTime)
