import subprocess
import logging
import time

start_time = time.time()
subprocess.run(['python', 'src/my_code.py'])
end_time = time.time()
elapsed_time = end_time - start_time

print("Execution time: {:.2f}".format(elapsed_time))