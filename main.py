from app.extractor.automation_extract import Extract_data_gov

def testing_login():
    Extract_data_gov().run()

if __name__ == '__main__':
    testing_login().run()
