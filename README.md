# Estate Module

**Version:** 1.0  
**Author:** TomioDeCode  
**Category:** App  
**Odoo Version:** 17.0

## Description

The Estate module is a feature-rich application designed for managing real estate properties, property types, offers, and tags within the Odoo 17 environment. This module serves as a learning exercise for understanding the basics of Odoo 17 module development. Below is a concise summary of its key components and usage:

## Features

1. **Estate Properties Management:** Create, update, and manage various estate properties with details such as name, description, location, and price.
2. **Property Types:** Define and categorize properties (e.g., apartment, house, villa).
3. **Property Offers:** Track and manage property offers, including accepting, refusing, and monitoring offer statuses.
4. **Property Tags:** Create tags for better property categorization and search functionality.
5. **Basic Workflows:** Implement simple workflows for managing property offers and statuses.
6. **Email Notifications:** Utilize simple email templates for notifications related to property events.
7. **Schedulers:** Set up automated tasks for property management.

## Installation Steps

1. **Clone the Module:**  
   Place the `estate` directory into your Odoo custom addons directory using the following command:
   ```bash
   git clone <repository-url> /path/to/odoo/custom/addons/estate

2. **Update Odoo Configuration:**
    Ensure your odoo.conf includes the path to your custom addons:

    plaintext
   
    ```bash
    addons_path = /path/to/odoo/addons,/path/to/odoo/custom/addons
3. **Install the Module**:
    Install the Module:
   
    ```bash
    Restart the Odoo server, navigate to the Apps menu, click on "Update Apps List," search for "Estate," and install it.

## Usage Instructions

    Properties: Create and manage properties by filling in necessary details.
    Property Types: Define and manage various property types through the designated menu.
    Property Offers: Handle offers, accept or refuse them, and track their status.
    Property Tags: Create and assign tags to properties for categorization.
    Email Notifications: Use sample templates for property-related notifications.

## Dependencies

    base
    mail

Ensure these dependencies are installed in your Odoo environment.
Security

## Security

The module includes a security file (ir.model.access.csv) to define user access rights. Review and adjust these settings as needed.
Scheduled Actions

## Scheduled Actions

The module features sample schedulers for automating tasks related to property management. Verify the scheduler settings align with your needs.
Contributing

## Contributing

To contribute, fork the repository and submit a pull request. For significant changes, initiate a discussion by opening an issue.
License

## License

The Estate module is licensed under the MIT License. Refer to the LICENSE file for detailed information.
Contact

## Contact

For queries or suggestions, reach out to the author at tomiodecode@gmail.com.
