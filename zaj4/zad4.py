def create_power_function(exponent):
    def power_function(base):
        return base ** exponent

    return power_function


square_function = create_power_function(2)
print(square_function(5))
