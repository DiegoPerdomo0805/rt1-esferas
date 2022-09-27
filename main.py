from ray import RayTracer

r = RayTracer(500, 500)
r.dense = 0.1
r.render()