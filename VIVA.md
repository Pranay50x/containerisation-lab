# Containerisation Lab Viva Questions and Short Answers

## 1. Program 1 - hello.py
Q1. What does the program print?
A1. It prints "hello world" using Python's print() function.

Q2. Why is this program used as the first example?
A2. It is the simplest program to understand Python syntax and container execution.

Q3. What is the purpose of the Dockerfile here?
A3. It sets up a Python environment, copies the file into /app, and runs hello.py.

Q4. Why is WORKDIR /app used?
A4. It sets the default working directory inside the container.

---

## 2. Program 2 - Simple Calculator
Q1. What does the program do?
A1. It takes two numbers and performs add, subtract, multiply, or divide based on user choice.

Q2. Why do we use float(input())?
A2. So decimal numbers can also be entered.

Q3. What happens if the user chooses division and the second number is 0?
A3. The program prints "Cant divide by 0".

Q4. Why is elif used?
A4. It checks only one matching condition instead of evaluating all conditions.

Q5. What is the purpose of the menu?
A5. It allows the user to select the operation.

Q6. What is the limitation of this program?
A6. It supports only four operations and does not handle invalid numeric input robustly.

---

## 3. Program 3 - Time-Consuming Loop
Q1. What is the objective of this program?
A1. It keeps the CPU busy for about 30 seconds.

Q2. Why is time.time() used?
A2. To measure the elapsed time and stop the loop after 30 seconds.

Q3. What is the key logic in the program?
A3. It runs a nested loop continuously until the time difference reaches 30 seconds.

Q4. Is this a CPU-bound or I/O-bound task?
A4. It is CPU-bound because it performs repeated calculations.

Q5. Why is this useful in containerization labs?
A5. It helps demonstrate how containers handle long-running tasks and resource usage.

Q6. What is the output of the program?
A6. It prints "starting task ..." and then "Task done" after the loop ends.

---

## 4. Program 4 - Factorial using Recursion
Q1. What does the program do?
A1. It calculates the factorial of a number using recursion.

Q2. What is recursion?
A2. A function calling itself to solve a smaller version of the same problem.

Q3. What is the base case?
A3. If n is 0 or 1, it returns 1 and stops recursion.

Q4. Why is the base case necessary?
A4. Without it, the function would keep calling itself forever.

Q5. What is the recursive formula used?
A5. fact(n) = n * fact(n-1)

Q6. What is a limitation of this code?
A6. It fails for negative numbers unless handled separately.

---

## 5. Program 5 - CSV Student Marks
Q1. What is the program doing?
A1. It reads student marks from a CSV file and prints a bar chart-like output.

Q2. Why is csv.DictReader used?
A2. It allows reading the CSV as dictionary rows using column names like Name and Marks.

Q3. What does maxmarks represent?
A3. It stores the highest marks among all students, used to scale the bars.

Q4. Why are bars printed with "=" characters?
A4. To visually represent the relative marks of each student.

Q5. What is the purpose of student.csv?
A5. It stores the input data used by the program.

Q6. What is a CSV file?
A6. A Comma-Separated Values file used for tabular data.

Q7. How is the scale of the bar decided?
A7. It is calculated relative to the maximum marks value.

---

## 6. Program 6 - Display Environment Variables
Q1. What does this program do?
A1. It prints all environment variables and their values.

Q2. What is an environment variable?
A2. A variable stored in the operating system environment and available to processes.

Q3. Why is this useful in containers?
A3. It helps debug configuration, secrets, and runtime settings in a container.

Q4. Which Python module is used?
A4. The os module.

Q5. How is the variable list accessed?
A5. Through os.environ.items().

Q6. Why is this important for Docker labs?
A6. Docker containers often rely on environment variables for configuration.

---

## 7. Program 7 - Host Reachability check using ping
Q1. What does the program do?
A1. It checks whether a host is reachable using the ping command.

Q2. Why is os.system() used?
A2. To execute the shell command from Python.

Q3. What does ping -c 4 do?
A3. It sends four ICMP echo requests to check connectivity.

Q4. What is the meaning of the return code?
A4. If the code is 0, the host is reachable; otherwise it is not.

Q5. Why does the program use sys.argv?
A5. To read the hostname passed as a command-line argument.

Q6. What is the major issue with this program in Docker?
A6. Some minimal container images may not include ping or may restrict network access.

---

## 8. Program 8 - Prime Number Check
Q1. What does this program check?
A1. It checks whether a given number is prime.

Q2. What is a prime number?
A2. A number greater than 1 that has no divisors other than 1 and itself.

Q3. Why does the loop start from 2?
A3. Because 1 is not a prime factor, and checking from 2 is the standard logic.

Q4. Why is the else block attached to the for loop?
A4. It executes if no divisor is found, meaning the number is prime.

Q5. What happens for numbers less than or equal to 1?
A5. The program says the number is not prime.

Q6. What is the time complexity?
A6. It is O(n) in the simple version.

