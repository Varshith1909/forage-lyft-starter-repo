from car import Car


class WilloughbyEngine(Car):
    def __init__(self, last_service_date, current_mileage, previous_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.previous_service_mileage = previous_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.previous_service_mileage > 60000
