# AI Powered Vehicle Valuation System

## Overview

An AI-powered used vehicle valuation platform that predicts resale value using Machine Learning and XGBoost.

## Features

- Vehicle Price Prediction
- FastAPI REST API
- Interactive Swagger Documentation
- Smart Brand/Model Search
- Server-backed Prediction History
- CSV export and printable report
- Health and metadata endpoints
- Professional Frontend
- AI-Based Estimation

## API Endpoints

- `POST /predict` — Get a new valuation
- `GET /brands` — List brands, optional `search` query
- `GET /models/{brand}` — List models for a brand, optional `search` query
- `GET /vehicle/{brand}/{model}` — Get variant and fuel/transmission details
- `GET /history` — Retrieve saved prediction history
- `DELETE /history` — Clear prediction history
- `GET /vehicles` — Search available vehicles
- `GET /metadata` — App metadata and dataset counts
- `GET /health` — Health check

## Tech Stack

- Python
- FastAPI
- XGBoost
- Scikit-learn
- Pandas
- HTML
- CSS
- JavaScript
- GitHub Codespaces

## Current Status

- Data Cleaning ✅
- EDA ✅
- Feature Engineering ✅
- Model Training ✅
- Model Evaluation ✅
- Backend API ✅
- Frontend Integration 🔄