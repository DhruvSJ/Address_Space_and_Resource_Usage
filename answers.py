# -*- coding: utf-8 -*-

# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b": None,
    "1d": None,
    "1e": None,
    "2b": None,
    "2c": None,
    "2d": None,
    "2e": None,
    "3b": None,
    "3c": None,
    "4a": None,
    "4bi": None,
    "4bii": None,
    "4biii": None,
    "4biv": None,
    "4bv": None,
    "4bvi": None
}
numerical = {
    "1a": None,
    "1c": None,
    "2ai32": None,
    "2aii32": None,
    "2aiii32": None,
    "2ai64": None,
    "2aii64": None,
    "2aiii64": None,
    "3ai32": None,
    "3aii32": None,
    "3aiii32": None,
    "3ai64": None,
    "3aii64": None,
    "3aiii64": None,
}

###########################################################
# Answer Section
# You may edit the values of variables below
###########################################################

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = "dsj6"

###########################################################
# (1) Stack, heap, and system calls
###########################################################

# (1.a) What is the size of the proces stack when it is
#   waiting for user input?
#   Enter your answer in bytes.
numerical["1a"] = 84000

# (1.b) Which addresses are for the local variables and
#   which ones are for the dynamically allocated variables?
#   What are the directions in which the stack and the heap
#   grow on your system?
wordy["1b"] = "The stack addresses are address 1, the local variables. the heap addresses are address 2, the dynamically allocated variables. Statck has higher addresses comparecd to heap. We also notice stack grows downwards(decreases) heap grows upwards(increases)."

# (1.c) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 132000

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = "Stack has limits : 7ffffffea000-7ffffffff000 \n heap has limits: 00602000-00623000 "

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = """There are total 13 system calls 
1.execve(): it runa dn executes the program or given file
2.mmap: used to dynamically allocate variables to the heap in virtual address space \n
3.open: Returns a file descriptor and used to reference libraries  
4.access: checks whether the calling process can access the file pathname.
5.Fstat: returns the information about the file.
6.close: closes  a  file descriptor, so that it no longer refers to any file and may be reused, for open libraries.
7.read: Reads commands in executable.
8.mprotect: Make sure that memory accesses follow the rules and not cause violations while running.
9.munmap: creates a new mapping in the virtual address space. similar to mmap.
10.brk: sets the end of the data segment to the value specified by addr.
11.Arch_prct: Print machine architecture. dont know specfic to prog1.
12.exit_group(): Terminates the program and exits all threads.
13.write:allows you to communicate with other users.
"""

###########################################################
# (2) Debugging Refresher
###########################################################

# (2.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables

# (2.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["2ai32"] = 1691 

# (2.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["2aii32"] = """14147584 # 13816x1024 using PID and smaps we got the observed run time.  
"""
# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = """ 1789952, I just added all the library tags 
"""
# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["2ai64"] = 2183

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = """ 16252928 # 15872x1024 using PID and smaps we got the observed run time.  
"""

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = """ 3874816, I just added all the library tags 
"""

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = "Line 6 causes the error, where we allocte the memory "

# (2.c) Explain the cause of this error.
wordy["2c"] = "A segment fault occurs because we try to allocate more space in the stacks than we actually have." 

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = """We used info frame command on two consecutive frames, say 1 & 2, to get the size of the frames by subtracting size of 2 - size of 1 (0xff6d53a0 -0xff5b03f0). We get the size 0x12fb0 = 1200048.
Since intergers are 4 bytes and we allocate 300000 integers, the stack is 12009472 bytes big. 
Therefore, program runs 10 times before the segfault 
 """

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = """A frame has Local variables, temorary parameters, return address ,saved registers and frame pointers. The size is 1200000 bytes.   

"""

###########################################################
# (3) More debugging
###########################################################

# (3.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables:

# (3.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["3ai32"] = 1984

# (3.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["3aii32"] =""" 447676416 # 437184x1024  using PID and smaps we got the totals time.  
"""
# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = """1961984 using pid and smaps we got the observed run time.  
"""

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = 2556

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] =""" 4451831398 # 43474916x1024 using PID and smaps we got the observed run time.  
"""

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] =""" 6512640 I just added all the library tags 
"""

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = """ Error occurs in line 19 where (memset(ch,"*", sizeof(b[0]+i);)memset tries to fill the memory with bytes outside of the allocated space. Thus 
causing a segment fault.
"""

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = "prog2 is a stack overflow vs prog3 is heap overflow,causing a memory leak "

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = """ The main error is due to memory leak,large number of malloc() vs lesser free(). To solve this we use free each time with malloc """



# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = """"approximate range from 0.000865868 secs to 0.000928858 secs"""

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = """"approx range from 0.000434930secs to 0.000499924 secs. CPU time is time spent in system calls within the kernel, however User time is time for the whole library code, which is still running in  user space.
 """

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = """1814676000 bytes, its the portion of memory occupied by a process that is held in main memory (RAM) """

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = " zero sinals "

# (4.b.v) voluntary context switches
wordy["4bv"] = " 2 switches"

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = """ 142, it suspends an active thread, and switches control to a different thread
"""

###########################################################
# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
###########################################################
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error of answer %s (should be a string)" % key)
