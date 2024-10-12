Attempt 1
W_0 = 3.582
A = 0.86
C = -0.05
W_payload = 0.2755
W_F = 0
ITERATIONS = 10

def raymers(W_0, A, C, W_payload, W_F, i):
    for _ in range (i):
        W_0 = W_payload / (1 - (W_F / W_0) - (A * W_0 ** C))

        
print(raymers(W_0, A, C, W_payload, W_F, ITERATIONS))

Attempt 2
W_0_Initial = (3.58225118) # Initial Estimate Weight Of Aircraft
A = (0.86) # Constant
C = (-0.05) # Constant
W_Payload = (0.27557783) # Payload Weight
W_F = (0) # Weight Of Fuel

WeW0 = A * W_0_Initial ** C
print(WeW0)

W0 = W_Payload / (1 - 0 - WeW0)
print(W0)








attempt 3 
W_0 = 3.582
A = 0.86
C = -0.05
W_payload = 0.2755
W_F = 0
ITERATIONS = 10
i = i + 1

def raymers(W_0, A, C, W_payload, W_F, i):
    for ITERATIONS in range(i):
        W_0 = W_payload / (1 - (W_F / W_0) - (A * W_0 ** C))

print(raymers(W_0, A, C, W_payload, W_F, ITERATIONS))

attempt 4
W_0 = 3.582
A = 0.86
C = -0.05
W_payload = 0.2755
W_F = 0
ITERATIONS = 10
i = 1

def raymers(W_0, A, C, W_payload, W_F, i):
    for i in range(10):
        W_0 = W_payload / (1 - (W_F / W_0) - (A * W_0 ** C))
        
i = i + 1

print(raymers(W_0, A, C, W_payload, W_F, i))

attempt 5 
W_0 = 3.582
A = (0.86) # Constant
C = (-0.05) # Constant
W_Payload = (0.27557783) # Payload Weight
W_F = (0) # Weight Of Fuel
i = 1

for i in range(10):
WeW0 = A * W_0_Initial ** C
print(WeW0)

for i in range(10):
W0 = W_Payload / (1 - 0 - WeW0)
print(W0)

i = i + 1
