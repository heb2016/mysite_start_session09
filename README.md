# mysite

As a class, this is where we'll start for Session 09.

To get this set up on your machine:

1. Fork and clone the repository
2. Open a command prompt and activate your djangoenv
3. Navigate to your mysite directory
4. Create a database using the model
`$ python manage.py migrate`
5. Create a super user - follow the instructions to finish creating super user
`$ python manage.py createsuperuser`
6. Start the server
`$ python manage.py runserver`
7. In your browser, open localhost:8000 to see the application


Read the documentation about the Django admin.

You’ll need to create a customized ModelAdmin class for the Post and Category models.

And you’ll need to create an InlineModelAdmin to represent Categories on the Post admin view.

Finally, you’ll need to exclude the ‘posts’ field from the form in your Category admin.

All told, those changes should not require more than about 15 total lines of code. The trick of course is reading and finding out which fifteen lines to write.

#Changes made since the end of Session 08:

*myblog/admin.py*

1. Created PostAdmin and CategoryAdmin classes
2. Added make_published function
3. Added CategorizationInline class
2. Registered Post and Category classes with their new Admin classes

*myblog/models.py*

1. Added a metaclass to Categories to make the name in the admin appears as "Categories" instead of "Categorys"
2. Added __unicode__ methods to both Post and Category classes
