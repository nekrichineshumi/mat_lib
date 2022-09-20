from trigonometry import sin
import math
pi = math.pi
print(&#39;pi:&#39;, pi)
for alpha in [0, pi, pi/2, pi/3, pi/4, pi/6]:
    print(f&#39;For angle: {0 if alpha == 0 else &quot;pi/&quot;+str(int(pi/alpha))}, Sine 
is ~ {sin(alpha)}&#39;)