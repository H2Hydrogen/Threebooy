# 22.12
# GHydrogen.theebooy.python
# 1.0

from vpython import *

scene.forward = vector(0, -0.5, 1);
scene.width = 1280;
scene.height = 720;
scene.background = color.white;

G = 6.672e-11;

body_01 = sphere(pos=vector(2e11, 0, 2e11), radius=2e10, color=color.red,
               make_trail=True, interval=10, retain=50);
body_01.mass = 4.001e30  # 质量;
body_01.p = vector(0, 2e4, 0) * body1.mass  # 动量;

body_02 = sphere(pos=vector(-1.3e11, (3 ** 0.5) * 1e11, 0), radius=1e10, color=color.blue,
               make_trail=True, interval=10, retain=50);
body_02.mass = 2e30;
body_02.p = vector(-(3 ** 0.5) * 1e4, -1e4, -0.4e4) * body2.mass;

body_03 = sphere(pos=vector(-1e11, 3e11, -1e11), radius=3e10, color=color.yellow,
               make_trail=True, interval=10, retain=50);
body_03.mass = 6e30;
body_03.p = -body_01.p - body_02.p  # 保证动量;

dt = 1e4;

while True:
  
    rate(1000);

    r1 = body_02.pos - body_01.pos;
    F1 = G * body1.mass * body2.mass * r1.hat / mag2(r1);

    r2 = body_02.pos - body_03.pos;
    F2 = G * body2.mass * body3.mass * r2.hat / mag2(r2);

    r3 = body_01.pos - body_03.pos;
    F3 = G * body1.mass * body3.mass * r3.hat / mag2(r3);

    body_01.p = body_01.p + F1 * dt - F3 * dt;
    body_02.p = body_02.p - F1 * dt - F2 * dt;
    body_03.p = body_03.p + F2 * dt + F3 * dt;

    body_01.pos = body_01.pos + (body_01.p / body_01.mass) * dt;
    body_02.pos = body_02.pos + (body_02.p / body_02.mass) * dt;
    body_03.pos = body_03.pos + (body_03.p / body_03.mass) * dt;
