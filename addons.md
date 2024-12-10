# Changes in pre-existing code

- An option in sidebar, to load the Google API key
    - Google API key is saved in .env file
    - If Google API key already there, no need to add API key, it will show API key loaded
    - If command is entered without API key, it will indicate the error
- File ReStructuring
    - Seprated necessary functions and also the things which are seprate are grouped
    - Grouped as src/ backend && functions && system ( system_prompt ) && UI
    - Structured the whole Krya project, including system prompt
    - A special Backend for the generated_output.py, you can .gitignore it if you don't want,
        like it won't be visible at github but will be visible in time of execution but will be in backend
    - Created a Docs folder, later update the documentation, architecture accordingly
- File Handling and File Linking
    - Seprated the system_prompt and the CSS file, make it look like more clean and structure
    - Linked the necessary file and also 
- Logo Issue fixed, do the naming properly it is getting conflit with the streamlit library


### Issues

- Test Cross platform, as the file system might not work
- Don't change the functions name or complete them they clash with the streamlit library files
- Make sure to include assests like inages or the pdf or flowchart in the assets folder
- Improve the Readme file