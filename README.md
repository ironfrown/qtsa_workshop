# Workshop on Quantum Time Series Analysis
**Author:** [Jacob Cybulski](http://jacobcybulski.com/) ([ironfrown](https://github.com/ironfrown))<br/>
**Location:** Melbourne, Australia<br/>
**Date:** October 2022

Jacob Cybulski is an independent researcher in quantum computing, quantum machine learning, classical machine learning and data visualisation. He also holds the position of Honorary Associate Professor in Quantum Computing, in the School of IT at Deakin University, Melbourne, Australia.

***I am a researcher***, and so if you wanted to use this work for your own research, publish your derivative work, or use it for commercial purposes, please acknowledge the author's work and cite this material as follows:
- Jacob Cybulski. “Workshop on Quantum Time Series Analysis.” *Ironfrown GitHub repository*, Melbourne, Australia, 2022.<br/> https://github.com/ironfrown/qtsa_workshop.

The workshop material was presented in the following events:
- Jacob Cybulski, "Key Concepts in Quantum Time Series Analysis", *School of IT, SEBE, Deakin University*, Burwood, Australia, 29 Sept 2022.
- Jacob Cybulski, keynote "Time Series Analysis Using Quantum Machine Learning", *Workshop on Quantum Machine Learning*, organised in collaboration with QWorld, QPoland, QIndia and Quantum AI Foundation. In association with IEEE Conference Trends in Quantum Computing and Emerging Business Technologies - TQCEBT 2022, 13 October 2022.


This repository consists of examples used in the workshop on Quantum Time Series Analysis (QTSA).
- [Workshop aims and objectives](#aims-and-objectives)
- [Prerequsite knowledge](#prerequsite-knowledge)
- [Materials and notebooks](#materials-and-notebooks)
- [Workshop tasks](#workshop-tasks)
- [Installation instructions for IBMQ Labs](#installation-instructions-for-ibmq-labs)
- [Software compatibility](#software-compatibility)

## Aims and objectives
The workshop provides some introductory material and is delivered via online meetings (e.g. Zoom, Teams or Webex). The workshop is practical and sets the following aim:

> To provide the participants with knowledge and skills needed 
> to engineer a quantum solution to practical time series analysis problems

It specifically qualifies its objectives as:

> We will not seek to explore quantum advantage of QTSA solutions over classical ones but rather 
> aim to gain experience in quantum manipulation and modelling of time series data.

## Prerequsite knowledge
The workshop makes some assumptions as to the audience knowledge and skills, i.e.

- Knowledge of Python
- Basic skills in Qiskit
- Fundamentals of Quantum Computing
- Understanding of Variational Quantum Circuits
- Awareness of Quantum Neural Network techniques

## Materials and notebooks
The following files are publicly available:

- [utils.py](./utils.py) - Utility classes and functions
- [qtsa_00_utils_v1.0_demo.ipynb](./qtsa_00_utils_v1.0_demo.ipynb) - Tests of support functions
- [qtsa_01_linreg_v1.6_demo.ipynb](./qtsa_01_linreg_v1.6_demo.ipynb) - Demo of quantum linear regression
- [qtsa_02_serial_model_demo_v8.9.ipynb](./qtsa_02_serial_model_demo_v8.9.ipynb) - Demo of QTSA with serial Fourier transforms
- [qtsa_03_parallel_model_problem_v8.9.ipynb](./qtsa_03_parallel_model_problem_v8.9.ipynb) - Problem notebook for QTSA with parallel Fourier transforms
- [qtsa_04_qnn_v1.2_demo.ipynb](./qtsa_04_qnn_v1.2_demo.ipynb) - Demo of QTSA with sliding window and a standard QNN
- [qtsa_05_sliding_wind_problem_v9.0.ipynb](./qtsa_05_sliding_wind_problem_v9.0.ipynb) - Problem notebook for QTSA with serial custom QNN

The following files are not available, but given to the workshop participants (after the workshop):

- [qtsa_03_parallel_model_answer_v8.9.ipynb](other/qtsa_not_available.ipynb) - Sample solution for QTSA with parallel Fourier transforms
- [qtsa_05_sliding_wind_answer_v9.0.ipynb](other/qtsa_not_available.ipynb) - Sample solution for QTSA with serial custom QNN

## Workshop tasks
Typically the following tasks are undertaken by the workshop participants:

- **Easy:** Study serial quantum Fourier transform TS fit.
    - Test it with various data sets, factors and optimisers.
    - Analyse, compare and find the best combination.
- **Medium:** Implement a parallel quantum Fourier transform TS fit.
    - Test it with various data sets, factors and optimisers.
    - Analyse, compare and find the best combination.
- **Hard:** Implement a serial sliding window QNN TS forecaster.
    - Test it with various data sets, factors and optimisers.
    - Analyse, compare and find the best combination.
- **Challenge:** Modify the SSW QNN for multi-variate TS data.
    - Test it with various data sets, factors and optimisers.
    - Analyse, compare and find the best combination.

## Installation instructions for IBMQ Labs
Instructions on using this repository on IBM Quantum (IBMQ):

- Create an IBMQ account and login<br/>
   *URL: https://quantum-computing.ibm.com/*
- Access ironfrown code on GitHub (here):<br/>
   *URL: https://github.com/ironfrown/qtsa_workshop*
- Download workshop files from GitHub:<br/>
   *Either via *git* or from *GitHub* web site (Code > Download ZIP)*<br/>
   *Save it as "qtsa_workshop-main.zip" (includes the enclosing folder)* 
- On IBMQ select the Lab option (Top left menu > Lab)
- In the IBMQ Labs file system identify the directory for the contents of the archive
- Upload "qtsa_workshop-main.zip" file into this directory (Labs top left icons > Upload files)
- Open a Python Console (Labs top left icons > New file + > Console)
- Type a statement "!unzip qtsa_workshop-main.zip" (Shit-Enter)
- Refresh the contents of the directory (Labs top left icons > Refresh file list)
- The contents of the workshop repository is ready for use within IBMQ Lab

## Software compatibility
Workshop examples have been tested on the following system:

| Qiskit Software	| Version |
| --- | :---: |
| qiskit-terra	| 0.21.0 |
| qiskit-aer	| 0.10.4 |
| qiskit-ibmq-provider	| 0.19.2 |
| qiskit	| 0.37.0 |
| qiskit-nature	| 0.4.2 |
| qiskit-finance	| 0.3.3 |
| qiskit-optimization	| 0.4.0 |
| qiskit-machine-learning	| 0.4.0 |
| | |
| <b>System information</b> | | 
| Python version	| 3.8.13 |
| Python compiler	| GCC 7.5.0 |
| OS	| Linux |
| Memory (Gb)	| 62 |
