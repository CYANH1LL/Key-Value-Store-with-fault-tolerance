#**********************
#*
#* Progam Name: MP1. Membership Protocol.
#*
#* Current file: submit.py
#* About this file: Submission python script.
#* 
#***********************


import hashlib
import random
import email
import email.message
import email.encoders
#import StringIO
import sys
import subprocess
import json
import os
import os.path
""""""""""""""""""""
anchoring_file = 'Application.cpp'

# Message displayed if compatibility hacks fail
compat_fail_msg = '\n\nERROR: Python 3 compatibility fix failed.\nPlease try running the script with the "python2" command instead of "python" or "python3".\n\n'
wrong_dir_msg = '\n\nERROR: Please run this script from the same directory where ' + anchoring_file + ' is.\n\n'

try:
  raw_input
except:
  # NameError
  try:
    raw_input = input
  except:
    raise Exception(compat_fail_msg)

# urllib2 hacks based on suggestions by Ed Schofield.
# Link: https://python-future.org/compatible_idioms.html?highlight=urllib2
try:
  # Python 2 versions
  from urlparse import urlparse
  from urllib import urlencode
  from urllib2 import urlopen, Request, HTTPError
except ImportError:
  # Python 3 versions
  try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
  except:
    raise Exception(compat_fail_msg)

if not os.path.isfile(anchoring_file):
  print(wrong_dir_msg)
  raise Exception(wrong_dir_msg)
else:
  print('Found file: ' + anchoring_file)

""""""""""""""""""""
class NullDevice:
  def write(self, s):
    pass

def submit():   
  print ('==\n== [sandbox] Submitting Solutions \n==')
  
  (login, password) = loginPrompt()
  if not login:
    print ('!! Submission Cancelled')
    return


  output = subprocess.Popen(['sh', 'run.sh', str(0)]).communicate()[0]
  submissions = [source(i) for i in range(4)]
  submitSolution(login, password, submissions)



# =========================== LOGIN HELPERS - NO NEED TO CONFIGURE THIS =======================================

def loginPrompt():
  """Prompt the user for login credentials. Returns a tuple (login, password)."""
  (login, password) = basicPrompt()
  return login, password


def basicPrompt():
  """Prompt the user for login credentials. Returns a tuple (login, password)."""
  login = raw_input('Login (Email address): ')
  password = raw_input('One-time Password (from the assignment page. This is NOT your own account\'s password): ')
  return login, password

def partPrompt():
  print ('Hello! These are the assignment parts that you can submit:')
  counter = 0
  for part in partFriendlyNames:
    counter += 1
    print (str(counter) + ') ' + partFriendlyNames[counter - 1])
  partIdx = int(raw_input('Please enter which part you want to submit (1-' + str(counter) + '): ')) - 1
  return (partIdx, partIds[partIdx])



def submit_url():
  """Returns the submission url."""
  return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"

def submitSolution(email_address, password, submissions):
  """Submits a solution to the server. Returns (result, string)."""
  values = { 
      "assignmentKey": akey,  \
      "submitterEmail": email_address, \
      "secret": password, \
      "parts": {
          partIds[0]: {
              "output": submissions[0]
          },
          partIds[1]: {
              "output": submissions[1]
          },
          partIds[2]: {
              "output": submissions[2]
          },
          partIds[3]: {
              "output": submissions[3]
          }
      }
    }
  url = submit_url()
  data = json.dumps(values).encode('utf-8')
  req = Request(url)
  req.add_header('Content-Type', 'application/json')
  req.add_header('Cache-Control', 'no-cache')
  response = urlopen(req, data)
  return

## This collects the source code (just for logging purposes) 
def source(partIdx):
  # open the file, get all lines
  f = open("dbg.%d.log" % partIdx)
  src = f.read() 
  f.close()
  return src
  
def cleanup():
    for i in range(4):
        try:
            os.remove("dbg.%s.log" % i)
        except:
            pass



akey = 'Lm64BvbLEeWEJw5JS44kjw'

# the "Identifier" you used when creating the part
partIds = ['PH3Q7', 'PIXym', 'mUKdC', 'peNB6']
# used to generate readable run-time information for students
partFriendlyNames = ['Create Test', 'Delete Test', 'Read Test', 'Update Test'] 
# source files to collect (just for our records)
submit()

cleanup()

