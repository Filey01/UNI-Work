#Define all variables, i.e replace non numerical values

guess_w0= 100
we= 3.31
wp= 20
w0=guess_w0

we_w0= 0.86*guess_w0**-0.05

for i in range(100):
	w0 = wp/(1 - w0*we_w0)
	
	print(f"Iteration {i+1}: w0 = {w0}")