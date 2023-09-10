# KirbyOTD
Python script that generates a different copy ability of Kirby every day.

Run it with the files `pastkirbyotds.csv & kirbycopyabilities.txt` in the same folder.

It will generate a new kirby based on the date and previous generations. If it already generated a kirby for the day, it will reuse that one rather than produce a new one. It will also avoid repeats by looking at previous generations. Once it has generated all of the copy abilities, it will wipe the data from the record.
