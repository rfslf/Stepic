x = input().split(' ')
if x[1] == 'mile': y = 1609*float(x[0])
if x[1] == 'yard': y = 0.9144*float(x[0])
if x[1] == 'foot': y = 0.3048*float(x[0])
if x[1] == 'inch': y = 0.0254*float(x[0])
if x[1] == 'km': y = 1000*float(x[0])
if x[1] == 'm': y = float(x[0])
if x[1] == 'cm': y = 0.01*float(x[0])
if x[1] == 'mm': y = 0.001*float(x[0])
if x[3] == 'mile': z = y/1609
if x[3] == 'yard': z = y/0.9144
if x[3] == 'foot': z = y/0.3048
if x[3] == 'inch': z = y/0.0254
if x[3] == 'km': z = y/1000
if x[3] == 'm': z = y
if x[3] == 'cm': z = y/0.01
if x[3] == 'mm': z = y/0.001
print('%.2e' % z)