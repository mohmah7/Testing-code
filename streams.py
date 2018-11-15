import sys

while True:
  # output to stdout:
  print("Yet another iteration ...")
  try:
    reading from sys.stdin (stop with Ctrl-D):
    number = raw_input("Enter a number: ")
  except EOFError:
    print("\nciao")
    break
  else:
    number = int(number)
    if number == 0:
      print >> sys.stderr, "0 has no inverse"
    else:
      print("inverse of %d is %f" % (number, 1.0/number))
