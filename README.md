---

# **Influencer Engagement and Sponsorship Coordination Platform**

## Overview
The **Influencer Engagement and Sponsorship Coordination Platform** is a web-based application that connects companies with influencers to manage marketing campaigns. Companies can create campaigns, review influencer applications, and process payments, while influencers can apply for campaigns, track their status, and mark them as complete.

The platform is built using **Flask** for backend logic, **Jinja2** templates for rendering HTML dynamically, **Bootstrap** for responsive UI, and **SQLite** for data storage.

---

## Features
### For Companies:
- **User Authentication**: Secure sign-up and login system.
- **Campaign Management**: Create, edit, and delete marketing campaigns.
- **Application Review**: Accept or reject applications from influencers.
- **Payment Processing**: Pay influencers upon campaign completion.

### For Influencers:
- **User Authentication**: Secure sign-up and login system.
- **Browse Campaigns**: View active campaigns and apply to them.
- **Track Applications**: Monitor the status of applications (pending, accepted, or rejected).
- **Mark Campaigns as Completed**: Mark campaigns as completed to initiate payment.

---

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: Jinja2, Bootstrap
- **Database**: SQLite
- **Templating Engine**: Jinja2
- **Styling**: Bootstrap for responsive design

---

## Installation

### Prerequisites
- Python 3.x
- Flask
- SQLite

### Clone the Repository
```bash
git clone https://github.com/yourusername/influencer-sponsorship-platform.git
cd influencer-sponsorship-platform
```

### Install Dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

### Database Setup
Initialize the SQLite database:
```bash
flask db init
flask db migrate
flask db upgrade
```

### Running the Application
To start the application, run the following command:
```bash
flask run
```

The app will be accessible at **http://127.0.0.1:5000/**.

---

## Usage

### User Authentication
- **Company Sign-Up**: Companies can create an account to manage campaigns.
- **Influencer Sign-Up**: Influencers can register to view and apply for campaigns.

### Campaign Management
- **Company Dashboard**: Companies can create new campaigns, edit existing ones, or delete them.
- **Influencer Dashboard**: Influencers can browse available campaigns and apply to the ones they are interested in.

### Application Workflow
- **Influencer Application**: Once applied, influencers can track the status of their applications.
- **Company Review**: Companies can accept or reject influencer applications.
- **Completion and Payment**: Once an influencer marks a campaign as completed, the company can process the payment for the agreed-upon amount.

---

## Project Structure

```
.
├── app/                   # Main application folder
│   ├── templates/         # HTML templates using Jinja2
│   ├── static/            # Static files (CSS, JS)
│   ├── models.py          # Database models (User, Campaign, Application)
│   ├── routes.py          # Flask routes and view logic
│   └── __init__.py        # Application factory
├── migrations/            # Database migrations folder
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── run.py                 # Entry point for running the app
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m "Add some feature"`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

---

## Future Enhancements
- **Advanced Analytics**: Adding campaign performance metrics.
- **Automated Payments**: Integration with payment gateways like PayPal or Stripe.
- **Improved User Profiles**: Additional features for influencers to showcase their portfolio.

---

## Contact
If you have any questions or issues, feel free to reach out at [parabgargeya@gmail.com].

---
