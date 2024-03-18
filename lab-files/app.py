def hello_world():
    return 'Hello, World!'

def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return (x1, x2)

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

    def fibonacci(n):
        """
        Generate the Fibonacci series up to the given number.

        Parameters:
        n (int): The number up to which the Fibonacci series should be generated.

        Returns:
        list: The Fibonacci series as a list.

        """
        fib_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers
        while len(fib_series) < n:
            next_num = fib_series[-1] + fib_series[-2]  # Calculate the next number in the series
            fib_series.append(next_num)  # Add the next number to the series
        return fib_series

"""
function calculateCarPrice(gasMileage, year, milesPerGallon) {
    const basePrice = 20000; // This is a placeholder value. Replace it with your own logic.
    const currentYear = new Date().getFullYear();
    const age = currentYear - year;

    // Assume the car loses 5% of its value for each year
    const depreciation = basePrice * 0.05 * age;

    // Assume the car is driven 12000 miles per year and the price of gas is $2.5 per gallon
    const yearlyGasCost = (12000 / milesPerGallon) * 2.5 * gasMileage;

    const finalPrice = basePrice - depreciation + yearlyGasCost;

    return finalPrice;
}
"""