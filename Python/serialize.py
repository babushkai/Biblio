import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.date):
            return (str(z))
        else:
            return super().default(z)