import pytest

from sqlalchemy import text, func
from sqlalchemy.sql import exists
from datetime import date

from weblite.db.dbhelper import *
from weblite.db.app_model import Staff


class TestDBHelper:
    session = db_session

    def setup_class(self):
        init_db()
        stmt = text('select name from sqlite_master where type = "table" and name = "staffs" ')
        rs = self.session.execute(stmt).fetchall()
        assert len(rs) == 1
        print('>>>>>> setup')

    @pytest.mark.dependency(name='create')
    @pytest.mark.parametrize("t_id", [1, 2, 3])
    def test_create(self, t_id):
        self.session.query(Staff).filter(Staff.id == t_id).delete()
        self.session.commit()

        t_staff = Staff(id=t_id, name='tester', c_level=100, on_boarding_dt=date.today(), phone='01234567')

        self.session.add(t_staff)
        self.session.commit()

    @pytest.mark.dependcy(name='query', depends=['create'])
    def test_query(self):
        rs = self.session.query(func.count('*')).select_from(Staff).scalar()
        assert rs == 3

        rs = self.session.query(Staff).filter(Staff.name.like('%test%')).limit(1).all()
        assert 'test' in rs[0].name, 'fail to find the test in query result'
        assert rs[0].on_boarding_dt == date.today()

        criteria = exists().where(Staff.c_level == 100)
        # scalar will throw exception if return multiple results
        rs = self.session.query(Staff.id).filter(criteria).limit(1).scalar()
        assert rs in [1, 2, 3]

    @classmethod
    def teardown_class(self):
        print('>>>>>> teardown')
        self.session.query(Staff).filter(Staff.name == 'tester').delete()
        self.session.commit()
