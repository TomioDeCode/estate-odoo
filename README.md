Estate Module

Version: 1.0
Author: TomioDeCode
Category: App
Odoo Version: 17.0
Description

The Estate module is designed to provide a simple application for managing estate properties, property types, property offers, and property tags. This module is created as a learning exercise to demonstrate the basic concepts of Odoo 17 module development.
Features

    Manage estate properties.
    Manage property types.
    Manage property offers.
    Manage property tags.
    Basic workflows for property offers and statuses.
    Simple email notification templates for property-related events.
    Schedulers for periodic tasks related to property management.

Installation

    Clone the Module: Place the estate directory in your Odoo custom addons directory.

    bash

git clone <repository-url> /path/to/odoo/custom/addons/estate

Update the Odoo Configuration: Make sure your Odoo configuration file (odoo.conf) includes the path to your custom addons directory:

plaintext

    addons_path = /path/to/odoo/addons,/path/to/odoo/custom/addons

    Install the Module: Restart the Odoo server and go to the Apps menu. Click on the "Update Apps List" button. Search for Estate and install it.

Usage

    Properties: Go to the Estate app and start by creating new properties. Fill in the details such as name, description, location, and price.

    Property Types: Define different property types (e.g., apartment, house, villa) using the Property Types menu.

    Property Offers: Manage offers for properties. You can accept or refuse offers, and track the status of each offer.

    Property Tags: Create and assign tags to properties for better categorization and searching.

    Email Notifications: The module includes a sample email template for notifications related to property events.

Dependencies

    base
    mail

Make sure these modules are installed and available in your Odoo environment.
Security

The module includes a security file (ir.model.access.csv) to define access rights and roles for different user groups. Review and customize these settings based on your requirements.
Scheduled Actions

The module includes sample schedulers that automate periodic tasks related to property management. Check the scheduler settings to ensure they meet your needs.
Contributing

If you wish to contribute to the development of this module, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any questions or suggestions, please contact the author at: tomiodecode@gmail.com
