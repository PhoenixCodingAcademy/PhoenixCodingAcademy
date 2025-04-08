# Sentinel Tower Gaming Desktop 360mm Liquid Cooled PC
* 24-Core Intel Ultra 9 285K - 8 Cores, 8 Threads, 3.7 GHz Base, 5.7 GHz Turbo [Passmark 67979](https://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+Ultra+9+285K&id=6296)
* 192GB DDR5 RAM
* 4TB Gen4 NVMe SSD
* 10TB HDD
* NVD GeForce RTX 5090 32GB
* WiFi 7
* Windows 11 Pro

[Amazon $6849](https://www.amazon.com/Sentinel-Desktop-Liquid-Cooled-PC/dp/B0DY87J55D)

You can always drop features to lower the price, but this looks pretty good. Comparable to what I use at home.

# Reasons

This Sentinel Tower Gaming Desktop presents an excellent choice for a classroom server dedicated to teaching students about AI LLMs and running an Ollama server. Here's a breakdown of why its specifications make it well-suited for this purpose:

1. Powerful Processor (Intel Ultra 9 285K):

* High Core and Thread Count: The 24 cores and 32 threads provide significant parallel processing capabilities. This is crucial for running multiple instances of LLMs simultaneously (if needed for demonstrations or individual student work) and for handling the computational demands of serving requests from multiple students.
* High Clock Speeds: The base clock of 3.7 GHz and turbo boost up to 5.7 GHz ensure that individual tasks and inferences are processed quickly, leading to a more responsive experience for the students.
* Strong Passmark Score: The impressive Passmark score of 67979 indicates top-tier performance, capable of handling demanding AI workloads.

2. Massive Amount of RAM (192GB DDR5):

* Handling Large Models: LLMs can be very memory-intensive. 192GB of high-speed DDR5 RAM allows the server to load and run even large language models efficiently without constantly swapping data to the slower SSD, which would significantly impact performance.
* Supporting Multiple Users: With a large amount of RAM, the server can comfortably handle requests from multiple students concurrently, each potentially interacting with different models or running their own experiments.
* Faster Training (Potentially): While the primary focus is teaching and running pre-trained models, if there's any exploration of fine-tuning or simpler training tasks, ample RAM is essential.

3. Fast and Large Storage (4TB Gen4 NVMe SSD + 10TB HDD):

* Fast Model Loading and Data Access (SSD): The 4TB Gen4 NVMe SSD offers incredibly fast read and write speeds. This will drastically reduce the time it takes to load LLM models into memory and access datasets, leading to a smoother and more productive learning environment.  
* Ample Storage for Models and Datasets (SSD + HDD): The combined 14TB of storage provides plenty of space to store various pre-trained LLMs, datasets for experimentation, student projects, and the Ollama server software itself. The larger, but slower, HDD can be used for less frequently accessed data or backups.

4. Powerful Dedicated GPU (NVIDIA GeForce RTX 5090 32GB):

* GPU Acceleration for LLM Inference and Training: NVIDIA GPUs are widely used for accelerating AI tasks, particularly LLM inference (generating text) and training. The RTX 5090 with 32GB of * VRAM offers substantial computational power for these operations. This can significantly speed up the response times of the LLMs for the students and potentially allow for demonstrations of fine-tuning or other GPU-intensive tasks.  
* CUDA and cuDNN Support: NVIDIA GPUs have excellent support for CUDA and cuDNN, which are essential libraries for accelerating deep learning workloads. Ollama and many other AI tools are optimized to leverage these technologies.  

5. High-Speed Networking (WiFi 7):

* Fast and Reliable Connections: WiFi 7 offers significantly faster speeds and lower latency compared to previous Wi-Fi standards. This ensures smooth and responsive connections for all the student workstations accessing the Ollama server, even with multiple concurrent users. While a wired connection (Ethernet) might be even more stable, WiFi 7 provides excellent wireless performance if wired infrastructure is limited.  

6. Professional Operating System (Windows 11 Pro):

* Robust and Feature-Rich: Windows 11 Pro offers features like enhanced security, virtualization capabilities (if needed for more advanced setups), and remote desktop access, which can be beneficial for managing the server and assisting students.  
* Broad Software Compatibility: Windows has a wide range of software compatibility, making it easier to install and manage various tools and libraries that might be needed for the AI curriculum.

# Classroom

Administrator
* Installs Ollama Server, pulls various models to try (`ollama pull ...`), and starts the server (`ollama serve`)

Student
* Installs on its machine:
  * Ollama Client
  * `uv` to run various Python virtual environments.
  * Git for Windows
  * AnythingLLM
  * Visual Code
  * Cursor

Teacher
* Walks the students through using this software and what can be done with it.


