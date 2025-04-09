<!--
DESCRIPTION: Learn about assembly language - the human-readable programming language that maps directly to machine code, and why understanding it remains valuable for modern programmers.
-->

[TOC]

# Overview

Machine code is a string of bytes that a CPU runs. All other programming languages are "compiled" into machine code before it is run on a specific machine. All programming languages that run on a computer must ultimately be rendered into machine code before the computer can execute it. This happens automatically behind the scenes so most people are unaware that it happens. But it must happen. If it is possible to do something with a computer, then it is equally possible to do it with machine code. There is nothing that another language can do that machine code cannot do, but the reverse is not always true.

There have been much evolution in this strategy in recent decades. Generally:

* You write code in some high-level language, like C#
* It gets compiled into "intermediate language" ("IL") and that is what you ship to your customers.
* When they run that IL code, their machine quickly compiles (Just In Time or "JIT") it into whatever machine they are running; e.g. x86, ARM, 68000.

**Assembly language** is a human readable programming language that maps one-for-one with a specific CPU's machine code.

Most programmers do not write in assembly language today. The high-level compilers, like C, C++, and Rust are so good that they often created faster, smaller machine code than the programmers can do with assembly language. And assembly language is an attractor to bugs.

Still, this page is a discussion of this subject because there are still good reasons to understand how this works:

* **Understanding Computer Architecture**: Assembly language provides a deep understanding of the computer architecture. It helps you understand how the processor and memory work.
* **Optimization**: Assembly language allows for direct hardware manipulation, access to specialized processor instructions, and can result in more efficient code execution. It's the gateway to optimization in speed, offering great efficiency and performance.
* **Hardware Interaction**: Assembly language allows for direct hardware interaction. This is particularly useful in areas where hardware interaction and high performance are paramount, such as in embedded systems, real-time systems, and device drivers.
* **Reverse Engineering**: Knowledge of assembly language is crucial for reverse engineering because it provides a low-level view of the code.
* **Learning Other Languages**: Understanding assembly can make learning other programming languages easier as it provides a solid foundation of how computers work.


# Details

For a general example of machine code, see the [COSMAC ELF](/pages/Cosmac Elf.md) page, where you program the computer by flipping toggle switches to enter the machine code bytes.


# References

Books:

* [Raspberry Pi Assembly Language RASPBIAN Beginners: Hands On Guide](https://www.amazon.com/Raspberry-Assembly-Language-RASPBIAN-Beginners/dp/1492135283)
* [Assembly Language Step-by-Step: Programming with DOS and Linux (Wiley computer publishing) by Jeff Duntemann (2000-06-26)](https://www.amazon.com/Assembly-Language-Step-Step-Programming/dp/B019TM7PES) - Jeff actually came to our wedding and is the reason I met my wife. He's a great writer.
* [The Art of 64-Bit Assembly, Volume 1: x86-64 Machine Organization and Programming](https://www.amazon.com/Art-64-Bit-Assembly-Language/dp/1718501080)
8 [Online Books on the subject](https://gitconnected.com/learn/assembly-language)

Sites:

* [CPU Visual Simulator](https://cpuvisualsimulator.github.io/)
* [8085 CPU Simulator and Visualizer](https://www.sim8085.com/)
* [The Visual 6502 ](http://www.visual6502.org/JSSim/index.html) - shows circuit lines as they connect when running the code.
* [MIPS Simulator](https://visualmips.github.io/)
* [One Compiler](https://onecompiler.com/assembly)
* [Code Academy - Introduction to Assembly Languages](https://www.codecademy.com/learn/computer-architecture-assembly-language)
* [Maria.js](https://marie.js.org/?addition) - another in-browser simulator
* [Intel 4004 Microprocessor Emulator](http://e4004.szyc.org/)
  * [Video to describe the 4004 emulator](https://www.youtube.com/watch?v=1JJbZ5kIBFE)

Videos:

* [Assembly Language in 100 Seconds](https://www.youtube.com/watch?v=4gwYkEK0gOk)
* [You Can Learn Assembly in 10 Minutes (it’s easy)](https://www.youtube.com/watch?v=jPDiaZS-2ok)
* [MIT OpenCourseWare - Assembly Language & Computer Architecture](https://www.youtube.com/watch?v=L1ung0wil9Y)
* [MIT OpenCourseWare - C to Assembly](https://www.youtube.com/watch?v=wt7a5BOztuM) - How C code gets translated via LLVM into machine code.

Courses:

* [Online Courses](https://www.classcentral.com/report/best-assembly-courses/)