Q7. How can the algorithm be improved?
A7. Check divisors only up to sqrt(n) for better efficiency.

---

## 9. Program 9 - Missing/Unlisted Program
Q1. Why is this a possible viva question?
A1. Because the repository does not show a clear prg9 directory.

Q2. What should a student answer if asked about it?
A2. Mention that the program is missing or not visible in the repository and confirm whether it was intentionally omitted.

Q3. Why is checking missing files important in a lab?
A3. It helps verify completeness and consistency of the repository.

---

## 10. Program 10 - Bash Script Hello Demo
Q1. What does this shell script do?
A1. It prints a welcome message inside the container.

Q2. Why is #!/bin/bash used?
A2. It specifies that the script should be run using the Bash shell.

Q3. Why is chmod +x needed?
A3. It makes the script executable.

Q4. What is the purpose of the Dockerfile here?
A4. It uses Ubuntu as the base image, copies the script, sets execute permission, and runs it.

Q5. Why is this a good Docker example?
A5. It shows how a shell script can be executed inside a container.

Q6. What is the difference between bash hello.sh and ./hello.sh?
A6. bash hello.sh runs the script with Bash explicitly, while ./hello.sh requires execute permission and shebang.

---

## 11. Program 11 - Temperature Converter
Q1. What does the program do?
A1. It converts temperature between Celsius and Fahrenheit.

Q2. What is the Celsius-to-Fahrenheit formula?
A2. F = (C × 9/5) + 32

Q3. What is the correct Fahrenheit-to-Celsius formula?
A3. C = (F - 32) × 5/9

Q4. Why is the given second formula wrong?
A4. It incorrectly subtracts 32 after multiplying, which does not match the standard formula.

Q5. Why is Python 3 division important here?
A5. It uses true division, so 9/5 gives a floating-point result instead of integer truncation.

Q6. What is the purpose of the choice input?
A6. It lets the user select which conversion to perform.

Q7. What is a practical application of this program?
A7. It can be used in weather, engineering, or scientific calculations.

---

# Docker Viva Questions and Short Answers

## 1. What is Docker?
Docker is a platform used to build, package, and run applications inside lightweight containers.

## 2. What is an image?
An image is a read-only template used to create containers.

## 3. What is a container?
A container is a running instance of a Docker image.

## 4. What is a Dockerfile?
A Dockerfile is a text file that contains instructions to build a Docker image.

## 5. What is the purpose of FROM in a Dockerfile?
FROM specifies the base image from which the container is built.

## 6. What is WORKDIR?
WORKDIR sets the working directory inside the container.

## 7. What is COPY used for?
COPY copies files from the host machine into the container.

## 8. What is CMD?
CMD provides the default command executed when the container starts.

## 9. What is ENTRYPOINT?
ENTRYPOINT sets the main command that runs when the container starts.

## 10. What is the difference between CMD and ENTRYPOINT?
CMD is easier to override, while ENTRYPOINT is more fixed and commonly used as the main application command.

## 11. Why is Docker useful?
Docker makes applications portable, consistent, and easy to deploy across environments.

## 12. Why are containers lighter than virtual machines?
Containers share the host OS kernel, so they use fewer resources.

## 13. What is a base image?
A base image is the starting layer for a Docker image, such as Python or Ubuntu.

## 14. What is docker build?
It builds a Docker image from a Dockerfile.

## 15. What is docker run?
It creates and starts a container from an image.

## 16. What is docker ps?
It shows the currently running containers.

## 17. What is docker images?
It lists all Docker images available on the machine.

## 18. Why is docker rm used?
It removes a stopped or unused container.

## 19. What is the use of --rm?
It automatically removes the container when it exits.

## 20. Why are environment variables important in Docker?
They configure application behavior without changing the code.

## 21. What is the difference between a Docker image and a Docker container?
Image is the blueprint; container is the running instance.

## 22. What is the role of the container in application deployment?
It packages the application and its dependencies so it runs the same way everywhere.

## 23. Why is containerization better than traditional setup?
It reduces dependency conflicts and makes setup reproducible.

## 24. Why do some containers fail to run ping?
Some minimal images do not include networking tools or may block ICMP access.

## 25. What is the main benefit of Docker in labs?
Docker helps students test and run programs consistently and quickly in isolated environments.

---

# Very Important Short Viva Summary

- Python programs in this repo teach core concepts like loops, conditions, file handling, recursion, and system interaction.
- Docker files show basic container setup using Python and Ubuntu images.
- A good viva answer should explain the logic of each program, its purpose, and how Docker executes it.
- In Docker viva, always remember: image, container, Dockerfile, FROM, WORKDIR, COPY, RUN, CMD, and containerization benefits.

# Final Preparation Tip
For viva, focus on:
- What the program does
- Why the logic is written that way
- What each crucial statement means
- How Docker builds and runs the application
- Why containers are useful in software development and labs

