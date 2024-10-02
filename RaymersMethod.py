>>> w_0_init = (3.582) # Initial weight of the aircraft
>>> A = 0.86 # A set constant
>>> C = -0.05 # A set constant
>>> W_PAYLOAD = (0.2755) # Payload weight
>>> W_F = 0 # Weight of A/C with fuel
>>> ITERATIONS = 5 # Number of iterations
>>>
>>> # Raymer's equation, iterated i times
>>> def raymers(w_0, a, c, w_payload, w_f, i):
...     for _ in range(i):
...         w_0 = w_payload / (1 - (w_f / w_0) - (a * w_0 ** c))
...
...     # Return final weight in kg
...     return (w_0)
...
>>> print(raymers(w_0_init, A, C, W_PAYLOAD, W_F, ITERATIONS))
1.6948617629300344
