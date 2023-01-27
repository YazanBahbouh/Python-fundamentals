# Assignment: Semi-Restful TV Shows (w/ Validations)
Now that we've got a basic understanding of the flow between models, views, and templates, let's make sure we know how to implement all 4 CRUD commands!

Remember that restful routing is simply a guideline of generally accepted routing naming conventions so other consumers of our routes can easily navigate our application and anticipate what the response will be for any given route. Since many web applications perform CRUD operations, you can imagine how confusing this could get if everyone followed different conventions for creating routing and method names for these operations.

Restful routing also gives us a chance to practice being methodical in our approach to building an application. For each step of CRUD, we start with the HTML, then build the routes to show that page. We can then build out the routes that will process any form submissions.

Ultimately, it's up to you (or maybe your boss) whether you also follow these rules/conventions, but we strongly encourage you to get familiar with the following rules for RESTful routing, as you may be making requests to, or someday creating your own, API.

Also, let's add validations to this Semi-Restful TV Shows assignment! Building off of the existing assignment, implement validations for form data entered to prevent dirty data from getting into your database. If a submission is invalid, display errors on the appropriate page.

    Objectives:

        • Practice ORM queries from the controller
        • Practice RESTful routing
        • Practice rendering query results to templates
        • Practice using form input to create table data
        • Practice validating data before entering it into the database
