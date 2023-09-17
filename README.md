# Cross-Platform File Sharing Application

## Overview

This is a cross-platform file-sharing application developed in Python. It provides a simple and efficient way to share files across different platforms. The application works smoothly for most file sizes; however, it encounters issues when handling large files that exceed available RAM.

## Issue: Memory Consumption

The primary challenge with this application is its memory consumption when dealing with very large files. When a file is selected for transfer, it is converted into a byte stream and temporarily stored in memory (RAM) before being segmented into smaller packets for network transfer. This process can lead to excessive memory usage, particularly when dealing with files larger than the available RAM.

## Proposed Solution

We are actively seeking innovative solutions to optimize memory management during file transfers. Our goal is to make the application more memory-efficient while maintaining its excellent CPU performance.

## How to Contribute

If you're interested in contributing to this project and helping us address the memory consumption issue, here's how you can get started:

1. **Fork the Repository**: Click the "Fork" button at the top right of this repository to create your copy.

2. **Clone the Repository**: Clone your forked repository to your local machine using the following command: git clone https://github.com/Hurley2017/Socket_Streaming

3. **Set Up Environment**: Ensure you have Python installed on your system. You may also need to install any project-specific dependencies mentioned in the code.

4. **Explore the Code**: Familiarize yourself with the project's codebase, especially the parts related to memory management during file transfers.

5. **Contribute**: Work on solutions or improvements related to memory optimization. You can submit pull requests with your changes.

6. **Testing**: Test your changes thoroughly to ensure they don't introduce new issues.

7. **Submit a Pull Request**: Create a pull request to propose your changes. Be sure to include a detailed description of your solution and how it improves memory usage.

## Contact

If you have any questions or suggestions regarding this project, feel free to reach out by [creating an issue](https://github.com/Hurley2017/Socket_Streaming/issues) or contacting the project owner directly.

## For you

We appreciate your interest and contributions to this project!

