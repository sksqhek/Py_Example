from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 32)

def sine_graph(amp, freq, theta, pattern):
    S = amp * np.sin(freq * X + theta)
    plt.plot(X, S, pattern + '--' )

sine_graph(1,2,0,'ro')
sine_graph(1,2,np.pi/2,'bo')
sine_graph(1,2,np.pi,'go')

plt.title('Example of matplotlib - sin(freq * X + theta)')
plt.xlabel('X')
plt.ylabel('sin(freq * X + theta)')

plt.show()