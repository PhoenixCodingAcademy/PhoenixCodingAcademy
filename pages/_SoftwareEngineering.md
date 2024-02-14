[TOC]

<!--
DESCRIPTION: General overview of Software Engineering principles and rules of thumb.
-->

# Overview

# Rules

* The faster you can change a line of code, compile, debug (set breakpoints, run, step into) the code and regression test it, the faster it will evolve to a great product.

* Decouple your application from the system.
  * REASON: Your application ("You") will likely be part of an evolving system, where you depend on modules ("Them") outside your control, such as operating systems, APIs, and databases. These are black box services. You won't have access to that code. You cannot see or change that code. It can change and break your application without warning. It will likely be non-deterministic and unpredictable, where APIs have breaking contracts, records get deleted, scheduled things expire, time elapses, geo-coordinates change, bugs creep in, behaviors do not match documentation (if any exist),
  * HOW: Their modules will do lots of things you don't care about. But it will do a few things that you do care about, e.g. calling one of their many APIs. How you use a subset of their modules is called a "contract". It contains details about where to connect, authentication, payloads in, parameters, payloads returned, and error codes.

# Details

##
Any application (no matter how big)

# References

* [Development slowness in big and legacy applications](_template.md)
  * One of the most damaging things for productivity is not being able to run the stack locally. This generally happens due to laziness and corner cutting.