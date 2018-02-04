from datetime import datetime
from sqlalchemy import create_engine, Column, String, Float, Integer, Date, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from weblite import app

engine = create_engine(app.config(['DATABASE_URI'],
	convert_unicode=True,
	**app.config['DATABASE_CONNECT_OPTIONS']))

db_session = scoped_session(sessionmaker(autocommit=False,
	autoflush=False,
	bind=engine))

def init_db():
	Model.metadata.create_all(bind=engine)

Model = declarative_base(name='Model')
Model.query = db_session.query_property()

class Employee(Model):
	__tablename__ = 'employees'
	id = Column('staff_id', Integer, primary_key = True)
	name = Column(String(50))
	onboarding_dt = Column(DateTime)
	vendor_name = Column(String(50))
	soe_id = Column(String(8))
	ge_id = Column(Integer)
	rec_id = Column(String(15))
	name_cn = Column(String(20))
	resign_dt = Column(DateTime)
	phone = Column(String(30))
	location = Column(String(20))
	social_id = Column(String(50))
	citi_lv = Column(String(10))
	citi_key = Column(String(20))
	lead_id = Column(Integer)
	last_upd = Column(DateTime)

class Event(Model):
	__tablename__ = 'events'
	id = Column('id', Integer, primary_key = True)
	soe_id = Column(String(8))
	event_desc = Column(String(200))
	event_type = Column(String(50))
	event_date = Column(Date)
	last_upd = Column(DateTime)

class Feedback(Model):
	__tablename__ = 'feedbacks'
	id = Column('id', Integer, primary_key = True)
	soe_id = Column(String(8))
	provider = Column(String(20))
	comments = Column(String(200))
	catetory = Column(String(50))
	positive_score = Column(Integer)

class BCEHist(Model):
	__tablename__ = 'bcehist'
	id = Column('bce_id', Integer, primary_key = True)
	dev_id = Column(String(20))
	bce_val = Column(Float)
	bce_date = Column(Date)
	bce_category = Column(String(20))

class CodingHist(Model):
	__tablename__ = 'codinghist'
	id = Column('cid', Integer, primary_key = True)
	dev_id = Column(String(20))
	chg_lines = Column(Integer)
	chg_dt = Column(Date)

class PAHist(Model):
	__tablename__ = 'pahists'
	id = Column('pa_id', Integer, primary_key = True)
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
		return dict(id = self.id, name = self.name,
					salary_old = self.salary_old, salary_new = salary_new,
					promoted = self.promoted, effected_lv = self.effected_lv,
					effected_dt = self.effected_dt)

class ReleaseHist(Model):
	__tablename__ = 'relhist'
	id = Column('rid', Integer, primary_key = True)
	project = Column

class Features(Model):
	__tablename__ = 'featurehist'
	id = Column('fid', Integer, primary_key = True)
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

if __name__ == '__main__':
	print('ok.')
