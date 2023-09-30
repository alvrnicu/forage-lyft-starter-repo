from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car

class car_factory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine,battery)

        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)

        return car

    def create_palindrome(current_date, warning_light_on): 
        battery = SpindlerBattery(warning_light_on)
        engine = SternmanEngine(warning_light_on)
        car = Car(engine, battery)

        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)

        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)

        return car