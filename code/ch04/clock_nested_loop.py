import time

# a 24 hour clock instead of 12 hour clock as shown in slides
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            # little trick, \r does carriage return only, no newline, so
            # end up at first column on same line, so clock appears to
            # update on same line real fast...
            print(f'{hours:02d}:{minutes:02d}:{seconds:02d}', end='\r')

            # haven't gotten to this in class yet, but put in a 1 second delay,
            # so acts like real clock, ctrl-c to interrupt
            time.sleep(1)
print()
