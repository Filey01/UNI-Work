initial_Takeoff_Weight = (3.5825118) # Initial weight of the aircraft
A = 0.86 # A set constant
C = -0.05 # A set constant
payload_Weight = (0.27557783) # Payload weight
takeoff_Weight = initial_Takeoff_Weight

# Raymer's equation, iterated i times
for i in range(100):
  takeoff_weight = initial_Takeoff_Weight

  initial_Takeoff_Weight = payload_Weight / (1 - (A * takeoff_weight ** C))
    
  print(f"Iteration {i+1}: takeoff_weight = {takeoff_weight}")
