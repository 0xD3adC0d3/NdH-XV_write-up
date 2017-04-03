In python 2.X, the random is not really random.
Given a seed, you'll get the same numbers in the same order.
The algorithm uses the PID as a seed.
We need to brute force this seed to see wich one was used to generate the first combination.
The generate another combination based on this seed and win.

1. Get the 1st winning combination (on the web app)
2. Launch the exploit.py script with the first winning combination as an argument
3. It ouputs the next winning combination
4. Write it on the web site
5. Validate the chal
