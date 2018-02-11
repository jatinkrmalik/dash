import flask
from models import *
from flask import jsonify


def view_user_det():
    byName = user_detail.objects.all()
    return jsonify(byName)


def view_sub_tbl():
    byName = subscriber_table.objects.all()
    return jsonify(byName)

def view_sub_pln():
    byName = subs_plan.objects.all()
    return jsonify(byName)


def view_trip():
    byName = trip.objects.all()
    return jsonify(byName)


def view_bus():
    byName = bus.objects.all()
    return jsonify(byName)


def view_route_det():
    byName = route_det.objects.all()
    return jsonify(byName)





commands = {'user_det': view_user_det,
            'subs_tbl': view_sub_tbl,
            'subs_pln' :view_sub_pln,
            'trip' :view_trip,
            'bus' :view_bus,
            'route_det' :view_route_det

            }


#commands[command](*vars)

