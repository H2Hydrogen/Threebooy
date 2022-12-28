# 22.12
# GHydrogen.theebooy.python
# 1.0

from vpython import *

scene.forward = vector(0, -0.5, 1);
scene.width = 1280;
scene.height = 720;
scene.background = color.white;

G = 6.672e-11;

body1 = sphere(pos=vector(2e11, 0, 2e11), radius=2e10, color=color.red,
               make_trail=True, interval=10, retain=50);
body1.mass = 4.001e30  # 质量;
body1.p = vector(0, 2e4, 0) * body1.mass  # 动量;

body2 = sphere(pos=vector(-1.3e11, (3 ** 0.5) * 1e11, 0), radius=1e10, color=color.blue,
               make_trail=True, interval=10, retain=50);
body2.mass = 2e30;
body2.p = vector(-(3 ** 0.5) * 1e4, -1e4, -0.4e4) * body2.mass;

body3 = sphere(pos=vector(-1e11, 3e11, -1e11), radius=3e10, color=color.yellow,
               make_trail=True, interval=10, retain=50);
body3.mass = 6e30;
body3.p = -body1.p - body2.p  # 保证动量;

dt = 1e4;

while True:
  
    rate(1000);

    r1 = body2.pos - body1.pos;
    F1 = G * body1.mass * body2.mass * r1.hat / mag2(r1);

    r2 = body2.pos - body3.pos;
    F2 = G * body2.mass * body3.mass * r2.hat / mag2(r2);

    r3 = body1.pos - body3.pos;
    F3 = G * body1.mass * body3.mass * r3.hat / mag2(r3);

    body1.p = body1.p + F1 * dt - F3 * dt;
    body2.p = body2.p - F1 * dt - F2 * dt;
    body3.p = body3.p + F2 * dt + F3 * dt;

    body1.pos = body1.pos + (body1.p / body1.mass) * dt;
    body2.pos = body2.pos + (body2.p / body2.mass) * dt;
    body3.pos = body3.pos + (body3.p / body3.mass) * dt;
