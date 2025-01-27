# import logging
# logging.basicConfig(level= 50)
# logging.debug("This is debug message")
# logging.info("module 2 got completed and module 3 started")
# logging.warning("The warning message is displaying")
# logging.error("The error message is displaying")
# logging.critical("The critical message is didplaying")

#Logging of all the levels
#importing module
# import logging

# # Create and configure logger
# logging.basicConfig(filename="newfile.txt",
#                     format='%(name)s %(levelname)s:%(message)s:%(process)s:%(lineno)s',
#                     filemode='w')

# # Creating an object
# logger = logging.getLogger()

# # Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

# # Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")

# Configuring logging
# import logging
# import logging.config

# logging.config.fileConfig('newfile.conf')

# # create logger
# logger = logging.getLogger('simpleExample')

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

#Python logging exception
import logging
logging.basicConfig(level = logging.DEBUG, filename = "newfile.log", filemode = 'w')
try:
    ag = int(input("Enter your age:"))
except Exception as obj:
    logging.error(str(obj))

#Pickling used to transfer python objects from one server to another server and vice a versa
import pickle
data = ['Ruchika', 64.2, 82]
#pickling
byte = pickle.dumps(data)
print(byte)

#unpickling
data1 = pickle.loads(byte)
print(data1)