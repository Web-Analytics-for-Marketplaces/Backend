Instructions
Copy the file named .env.example and rename it to .env.

Fill in the MONGO_USER and MONGO_PASSWORD variables in the .env file. You can leave the sample values from .env.example for testing.

Running with Docker
Build and start the containers:

bash
Копировать
Редактировать
docker-compose up -d --build
Open the frontend in your browser:
http://localhost

View the Swagger API documentation:
http://localhost:8000/docs

Access the MongoDB admin panel, logging in with username user and password 123:
http://localhost:8081

Storybook
From the project root, start Storybook:

bash
Копировать
Редактировать
cd frontend
pnpm sb
Open Storybook in your browser:
http://localhost:6006

Tests
Run unit and component tests in the terminal:

bash
Копировать
Редактировать
cd frontend
pnpm test
Run the test UI in the browser:

bash
Копировать
Редактировать
cd frontend
pnpm test:ui
Open the test report:
http://localhost:51204/__vitest__/#/

End-to-End (E2E) Tests
Run E2E tests in the terminal:

bash
Копировать
Редактировать
cd frontend
pnpm test:e2e
Run the E2E test UI in the browser:

bash
Копировать
Редактировать
cd frontend
pnpm test:e2e-ui
Playwright Commands
bash
Копировать
Редактировать
# Run all end-to-end tests
pnpm exec playwright test

# Start interactive test UI
pnpm exec playwright test --ui

# Run only on Chromium
pnpm exec playwright test --project=chromium

# Run tests in a specific file
pnpm exec playwright test path/to/file.spec.ts

# Debug tests
pnpm exec playwright test --debug

# Generate tests with Codegen
pnpm exec playwright codegen
Example Wildberries API Request
Endpoint:

bash
Копировать
Редактировать
POST https://app.marketspace.ru/testing-api/adv/v2/fullstats
Request Body:

json
Копировать
Редактировать
[
  { "id": 19447497, "dates": ["2024-10-08"] },
  { "id": 18854755, "dates": ["2024-10-08"] }
]
Requirements Document
Access the specification here:
https://docs.google.com/document/d/1IT78RNaJeabQUcPnHYBCZDoC12Xx-HvsWzWWYHOss8Q/

Key Terms

Advert: an advertising campaign

nm: a product (item)

Tasks

Build a NestJS + TypeScript API with MongoDB.

Integrate with the Wildberries stats API (use the testing proxy at https://app.marketspace.ru/testing-api/…).

Create a React + TypeScript frontend that sends requests and displays a table of nm items with their aggregated statistics, including filters matching the backend.

(Optional) Add Docker support, ESLint, additional utilities, validation, and Swagger documentation.

Behavior

The API must accept a request for a single advert ID and date, for example:

json
Копировать
Редактировать
{ "advert": 12, "date": "2024-09-09" }
It should first look up the data in MongoDB. If not found, it should fetch from Wildberries, store it in MongoDB, and then return it.

The response must include:

A summary object with total clicks, ctr, and cpc.

A list array of objects grouped by nmId, each with clicks, ctr, and cpc.

Sample Response:

json
Копировать
Редактировать
{
  "summary": { "clicks": 2, "ctr": 0.19, "cpc": 0.09 },
  "list": [
    { "nmId": 123, "clicks": 2, "ctr": 0.19, "cpc": 0.09 },
    { "nmId": 124, "clicks": 2, "ctr": 0.19, "cpc": 0.09 }
  ]
}
