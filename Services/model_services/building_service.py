import models.building as mb


def create_building(name, price, income, build_time):
    return mb.Building(name, price, income, build_time)
