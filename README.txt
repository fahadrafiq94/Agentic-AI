
Financial Agent with Phi Data
=============================

This repository contains a **Financial Agent** built using the **Phi Data** framework. The agent leverages AI capabilities to assist with financial tasks, such as answering queries, generating reports, and analyzing data.

Features
--------
- Seamless integration with Phi Data for AI-driven insights.
- Local environment setup for development and testing.
- Interactive playground for chatting with the Financial Agent.

Setup Instructions
------------------

1. Clone the Repository
------------------------
    git clone https://github.com/your-username/financial-agent-phi-data.git
    cd financial-agent-phi-data

2. Install Dependencies
------------------------
Install all required Python libraries listed in `requirements.txt`:
    pip install -r requirements.txt

3. Set API Keys
---------------
Create a `.env` file in the project directory and paste your API keys into it. For example:
    OPENAI_API_KEY=your_openai_api_key
    PHI_DATA_API_KEY=your_phi_data_api_key

Ensure your API keys are valid and have the necessary permissions.

4. Run the Playground
---------------------
Launch the Phi Data playground to interact with the Financial Agent:
    python playground.py

5. Access the Playground
------------------------
Open your browser and navigate to the following link to access the Phi Data playground:
    http://localhost:7777

Here, you can chat with the Financial Agent and explore its capabilities.

Usage
-----
- Use the Phi Data Playground to ask financial queries, generate insights, or test custom scenarios.
- The agent is pre-configured to handle financial datasets and provide meaningful outputs.

Repository Structure
--------------------
.
├── playground.py       # Main script to launch the Phi Data Playground
├── requirements.txt    # List of Python dependencies
├── .env.example        # Example file for API keys
├── README.md           # Documentation (this file)
├── src/                # Source code for the Financial Agent
│   ├── agent.py        # Financial Agent implementation
│   ├── utils.py        # Utility functions
│   └── config.py       # Configuration setup

Support
-------
If you encounter any issues or have questions, feel free to open an issue in this repository or contact the maintainers.

Happy coding! 😊
