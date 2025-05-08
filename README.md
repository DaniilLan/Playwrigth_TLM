```
├───config
│ 
├───core
│   ├───db
│   │   └───models
│   │   
│   │   
│   └───utils
│    
├───page_objects
│   ├───locators
│   │  
│   ├───page
│   
│   
├───screenshot_tests
│   ├───expect_css_style
│   ├───expect_text
│   └───wait_visible_elements
├───tests
```

```
+---config
|   |   config.py
|   |   __init__.py
|   |
|
+---core
|   +---db
|   |   |   db.py
|   |   |
|   |   +---models
|   |   |   |   public.py
|   |   |   |
|   |   |
|   |
|   \---utils
|       |   api_client.py
|       |   data_generators.py
|       |   file_helpers.py
|       |
|
+---page_objects
|   |   base_page.py
|   |   __init__.py
|   |
|   +---locators
|   |   |   base_locators.py
|   |   |   __init__.py
|   |   |
|   |
|   +---page
|   |   |   all_measurements.py
|   |   |   auth.py
|   |   |   help.py
|   |   |   meeting.py
|   |   |   support.py
|   |   |   user.py
|   |   |   __init__.py
|   |   |
|   |
|
+---screenshot_tests
|   +---expect_css_style
|   |       expect_css_style_validation_error.png
|   |
|   +---expect_text
|   |       expect_text_validation_error.png
|   |
|   \---wait_visible_elements
|           wait_visible_elements_playwright_timeout.png
|
+---tests
|   |   test_all_measurements_page.py
|   |   test_auth_page.py
|   |   test_help_page.py
|   |   test_meeting_page.py
|   |   test_support_page.py
|   |   test_user_page.py

```
