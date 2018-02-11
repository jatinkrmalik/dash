import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()


class route_det(db.Document):
    route_no = db.StringField(max_length=60)
    src= db.IntField()
    dest= db.IntField()
    from_to_flag = db.BooleanField()

class bus(db.Document):
    bus_id = db.IntField()
    driver_name = db.StringField(max_length=60)
    vend_id= db.StringField(max_length=60)
    route_no = route_det.route_no
    no_of_seat = db.IntField()


class subs_plan(db.Document):
    plan_id=db.IntField()
    route_no = db.ListField()
    no_of_day = db.IntField()
    plan_price = db.IntField()




class trip(db.Document):
    phone = db.StringField(max_length=60)
    trip_id = db.IntField()
    bus_id=db.IntField()
    route_no = db.IntField()
    time_stamp= db.DateTimeField()





class user_detail(db.Document):

    phone = db.StringField(max_length=60)
    email = db.EmailField(max_length=60)
    gender = db.StringField()
    address = db.StringField()
    name = db.StringField(max_length=60)
    credits=db.IntField()
    last_ten_trip=db.ListField()




class subscriber_table(db.Document):
    count_ride= db.IntField()
    route_no= db.IntField()
    phone = db.StringField(max_length=60)
    plan_id= db.IntField()
    trip_id= db.IntField()
    plan_validity= db.DateTimeField()





















