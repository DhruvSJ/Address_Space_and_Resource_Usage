# Address_Space_and_Resource_Usage
This assignment has three main goals. First, you will learn in concrete terms
what the different segments of a virtual address space (or simply address space) are. Second,
you will learn to use three Linux facilities - /proc, strace, and getrusage - to
record/measure certain aspects of process resource usage. Finally, we hope that Lab 1 will
serve to refresh your understanding of (or make you learn in case you lack it): (i) logging
into a Linux machine (ssh, VPN, 2FA) and using basic Linux shell and commands, (ii)
compiling a C program (gcc, make), creating/linking against libraries, (iii) debugging
(gdb), (iv) working with a code repository (github), (v) using Linux man pages (the man
command), and (vi) basic hexadecimal arithmetic.

#Description of Tasks

1. Stack, heap, and system calls: The executable named prog1 contains a function
that is recursively called 10 times. This function has a local variable and a dynamically
allocated variable. Upon each invocation, the function displays the addresses
of both these variables on the console. After 10 invocations, the program waits for a
key to be pressed on the keyboard before concluding. We would like you to observe
the addresses displayed by prog1 and answer the following:
(a) What is the size of the process stack when it is waiting for user input? (Hint:
Use the contents of /proc/PID/smaps that the /proc file system maintains
for this process where we are denoting its process ID by PID. While the program
waits for a user input, try running ps -ef | grep prog1. This will
give you PID. You can then look at the smaps entry for this process (cat
/proc/PID/smaps) to see a description of the current memory allocation to
each segment of the process address space.
