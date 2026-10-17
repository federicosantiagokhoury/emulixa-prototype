# Emulixa - Scientific Formulation Intelligence

An early stage scientific software prototype exploring how historical formulation experiments can support data driven research and development.

Built with **Python, React and JavaScript**. Emulixa aims to help formulation scientists retrieve experimental records, analyse formulation properties and eventually use machine learning to inform future experiments.

## Current functionality

- Process and structure experimental formulation datasets using Python.
- Load formulation records into a React application.
- Filter formulations by whether stability testing was performed.
- Select individual formulations and inspect measured properties including turbidity and viscosity.

## Technology stack

- **Python:** Scientific data processing and dataset preparation.
- **React:** Interactive formulation browser.
- **JavaScript:** Frontend logic, filtering and state management.
- **Vite:** Frontend development environment.
- **JSON:** Structured experimental records.

## Development roadmap

- [x] Dataset ingestion and preprocessing
- [x] Basic formulation retrieval and filtering
- [x] Individual formulation inspection
- [ ] Formulation comparison interface
- [ ] Machine learning inference integration
- [ ] Experiment recommendation workflows
- [ ] Improved frontend architecture and visualisation

## Research background

Emulixa builds on my research interests in machine learning, computational chemistry and formulation science.
My first-author peer-reviewed research explored machine learning for predicting emulsion properties. The published research reported an R^2 of 0.93 and a mean absolute percentage error of 12.1% for its evaluated prediction task.
These results describe the published research, **not the performance of the current Emulixa prototype**.

## Dataset

The prototype uses the publicly available *Liquid Formulations Dataset* associated with the research publication *Accelerating Formulation Design via Machine Learning: Generating a High-throughput Shampoo Formulations Dataset*.
Source: https://springernature.figshare.com/articles/software/Liquid_Formulations_Dataset/25451878
The source dataset is distributed under CC0. The dataset is third-party research data and is distinct from my published emulsion machine learning research.

## Running locally

```bash
cd frontend
npm install
npm run dev
```
Open the local URL displayed by Vite.

## Project status

**Active development - October 2026**

This repository currently demonstrates data processing and frontend exploration. Predictive modelling and advanced descision support capabilities are planned and should not be interpreted as implemented product functionality.