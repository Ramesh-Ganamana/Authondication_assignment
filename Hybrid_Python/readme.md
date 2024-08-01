


This is the framework structure 

Hybrid_Python/
├── Configurations/
│ └── config.ini
├── pageObjects/
│ ├── init.py
│ └── item_page.py
├── Reports/
│ ├── Reports.html
│ └── assets/
│ └── style.css
├── testCases/
│ ├── init.py
│ ├── conftest.py
│ ├── test_item.py
│ ├── test_response.py
│ └── reports/
│ ├── Reports.html
│ └── assets/
│ └── style.css
├── utilities/
│ ├── init.py
│ ├── API.py
│ ├── customLogger.py
│ └── readProperties.py
├── demo.py
├── pytest.ini
├── readme.md
└── requirements.txt


1. Open Terminal or Command Prompt : open command prompt or terminal and navigate to project directory.

2. Activate Virtual Environment : Activate Virtual environment in automation project directory.

3. Install All dependencies : Install all dependencies using pip install command
    ````     
   pip install selenium
   pip install pytest 
   pip install webdriver-manager
   pip install pytest-html

   ````
### Run Test cases  :- 
Open the command prompt and run pytest to run specific test cases.
```
    pytest path/to/your/test_file.py
    
```

Tor UI "After clicking on proceed to pay in  website, it prompts for a login. As I'm unable to provide personal information here, I am concluding this session."
I used pytest html reports 
For api I just gust did get call and post call 
I make the code as reusable code. we can do DB testing like api we just need to create another file. 
This is the  framework I developed. 
I can make Mobile automation framework also.  




