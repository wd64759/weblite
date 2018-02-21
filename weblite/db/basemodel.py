from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

import json
import re
from datetime import datetime, date

BaseModel = declarative_base()
reserved_attrs = ['_sa_instance_state']


def is_date(self, dateStr):
    m = re.match('\d{4}-\d{1,2}-\d{1,2}', dateStr)
    return True if m else False


def is_datetime(self, datetimeStr):
    m = re.match('\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}', datetimeStr)
    return True if m else False


def update_from(self, target):
    for f in self.get_update_fields():
        if hasattr(target, f):
            v = getattr(target, f)
            setattr(self, f, v)


def update_from_dict(self, dictObj):
    # remove the last_upd field
    if 'last_upd' in dictObj:
        dictObj.pop('last_upd')

    # handle the string to date conversion
    dt_fields = [x for x in dictObj.keys() if x.endswith('_dt') and x in self.get_update_fields()]

    for _df in dt_fields:
        dVal = dictObj.pop(_df)
        if self.isDateStr(dVal):
            dictObj[_df] = datetime.strptime(dVal, '%Y-%m-%d').date()
        if self.isDateTimeStr(dVal):
            dictObj[_df] = datetime.strptime(dVal, '%Y-%m-%d %H:%M:%S')

    for f in self.get_update_fields():
        if f in dictObj:
            v = dictObj[f]
            setattr(self, f, v)


class ModelEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            json.JSONEncoder.default(self, o)


def to_json(self):
    jDict = self.__dict__.copy()
    for x in reserved_attrs:
        if x in jDict:
            jDict.pop(x)
    return json.dump(jDict, cls=ModelEncoder, sort_keys=True)


BaseModel.update_from = update_from
BaseModel.update_from_dict = update_from_dict
BaseModel.to_json = to_json
BaseModel.is_date = is_date
BaseModel.is_datetime = is_datetime
