# ID-Comparator

Online Payment is a must need feature today. It is essential for all the online payments institutions to complete the customers KYC(Know-Your-Customer) to validate any customer.
This requires the user to manually type all the important information. This project helps the user in validating itself.

This is a terminal based application that aims to compare data available in different Identity cards of a person. It also compares the images of that person in the ID cards.

The user just need to give its information and the identity proof. The application itself scapes the data from the ID Cards and compares it. It provides the user with a dataframe consisting of inconsistencies in the ID cards.

Apart from comparing the data in the ID cards, it also compared the images, if provided in the ID cards. This validates that both the ID cards belong to the user and helps the financial institutions with the validation of the customer.

Google vision API has been used for extraction the data from the images (Optical Character Recognition). Aldo FacePP API has been used for comparing the faces. The results have been accumulated in a dataframe showing the correct and incorrect entities.

This project is in development phase.
