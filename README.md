```
│
├── config 
│   └── config.py
│
├── core
│   ├── db
│   │   ├── db.py
│   │   └── models
│   │       └── public.py
│   │
│   └── utils
│       ├── api_client.py
│       ├── data_generators.py
│       └── file_helpers.py
│
├── page_objects
│   ├── base_page.py
│   ├── locators
│   │   └── base_locators.py
│   │
│   └── page
│       └── auth.py
│
├── screenshot_tests
│   ├── expect_css_style
│   │   └── expect_css_style_validation_error.png
│   ├── expect_text
│   │   └── expect_text_validation_error.png
│   └── wait_visible_elements
│       └── wait_visible_elements_playwright_timeout.png
│
└── tests
    └── test_auth_page.py
```
