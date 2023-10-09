import predict
tle = """0 LEMUR 1
1 40044U 14033AL  15013.74135905  .00002013  00000-0  31503-3 0  6119
2 40044 097.9584 269.2923 0059425 258.2447 101.2095 14.72707190 30443"""
qth = (37.771034, 122.413815, 7)  # lat (N), long (W), alt (meters)
predict.observe(tle, qth) # optional time argument defaults to time.time()
# => {'altitude': 676.8782276657903,
#     'azimuth': 96.04762045174824,
#     'beta_angle': -27.92735429908726,
#     'decayed': 0,
#     'doppler': 1259.6041017128405,
#     'eci_obs_x': -2438.227652191655,
#     'eci_obs_y': -4420.154476060397,
#     'eci_obs_z': 3885.390601342013,
#     'eci_sun_x': 148633398.020844,
#     'eci_sun_y': -7451536.44122029,
#     'eci_sun_z': -3229999.50056359,
#     'eci_vx': 0.20076213530665032,
#     'eci_vy': -1.3282146055077213,
#     'eci_vz': 7.377067234096598,
#     'eci_x': 6045.827328897242,
#     'eci_y': -3540.5885778261277,
#     'eci_z': -825.4065096776636,
#     'eclipse_depth': -87.61858291647795,
#     'elevation': -43.711904591801726,
#     'epoch': 1521290038.347793,
#     'footprint': 5633.548906707907,
#     'geostationary': 0,
#     'has_aos': 1,
#     'latitude': -6.759563817939698,
#     'longitude': 326.1137007912563,
#     'name': '0 LEMUR 1',
#     'norad_id': 40044,
#     'orbit': 20532,
#     'orbital_model': 'SGP4',
#     'orbital_phase': 145.3256815318047,
#     'orbital_velocity': 26994.138671706416,
#     'slant_range': 9743.943478523843,
#     'sunlit': 1,
#     'visibility': 'D'
#    }

transit_start = 1680775200
transit_stop = 1681034400

p = predict.transits(tle, qth, transit_start, transit_stop)

print("Start of Transit\tTransit Duration (s)\tPeak Elevation")
for transit in p:
    print(f"{transit.start}\t{transit.duration()}\t{transit.peak()['elevation']}")

import itertools
from multiprocessing.pool import Pool
import time

import predict
import requests

# Define a function that returns arguments for all the transits() calls you want to make
def _transits_call_arguments():
    now = time.time()
    tle = requests.get('http://tle.spire.com/25544').text.rstrip()
    for latitude in range(-90, 91, 15):
        for longitude in range(-180, 181, 15):
            qth = (latitude, longitude, 0)
            yield {'tle': tle, 'qth': qth, 'ending_before': now+60*60*24*7}

# Define a function that calls the transit function on a set of arguments and does per-transit processing
def _transits_call_fx(kwargs):
    try:
        transits = list(predict.transits(**kwargs))
        return [t.above(10) for t in transits]
    except predict.PredictException:
        pass

# Map the transit() caller across all the arguments you want, then flatten results into a single list
pool = Pool(processes=10)
array_of_results = pool.map(_transits_call_fx, _transits_call_arguments())
flattened_results = list(itertools.chain.from_iterable(filter(None, array_of_results)))
transits = flattened_results