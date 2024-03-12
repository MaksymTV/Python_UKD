a = 5
b = 10

#Істина: and

(a > 0) and (b > 5)
(a != b) and (a % 2 == 0)

#Хибність: and

(a < 0) and (b > 15)
(a == b) and (a % 2 == 1)

#Істина: or

(a > 0) or (b > 5)
(a == b) or (a % 2 == 1)

#Хибність: or

(a < 0) or (b < 15)
(a != b) or (a % 2 == 0)