# -*- coding: utf-8 -*-

# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b":None,
    "1d":None,
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
ID = "dxk5418"

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
wordy["1b"] = "Address 1 is for the local variable, and address 2 is for the dynamically allocated variable. Stack grows from higher to lower addresses, and heap grows from lower to higher addresses."

# (1.c) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 132000

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = "The stack's address limits is 0x15000, which its starting addresses and ending addresses are 0x7ffc43926000 and 0x7ffc4393b000. The heap's address limits is 0x21000, which its starting addresses and ending addresses are  0x019d2000 and 0x019f3000."

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = '''execve("", [""], [/* 68 vars */]) = 0:  Execute the program pointed to by first argument, the filename. And the second argument is an array of argument strings passed to the current program. The third argument is an array strings passed to the new program as environment. It returns nothing when success and here it returns zero. brk(0)                                  = 0xf0c000: change the program break to provide more memory to use. mmap(NULL, 299712, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fdec9c1c000: creates a new mapping in the virtual address space of the calling process. The length of the mapping is set to 299712. Fd is set to 3 and offset is 0. The kernel chooses the (page-aligned) address at which to create the mapping. The flags arguments indicate that the updates to the mapping are not visible to other processes mapping the same file, and are not carried through to the underlying file and the mapping is not backed by any file. access("", R_OK)      = -1 ENOENT (No such file or directory): Check if the file(/etc/ld.so.preload) can be accessed, and the second argument R_OK tests if the file exists and grants read, which returns that the first argument, pathname does not exist or is a dangling symbolic link. open("", O_RDONLY)      = 3: Open the file descriptor 3 for the caching the map from plain shared library names(pathname, first argument) with access mode to be read-only(second argument), which returns the file descriptor 3.fstat(3, {st_mode=S_IFREG|0755, st_size=1930416, ...}) = 0: obtain information about open file associated with file descriptor 3, and write it to the buffer which is second argument. REturn 0 to indicate success. close(3)                                = 0: it closes the file descriptor open by system call, open() and it takes the file descriptor as argument then close it. It returns the zero on success in this situation. read(3, "2"..., 832) = 832 :this system call reads up to 832 bytes from file descriptor 3 in to the buffer starting at second argument. It returns the bytes that is read, which is 832 bytes here.mprotect(0x32cad8b000, 2093056, PROT_NONE) = 0: changes the access protection of the memory starting from 0x32cad8b000 to (0x32cad8b000+2093956-1), the third argument is to set the access flag so that the memory in the range above cannot be accessed at all. Return 0 to indicate success.'''


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
numerical["2aii32"] = 14147584

# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = 1789952

# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["2ai64"] = 2183

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = 16252928

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = 3874816

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = '''Program received signal SIGSEGV, Segmentation fault.
0x00000000004005af in allocate (count=Cannot access memory at address 0x7fffff366f0c
) at prog2.c:5(with 64-bits compiled code)'''

# (2.c) Explain the cause of this error.
wordy["2c"] = "The function allocate is trying to access memory at address 0x7fffff366f0c, which is overflowed. Since there is no enough space for the int x[300000] to use when the allocate at the 11th recursion. The ending addresses of the limits of stack is 7fffff48b000(stack grows from higher to lower),and 0x7fffff366f0c is less than the ending address of the limits of stack."

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = "Observing the output of prog2, the size for each frame is 0xfffffed8bc0-0xfffffdb3c10 = 1200048 bytes(decimal). Using the ulimit -s, the total size of stack of the program assigned by system is 10240K bytes, 10240*1024/1200048 = 8.737 times. Based on the calculation, the program will run 8 times then causes the core dumped. Acutally, the total size of the stack is 12008472 bytes(decimal) using the pmap PID command to check the starting and ending addresses of the stack. After some basic calculation, we have 12008472/1200048 = 10.00749 times, which is the reason why the recursion only run 10 times and exit at 11th times.So the estimated invocations is 10.00749 times, and the program acctually run 10 time, stopping at 11th times."

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = "Generally, the contents inside the frame are local variable, the return address, argument variables passed on the stack, and saved copys of any registers. In the program, all of them are present in this program. The size for the local variable:int x[300000] is 1200000 bytes,a char pointerL 8 bytes ,regsiter address: rbp and rip, 8 bytes(64 bits system), 4 bytes(32 bits system),argument: count, 4 bytes,saved register: 8 bytes "

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
numerical["3aii32"] = 447676416

# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = 1961984

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = 2556

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] = 44518313984

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] = 6512640

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = "Address 0x0 is not stack'd, malloc'd or (recently) free'd. The problem here is that the heap is overflowed. Also, according to the statement here Invalid write of size 1 ==19750==    at 0x4A09AD8: mem(mc_replace_strmem.c:1011), the function mem set is trying to access the invaild memory address."

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = "Different from the problem in question 2, which is caused by stack overflow, the problem here is basically caused by heap overflow."

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = "According to the report by using the valgrind, it says that total heap usage: 1,009,999 allocs, 88,498 frees, 2,039,998,000 bytes allocated. After I check the check.c and prog4.c file, the allocated memory is not freed in the function allocate1 and allocate. Function allocate only free the memory when the i is prime number and function allocate1 number only free the memory when the i is odd number. I fix the problem by change the call of allocate to allocate2."

# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = "The user CPU time is 0.909861s."

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = "The system CPU time is 0.452931s. User CPU time is time spent on the processor when run the code or code in libraries. System CPU time is the time spent tunning code in the operting system kernel on the behalf of the program."

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = "1814676 bytes, and maximum resident set size is the part of memory occupied by a process that is held in amin memory(RAM)."

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = "0, kernel and operating system."

# (4.b.v) voluntary context switches
wordy["4bv"] = "3"

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = "141, voluntary context switches occurs when a thread blocks beacuse it requires a resource that is uavailable. An involuntary context switch occurs when a thread executes for the duration of thread's time , or thwn the system identifies a higher-priority thread to run."

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
