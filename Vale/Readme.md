# Failure Prediction in PT VALE Indonesia

## Development Status

Still in very early works.

## Directories Descriptions

Here brief directories descriptions (in alphabetic order):
- [DataGUI](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/DataGUI): A GUI Prototype. The developement generally has been stopped
- [Docs](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/Docs): General Documentation. Updated as the project is on going.
- [Forecasting_Classifier_NN](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/Forecasting_Classifier_NN): Early work of Neural Network implementation. Maybe updated as the project is on going.
- [PIWebAPI_PISDK](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/PIWebAPI_PISDK): Testing and Notes about connecting to PI-System. It will be integrated to main project directory.
- [PredictPIServer](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/PredictPIServer): **Main Implementation project**. First Priority as the development on going.
- [TestOlahPy](https://github.com/mekatronik-achmadi/Predict-CBM/tree/main/Vale/TestOlahPy): Testing and Notes about Data Analysis. It will be integrated to main project directory.

## Documentation

Here main documentation:

- [Deployment](https://github.com/mekatronik-achmadi/Predict-CBM/blob/main/Vale/PredictPIServer/deployment.md)
- [Framework API](https://github.com/mekatronik-achmadi/Predict-CBM/blob/main/Vale/PredictPIServer/python_api.md)
- [Server Access](https://github.com/mekatronik-achmadi/Predict-CBM/blob/main/Vale/PredictPIServer/server_access.md)

## Requirement Breakdown

The development has three large part:
- [Source Tree Management](#source-tree-management)
- [PI System Intergration](#pi-system-intergration)
- [Data Analysis and Prediction](#data-analysis-and-prediction)

**NOTES:** Git/Github Pull Request also can be arranged at cost the repository being public.

### Source Tree Management

Task List:
- [x] Markdown Documentation
    - [ ] Deployment
    - [ ] Framework API
- [ ] In-Code Doxygen Documentation
- [ ] Python Class/Framework
    - [x] Integrate PI System
        - [x] Local PIWebAPI
        - [ ] AVD PIWebAPI
    - [ ] Integrate Data Analysis
        - [ ] GUI Plotter/Viewer
    - [ ] Packaging/Deployment
        - [ ] Windows requirements
        - [ ] Self Contained Image
        - [ ] Self Extraction (NSIS)
        - [ ] Other Options
- [x] Main Repository Maintainer

Maintainer: Achmadi, ST MT

### PI System Intergration

Task List:
- [ ] Testing API Connector/Interop
    - [x] PI-SDK Via Python
        - [x] Insert Pre-Given Data
    - [x] Web/REST API
        - [x] API Search Query
        - [x] Read/Write Attribute
        - [x] Read/Write PI Point
    - [ ] Wrapping Up
- [ ] API Listing
- [ ] Reading/Streaming
    - [x] Testing Reading / Writing
    - [ ] Real-time Streaming
    - [ ] Large Buffering

Maintainer: Apriyanto Dwi Prasetyo, ST

### Data Analysis and Prediction

Task List:
- [ ] Variable Identification
    - [ ] Listing/Collecting
    - [ ] Classification
- [ ] Modeling
    - [ ] Variable Based
    - [ ] Generic Statistics
    - [ ] Generic Neural Network
    - [ ] Other Options
- [x] Orbital Analysis

Additional Task:
- [x] PDF/LaTeX Documentation

Maintainer: Muhammad Ammar Assyraf, ST MT

## Document URL

### Discord Storage
