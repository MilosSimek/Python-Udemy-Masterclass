# import time

# print(time.gmtime(0))

# print(time.localtime())
# print(time.localtime(time.time()))

# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("Year", time_here[0], time_here.tm_year)
# print("Month", time_here[1], time_here.tm_mon)
# print("Day", time_here[2], time_here.tm_mday)

import time
#from time import time as my_timer
#from time import perf_counter as my_timer
#from time import monotonic as my_timer
# from time import process_time as my_timer
# import random

# input("Press enter to start")

# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press enter to stop")

# end_time = my_timer()

# print("Started at " + time.strftime("%X", time.localtime(start_time)))
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))

# print(f"Your reaction time was {end_time - start_time}")


print("time():\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))

