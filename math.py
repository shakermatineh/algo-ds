import math

class RunningSampleStats:
    def __init__(self):
        self.n = 0
        self.mean = 0.0
        self.M2 = 0.0 #  sum of squares of differences from the mean
        self.std_dev = float('nan')

    def addNum(self, num: float) -> None:
        self.n += 1
        
        # Diff of new number and current mean
        delta = num - self.mean
        
        # mean_new = mean_old + (num - mean_old) / new_count
        self.mean += delta / self.n
        
        # Diff of the new number and updated mean
        delta2 = num - self.mean
        
        # M2_new = M2_old + (num - mean_old) * (num - mean_new)
        self.M2 += delta * delta2
        
        if self.n > 1:
            """
            Bessel's correction makes the sample variance an unbiased estimator of the population variance.
            An estimator is unbiased if the expected value (mean) of the estimator equals the true value 
            of the parameter being estimated.

            Sample mean itself is an estimate of true population mean and introduces a slight bias:
            Sample mean tends to be closer to the sample points than the true population mean would be.
            As a result nominator is smaller than it should be and it can be corrected by decrementing denominator. 
            If denom is n-1 we can prove that sample std is unbiased estimator or true std.
            """
            self.std_dev = math.sqrt(self.M2 / (self.n - 1))
        elif self.n == 1:
            # undefined for a single data point
            self.std_dev = float('nan')

    def findStandardDeviation(self) -> float:
        return self.std_dev

    def findMean(self) -> float:
        return self.mean

# Example usage
sample_stats = RunningSampleStats()
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    sample_stats.addNum(num)
    print(f"Added {num}: mean = {sample_stats.findMean()}, std_dev = {sample_stats.findStandardDeviation()}")
