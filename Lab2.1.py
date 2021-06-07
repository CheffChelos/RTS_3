from matplotlib.pyplot import plot, show, legend
from numpy import zeros, sin, cos, random, pi

n = 6
ωгр = 1200
N = 64

def generate_signal():
	x = zeros(N)
	for i in range(n):
		amplitude = random.uniform(0.0, 1000.0)
		phase = random.uniform(-pi / 2, pi / 2)
		ω = ωгр / n * (i + 1)
		for t in range(N):
			x[t] += amplitude * sin(ω * t + phase)
	return x

def dft(signal):
	res = zeros(N)
	for p in range(N):
		sum = 0
		for k in range(N):
			angle = 2 * pi * p * k / N
			sum += signal[k] * complex(cos(angle), -sin(angle))
		res[p] = abs(sum)
	return res


random_signal = generate_signal()

plot(range(N), random_signal)
show()
plot(range(N), dft(random_signal))
show()