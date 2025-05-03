# Marketplace Backend

A Django-based backend for an e-commerce marketplace with multiple microservices including inventory management, analytics, advertising, barcode generation, and reporting.

## Features

- **Inventory Management**: Product and stock tracking
- **Analytics**: Sales tracking and analysis
- **Advertising**: Campaign management and ad metrics
- **Barcode Generator**: Product barcode generation and storage
- **Reporting**: Asynchronous report generation with Celery

## Requirements

- Python 3.9+
- PostgreSQL
- Redis (for Celery)

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure your environment variables
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## API Endpoints

- **Inventory**: `/api/inventory/`
  - Products: `/api/inventory/products/`
  - Stock: `/api/inventory/stocks/`
- **Analytics**: `/api/analytics/`
  - Sales: `/api/analytics/sales/`
- **Advertising**: `/api/ads/`
  - Campaigns: `/api/ads/campaigns/`
  - Metrics: `/api/ads/metrics/`
- **Barcode Generator**: `/api/barcode/`
  - Barcodes: `/api/barcode/barcodes/`
- **Reporting**: `/api/reporting/`
  - Reports: `/api/reporting/reports/`

## Running Celery

Start the Celery worker:
```
celery -A marketplace_backend worker -l info
```

## Admin Interface

Access the Django admin interface at `/admin/` to manage all data.